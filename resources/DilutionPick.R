##########################
message("#################################################################################################################")
message("#DilutionPickR  v0.1")
message("#J Bisanz 1 Dec 2020")
message("#Picks appropriate dilution from primary PCR for AmpliconSeq Protocol")
message("#################################################################################################################")
message(" ")

##########################
#Get arguments
suppressMessages(library(optparse))
option_list = list(
  make_option(c("-c", "--csv"), type="character", help="Quantification Amplification Results_SYBR.csv exported from BioRad CFX384", metavar="character"),
  make_option(c("-t", "--tracking"), type="character", help="The 16S tracking sheet (an excel file downloaded from AmpliconSeq).", metavar="character"),
  make_option(c("-i", "--plateid"), type="numeric", default="1", help="Which plate are we looking at (to pull sample names)?", metavar="character"),
  make_option(c("-o", "--output"), type="character", default="WellsForIndexing.csv", help="A csv file which will contain the appropriate wells to pick", metavar="character"),
  make_option(c("-p", "--pdf"), type="character", default="PrimaryCurves.pdf", help="A set of ", metavar="character"),
  make_option(c("-r", "--rfu"), type="numeric", help="The max RFU used for picking (default=detected from samples using 3rd quartile)", metavar="numeric"),
  make_option(c("-f", "--fraction"), type="numeric", default="0.8", help="Pick the dilution closest to fraction x  RFU", metavar="numeric")
)


opt_parser = OptionParser(option_list=option_list)
opt = parse_args(opt_parser)

#opt$csv="/turnbaughlab/projects/Caloric Restriction/16S/primarypcr/CALORICRESTRICT-admin_2020-11-30 19-05-20_CT018087 -  Quantification Amplification Results_SYBR.csv"
#opt$tracking="/turnbaughlab/projects/Caloric Restriction/16S/16S_TrackingSheet.xlsx"
#opt$plateid="1"

if (is.null(opt$csv) | is.null(opt$tracking) | is.null(opt$plateid)){
  print_help(opt_parser)
  stop("Specify the ampification results (--csv), tracking sheet (--tracking), and plate ID (--plateid)", call.=FALSE)
}

message(date(), "---> Loading tidyverse and readxl")
suppressMessages(library(tidyverse))
suppressMessages(library(readxl))

suppressMessages(suppressWarnings(amps<-read_csv(opt$csv)))
suppressMessages(suppressWarnings(tracking<-read_excel(opt$tracking, col_names = FALSE)))

amps<-
  amps %>%
  select(-X1) %>%
  gather(-Cycle, key="Well", value="RFU")

line<-grep(paste0("Extraction and Indexing Plate ", opt$plateid, " of 6"), tracking[,1]$...1)

tracking<-tracking[(line+1):(line+9),]
colnames(tracking)<-c("Row", 1:12)
tracking<-
  tracking[-1,] %>%
  gather(-Row, key="Column", value="SampleID") %>%
  mutate(Column=as.numeric(Column))
  
tracking<-
  tracking %>%
  dplyr::select(SampleID, Row_96well=Row, Column_96well=Column)

tracking$Row_384well <- rep(seq(1,16,2),12)
tracking$Column_384well <- tracking$Column_96well

tracking<-
bind_rows(tracking %>% mutate(dilution=1),
      tracking %>% mutate(Row_384well=Row_384well+1, dilution=10),
      tracking %>% mutate(Column_384well=Column_384well+12, dilution=100),
      tracking %>% mutate(Row_384well=Row_384well+1,Column_384well=Column_384well+12, dilution=1000)
)

tracking<-tracking %>% mutate(Row_384well=LETTERS[Row_384well])

tracking<-tracking %>% 
  mutate(Well_96=paste0(Row_96well, Column_96well), Well_384=paste0(Row_384well, Column_384well)) %>%
  dplyr::select(SampleID, dilution, Well_96, Well_384)

amps<-
amps %>% dplyr::rename(Well_384=Well) %>% left_join(tracking) %>%
  filter(!grepl("^Empty", SampleID)) %>%
  dplyr::select(SampleID, dilution, Well_96, Well_384, Cycle, RFU)

if(is.null(opt$rfu)){opt$rfu<-amps %>% filter(dilution==1 & Cycle==max(amps$Cycle)) %>% pull(RFU) %>% median()}

picks<-
amps %>%
  filter(Cycle==max(amps$Cycle)) %>%
  group_by(SampleID) %>%
  filter(abs(RFU - (opt$rfu*opt$fraction)) == min(abs(RFU - opt$rfu*opt$fraction))) %>%
  select(SampleID, dilution, Well_96) %>%
  mutate(Status="Index")

amps<-
amps %>%
  left_join(picks) %>%
  mutate(Status=if_else(is.na(Status), "Discard","Index"))


pdf(gsub("\\.pdf",paste0("_Plate",opt$plateid,".pdf"), opt$pdf), height=8, width=10.5)
print(
  amps %>%
    filter(Status=="Index") %>%
    ggplot(aes(x=Cycle, y=RFU, group=SampleID)) +
    theme_bw() +
    geom_line() +
    ggtitle(paste0("Samples for Indexing: Plate ", opt$plateid))
)

print(
  amps %>% 
  select(Well_384, Status) %>% 
  mutate(row=gsub("[A-Z]", "", Well_384) %>% as.numeric()) %>%
  mutate(column=gsub("[0-9]", "", Well_384) %>% factor(., levels=rev(LETTERS[1:16]))) %>%
  ggplot(aes(x=row, y=column, fill=Status)) +
  geom_tile() +
  ggtitle(paste0("Wells to pick: Plate ", opt$plateid)) +
  theme_bw() +
  scale_x_continuous(breaks=1:24) +
  scale_fill_manual(values=c("grey50","indianred"))
)

for(samp in unique(amps$SampleID)){
    print(
    amps %>%
    filter(SampleID==samp) %>%
    ggplot(aes(x=Cycle, y=RFU, color=Status, group=dilution)) + 
    geom_line() +
    geom_hline(yintercept = opt$rfu, linetype="dashed", color="red") +
    theme_bw() +
    ggtitle(paste0("Plate:", opt$plateid," Well:", (amps %>% filter(SampleID==samp) %>% pull(Well_96) %>% .[1])," Sample:", samp))
    )
}
dev.off()

amps %>%
  filter(Cycle==max(amps$Cycle) & Status=="Index") %>%
  arrange(Well_96) %>%
  select(SampleID, dilution, gDNA_Well=Well_96, PrimaryPCR_Well=Well_384) %>%
  mutate(row=gsub("[A-Z]", "", gDNA_Well) %>% as.numeric()) %>%
  mutate(column=gsub("[0-9]", "", gDNA_Well)) %>%
  arrange(row) %>%
  arrange(column) %>%
  dplyr::select(-row, -column) %>%
  write_csv(gsub("\\.csv",paste0("_Plate",opt$plateid,".csv"),opt$output))
 
message("---------------------------> !!!Script is complete, please manually check over outputs!!!")
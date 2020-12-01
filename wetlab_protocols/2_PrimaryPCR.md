# Protocol 2- Primary PCR

## Theory
This protocol and the subsequent indexing steps were originally derived from a “Systematic improvement of amplicon marker gene methods for increased accuracy in microbiome studies” [doi:10.1038/nbt.3601](https://www.nature.com/articles/nbt.3601). The methods have been modified for our equipment and supplies, and the indexes have been switched to use dual error-correcting barcodes. **It is possible that portions of the original protocol have been copied verbatim in these protocols and the original manuscript should be cited for the method.**

To prevent against over-amplification, and thus massive amounts of reads lost to chimeras and other technical artifacts (>20%), the primary PCR is carried out as a quantitative PCR that provides real-time feed back on amplification. This gives information on if an amplicon has been formed and negates the needs to run any gels to check for amplication. The downside is that primer dimers that occur after cycle 25 may mask amplicons in low biomass samples. If studying low biomass samples (ex skin), 30 cycles of PCR should be run, and amplicons inspected by gel electrophoresis or similar method.

The goal of this protocol is to get mid-to-late amplification to carry forward for indexing. To get optimal amplification, a 10-fold dilution series is created and the optimal dilution is selected. In PCR, a 10-fold dilution corresponds to a delay of 3.3 cycles, thus 4x10-fold dilutions cover a range of ~13 cycles. PCR inhibition, which commonly happens with filter-based extractions, can be directly visualized here as 10-fold dilutions amplifying similarly (or better) than its undiluted stock. Remember there should be ~3 cycles between dilutions. Inhibition has not been seen with the Zymo approach, but has been seen with the Promega and Powersoil-based extractions. A direct cause of inhibition is carryover of ethanol containing wash buffer from column based approaches.

Another advantage of this amplification strategy is that you can mix and match 16S variable regions without ordering new indexes. A list of primers is attached below however it is reccomended to use V4_515Fmod_Nextera and V4_806Rmod_Nextera which are the revised EMP V4 primers. It is also possible to sequence multiple variable regions or combine 16S rRNA and ITS into a single run so long as the indexes do not overlap.

## Materials
- [ ] Opentrons OT-2 with 20ul multichannel.
- [ ] 1 x USA Scientific 12 Well Reservoir 22 mL (USA Scientific 1061-8150) 
- [ ] 2 x Opentrons filter 20ul tips (https://shop.opentrons.com/collections/opentrons-tips/products/opentrons-20ul-filter-tips)
- [ ] 384 Plates for qPCR (Biorad #HSP3865)
- [ ] [gDNA from Protocol 1](https://github.com/jbisanz/AmpliconSeq/blob/master/wetlab_protocols/1_DNAExtraction.md) in a 96 well plate (Biorad hsp9601)
- [ ] Optically clear Plate Seals (Biorad Microseal ‘B’ #MSB1001)
- [ ] DMSO for PCR (Sigma D8418-50mL)
- [ ] SYBR Green I (Sigma S9430 - 10,000x stock) - diluted 10x in DMSO to 1000x
- [ ] KAPA HiFi Hot Start PCR kit (KAPA KK2502) - **order your own. may need to order 2 depending on number of samples to cover indexing reactions**
- [ ] PCR primers of choice at 100µM (see Table 1)
- [ ] Nuclease-free H2O (Life Tech 0977-023)


## Protocol
***Location:** PCR hood or separate room/area from other steps*
- [ ] Treat PCR area with UV light for ~15 minutes.
- [ ] Generate enough PCR master mix for 420 rxns according to **Table 2** in the first column of a 12 well reservoir.
- [ ] Thaw gDNA plate on ice and briefly centrifuge to prevent cross contamination.
- [ ] Set up OT-2 according to **Figure 1** below.
- [ ] Download ot2_scripts/2_PrimaryPCR.py
- [ ] Upload 2_PrimaryPCR.py to OT-2 using Opentrons App.
- [ ] Calibrate all deck positions
- [ ] Run protocol. **Estimated time of completion: XXXXXXXX**
- [ ] After qPCR run is done, transfer plates to -20˚C if processing is going to be paused.

## QC
A successful amplification curve should had formed for all samples, and no curves should be observed for negative controls (**Figure 2**). Optionally, a 1% agarose gel can be used to spot check some amplifications. Note: undiluted samples will be found in every other row starting in columns A1:A12.

## Figures

![fig1](https://github.com/jbisanz/AmpliconSeq/blob/master/images/primaryPCRlayout.png)
**Figure 1**. OT-2 deck positions for primary PCR. **Position 1:** gDNA from Protocol 1 in skirted biorad 96 well plate. **Position 2:** 384 biorad qPCR plate. **Position 4 and 7:** 20ul filter tips. **Position 5:** Mastermix in the first column of 12-well reservoir. Left mount: p20 single channel. Right mount: p20 multichannel.

![fig2](https://github.com/jbisanz/AmpliconSeq/blob/master/images/ampcurves.png)
**Figure 2**. qPCR amplification curves for a single sample shows dilution series. The 10x or 100x dilutions are ideal for carrying forward. Note that the extraction blanks have not amplified. Amplification may be observed at 25 cycles of PCR due to primer dimers. See protocols for low biomass samples for more information and recommendations.

## Tables

**Table 1. Primers for primary PCR**
**Primer name** | **Marker gene** | **Target region** | **Sequence**
----------------|-----------------|-------------------|---------------
V4_515Fmod_Nextera | 16S rRNA | V4 | TCGTCGGCAGCGTCAGATGTGTATAAGAGACAGGTGYCAGCMGCCGCGGTAA
V4_806Rmod_Nextera | 16S rRNA | V4 | GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAGGGACTACNVGGGTWTCTAAT
V1_27F_Nextera | 16S rRNA | V1-V3 | TCGTCGGCAGCGTCAGATGTGTATAAGAGACAGAGAGTTTGATCMTGGCTCAG
V3_534R_Nextera | 16S rRNA | V1-V3 | GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAGATTACCGCGGCTGCTGG
V3_357F_Nextera | 16S rRNA | V3-V4, V3-V5 | TCGTCGGCAGCGTCAGATGTGTATAAGAGACAGCCTACGGGAGGCAGCAG
V4_515F_Nextera | 16S rRNA | V4, V4-V6 | TCGTCGGCAGCGTCAGATGTGTATAAGAGACAGGTGCCAGCMGCCGCGGTAA
V4_806R_Nextera | 16S rRNA | V3-V4, V4 | GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAGGGACTACHVGGGTWTCTAAT
V5F_Nextera  | 16S rRNA | V5-V6 | TCGTCGGCAGCGTCAGATGTGTATAAGAGACAGRGGATTAGATACCC
V5_926R_Nextera | 16S rRNA | V3-V5 | GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAGCCGTCAATTCMTTTRAGT
V6R_Nextera | 16S rRNA | V5-V6, V4-V6 | GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAGCGACRRCCATGCANCACCT
18S_V9_1391_F_Nextera | 18S rRNA | V9 | TCGTCGGCAGCGTCAGATGTGTATAAGAGACAGGTACACACCGCCCGTC
18S_V9_EukBr_R_Nextera | 18S rRNA | V9 | GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAGTGATCCTTCTGCAGGTTCACCTAC
ITS1F_Nextera | ITS | ITS1 | TCGTCGGCAGCGTCAGATGTGTATAAGAGACAGCTTGGTCATTTAGAGGAAG*TAA
ITS2_Nextera | ITS | ITS1 | GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAGGCTGCGTTCTTCATCGA*TGC
5.8SR_Nextera | ITS | ITS2 | TCGTCGGCAGCGTCAGATGTGTATAAGAGACAGTCGATGAAGAACGCAGCG
ITS4_Nextera | ITS | ITS2 | GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAGTCCTCCGCTTATTGATATGC

**Table 2. Primary PCR Master Mix**
Component	| 1 Rxn (µL) | 420 Rxns (µL) 
----------|------------|--------------
Nuclease-free H2O	| 5.2055 | 2186.31
5x KAPA HiFi Buffer	| 1.8	| 756
10 mM dNTPs	| 0.27 |	113.4
DMSO	| 0.45	| 189
1000x SYBR Green	| 0.0045	| 1.89
100 µM Forward Primer	| 0.045	| 18.9
100 µM Reverse Primer	| 0.045	| 18.9
KAPA HiFi polymerase	| 0.18	| 75.6
Template | 1.0 | 420
**Total**	| **9.0**	| **3780.0**

**Table 3. Primary PCR Amplification Parameters**
Cycle |	Temperature (˚C)  | Time
------|-------------------|------
Initial Denaturation   |	95	| 5 min
22 cycles\*:
Denature | 98˚C | 20 sec
Anneal | 55˚C	| 15 sec
Extend | 72˚C | 60 sec
Holding	| 4˚C	Hold | 0 sec

\**22 cycles is a good starting point here. With V4 primers, primer dimers will occur by cycle 25 and will make judging the success of amplification difficult.*


# Protocol 3: Cherry Picking and Indexing PCR


## Automated picking of dilution
Requirements: an installation of R, and the packages tidyverse, and optparse.
```
Rscript ~/GitHub/AmpliconSeq/resources/DilutionPick.R --csv "primarypcr/CALORICRESTRICT-admin_2020-11-30 19-05-20_CT018087 -  Quantification Amplification Results_SYBR.csv" --tracking 16S_TrackingSheet.xlsx --plateid 1
```

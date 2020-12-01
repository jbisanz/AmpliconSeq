# Protocol 3: Cherry Picking and Indexing PCR

## Theory

While the primary PCR has created the amplicons for sequencing, there is no identifying information on the DNA to tell the sample of origin. This is the purpose of the indexing PCR. In the emp protocol, a single index/barcode is incorporated onto the reverse (or forward depending on version) primer. Here there are two indices/barcodes on both sides of the amplicon. In this way, fewer barcodes can be used as samples are recognized as the combination of left and right barcodes. For example, in our current set up 24 forward, and 24 reverse give 576 combinations. The same amount of sequence capacity would require 576 distinct (and long, and expensive) reverse primers. There are currently 6 replicate sets of primer aliquots in the -20˚C. Please note your usage and date on the bag.

The first step of this protocol is to pick the appropriate dilution from the primary PCR. If using low biomass samples, this step should be skipped as dilutions were not performed. This can be performed automatically using a script included in resources called DilutionPick.R. It can be run as below to generate a table of the wells to be picked.

```
Rscript ~/GitHub/AmpliconSeq/resources/DilutionPick.R --csv "primarypcr/CALORICRESTRICT-admin_2020-11-30 19-05-20_CT018087 -  Quantification Amplification Results_SYBR.csv" --tracking 16S_TrackingSheet.xlsx --plateid 4
```

The resulting outputs include WellsForIndexing_PlateX.csv and PrimaryCurves_PlateX.pdf. The amplification curves show which dilution was selected for indexing based on trying to be closest to 0.7x the maximum (i.e. plateaued) signal as seen in Figure 1. The goal is to prevent over amplification. Note also from these plots what has happened with your negative controls, for example as seen in Figure 2.

The most important output is the WellsForIndexing.csv file which needs to be copy and pasted inside of 3_CherryPickandIndex_template.py.

# Materials
- [ ] 96 Well Plates (USA Sci #1402-9200)
- [ ] DMSO for PCR (Sigma D8418-50mL)
- [ ] KAPA HiFi PCR kit (KAPA KK2502) - **order your own**
- [ ] Indexing Primer plate (Pick 1 of 6 for each plate to be sequenced without overlapping).
- [ ] Nuclease-free H2O (Life Tech 0977-023)
- [ ] Opentrons OT-2 with gen2 20ul multichannel and 20ul single channel.
- [ ] 1 x USA Scientific 12 Well Reservoir 22 mL (USA Scientific 1061-8150) 
- [ ] 4 x Opentrons filter 20ul tips (https://shop.opentrons.com/collections/opentrons-tips/products/opentrons-20ul-filter-tips)
- [ ] Primary PCR amplicons in 384 Plate for qPCR (Biorad #HSP3865)
- [ ] 2x Bio-Rad 96 Well Plate 200 µL skirted PCR plate  (Biorad hsp9601)
- [ ] Optically clear Plate Seals (Biorad Microseal ‘B’ #MSB1001)


##### Table 4.2.1. Indexing PCR Master Mix (3.3x)

Component	| 1 Rxn (20µL rxn) | 110 Rxns
----------|------------------|----------
5x KAPA HiFi Buffer	| 4 | 440
10 mM dNTPs | 0.6 | 66
DMSO | 1.0 | 110
KAPA HiFi polymerase | 0.4 | 44
**Total**	| **6.0** | **660**

#### 4.3 Protocol
***Location:** Anywhere that is not the PCR hood or where final libraries are being prepared. Due to the limited number of cycles, the main risk of contamination here comes from other sequencing libraries.*
- [ ] Transfer 2 µL of non-plateaued reaction into a new 96 well plate containing 198 µL of H2O to create a 100-fold dilution of the primary PCR. Label this for long-term storage.
- [ ] In a new 96 well plate, add 6µL master mix to every well (Table 4.2.1).
- [ ] To each well, add 4µL of indexing primer from a stock plate being sure replicate the same layout. **SPIN INDEX PLATES BEFORE REMOVING SEAL.**
- [ ] Add 10 µL of 100-fold dilution plate being sure to replicate the same layout.
- [ ] Cover plate and briefly centrifuge.
- [ ] Complete amplification as per the protocol in Table 4.3.1.
- [ ] After amplification, use the Qubit (or Quantit kit) to spot check postive and negative controls. Negative controls should be <2ng/µL and positive controls should be >20ng/µL.

##### Table 4.3.1. Indexing Amplification Parameters
Cycle | Temperature (˚C)	| Time
------|-------------------|------
Initial | Denaturation	95 | 	5 min
10 cycles:
Denature | 98˚C | 20 sec
Anneal | 55˚C | 15 sec
Extend | 72˚C | 60 sec
Holding	| 4˚C	Hold | (0 sec)


## Automated picking of dilution
Requirements: an installation of R, and the packages tidyverse, and optparse.

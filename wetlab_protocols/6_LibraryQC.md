# Protocol 5 - Library QC

## Theory
While using the Nanodrop is convienient, it is not accurate for concentrations less than ~10-20ng/µL and lacks the sensitivity required. The QuBit/QuantiT uses a fluorescent dye to specifically quantify dsDNA and is generally much more sensitive and specific than the Nanodrop, and once upon a time was how people normalized sequencing libraries. The most up to date way is via qPCR. This is accomplished by using primers against the Illumina sequencing adapters so in effect, you are only quantifying the portion of DNA that can actually be sequenced for the most sensitive quantification. **Accurate quantification is key for getting the correct cluster density on the sequencer.** This step represents one of the most important steps in your library generation and will directly influence the read depth and quality of your sequencing run. Inaccuracy in this step could completely render your sequencing run useless. *Also while not explicitly required, it is not a bad idea to run a 2% gel and/or a HS DNA bioanalyzer chip to look at size distribution in the library and ensure that size selection is not necessary. If V4 amplicon used, band should be ~435 bp and be free of other bands. 

## Materials
- [ ] KAPA Library Quantification Kit for Illumina Platforms (KAPA KK4824) *Standards can be ordered separately as they are limiting reagent of kit (KAPA KK4903)*
- [ ] 384 Plates for qPCR (Biorad #HSP3865)
- [ ] Optically clear Plate Seals (Biorad Microseal ‘B’ #MSB1001)
- [ ] Dilution Buffer (10 mM Tris-HCl pH 8, 0.05% Tween, note can be prepared from Qiagen EB + Tween)

## Protocol
***Location:** lab bench.*
- [ ] If first time using kit, add the 10X primer premix to the KAPA SYBRFast qPCR Master Mix (2X)
- [ ] Using whatever layout you choose, 6µL to 30 wells of a 384 well plate  ((6 standards x 3 replicates) + (3 dilutions of library x 3 replicates) + 3 NTC))
- [ ] Transfer 4 µL of the 6 standards into triplicate wells.
- [ ] Create a CAREFULL dilution series of your library in Dilution Buffer with the following dilutions being sure to mix between:
	- [ ] 2 µL of library into 198 buffer (100x)
	- [ ]	2 µL of library into 198 buffer (10,000x)
	- [ ]	20 µL into 180 buffer (100,000x)
 	- [ ]	20 µL into 180 buffer (1,000,000x)
- [ ] Transfer 4 µL of the last 3 dilutions (1e4, 1e5, and 1e6 dilutions) in triplicate to appropriate wells of a 384 well plate.
- [ ] Seal plate with optically clear cover and centrifuge briefly.
- [ ] Amplify according to the parameters in Table 1 on the BioRad CFX384.
- [ ] After completion of the run, export the data. 
- [ ] From the Cq results: plate view, transfer appropriate values to the the excel spread sheet (TrackingSheet.xlsx) into the highlighted boxes in the LibraryNorm tab. Use the average fragment length appropriate to your amplicon (435 for V4).
- [ ] To be successful, the amplification efficiency should be 90-110% and the R2 value should be greater than 0.99. *Sanity check: Your QuBit/Nanodrop calculations should be in the same ballpark as the qPCR result. If these are extremely different something has gone wrong. Requantify and run bioanalyzer chip to ensure proper library size distribution.*
- [ ] Record the concentration of the undiluted library in nM for going forward.

# Tables
**Table 1 Library Quantification qPCR**
Cycle	| Temperature (˚C) | Time
------|------------------|------
Initial Denaturation | 95 | 5 min
35 cycles:	
Denature | 95 | 30 sec
Anneal/Extend | 60 | 45 sec
Melt Curve | 65->95 | NA

# Protocol 1 - HTP DNA Extraction

## Theory
Ideally we want a high-throughput extraction method that is scalable and would allow for direct sequencing and qPCR analysis that has internal controls to ensure accuracy and reproducibility of microbial profiles. After testing a number of protocols, we have been using the ZymoBIOMICS magnetic capture protocol which is scalable and can be partially automated. While yeilds from fecal are on the low side ~10ng/ul, sequencing of controls shows even lysis and it is possible to recover extremely low concentrations of bacteria in low biomass samples. **To facilitate downstream analysis, a template is provided in resources/TrackingSheet.xlsx. Use this file to layout your DNA extractions.** Ideally each plate should include at least 2 negative controls (just extracting water) and a positive control (ex. zymo community standard). Randomly layout negative and positive controls on plate and avoid laying out samples both within and between plates following experimental variables. For example: do not put all disease samples on one plate, and controls on another as this could introduce a false signal due to batch effects. Note, either lysing plates/strips or individual tubes can be used (see ordering information below); however, individual tubes are recommended if cross contamination is unacceptable in study design. The Biospec Mini-beadbeater-96 can lyse 48 samples at a time. Yield is sufficient for amplicon or Nextera-style metagenomic libraries as desired.

*Note: Before starting, ensure you have all reagents. Non-communical reagents are indicated below.*

## Materials
- [ ] ZymoBIOMICS 96 MagBead DNA Kit (D4308)
- [ ] ZymoBIOMICS Community Standard (Zymo D6300) 
- [ ] VWR Deep Well Plate (75870-796)
- [ ] Magnetic Capture Stand (Zymo ZR-96)
- [ ] Bio-Rad 96 Well Plate 200 µL skirted PCR plate  (Biorad hsp9601) 
- [ ] 1000µL tips (USA scientific 1122-1730)
- [ ] Fast Prep 96 Or Equivalent (MPBio)
- [ ] Eppendor Research Plus 8 channel (USA Scientific 4031-5206)
- [ ] Analytical Scale (if sample weights are desired).


## Protocol
*Location: Biological safety cabinet acceptable for BSL2 work should be used. Remember that samples, especially those from humans could contain a wide variety of pathogens and should be treated with universal caution. After extraction, all pathogens will have been deactivated and samples instead need to be protected from outside contamination*
- [ ] Treat extraction area with UV ~15 minutes and/or 0.5% bleach.
- [ ] Weigh Empty Lysing Tube and tare scale (if using solid samples)
- [ ] Transfer ~50 mg feces, or ~half mouse fecal pellet, or 200µL liquid sample into lysing tube.
- [ ] Record weight of tube in Tracking_Sheet.xlsx
- [ ] Add 750 µL ZymoBIOMICS lysis solution to lysing tube (650 µL if using lysing rack).
- [ ] Disrupt for 1 minutes in FastPrep 96
- [ ] Wait 5 minutes
- [ ] repeat previous 2 steps for a total of 5 minutes bead beating.
- [ ] Centrifuge 5 minutes at ~10,000 x g
- [ ] Transfer 200 µL supernatant to 2 mL deep-well plate (BindingPlate).
- [ ] Add 600 µl MagBinding Buffer
- [ ] Add 25 µL MagBinding Beads and mix by pipette
- [ ] Transfer to magnetic stand and wait for supernatant to clear, discard supernatant
- [ ] Add 500 µL MagBinding Buffer and mix by pipette
- [ ] Transfer to magnetic stand and wait for supernatant to clear, discard supernatant
- [ ] Add 500 µL MagWash 1 and mix by pipette
- [ ] Transfer to magnetic stand and wait for supernatant to clear, discard supernatant
- [ ] Add 900 µL MagWash 2 and mix by pipette
- [ ] Transfer to magnetic stand and wait for supernatant to clear, discard supernatant
- [ ] Add 900 µL MagWash 2 and mix by pipette
- [ ] Transfer to magnetic stand and wait for supernatant to clear, discard supernatant
- [ ] Add 900 µL MagWash 2 and mix by pipette
- [ ] Transfer to magnetic stand and wait for supernatant to clear, discard supernatant
- [ ] Air Dry 30 minutes (or 10 minutes on 55˚C heating element)
- [ ] Add 50 µL DNase/RNase Free Water
- [ ] Capture beads on magnetic stand
- [ ] Transfer supernatant containing DNA to a new full skirted 96 well plate.
- [ ] Store plate at <= -20˚C or proceed to 1˚ amplification.

## QC
Spot check samples and negative controls using Nanodrop and/or Qubit. Successful (high biomass) samples should be >10ng/µL with a 260/280>1.6 and 260/230>1.4.  If the 260/230 is <1.4, Nanodrop quantification is not accurate and Qubit should be used instead. **Yield is not an indicator of evenness of extraction.** 


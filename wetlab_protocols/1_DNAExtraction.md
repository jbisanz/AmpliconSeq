# Protocol 1 - HTP DNA Extraction

## Theory
Ideally we want a high-throughput extraction method that is scalable and would allow for direct sequencing and qPCR analysis that has internal controls to ensure accuracy and reproducibility of microbial profiles. After testing a number of protocols, we have been using the ZymoBIOMICS magnetic capture protocol which is scalable and can be partially automated. While yeilds from fecal are on the low side ~10ng/ul, sequencing of controls shows even lysis and it is possible to recover extremely low concentrations of bacteria in low biomass samples. **To facilitate downstream analysis, a template is provided in resources/TrackingSheet.xlsx. Use this file to layout your DNA extractions.** Ideally each plate should include at least 2 negative controls (just extracting water) and a positive control (ex. zymo community standard). Randomly layout negative and positive controls on plate and avoid laying out samples both within and between plates following experimental variables. For example: do not put all disease samples on one plate, and controls on another as this could introduce a false signal due to batch effects. Note, either lysing plates/strips or individual tubes can be used (see ordering information below); however, individual tubes are recommended if cross contamination is unacceptable in study design. The Biospec Mini-beadbeater-96 can lyse 48 samples at a time. Yield is sufficient for amplicon or Nextera-style metagenomic libraries as desired.

*Note: Before starting, ensure you have all reagents. Non-communical reagents are indicated below.*

## Materials
- [ ] ZymoBIOMICS 96 MagBead DNA Kit (Zymo D4302 OR D4308) - **order your own**
- [ ] ZymoBIOMICS Community Standard (Zymo D6300) 
- [ ] USA Scientific 96 Deep Well Plate 2.4 mL (USA Scientific 1896-2000) 
- [ ] Bio-Rad 96 Well Plate 200 µL skirted PCR plate  (Biorad hsp9601) 
- [ ] Beta Mercaptoethanol (BioRad 1610710) 
- [ ] 1000µL tips (USA scientific 1122-1730)
- [ ] Biospec Mini-Beadbeater-96 or similar*
- [ ] Opentrons OT-2 with gen 2 Magnetic module, 1000ul single channel, and 300ul multichannel.
- [ ] 3 x Agilent 1 well 290 mL reservoirs (Agilent 201252-100)
- [ ] 1 x USA Scientific 12 Well Reservoir 22 mL (USA Scientific 1061-8150) 
- [ ] 1 x Opentrons filter 200ul tips (https://shop.opentrons.com/collections/opentrons-tips/products/opentrons-200ul-filter-tips)
- [ ] 4 x Opentrons filter 1000ul tips (https://shop.opentrons.com/collections/opentrons-tips/products/opentrons-1000ul-filter-tips)
<br>*Note: plates will not fit in tissuelyzer or MoBio options!*

## Protocol
*Location: Biological safety cabinet acceptable for BSL2 work should be used. Remember that samples, especially those from humans could contain a wide variety of pathogens and should be treated with universal caution. After extraction, all pathogens will have been deactivated and samples instead need to be protected from outside contamination*
- [ ] Treat extraction area with UV ~15 minutes or 0.5% bleach.
- [ ] Add 750 µL beta-mercaptoethanol to 150mL bottle of MagBinding Buffer  *(0.5% (v/v) i.e., 500 µl per 100 ml)*
- [ ] Transfer ~50 mg or half fecal pellet, or 200µL liquid sample into lysing tube or plate.
- [ ] Add 650 µL ZymoBIOMICS lysis solution if using lysing rack, add 750 µL if using individual tubes.
- [ ] Disrupt for 5 minutes in Biospec beadbeater (be sure that it is completely tightened and put a folded up large kimwipe under the lid to keep pressure on the strip lids if using strips)
- [ ] Wait 5 minutes
- [ ] repeat previous 2 steps 3 more times for a total of 20 minutes in minispec
- [ ] Incubate at 65˚C for 10 min (optional for Gram +ve organisms or human samples, akin to EMP protocol).
- [ ] Centrifuge 5 minutes at ~3000g.
- [ ] Transfer 200 µL supernatant to 2 mL deep-well plate (BindingPlate).
<br>*Note: optional stoping point before carrying on to automated cleanup
- [ ] Step up OT-2 according to **Figure 1**.
- [ ] Download ot2_scripts/1_ZymoMagWash.py and load into opentrons app. If not extracting entire plate, adjust line 18 (wells_to_extract).
- [ ] Calibrate all deck positions
- [ ] Run protocol. **Expected Run Time = XXXXXXXXXXXXX min**
- [ ] Take gDNA forward for primary PCR

## QC
Spot check samples and negative controls using Nanodrop and/or Qubit. Successful (high biomass) samples should be >5ng/µL with a 260/280>1.6 and 260/230>1.4.  If the 260/230 is <1.4, Nanodrop quantification is not accurate and Qubit should be used instead. **Yield is not an indicator of evenness of extraction.**


![Fig1](../images/zymolayout.png?)
<br>**Figure 1.** OT-2 deck layout. Deck positions are sequentially numbered 1-11 from the bottom left to the top right. **Position 1 (BINDINGPLATE)***: 200ul supernatant in deep well plate ontop of magnetic binding module. ***Position 2 (OTHERS)***: 12 well reservoir, first column contains 5.5 mL magbeads, second column contains 10 mL H2O, third column contains 15 mL H2O. **Position 3 (ELUTIONPLATE)**: Empty 96 well biorad PCR plate to collect final DNA. **Positions 4-6**: contain 132 mL binding buffer, 110 mL Magwash 1, and 210mL Magwash 2 respectively. **Positions 7-9, 11**: 1000ul tips. **Position 10**: 200ul tips.


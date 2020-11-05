### 3. Primary PCR
#### 3.1. Theory
To prevent against over-amplification, the primary PCR is carried out as a quantitative PCR that provides real-time feed back on amplification. The goal is to get mid-to-late amplification to carry forward for indexing. To get optimal amplification, a 10-fold dilution series is created and the optimal dilution is selected. In PCR, a 10-fold dilution corresponds to a delay of 3.3 cycles, thus 4x10-fold dilutions cover a range of ~13 cycles. In practice, for mouse samples extracted with the above approach, 10-fold dilutions seems to captured nicely at 20 cycles of PCR with lower density samples (such as pure culture gavages) being captured at the 1X concentration. For these types I would recommend running only two dilutions. For more complex or mixed samples types, It is recommended to do a full 4x10-fold dilutions. PCR inhibition can be directly visualized here as 10-fold dilutions amplifying similarly (or better) than its undiluted stock. Remember there should be ~3 cycles between dilutions. Inhibition has not been seen with the Zymo approach, but has been seen with the Promega based extraction. A direct cause of inhibition is carryover of ethanol containing wash buffer from column based approaches.

#### 3.2. Materials
- [ ] 384 Plates for qPCR (Biorad #HSP3865)
- [ ] 96 Well Plates (USA Sci #1402-9200)
- [ ] Optically clear Plate Seals (Biorad Microseal ‘B’ #MSB1001)
- [ ] DMSO for PCR (Sigma D8418-50mL)
- [ ] SYBR Green I (Sigma S9430 - 10,000x stock) - diluted 10x in DMSO to 1000x
- [ ] KAPA HiFi Hot Start PCR kit (KAPA KK2502) - **order your own. Have a set for primary PCR (different from indexing PCR, see below)**
- [ ] Amplification primers of choice at 100µM (see Table 8.1)
- [ ] Nuclease-free H2O (Life Tech 0977-023)

##### Table 3.2.1. Primary PCR Master Mix

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

#### 3.3 Protocol
***Location:** PCR hood or separate room/area from other steps*
- [ ] Treat PCR area with UV light for ~15 minutes.
- [ ] Add 8µL of PCR master mix (prepared as per Table 3.2.1) to all wells of a 384 well plate.
- [ ] Divide 384 plate into 4 quadrants and add 1 µL of template DNA to the first quadrant replicating the plate. This layout is at your discretion.
- [ ] Carry out 3x 10-fold dilutions of each sample into the next 3 quadrants by transferring 1 µL with a multichannel being sure to leave at least 1 no template control. Perhaps by not adding control in the most dilute reaction.
- [ ] Cover plate and briefly centrifuge.
- [ ] Amplify using the BioRad CFX384 according to the parameters of Table 3.3.1.

##### Table 3.3.1. Primary PCR Amplification Parameters
Cycle |	Temperature (˚C)  | Time
------|-------------------|------
Initial Denaturation   |	95	| 5 min
20 cycles:
Denature | 98˚C | 20 sec
Anneal | 55˚C	| 15 sec
Extend | 72˚C | 60 sec
Holding	| 4˚C	Hold | 0 sec

\**20 cycles is a good starting point here. With V4 primers, primer dimers will occur by cycle 25 and will make success of amplification difficult.*

##### Table 8.1 Primers for primary PCR
**Primer name** | **Marker gene** | **Target region** | **Sequence**
----------------|-----------------|-------------------|---------------
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

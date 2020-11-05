from opentrons import protocol_api
import csv

# metadata
metadata = {
	'protocolName': 'Cherrypick and index', 
	'author': 'J Bisanz, jordan.bisanz@gmail.com',
	'description': 'Cherry picking of appropriate dilution from primary PCR, 100x dilution, and setup of indexing PCR reaction',
	'apiLevel': '2.7'
}


# The data below is taken from a CSV wherein the first column defines the well of a sample from the original DNA extraction layout and the second column is the appropriate dilution from the 384 well primary pcr.
# Lines 17-112 are to be replaced with the users data
loadings = '''
indexing_well,primarypcr_well
A1,B1
B1,D1
C1,F1
D1,H1
E1,J1
F1,L1
G1,M1
H1,P1
A2,A2
B2,C2
C2,E2
D2,G2
E2,I2
F2,K2
G2,M2
H2,O2
A3,B3
B3,D3
C3,F3
D3,H3
E3,J3
F3,L3
G3,N3
H3,P3
A4,B4
B4,D4
C4,F4
D4,H4
E4,J4
F4,L4
G4,N4
H4,P4
A5,A5
B5,C5
C5,E5
D5,H5
E5,J5
F5,L5
G5,M5
H5,P5
A6,A6
B6,C6
C6,E6
D6,G6
E6,I6
F6,K6
G6,M6
H6,O6
A7,B7
B7,D7
C7,E7
D7,H7
E7,I7
F7,K7
G7,M7
H7,O7
A8,B8
B8,D8
C8,E8
D8,G8
E8,I8
F8,K8
G8,N8
H8,P8
A9,B9
B9,D9
C9,F9
D9,H9
E9,J9
F9,L9
G9,N9
H9,O9
A10,B10
B10,C10
C10,F10
D10,H10
E10,J10
F10,K10
G10,N10
H10,O10
A11,A11
B11,C11
C11,E11
D11,G11
E11,J11
F11,K11
G11,M11
H11,O11
A12,A12
B12,C12
C12,E12
D12,H12
E12,I12
F12,K12
G12,M12
H12,O12
'''

def run(protocol: protocol_api.ProtocolContext):

	# define labware and locations
	tips1 = protocol.load_labware('opentrons_96_filtertiprack_20ul', '1') # 20ul filter tips on deck position 1
	tips4 = protocol.load_labware('opentrons_96_filtertiprack_20ul', '4') # 20ul filter tips on deck position 4
	tips7 = protocol.load_labware('opentrons_96_filtertiprack_20ul', '7') # 20ul filter tips on deck position 7
	tips10 = protocol.load_labware('opentrons_96_filtertiprack_20ul', '10') # 20ul filter tips on deck position 10
	indexpcr = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '2') # plate to conduct indexing pcr in
	indexplate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '3') # skirted 96 well plate containing arrayed indexes
	primarypcr = protocol.load_labware('biorad384pcrplate_384_wellplate_40ul', '5') # skirted 384 well plate of amplicons
	dilutionplate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '6') # a plate to carryout 100x dilutions. NOTE: this plate already has 150µL of water in each well!!!!!
	reservoir = protocol.load_labware('usascientific_12_reservoir_22ml', '8') # reservoir with indexing mastermix (660ul) in A1 (First column)

	# define pipettes
	left_pipette = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tips1, tips4, tips7, tips10])
	right_pipette = protocol.load_instrument('p20_multi_gen2', 'right', tip_racks=[tips1, tips4, tips7, tips10])
	
	# transfer 1.5µL from the cherry picked wells defined in loadings to the corresponding point on the dilution plate and mix
	loadings_parsed = loadings.splitlines()[1:] # Discard the blank first line.
	for load in csv.DictReader(loadings_parsed):
		left_pipette.pick_up_tip()
		left_pipette.aspirate(1.5, primarypcr[load['primarypcr_well']])
		left_pipette.dispense(1.5, dilutionplate[load['indexing_well']])
		left_pipette.mix(10, 15, dilutionplate[load['indexing_well']]) # mix 10x by pipetting up and down 15ul
		left_pipette.drop_tip()	 


	# load the master mix into the indexing plate. NOTE: when using multichannel, only reference the top well... IE A1 to get entire column of B1, C1 ... 
	right_pipette.pick_up_tip() # only using a single set of tips to load mastermix as is same in every well.
	#Oh python... when you want a range from 1:12 you have to say 1:13 as it doesn't give the last number
	for i in range(1, 13): 
		right_pipette.aspirate(6, reservoir['A1'])
		right_pipette.dispense(6, indexpcr['A'+str(i)])
	right_pipette.drop_tip() 

	
	# load the indexes
	for i in range(1, 13): 
		right_pipette.pick_up_tip()
		right_pipette.aspirate(4, indexplate['A'+str(i)])
		right_pipette.dispense(4, indexpcr['A'+str(i)])
		right_pipette.drop_tip() 
	
	# add the templates
	for i in range(1, 13): 
		right_pipette.pick_up_tip()
		right_pipette.aspirate(10, dilutionplate['A'+str(i)])
		right_pipette.dispense(10, indexpcr['A'+str(i)])
		right_pipette.drop_tip() 

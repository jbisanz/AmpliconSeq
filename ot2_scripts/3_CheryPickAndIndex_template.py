from opentrons import protocol_api
import csv

# metadata
metadata = {
	'protocolName': 'Cherrypick and index', 
	'author': 'J Bisanz, jordan.bisanz@gmail.com',
	'description': 'Cherry picking of appropriate dilution from primary PCR, 100x dilution, and setup of indexing PCR reaction',
	'apiLevel': '2.7'
}


# The data below is taken from a CSV wherein the first column defines the well of a sample from the original DNA extraction layout, the second column is the appropriate dilution from the 384 well primary pcr, and the third column is the well to grab.
# Lines 17-112 are to be replaced with the users data
loadings = '''
extraction_well,dilution_factor,primarypcr_well
A1,1,A1
B1,1,C1
C1,1,E1
D1,1,G1
E1,1,I1
F1,1,K1
G1,1,M1
H1,1,O1
A2,1,A2
B2,1,C2
C2,1,E2
D2,1,G2
E2,1,I2
F2,1,K2
G2,1,M2
H2,1,O2
A3,1,A3
B3,1,C3
C3,1,E3
D3,1,G3
E3,1,I3
F3,1,K3
G3,1,M3
H3,1,O3
A4,1,A4
B4,1,C4
C4,1,E4
D4,1,G4
E4,1,I4
F4,1,K4
G4,1,M4
H4,1,O4
A5,1,A5
B5,1,C5
C5,1,E5
D5,1,G5
E5,1,I5
F5,1,K5
G5,1,M5
H5,1,O5
A6,1,A6
B6,1,C6
C6,1,E6
D6,1,G6
E6,1,I6
F6,1,K6
G6,1,M6
H6,1,O6
A7,1,A7
B7,1,C7
C7,1,E7
D7,1,G7
E7,1,I7
F7,1,K7
G7,1,M7
H7,1,O7
A8,1,A8
B8,1,C8
C8,1,E8
D8,1,G8
E8,1,I8
F8,1,K8
G8,1,M8
H8,1,O8
A9,1,A9
B9,1,C9
C9,1,E9
D9,1,G9
E9,1,I9
F9,1,K9
G9,1,M9
H9,1,O9
A10,1,A10
B10,1,C10
C10,1,E10
D10,1,G10
E10,1,I10
F10,1,K10
G10,1,M10
H10,1,O10
A11,1,A11
B11,1,C11
C11,1,E11
D11,1,G11
E11,1,I11
F11,1,K11
G11,1,M11
H11,1,O11
A12,1,A12
B12,1,C12
C12,1,E12
D12,1,G12
E12,1,I12
F12,1,K12
G12,1,M12
H12,1,O12
'''

# Use the lines below to bypass steps (False to bypass)
loadwater = True
cherrypick = True
loadmastermix = True
loadindex = True
loadtemplate = True

def run(protocol: protocol_api.ProtocolContext):

	# define labware and locations
	tips1 = protocol.load_labware('opentrons_96_filtertiprack_20ul', '1') # 20ul filter tips on deck position 1
	tips4 = protocol.load_labware('opentrons_96_filtertiprack_20ul', '4') # 20ul filter tips on deck position 4
	tips7 = protocol.load_labware('opentrons_96_filtertiprack_20ul', '7') # 20ul filter tips on deck position 7
	tips10 = protocol.load_labware('opentrons_96_filtertiprack_20ul', '10') # 20ul filter tips on deck position 10
	tips11 = protocol.load_labware('opentrons_96_filtertiprack_20ul', '11') # 20ul filter tips on deck position 11
	indexpcr = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '2') # plate to conduct indexing pcr in
	indexplate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '3') # skirted 96 well plate containing arrayed indexes
	primarypcr = protocol.load_labware('biorad384pcrplate_384_wellplate_40ul', '6') # skirted 384 well plate of amplicons
	dilutionplate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '5') # a plate to carryout 100x dilutions.
	reservoir = protocol.load_labware('usascientific_12_reservoir_22ml', '8') # reservoir with indexing mastermix (660ul) in A1 (First column) and Water (5 mL)

	# define pipettes
	left_pipette = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tips1, tips4, tips7, tips10, tips11])
	right_pipette = protocol.load_instrument('p20_multi_gen2', 'right', tip_racks=[tips1, tips4, tips7, tips10, tips11])
		
	#load water into the dilution plate for a 100x dilution
	if loadwater:
		right_pipette.pick_up_tip() #use single set of tips
		for i in range(1, 13): 
			for p in range(1, 5):
				right_pipette.aspirate(20, reservoir['A2'])
				right_pipette.dispense(20, indexpcr['A'+str(i)])
		right_pipette.drop_tip() 
	
	# transfer 1µL from the cherry picked wells defined in loadings to the corresponding point on the dilution plate
	if cherrypick:
		loadings_parsed = loadings.splitlines()[1:] # Discard the blank first line.
		for load in csv.DictReader(loadings_parsed):
			left_pipette.pick_up_tip()
			left_pipette.aspirate(1, primarypcr[load['primarypcr_well']])
			left_pipette.dispense(1, dilutionplate[load['extraction_well']])
			left_pipette.drop_tip()	 
	

	# load the master mix into the indexing plate.
	if loadmastermix:
		right_pipette.pick_up_tip() # only using a single set of tips to load mastermix as is same in every well.
		for i in range(1, 13): 
			right_pipette.aspirate(6, reservoir['A1'])
			right_pipette.dispense(6, indexpcr['A'+str(i)])
		right_pipette.drop_tip() 
	
	# load the indexes
	if loadindex:
		for i in range(1, 13): 
			right_pipette.pick_up_tip()
			right_pipette.aspirate(4, indexplate['A'+str(i)])
			right_pipette.dispense(4, indexpcr['A'+str(i)])
			right_pipette.drop_tip() 
	
	# add the templates
	if loadtemplate:
		for i in range(1, 13): 
			right_pipette.pick_up_tip()
			right_pipette.mix(5, 20, dilutionplate['A'+str(i)]) # mix 5x by pipetting up and down 20ul
			right_pipette.aspirate(10, dilutionplate['A'+str(i)])
			right_pipette.dispense(10, indexpcr['A'+str(i)])
			right_pipette.drop_tip() 

from opentrons import protocol_api
import csv

# metadata
metadata = {
	'protocolName': 'Cherrypick and index', 
	'author': 'J Bisanz, jordan.bisanz@gmail.com',
	'description': 'Cherry picking of appropriate dilution from primary PCR, 100x dilution, and setup of indexing PCR reaction',
	'apiLevel': '2.7'
}


# The data below is taken from a CSV wherein the first column defines the Sample name, second the dilution to be indexed, the third the original well position, and 4 the well in the 384 well primary pcr
# This can be generated using DilutionPick.R
# Lines 17-112 are to be replaced with the users data
loadings = '''
SampleID,dilution,gDNA_Well,PrimaryPCR_Well
crp1_daym3,100,A1,A13
crp2_daym3,10,A2,B2
crp3_daym3,10,A3,B3
crp4_daym3,10,A4,B4
crp5_daym3,1,A5,A5
crp6_daym3,10,A6,B6
crp7_daym3,10,A7,B7
crp8_daym3,100,A8,A20
crp9_daym3,1,A9,A9
crp10_daym3,10,A10,B10
crp11_daym3,10,A11,B11
crp12_daym3,10,A12,B12
crp1_daym2,1,B1,C1
extraction_blank1,1,B2,C2
crp2_daym2,1,B3,C3
crp3_daym2,10,B4,D4
crp4_daym2,1,B5,C5
crp5_daym2,1,B6,C6
crp6_daym2,10,B7,D7
crp7_daym2,100,B8,C20
crp8_daym2,1,B9,C9
crp9_daym2,1,B10,C10
crp10_daym2,10,B11,D11
crp11_daym2,10,B12,D12
crp12_daym2,100,C1,E13
crp1_daym1,10,C2,F2
crp2_daym1,10,C3,F3
crp3_daym1,1,C4,E4
crp4_daym1,100,C5,E17
crp5_daym1,1,C6,E6
crp6_daym1,1,C7,E7
crp7_daym1,1000,C8,F20
crp8_daym1,10,C9,F9
crp9_daym1,1,C10,E10
crp10_daym1,10,C11,F11
crp11_daym1,1,C12,E12
crp12_daym1,100,D1,G13
crp1_day0,10,D2,H2
crp2_day0,10,D3,H3
extraction_std,1,D4,G4
crp3_day0,1,D5,G5
crp4_day0,1,D6,G6
crp5_day0,100,D7,G19
crp6_day0,100,D8,G20
crp7_day0,1000,D9,H21
crp8_day0,1,D10,G10
crp9_day0,1,D11,G11
crp10_day0,1,D12,G12
crp11_day0,10,E1,J1
crp12_day0,1,E2,I2
crp1_day1,10,E3,J3
crp2_day1,1,E4,I4
crp3_day1,10,E5,J5
crp4_day1,1,E6,I6
crp5_day1,1,E7,I7
crp6_day1,1,E8,I8
crp7_day1,10,E9,J9
crp8_day1,1,E10,I10
NTC,1,E11,I11
crp9_day1,1,E12,I12
crp10_day1cecum,10,F1,L1
crp11_day1cecum,1,F2,K2
crp12_day1cecum,1,F3,K3
crp1_day2,1,F4,K4
crp2_day2,10,F5,L5
crp3_day2,1000,F6,L18
crp4_day2,1,F7,K7
crp5_day2,1,F8,K8
crp6_day2,10,F9,L9
crp7_day2,1,F10,K10
crp8_day2,1,F11,K11
crp9_day2,1,F12,K12
crp1_day3,10,G1,N1
hm3_std,1,G2,M2
crp2_day3,1,G3,M3
crp3_day3,1,G4,M4
crp4_day3,10,G5,N5
crp5_day3,100,G6,M18
crp6_day3,10,G7,N7
crp7_day3,1,G8,M8
crp8_day3,10,G9,N9
crp9_day3,1,G10,M10
crp1_day4,10,G11,N11
crp2_day4,1,G12,M12
crp3_day4,10,H1,P1
crp4_day4,10,H2,P2
crp5_day4,10,H3,P3
crp6_day4,1,H4,O4
crp7_day4,1,H5,O5
crp8_day4,10,H6,P6
crp9_day4,1,H7,O7
pcrstd_ZRC1957009,1,H8,O8
extraction_blank3,1,H9,O9
extraction_blank4,1,H10,O10
extraction_blank5,1,H11,O11
extraction_blank6,1,H12,O12
'''

# Use the lines below to bypass steps (False to bypass)
loadwater = False
cherrypick = True
loadmastermix = False
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
	if loadwater or loadmastermix: reservoir = protocol.load_labware('usascientific_12_reservoir_22ml', '8') # reservoir with indexing mastermix (660ul) in A1 (First column) and Water (5 mL)

	# define pipettes
	left_pipette = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tips1, tips4, tips7, tips10, tips11])
	right_pipette = protocol.load_instrument('p20_multi_gen2', 'right', tip_racks=[tips1, tips4, tips7, tips10, tips11])
		
	#load water into the dilution plate for a 100x dilution
	if loadwater:
		right_pipette.pick_up_tip() #use single set of tips
		for i in range(1, 13): 
			for p in range(1, 5): # do 5 times for 100ul total
				right_pipette.aspirate(20, reservoir['A2'])
				right_pipette.dispense(20, indexpcr['A'+str(i)])
		right_pipette.drop_tip() 
	
	# transfer 1µL from the cherry picked wells defined in loadings to the corresponding point on the dilution plate
	if cherrypick:
		loadings_parsed = loadings.splitlines()[1:] # Discard the blank first line.
		for load in csv.DictReader(loadings_parsed):
			left_pipette.pick_up_tip()
			left_pipette.aspirate(1, primarypcr[load['PrimaryPCR_Well']])
			left_pipette.dispense(1, dilutionplate[load['gDNA_Well']])
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
			right_pipette.mix(3, 20, dilutionplate['A'+str(i)]) # mix 5x by pipetting up and down 20ul
			right_pipette.aspirate(10, dilutionplate['A'+str(i)])
			right_pipette.dispense(10, indexpcr['A'+str(i)])
			right_pipette.drop_tip() 

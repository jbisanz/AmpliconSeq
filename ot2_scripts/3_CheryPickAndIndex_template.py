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
Zymo_MGSBatch2_plate2,1,A1,A1
LOGICS_8350110,10,A2,B2
LOGICS_8350016,10,A3,B3
LOGICS_8350003,1,A4,A4
LOGICS_8350054,1,A5,A5
LOGICS_8350015,1000,B1,D13
LOGICS_8350194,100,B2,C14
LOGICS_8350154,100,B3,C15
LOGICS_8350170,10,B4,D4
LOGICS_8350052,1,B5,C5
LOGICS_8350064,1,C1,E1
LOGICS_8350068,1000,C2,F14
Assembly_negative2_plate2,1,C3,E3
LOGICS_8350038,1,C4,E4
LOGICS_8350005,100,C5,E17
Blank2_MGSBatch3_plate2,1,D1,G1
LOGICS_8350089,1000,D2,H14
LOGICS_8350069,1,D3,G3
LOGICS_8350215,10,D4,H4
Blank3_MGSBatch4_plate2,1000,D5,H17
LOGICS_8350128,1,E1,I1
LOGICS_8350138,1,E2,I2
Zymo_MGSBatch1_plate2,100,E3,I15
LOGICS_8350111,10,E4,J4
LOGICS_8350007,1000,E5,J17
LOGICS_8350053,1000,F1,L13
LOGICS_8350214,100,F2,K14
LOGICS_8350028,10,F3,L3
LOGICS_8350078,10,F4,L4
LOGICS_8350145,1,F5,K5
LOGICS_8350039,10,G1,N1
LOGICS_8350046,100,G2,M14
LOGICS_8350004,1000,G3,N15
Assembly_negative1_plate2,1,G4,M4
PJT_InternalStandard_plate2,1000,G5,N17
Blank1_MGSBatch2_plate2,1,H1,O1
LOGICS_8350058,10,H2,P2
LOGICS_8350114,100,H3,O15
LOGICS_8350177,1000,H4,P16
DNA_Standard,1,H5,O5
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
	if loadwater or loadmastermix: reservoir = protocol.load_labware('usascientific_12_reservoir_22ml', '8') # reservoir with indexing mastermix (660ul) in A1 (First column) and Water (10 mL)

	# define pipettes
	left_pipette = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tips1, tips4, tips7, tips10, tips11])
	right_pipette = protocol.load_instrument('p20_multi_gen2', 'right', tip_racks=[tips1, tips4, tips7, tips10, tips11])
		
	#load water into the dilution plate for a 100x dilution
	if loadwater:
		right_pipette.pick_up_tip() #use single set of tips
		for i in range(1, 13): 
			for p in range(1, 6): # do 5 times for 100ul total
				right_pipette.aspirate(20, reservoir['A2'])
				right_pipette.dispense(20, dilutionplate['A'+str(i)])
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

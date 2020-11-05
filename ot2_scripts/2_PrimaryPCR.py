from opentrons import protocol_api


# metadata
metadata = {
	'protocolName': 'Primary PCR', 
	'author': 'J Bisanz, jordan.bisanz@gmail.com',
	'description': 'Load primary pcr mastermix and carryout 10-fold dilutions of template in 384 well qpcr plate',
	'apiLevel': '2.7'
}

def run(protocol: protocol_api.ProtocolContext):

	# define labware and locations
	tips1 = protocol.load_labware('opentrons_96_filtertiprack_20ul', '1') # 20ul filter tips on deck position 1
	tips4 = protocol.load_labware('opentrons_96_filtertiprack_20ul', '4') # 20ul filter tips on deck position 4
	reservoir = protocol.load_labware('usascientific_12_reservoir_22ml', '2') # reservoir with pcr mastermix (3.8mL) in A1 (First column)
	primarypcr = protocol.load_labware('biorad384pcrplate_384_wellplate_40ul', '3') # skirted 384 well plate of amplicons
	gDNA = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '5') # skirted 96 well plate containing extracted DNA

	# define pipettes
	left_pipette = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tips1, tips4])
	right_pipette = protocol.load_instrument('p20_multi_gen2', 'right', tip_racks=[tips1, tips4])

	# load the master mix into the pcr plate. NOTE: when using multichannel, only reference the top well... IE A1 to get entire column of B1, C1 ... 
	right_pipette.pick_up_tip() # only using a single set of tips to load mastermix as is same in every well.
	for i in range(1, 13): 
		right_pipette.aspirate(8, reservoir['A1'])
		right_pipette.dispense(8, primarypcr['A'+str(i)])
	right_pipette.drop_tip() 

	# add the templates and do dilution series
	for i in range(1, 13): 
		right_pipette.pick_up_tip() #note to save tips, not changing tips between dilutions as this is not intended to be quantitative
		#transfer 1ul from gDNA plate to pcr plate
		right_pipette.aspirate(1, gDNA['A'+str(i)])
		right_pipette.dispense(1, primarypcr['A'+str(i)])
		right_pipette.mix(10, 5, primarypcr['A'+str(i)]) # mix 10x by pipetting up and down 5ul
		#transfer down one row
		right_pipette.aspirate(1, primarypcr['A'+str(i)])
		right_pipette.dispense(1, primarypcr[chr(ord('A') + 1)+str(i)]) #chr(ord('A') + 1) gets the next letter in the alphabet
		right_pipette.mix(10, 5, primarypcr[chr(ord('A') + 1)+str(i)])
		#transfer over 12 columns
		right_pipette.aspirate(1, primarypcr[chr(ord('A') + 1)+str(i)])
		right_pipette.dispense(1, primarypcr['A'+str(i+12)])
		right_pipette.mix(10, 5, primarypcr['A'+str(i+12)])
		#transfer down one column again
		right_pipette.aspirate(1, primarypcr['A'+str(i+12)])
		right_pipette.dispense(1, primarypcr[chr(ord('A') + 1)+str(i+12)])
		right_pipette.mix(10, 5, primarypcr[chr(ord('A') + 1)+str(i+12)])
		#drop tip and move to next column on original plate
		right_pipette.drop_tip() 

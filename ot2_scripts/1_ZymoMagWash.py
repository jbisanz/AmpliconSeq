from opentrons import protocol_api

# metadata
metadata = {
	'protocolName': 'Zymo Mag Wash', 
	'author': 'J Bisanz, jordan.bisanz@gmail.com',
	'description': 'Carryout washing and elution steps of zymobiomics 96 MAgBead DNA Kit (D4608/4302). Tip usage has been optimized to allow the protocol to run without intervention and as such dirty tips will be returned to boxes. Dispose of tip boxes after use.',
	'apiLevel': '2.7'
}

def run(protocol: protocol_api.ProtocolContext):

	# which steps should be run?
	AddBeads = True
	AddBindingBuffer = True
	CaptureBinding = True
	Wash1 = True
	Wash2 = True
	Wash2repeat = True
	Dry = True
	Elute = True

	# set tweakable variables
	elution_volume = 100 # ul of water to add to final beads
	elution_to_plate = 70 # ul to transfer to final elution plate
	capture_depth = -3 # depth below ideal bottom of plate to remove supernatants, this may be required as a function of a poor calibration or labware def
	capture_min = 2 # number of minutes to capture beads on magnets
	cols_to_extract = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # which columns should be extracted?
	nmix = 5 # number of times to pipette to mix
	drying_min = 20 # number of minutes to evaporate residual ethanol !!!! SET TO 20
	trash_speed = 1 # the relative speed to discard of liquids into trash, this is an integer multiplier of normal speed, set higher to clear bubbles on outside of tip


	
	# define deck layout
	MagModule = protocol.load_module('magnetic module gen2', 10)
	BindingPlate = MagModule.load_labware('nest_96_wellplate_2ml_deep') # use the
	ElutionPlate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '3') # an empty biorad 96 well plate

	BeadsAndWater = protocol.load_labware('usascientific_12_reservoir_22ml', '2') # magbeads in A1 (4 mL), water in A2 (10mL), the end columns will be used for waste
	BindingBuffer = protocol.load_labware('agilent_1_reservoir_290ml', '7') # reservoir with 70 mL binding buffer
	MagWash1 = protocol.load_labware('agilent_1_reservoir_290ml', '4') # reservoir with 100 mL magwash1
	MagWash2 = protocol.load_labware('agilent_1_reservoir_290ml', '1') # reservoir with 200 mL magwash2

	tips_binding = protocol.load_labware('opentrons_96_filtertiprack_200ul', '11')
	tips_wash1 =  protocol.load_labware('opentrons_96_filtertiprack_200ul', '8')
	tips_wash2 =  protocol.load_labware('opentrons_96_filtertiprack_200ul', '5')
	tips_wash2_repeat =  protocol.load_labware('opentrons_96_filtertiprack_200ul', '9')
	tips_elution = protocol.load_labware('opentrons_96_filtertiprack_200ul', '6')

	fixed_trash = protocol.fixed_trash['A1']


	set_rail_lights = True

	# define pipettes
	multichannel = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[tips_binding, tips_wash1, tips_wash2, tips_wash2_repeat, tips_elution])
	#P1000 = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[tips_binding, tips_wash1, tips_wash2, tips_wash2rep])

	### Prerun setup ########################################
	MagModule.disengage()

	### MAG BINDING ######################################

	if AddBindingBuffer:
		protocol.comment('--------->Adding 600 ul binding buffer')
		multichannel.pick_up_tip(tips_binding['A1'])
		for i in cols_to_extract:
			multichannel.aspirate(200, BindingBuffer['A1'])
			multichannel.dispense(200, BindingPlate['A'+str(i)].top(4))
			#multichannel.blow_out()
			multichannel.aspirate(200, BindingBuffer['A1'])
			multichannel.dispense(200, BindingPlate['A'+str(i)].top(4))
			#multichannel.blow_out()
			multichannel.aspirate(200, BindingBuffer['A1'])
			multichannel.dispense(200, BindingPlate['A'+str(i)].top(4))
			#multichannel.blow_out()
		multichannel.return_tip()
		
	if AddBeads:
		protocol.comment('--------->Adding 25ul mag beads')
		multichannel.pick_up_tip(tips_binding['A2'])
		multichannel.mix(10, 100, BeadsAndWater['A1'].bottom(3)) # mix beads 20 x by pulling up 100ul
		for i in cols_to_extract:
			multichannel.aspirate(25, BeadsAndWater['A1'])
			multichannel.dispense(25, BindingPlate['A'+str(i)].top(4)
		multichannel.return_tip()
		for i in cols_to_extract:
			multichannel.pick_up_tip(tips_binding['A'+str(i)])
			multichannel.mix(10, 200, BeadsAndWater['A1'].bottom(3))
			multichannel.return_tip()
		
	if CaptureBinding:
		protocol.comment('--------->Removing Binding Buffer')
		MagModule.engage()
		protocol.delay(minutes=capture_min)
		for i in cols_to_extract:
			multichannel.pick_up_tip(tips_binding['A'+str(i)])
			multichannel.aspirate(200, BindingPlate['A'+str(i)])
			multichannel.dispense(200, fixed_trash, rate = trash_speed)
			#multichannel.blow_out()
			multichannel.touch_tip()
			multichannel.aspirate(200, BindingPlate['A'+str(i)])
			multichannel.dispense(200, fixed_trash, rate = trash_speed)
			#multichannel.blow_out()
			multichannel.touch_tip()
			multichannel.aspirate(200, BindingPlate['A'+str(i)])
			multichannel.dispense(200, fixed_trash, rate = trash_speed)
			#multichannel.blow_out()
			multichannel.aspirate(200, BindingPlate['A'+str(i)].bottom(capture_depth), rate=0.2)
			multichannel.dispense(200, fixed_trash, rate = trash_speed)
			#multichannel.blow_out()
			multichannel.return_tip()
		
	if Wash1:
		protocol.comment('--------->Doing Wash 1')
		MagModule.disengage()
		multichannel.pick_up_tip(tips_wash1['A1'])
		for i in cols_to_extract:
			multichannel.aspirate(200, MagWash1['A1'])
			multichannel.dispense(200, BindingPlate['A'+str(i)].top(4))
			#multichannel.blow_out()
			multichannel.aspirate(200, MagWash1['A1'])
			multichannel.dispense(200, BindingPlate['A'+str(i)].top(4))
			#multichannel.blow_out()
			multichannel.aspirate(200, MagWash1['A1'])
			multichannel.dispense(200, BindingPlate['A'+str(i)].top(4))
			#multichannel.blow_out()
			multichannel.aspirate(200, MagWash1['A1'])
			multichannel.dispense(200, BindingPlate['A'+str(i)].top(4))
			#multichannel.blow_out()
		multichannel.return_tip()	
		for i in cols_to_extract:
			multichannel.pick_up_tip(tips_wash1['A'+str(i)])
			multichannel.aspirate(100, MagWash1['A1'])
			multichannel.dispense(100, BindingPlate['A'+str(i)])
			multichannel.mix(nmix, 180, BindingPlate['A'+str(i)].bottom(2))
			multichannel.blow_out()
			multichannel.return_tip()
		MagModule.engage()
		protocol.delay(minutes=capture_min)
		for i in cols_to_extract:
			multichannel.pick_up_tip(tips_wash1['A'+str(i)])
			multichannel.aspirate(200, BindingPlate['A'+str(i)])
			multichannel.dispense(200, fixed_trash, rate = trash_speed)
			#multichannel.blow_out()
			multichannel.aspirate(200, BindingPlate['A'+str(i)])
			multichannel.dispense(200, fixed_trash, rate = trash_speed)
			#multichannel.blow_out()
			multichannel.aspirate(200, BindingPlate['A'+str(i)])
			multichannel.dispense(200, fixed_trash, rate = trash_speed)
			#multichannel.blow_out()
			multichannel.aspirate(200, BindingPlate['A'+str(i)])
			multichannel.dispense(200, fixed_trash, rate = trash_speed)
			#multichannel.blow_out()
			multichannel.aspirate(200, BindingPlate['A'+str(i)].bottom(capture_depth), rate=0.2)
			multichannel.dispense(200, fixed_trash, rate = trash_speed)
			multichannel.blow_out()
			multichannel.return_tip()
			
	if Wash2:
		protocol.comment('--------->Doing Wash 2')
		MagModule.disengage()
		multichannel.pick_up_tip(tips_wash2['A1'])
		for i in cols_to_extract:
			multichannel.aspirate(200, MagWash2['A1'])
			multichannel.dispense(200, BindingPlate['A'+str(i)].top(4))
			#multichannel.blow_out()
			multichannel.aspirate(200, MagWash2['A1'])
			multichannel.dispense(200, BindingPlate['A'+str(i)].top(4))
			#multichannel.blow_out()
			multichannel.aspirate(200, MagWash2['A1'])
			multichannel.dispense(200, BindingPlate['A'+str(i)].top(4))
			#multichannel.blow_out()
			multichannel.aspirate(200, MagWash2['A1'])
			multichannel.dispense(200, BindingPlate['A'+str(i)].top(4))
			#multichannel.blow_out()
		multichannel.return_tip()	
		for i in cols_to_extract:
			multichannel.pick_up_tip(tips_wash2['A'+str(i)])
			multichannel.aspirate(100, MagWash2['A1'])
			multichannel.dispense(100, BindingPlate['A'+str(i)])
			multichannel.mix(nmix, 180, BindingPlate['A'+str(i)].bottom(2))
			multichannel.blow_out()
			multichannel.return_tip()
		MagModule.engage()
		protocol.delay(minutes=capture_min)
		for i in cols_to_extract:
			multichannel.pick_up_tip(tips_wash2['A'+str(i)])
			multichannel.aspirate(200, BindingPlate['A'+str(i)])
			multichannel.dispense(200, fixed_trash, rate = trash_speed)
			#multichannel.blow_out()
			multichannel.aspirate(200, BindingPlate['A'+str(i)])
			multichannel.dispense(200, fixed_trash, rate = trash_speed)
			#multichannel.blow_out()
			multichannel.aspirate(200, BindingPlate['A'+str(i)])
			multichannel.dispense(200, fixed_trash, rate = trash_speed)
			#multichannel.blow_out()
			multichannel.aspirate(200, BindingPlate['A'+str(i)]) # is this a calibration issue?
			multichannel.dispense(200, fixed_trash, rate = trash_speed)
			#multichannel.blow_out()
			multichannel.aspirate(200, BindingPlate['A'+str(i)].bottom(capture_depth), rate=0.2)
			multichannel.dispense(200, fixed_trash, rate = trash_speed)
			#multichannel.blow_out()
			multichannel.return_tip()
			
	if Wash2repeat:
		protocol.comment('--------->Repeating Wash 2')
		MagModule.disengage()
		multichannel.pick_up_tip(tips_wash2_repeat['A1'])
		for i in cols_to_extract:
			multichannel.aspirate(200, MagWash2['A1'])
			multichannel.dispense(200, BindingPlate['A'+str(i)].top(4))
			#multichannel.blow_out()
			multichannel.aspirate(200, MagWash2['A1'])
			multichannel.dispense(200, BindingPlate['A'+str(i)].top(4))
			#multichannel.blow_out()
			multichannel.aspirate(200, MagWash2['A1'])
			multichannel.dispense(200, BindingPlate['A'+str(i)].top(4))
			#multichannel.blow_out()
			multichannel.aspirate(200, MagWash2['A1'])
			multichannel.dispense(200, BindingPlate['A'+str(i)].top(4))
			#multichannel.blow_out()
		multichannel.return_tip()	
		for i in cols_to_extract:
			multichannel.pick_up_tip(tips_wash2_repeat['A'+str(i)])
			multichannel.aspirate(100, MagWash2['A1'])
			multichannel.dispense(100, BindingPlate['A'+str(i)])
			multichannel.mix(nmix, 180, BindingPlate['A'+str(i)].bottom(5))
			multichannel.blow_out()
			multichannel.return_tip()
		MagModule.engage()
		protocol.delay(minutes=capture_min)
		for i in cols_to_extract:
			multichannel.pick_up_tip(tips_wash2_repeat['A'+str(i)])
			multichannel.aspirate(200, BindingPlate['A'+str(i)])
			multichannel.dispense(200, fixed_trash, rate = trash_speed)
			#multichannel.blow_out()
			multichannel.aspirate(200, BindingPlate['A'+str(i)])
			multichannel.dispense(200, fixed_trash, rate = trash_speed)
			#multichannel.blow_out()
			multichannel.aspirate(200, BindingPlate['A'+str(i)])
			multichannel.dispense(200, fixed_trash, rate = trash_speed)
			#multichannel.blow_out()
			multichannel.aspirate(200, BindingPlate['A'+str(i)]) # is this a calibration issue?
			multichannel.dispense(200, fixed_trash, rate = trash_speed)
			#multichannel.blow_out()
			multichannel.aspirate(200, BindingPlate['A'+str(i)].bottom(capture_depth), rate=0.2)
			multichannel.dispense(200, fixed_trash, rate = trash_speed)
			#multichannel.blow_out()
			multichannel.return_tip()
	
	if Dry:
		protocol.comment('--------->Drying DNA')
		protocol.delay(minutes=drying_min)

	if Elute:
		protocol.comment('--------->Eluting DNA')
		MagModule.disengage()
		for i in cols_to_extract:
			multichannel.pick_up_tip(tips_elution['A'+str(i)])
			multichannel.aspirate(elution_volume, BeadsAndWater['A2'])
			multichannel.dispense(elution_volume, BindingPlate['A'+str(i)])
			multichannel.mix(nmix, elution_to_plate, BindingPlate['A'+str(i)].bottom(capture_depth))
			#multichannel.blow_out()
			multichannel.return_tip()
		MagModule.engage()
		protocol.delay(minutes=capture_min)
		for i in cols_to_extract:
			multichannel.pick_up_tip(tips_elution['A'+str(i)])
			multichannel.aspirate(elution_to_plate, BindingPlate['A'+str(i)].bottom(capture_depth+1), rate=0.2)
			multichannel.dispense(elution_to_plate, ElutionPlate['A'+str(i)])
			#multichannel.blow_out()
			multichannel.return_tip()

			
	
			
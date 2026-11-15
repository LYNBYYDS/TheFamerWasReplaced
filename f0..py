def main_sunflower():
	
	# 0 其他
	# 1 太阳花
	
	type = [
			[1, 1, 1, 1, 1, 1, 1, 1],
			[1, 1, 1, 1, 1, 1, 1, 1],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0]]
	
	clear()
	
	for i in range(get_world_size()):
		till()
		plant(Entities.Sunflower)
		if get_water() < 0.5:
			use_item(Items.Water)
			use_item(Items.Fertilizer)
		move(North)
	move(East)
	for i in range(get_world_size()):
		till()
		plant(Entities.Sunflower)
		if get_water() < 0.5:
			use_item(Items.Water)
			use_item(Items.Fertilizer)
		move(North)
	move(East)
	for i in range(get_world_size()):
		till()
		plant(Entities.Sunflower)
		if get_water() < 0.5:
			use_item(Items.Water)
			use_item(Items.Fertilizer)
		move(North)
	move(West)
	move(West)
	

	while True :
		for i in range(get_world_size()):
			harvest()
			if get_water() < 0.5:
				use_item(Items.Water)
				use_item(Items.Fertilizer)
			plant(Entities.Sunflower)
			move(North)
		move(East)
		for i in range(get_world_size()):
			harvest()
			if get_water() < 0.5:
				use_item(Items.Water)
				use_item(Items.Fertilizer)
			plant(Entities.Sunflower)
			move(North)
		move(East)
		for i in range(get_world_size()):
			harvest()
			if get_water() < 0.5:
				use_item(Items.Water)
				use_item(Items.Fertilizer)
			plant(Entities.Sunflower)
			move(North)
		move(West)
		move(West)
#-----------------------------------------------------------------------------#	
		
		
		
		
			
def AtoB(x_start,y_start,x_end,y_end):
	
	if x_start < x_end :
		for i in range(x_end - x_start):
			move(East)
	elif x_start > x_end :
		for i in range(x_start - x_end):
			move(West)
	
	if y_start < y_end :
		for i in range(y_end - y_start):
			move(North)
	elif y_start > y_end :
		for i in range(y_start - y_end):
			move(South)


def main_comb():
	
	clear()
	
	turn = 0
	companion = [
				[0, 0, Entities.Grass],
				[0, 1, Entities.Grass],
				[0, 2, Entities.Grass],
				[0, 3, Entities.Grass],
				[0, 4, Entities.Grass],
				[0, 5, Entities.Grass],
				[0, 6, Entities.Grass],
				[0, 7, Entities.Grass]
				]
	
	while True :
		
		AtoB(get_pos_x(),get_pos_y(),companion[turn][0],companion[turn][1])
	
		if get_entity_type() != None or can_harvest() :
			if (get_entity_type() == Entities.Grass or get_entity_type() == Entities.Bush) :
				harvest()
			elif(get_entity_type() == Entities.Tree or get_entity_type() == Entities.Carrot) :
				harvest()
				till()
		else :
			while(not can_harvest()):
				print("not ready")
	
		
		turn = (turn+7)%8
		plant_type, (x, y) = get_companion()
				
		AtoB(get_pos_x(),get_pos_y(),x,y)	
		
		if get_entity_type() != None or can_harvest() :
			if (get_entity_type() == Entities.Grass or get_entity_type() == Entities.Bush) :
				if (plant_type == Entities.Grass or plant_type == Entities.Bush) :
					harvest()
					if get_water() < 0.5:
						use_item(Items.Water)
						use_item(Items.Fertilizer)
					plant(plant_type)
				elif(plant_type == Entities.Tree or plant_type == Entities.Carrot) :
					harvest()
					if get_water() < 0.5:
						use_item(Items.Water)
						use_item(Items.Fertilizer)
					till()
					plant(plant_type)
			if (get_entity_type() == Entities.Tree or get_entity_type() == Entities.Carrot) :
				if (plant_type == Entities.Grass or plant_type == Entities.Bush) :
					harvest()
					if get_water() < 0.5:
						use_item(Items.Water)
						use_item(Items.Fertilizer)
					till()
					plant(plant_type)
				elif(plant_type == Entities.Tree or plant_type == Entities.Carrot) :
					harvest()
					if get_water() < 0.5:
						use_item(Items.Water)
						use_item(Items.Fertilizer)
					plant(plant_type)
		else :
			while(not can_harvest()):
				print("not ready")
	
		turn = (turn+1)%8
		companion[turn][0] = x
		companion[turn][1] = y
		companion[turn][2] = plant_type
		turn = (turn+1)%8
		

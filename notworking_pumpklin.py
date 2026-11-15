
			
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
			
			
def harvest_sunflower():
	for i in range(2):
		AtoB(get_pos_x(), get_pos_y(), 0, 6+i)
		for j in range(5):
			harvest()
			plant(Entities.Sunflower)
			move(East)

			

def main_pumpkin():
	
	# 0 其他
	# 1 南瓜
	
	type = [
			[1, 1, 1, 1, 1, 1, 0, 0],
			[1, 1, 1, 1, 1, 1, 0, 0],
			[1, 1, 1, 1, 1, 1, 0, 0],
			[1, 1, 1, 1, 1, 1, 0, 0],
			[1, 1, 1, 1, 1, 1, 0, 0],
			[1, 1, 1, 1, 1, 1, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0]]
	
	clear()
			
	counter = 0
	
	dead_pumpkin_coords = [
								[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], 
								[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], 
								[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], 
								[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], 
								[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], 
								[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]
								]
								
	turn = 0
	
	
	while True :
		
		print(turn)
		
		if turn == 0:
			for i in range(get_world_size()):
				for j in range(get_world_size()):
					if type[i][j] == 0 :
						if i != 5 :
							till()
							plant(Entities.Sunflower)
					if type[i][j] == 1 :
						till()
						plant(Entities.Pumpkin)
					move(North)
				move(East)
				if i >= 5 :
					break
					
		elif turn == 1:
			for i in range(6):
				AtoB(get_pos_x(), get_pos_y(), 0+i, 0)
				for j in range(6):
					if get_entity_type() == Entities.Dead_Pumpkin :
						plant(Entities.Pumpkin)
						dead_pumpkin_coords[counter][0] = get_pos_x()
						dead_pumpkin_coords[counter][1] = get_pos_y()
						counter = counter + 1
					move(North)
			
		elif turn > 1 and counter == 0 :
			AtoB(get_pos_x(), get_pos_y(), 0, 0)
			harvest()
			turn = -1
			for i in range(6):
				AtoB(get_pos_x(), get_pos_y(), 0+i, 0)
				for j in range(6):
					plant(Entities.Pumpkin)
					move(North)
				
		if turn > 1 and counter != 0:
			
			for i in range(counter):
				AtoB(get_pos_x(), get_pos_y(), dead_pumpkin_coords[i][0], dead_pumpkin_coords[i][1])
				if get_entity_type() == Entities.Dead_Pumpkin :
					plant(Entities.Pumpkin)
				else :
					dead_pumpkin_coords.pop(i)
					dead_pumpkin_coords.append([0, 0])
					counter = counter -1
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
					
		
						
		turn = turn + 1
		
		
		harvest_sunflower()

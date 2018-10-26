class room():
	def __init__(self,name,description):
		self.room_name = name 
		self.r_description = description
		self.room_dict = {}
		self.treasure_list = []
		"""Sets paramaters for the room class that creates room instances. The __init__ method creates the variables, some through the paramater inputs, and names them.
		
		Variables:
		self.room_name is the name of the room in string form and pulls from the parameter input name.
		self.r_description is the description of the room in string form and pulls from the parameter input description.
		self.room_dict is a dictionary that will be set to contain keys that are directional and values that are other room instances. Currently set to an empty dictionary.
		Self.treasure_list is a list that will be set to contain instances of treasure that can be found in the room. Currently set to an empty list.
		"""
	def get_room_name(self):
		return self.room_name
	def set_room_name(self,name):
		self.room_name = room_name
	def get_r_description(self):
		return self.r_description
	def set_r_description(self,r_description):
		self.r_description = r_description
	def get_room_dict(self):
		return self.room_dict
	def set_room_dict(self,room_dict):
		self.room_dict = room_dict
	def get_treasure_list(self):
		return self.treasure_list
	def set_treasure_list(self,treasure_list):
		self.treasure_list = treasure_list
class player():
	def __init__(self):
		self.current_room = ''
		self.num_lives = 3
		self.inventory = []
		self.points = 0
		"""Sets paramaters, in this case none, for the player class that creates the player instance. The __init__ method creates the variables and names them.
		
		Variables:
		self.current_room will be set to the name of the current room in string form. Currently an empty string.
		self.num_lives is set to 3 to start and is the amount of lives for the player. Hitting a wall or entering secret code will manipulate it later. Will be callable in game.
		self.inventory will be set to contain the names of each treasure collected in string form. Currently set to an empty list. Will be callable in game.
		Self.points will be set to new values every time that a treasure is collected. Currently set to 0 to start. Will be callable in game.
		"""
	def get_current_room(self):
		return self.current_room
	def set_current_room(self,current_room):
		self.current_room = current_room
	def get_num_lives(self):
		return self.num_lives
	def set_num_lives(self,num_lives):
		self.num_lives = num_lives
	def get_inventory(self):
		return self.inventory
	def set_inventory(self,inventory):
		self.inventory = inventory
	def get_points(self):
		return self.points
	def set_points(self, points):
		self.points = points
class treasure():
	def __init__(self,name,t_description,num_points):
		self.name = name
		self.t_description = t_description
		self.num_points = num_points
		"""Sets paramaters for the treasure class that creates the treasure instances. The __init__ method creates the variables and names them.
		
		Variables:
		self.name will pull from the parameter name and will be the name of the treasure in string form.
		self.t_description will pull from the parameter t_description and be the desciption of the treasure in string form.
		Self.num_points will pull from the parameter num_points and will be the number of points the treasure is worth in integer form.
		"""
	def get_name(self):
		return self.name
	def set_name(self,name):
		self.name = name
	def get_t_description(self):
		return self.t_description
	def set_t_description(self,t_description):
		self.t_description = t_description
	def get_num_points(self):
		return self.num_points
	def set_num_points(self,num_points):
		self.num_points = num_points
class game():
	def __init__(self):
		self.player = player()
		self.room_1 = room('Room 1','You are standing in a comfy starting point! Your objective is to collect treasure and reach 100 points. Once you are at 100 points you must get to the end room. Running into a wall will result in losing a life. You have 3 lives.')
		self.room_2 = room('Room 2','Wow, you just entered a horrifying wasteland!')
		self.room_3 = room('Room 3','Very close to the end, beware of your points!')
		self.room_4 = room('Room 4','Odd room.')
		self.room_5 = room('Room 5','Tiny shed of a room.')
		self.room_6 = room('Room 6','Welcome to the end! Got enough points?')
		self.room_7 = room('Room 7','Very odd room.')
		self.room_8 = room('Room 8','Huge throne room!')
		self.room_9 = room('Room 9','Swampy room.')
		self.room_1.set_room_dict({'s':self.room_2})
		self.room_2.set_room_dict({'s':self.room_3,'w':self.room_4,'e':self.room_5,'n':self.room_1})
		self.room_3.set_room_dict({'e':self.room_6,'n':self.room_2})
		self.room_4.set_room_dict({'w':self.room_7,'e':self.room_2})
		self.room_5.set_room_dict({'w':self.room_2,'e':self.room_9})
		self.room_6.set_room_dict({'w':self.room_3})
		self.room_7.set_room_dict({'s':self.room_8,'e':self.room_4})
		self.room_8.set_room_dict({'n':self.room_7})
		self.room_9.set_room_dict({'w':self.room_5})
		self.treasure_1 = treasure('Bag','A shiny bag was collected!',10)
		self.treasure_2 = treasure('Ring','A big diamond ring was collected!',20)
		self.treasure_3 = treasure('Crown','A crown for a king was collected!',30)
		self.treasure_4 = treasure('Goblet','A mighty fine goblet was collected!',30)
		self.treasure_5 = treasure('Marble','A small marble was collected!',5)
		self.treasure_6 = treasure('String','A string for the marble was collected!',5)
		self.room_2.set_treasure_list([self.treasure_1])
		self.room_3.set_treasure_list([self.treasure_2])
		self.room_8.set_treasure_list([self.treasure_3,self.treasure_4])
		self.room_9.set_treasure_list([self.treasure_5,self.treasure_6])
		self.start_room = self.room_1
		self.end_room = self.room_6
		"""Sets paramaters, in this case none, for the game class that creates the game instance. The __init__ method creates the variables and names them.
		
		Variables:
		self.player creates the player instance and calls the player class.
		self.room_i has 9 different variables and each creates a seperate room by calling the room class with name and description parameters placed in.
		self.room_i also has the .set_room_dict() method called on all 9 different rooms to pair directional keys to other room instances.
		self.treasure_i has 6 different variables and each creates a seperate treasure by calling the treasure class with name, desctiption, nad points parameters placed in.
		self.room_i has 4 of the 9 different room variables again but this time with the .set_treasure_list() method to place treasure instances in a list in those rooms.
		self.start_room sets the start room as self.room_1.
		self.end_room sets the end room as self.room_6.
		"""
	def get_start_room(self):
		return self.start_room
	def set_start_room(self,start_room):
		self.start_room = start_room
	def get_end_room(self):
		return self.end_room
	def set_end_room(self,end_room):
		self.end_room = end_room
	def play(self):
		self.player.set_current_room(self.start_room)
		print(self.player.get_current_room().get_r_description())
		while self.player.get_num_lives() > 0 and self.player.get_inventory() != ['Exit loop.']:
			direction = input("Type which direction you would like to go! Options are 'n', 's', 'e', 'w'. You may also check your lives by typing 'lives', your points by typing in 'points', and your inventory by typing 'inventory'.")
			while direction in ['Magical fairy grant me another life!','lives','points','inventory'] or direction not in ['n','s','e','w']:
				if direction == 'Magical fairy grant me another life!':
					self.player.set_num_lives(self.player.get_num_lives() + 1)
					print('Your new life total is {}!'.format(self.player.get_num_lives()))
					direction = input("Type which direction you would like to go! Options are 'n', 's', 'e', 'w'. You may also check your lives by typing 'lives', your points by typing in 'points', and your inventory by typing 'inventory'.")
				elif direction == 'lives':
					print('You have {} lives.'.format(self.player.get_num_lives()))
					direction = input("Type which direction you would like to go! Options are 'n', 's', 'e', 'w'. You may also check your lives by typing 'lives', your points by typing in 'points', and your inventory by typing 'inventory'.")
				elif direction == 'points':
					print('You have {} points.'.format(self.player.get_points()))
					direction = input("Type which direction you would like to go! Options are 'n', 's', 'e', 'w'. You may also check your lives by typing 'lives', your points by typing in 'points', and your inventory by typing 'inventory'.")
				elif direction == 'inventory':
					if len(self.player.inventory) > 0:
						print('Your inventory list is {}.'.format(self.player.get_inventory()))
						direction = input("Type which direction you would like to go! Options are 'n', 's', 'e', 'w'. You may also check your lives by typing 'lives', your points by typing in 'points', and your inventory by typing 'inventory'.")
					else:
						print('You have no items in your inventory.')
						direction = input("Type which direction you would like to go! Options are 'n', 's', 'e', 'w'. You may also check your lives by typing 'lives', your points by typing in 'points', and your inventory by typing 'inventory'.")
				else:
					direction =  input("ENTRY NOT VALID. Type which direction you would like to go! Options are 'n', 's', 'e', 'w'. You may also check your lives by typing 'lives', your points by typing in 'points', and your inventory by typing 'inventory'.")
			if direction in self.player.get_current_room().get_room_dict():
				self.player.set_current_room(self.player.get_current_room().get_room_dict()[direction])
				print(self.player.get_current_room().get_r_description())
				if len(self.player.get_current_room().get_treasure_list()) > 0:
					for t in self.player.get_current_room().get_treasure_list():  
						print(t.get_t_description() + ' This item is worth {} points!'.format(t.get_num_points()))
						self.player.set_points(self.player.get_points() + t.get_num_points())
						self.player.inventory.append(t.get_name())
					self.player.get_current_room().set_treasure_list([])
					print('Your new total is {} points and your items have been added to your inventory!'.format(self.player.get_points()))
			else:
				self.player.set_num_lives(self.player.get_num_lives() - 1)
				print('You lost a life! Your new life total is {}'.format(self.player.get_num_lives()))
			if self.player.get_current_room() == self.end_room and self.player.get_points() == 100 and self.player.get_num_lives() > 0:
				print('Congrats you have enough points! You win!')
				self.player.set_inventory(['Exit loop.'])
			elif self.player.get_current_room() == self.end_room and self.player.get_points() < 100 and self.player.get_num_lives() > 0:
				print('You do not have 100 points, turn around.')
		if self.player.get_num_lives() < 1:
			print('You lose.')
			"""the play method is what actually runs the game and allows the player to move room to room collecting items and points.

			Steps:
			Starts a while loop that keeps running until the player loses all lives or hits a point where there is a force exit.
			direction is a variable that asks for an input on what the player would like to do.
			There is then another while loop that runs until the player enters a directional value such as 'n', 's', 'e', 'w'.
			In this loop there are numerous if, elif, and else statements. These allow the player to call their inventory, points, and lives. As well there is a secret cheat.
			After the second while loop there is more if and else statements, the first two deal with the direction, either moving a player to the next room or taking a life.
			The next two if and elif statements deal with winning and exiting the original while loop or asking the player to turn around because they do not have the points.
			The last if statement is outside the original while loop where if they reach 0 lives then they lose.
			"""
game().play()
import unittest
room = room('Test room','Test room for unittest.')
room.set_treasure_list(['Test object'])
player = player()
player.set_points(60)
player.set_num_lives(1)
class test_room_and_player(unittest.TestCase):
	def test_get_treasure_list(self):
		self.assertEqual(room.get_treasure_list(), ['Test object'])
		"""Testing .get_treasure_list() works correctly.

		Steps:
		Utilizes the unittest import.
		Room variable is set by calling the room class with parameters.
		Room treasure list is set using the .set_treasure_list() method."""
	def test_get_r_description(self):
		self.assertEqual(room.get_r_description(), 'Test room for unittest.')
		"""Testing .get_r_description() works correctly.

		Steps:
		Utilizes the unittest import.
		Room variable is set by calling the room class with parameters.
		Room description is set in those parameters."""
	def test_get_room_name(self):
		self.assertEqual(room.get_room_name(), 'Test room')
		"""Testing .get_room_name() works correctly.

		Steps:
		Utilizes the unittest import.
		Room variable is set by calling the room class with parameters.
		Room name is set in those parameters."""
	def test_get_points(self):
		self.assertEqual(player.get_points(), 60)
		"""Testing .get_points() works correctly.

		Steps:
		Utilizes the unittest import.
		Player variable is set by calling the player class with parameters.
		Player points is set using the .set_points() method."""
	def test_get_num_lives(self):
		self.assertEqual(player.get_num_lives(), 1)
		"""Testing .get_num_lives() works correctly.

		Steps:
		Utilizes the unittest import.
		Player variable is set by calling the player class with parameters.
		Player points is set using the .set_num_lives() method."""
print(unittest.main(verbosity = 2))


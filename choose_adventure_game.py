rooms = {"hall": {"description": "A long, dark hall.",
                  "north": "kitchen", 
                  "east": "library",
                  "items": ['flashlight']
                  },
    "kitchen": {"description": "A kitchen with a strange smell.", 
                "south": "hall",
                'north': 'great hall',
                'items': ["paper scrap"""],
                'dark': True
                },
    "library": {"description": "Filled with dusty books. There is a treasure chest in the corner with a code lock.", 
                "west": "hall",
                'items': [],
                'locked' : True,
                'dark' : True
                },
    """great hall""": {"description": "A large throne room, tattered banners drape the walls.", 
                "south": "kitchen",
                'items': ["""rusty sword"""],
                'dark' : True,
                'monster': {'Name' : 'Spectral King', 'HP': 10, 'Attack': 6}
                }
}

player_HP = 20
player_attack = 1
inventory = []

if 'rusty sword' in inventory:
    player_attack += 5

def describe_room(player_position, current_room):
    if not current_room['items']:
            print(f"\nYou are in the {player_position}. {current_room['description']} There is nothing else here.")
    else:
                print(f"\nYou are in the {player_position}. {current_room['description']} In the {player_position} is: {', '.join(current_room['items'])}")
       
    
def move_player(player_position, current_room):
        print(f"\nYou are in the {player_position}.")
        if "north" in current_room:
            print("You can go North")
        if "south" in current_room:
            print("You can go South")
        if "east" in current_room:
            print("You can go East")
        if "west" in current_room:
            print("You can go West")
            
        player_choice = input('\nWhich way would you like to go? ')
        direction = player_choice.lower()
        if direction in current_room:
            next_room = current_room[direction]
            room_info = rooms[next_room]
            if room_info.get('locked'):
                if 'key' in inventory:
                    print("You use the key.")
                    room_info['locked'] = False
                    player_position = current_room[direction]
                else:
                    print("This way is locked.")
                    return player_position
            
            if room_info.get('dark'):
                    if 'flashlight' in inventory:
                        print("\nIt is dark in here. You turn on the flashlight.")
                        player_position = current_room[direction]
                    else:
                        print(f"\nIt is too dark in there. You better stay in the {player_position}.")
                        return player_position
            else:
                player_position = current_room[direction]
        else:
            print("You can't go that way.")
        return player_position
        
def pick_up_item(current_room):
        print(current_room['items'])
        item = input("Which item would you like to take? ")
        if item in current_room['items']:
                inventory.append(item)
                current_room['items'].remove(item)
                print(f"{item} added to inventory.")
        else:
                print(f"{item} is not here.")
                
def check_inventory():    
            if not inventory:
                print("You have no items in your inventory.")
            else:
                print("Inventory: "+', '.join(inventory))
                if '''paper_scrap''' in inventory:
                    print("The paper scrap says 5293")
    
def drop_item(player_position, current_room):
        item = input("Which item would you like to drop? ")
        if item in inventory:
            current_room['items'].append(item)
            inventory.remove(item)
            print(f"{item} left in {player_position}")
        else:
            print(f"You do not have {item} in your inventory.")
            
def open_chest():        
        code_guess = int(input("What is the code: "))
        if code_guess == 5293:
            print("The chest opens and is filled with gold! Congratulations, you win!")
        else:
            print("The lock stays firmly closed.")
            
def enter_combat(player_HP, current_room, player_attack):
    monster_name = current_room['monster']['Name']
    monster_HP = current_room['monster']['HP']
    monster_attack = current_room['monster']['Attack']
    while monster_HP > 0 and player_HP > 0:
        print("""What would you like to do?
              1. Attack
              2. Dodge
              3. Flee
              4. Check Inventory
              5. Exit
              """)
        choice = input('Choose an option: ')
    
        if choice == "1":
            print(f"The {monster_name} attacks!")
            player_HP -= monster_attack
            print(f"Your HP: {player_HP}")
            monster_HP -= player_attack
            print(f"{monster_name}'s HP: {monster_HP}")
            
    if player_HP <= 0:
        print("You are defeated. Game over")
    if monster_HP <= 0:
        print('You have defeated the monster!')
        del current_room['monster']
        if current_room == 'great hall':
            current_room['items'].append('key')
            return player_HP
        
def main_menu():
        player_position = "hall"
        while True:
            if player_HP <= 0 :
                print("You are defeated. Game over.")
                break
            current_room = rooms[player_position]
            describe_room(player_position, current_room)
            
            if current_room.get('monster'):
                print("""
                      A spectral king bearing a glowing sword rises to meet you.
                      What would you like to do?
                      1. Fight
                      2. Pick up item
                      3. Drop item
                      4. Check Inventory
                      5. Flee
                      6. Exit
                      """)
                      
                choice = input('Choose an option: ')
                
                if choice == "1":
                   enter_combat(player_HP, current_room, player_attack)
                elif choice == "2":
                   pick_up_item(current_room)
                elif choice == "3":
                   drop_item(player_position, current_room)
                elif choice == "4":
                   check_inventory()
                elif choice == "5":
                    move_player()
                elif choice == '6':
                   print('Goodbye!')
                   break
                else:
                   print('Invalid. Please try again.')
            
            elif player_position != 'library':
                 print("""
                       What would you like to do?
                       1. Move
                       2. Pick up item
                       3. Drop item
                       4. Check Inventory
                       5.Exit
                       """)
                 choice = input("Choose an option: ")
             
                 if choice == "1":
                    player_position = move_player(player_position, current_room)
                 elif choice == "2":
                    pick_up_item(current_room)
                 elif choice == "3":
                    drop_item(player_position, current_room)
                 elif choice == "4":
                    check_inventory()
                 elif choice == '5':
                    print('Goodbye!')
                    break
                 else:
                    print('Invalid. Please try again.')
            else:
                print("""
                      What would you like to do?
                      1. Move
                      2. Pick up item
                      3. Drop item
                      4. Check Inventory
                      5.Open Chest
                      6.Exit
                      """)
                choice = input("Choose an option: ")
             
                if choice == "1":
                        player_position = move_player(player_position, current_room)
                elif choice == "2":
                        pick_up_item(current_room)
                elif choice == "3":
                        drop_item(player_position, current_room)
                elif choice == "4":
                        check_inventory()
                elif choice == "5":
                    open_chest()
                elif choice == '6':
                        print('Goodbye!')
                        break
                else:
                    print('Invalid. Please try again.')
                    
main_menu()
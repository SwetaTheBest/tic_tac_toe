

# make grid to display game
def make_grid():
    print(f'''
                   |     |     
              __{game["p1"]}__|__{game["p2"]}__|__{game["p3"]}__
              __{game["p4"]}__|__{game["p5"]}__|__{game["p6"]}__
                {game["p7"]}  |  {game["p8"]}  |  {game["p9"]}  
                   |     |     
                        
                ''')

# make dictionary for places
game = {"p1" : "_", "p2": "_","p3": "_",
        "p4" : "_", "p5": "_","p6": "_",
        "p7" : " ", "p8": " ","p9": " "}

def check_invalid_value(value)-> str:
    if value > 9 or value < 1:
        value = int(input("Please enter a value between 1 to 9 for grid."))
        check_invalid_value(value)
    else:
        print("")
    return str(value)



def check_blank_value(value, turn):
    new_value = check_invalid_value(value)
    place = "p"+new_value
    if game[place] != "X" and game[place] != "0":
            game[place] = turn
            make_grid()
    else:
        new_value = int(input("This place is already taken. Please enter another value: "))
        check_blank_value(new_value,turn)


def check_for_win()-> bool:
    if game["p1"] != "_" and game["p1"] != " " and game["p1"] == game ["p2"] == game["p3"]:
        print(f"**************** {game['p1']} Won!****************")
        return True
    elif game["p4"] != "_" and game["p4"] != " " and game["p4"] == game["p5"] == game["p6"]:
        print(f"**************** {game['p4']} Won!****************")
        return True
    elif game["p7"] != "_" and game["p7"] != " " and game["p7"] == game["p8"] == game["p9"]:
        print(f"**************** {game['p7']} Won!****************")
        return True
    elif game["p1"] != "_" and game["p1"] != " " and game["p1"] == game["p4"] == game["p7"]:
        print(f"**************** {game['p1']} Won!****************")
        return True
    elif game["p2"] != "_" and game["p2"] != " " and game["p2"] == game["p5"] == game["p8"]:
        print(f"**************** {game['p2']} Won!****************")
        return True
    elif game["p3"] != "_" and game["p3"] != " " and game["p3"] == game["p6"] == game["p9"]:
        print(f"**************** {game['p3']} Won!****************")
        return True
    elif game["p1"] != "_" and game["p1"] != " " and game["p1"] == game["p5"] == game["p9"]:
        print(f"**************** {game['p1']} Won!****************")
        return True
    elif game["p7"] != "_" and game["p7"] != " " and game["p7"] == game["p5"] == game["p3"]:
        print(f"**************** {game['p7']} Won!****************")
        return True
    else: 
        return False


for i in range(10):
    if i == 9:
        print('''****************
    It's a Draw.
    GAME OVER
****************
              ''')
        break
    print(f"**************** Turn {i+1}:")
    if i % 2 == 0:
        x_value = int(input("X\'s Turn: Please enter your place: (1 to 9): "))
        check_blank_value(x_value, "X")
        if i >= 4:
            if check_for_win():
                print('''_________________________
    Thanks for playing      
_________________________''')
                break

    else:
        y_value = int(input("0\'s Turn: Please enter your place: (1 to 9): "))
        check_blank_value(y_value,"0")
        if i >= 4:
            if check_for_win():
                print('''_________________________
    Thanks for playing      
 _________________________''')
                break

    





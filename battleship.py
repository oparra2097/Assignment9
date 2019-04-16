
random_row = random.randint(0,4)
    random_column = random.randint(0,4)
    print("Game",g)
    guest_row = int(input("\n\nEnter a row: "))
    guest_column = int(input("\nEnter a column: "))
    
    n = 5
    a = [['.'] * n for i in range(n)]
    
    
    a[guest_row][guest_column] = "*"
    a[random_row][random_column] = '8'
    
    if (guest_row < 5 and guest_column < 5 and guest_row > -1 and guest_column > -1):
        
        if (a[guest_row][guest_column] == a[random_row][random_column]):
            print("You have sunk the battle ship!")
            
        else:
            print("You have failed to sink the battle ship")
            
            for row in a:
                print(' '.join(row))
                
                
            g + 1
                
            if (g < 4):
                battleship(g + 1)
            else: 
                print("Game Over")
    else:    
        print ("You out of range")    
        
        
        
g = 1      
battleship(g)

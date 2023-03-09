
def Is_win(gameboard):
    if(gameboard["0"]!="" and gameboard["0"]==gameboard["1"] 
       and gameboard["1"] == gameboard["2"]):
        return gameboard["0"]
    
    elif (gameboard["3"]!="" and gameboard["3"]==gameboard["4"] 
       and gameboard["4"]==gameboard["5"]):
        return gameboard["3"]
    
    elif (gameboard["6"]!="" and gameboard["6"]==gameboard["7"] 
       and gameboard["7"]==gameboard["8"]):
        return gameboard["6"]
    
    elif (gameboard["0"]!="" and gameboard["0"]==gameboard["3"] 
       and gameboard["3"]==gameboard["6"]):
        return gameboard["0"]
    
    elif (gameboard["1"]!="" and gameboard["1"]==gameboard["4"] 
       and gameboard["4"]==gameboard["7"]):
        return gameboard["1"]
    
    elif (gameboard["2"]!="" and gameboard["2"]==gameboard["5"] 
       and gameboard["5"]==gameboard["8"]):
        return gameboard["2"]
    
    elif (gameboard["0"]!="" and gameboard["0"]==gameboard["4"] 
       and gameboard["4"]==gameboard["8"]):
        return gameboard["0"]
    
    elif (gameboard["2"]!="" and gameboard["2"]==gameboard["4"] 
       and gameboard["4"]==gameboard["6"]):
        return gameboard["2"]
    

    else:
        return None
def Is_draw(gameboard):
    for i in gameboard:
        if gameboard[i] =="":
            return False
    return True        
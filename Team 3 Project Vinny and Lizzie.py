#Vinny and Lizzie
def move(my_score, their_score, my_history, their_history,result):
    if (my_history) == 0:
        return 'c'
    if (their_history[len(their_history)-1]) == 'c':
        return 'c'
    else:
        return 'b'
        



#their_history == "b,c  "
#my_history == "c, 
#len(their_history)"

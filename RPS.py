import random

# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
found_pattern=False
found_pattern_length=1
pattern=[]
recheck_pattern=False
recheck_from=0
last_plays=[]
def player(prev_play, opponent_history=[]):
    global found_pattern,pattern,found_pattern_length
    if prev_play:
        opponent_history.append(prev_play)
    guess = "R"
    if len(opponent_history)>5 and len(opponent_history)<100 and found_pattern==False:
        check_for_pattern(opponent_history[:30])
    else: 
        if(recheck_pattern==True and recheck_from!=0):
            if(len(opponent_history)-recheck_from>30):
                pattern=[]
                check_for_pattern(opponent_history[recheck_from:])
                
    if(found_pattern==False):
        guess=check_for_copy(last_plays,opponent_history)

    if (found_pattern==True):
        guess=oppossite_move(len(opponent_history),opponent_history[-1],[])
    if (found_pattern==False and found_copy==False):
        pick_random()
    return guess




def check_for_pattern(opponent_history):
    global found_pattern, pattern, found_pattern_length,recheck_from

    for i,char in enumerate(opponent_history):
        recheck_from=(len(opponent_history))
        a=opponent_history[:len(opponent_history)//2]
        b=opponent_history[len(opponent_history)//2:]
        if(a==b):
            print('\n\n\n\nOpponent:',opponent_history,'\n\nprima lista', a,'\na doua lista', b)
            found_pattern=True
            found_pattern_length=len(a)
            pattern=a
            return oppossite_move(len(opponent_history),opponent_history[-1],pattern)


def oppossite_move(list_length,prev_play,pat):
    rest=list_length%found_pattern_length
    
    if(prev_play!=pattern[(list_length-1)%found_pattern_length]):
        found_pattern=False
        recheck_from=list_length
    ol =oppossite_letter(pattern[rest])
     

    return ol

def oppossite_letter(letter):
    if(letter=='R'): return 'P'
    if(letter=='P'): return 'S'
    if(letter=='S'): return 'R'

def pick_random():
    return random.choice(('R','P','S'))



found_copy=False

def check_for_copy(last_plays,opponent_history):
    global found_pattern, pattern, found_pattern_length

    for i,char in enumerate(opponent_history):
        
        a=opponent_history[(len(opponent_history)-15):len(opponent_history)]
        b=opponent_history[(len(last_plays)-15):len(last_plays)]
        c=[]
        for ch in b:
            c.append(oppossite_letter(ch))
        if(a==c.reverse()):
            print('\n\n\n\nOpponent:',opponent_history,'\n\nprima lista', a,'\na doua lista', b)
            found_copy=True
            pattern=c.append(a)
            return pattern[0]






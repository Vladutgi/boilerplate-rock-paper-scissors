import random

# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
pattern=[]
last_plays=[]
mrugesh=False
last_move_copy=False
found_abbey=False
current_pattern_type=None
def player(prev_play, opponent_history=[]):
    global pattern,last_plays,last_move_copy,found_abbey,current_pattern_type,mrugesh
    
    if prev_play == "":
        reset_state()
        opponent_history.clear()
        last_plays.clear()
        last_plays=[]
        current_pattern_type=None
        pattern = []


    if prev_play:
        opponent_history.append(prev_play)

    guess = None 
    



    if current_pattern_type and len(last_plays)>30:
        counting=0
        for x in range(1,7):
            if last_plays[-x]==oppossite_letter(opponent_history[-x]):
                counting+=1

        if counting<5:
            
            if current_pattern_type == 'kris':
                last_move_copy = False
            elif current_pattern_type == 'abbey':
                found_abbey = False
            elif current_pattern_type == 'mrugesh':
                mrugesh = False
            elif current_pattern_type == 'quincy':
                pattern=[]
            current_pattern_type = None
            
    #print(current_pattern_type)

    if  len(last_plays) > 30:
        mrugesh_guess= check_for_mrugesh(opponent_history,last_plays)

        if mrugesh_guess:
            guess=mrugesh_guess
            last_plays.append(guess)
            current_pattern_type='mrugesh'
            return guess

    if not pattern :
        check_for_pattern(opponent_history[-30:])

        
    if pattern:
        rest=len(opponent_history)%len(pattern)

        if opponent_history[-1]!=pattern[(len(opponent_history)-1)%len(pattern)]:
            pattern=[]

        else:
            guess=oppossite_letter(pattern[rest])
            last_plays.append(guess)
            current_pattern_type='quincy'
            return guess
    


    if not last_move_copy:
        check_for_last_move_copying(opponent_history[-30:],last_plays[-30:])


    if last_move_copy and len(last_plays) > 30:
        if  opponent_history[-1] == oppossite_letter(last_plays[-2]):

            guess= oppossite_letter(last_plays[-1])

            last_plays.append(guess)
            current_pattern_type='kris'
            return guess






    
    if len(last_plays) >= 30:
        abbey_guess = check_for_abbey(last_plays[-30:], opponent_history[-30:])
        if abbey_guess:
            guess = abbey_guess
            last_plays.append(guess)
            current_pattern_type = 'abbey'
            return guess

    
   
    if guess is None:
        if len(opponent_history) > 0:
            guess = oppossite_letter(opponent_history[-1])  
        else:
            guess = 'S'
        last_plays.append(guess)
    return guess





def check_for_pattern(opponent_history): #for quincy
    global pattern
    if len(opponent_history)<10:    return None
    max_pattern=[]
    max_legth=len(opponent_history)//2


    for j in range(6,max_legth+1):

        part1 = opponent_history[-2 * j:-j]
        part2 = opponent_history[-j:]
        if part1 == part2:
            max_pattern = part1
    if max_pattern:
        pattern = max_pattern

def reset_state():
    global found_abbey,mrugesh,last_move_copy,current_pattern_type,pattern
    
    found_abbey=False
    mrugesh=False
    last_move_copy=False
    current_pattern_type=None
    pattern.clear()
    


def oppossite_letter(letter):
    if(letter=='R'): return 'P'
    if(letter=='P'): return 'S'
    if(letter=='S'): return 'R'






        


def remaining_option(not_those):
    options=['S','P','R']
    for item in not_those:
        if item in options:
            options.remove(item)

    return options[0] if options else None




def check_for_last_move_copying(oh,lp):
    global last_move_copy
    if len(oh) > 1 and len(lp) > 1:
        for length in range(5, 11):  
            if oh[-length+1:] == lp[-length:-1]:
                last_move_copy = True



def check_for_abbey(my_history, opponent_history):
    global found_abbey

    if len(opponent_history) < 3:
        return None

    play_order = {
        "RR": {'R': 0, 'P': 0, 'S': 0},
        "RP": {'R': 0, 'P': 0, 'S': 0},
        "RS": {'R': 0, 'P': 0, 'S': 0},
        "PR": {'R': 0, 'P': 0, 'S': 0},
        "PP": {'R': 0, 'P': 0, 'S': 0},
        "PS": {'R': 0, 'P': 0, 'S': 0},
        "SR": {'R': 0, 'P': 0, 'S': 0},
        "SP": {'R': 0, 'P': 0, 'S': 0},
        "SS": {'R': 0, 'P': 0, 'S': 0},
    }

    for i in range(len(my_history) - 2):
        prev = my_history[i] + my_history[i + 1]
        move = opponent_history[i + 2]
        if prev in play_order:
            play_order[prev][move] += 1

    key = my_history[-2] + my_history[-1]
    if key in play_order:
        prediction = max(play_order[key], key=play_order[key].get)
        found_abbey = True
        return oppossite_letter(prediction)

    return None






def check_for_mrugesh(oh,lp):
    global mrugesh

    if(len(oh)<25 or len(lp)<15):
        return None

    count=0

    
    for i in range(1,11):
        my_most = max(set(lp[-10-i:-i]), key=lp[-10-i:-i].count)
        if oppossite_letter(my_most) == oh[-i]:
            count += 1

    if count>=9:

        mrugesh = True
        most_frequent = max(set(lp[-10:]), key=lp[-10:].count)
        predicted_mrugesh_move = oppossite_letter(most_frequent)
        guess = oppossite_letter(predicted_mrugesh_move)
    
        return guess
    else: return None



def pick_random():
    return random.choice(('R','P','S'))
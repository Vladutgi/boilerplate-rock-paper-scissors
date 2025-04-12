import random

# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
found_pattern=False
found_pattern_length=1
pattern=[]
recheck_pattern=False
recheck_from=0
last_plays=[]
found_copy=False
found_x_copy=False
delay=None
last_move_copy=False
def player(prev_play, opponent_history=[]):
    global found_pattern, pattern, found_pattern_length, last_plays, found_copy, recheck_pattern, recheck_from,found_x_copy,delay,last_move_copy

    if prev_play:
        opponent_history.append(prev_play)

    guess = None 
    

    if found_copy:
        found_pattern=False
        found_x_copy=False
        last_move_copy=False
        guess=check_for_copy(last_plays,opponent_history)

        if guess:
            last_plays.append(guess)
            return guess

        else:
            found_copy=False

    if found_pattern:
        found_copy=False
        found_x_copy=False
        last_move_copy=False
        guess=oppossite_move(opponent_history)
        
        if guess:
            last_plays.append(guess)
            return guess
        else:
            found_pattern=False
    

    if found_x_copy:
        found_pattern=False
        found_copy=False
        last_move_copy=False
        if delay is not None:
            guess = opponent_history[-delay]
            if guess:
                last_plays.append(guess)
                return guess
        
            else:
                found_x_copy=False


    if last_move_copy:
        found_pattern=False
        found_copy=False
        found_x_copy=False
        guess= remaining_option([last_plays[-1],oppossite_letter(last_plays[-1])])
        last_plays.append(guess)
        return guess
        

    if 5 < len(opponent_history)<31 and not found_pattern:
        check_for_pattern(opponent_history[:30])

    
    if len(opponent_history)>=31:
        if not pattern:
            check_for_pattern(opponent_history[-30:])
            check_for_copy(last_plays,opponent_history)
            last_move_copying(opponent_history[-30:],last_plays[-30:])
        if(recheck_pattern and recheck_from!=0 and len(opponent_history) - recheck_from > 30):
            pattern=[]

            check_for_pattern(opponent_history[-30:])
            check_for_copy(last_plays,opponent_history)
            last_move_copying(opponent_history[-30:],last_plays[-30:])
                
    

    if not guess:
        if len(last_plays)>5:
            guess = for_mrugesh(last_plays)
        else: guess=pick_random
        last_plays.append(guess)
    
    return guess





def check_for_pattern(opponent_history):
    
    global found_pattern, pattern, found_pattern_length, recheck_from, recheck_pattern

    half=len(opponent_history)//2
    
    a=opponent_history[:half]
    b=opponent_history[half:]
    if(a==b and a):
            found_pattern=True
            pattern=a
            found_pattern_length=len(a)
            recheck_pattern=False
            recheck_from = len(opponent_history)
            #print('\n\n\n\nOpponent:',opponent_history,'\n\nprima lista', a,'\na doua lista', b)


def oppossite_move(opponent_history):
    global pattern, found_pattern, found_pattern_length
    global recheck_pattern, recheck_from

    if not pattern or not found_pattern_length:
        return None

    rest=len(opponent_history)%found_pattern_length
    
    expected = pattern[rest]
    lp= opponent_history[-1]
    if lp!=pattern[(len(opponent_history)-1)%found_pattern_length]:
        found_pattern=False
        pattern=[]
        recheck_pattern=True
        recheck_from=len(opponent_history)
        return None
    return oppossite_letter(expected)

def oppossite_letter(letter):
    if(letter=='R'): return 'P'
    if(letter=='P'): return 'S'
    if(letter=='S'): return 'R'

def pick_random():
    return random.choice(('R','P','S'))




def check_for_copy(lp,oh):
    global found_copy, pattern

    if len(lp)<15 and len(oh)<15:
        return None
    oh_length=len(oh)
    
    a=oh[-10:]
    b=oh[-30:-15]

    if(a==b):
        found_copy=True
        pattern=a+b
        #print(f"Found copy pattern: {a} | My last plays: {b}")

        return oppossite_letter(pattern[oh_length%len(pattern)])



def check_for_x_move_copy(oh,lp):
    global found_x_copy
    max_delay=min(20,len(lp)-5)
    possible_delays = []


    for delay in range(1,max_delay+1): 
        

        for i in range(5,len(oh) - delay ):

            lp_slice=lp[-i-delay:-i]
            oh_slice=oh[-i-5:-i]
            if lp_slice == oh_slice:

                #print(f'Found copy: opponent copying with delay {delay}')
                possible_delays.append(delay)
                break
            #else: print('No pattern was found')
    if possible_delays:
        found_x_copy=True
        delay= max(set(possible_delays), key=possible_delays.count)
        return delay
    return None


def last_move_copying(oh,lp):
    global last_move_copy
    if len(oh) > 1 and len(lp) > 1:

        for length in range(5, 11):  

            if oh[-length+1:] == lp[-length:-1]:
                print('last_move_copy')  
                last_move_copy = True
                return  

        
def for_mrugesh(lp):
    return oppossite_letter(lp[-2])

def remaining_option(not_those):
    options=['S','P','R']
    for item in not_those:
        if item in options:
            options.remove(item)
    #print('not_those', not_those)
    #print(options[0])
    return options[0] if options else None



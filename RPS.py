import random

# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
found_pattern=False
found_pattern_length=1
pattern=[]
recheck_pattern=False
recheck_from=0
last_plays=[]
found_copy=False

def player(prev_play, opponent_history=[]):
    global found_pattern,pattern,found_pattern_length,last_plays,found_copy
    if prev_play:
        opponent_history.append(prev_play)
    guess = "R"
    if len(opponent_history)>5 and len(opponent_history)<31 and found_pattern==False:
        check_for_pattern(opponent_history[:30])

    else: 
        if (len(opponent_history)>=31 and pattern==[]):
            check_for_pattern(opponent_history[recheck_from:])
            check_for_copy(last_plays,opponent_history,len(opponent_history))

        if(recheck_pattern==True and recheck_from!=0):
            if(len(opponent_history)-recheck_from>30):
                pattern=[]

                if(len(opponent_history)>20):
                    check_for_pattern(opponent_history[recheck_from:])
                    check_for_copy(last_plays,opponent_history,len(opponent_history))
                
    if(found_copy==True):
        found_pattern=False
        found_pattern_length=0
        guess=check_for_copy(last_plays,opponent_history,len(opponent_history))

        if(last_plays[-1]!=oppossite_letter(opponent_history[-1])):
            found_copy=False

    if (found_pattern==True):
        found_copy=False
        guess=oppossite_move(len(opponent_history),opponent_history[-1])
        
        return guess

    if (found_pattern==False and found_copy==False and len(opponent_history)>20):
        copy_guess = check_for_copy(last_plays,opponent_history,len(opponent_history))
        if copy_guess:
            guess=copy_guess
        else: 
            pick_random()
    if guess==None:
        guess=pick_random()

    last_plays.append(guess)
    
    return guess





def check_for_pattern(opponent_history):
    global found_pattern, pattern, found_pattern_length,recheck_from,recheck_pattern

    for i,char in enumerate(opponent_history):
        recheck_from=(len(opponent_history))
        a=opponent_history[:len(opponent_history)//2]
        b=opponent_history[len(opponent_history)//2:]
        if(a==b):
            print('\n\n\n\nOpponent:',opponent_history,'\n\nprima lista', a,'\na doua lista', b)
            found_pattern=True
            found_pattern_length=len(a)
            recheck_pattern=False
            pattern=a
            return oppossite_move(len(opponent_history),opponent_history[-1])
    if pattern==[] :
        check_for_x_move_copy(opponent_history[:30],last_plays)

def oppossite_move(list_length,prev_play):
    global pattern
    if( pattern==[]):
        return pick_random()
    rest=list_length%found_pattern_length
    
    ol =oppossite_letter(pattern[rest])
    if(prev_play!=pattern[(list_length-1)%found_pattern_length]):
        found_pattern=False
        recheck_from=list_length
        recheck_pattern=True
        pattern=[]

    return ol

def oppossite_letter(letter):
    if(letter=='R'): return 'P'
    if(letter=='P'): return 'S'
    if(letter=='S'): return 'R'

def pick_random():
    return random.choice(('R','P','S'))




def check_for_copy(lp,oh,oh_length):
    global found_pattern, pattern, found_pattern_length,found_copy

    #check_for_x_move_copy(oh[:30],lp[:30])

    for i,char in enumerate(oh):
        
        a=oh[(len(oh)-15):len(oh)]
        b=oh[(len(lp)-30):(len(lp)-15)]


        c=[]
        for ch in b:
            c.append(oppossite_letter(ch))
        if(a==b):
           # print('\n\n\n\nOpponent:',oh,'\n\nprima lista copiata', a,'\na doua lista copiata', b)
            found_copy=True
            pattern=a+c
            return pattern[oh_length%len(a+b)]



def check_for_x_move_copy(oh,lp):
    max_delay=min(20,len(lp)-5)
    for delay in range(1,max_delay+1):

        for i in range(1,min(len(oh),len(lp)-delay-5)+1):

            lp_slice=lp[-i-delay-5:-i-delay]
            oh_slice=oh[-i-5:-i-1]
            if lp_slice == oh_slice:

                print(f'Found copy: opponent copying with delay {delay}')
                return

x = ['R', 'P', 'S', 'R', 'P', 'S', 'R', 'P', 'S', 'R', 'P', 'S', 'R', 'P', 'S']
y = ['P', 'S', 'R', 'P', 'S', 'R', 'P', 'S', 'R', 'P', 'S', 'R', 'P', 'S', 'R']

check_for_x_move_copy(x, y)

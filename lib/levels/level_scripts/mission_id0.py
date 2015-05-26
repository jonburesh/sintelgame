#NEEDS RE-CODE
import bge

def main():
	cont = bge.logic.getCurrentController()
	own = cont.owner
	
	w_key = cont.sensors['w_key'].positive
	flag_one_got = cont.sensors['flag_one_got'].positive
	flag_two_got = cont.sensors['flag_two_got'].positive
	shift_key = cont.sensors['shift_key'].positive
	left_click = cont.sensors['left_click'].positive
	dummy_dead = cont.sensors['dummy_dead'].positive
	
	g_voice_1 = cont.actuators['g_voice_1']
	g_voice_2 = cont.actuators['g_voice_2']
	g_voice_3 = cont.actuators['g_voice_3']
	g_voice_4 = cont.actuators['g_voice_4']
	g_voice_5 = cont.actuators['g_voice_5']
	g_voice_6 = cont.actuators['g_voice_6']
	g_voice_7 = cont.actuators['g_voice_7']
	g_voice_8 = cont.actuators['g_voice_8']
	g_voice_9 = cont.actuators['g_voice_9']
	g_voice_10 = cont.actuators['g_voice_10']
	
	one_mess = cont.actuators['1_mess']
	two_mess = cont.actuators['2_mess']
	flag_one = cont.actuators['flag_one']
	three_mess = cont.actuators['3_mess']
	four_mess = cont.actuators['4_mess']
	five_mess = cont.actuators['5_mess']
	six_mess = cont.actuators['6_mess']
	flag_two = cont.actuators['flag_two']
	seven_mess = cont.actuators['7_mess']
	eight_mess = cont.actuators['8_mess']
	nine_mess = cont.actuators['9_mess']
	dummy_s = cont.actuators['dummy_s']
	ten_mess = cont.actuators['10_mess']
	eleven_mess = cont.actuators['11_mess']
	end_tut = cont.actuators['end_tut']
	lock_mess = cont.actuators['lock_mess']
	
	own['timer']+=1
	
	if own['goal']==0:
		if own['sent']!=1:
			if own['timer']>=50:
				cont.activate(one_mess)
				cont.activate(g_voice_1)
				own['sent']=1
		if w_key:
			own['sent']=0
			own['timer']=0
			own['goal']=1
	
	if own['goal']==1:
		if own['sent']!=1:
			if own['timer']>=50:
				cont.activate(two_mess)
				cont.activate(g_voice_2)
				cont.activate(flag_one)
				own['sent']=1
		if flag_one_got:
			own['sent']=0
			own['timer']=0
			own['goal']=2
	
	if own['goal']==2:
		if own['sent']!=1:
			cont.activate(three_mess)
			cont.activate(g_voice_3)
			own['sent']=0
			own['timer']=0
			own['goal']=3
	
	if own['goal']==3:
		if own['timer']>=200:
			if own['sent']!=1:
				cont.activate(four_mess)
				own['sent']=1
		if own['timer']>=400:
			own['sent']=0
			own['timer']=0
			own['goal']=4
	
	if own['goal']==4:
		if own['sent']!=1:
			if own['timer']>=50:
				cont.activate(five_mess)
				cont.activate(g_voice_4)
				own['sent']=0
				own['timer']=0
				own['goal']=5
	
	if own['goal']==5:

		if shift_key:
			own['sent']=0
			own['goal']=6
	
	if own['goal']==6:
		if own['sent']!=1:
			if own['timer']>=175:
				own['sent']=1
				cont.activate(flag_two)
				cont.activate(six_mess)
				cont.activate(g_voice_5)
		if flag_two_got:
			own['sent']=0
			own['timer']=0
			own['goal']=7
	
	if own['goal']==7:
		if own['sent']!=1:
			own['sent']=1
			cont.activate(seven_mess)
			cont.activate(g_voice_6)
		if own['timer']>=250:
			own['sent']=0
			own['timer']=0
			own['goal']=8
	
	if own['goal']==8:
		if own['sent']!=1:
			cont.activate(eight_mess)
			cont.activate(g_voice_7)
			own['sent']=1
		if left_click:
			own['sent']=0
			own['timer']=0
			own['goal']=9
	
	if own['goal']==9:
		if own['sent']!=1:
			if own['timer']>=150:
				own['sent']=1
				cont.activate(dummy_s)
				cont.activate(nine_mess)
				cont.activate(g_voice_8)
		if own['timer']>=365:
			own['sent']=0
			own['timer']=0
			own['goal']=10
	
	if own['goal']==10:
		if own['sent']!=1:
			cont.activate(ten_mess)
			cont.activate(g_voice_9)
			cont.activate(lock_mess)
			own['sent']=1
		if dummy_dead:
			own['sent']=0
			own['timer']=0
			own['goal']=11
	
	if own['goal']==11:
		if own['sent']!=1:
			cont.activate(eleven_mess)
			cont.activate(g_voice_10)
			own['timer']=0
			own['sent']=1
		if own['timer']>=150:
			cont.activate(end_tut)
			own['timer']=0
			own['goal']=12
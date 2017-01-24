import time
import random
import webbrowser
total_breaks = 0
break_count = 0
print("Work break program started: " + time.ctime())
while(break_count < total_breaks):
	time.sleep(60 * 30)
	song_list = ["https://www.youtube.com/watch?v=U4U19zwFENs","https://www.youtube.com/watch?v=A_ulZiob5I0","https://www.youtube.com/watch?v=9CBBYCkxHns","https://www.youtube.com/watch?v=XUjAtYQkFm8","https://www.youtube.com/watch?v=6XJBDX3Z0BY","https://www.youtube.com/watch?v=mehLx_Fjv_c","https://www.youtube.com/watch?v=xkj3HO6t8O4","https://www.youtube.com/watch?v=Ml6P_pB9hII","https://www.youtube.com/watch?v=EMxNGnfV9Xs","https://www.youtube.com/watch?v=yKNxeF4KMsY"]
	webbrowser.open(random.choice(song_list))
	break_count = break_count + 1 
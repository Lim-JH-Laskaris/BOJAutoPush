solution = lambda x,y=0,z=0 : solution((x+y)//10,(x+y)%10,z+(x+y)//10) if (x+y)//10 > 0 else z 
a,b,v = map(int,input().split())
print((v-b)//(a-b) if (v-b)%(a-b)==0 else (v-b)//(a-b)+1)
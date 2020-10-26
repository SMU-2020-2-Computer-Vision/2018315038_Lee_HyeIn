import numpy as np

a = np.arange(10,30,5)
print(a)

b = np.arange(0,2,0.3)
print(b) # 0부터 2인데 2포함x, 0.3간격으로 출력

c = np.linspace(0,2,9)
print(c) #0부터 2포함까지 일정간격 9개 출력

x = np.linspace(0,2*np.pi, 100)
f = np.sin(x)



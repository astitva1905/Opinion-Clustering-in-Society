import pygame
import math
import sys
import random
#timestep function
def timestep(a):
	c=0
	for i in range(n):
		for j in range(n):
			on = 0
			ze = 0
			if i!=n-1 and j!=n-1:
				if a[i-1][j-1]==0:
					ze+=1
				else:
					on+=1
				if a[i][j-1]==0:
					ze+=1
				else:
					on+=1
				if a[i+1][j-1]==0:
					ze+=1
				else:
					on+=1
				if a[i+1][j]==0:
					ze+=1
				else:
					on+=1
				if a[i+1][j+1]==0:
					ze+=1
				else:
					on+=1
				if a[i][j+1]==0:
					ze+=1
				else:
					on+=1
				if a[i-1][j+1]==0:
					ze+=1
				else:
					on+=1
				if a[i-1][j]==0:
					ze+=1
				else:
					on+=1
			elif i==n-1 and j!=n-1:
				if a[i-1][j-1]==0:
					ze+=1
				else:
					on+=1
				if a[i][j-1]==0:
					ze+=1
				else:
					on+=1
				if a[0][j-1]==0:
					ze+=1
				else:
					on+=1
				if a[0][j]==0:
					ze+=1
				else:
					on+=1
				if a[0][j+1]==0:
					ze+=1
				else:
					on+=1
				if a[i][j+1]==0:
					ze+=1
				else:
					on+=1
				if a[i-1][j+1]==0:
					ze+=1
				else:
					on+=1
				if a[i-1][j]==0:
					ze+=1
				else:
					on+=1
			elif i!=n-1 and j==n-1:
				if a[i-1][j-1]==0:
					ze+=1
				else:
					on+=1
				if a[i][j-1]==0:
					ze+=1
				else:
					on+=1
				if a[i+1][j-1]==0:
					ze+=1
				else:
					on+=1
				if a[i+1][j]==0:
					ze+=1
				else:
					on+=1
				if a[i+1][0]==0:
					ze+=1
				else:
					on+=1
				if a[i][0]==0:
					ze+=1
				else:
					on+=1
				if a[i-1][0]==0:
					ze+=1
				else:
					on+=1
				if a[i-1][j]==0:
					ze+=1
				else:
					on+=1
			elif i==n-1 and j==n-1:
				if a[i-1][j-1]==0:
					ze+=1
				else:
					on+=1
				if a[i][j-1]==0:
					ze+=1
				else:
					on+=1
				if a[0][j-1]==0:
					ze+=1
				else:
					on+=1
				if a[0][j]==0:
					ze+=1
				else:
					on+=1
				if a[0][0]==0:
					ze+=1
				else:
					on+=1
				if a[i][0]==0:
					ze+=1
				else:
					on+=1
				if a[i-1][0]==0:
					ze+=1
				else:
					on+=1
				if a[i-1][j]==0:
					ze+=1
				else:
					on+=1
			if on>4:
				a[i][j]=1
			elif ze>4:
				a[i][j]=0
			else:
				pass
	return a

#width and color globals
width = 600
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)

#initial map
a = []
n = int(input("Input the number of rows"))
for i in range(n):
	b = []
	for j in range(n):
		b.append(random.randint(0,1))
	a.append(b)

#square size
sq = int(width/n)

#pygame grid maker
def drgrid(a):
	for i in range(len(a)):
		for j in range(len(a)):
			if a[i][j]==0:
				pygame.draw.rect(screen,blue, (j*sq, i*sq,sq,sq),0)
			elif a[i][j]==1:
				pygame.draw.rect(screen,green, (j*sq, i*sq,sq,sq),0)

#pygame starter
pygame.init() 

#pygame display
screen = pygame.display.set_mode((width,width))

#calling grid maker function
drgrid(a)

#updating pygame display i.e. map
pygame.display.update()

#timesteps
t = int(input("Input the number of timesteps "))



#additional timesteps
c = int(input("Input additional steps "))



run = True
c = 0
while run:
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if c==0:
				print("1.")
				for i in range(t):
					a = timestep(a)
					drgrid(a)
					pygame.display.update()
					if i<=3:
						pygame.time.delay(250)
					elif i <=10:
						pygame.time.delay(150)
				pygame.display.update()
				c+=1
			elif c==1:
				print("2.")
				for i in range(c):
					a = timestep(a)
					drgrid(a)
					pygame.display.update()
					if i<=10:
						pygame.time.delay(50)
				pygame.display.update()
				c+=1
			elif c==2:
				print("The program is over.\n Please click X in the top right to quit")	
				
				#for i in a:
				#	print(*i)
		if event.type == pygame.MOUSEMOTION:
			pass
			

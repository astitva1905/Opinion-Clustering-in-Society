# Opinion-Clustering-in-Society

## A project in Social Psychology 

Hey Everyone, So I took an introductory course in Social Psychology in college, and it was an amazing course with an amazing teacher.<br>
We had to submit a term paper by the end of the course, and all I need is a opening to add coding to my projects 😂. <br>
So, while going through ideas that we could do the term paper on, not only did we decide upon an amazing topic to tackle in Social psychology, I found my opening to add code in it <br>
<br>
So the idea I had to add code in my project wasn't original at all, I found it while researching for this project on this online course site: <br> 
[Cellular automata to study social self-organisation](https://www.futurelearn.com/courses/complexity-and-uncertainty/9/todo/97429) <br>
The site is called Future Learn and they have a lot of great courses, I found it while researching for this project and it helped, so definitely check it out! <br><br>

Our term paper was about Social Psychology in Voting Behaviour. <br>
Now, an important point in Voting behaviour (as well as general preferential behaviour of humans) is opinion clustering. 
Our entire term paper had many points about the topic, but the simulation that I coded up dealt mainly with opinion clustering. 

### What's Opinion CLustering now ? 
Oka so, opinion clustering is basically a pattern that emerges in the Society as a whole, when individuals of the society interact with each other. <br>
Clustering is basically a similarity of opinion in a local region, but many diverse opinions in the global scale. <br>
So basically, you and your close friends, parents, close family may have similar opinions about many things. The same would be the case for someone else who you dont directly know at all. <br>
But your opinions, and that other persons opinions might be different. So in your local region (you with your close friends and family) has the similar prevelant opinions and his/her local region also has similar prevelant opinions, but both these opinions may be different among themselves. <br>
Thus in the entire society there may be many "groups" or clusters that have same opinions among them, but in the global scale all these clusters may have different opinions with respect to each other. <br>

### Okay, but where's the simulation at?
So the idea for the simulation is to replicate opinion clustering in society in a very simple setting. <br>
We take two political parties, Green and Blue, and each and every person supports either Green or Blue. <br>
We start off with a random map, with every person in it having a randomly assigned opinion of either Blue of Green. <br> 
We then use a very important rule, that is actually one of the causes of clutering ( Local social influence ). <br>
For the purposes of our simulation, this local social influence rule is simple. If the majority of people around you support a specific Party but you don't, you'll switch to supporting that party eventually <br>
So using this preset we design a simulation, and run it for some amount of time, to see that this random map of opinions has actually transformed into geographical clusters of opinions! <br>

### The Simulation ( Using 2D Cellular automata)

1. The entire map of the cellular automata represents our defined “world”. 
2. Each cell in the map defines a location where exactly 1 person lives. 
3. Each cell contains a value (represented using a color) that defines the person’s political beliefs.
For simplicity we can assume that this represents which political party they favor.
4. Each cell’s neighborhood is a Moore neighborhood i.e. the 8 cells around this cell.
This neighborhood is the place where the local social influence rule defined before works i.e. the people around you are only the 8 people in the 8 cells around your cell.
5. A toroid geometry is followed i.e. the cells on the top most and bottom most row are
considered neighbors and so are the cells on the left most and right most columns. This is
shown below in the figure. This is how we visualize our grid of cells to be structured.
6. Each cell’s political belief is influenced by the beliefs of its neighborhood
7. A cell changes its existing political belief in a timestep if and only if majority of cells in its
neighborhood have different beliefs. The cells new belief is then the same as the belief of the
majority of the cells in its neighborhood. 

### What it looks like

See the following two photos of the simulation, one is the starting map and the other is the after a considerable amount of timesteps. <br>
The starting map is random, it has people (living in the cells) that randomly believe in either the Green party or the Blue party. <br>
People change their opinions because of the direct social influence by people around them, and After a few timesteps, we see the opinion clustering. <br>

![Image1]()<br><br>
![Image2]()<br>

### Instructions to use the simulation:

1. Install python on your computer. -> https://www.python.org/downloads/
2. After installing python, go to your command prompt on windows (Search CMD in your search bar) 
3. In your command prompt, write the command - pip install pygame
4. Download the file Grid.py onto your Desktop folder
5. After downloading, go to command prompt and type - cd Desktop 
6. Then on the command prompt type - python Grid.py
7. The simulation is now active!
8. To use the simulation, type the desired number of rows in the command prompt when asked for this and hit enter. (Keep it below 130)
9. When asked for number of timesteps type in 500  and hit enter
10. When asked for additional timesteps write 100 and hit enter.
11. Now click in the center of the pygame window. The simulation should start. 
12. Click again to complete the simulation's additional timesteps.
13. On your 3rd click you should see the command prompt saying that the simulation is now over. 
14. Then click the X button of the pygame window to close it. 
<br>
P.S. - Don't worry if the pygame window says Not Responding, it does that if nothing is changing after some timesteps, which is expected after enough number of timesteps. <br>
Don't press quit, it'll keep working normally and the Not Responding sign goes away once it's done with all the timesteps!

### Conclusion

So that was it, we saw a simulation that demonstrates geographical opinion clustering in societies in the context of Voting Behaviour. If you want a real life example of this, think about the Red and Blue states of USA. Crazy, right ?


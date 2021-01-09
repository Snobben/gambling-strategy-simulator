## Welcome to my humble first pages blogpost!

In this project i have attempted to find the best risk-averse strategy for betting in a dice game where you win if the sum of your six rolled dice are higher than your opponents sum. What tempted me to this project was the fact that this game was implemented in an online video game with a special rule; namely that the player who first posted the bet for anyone to accept, won if the sum of the dices were equal. I realized that the expected value for player one were in fact positive, and it got me interested in finding the best strategy such that one could potentially earn a practically infinite amount of money - But mostly im doing this project to practice my python skills, and for entering the world of github and blogpages with a cute and interesting problem. I do think my findings where somewhat interesting, even though they were quite predictible if one gives some thought to the problem.


### Introduction to rules
The rules of the game are very straightforward:
- One player decides an amount to bet.
- Any other player can choose to enter into the bet for the amount set by player 1.
- Both players roll six dice, and the player with the highest sum wins. 
- If equal, player one, whom chose the bet size, wins. 
- The payout is 1.98 times the betsize.

### Expected value and some notes
Because of the fact that player one wins when the sums of dice are equal, his chance of winning the bet is about 53%, and his expected value is about 5% more than his bet. See the link [here](https://docs.google.com/spreadsheets/d/e/2PACX-1vRZcc7A6GpOF1pE0yLyRiQKSyRzkLK1YklM5ddor0bcZwLMjOf5fOvdxAbyp50GCsaDNBXjDuu8xfOk/pubhtml) for my calculations showing these results. Note that this expected value is per bet. If one instead were to bet a thousand times, the expected value is (1.05)^1000. This is an astronomical value, and my calculated averages from my simulations were never close to that high. This can be explained by the fact that the expected return gets inflated by the very improbable edge cases where one wins close to every time. If i had ran simulations with millions of runs, it would be more likely to observe such edge cases.

### Code
If you want to check out my code for a better understanding, please do. Here i will simply explain the main flow of the program: First, i generate six random numbers and compare the sum of these. This simulates the dice-throwing. Then i compare the sums, and conclude that player one wins if his sum is equal or higher. Then i created functions for deciding how many times this dice throwing and sum comparisons shall be done. On the basis of the recorded score of all dice throws, i calculate the resulting money player one ends up with. These series of bets and resulting money is repeated and recorded in a strategy tester function, for a specified number of runs. To compare strategies, i wrote functions for simulating and plotting multiple strategies with different bet sizes. My code has not been optimized for better run time yet, but i will probably look into it in the future. Please comment if you do notice simple ways to optimize.
### Plots and analysis
The first thing i was interested in was getting a feel for how the simulations behaved, and so i did not put too many bets and number of runs in the script to reduce run time. The y axis is money earned where 1 is the initial amount, and each x on the x axis represents a given sequence of bets with the given strategy. The bet size is incremented to the right, such that plot two has betsize equal to the original bet size increment 0.05 + an additional 0.05. The next has 0.05 + 2x0.05 and so forth.
Plot one inputs: 100 runs, 100 bets, 0.05 bet size increment, 9 strategies.  
![Plot one](https://raw.githubusercontent.com/Snobben/gambling-strategy-simulator/gh-pages/Plots%20and%20stats%20for%20gambling-strategy-simulator/plot1-logfalse.png)  

We already see how much riskier the higher betsize strategies are - Almost none of the runs with high betting sizes are profitable, although the few successful runs are very profitable. Since it is quite hard to see the average and initial money lines in this plot, i will plot the same and all consequent simulations using log scale to easier comprehend the plots.

![Plot one log](https://raw.githubusercontent.com/Snobben/gambling-strategy-simulator/gh-pages/Plots%20and%20stats%20for%20gambling-strategy-simulator/plot1-gambling-strategy-simulator.png)  

With log scale enabled, it becomes much clearer how the high risk strategies loses money most of the time, but really pays off sometimes. For clutter considerations, all tables of statistics belonging to the simulations can be found [here.](https://docs.google.com/spreadsheets/d/e/2PACX-1vRm0mpG-dfmNisu60bSiYNpGngs8tkqWbav9yClnjI36PVNMLLdlqSEx6FczNmVJaouz3_PxUH9dRVH/pubhtml) In the first table of stats, titled plot 1,  we can spot that the average payoff is clearly higher for high risk strategies, but the lowest are also severely smaller. In my opinion, the fact that one loses almost always with high risk strategies points to having a quite low bet size. Therefore, in the next plot, i have reduced the bet size increment to 0.01, and with sixteen strategies we will see the more "zoomed in" betting range from 0.01 to 0.16. I have increased the number of bets since the small betting size probably requires a lot of bets to be highly profitable. Do note that i will not try having more than 10 000 bets in a simulations because the point of this project is partly based on my aspiration to get rich in a video game by posting bets; i do not have the time or will to place a million bets. In a more real world application of this, venture capitalists will not be able to place capital in millions of risky start ups - One is limited in how many "bets" one is able to place.
Plot two inputs:
100 runs, 1000 bets, 0.01 bet size increment, 16 strategies. By increasing the amount of bets, we expect a higher return on all strategies since the amount invested is higher.

Plot two:
![Plot two](https://raw.githubusercontent.com/Snobben/gambling-strategy-simulator/gh-pages/Plots%20and%20stats%20for%20gambling-strategy-simulator/plot2log.png)

Here we can observe that the lowest risk strategies actually almost avoids loss. Unfortunately these low risk strategy also give us quite small returns, compared to the slightly more risky strategies. Since we increased the times to bet tenfold, we observe big increases in average returns across the bord. (23x return for the 5% strategy vs 1.3x for the five percent strategy in the previous plot, with only 100 times to bet.) From the stats sheet, plot 2, we can also see how all strategies with a betsize over 7% has a lower quartile value of less than the initial money value 1. Therefore, in my next plot, i will make an even more fine-grained picture by reducing the bet size increment to 0.5%. With sixteen strategies, the max is thus 8%, and we avoid the untolerably high risk strategies identified.

Plot three inputs:nums_of_runs = 100, times_to_bet = 1000, initial_money = 1, betsize_percentage = 0.005, nums_of_strategies = 16

Plot three:
![Plot 3](https://raw.githubusercontent.com/Snobben/gambling-strategy-simulator/gh-pages/Plots%20and%20stats%20for%20gambling-strategy-simulator/plot3log.png)

This doesn't really give us any new information, except more fine-grained view of the behaviour of the different strategies such that one can choose one that fits a given risk profile. We do observe that the numbers have changed quite a bit from the previous simulation for the same inputs, showing how much variability and uncertainty is ingrained in these kinds of gambling games. For my next and final plot, i decided to increase number of runs to 1000, such that we can get a better look at the variability present. Also, i have upped the times to bet tenfold again, to 10000, to really show how powerful exponential growth can be. I have capped the bet size at 6% because it seems obvious that any higher is too risky for any agent, even quite risk-neutral ones. 


Plot 4 inputs: nums_of_runs = 1000, times_to_bet = 10000, initial_money = 1, betsize_percentage = 0.005, nums_of_strategies = 12

Plot four:
![Plot four](https://raw.githubusercontent.com/Snobben/gambling-strategy-simulator/gh-pages/Plots%20and%20stats%20for%20gambling-strategy-simulator/plot-four.png)

First of all, the plots have become quite unreadable because of the number of runs, but we do manage to see that the average returns are massive, and increasing with the bet size increment. However, looking at 95% low and minimum value, we can observe that it is actually 4% and 3% respectively who have the best/highest values. And so i conclude that the optimal bet size given a healthy risk aversion, is in the 3-4% range. 

### Notes on methods for deciding the optimal strategy
For a risk neutral agent, maximizing average return is the goal function. Therefore, a higher betsize will always be preferred, and therefore this project would never have any thing to uncover.
For a risk-averse agent, the picture gets more complicated. It becomes a question of what level of risk one is willing to tolerate for certain returns. 
I have in this project decided to simply mathematically formulate what i feel like best represents my risk tolerance facing this betting problem (with minimum and 95% low thresholds.
I will when i get time try to implement a prospect theory value system for deciding the betting strategy, in which the preferance/value function is more intricate in how it considers different value levels. I have until now used a value/rating system based on one "slice" of the continuum of runs, instead of somehow integrating the sum of all the results using some value metrics to determine the score for a strategy as a whole. I am very excited for the idea of applying this more complicated consideration method, especially if i manage to align it with the intuitive evaluation systems of people generally. 



### Closing thoughts


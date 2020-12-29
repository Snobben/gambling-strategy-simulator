## Welcome to my humble first pages blogpost!

In this project i have attempted to find the best risk-averse strategy for betting in a dice game where you win if the sum of your six rolled dice are higher than your opponents sum. What tempted me to this project was the fact that this game was implemented in an online video game with a special rule; namely that the player who first posted the bet for anyone to accept, won if the sum of the dices were equal. I realized that the expected value for player one were in fact positive, and it got me interested in finding the best strategy such that one could potentially earn a practically infinite amount of money - But mostly im doing this project to practice my still very limited python skills, and for entering the world of github and pages with a cute and interesting problem. I do think my findings where somewhat interesting, even though they were quite predictible if one gives some thought to the problem.


### Introduction to rules
The rules of the game are very straightforward:
- One player decides an amount to bet.
- Any other player can choose to enter into the bet for the amount set by player 1.
- Both players roll six dice, and the player with the highest sum wins. 
- If equal, player one, whom chose the bet size, wins. 
- The payout is 1.98 times the betsize.

### Expected value and some notes
Because of the fact that player one wins when the sums of dice are equal, his chance of winning the bet is about 53%, and his expected value is about 5% more than his bet. See the link here for my calculations showing these results. Note that this expected value is per bet. If one were to bet a thousand times, the expected value is (1.05)^1000. This is an astronomical value, and my calculated averages from my simulations were never close to that high. That can be explained by the fact that this average expected return gets very inflated by the very improbable edge cases where one wins close to every time. There is a practically zero  ((0,53)^1000 to be specific) chance for winning every time if one bets a 1000 times.

### Plots and analysis
The first thing i was interested in was getting a feel for how the simulations behaved, and so i did not put too many bets and number of runs in the script to reduce run time.
Plot one inputs: 100 runs, 100 bets, 0.05 bet size increment, 9 strategies.
In plot one, we can see how the strategies with increased betsizes have a higher average (the green line), but most of the betting runs is not profitable. Therefore, we can already deduce that higher betsizes are more risky. We can also see that there is not a single strategy who always avoids loss. In my next plot, i will therefore reduce the bet size increment increase number of bets.
Plot two inputs:
100 runs, 1000 bets, 0.01 bet size increment, 9 strategies.
Here we can observe that the lowest risk strategies actually completely avoids loss. Unfortunately these low risk strategy also give us quite small returns, compared to the slightly more risky strategies. 
### Methods for deciding the optimal strategy

	![Plot four](https://raw.githubusercontent.com/Snobben/gambling-strategy-simulator/gh-pages/Plots%20and%20stats%20for%20gambling-strategy-simulator/plot-four.png)

### Closing thoughts


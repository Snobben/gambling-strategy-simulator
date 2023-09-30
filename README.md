### Gambling-strategy-simulator
Was playing an  online game with gambling in it where i noticed the expected value for inserting bets were positive; 
The rules were as following: 
- One player decides an amount to bet.
- Any other player can choose to enter into the bet for the amount set by player 1.
- Both players roll six dice, and the player with the highest sum wins. 
- If equal, player one, whom chose the bet size, wins. 
- The payout is 1.98 times the betsize. Therefore, the expected payout for player one is about 1.056 the initial betsize.

My aspiration for this project is to try to decide the optimal bet size relative to the the money at hand, trying to get the highest "stable return",
meaning not only maximizing the average expected return but also considering risk.
I'm sure this problem could be solved formally with math (ref the kelly criterion as i became aware of later), but i decided to use monte carlo simulations
to at least get a decent estimate/idea of what bet percentage is optimal.
As my plots show, a bet size too small (<0.01) gives unsatisfying returns, and too big a betsize (>0.10) make it inevitable going bust over time, even though the occational payout is huge.
The optimal bet size for this particular payout and chance structure seems to be about 4%. 

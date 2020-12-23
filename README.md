# Gambling-strategy-simulator
# Was playing an  online game with gambling in it where i noticed the expected value for inserting bets was positive; 
# The rules were as following: 
# - One player decides an amount to bet.
# - Any other player can choose to enter into the bet for the amount set by player 1.
# Both players roll six die, and the player with the highest sum of die wins. If equal, player one, whom chose the bet size, wins. 
# The payout is 1.98 times the betsize. Therefore, the expected payout for player one is about 1.05 the initial betsize (did the math, trust me:))
# My aspiration for this project is to try to decide the optimal bet size relative to the the money at hand, trying to get the highest "stable return",
# meaning not only maximizing the average expected return but also considering risk.
# I'm sure this problem could be solved formally with math, and please do notice me if you manage so, but i decided to use monte carlo simulations,
# to at least get a decent estimate/idea of what bet percentage is optimal.
#As my plots show (and probably as expected), a bet size too small (<0.01) gives unsatisfying returns, and too big (>0.10) gives very unlikely but potentially exponential returns.

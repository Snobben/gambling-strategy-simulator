import random

#Rolling the six die for each "player" and calculating their total score for the round.
def dieroller():
    die_list1 = []
    die_list2 = []
    for i in range(6):
        die_list1.append(random.randint(1, 6))
        die_list2.append(random.randint(1, 6))
    sum1 = 0
    sum2 = 0
    for element in die_list1:
        sum1 += element
    for element in die_list2:
        sum2 += element
    return sum1, sum2

#Returning True if player one won, and false if not. Note that player one wins when the players sum is equal.
def die_result(sum1, sum2):
    return sum1 >= sum2

#Simulating n times of dice rolled and recording the subsequent results.
def repeat_play(times_to_bet):
    result_list = []
    for i in range(times_to_bet):
        sum1 = dieroller()[0]
        sum2 = dieroller()[1]
        result = die_result(sum1, sum2)
        result_list.append(result)
    return (result_list)

#Function for actually counting the number of times player one wins. Currently not used.
def result_counter(times_to_bet):
    result_list = repeat_play(times_to_bet)
    times_won = 0
    for element in result_list:
        if element:
            times_won += 1
    print("Times won:", times_won, "Times lost:", (times_to_bet - times_won))

#Tracking the money player one accumulates over the course of games.
def cash_tracker(times_to_bet, initial_money, betsize_percentage):
    result_list = repeat_play(times_to_bet)
    money = 0
    money += initial_money
    for element in result_list:
        betsize = money * betsize_percentage
        money -= betsize
        if element:
            money += betsize * 1.98
    return (money)

#Simulating the game for a given betsize, initial money and subsequent times to bet for a chosen number of runs.
#Stores the end money sum for further calculation and visualization.
def strategy_tester(nums_of_runs, times_to_bet, initial_money, betsize_percentage):
    strategy_result_list = []
    for i in range(nums_of_runs):
        strategy_result_list.append(cash_tracker(times_to_bet, initial_money, betsize_percentage))
    return strategy_result_list

#Isn't used anywhere right now, but is interesting to look at in combination with the plots in deciding the best strategy.
def stat_maker(strategy_result_list):
    average = 0
    for element in strategy_result_list:
        average += element
    average = average / nums_of_runs
    variance = 0
    for element in strategy_result_list:
        variance = variance + (average - element) * (average - element)
    variance = variance / nums_of_runs
    standard_deviance = variance ** (1 / 2)
    sorted_list = sorted(strategy_result_list)
    lower_quartile_value = sorted_list[round(nums_of_runs * 0.25)]
    upper_quartile_value = sorted_list[round(nums_of_runs * 0.75)]
    ninety_five_percent_low = sorted_list[round(nums_of_runs * 0.05)]
    stat_list = [average, standard_deviance, lower_quartile_value, upper_quartile_value, ninety_five_percent_low,
                 min(strategy_result_list), max(strategy_result_list)]
    return stat_list

#Plotting different strategies and plotting the end money sums against eachother and internally against the baseline/
#initial money at hand to compare how efficient the strategies are.
def plot_result():
    from matplotlib import pyplot as plt
    j = 0
    for i in range(1, 10, 1):
        j += 1
        strategy_result_list = strategy_tester(100, 3650, 1, i*0.02)
        plt.plot([x for x in range(100)], [1 for x in range(100)])
        plt.yscale("log")
        plt.subplot((430+j))
        plt.plot([num for num in range(100)], strategy_result_list)
    plt.show()

plot_result()


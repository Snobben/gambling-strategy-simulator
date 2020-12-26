import random
import math

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
def stat_maker(strategy_result_list, nums_of_runs):
    average = 0
    for i in range(len(strategy_result_list)):
        average += strategy_result_list[i]
    average = average / nums_of_runs
    variance = 0
    for element in strategy_result_list:
        variance = variance + (average - element)**2
    variance = variance / nums_of_runs
    standard_deviance = math.sqrt(variance)
    sorted_list = sorted(strategy_result_list)
    lower_quartile_value = sorted_list[round(nums_of_runs * 0.25)]
    upper_quartile_value = sorted_list[round(nums_of_runs * 0.75)]
    ninety_five_percent_low = sorted_list[round(nums_of_runs * 0.05)]
    stat_list = [average, standard_deviance, lower_quartile_value, upper_quartile_value, ninety_five_percent_low,
                 min(strategy_result_list), max(strategy_result_list)]
    return stat_list

#Plotting different strategies and plotting the end money sums against eachother and internally against the baseline/
#initial money at hand to compare how efficient the strategies are.
def plot_result(nums_of_runs, strategies_list, nums_of_strategies, log_scale):
    from matplotlib import pyplot as plt
    rowsandcols = plot_scaler(nums_of_strategies)
    rows = rowsandcols[0]
    columns = rowsandcols[1]
    for i in range(nums_of_strategies):
        strat_list = strategies_list[i]
        average = stat_maker(strat_list, nums_of_runs)[0]

        plt.subplot(rows, columns, (i+1))
        if log_scale:
            plt.yscale("log")
        plt.plot([x for x in range(nums_of_runs)], [1 for x in range(nums_of_runs)])#Plotting initial money at hand
        plt.plot([x for x in range(nums_of_runs)], [average for x in range(nums_of_runs)])#Plotting average money for each strategy
        plt.plot([num for num in range(nums_of_runs)], strat_list)

        print(stat_maker(strat_list, nums_of_runs))
    plt.show()

#Seperated out the function for deciding the number of strategies from the plot function for more flexibility.
def multiple_strategy_tester(nums_of_strategies, nums_of_runs, times_to_bet, initial_money, betsize_percentage):
    strategies_list = []
    for i in range(nums_of_strategies):
        strategies_list.append(strategy_tester(nums_of_runs, times_to_bet, initial_money, (i+1) * betsize_percentage))
    return strategies_list

def plot_scaler(nums_of_strategies):
    columns = math.floor(math.sqrt(nums_of_strategies))
    if nums_of_strategies <= (columns**2 + columns) and nums_of_strategies > columns**2:
        rows = columns + 1
    elif nums_of_strategies > (columns**2 + columns):
        columns += 1
        rows = columns
    else:
        rows = columns
    return ([rows, columns])

def main():
    nums_of_runs = 100
    times_to_bet = 100
    initial_money = 1
    betsize_percentage = 0.01
    nums_of_strategies = 15
    to_plot = True
    log_scale = True
    strategies_list = multiple_strategy_tester(nums_of_strategies, nums_of_runs, times_to_bet, initial_money, betsize_percentage)
    if to_plot:
        plot_result(nums_of_runs, strategies_list, nums_of_strategies, log_scale)
main()



#Mål videre:
#Gjøre litt matte
#Gå nærmere inn på ca beste nivå
#Undersøke effekten av times to bet
#Lage stopp-funksjon.
#Lage bloggpost
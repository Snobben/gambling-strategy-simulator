import random


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


def die_result(sum1, sum2):
    return sum1 >= sum2


def repeat_play(times_to_bet):
    result_list = []
    for i in range(times_to_bet):
        sum1 = dieroller()[0]
        sum2 = dieroller()[1]
        result = die_result(sum1, sum2)
        result_list.append(result)
    return (result_list)


def result_counter(times_to_bet):
    result_list = repeat_play(times_to_bet)
    times_won = 0
    for element in result_list:
        if element:
            times_won += 1
    print("Times won:", times_won, "Times lost:", (times_to_bet - times_won))


def cash_tracker(times_to_bet, initial_money, betsize_percentage):
    result_list = repeat_play(times_to_bet)
    money = 0
    money += initial_money
    for element in result_list:
        betsize = money * betsize_percentage
        money -= betsize
        if element:
            money += betsize * 1.98
        elif money <= 0.1 * initial_money:
            continue
            # return (money, False)
    return (money)


def strategy_tester(nums_of_runs, times_to_bet, initial_money, betsize_percentage):
    strategy_result_list = []
    for i in range(nums_of_runs):
        strategy_result_list.append(cash_tracker(times_to_bet, initial_money, betsize_percentage))
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
    stat_list = [average, standard_deviance, lower_quartile_value, upper_quartile_value, ninety_five_percent_low, min(strategy_result_list), max(strategy_result_list), strategy_result_list]
    return (stat_list)





# Maximise this function with respect to the lower quartile value, using the bet_size_percentage as input parameter.

def plot_result():
    from matplotlib import pyplot as plt
    j = 0
    for i in range(1, 10, 1):
        j += 1
        stat_list = strategy_tester(100, 1000, 1, i*0.01)
        strategy_result_list = stat_list[7]
        #plt.plot(strategy_result_list)
        #plt.plot([x for x in range(100)], [1 for x in range(100)])

        plt.subplot((430+j))
        plt.plot([num for num in range(100)], strategy_result_list)

    plt.show()


plot_result()


#!/usr/bin/python

import argparse


def find_max_profit(prices):
    max_profit = None
    for i in range(len(prices)):
        found_lower = False
        for j in range(len(prices)):
            if(i == j):
                continue
            if(j < i):
                if(prices[i] - prices[j] > max_profit):
                    max_profit = prices[i] - prices[j]
                    found_lower = True
            elif(found_lower == False):
                if(max_profit == None):
                    max_profit = prices[j] - prices[i]
                elif(max_profit < prices[j] - prices[i]):
                    max_profit = prices[j] - prices[i]
            else:
                continue
    print(f"Max profit = {max_profit}")
    return max_profit

    # continue_search = True
    # start_index = 0
    # max_profit = 0

    # while(continue_search):
    #     max_price_index = 0
    #     min_price_index = 0
    #     # Find the index of the greatest value
    #     for i in range(start_index, len(prices)):
    #         if prices[i] > prices[max_price_index]:
    #             max_price_index = i

    #     # Find the index of the smallest value that exists before the greatest
    #     # value in the list
    #     did_find_min = False
    #     next_max_index = max_price_index + 1

    #     # as long as the largest index isn't first
    #     if(max_price_index != start_index):
    #         for i in range(start_index, max_price_index):
    #             if prices[i] < prices[min_price_index]:
    #                 min_price_index = i
    #                 did_find_min = True

    #     # if no lower value is found previously
    #     if(did_find_min == False):
    #         for i in range(max_price_index + 1, len(prices)):
    #             if(prices[i] > prices[next_max_index]):
    #                 next_max_index = i
    #         competing_price = prices[max_price_index] - prices[next_max_index]

    #     else:
    #         competing_price = prices[max_price_index] - prices[min_price_index]
    #     # Set the start index to the element directly after the greatest value
    #     # index

    #     if(max_price_index + 1 < len(prices) - 1):
    #         start_index = max_price_index + 1
    #         if(did_find_min == False):
    #             max_price_index += 1
    #     else:
    #         continue_search = False

    #     # Get the difference between the values and compare it to the
    #     # greatest profit value that has already been found

    #     if(competing_price > max_profit):
    #         max_profit = competing_price

    # return competing_price


my_prices = [8, 7, 25, 223, 5, 222, 1, 58]
find_max_profit(my_prices)

if __name__ == '__main__':
        # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))

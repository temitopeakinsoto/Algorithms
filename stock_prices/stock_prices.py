#!/usr/bin/python

import argparse


  
def find_max_profit(prices): 

  # Init max_profit_so_Far to a negative number
  max_profit_so_far = -999999999999999
  current_min_price_so_far = prices[0]

  for i in range(0, len(prices)):

    if prices[i] < current_min_price_so_far:
      current_min_price_so_far = prices[i]

    for j in range(i+1, len(prices)):

      if prices[j] - prices[i] > max_profit_so_far:
        max_profit_so_far = prices[j] - prices[i]
        
  return max_profit_so_far,current_min_price_so_far

    
print("-----------")
print(find_max_profit([100, 90, 80, 50, 20, 10]))
print(find_max_profit([1050, 270, 1540, 3800, 2]))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
# jose 
#paul

# ()(){}
# (){}
# {}
# empty 
# (())
'''
def is_valid(s):
    dict = {"(":")", "[":"]", "{":"}"}
    stack = []

    for char in s:
        if char in dict:
            stack.append(char)
        else:
           # check if its equal to key 
           # if not -> false 
            if dict[stack[-1]] != char:
                return False
            # if true 
            # pop 
            stack.pop()
    # return true if the stack is empty 
    return not stack
s = "()[]{}"
print(is_valid(s))


''' 


def max_profit(prices):
    min_price = 90000000000
    maximum_profit = 0
    # loop through list:
    for price in prices:
        # if prices is lower than min:
            # make prices the min 
        if price < min_price:
            min_price = price 
        # do prices - min_price  -> profit 
        profit = price - min_price
        # ex  7 - 1 =6
        # append max_profit to a variable 
        if profit > maximum_profit:
            maximum_profit = profit
        # if new profit is > old profit , update profit 
        # return final profit
    return maximum_profit
    
prices = [7,1,5,3,6,4]
print(max_profit(prices))




def max_profit(prices):
    min_price = 90000000000
    maximum_profit = 0
    # loop through list:
    for price in prices:
        # if prices is lower than min:
            # make prices the min 
        if price < min_price:
            min_price = price 
        # do prices - min_price  -> profit 
        profit = price - min_price
        # append max_profit to a variable 
        if profit > maximum_profit:
            maximum_profit = profit
        # if new profit is > old profit , update profit 
        # return final profit
    return maximum_profit
    
prices1 = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
print(max_profit(prices))

#<function max_profit at 0x7b19582884a0>
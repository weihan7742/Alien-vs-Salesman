"""
Author: Ng Wei Han
"""

#%%
def best_itinerary(profit,prison_time,home):
    """
    Function which finds the maximum amount of money that can be earned
    by the salesperson using dynamic programming method.

    :param profit: List of lists in which the elements of inner lists representing the 
    profit that can be earned on a specific day. 
    :param prison_time: List of non-negative integers in which prison_time[i] is 
    number of days city i requires visitors to prison
    :param home: Integer between 0 and n-1 where n is the number of days which represents
    the city that the salesperson starts in.
    :return: An integer which is the maximum amount of money that can be earned by the
    salesperson.

    ---Time Complexity---
    Best/Worst: O(nd) 
    n - number of cities
    d - number of days or number of interior lists in profit
    The algorithm will loop through the list, and during each loop, it will loop
    through the inner list, which gives final O(nd) time complexity.

    ---Space Complexity---
    Best/Worst: O(nd)
    Auxiliary Space: O(nd)
    n - number of cities
    d - number of days or number of interior lists in profit
    Only 1 memoization array with the size of n*d has been initialized.
    """
    
    # Initialize memo 
    memo = [[[-1,-1]]*(len(profit[0])+1) for _ in range(len(profit)+2)] 

    # Initialize 0 in first row 
    memo[0] = [[0,0] for _ in range(len(profit[0])+1)]

    # Initialize 0 in last row
    memo[-1] = [[0,0] for _ in range(len(profit[0])+1)]

    num_row = len(memo)
    num_col = len(memo[0]) 
    # Initialize 0 in first column
    for i in range(len(memo)):
        memo[i][0] = [0,0]

    for i in range(num_row-2,0,-1): # Iterate through the rows
        for j in range(1,num_col): # Iterate through the columns
            curr_memo = memo[i][j]
            prev_memo = memo[i+1][j]
            curr_item = profit[i-1][j-1]

            left_qrt = [0,0]
            right_qrt = [0,0]

            left_adjacent = [0,0]
            right_adjacent = [0,0]

            # Add items
            item_1 = curr_item+prev_memo[0]
            item_2 = prev_memo[1]

            if item_2 > 0:
                item_2 += curr_item
            
            curr_memo = [item_1,item_2]

            # Check for left adjacent
            if j-1 > 0:
                left_adjacent = memo[i+1][j-1]
            
            # Check for right adjacent
            if j+1 < num_col:
                right_adjacent = memo[i+1][j+1]
            

            if curr_memo[1] < left_adjacent[1]:
                if left_adjacent[1]-memo[i+2][j-1][1] != profit[i][j-2]:
                    curr_memo[1] = left_adjacent[1]

            if right_adjacent[1] > curr_memo[1]:
                if right_adjacent[1]-memo[i+2][j+1][1] != profit[i][j]:
                    curr_memo[1] = right_adjacent[1]

            # Check if can traverse to left bottom and take item_1
            if j-1 > 0 and i+prison_time[j-2]+1 < len(memo):
                left_qrt = memo[i+prison_time[j-2]+1][j-1]
            # Check if can traverse to right bottom and take item_1
            if j+1 < num_col and i+prison_time[j]+1 < len(memo): 
                right_qrt = memo[i+prison_time[j]+1][j+1]

            curr_memo[1] = max(curr_memo[1],left_qrt[0],right_qrt[0],left_qrt[1],right_qrt[1])
            curr_memo[0] = max(curr_memo[0],left_qrt[0],right_qrt[0])

            memo[i][j] = curr_memo

    # print_matrix(profit)
    return max(memo[1][home+1])
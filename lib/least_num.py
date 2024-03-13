def solution(A):
    #Only get the positive numbers
    pos_nums = [i for i in A if i > 0 and isinstance(i, int)]
    #if number is not positive, return 1
    if not pos_nums:
        return 1
    #sort the numbers in assending order
    pos_nums.sort()

    #To find the smallest number that does not occur in the list:
    least_num = 1
    for num in pos_nums:
        if num == least_num:
            least_num += 1
        elif num > least_num:
            break
    return least_num
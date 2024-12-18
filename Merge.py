import timeit
def MergeSort(a_list):
    star_time = timeit.default_timer()
    op = 0

    n = len(a_list)
    if n < 2:
        return a_list
    mid = n // 2
    left = a_list[:mid]
    right = a_list[mid:]
    MergeSort (left)
    MergeSort (right)

    i = 0; j = 0; k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a_list[k] = left[i] 
            i = i + 1
        else:
            a_list[k] = right[j]
            j = j + 1
        k = k + 1
    while i < len(left): 
        a_list[k] = left[i]
        i = i + 1
        k = k + 1
    while j < len(right): 
        a_list[k] = right[j]
        j = j + 1
        k = k + 1
        op += 1 

    time = timeit.default_timer() - star_time
    return a_list,op,time

if __name__=='__main__':

    A = [2, 7, 4, 1, 5, 3, 9, 10, 15, 11, 13, 12, 16, 14, 18, 20, 19, 17, 21, 22, 23, 24]
    a,op,time = MergeSort(A)
    mstime = time*1000
    print(a)
    print(f'จำนวนครั้งการทำ Sort = {op}')
    print(f'เวลาการทำงาน {time:.10f} วินาที หรือ {mstime:.5f} มิลลิวินาที')

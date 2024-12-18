import timeit
star_time = timeit.default_timer()
def QuickSort(a_list, start, end):
    n = len(a_list)
    if start < end:
        pIndex = QuickSort_partition(a_list, start, end)
        QuickSort(a_list, start, pIndex-1) 
        QuickSort(a_list, pIndex+1, end)
    
    return a_list

def QuickSort_partition(a_list, start, end):
    pIndex = start
    # select last pos as index 
    pivot = a_list[end]

    # push less value to the left 
    for i in range(start, end): 
        if a_list[i] <= pivot: 
            temp = a_list[i]
            a_list[i] = a_list[pIndex] 
            a_list[pIndex] = temp 
            pIndex = pIndex + 1
    temp = a_list[pIndex]
    a_list[pIndex] = a_list[end] 
    a_list[end] = temp
    return pIndex

if __name__=='__main__':
    
    time = timeit.default_timer() - star_time
    A = [2, 7, 4, 1, 5, 3, 9, 10, 15, 11, 13, 12, 16, 14, 18, 20, 19, 17, 21, 22, 23, 24]
    print(A)

    QuickSort(A,0,len(A)-1)
    print(A)
    
    mstime = time*1000
    print(f'จำนวนครั้งการทำ Sort = {op}')
    print(f'เวลาการทำงาน {time:.10f} วินาที หรือ {mstime:.5f} มิลลิวินาที')

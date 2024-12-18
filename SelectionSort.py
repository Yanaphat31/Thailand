import timeit
def SelectionSort(a_list):
    star_time = timeit.default_timer()
    op = 0

    n = len(a_list)
    for i in range(0, n-1):
        iMin = i
        flag = 0
        for j in range(i+1, n):
            if a_list[j] > a_list[iMin]:
                iMin = j
            flag = 1
        
        if flag == 0:
            break
        temp = a_list[i]
        a_list[i] = a_list[iMin]
        a_list[iMin] = temp

    time = timeit.default_timer() - star_time
    return a_list,op,time

if __name__=='__main__':

    A = [2, 7, 4, 1, 5, 3, 9, 10, 15, 11, 13, 12, 16, 14, 18, 20, 19, 17, 21, 22, 23, 24]
    print(A)

    a,op,time = SelectionSort(A)
    mstime = time*1000
    print(a)
    print(f'จำนวนครั้งการทำ Sort = {op}')
    print(f'เวลาการทำงาน {time:.10f} วินาที หรือ {mstime:.5f} มิลลิวินาที')
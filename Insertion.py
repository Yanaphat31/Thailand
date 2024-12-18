import timeit
def InsertionSort(a_list):
    star_time = timeit.default_timer()
    op = 0
    
    n = len(a_list)

    for i in range(1, n):
        temp = a_list[i]
        hole = i

        while hole>0 and a_list[hole-1]<temp: 
            a_list[hole] = a_list[hole-1]
            hole = hole-1
    
        a_list[hole] = temp
        op += 1 
    time = timeit.default_timer() - star_time
    return a_list,op,time

if __name__=='__main__':

    A = [2, 7, 4, 1, 5, 3, 9, 10, 15, 11, 13, 12, 16, 14, 18, 20, 19, 17, 21, 22, 23, 24]
    print(A)
    a,op,time = InsertionSort(A)
    mstime = time*1000
    print(a)
    print(f'จำนวนครั้งการทำ Sort = {op}')
    print(f'เวลาการทำงาน {time:.10f} วินาที หรือ {mstime:.5f} มิลลิวินาที')

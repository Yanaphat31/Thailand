import timeit
def BubbleSort(a_list):

    star_time = timeit.default_timer()
    op = 0

    n = len(a_list)
    for k in range(1, n):
        flag = 0
        for i in range(0, n - k):
            if a_list[i] < a_list[i+1]:  #เครื่องหมาย
                tmp = a_list[i]
                a_list[i] = a_list[i+1]
                a_list[i+1] = tmp
                op += 1
                flag = 1
        if flag == 0:
            break
    time = timeit.default_timer() - star_time
    return a_list,op,time #Return or Not

if __name__=='__main__':

    A = [2, 7, 4, 1, 5, 3, 9, 10, 15, 11, 13, 12, 16, 14, 18, 20, 19, 17,]
    print(A)
    
    a,op,time = BubbleSort(A)
    mstime = time*1000
    print(a)
    print(f'จำนวนครั้งการทำ Sort = {op}')
    print(f'เวลาการทำงาน {time:.10f} วินาที หรือ {mstime:.5f} มิลลิวินาที')
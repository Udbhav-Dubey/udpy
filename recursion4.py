#Sum of first N numbers
def func(sum,num):
    if (num==0):
        print(sum)
        return ;
    sum+=num
    func(sum,num-1)

num=int(input("please enter the number : "))
func(0,num)

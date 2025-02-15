#programe to read the numbers until -1 is encountered .Find the average of positive numbers and negative numbers entered by the user.
negative=positive=zeros=0
neg_sum=0
pos_sum=0
average_neg=0
average_pos=0
print("Enter the '-1 ' for the exit...")
while 1 :
    num=int(input("Enter the number positive and negative \n>>> "))
    if num==-1:
        break
    elif num<0:
        negative-=neg_sum
        negative-=1
    elif num>0:
        positive+=pos_sum
        positive+=1
    else:
        print("its a zero.")
    
average_neg=float(neg_sum)/negative
average_pos=float(pos_sum)/positive
print("THE AVERAGE OF THE POSITIVE NUMBERS IS "+str(average_pos))
print("THE AVERAGE OF THE NEGATIVE NUMBERS IS "+str(average_neg))
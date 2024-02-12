import random
import time

operators=["+","-","*"]
total_value=10

def generate_expr():
    right=random.randint(2,12)
    left=random.randint(2,12)
    operator=random.choice(operators)
    exrp=str(left)+ " " +operator+ " "+str(right)
    answer=eval(exrp)

    return exrp,answer


start=time.time()
for i in range(total_value):
    value,ans=generate_expr()
   
    print("this is ur {} quetion".format(i+1))
    while True:
        guess=input(value+" = ")
        if int(guess)==ans:
            break
        else:
            print("try untill u get it ")
            
print("hey its done good job ")
end=time.time()
total_time=end-start
round_total_time=round(total_time,2)
print("you took {} seconds ".format(round_total_time))


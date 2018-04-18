import cProfile
import random
import time
start = time.time()

def test1(t):
    s1 = random.randint(1,10)
    s2 = random.randint(1,10)
    s3 = random.choice(['+','-','*','/'])
    cal(s1,s2,s3,t)

def test2(t):
    s1 = random.randint(1,10)
    s2 = random.randint(s1,11)
    s3 = random.randint(1,10)
    s4 = random.randint(s3,11)
    s5 = random.choice(['+','-'])
    sr = "第" + str(t) + "题：" + str(s1) + '÷'+ str(s2) + s5+str(s3) + '÷'+ str(s4) + '='
    l1.append(sr)
    if s5 == '+':
        l2.append(s1 / s2 + s3 / s4)
    else:
        if s1 / s2 - s3  / s4 > 0:
            l2.append(s1 / s2 - s3 / s4)
        else:
            sr = "第" + str(t)  +"题：" + str(s3) +  '÷'+ str(s4) + s5 + str(s1)  +  '÷' + str(s2) + '='
            l2.append(s3 / s4 - s1  /s2)
def cal(s1,s2,s3,t):
    sr = "第" + str(t) +  "题：" + str(s1) + s3 + str(s2) +  '='
    if s3 == '+':
        l2.append(s1 + s2)
    elif s3 == '-':
        if s1 >= s2:
            l2.append(s1 - s2)
        else:
            sr = "第" + str(t) + "题：" + str(s2) + s3 + str(s1) + '='
            l2.append(s2 - s1)
    elif s3 == '*':
        sr = "第" + str(t) + "题：" + str(s1) + 'x' + str(s2) + '='
        l2.append(s1 * s2)
    elif s3 == '/':
        sr = "第" + str(t) + "题：" + str(s1) + '÷' + str(s2) + '='
        l2.append(s1 / s2)
    l1.append(sr)
t = 1
l1 = []
l2 = []

while t <= 10:
    if t <= 5:
        test1(t)
    elif t <= 10:
        test2(t)
    print(l1[t - 1])
    n=eval(input())
    if l2[t -1] == n:
        print("回答正确！")
    else:
        print("回答错误！")
    t += 1

cProfile.run('cal')
cProfile.run('test1')
cProfile.run('test2')
end=time.time()
print(end-start)
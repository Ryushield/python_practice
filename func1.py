#func1.py
#함수정의

def setValue(newValue):
    x=newValue
    print(x)


#함수 호출
setValue(5)


#값을 리턴하는 함수
def swap(x,y):
    return y,x

result = swap(5,6)
print(result)
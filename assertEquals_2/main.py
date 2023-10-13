# main 함수는 다수의 function이 있는 함수입니다. 

def foo(a,b) : 
    return a / b 

def bar(a,b) :
    return a * b

def sum(a,b) :
    return a + b

def sub(a,b) :
    return a - b

def main() :
    print("Hello World!")
    print("foo(10,5) : ", foo(10,5))
    print("bar(10,5) : ", bar(10,5))
    print("sum(10,5) : ", sum(10,5))
    print("sub(10,5) : ", sub(10,5))
    
if __name__ == "__main__" :
    main()
    

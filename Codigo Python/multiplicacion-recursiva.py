def multi( a, b):
    if b > 1:
        b-=1
        return  a + multi(a, b)
    else:
        return a

def main():
    print(multi(3, 5))

if __name__ == "__main__":
    main()
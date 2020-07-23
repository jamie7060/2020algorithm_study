def palindrome_check(A):
    n = len(A)
    is_palindrome = True
    #앞과 뒤 비교
    for j in range(int(n/2)):
        if(A[j] != A[n-1-j]):
            print("회문이 아닙니다.")
            is_palindrome = False
            break
    
    if(is_palindrome == True):
        print("회문입니다.")

palindrome_check("구구갸갸")
palindrome_check("asddsa")
palindrome_check("랑사사랑")

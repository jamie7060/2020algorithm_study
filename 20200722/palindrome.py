# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
#문자열 input
string = list(input())
#질의 수
n = int(input())
#질의 수만큼 for문
for i in range(n):
	a, b = map(int, input().split())
	is_palindrome = True
	partial = string[a-1:b]
	partial_len = len(partial)
    #앞과 뒤 비교
	for j in range(int(partial_len/2)):
		if(partial[j] != partial[partial_len-1-j]):
			print(0)
			is_palindrome = False
			break
	
	if(is_palindrome == True):
		print(1)

"""
동적 계획법을 이용해서 a번째 문자열부터 b번째 문자열이 회문인지 아닌지 저장하는 배열을 만들어서 풀 수도 있다.
d[a][b] = (string[a] == string[b] && d[a+1] == d[b-1])
"""

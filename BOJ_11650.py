import sys
n = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(n)]  # 입력 줄이기

num_list.sort()

sys.stdout.write('\n'.join(map(str, num_list)))  # 출력 줄이기

#sys.stdin.readline() -> input()
#sys.stdout.write() - > print()
#.join() 괄호안의 문자열 리스트를 .앞의 문자단위로 끊어서 하나의 문자열로 만드는 기능
#map(type, list) 어떤 리스트에 대해 특정한 타입을 각 요소별로 맵핑시키는 기능
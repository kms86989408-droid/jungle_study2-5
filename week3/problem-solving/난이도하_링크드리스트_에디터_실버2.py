# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406
import sys

# s = sys.stdin.readline().strip()
# m = int(sys.stdin.readline())

# left = list(s)    
# right = []

# for i in range(m):
#     cmd = sys.stdin.readline().split()

#     if cmd[0] == "L":
#         if len(left) != 0 :
#             right.append(left.pop())
#     elif cmd[0] == "D":
#         if len(right) != 0 :    
#             left.append(right.pop())    
#     elif cmd[0] == "B":
#         if len(left) != 0 :
#             left.pop()
#     elif cmd[0] == "P":
#         left.append(cmd[1])

# print("".join(left+right[::-1]))
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def insert(cursor, data):
    node = Node(data)
    node.prev = cursor.prev
    node.next = cursor
    cursor.prev.next = node
    cursor.prev = node        
        
s = input().rstrip()
m = int(input())

head = Node(None) #시작더미
tail = Node(None) #끝 더미

head.next = tail
tail.prev = head
cursor = tail

for c in s:
    insert(cursor, c)
        
for i in range(m):
    cmd = input().split()
    if cmd[0] == "L":
        if cursor.prev != head:
            cursor = cursor.prev
    elif cmd[0] == "D":
            if cursor != tail:
                cursor = cursor.next
    elif cmd[0] == "B":
        if cursor.prev != head:
            cursor.prev.prev.next = cursor
            cursor.prev = cursor.prev.prev
    elif cmd[0] == "P":
        insert(cursor, cmd[1])
node = head.next
result = []

while node != tail:
    result.append(node.data)
    node = node.next


sys.stdout.write("".join(result))
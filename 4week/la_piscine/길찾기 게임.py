import sys
sys.setrecursionlimit(10**6) # 런타임에러 방지

# Tree 클래스 생성하기
class Tree:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.data = None
        self.index = None

# 전위순회
def preOrder(root, vector):
    if root == None:
        return vector
        
    vector.append(root.index)
    preOrder(root.left,vector)
    preOrder(root.right,vector)
        
    return vector
    
# 후위순회
def postOrder(root, vector):

    if root == None:
        return vector
    postOrder(root.left, vector)
    postOrder(root.right, vector)
    vector.append(root.index)

    return vector

def solution(nodeinfo):
    # 이진 트리에 데이터 저장
    root = None
    
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
        
    # y좌표를 기준으로 내림차순 정렬
    nodeinfo = sorted(nodeinfo, key= lambda x:x[1], reverse=True)
    
    # enumerate 함수로 for문 반복
    for i,node in enumerate(nodeinfo):
        newTree = Tree()
        newTree.index = node[2]
        newTree.data = node
        
        if root == None:
            root = newTree
        else:
            curTree = root
            
            while 1:
                # 새로 삽입하려는 데이터가 원래 데이터보다 크다면 오른쪽에 삽입
                if curTree.data[0] < newTree.data[0]:
                    # 현재 노드의 오른쪽 노드가 null이라면
                    if curTree.right == None:
                        curTree.right = newTree
                        newTree.parent = curTree
                        break
                    # 현재 노드의 오른쪽 노드를 현재 노드로 다시 정의한다
                    else:
                        curTree = curTree.right
                        
                # 새로 삽입하려는 데이터가 원래 데이터보다 작다면 왼쪽에 삽입
                else:
                    # 현재 노드의 왼쪽 노드가 null이라면
                    if curTree.left == None:
                        curTree.left = newTree
                        newTree.parent = curTree
                        break
                    # 현재 노드의 왼쪽 노드를 현재 노드로 다시 정의한다
                    else:
                        curTree = curTree.left

    # 최종 순회 후 결과값을 저장
    answer = [preOrder(root,[]), postOrder(root,[])]
    return answer
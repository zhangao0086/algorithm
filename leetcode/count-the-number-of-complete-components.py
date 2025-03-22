from collections import defaultdict
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(node, visited, component):
            visited.add(node)
            component.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited, component)
                    
        def is_complete_component(nodes):
            size = len(nodes)
            # 检查每个节点是否都与其他所有节点相连
            for node in nodes:
                if len(graph[node]) != size - 1:
                    return False
            return True
                    
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                component = []
                dfs(i, visited, component)
                if is_complete_component(component):
                    count += 1
        return count

if __name__ == '__main__':
    solution = Solution()
    print(solution.countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4]]))
    print(solution.countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]))

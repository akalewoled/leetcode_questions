class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        relation=defaultdict(list)
        for rich,poor in richer:
            relation[poor].append(rich)
        solution=[-1 for _ in range(len(quiet))]
        # a defs to calulate the quiter
        def dfs(node):
            if (solution[node]) != -1 :
                 return solution[node]
            rich=node
            quite=quiet[node]
            for richers in relation[node] :
                ind=dfs(richers)
                if quite > quiet[ind]:
                    rich=ind
                    quite=quiet[rich]
            solution[node] = rich
            return rich
        # the main function
        for  i in range(len(quiet)):
            solution[i]=dfs(i)
        return solution 

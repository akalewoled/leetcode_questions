class Solution:
    def findRightInterval(self, items: List[List[int]]) -> List[int]:
        search_array=[]
        for i in range(len(items)):
            search_array.append([items[i][0],i])
        search_array.sort()
        print(search_array)
        final=[]

        for i in items:
            target=i[1]
            left=0
            right=len(items)-1

            while left <=right:
                mid=left+(right-left)//2
                if search_array[mid][0]<target:
                    left=mid+1
                else:
                    right=mid-1
            if left >len(items)-1:
                final.append(-1)
            else:
                final.append(search_array[left][1])
        return final

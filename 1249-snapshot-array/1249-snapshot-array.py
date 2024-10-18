class SnapshotArray:

    def __init__(self, length: int):
        self.array=[[[-1,0]] for _ in range(length)]
        self.snapid=0
        

    def set(self, index: int, val: int) -> None:
        self.array[index].append([self.snapid,val])
        

    def snap(self) -> int:
        ID= self.snapid
        self.snapid+=1
        return ID
        

    def get(self, index: int, snapid: int) -> int:
        result=self.array[index]
        value=result[0][1]
        #lets fined the nearest snapshot
        for snap_id,val in result:
            if snapid >=snap_id:
                value=val
            else:
                break
        return value


        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
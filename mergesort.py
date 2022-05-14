class solution():
    def mergesort(self, nlist):
        print(nlist)
        print("222222")
        return self.split(nlist)
       
    def split(self, nlist):
        if len(nlist) == 0:
            return       
        mid = int(len(nlist)/2)
        left = self.split(nlist[:mid])
        right = self.split(nlist[mid+1:])
        print(left, right)
        return self.merge(left, right)

    def merge(self, left, right):
        res = []
        if not left:
            return right
        if not right:
            return left
        while left and right:
            if left[0] <= right[0]:
                res.append(left[0])
                left.pop(0)
            else:
                res.append(right[0])
                right.pop(0)
        
        while right:
            res.append(right[0])
            right.pop(0)
        while left:
            res.append(left[0])
            left.pop(0)
        return res    
        



if __name__ == "__main__":
    a = solution()
    nlist = [1, 2, 7, 9, 5, 4, 3, 0]
    print(a.mergesort(nlist)) 



    

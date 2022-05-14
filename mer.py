class solution():
    def mergesort(self, nlist):
        return self.split(nlist)
       
    def split(self, nlist):
        if len(nlist) <=1:
            return nlist
        mid = int(len(nlist)/2)
        left = self.split(nlist[:mid])
        right = self.split(nlist[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        res = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        if i <= len(left)-1:
            while i < len(left):
                res.append(left[i])
                i += 1
        if j <= len(right) -1:
            while j < len(right):
                res.append(right[j])
                j += 1
        return res    
        



if __name__ == "__main__":
    a = solution()
    nlist = [1, 2, 7, 9, 5, 4, 3, 0, 77, 21]
    print(a.mergesort(nlist)) 



    

class solution():
    def bubblesort(self, nlist):
        if not nlist:
            return None
        i = 0
        length = len(nlist)
        
        for i in range(len(nlist)-1):
            for j in range(1, len(nlist)-i):
                if nlist[j-1] > nlist[j]:
                    nlist[j-1], nlist[j] = nlist[j], nlist[j-1]
        return nlist






if __name__ == '__main__':
    a = solution()
    lists = [2, 4, 1, 5, 3]
    print(a.bubblesort(lists))
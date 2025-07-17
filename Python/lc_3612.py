class Solution:
    def processStr(self, s: str) -> str:

        newList=[]
        for ch in s:
            if ch=='*':
                if len(newList)>0:
                    newList.pop()
            elif ch=="#":
                newList.extend(newList)
            elif ch=="%":
                newList.reverse()
            elif ch.islower():
                newList.append(ch)

        result=""

        for element in newList:
            
            result+=element

        return result
                

        
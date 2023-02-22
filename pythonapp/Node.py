class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


    def racine(self, L, L1):

        if self is not None:
            if self.data[0]!="" and self.data[1]=="" and self.data[2]=="":
                ch="double score =0; \nfor (int spec=0;spec<height;++spec) score+=resultProcess[spec] * "+str(self.data[0])+"[spec];\n"
                L.append(ch)
            elif self.data[0]=="" and self.data[1]!="" and self.data[2]!="":
                ch="if (score > "+self.data[1]+" &&  score <= "+self.data[2]+" ) Result[pixel]=(byte)Products.xx;"
                L.append(ch)
            else :
                ch="if (score > "+self.data[1]+" &&  score <= "+self.data[2]+" ) \n{ score =0; \nfor (int spec=0;spec<height;++spec) score+=resultProcess[spec] * "+str(self.data[0])+"[spec];\n "
                L.append(ch)
                L1.append(self.count_children()+len(L))



    def count_children(self):
        count = 0
        if self.left is not None:
            count += 1
            count += self.left.count_children()
        if self.right is not None:
            count += 1
            count += self.right.count_children()
        return count

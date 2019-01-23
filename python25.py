class node():
    def __init__(self,data,string):
        self.data=data
        self.string=string
        self.next=None
        self.prev=None
        self.down=None

class link_list():
    def __init__(self):
        self.head=None

    def add_node(self,data,string):
        temp1 = None
        new_node=node(data,string)
        new_node1 = node(data, string)
        if self.head==None:
            self.head=new_node
            temp1=self.head
            temp1.down=new_node1
        else:
            temp=self.head
            while temp.next!=None and temp.next.data<data:
                temp=temp.next

            if temp.data==data:
                temp1=temp
            elif temp.prev==None and temp.data>data:
                new_node.next=temp
                temp.prev=new_node
                self.head=new_node
                temp1=self.head
            elif data>temp.data and temp.next!=None:
                new_node.next=temp.next
                new_node.prev=temp
                temp.next.prev=new_node
                temp.next=new_node
                temp1=new_node
            elif temp.next==None:
                new_node.prev=temp
                temp.next=new_node
                temp1=new_node


            temp=temp1
            while temp.down!=None:
                temp=temp.down
            temp.down=new_node1
def CONTACTS1(queries):
    l1=link_list()
    count=[]
    for query in queries:
        if query[0] == 'add':
            l1.add_node(ord(query[1][0]),query[1])
        elif query[0] == 'find':
            counter=0
            temp=l1.head
            while temp.data<ord(query[1][0]) and temp.next!=None:
                temp=temp.next
            if temp.data!=ord(query[1][0]):
                count.append(counter)
                continue
            while temp.down!=None:
                temp=temp.down
                data=temp.string
                if query[1]==data[0:len(query[1])]:
                    counter+=1
            count.append(counter)
    return count

"""           string = sorted(string)
            l=len(string)
            for z in range(l):
                if query[1][0] == string[z][0]:

                    while z<l and string[z][0:len(query[1])] != query[1] and query[1][0] == string[z][0]:
                        z=z+1
                    while(z<l and string[z][0:len(query[1])] == query[1] ):
                        counter+=1
                        z=z+1
                break

            count.append(counter)

    return count"""





def contacts(queries):
    string=[]
    count=[]
    for query in queries:
        if query[0] == 'add':
            string.append(query[1])
        elif query[0] == 'find':
            counter=0
            string = sorted(string)
            l=len(string)
            for z in range(l):
                if query[1][0] == string[z][0]:

                    while z<l and string[z][0:len(query[1])] != query[1] and query[1][0] == string[z][0]:
                        z=z+1
                    while(z<l and string[z][0:len(query[1])] == query[1] ):
                        counter+=1
                        z=z+1
                break

            count.append(counter)

    return count



queries_rows = int(input())

queries = []

for _ in range(queries_rows):
    queries.append(input().rstrip().split())

result = CONTACTS1(queries)

print(result)
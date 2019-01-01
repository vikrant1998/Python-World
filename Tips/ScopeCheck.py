'''
Only the things modified within the list will be affected outside.
if the list is set to something else, then the changes are lost.
'''
def ListScope(l):
    l.pop()
    l.append(6)

'''
Nothing is changed.
'''
def VarScope(var1, var2):
    var1 = "changed"
    var1 = 1
    var2 = 2
'''
Every change is reflected.
'''
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def ChangeNode(node):
    node.val += 1
    node.next = ListNode(node.val + 1)

def ChangeStuff(s):
    s.add(1)

if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5]
    ListScope(l1)
    #print(l1)

    a = "hello"
    b = 1
    VarScope(a, b)
    print(a, b)

    b = [1]
    #VarScope(b)
    #print(b)

    n1 = ListNode(1)
    ChangeNode(n1)
    #print(n1.val)
    #print(n1.next.val)

    s = set()
    m = dict()
    ChangeStuff(s)
    #print(s)

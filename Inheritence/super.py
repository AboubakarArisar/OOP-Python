#super keyword in python

class A:
    def __init__(self):
        print("Init of A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Init of B")


obj = B()

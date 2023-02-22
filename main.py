from tkinter import *
from Node import Node
from BinaryTree import BinaryTree

global tree
tree = BinaryTree()


class BinaryTreeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Binary Tree Builder")

        # Create input fields for PLS , ranges and path
        self.PLS_label = Label(master, text="PLS:")
        self.PLS_label.pack()
        self.PLS_entry = Entry(master)
        self.PLS_entry.pack()

        self.lrange_label = Label(master, text="LRANGE :")
        self.lrange_label.pack()
        self.lrange_entry = Entry(master)
        self.lrange_entry.pack()

        self.rrange_label = Label(master, text="RRANGE :")
        self.rrange_label.pack()
        self.rrange_entry = Entry(master)
        self.rrange_entry.pack()

        self.Path_label = Label(master, text="insert Path:")
        self.Path_label.pack()
        self.Path_entry = Entry(master)
        self.Path_entry.pack()

        # Create a button to add a new node to the tree
        self.add_node_button = Button(master, text="Add Node", command=self.add_node)
        self.add_node_button.pack()

        # Create a button to generate the code for the tree
        self.generate_code_button = Button(master, text="Generate Code", command=self.generate_code)
        self.generate_code_button.pack()

    def add_node(self):
        # Get the PLS and ranges from the user
        pls = self.PLS_entry.get()
        lrange = self.lrange_entry.get()
        rrange = self.rrange_entry.get()
        path = self.Path_entry.get()
        # Create a new data with the PLS and ranges
        data = [pls, lrange, rrange]
        # Add the node to the tree
        tree.add_node(data, path)

        # Clear the input fields
        self.PLS_entry.delete(0, END)
        self.lrange_entry.delete(0, END)
        self.rrange_entry.delete(0, END)
        self.Path_entry.delete(0, END)

    def generate_code(self):
        L=L1=[]
        tree.root.racine(L, L1)
        print(L1)
        #tree.print_preorder()


root = Tk()
my_gui = BinaryTreeGUI(root)
root.mainloop()

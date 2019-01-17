
import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(node.data)

        node = node.next
        if node:
            print(sep)

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    temp=head
    x=0
    new_node=SinglyLinkedListNode(data)
    while x<position-1 and temp.next!=None:
        x=x+1
        temp=temp.next
    if temp.next==None:
        temp.next=new_node
    else:
        new_node.next=temp.next
        temp.next=new_node
    return head




llist_count = int(input())

llist = SinglyLinkedList()

for _ in range(llist_count):
    llist_item = int(input())
    llist.insert_node(llist_item)

data = int(input())

position = int(input())

llist_head = insertNodeAtPosition(llist.head, data, position)
print_singly_linked_list(llist.head, '\n')
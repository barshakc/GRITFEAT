"""
Add two numbersYou are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
https://leetcode.com/problems/add-two-numbers/
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

    def addTwoNums(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(0)
        current = head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carry
            new_digit = sum % 10
            carry = sum // 10

            current.next = ListNode(new_digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return head.next

if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))  
    l2 = ListNode(5, ListNode(6, ListNode(4)))  

    solution = ListNode()
    result = solution.addTwoNums(l1, l2)

    while result:
        print(result.val, end="")
        result = result.next
    print()  
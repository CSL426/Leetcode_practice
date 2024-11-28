# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        current = head

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next
    #  temp.next = l1 or l2  #5
    #     return dummy.next #6

def create_node(nums):
    """
    :type list: List
    :rtype: Optional[ListNode]
    """
    if not nums:
        return None

    head = ListNode(nums[0])
    current = head

    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    
    return head


if __name__ == "__main__":
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    list_node1 = create_node(list1)
    list_node2 = create_node(list2)
    # print(Solution().mergeTwoLists(list1, list2))
    print(list_node2)

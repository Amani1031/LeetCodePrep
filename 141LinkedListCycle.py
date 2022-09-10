from typing import Optional, List

class ListNode:
  def __init__(self, x):
      self.val = x
      self.next = None
  def __repr__(self):
      list_str = str(self.val)
      while True:
          self = self.ref
          if self is None:
              return list_str
          list_str += "-" + str(self.val)

class Solution:
    def hasCycle(head: Optional[ListNode]) -> bool:
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                print(slow)
                print(fast)
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

Solution.hasCycle([3,2,0,-4])
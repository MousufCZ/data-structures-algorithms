// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) {
        this.val = val;
    }
    ListNode(int val, ListNode next) {
        this.val = val; this.next = next;
    }
}

class Solution{
    public ListNode addTwoNumbers(ListNode firstList, ListNode secondList) {
        // Dummy node which willl be the starting point of the result list.
        ListNode dummyNode = new ListNode(0);

        // A variable that will kwwp track of carry
        int carry = 0;

        // This will be used to iterate over the new list.
        ListNode current = dummyNode;

        // Iterate as long as there is a node left in either list or there is a carry-over
        while (firstList != null || secondList != null || carry != 0) {
            int sum = (firstList == null ? 0 : firstList.val) + 
            (secondList == null ? 0 : secondList.val) + carry;

            carry = sum / 10;

            current.next = new ListNode(sum % 10);

            current = current.next;

            firstList = firstList == null ? null : firstList.next;
            secondList = secondList == null ? null : secondList.next;

        }
        return dummyNode.next;
    }
}

public class AddTwoNumbers {
    public static void main(String[] args) {
        ListNode firstList = new ListNode(2, new ListNode(4, new ListNode(3)));
        ListNode secondList = new ListNode(5, new ListNode(6, new ListNode(4)));

        Solution solution = new Solution();
        
        ListNode result = solution.addTwoNumbers(firstList, secondList);
        
        // Print the result
        System.out.print("Result: ");
        while (result != null) {
            System.out.print(result.val);
            if (result.next != null) System.out.print(" -> ");
            result = result.next;
        }

    }
}
package datastructure;

class ListNode {
	int val;
	ListNode next;
	ListNode(int x){
		val = x;
		next = null;
	}
	@Override
	public String toString(){
		return new Integer(val).toString();
	}
}

public class ListNodeDemo {
	public static void main(String[] args){
		int N = 100, pos = 0;
		int[] target = new int[N];
		for(int i = 0; i < N; i++) target[i] = (int)(1000*Math.random());
		ListNode head = ListNodeLink(target);
		while(head != null){
			if (head.val != target[pos++]){
				System.out.println("Not good ListNode Link");
				System.out.println(pos);
				return;
			}
			head = head.next;
		}
		System.out.println("Generate ListNode Link Successfully!");
	}
	public static ListNode ListNodeLink(int[] nums){
		int len = nums.length;
		if (len == 0) return null;
		ListNode head = new ListNode(nums[0]);
		ListNode current = head;
		for(int i = 1; i < len; i++){
			current.next = new ListNode(nums[i]);
			current = current.next;
		}
		return head;
	}
}

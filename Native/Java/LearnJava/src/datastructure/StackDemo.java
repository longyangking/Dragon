package datastructure;

class Stack{
	ListNode top;
	public ListNode peek(){
		if (top != null){
			return top;
		}
		return null;
	}
	public ListNode pop(){
		if (top == null){
			return null;
		}
		ListNode temp = new ListNode(top.val);
		top = top.next;
		return temp;
	}
	public void push(ListNode n){
		if (n != null){
			n.next = top;
			top = n;
		}
	}
	@Override
	public String toString(){
		if (top == null) return null;
		StringBuffer elements = new StringBuffer();
		ListNode current = top;
		while (current != null){
			elements.append(current.val);
			elements.append(",");
			current = current.next;
		}
		return elements.toString();
	}
}

public class StackDemo {
	public static void main(String[] args){
		int N = 10;
		int[] nums = new int[N];
		for(int i = 0; i<N; i++) nums[i] = (int)(1000*Math.random());
		System.out.println("-------------Test Stack----------");
		Stack head = initStack(nums);
		System.out.println(head);
		System.out.println(head.pop());
		System.out.println(head);
	}
	public static Stack initStack(int[] nums){
		int len = nums.length;
		if (len == 0) return null;
		Stack head = new Stack();
		for(int i = 0; i<len; i++) head.push(new ListNode(nums[i]));
		return head;
	}
}

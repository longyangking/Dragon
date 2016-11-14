package datastructure;

class Quene {
	ListNode first, last;
	public void enquene(ListNode n){
		if (first == null){
			first = n;
			last = first;
		} else {
			last.next = n;
			last = n;
		}
	}
	
	public ListNode dequene(){
		if (first == null) return null;
		ListNode temp = new ListNode(first.val);
		first = first.next;
		return temp;
	}
	
	@Override
	public String toString(){
		StringBuffer str  = new StringBuffer();
		ListNode head = first;
		while (head != null){
			str.append(head);
			str.append(",");
			head = head.next;
		}
		return str.toString();
	}
}

public class QueenDemo {
	public static void main(String[] args){
		int N = 10;
		int[] nums = new int[N];
		for(int i = 0; i<N; i++) nums[i] = (int)(Math.random()*100);
		Quene quene = initQuene(nums);
		System.out.println("--------------Init Quene--------------");
		System.out.println(quene);
		System.out.println(quene.dequene());
		System.out.println(quene);
	}
	public static Quene initQuene(int[] nums){
		int len = nums.length;
		if (len == 0) return null;
		Quene quene = new Quene();
		for(int i = 0; i<len; i++){
			ListNode node = new ListNode(nums[i]);
			quene.enquene(node);
		}
		return quene;
	}
}

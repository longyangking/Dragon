package datastructure;

class TreeNode {
	int value;
	TreeNode left;
	TreeNode right;
	public TreeNode(int value){
		this.value = value;
		this.left = null;
		this.right = null;
	}
	@Override 
	public String toString(){
		return new Integer(value).toString();
	}
}

public class TreeDemo {
	public static void main(String[] args){
		System.out.println("---------------- Tree ---------------");
		int N = 10;
		int[] nums = new int[N];
		for(int i = 0; i<N; i++) nums[i] = (int)(100*Math.random());
		for(int i = 0; i<N; i++) System.out.printf("%d ",nums[i]);
		System.out.println("");
		TreeNode tree = initTree(nums);
		printTree(tree);
	}
	public static TreeNode initTree(int[] nums){
		int len = nums.length, pos = 0;
		if (len == 0) return null;
		TreeNode head = new TreeNode(nums[pos++]);
		TreeNode current = head;
		while (pos < len){
			if (current.left == null){
				current.left = new TreeNode(nums[pos++]);
				continue;
			}
			if (current.right == null){
				current.right = new TreeNode(nums[pos++]);
				continue;
			}
			current = current.left;
		}
		return head;
	}
	public static void printTree(TreeNode tree){
		if (tree == null) return;
		System.out.printf("%s ",tree);
		printTree(tree.left);
		printTree(tree.right);
	}
}

package datastructure;

class GraphNode {
	int val;
	GraphNode next;
	GraphNode[] neighbors;
	boolean visited;
	public GraphNode(int x){
		val = x;
	}
	public GraphNode(int x, GraphNode[] n){
		val = x;
		neighbors = n;
	}
	public String toString(){
		return "value: "+this.val;
	}
}

public class GraphDemo {
	public static void main(String[] args){
		
	}
}

package basictypes;

public class BoxMethod {
	public static void main(String[] args){
		AutoBox();
	}
	public static void AutoBox(){
		System.out.println("-----------Test AutoBox------------");
		Integer a = new Integer(3);
		Integer b = 3;
		int c = 3;
		System.out.println(a == b); //False, not same reference
		System.out.println(a == c); //True, compare after unboxing
		
		Integer f1 = 100, f2 = 100, f3 = 150, f4 = 150;
		System.out.println(f1 == f2); //True, IntegerCache.cache[100 + (-IntegerCache.low)];
		System.out.println(f3 == f4); //False, new Integer(150) 
	}
}

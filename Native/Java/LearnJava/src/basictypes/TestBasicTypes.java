package basictypes;

public class TestBasicTypes {
	public static void main(String[] args){
		//TypesInfo();
		//TypeConversion();
		//AutoBox();
		JavaStackAndHeap();
	}
	public static void TypesInfo(){
		/**
		 * 8 kinds of basic types
		 * byte, short, int, long, float, double, char, boolean
		 */
		System.out.println("-----------Test Basic Types------------");
		System.out.println("-----------Byte Info------------");
		System.out.println("Byte MAX: " + Byte.MAX_VALUE);
		System.out.println("Byte MIN: " + Byte.MIN_VALUE);
		System.out.println("Byte BYTES: " + Byte.BYTES);
		System.out.println("Byte BITS: " + Byte.SIZE);
		System.out.println("-----------Integer Info------------");
		System.out.println("Integer MAX: " + Integer.MAX_VALUE);
		System.out.println("Integer MIN: " + Integer.MIN_VALUE);
		System.out.println("Integer BYTES: " + Integer.BYTES);
		System.out.println("Integer BITS: " + Integer.SIZE);
		System.out.println("-----------Float Info------------");
		System.out.println("Float MAX: " + Float.MAX_VALUE);
		System.out.println("Float MIN: " + Float.MIN_VALUE);
		System.out.println("Float BYTES: " + Float.BYTES);
		System.out.println("Float BITS: " + Float.SIZE);
		System.out.println("-----------Double Info------------");
		System.out.println("Double MAX: " + Double.MAX_VALUE);
		System.out.println("Double MIN: " + Double.MIN_VALUE);
		System.out.println("Double BYTES: " + Double.BYTES);
		System.out.println("Double BITS: " + Double.SIZE);
	}
	public static void TypeConversion(){
		System.out.println("-----------Test Type Conversion------------");
		short s1 = 1; 
		s1 = (short)(s1 + 1); //The explicit conversion
		s1 += 1; //The implicit conversion
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
	public static void JavaStackAndHeap(){
		System.out.println("-----------Java Stack & Heap------------");
		String str = new String("Hello World!");
		/**
		 * str : Reference, saved in stack
		 * new String() : Object, saved in heap
		 * "Hello World!" : Data, saved in static area
		 */
		System.out.println(str);
	}
}

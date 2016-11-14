package reflection;

public class TestReflection {
	public static void main(String[] args){
		System.out.println("-----------------Java Reflection Demo------------------");
		Class<?> classdemo = null;
		try {
			classdemo = Class.forName("reflection.ReflectionDemo");
		} catch (ClassNotFoundException e){
			System.out.println("Class not found");
			e.printStackTrace();
		}
		ReflectionDemo demo = null;
		try {
			demo = (ReflectionDemo)classdemo.newInstance();
		} catch(Exception e){
			System.out.println("Error in new instance");
			e.printStackTrace();
		}
		demo.test1();
	}
}

class ReflectionDemo {
	static int staticValue = 0;
	int instanceValue;
	public ReflectionDemo(){
		System.out.println("Constructor 1 : Demo");
		this.instanceValue  = 0;
	}
	{
		//Will run before the constructor
		System.out.println("Extra Code : Demo");
	}
	static {
		//Will run after loading or defining class
		System.out.println("Initiate Static : Demo");
		staticValue = 88;
	}
	public ReflectionDemo(int i){
		System.out.println("Constructor 2 : Demo");
		this.instanceValue = i;
	}
	public void test1(){
		System.out.println("Test 1 : Demo Instance");
	}
	public int test2(){
		System.out.println("Test 2 : Demo Instance");
		return this.instanceValue;
	}
	public int test3(int i){
		System.out.println("Test 3 : Demo Instance");
		return i + 1;
	}
}
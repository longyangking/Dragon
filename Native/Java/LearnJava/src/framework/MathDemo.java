package framework;

public class MathDemo {
	public static void main(String[] args){
		System.out.println("-----------Test Math Module------------");
		Round();
	}
	public static void Round(){
		System.out.println("-----------Math.round------------");
		/**
		 * Math.round(value) = Math.floor(value + 0.5)
		 */
		System.out.println(Math.round(11.5));
		System.out.println(Math.round(-11.5));
	}
}

package reflection;

import java.lang.annotation.*;
import java.lang.reflect.*;

@Retention(RetentionPolicy.RUNTIME)
@interface MyAnnotation {
	String str();
	int val();
}

@Retention(RetentionPolicy.RUNTIME)
@interface What {
	String description();
	String extra() default "Default Extra Info";
}

@What(description = "Class for testing Meta Data")
@MyAnnotation(str = "MetaData Class Sample", val = 9999)
class MetaData {
	@MyAnnotation(str = "MetaData Static Example", val = 100)
	public static void myStaticMethod(){
	}
	
	@MyAnnotation(str = "MetaData Method 1", val = 1)
	public void myMethod(){
		System.out.println("MetaData Method 1");
	}
	@MyAnnotation(str = "MetaData Method 2", val = 2)
	public void myMethod(String s, int i){
		System.out.println("MetaData Method 2");
	}
	@MyAnnotation(str = "MetaData Method 3", val = 3)
	@What(description = "Just a method")
	public void mySpMethod(){
		System.out.println("MetaData Method 3");
	}
}

public class MetaDataDemo {
	public static void main(String[] args){
		getAnnotation();
	}
	public static void getAnnotation(){
		MetaData meta = new MetaData();
		try {
			//Get annotation for static method
			Class<?> c = meta.getClass();
			Method m = c.getMethod("myStaticMethod");
			MyAnnotation anno = m.getAnnotation(MyAnnotation.class);
			System.out.println(anno.str() + ":" + anno.val());
			
			//Get annotation for method 1
			m = c.getMethod("myMethod");
			anno = m.getAnnotation(MyAnnotation.class);
			System.out.println(anno.str() + ":" + anno.val());
			
			//Get annotation for method 2
			m = c.getMethod("myMethod",String.class,int.class);
			anno = m.getAnnotation(MyAnnotation.class);
			System.out.println(anno.str() + ":" + anno.val());
			
			//Print all annotation about class
			Annotation[] annos = c.getAnnotations();
			System.out.println("All annotations for class:");
			for(Annotation a:annos) System.out.println(a);
			
			//Print all annotation about method
			annos = c.getMethod("mySpMethod").getAnnotations();
			System.out.println("All annotations for method:");
			for(Annotation a:annos) System.out.println(a);
		} catch (NoSuchMethodException exc){
			System.out.println("Method not found!");
		}
	}
}

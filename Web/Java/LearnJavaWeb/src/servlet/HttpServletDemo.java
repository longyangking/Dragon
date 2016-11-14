package servlet;
import javax.servlet.http.*;
import java.io.*;

/**
 * The third way to generate Servlet by inheriting class HttpServlet
 * @author LongYang
 *
 */
public class HttpServletDemo extends HttpServlet {
	/**
	 * 
	 */
	private static final long serialVersionUID = -8559245836245282108L;

	/**
	 * Override doGet to process the request GET
	 */
	@Override
	public void doGet(HttpServletRequest req, HttpServletResponse res){
		/**
		 * Service Logic
		 */
		try {
			PrintWriter pw = res.getWriter();
			pw.println("Hello, HttpServlet!");
		} catch(Exception e){
			e.printStackTrace();
		}
	}
	
	/**
	 * Override doPost to process the request POST
	 */
	@Override
	public void doPost(HttpServletRequest req, HttpServletResponse res){
		this.doGet(req, res);
	}
}

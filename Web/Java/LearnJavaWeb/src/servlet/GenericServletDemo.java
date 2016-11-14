package servlet;
import javax.servlet.*;
import java.io.*;

public class GenericServletDemo extends GenericServlet {
	
	/**
	 * Serial Version UID
	 */
	private static final long serialVersionUID = 8949601085893946444L;

	/**
	 * Just rewrite the method service, compared with Servlet
	 */
	@Override
	public void service(ServletRequest req, ServletResponse res) throws ServletException, IOException {
		try {
			PrintWriter pw = res.getWriter();
			pw.println("Hello World! Generic!");
		} catch(Exception e){
			e.printStackTrace();
		}
	}
	
}

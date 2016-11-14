package servlet;
import javax.servlet.*;
import java.io.*;

public class ServletBasicDemo implements Servlet {

	/**
	 * Release the resources
	 * When:
	 * 		1. Reload this servlet (this webapp)
	 * 		2. Close Tomcat
	 * 		3. Shutdown Computer
	 */
	@Override
	public void destroy() {
		System.out.println("Destory it");
	}

	@Override
	public ServletConfig getServletConfig() {
		return null;
	}

	@Override
	public String getServletInfo() {
		return null;
	}

	/**
	 * Initiate servlet, just like constructor in class
	 */
	@Override
	public void init(ServletConfig arg0) throws ServletException {
		System.out.println("Init it");
	}

	/**
	 * Process the industrical logical services
	 * All service code shall be written here
	 * It will be invoked when the user access this servlet
	 * @param req Get information from client (Browser)
	 * @param res Return information to client (Browser)
	 */
	@Override
	public void service(ServletRequest req, ServletResponse res) throws ServletException, IOException {
		System.out.println("Serve it!");
		PrintWriter pw = res.getWriter();
		pw.println("Hellom World");
	}
	
	
}

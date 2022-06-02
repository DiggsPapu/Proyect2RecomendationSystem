package Proyect2;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

import Proyect2.Neo4j;

/**
 * Servlet implementation class CreateUsersServlet
 */
@WebServlet("/CreateUsersServlet")
public class CreateUsersServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public CreateUsersServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		PrintWriter out = response.getWriter();
	 	response.setContentType("application/json");
	 	response.setCharacterEncoding("UTF-8");
	 	JSONObject myResponse = new JSONObject();
	 	String name = request.getParameter("name");
	 	String password = request.getParameter("Password");
	 	String sector1 = request.getParameter("typeSector1");
	 	String sector2 = request.getParameter("typeSector2");
	 	String sector3 = request.getParameter("typeSector3");
	 	int Risk = Integer.valueOf(request.getParameter("risk"));
	 	int rentability = Integer.valueOf(request.getParameter("rent"));
	 	int Size = Integer.valueOf(request.getParameter("size"));
	 	int Books= Integer.valueOf(request.getParameter("books"));
	 	int Fierce = Integer.valueOf(request.getParameter("fierce"));
	 	try ( Neo4j neo4jDriver = new Neo4j( "bolt://localhost:7687", "neo4j", "Manager123" ) )
	        {
			 	String myResultTx = neo4jDriver.insertPerson1(name, password, sector1, sector2, sector3, Risk, rentability, Size, Books, Fierce);
	        	myResponse.put("Resultado", myResultTx);
	        	
	        } catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				myResponse.put("resultado", "Error: " + e.getMessage());
				
			}
	 	
	 	
	 	out.println(myResponse);
	 	out.flush();
	
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}

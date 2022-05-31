/**
 * 
 */
package Proyect2;

import org.neo4j.driver.AuthTokens;
import org.neo4j.driver.Driver;
import org.neo4j.driver.GraphDatabase;
import org.neo4j.driver.Record;
import org.neo4j.driver.Result;
import org.neo4j.driver.Session;
import org.neo4j.driver.Transaction;
import org.neo4j.driver.TransactionWork;
import org.neo4j.driver.summary.ResultSummary;

import static org.neo4j.driver.Values.parameters;

import java.util.LinkedList;
import java.util.List;
/**
 * @author Administrator
 *
 */
public class Neo4j implements AutoCloseable{

    private final Driver driver;
    

    public Neo4j( String uri, String user, String password )
    {
        driver = GraphDatabase.driver( uri, AuthTokens.basic( user, password ) );
    }
    public void close() throws Exception
    {
        driver.close();
    }

//    public void printGreeting( final String message )
//    {
//        try ( Session session = driver.session() )
//        {
//            String greeting = session.writeTransaction( new TransactionWork<String>()
//            {
//                @Override
//                public String execute( Transaction tx )
//                {
//                    Result result = tx.run( "CREATE (a:Greeting) " +
//                                                     "SET a.message = $message " +
//                                                     "RETURN a.message + ', from node ' + id(a)",
//                            parameters( "message", message ) );
//                    return result.single().get( 0 ).asString();
//                }
//            } );
//            System.out.println( greeting );
//        }
//    }
    
//    public LinkedList<String> getBusinesses()
//    {
//    	 try ( Session session = driver.session() )
//         {
//    		 
//    		 
//    		 LinkedList<String> actors = session.readTransaction( new TransactionWork<LinkedList<String>>()
//             {
//                 @Override
//                 public LinkedList<String> execute( Transaction tx )
//                 {
//                     Result result = tx.run( "MATCH (people:Person) RETURN people.name");
//                     LinkedList<String> myactors = new LinkedList<String>();
//                     List<Record> registros = result.list();
//                     for (int i = 0; i < registros.size(); i++) {
//                    	 //myactors.add(registros.get(i).toString());
//                    	 myactors.add(registros.get(i).get("people.name").asString());
//                     }
//                     
//                     return myactors;
//                 }
//             } );
//             
//             return actors;
//         }
//    }
    /**
     * It is to get the people that is compatible with the user
     * @param user
     * @return
     */
//    public LinkedList<String> getCompatiblePersons(final String user)
//    {
//   	 try ( Session session = driver.session() )
//        {
//   		 
//   		 
//   		 LinkedList<String> actors = session.readTransaction( new TransactionWork<LinkedList<String>>()
//            {
//                @Override
//                public LinkedList<String> execute( Transaction tx )
//                {
//                	
//                	Result sector = tx.run( "match (a:user {name: \"" + user + "\"})-[:InterestedInTheSectorOf]->(business)");
//                	Result sizeTheyWant= tx.run( "match (a:user {name: \"" + user + "\"})-[:InterestedInTheSectorOf]->(business)");
//                    LinkedList<String> myactors = new LinkedList<String>();
//                    List<Record> registros = result.list();
//                    for (int i = 0; i < registros.size(); i++) {
//                   	 //myactors.add(registros.get(i).toString());
//                   	 myactors.add(registros.get(i).get("actorMovies.title").asString());
//                    }
//                    
//                    return myactors;
//                }
//            } );
//            
//            return actors;
//        }
//   }
    
public String insertPerson(final int id, String name, final int password, final String rentability, final int size, final String TypeBusiness1, final String TypeBusiness2, final String TypeBusiness3, final String InvestingPotency) {
	try ( Session session = driver.session() ) //Initialize driver
    {
		 
		 String result = session.writeTransaction( new TransactionWork<String>()
		 
        {
            @Override
            public String execute( Transaction tx )
            {
//            	tx.run( "CREATE (b:User {ID:'" + id + "', PASSWORD:"+ password + "', rentability:"+ rentability+ ", size:'"+ size + "', TypeBusiness1:"+ TypeBusiness1+ "', TypeBusiness2:"+ TypeBusiness2+ "', TypeBusiness3:"+ TypeBusiness3+ "', InvestingPotency:"+ InvestingPotency+"'})");
            	tx.run( "CREATE (b:User {ID:'" + id + "', PASSWORD:"+ password +"'})");
                
                return "OK";
            }
        }
		 
		 );
        
        return result;
    } catch (Exception e) {
    	return e.getMessage();
    }
}

public String insertPerson1(final String name, final String password, final String sector1, final String sector2, final String sector3 ) {
	try ( Session session = driver.session() ) //Initialize driver
    {
		 
		 String result = session.writeTransaction( new TransactionWork<String>()
		 
        {
            @Override
            public String execute( Transaction tx )
            {
            	String name1 = new String(name);
            	String password1 = new String(password);
            	
            	String TypeSector1 = new String(sector1);
            	String TypeSector2 = new String(sector2);
            	String TypeSector3 = new String(sector3);
            	boolean val1 = TypeSector1.equals("Bancos") || TypeSector1.equals("Mineria") || TypeSector1.equals("Aerolineas") || TypeSector1.equals("Transporte") || TypeSector1.equals("Energia") || TypeSector1.equals("Mecanica") || TypeSector1.equals("Turismo") || TypeSector1.equals("Quimica") || TypeSector1.equals("Textiles") || TypeSector1.equals("Salud") || TypeSector1.equals("Telecomunicaciones") || TypeSector1.equals("Inmobiliaria");
            	boolean val2 = TypeSector2.equals("Bancos") || TypeSector2.equals("Mineria") || TypeSector2.equals("Aerolineas") || TypeSector2.equals("Transporte") || TypeSector2.equals("Energia") || TypeSector2.equals("Mecanica") || TypeSector2.equals("Turismo") || TypeSector2.equals("Quimica") || TypeSector2.equals("Textiles") || TypeSector2.equals("Salud") || TypeSector2.equals("Telecomunicaciones") || TypeSector2.equals("Inmobiliaria");
            	boolean val3 = TypeSector3.equals("Bancos") || TypeSector3.equals("Mineria") || TypeSector3.equals("Aerolineas") || TypeSector3.equals("Transporte") || TypeSector3.equals("Energia") || TypeSector3.equals("Mecanica") || TypeSector3.equals("Turismo") || TypeSector3.equals("Quimica") || TypeSector3.equals("Textiles") || TypeSector3.equals("Salud") || TypeSector3.equals("Telecomunicaciones") || TypeSector3.equals("Inmobiliaria");
            	
            	if ( val1 && val2 && val3 ) {
            		tx.run( "CREATE ( b : user { name:'" + name1 + "', password:'"+ password1 + "', TypeBusiness1:'"+ TypeSector1 + "', TypeBusiness2:'"+ TypeSector2 + "', TypeBusiness3:'"+ TypeSector3 + "'})");
                	
            	}
            	tx.run( "CREATE ( b : user { name:'" + name1 + "', password:'"+ password1 + "', TypeBusiness1:'"+ TypeSector1 + "', TypeBusiness2:'"+ TypeSector2 + "', TypeBusiness3:'"+ TypeSector3 + "'})");
            	
                return "OK";
            }
        }
		 
		 );
        
        return null;
    } catch (Exception e) {
    	return e.getMessage();
    }
}
}

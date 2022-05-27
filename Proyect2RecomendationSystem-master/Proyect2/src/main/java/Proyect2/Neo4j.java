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
@Override
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
                    tx.run( "CREATE (b:User {ID:'" + id + "', PASSWORD:"+ password + "', rentability:"+ rentability+ ", size:'"+ size + "', TypeBusiness1:"+ TypeBusiness1+ "', TypeBusiness2:"+ TypeBusiness2+ "', TypeBusiness3:"+ TypeBusiness3+ "', InvestingPotency:"+ InvestingPotency+"'})");
                    
                    return "OK";
                }
            }
   		 
   		 );
            
            return result;
        } catch (Exception e) {
        	return e.getMessage();
        }
    }

}

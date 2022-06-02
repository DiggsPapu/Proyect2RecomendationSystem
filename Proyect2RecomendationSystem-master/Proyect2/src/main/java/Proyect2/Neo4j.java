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

public String insertPerson2(final String name, final String password, final String sector1, final String sector2, final String sector3 ) {
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

public String insertPerson1(final String name, final String password, final String sector1, final String sector2, final String sector3, final int risk, final int rent, final int size, final int  books, final int fierce) {
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
            	int risk1 = risk;
            	int rent1 = rent;
            	int size1 = size;
            	int books1 = books;
            	int fierce1 = fierce;
            	
            	tx.run( "CREATE ( b : user { name:'" + name1 + "', password:'" + password1 + "', TypeBusiness1:'" + TypeSector1 + "', TypeBusiness2:'" + TypeSector2 + "', TypeBusiness3:'" + TypeSector3 + "', riesgo:" + risk1 + ", rentabilidad:" + rent1 + ", tamanio:" + size1 + ", libros:" + books1 + ", agresividad:" + fierce1 + "})");
//            	//Match the user with the business sector
//            	tx.run( "match( a : user ), ( b : Business ) where a.TypeBusiness1=b.SECTOR OR a.TypeBusiness2=b.SECTOR OR a.TypeBusiness3=b.SECTOR AND a.name=" + name1 + " AND a.password=" + password1 + " Create(a)-[r:InterestedInTheSectorOf{name: a.name +'<->' + b.name}]->(b)");
//		 		//Match the user with the Business risk
//		 		tx.run( "match( a : USUARIO ),( b : Business ) where a.Risk>=6 AND b.VAR=-10000 AND a.name=" + name1 + "AND a.password=" + password1 + "OR a.Risk=5 AND b.VAR<=0 AND b.VAR<>-10000 AND a.name=" + name1 + " AND a.password=" + password1 + "OR a.Risk=4 AND b.VAR<=0.0015 AND b.VAR>0 AND a.name=" + name1 + " AND a.password=" + password1 + "OR a.Risk=3 AND b.VAR>0.0015 AND b.VAR<=0.004 AND a.name=" + name1 + " AND a.password=" + password1 + "OR a.Risk=2 AND b.VAR>0.004 AND b.VAR<=0.007 AND a.name=" + name1 + " AND a.password=" + password1 + "OR a.Risk=1 AND b.VAR>0.007 AND a.name=" + name1 + " AND a.password=" + password1 + "Create(a)-[r:IdealVariacion{name:a.name+'<->'+b.name}]->(b)");
//		 		//Match the user with the Business Rentability
//		 		tx.run( "match( a : USUARIO ),( b : Business ) where a.Rentabilidad=0 AND b.PER<>-10000 AND b.PER<=700 AND a.name=" + name1 + " AND a.password=" + password1 + "OR a.Rentabilidad=2 AND b.PER>700 AND b.PER<=1400 AND a.name=" + name1 + " AND a.password=" + password1 + "OR a.Rentabilidad=3 AND b.PER>1400 AND b.PER<=2000 AND a.name=" + name1 + " AND a.password=" + password1 + "OR a.Rentabilidad=5 AND b.PER>2000 AND a.name=" + name1 + " AND a.password=" + password1 + " Create(a)-[r:IdealBenefitRelation{name:a.name+'<->'+b.name}]->(b)");
//		 		//Match the user with the Business Size
//		 		tx.run( "match( a : USUARIO ),( b : Business ) where a.Tamanio=0 AND b.COTIZACION<=700 AND a.name=" + name1 + " AND a.password=" + password1 + "OR a.Tamanio=2 AND b.COTIZACION>700 AND b.PER<=4000 AND a.name=" + name1 + " AND a.password=" + password1 + "OR a.Tamanio=3 AND b.COTIZACION>4000 AND b.COTIZACION<=12000 AND a.name=" + name1 + " AND a.password=" + password1 + "OR a.Tamanio=2 AND b.COTIZACION>12000 AND b.COTIZACION<=18000 AND a.name=" + name1 + " AND a.password=" + password1 + "OR a.Tamanio=1 AND b.COTIZACION>18000 AND a.name=" + name1 + " AND a.password=" + password1 + " Create(a)-[r:IdealTamanio{name:a.name+'<->'+b.name}]->(b)");
//		 		//Match the user with the Business Books
//		 		tx.run( "match( a : USUARIO ),( b : Business ) where a.Libros<=0 AND b.PVC<>-10000 AND a.name=" + name1 + " AND a.password=" + password1 + "OR a.Libros=1 AND b.PVC<=100 AND b.PVC<>-10000 AND a.name=" + name1 + " AND a.password=" + password1 + "OR a.Tamanio=2 AND b.PVC>100 AND b.PVC<=300 AND a.name=" + name1 + " AND a.password=" + password1 + "OR a.Libros=3 AND b.PVC>300 AND b.PVC<=700 AND a.name=" + name1 + " AND a.password=" + password1 + "OR a.Libros=4 AND b.PVC>300 AND b.PVC<=700 AND a.name=" + name1 + " AND a.password=" + password1 + "OR a.Libros=5 AND b.PVC>700 AND a.name=" + name1 + " AND a.password=" + password1 + " Create(a)-[r:IdealReporteDeLibros{name:a.name+'<->'+b.name}]->(b)");
//		 		//Match the user with the Business Fierce
//		 		tx.run( "match( a : USUARIO ),( b : Business ) where a.Agresividad<=0 AND b.PEG<>-10000 AND b.PEG<=10 AND a.name=" + name1 + " AND a.password=" + password1 + "OR a.Agresividad=1 AND b.PEG<=40 AND b.PEG>10 AND a.name=" + name1 + " AND a.password=" + password1 + "OR a.Agresividad=2 AND b.PEG>40 AND b.PEG<=1000 AND a.name=" + name1 + " AND a.password=" + password1 + "OR a.Agresividad>=3 AND b.PEG>1000 AND a.name=" + name1 + " AND a.password=" + password1 + "OR a.Libros=4 AND b.PVC>300 AND b.PVC<=700 AND a.name=" + name1 + " AND a.password=" + password1 + "OR a.Libros=5 AND b.PVC>700 AND a.name=" + name1 + " AND a.password=" + password1 + " Create(a)-[r:IdealReporteDeLibros{name:a.name+'<->'+b.name}]->(b)");
////		 		
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

This file is used to demonstrate the SQLi Injection.
Python contains the library named sqli3 which doesn't require the installation of sql. 
import sql3
establish the connection and then connect python and sql3 using cursor (  conn=sql3.connect(users.db) and cursor=conn.cursor() ) 
execute the query and then add the db structure ,insert the values 
create a query to add the username and password and close the connection (conn.close() )
run the file -> enter '' oR '1'=='1' -- in input -> database created 

Enter 
username ='' OR '1'=='1' --' 
where '' represents empty space and 1==1 is always true , -- comments the rest of the statement 

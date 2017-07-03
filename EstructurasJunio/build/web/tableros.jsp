<%@page import="java.io.StringReader"%> 
<%@page import="java.io.FileReader"%>
<%@page import="java.nio.charset.StandardCharsets"%>
<%@page import="java.io.ByteArrayInputStream"%>
<%@page import="java.io.InputStream"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import = "conexion.Conexion" %>
<%@page import= "com.opencsv.*;"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Tableros</title>
        <%Conexion con = new Conexion();%>
    <%String[] coordenadas = con.parametros().split(",");
      CSVReader reader = null;
      String[] nextLine = null;
    %>
    </head>
    
    
    <form action = "disparar.jsp" method = "post">
        Nivel:
        <select name = "nivel">
            <option value="1">1. Satelites</option>
            <option value="2">2. Aviones</option>
            <option value="3">3. Barcos</option>
            <option value="4">4. Submarinos</option>
          </select>
        <br />
        Columna:  <input type = "text" name = "x" size = "50" />
         <br />
        Fila:  <input type = "text" name = "y" size = "50" />     
         
         <br />
         <br />
         <input type = "submit" value = "Disparar" />
      </form>
    
    <br>
    <br>
    <t2>Naves Propias</t2>
    <br>
    <h3>Satelites</h3>
    <table border="1" cellpadding="8">
        
        <%
            try{
                 StringReader read = new StringReader(con.tablero("1", session.getAttribute("nickname").toString()));
                 reader = new CSVReader(read);
                 nextLine = reader.readNext();
            }catch(Exception ex)
            {
            out.println(ex.toString());
            }
           %>
           
    <% for(int a=0;a<Integer.parseInt(coordenadas[1]);a++)
    {  
        %>
    <tr>
         <% for(int b=0;b<Integer.parseInt(coordenadas[0]);b++)
    {  
        %>
        <th> <%
try{
  //eliminar el ciclo, leer de forma más eficiente
     //con.errores("entrando al ciclo");
    // con.errores(String.valueOf(Integer.parseInt(nextLine[0])-1) + " = " + String);
        
           if(nextLine != null)
{
    //con.errores(nextLine[0] + " = " + b + nextLine[1]);
    
if(Integer.parseInt(nextLine[0])-1 == b && Integer.parseInt(nextLine[1])-1 == a)
        {        
           // con.errores(nextLine[2]);
            if(Integer.parseInt(nextLine[2]) == 0)
            {
                %> o <%
            }
            else{
                %> x <%
            }
nextLine = reader.readNext();
        }

}
        

}catch(Exception ex)
{
    
out.println(ex.toString());
System.out.println(ex.toString());
con.errores(ex.toString());
}
       
        %>
        </th>
        <%
            }%>
    </tr>
    <%
    }%>
    </table>
    
        <br>
    <br>
    <% nextLine=null;%>
    <h3>Aviones</h3>
    <table border="1" cellpadding="8">
        
        <%
            try{
                 StringReader read = new StringReader(con.tablero("2", session.getAttribute("nickname").toString()));
                 reader = new CSVReader(read);
                 nextLine = reader.readNext();
            }catch(Exception ex)
            {
            out.println(ex.toString());
            }
           %>
    <% for(int y=0;y<Integer.parseInt(coordenadas[1]);y++)
    {  
        %>
    <tr>
         <% for(int x=0;x<Integer.parseInt(coordenadas[0]);x++)
    {  
        %>
        <th>
            <%
try{
           if(nextLine != null)
{   
if(Integer.parseInt(nextLine[0])-1 == x && Integer.parseInt(nextLine[1])-1 == y)
        {        
            //con.errores(nextLine[2]);
            if(Integer.parseInt(nextLine[2]) == 0)
            {
                %> o <%
            }
            else{
                %> x <%
            }
nextLine = reader.readNext();
        }

}
}catch(Exception ex)
{
    
out.println(ex.toString());
System.out.println(ex.toString());
con.errores(ex.toString());
}
       
        %>
        </th>
        <%
            }%>
    </tr>
    <%
    }%>
    </table>
    
        <br>
    <br>
    
    <% nextLine=null;%>
    <h3>Barcos</h3>
    <table border="1" cellpadding="8">
         <%
            try{
                 StringReader read = new StringReader(con.tablero("3", session.getAttribute("nickname").toString()));
                 reader = new CSVReader(read);
                 nextLine = reader.readNext();
            }catch(Exception ex)
            {
            out.println(ex.toString());
            }
           %>
    <% for(int j=0;j<Integer.parseInt(coordenadas[1]);j++)
    {  
        %>
    <tr>
         <% for(int i=0;i<Integer.parseInt(coordenadas[0]);i++)
    {  
        %>
        <th>
            
            <%
try{
           if(nextLine != null)
{   
if(Integer.parseInt(nextLine[0])-1 == i && Integer.parseInt(nextLine[1])-1 == j)
        {        
            //con.errores(nextLine[2]);
            if(Integer.parseInt(nextLine[2]) == 0)
            {
                %> o <%
            }
            else{
                %> x <%
            }
nextLine = reader.readNext();
        }

}
}catch(Exception ex)
{
    
out.println(ex.toString());
System.out.println(ex.toString());
con.errores(ex.toString());
}
       
        %>
        </th>
        <%
            }%>
    </tr>
    <%
    }%>
    </table>
    
        <br>
    <br>
    
    <% nextLine=null;%>
    <h3>Submarinos</h3>
    <table border="1" cellpadding="8">
         <%
            try{
                 StringReader read = new StringReader(con.tablero("4", session.getAttribute("nickname").toString()));
                 reader = new CSVReader(read);
                 nextLine = reader.readNext();
            }catch(Exception ex)
            {
            out.println(ex.toString());
            }
           %>
    <% for(int yy=0;yy<Integer.parseInt(coordenadas[1]);yy++)
    {  
        %>
    <tr>
         <% for(int xx=0;xx<Integer.parseInt(coordenadas[0]);xx++)
    {  
        %>
        <th>
            <%
try{
           if(nextLine != null)
{   
if(Integer.parseInt(nextLine[0])-1 == xx && Integer.parseInt(nextLine[1])-1 == yy)
        {        
            //con.errores(nextLine[2]);
            if(Integer.parseInt(nextLine[2]) == 0)
            {
                %> o <%
            }
            else{
                %> x <%
            }
nextLine = reader.readNext();
        }

}
}catch(Exception ex)
{
    
out.println(ex.toString());
System.out.println(ex.toString());
con.errores(ex.toString());
}
       
        %>
        </th>
        <%
            }%>
    </tr>
    <%
    }%>
    </table>
    
    <br>
    <br>
    <t2>Naves Enemigas</t2>
    <br>
        <h3>Satelites</h3>
    <table border="1" cellpadding="8">
    <% for(int y=0;y<Integer.parseInt(coordenadas[1]);y++)
    {  
        %>
    <tr>
         <% for(int x=0;x<Integer.parseInt(coordenadas[0]);x++)
    {  
        %>
        <th></th>
        <%
            }%>
    </tr>
    <%
    }%>
    </table>
    
        <br>
    <br>
    
    <h3>Aviones</h3>
    <table border="1" cellpadding="8">
    <% for(int y=0;y<Integer.parseInt(coordenadas[1]);y++)
    {  
        %>
    <tr>
         <% for(int x=0;x<Integer.parseInt(coordenadas[0]);x++)
    {  
        %>
        <th></th>
        <%
            }%>
    </tr>
    <%
    }%>
    </table>
    
        <br>
    <br>
    
    
    <h3>Barcos</h3>
    <table border="1" cellpadding="8">
    <% for(int y=0;y<Integer.parseInt(coordenadas[1]);y++)
    {  
        %>
    <tr>
         <% for(int x=0;x<Integer.parseInt(coordenadas[0]);x++)
    {  
        %>
        <th></th>
        <%
            }%>
    </tr>
    <%
    }%>
    </table>
    
        <br>
    <br>
    
    
    <h3>Submarinos</h3>
    <table border="1" cellpadding="8">
    <% for(int y=0;y<Integer.parseInt(coordenadas[1]);y++)
    {  
        %>
    <tr>
         <% for(int x=0;x<Integer.parseInt(coordenadas[0]);x++)
    {  
        %>
        <th></th>
        <%
            }%>
    </tr>
    <%
    }%>
    </table>
    
    
    </body>
</html>

<%@page import = "conexion.Conexion"  %>
<%@page import= "com.opencsv.*;"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Consultas</title>
    </head>
    <body>
        <%
    Conexion con = new Conexion();
    String[] datos = con.conjuegos("hola").split(",");
    String[] usuarios = con.conusuarios("hola").split(",");
      
      String primero = datos[0];
    String ultimo = datos[datos.length-1];
    %>
    <h3>Partida con menos tiros: </h3>
    <%
     out.print(primero.toString());
     %>
     <h3>Partida con mas tiros: </h3>
       <%      
        out.print(ultimo.toString());
    %>
    
    <h3>Top 10 usuarios:</h3>
    
    <%try{
        for(int i=usuarios.length-1;i>0;i--)
        {
            out.print("usuario: " + usuarios[i]);
            %>
            <br>
            <%
        }
    }catch(Exception ex){
        out.print(ex.toString());
    }
        %>
    
    </body>
</html>

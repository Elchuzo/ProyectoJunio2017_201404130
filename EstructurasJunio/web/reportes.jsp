<%@page import = "conexion.Conexion"  %>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<%Conexion con = new Conexion();%>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <h1>Matriz</h1>
        <h2>satelites</h2>
        <%
            
        out.println("<img src=\"" + con.graficar("matriz",session.getAttribute("nickname").toString(),"satelites") + "\">");
               
        %>
        <br>
        <br>
        <br>
        <h2>barcos</h2>
        <%
            
        out.println("<img src=\"" + con.graficar("matriz",session.getAttribute("nickname").toString(),"barcos") + "\">");
               
        %>
        <br>
        <br>
        <br>
        <h2>aviones</h2>
        <%
            
        out.println("<img src=\"" + con.graficar("matriz",session.getAttribute("nickname").toString(),"aviones") + "\">");
                
        %>
        <br>
        <br>
        <br>
        <h2>submarinos</h2>
        <%
            
        out.println("<img src=\"" + con.graficar("matriz",session.getAttribute("nickname").toString(),"submarinos") + "\">");
           
        %>
        
        <br>
        <br>
        <br>
        <h2>arbol</h2>
        <%
            
        out.println("<img src=\"" + con.graficar("arbol",session.getAttribute("nickname").toString(),"arbol") + "\">");
           
        %>
        
        <br>
        <br>
        <br>
        <h2>arbol con listas</h2>
        <%
            
        out.println("<img src=\"" + con.graficar("arbolconlistas",session.getAttribute("nickname").toString(),"arbolconlistas") + "\">");
           
        %>
        
    </body>
</html>

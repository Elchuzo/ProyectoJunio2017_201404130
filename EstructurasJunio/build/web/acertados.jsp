<%@page import = "conexion.Conexion"  %>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<%Conexion con = new Conexion();%>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Tiros Acertados</title>
    </head>
    <body>
        <h1>Cubo</h1>
        <h2>satelites</h2>
        <%
            
        out.println("<img src=\"" + con.graficar("fallados",session.getAttribute("nickname").toString(),"satelites") + "\">");
               
        %>
        <br>
        <br>
        <br>
        <h2>barcos</h2>
        <%
            
        out.println("<img src=\"" + con.graficar("fallados",session.getAttribute("nickname").toString(),"barcos") + "\">");
               
        %>
        <br>
        <br>
        <br>
        <h2>aviones</h2>
        <%
            
        out.println("<img src=\"" + con.graficar("fallados",session.getAttribute("nickname").toString(),"aviones") + "\">");
                
        %>
        <br>
        <br>
        <br>
        <h2>submarinos</h2>
        <%
            
        out.println("<img src=\"" + con.graficar("fallados",session.getAttribute("nickname").toString(),"submarinos") + "\">");
           
        %>
        
        <br>
        <br>
        <br>
    </body>
</html>

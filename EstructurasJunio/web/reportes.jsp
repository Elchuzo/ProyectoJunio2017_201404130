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

<%@page import = "conexion.Conexion"  %>
<%
    Conexion con = new Conexion();
    String nickname = request.getParameter("usuario");
    String contrasena = request.getParameter("contrasena");
    
    if (con.registrar(nickname, contrasena)){
        response.sendRedirect("exito.jsp");
    } else {
        out.println("Invalid password <a href='index.jsp'>try again</a>");
    }
%>
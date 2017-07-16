<%@page import = "conexion.Conexion"  %>
<%
    Conexion con = new Conexion();
    String parametro = request.getParameter("parametro");
       con.param(parametro);
       response.sendRedirect("opciones.jsp");

%>
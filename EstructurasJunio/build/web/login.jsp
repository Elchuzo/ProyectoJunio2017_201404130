<%@page import = "conexion.Conexion"  %>
<%
    Conexion con = new Conexion();
    String nickname = request.getParameter("usuario");
    String contrasena = request.getParameter("contrasena");
    if (con.iniciar(nickname, contrasena)) {
        session.setAttribute("nickname", nickname);
        //out.println("welcome " + userid);
        //out.println("<a href='logout.jsp'>Log out</a>");
       response.sendRedirect("estParametro.jsp");
      
    } else {
        out.println("Contraseña incorrecta <a href='Inicio.jsp'> intentelo de nuevo</a>");
    }
%>
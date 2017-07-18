<%@page import = "conexion.Conexion"  %>
<%
    Conexion con = new Conexion();
    String nombre = session.getAttribute("nickname").toString();
    String contacto = request.getParameter("usuario");
    String nuevo = request.getParameter("nuevo");
        
        //session.setAttribute("nombre", nombre);
        con.elcontacto(nombre, contacto, nuevo);
        //out.println("welcome " + userid);
        //out.println("<a href='logout.jsp'>Log out</a>");
       response.sendRedirect("contactos.jsp");
      

%>
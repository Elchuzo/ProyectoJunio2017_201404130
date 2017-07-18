<%@page import = "conexion.Conexion"  %>
<%
    Conexion con = new Conexion();
    String nombre = session.getAttribute("nickname").toString();
    String contacto = request.getParameter("contacto");
        
        //session.setAttribute("nombre", nombre);
        con.eliminarcont(nombre, contacto); 
        //out.println("welcome " + userid);
        //out.println("<a href='logout.jsp'>Log out</a>");
       response.sendRedirect("contactos.jsp");
      

%>
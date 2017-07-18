<%@page import = "conexion.Conexion"  %>
<%
    Conexion con = new Conexion();
    String nombre = session.getAttribute("nickname").toString();
    String tiro = request.getParameter("tiro");
    String x = request.getParameter("x");
    String y = request.getParameter("y");
    String xx = request.getParameter("xx");
    String yy = request.getParameter("yy");
        
        //session.setAttribute("nombre", nombre);
        con.editarb(tiro, x, y,xx,yy); 
        //out.println("welcome " + userid);
        //out.println("<a href='logout.jsp'>Log out</a>");
       response.sendRedirect("historialjuego.jsp");
      

%>
<%@page import = "conexion.Conexion"  %>
<%
    Conexion con = new Conexion();
    String nickname = session.getAttribute("nickname").toString();
    String nivel = request.getParameter("nivel");
    String posx = request.getParameter("x");
    String posy = request.getParameter("y");
    String res = con.disparar(nickname, nivel, posx, posy);
    out.println(res);
    response.sendRedirect(request.getContextPath() + "/tableros.jsp?resultado="+res);
%>

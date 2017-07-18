<%@page import = "conexion.Conexion"  %>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<%Conexion con = new Conexion();%>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Reportes</title>
        <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
   </head>
   
   <body>
              <nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">Battleship</a>
    </div>
    <ul class="nav navbar-nav">
      <li><a href="#">Home</a></li>
      <li ><a href="carga.jsp">Cargar Archivo</a></li>
      <li><a href="menugraficas.jsp">Historial</a></li>
      <li class="active"> <a href="menugraficas.jsp">Reportes</a></li>
      <li><a href="consultas.jsp">Consultas</a></li>
      <li><a href="tableros.jsp">Juego Actual</a></li>
      <li><a href="Cerrar.jsp">Cerrar Sesión</a></li>
    </ul>
  </div>
</nav>
    </head>
    <body>
        
        <h2>Contactos</h2>
        <%
            
        out.println("<img src=\"" + con.graficar("contactos",session.getAttribute("nickname").toString(),"arbol") + "\">");
           
        %>

        <form action="eliminarcontacto.jsp">
            <input type="text" class="form-control" id="contacto" name="contacto" placeholder="contacto">
            <br>
        <button class="btn btn-default btn-lg pull-left">Eliminar contacto</button>
        </form>
        <br>
        <form action="editarcontacto.jsp">
            <input type="text" class="form-control" id="usuario" name="usuario" placeholder="Usuario">
            <br>
            <input type="text" class="form-control" id="nuevo" name="nuevo" placeholder="Nuevo">
            <br>
        <button class="btn btn-default btn-lg pull-left">editar contacto</button>
        </form>
        
    </body>
</html>
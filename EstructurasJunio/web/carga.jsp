<%-- 
    Document   : carga
    Created on : 26/06/2017, 06:33:15 PM
    Author     : Oscar
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
   <head>
      <title>Cargar Archivos</title>
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
      <li class="active"><a href="carga.jsp">Cargar Archivo</a></li>
      <li><a href="historialjuego.jsp">Historial</a></li>
      <li><a href="menugraficas.jsp">Reportes</a></li>
      <li><a href="consultas.jsp">Consultas</a></li>
      <li><a href="tableros.jsp">Juego Actual</a></li>
      <li><a href="Cerrar.jsp">Cerrar Sesión</a></li>
    </ul>
  </div>
</nav>
       
      <h1>Cargar</h1>
      <br/>
      <h3>Usuarios: </h3>
      <form action = "file.jsp" method = "post"
         enctype = "multipart/form-data">
         <input type = "file" name = "usuarios" size = "50" />
         <br />
         <br />
         <input type = "submit" value = "Cargar" />
      </form>
      <h3>Naves: </h3>
      <form action = "file.jsp" method = "post"
         enctype = "multipart/form-data">
         <input type = "file" name = "naves" size = "50" />
         <br />
         <br />
         <input type = "submit" value = "Cargar" />
      </form>
      <h3>Partidas: </h3>
      <form action = "file.jsp" method = "post"
         enctype = "multipart/form-data">
         <input type = "file" name = "partidas" size = "50" />
         <br />
         <br />
         <input type = "submit" value = "Cargar" />
      </form>
      <h3>Juego Actual: </h3>
      <form action = "file.jsp" method = "post"
         enctype = "multipart/form-data">
         <input type = "file" name = "juego" size = "50" />
         <br />
         <br />
         <input type = "submit" value = "Cargar" />
      </form>
      <h3>Tiros: </h3>
      <form action = "file.jsp" method = "post"
         enctype = "multipart/form-data">
         <input type = "file" name = "tiros" size = "50" />
         <br />
         <br />
         <input type = "submit" value = "Cargar" />
      </form>
      <h3>Contactos: </h3>
      <form action = "file.jsp" method = "post"
         enctype = "multipart/form-data">
         <input type = "file" name = "contactos" size = "50" />
         <br />
         <br />
         <input type = "submit" value = "Cargar" />
      </form>

      
      
      
   </body>
   
</html>
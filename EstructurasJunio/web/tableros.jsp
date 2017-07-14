<%@page import="java.io.StringReader"%> 
<%@page import="java.io.FileReader"%>
<%@page import="java.nio.charset.StandardCharsets"%>
<%@page import="java.io.ByteArrayInputStream"%>
<%@page import="java.io.InputStream"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import = "conexion.Conexion" %>
<%@page import= "com.opencsv.*;"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link href="css/bootstrap.css" rel="stylesheet">
        <title>Tableros</title>

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
      <li><a href="menugraficas.jsp">Reportes</a></li>
      <li><a href="consultas.jsp">Consultas</a></li>
      <li><a href="tableros.jsp">Juego Actual</a></li>
      <li><a href="Cerrar.jsp">Cerrar Sesión</a></li>
    </ul>
  </div>
</nav>
        <%Conexion con = new Conexion();%>
    <%String[] coordenadas = con.parametros().split(",");
      CSVReader reader = null;
      String[] nextLine = null;
      String res = "..."; 
      res = request.getParameter("resultado");
    %>
    </head>
    
    
    <form action = "disparar.jsp" method = "post">
        Nivel:
        <select name = "nivel">
            <option value="1">1. Satelites</option>
            <option value="2">2. Aviones</option>
            <option value="3">3. Barcos</option>
            <option value="4">4. Submarinos</option>
          </select>
        <br />
        
         <div class="form-group col-xs-12 floating-label-form-group controls">
                                <label for="name">Columna</label>
                                <input type="text" class="form-control" placeholder="Columna" name="x" size="50" required data-validation-required-message="Por favor ingrese una columna.">
        </div>
        <div class="form-group col-xs-12 floating-label-form-group controls">
                                <label for="name">Fila</label>
                                <input type="text" class="form-control" placeholder="Fila" name="y" size="50" required data-validation-required-message="Por favor ingrese una fila.">
        </div>

        <div class="form-group col-xs-12" align="center">
            <button type="submit" class="btn btn-success btn-lg">Disparar</button>
        </div>
         
      </form>
    <%if(res != null)
    {      
        out.print(res);
}%>
    <br>
    <br>
    
    <div class="container">
    <div class="col-sm-6">                

    <h2>Naves Propias</h2>

    <div class="tab">
      <button class="tablinks" onclick="openMap(event, 'Satelites1')" id="defaultOpen">Satelites</button>
      <button class="tablinks" onclick="openMap(event, 'Aviones1')">Aviones</button>
      <button class="tablinks" onclick="openMap(event, 'Barcos1')">Barcos</button>
      <button class="tablinks" onclick="openMap(event, 'Submarinos1')">Submarinos</button>
    </div>

    </div>
    <div class="col-sm-6">

    <h2>Naves Enemigas</h2>  

    <div class="tab">
      <button class="tablinks" onclick="openMap(event, 'Satelites2')">Satelites</button>
      <button class="tablinks" onclick="openMap(event, 'Aviones2')">Aviones</button>
      <button class="tablinks" onclick="openMap(event, 'Barcos2')">Barcos</button>
      <button class="tablinks" onclick="openMap(event, 'Submarinos2')">Submarinos</button>
    </div>

    </div>
    </div>
    
      <hr>
      
      <div id="Satelites1" class="tabcontent">
  <h3>Satelites 1</h3>

  <div class="container">
  <div class="col-sm-2">
      <table class="table table-responsive table-bordered table-he" >
        
          <%
            try{
                 StringReader read = new StringReader(con.tablero("1", session.getAttribute("nickname").toString()));
                 reader = new CSVReader(read);
                 nextLine = reader.readNext();
            }catch(Exception ex)
            {
            out.println(ex.toString());
            }
           %>
          
          <thead>  <!--acá las cabezeras-->
    <tr> 
      <th>1</th>
    </tr>
  </thead>
    <tbody>

                <% for(int a=0;a<Integer.parseInt(coordenadas[1]);a++)
            {  
                %>
            <tr>
                 <% for(int b=0;b<Integer.parseInt(coordenadas[0]);b++)
            {  
                %>
                <td> <%
        try{
          //eliminar el ciclo, leer de forma más eficiente
             //con.errores("entrando al ciclo");
            // con.errores(String.valueOf(Integer.parseInt(nextLine[0])-1) + " = " + String);

                   if(nextLine != null)
        {
            //con.errores(nextLine[0] + " = " + b + nextLine[1]);

        if(Integer.parseInt(nextLine[0])-1 == b && Integer.parseInt(nextLine[1])-1 == a)
                {        
                   // con.errores(nextLine[2]);
                    if(Integer.parseInt(nextLine[2]) == 0)
                    {
                        %> o <%
                    }
                    else{
                        %> x <%
                    }
        nextLine = reader.readNext();
                }

        }


        }catch(Exception ex)
        {

        out.println(ex.toString());
        System.out.println(ex.toString());
        con.errores(ex.toString());
        }

                %>
                </td>
                <%
                    }%>
            </tr>
            <%
            }%>
       
    </tbody>
    </table>
</div>
</div>
</div>
            
      <div id="Aviones1" class="tabcontent">
  <h3>Aviones 1</h3>

  <div class="container">
  <div class="col-sm-2">
      <table class="table table-responsive table-bordered table-he" >
        
          <%
            try{
                 StringReader read = new StringReader(con.tablero("2", session.getAttribute("nickname").toString()));
                 reader = new CSVReader(read);
                 nextLine = reader.readNext();
            }catch(Exception ex)
            {
            out.println(ex.toString());
            }
           %>
          
          <thead>  <!--acá las cabezeras-->
    <tr> 
      <th>1</th>
    </tr>
  </thead>
    <tbody>

                <% for(int a=0;a<Integer.parseInt(coordenadas[1]);a++)
            {  
                %>
            <tr>
                 <% for(int b=0;b<Integer.parseInt(coordenadas[0]);b++)
            {  
                %>
                <td> <%
        try{
          //eliminar el ciclo, leer de forma más eficiente
             //con.errores("entrando al ciclo");
            // con.errores(String.valueOf(Integer.parseInt(nextLine[0])-1) + " = " + String);

                   if(nextLine != null)
        {
            //con.errores(nextLine[0] + " = " + b + nextLine[1]);

        if(Integer.parseInt(nextLine[0])-1 == b && Integer.parseInt(nextLine[1])-1 == a)
                {        
                   // con.errores(nextLine[2]);
                    if(Integer.parseInt(nextLine[2]) == 0)
                    {
                        %> o <%
                    }
                    else{
                        %> x <%
                    }
        nextLine = reader.readNext();
                }

        }


        }catch(Exception ex)
        {

        out.println(ex.toString());
        System.out.println(ex.toString());
        con.errores(ex.toString());
        }

                %>
                </td>
                <%
                    }%>
            </tr>
            <%
            }%>
       
    </tbody>
    </table>
</div>
</div>
</div>
            
    
    <% nextLine=null;%>
    

       <div id="Barcos1" class="tabcontent">
  <h3>Barcos 1</h3>

  <div class="container">
  <div class="col-sm-2">
      <table class="table table-responsive table-bordered table-he" >
        
          <%
            try{
                 StringReader read = new StringReader(con.tablero("3", session.getAttribute("nickname").toString()));
                 reader = new CSVReader(read);
                 nextLine = reader.readNext();
            }catch(Exception ex)
            {
            out.println(ex.toString());
            }
           %>
          
          <thead>  <!--acá las cabezeras-->
    <tr> 
      <th>1</th>
    </tr>
  </thead>
    <tbody>

                <% for(int a=0;a<Integer.parseInt(coordenadas[1]);a++)
            {  
                %>
            <tr>
                 <% for(int b=0;b<Integer.parseInt(coordenadas[0]);b++)
            {  
                %>
                <td> <%
        try{
          //eliminar el ciclo, leer de forma más eficiente
             //con.errores("entrando al ciclo");
            // con.errores(String.valueOf(Integer.parseInt(nextLine[0])-1) + " = " + String);

                   if(nextLine != null)
        {
            //con.errores(nextLine[0] + " = " + b + nextLine[1]);

        if(Integer.parseInt(nextLine[0])-1 == b && Integer.parseInt(nextLine[1])-1 == a)
                {        
                   // con.errores(nextLine[2]);
                    if(Integer.parseInt(nextLine[2]) == 0)
                    {
                        %> o <%
                    }
                    else{
                        %> x <%
                    }
        nextLine = reader.readNext();
                }

        }


        }catch(Exception ex)
        {

        out.println(ex.toString());
        System.out.println(ex.toString());
        con.errores(ex.toString());
        }

                %>
                </td>
                <%
                    }%>
            </tr>
            <%
            }%>
       
    </tbody>
    </table>
</div>
</div>
</div>
    

    
 <div id="Submarinos1" class="tabcontent">
  <h3>Submarinos 1</h3>

  <div class="container">
  <div class="col-sm-2">
      <table class="table table-responsive table-bordered table-he" >
        
          <%
            try{
                 StringReader read = new StringReader(con.tablero("4", session.getAttribute("nickname").toString()));
                 reader = new CSVReader(read);
                 nextLine = reader.readNext();
            }catch(Exception ex)
            {
            out.println(ex.toString());
            }
           %>
          
          <thead>  <!--acá las cabezeras-->
    <tr> 
      <th>1</th>
    </tr>
  </thead>
    <tbody>

                <% for(int a=0;a<Integer.parseInt(coordenadas[1]);a++)
            {  
                %>
            <tr>
                 <% for(int b=0;b<Integer.parseInt(coordenadas[0]);b++)
            {  
                %>
                <td> <%
        try{
          //eliminar el ciclo, leer de forma más eficiente
             //con.errores("entrando al ciclo");
            // con.errores(String.valueOf(Integer.parseInt(nextLine[0])-1) + " = " + String);

                   if(nextLine != null)
        {
            //con.errores(nextLine[0] + " = " + b + nextLine[1]);

        if(Integer.parseInt(nextLine[0])-1 == b && Integer.parseInt(nextLine[1])-1 == a)
                {        
                   // con.errores(nextLine[2]);
                    if(Integer.parseInt(nextLine[2]) == 0)
                    {
                        %> o <%
                    }
                    else{
                        %> x <%
                    }
        nextLine = reader.readNext();
                }

        }


        }catch(Exception ex)
        {

        out.println(ex.toString());
        System.out.println(ex.toString());
        con.errores(ex.toString());
        }

                %>
                </td>
                <%
                    }%>
            </tr>
            <%
            }%>
       
    </tbody>
    </table>
</div>
</div>
</div>
 

            <div id="Satelites2" class="tabcontent">
  <h3>Satelites 2</h3>

  <div class="container">
  <div class="col-sm-2">
      <table class="table table-responsive table-bordered table-he" >
        
          <%
            try{
                 StringReader read = new StringReader(con.tablero("1", con.enemigo(session.getAttribute("nickname").toString())));
                 reader = new CSVReader(read);
                 nextLine = reader.readNext();
            }catch(Exception ex)
            {
            out.println(ex.toString());
            }
           %>
          
          <thead>  <!--acá las cabezeras-->
    <tr> 
      <th>1</th>
    </tr>
  </thead>
    <tbody>

                <% for(int a=0;a<Integer.parseInt(coordenadas[1]);a++)
            {  
                %>
            <tr>
                 <% for(int b=0;b<Integer.parseInt(coordenadas[0]);b++)
            {  
                %>
                <td> <%
        try{
          //eliminar el ciclo, leer de forma más eficiente
             //con.errores("entrando al ciclo");
            // con.errores(String.valueOf(Integer.parseInt(nextLine[0])-1) + " = " + String);

                   if(nextLine != null)
        {
            //con.errores(nextLine[0] + " = " + b + nextLine[1]);

        if(Integer.parseInt(nextLine[0])-1 == b && Integer.parseInt(nextLine[1])-1 == a)
                {        
                   // con.errores(nextLine[2]);
                    if(Integer.parseInt(nextLine[2]) == 0)
                    {
                        %> o <%
                    }
                    else{
                        %> x <%
                    }
        nextLine = reader.readNext();
                }

        }


        }catch(Exception ex)
        {

        out.println(ex.toString());
        System.out.println(ex.toString());
        con.errores(ex.toString());
        }

                %>
                </td>
                <%
                    }%>
            </tr>
            <%
            }%>
       
    </tbody>
    </table>
</div>
</div>
</div>
            
 
            <div id="Aviones2" class="tabcontent">
  <h3>Aviones 2</h3>

  <div class="container">
  <div class="col-sm-2">
      <table class="table table-responsive table-bordered table-he" >
        
          <%
            try{
                 StringReader read = new StringReader(con.tablero("2", con.enemigo(session.getAttribute("nickname").toString())));
                 reader = new CSVReader(read);
                 nextLine = reader.readNext();
            }catch(Exception ex)
            {
            out.println(ex.toString());
            }
           %>
          
          <thead>  <!--acá las cabezeras-->
    <tr> 
      <th>1</th>
    </tr>
  </thead>
    <tbody>

                <% for(int a=0;a<Integer.parseInt(coordenadas[1]);a++)
            {  
                %>
            <tr>
                 <% for(int b=0;b<Integer.parseInt(coordenadas[0]);b++)
            {  
                %>
                <td> <%
        try{
          //eliminar el ciclo, leer de forma más eficiente
             //con.errores("entrando al ciclo");
            // con.errores(String.valueOf(Integer.parseInt(nextLine[0])-1) + " = " + String);

                   if(nextLine != null)
        {
            //con.errores(nextLine[0] + " = " + b + nextLine[1]);

        if(Integer.parseInt(nextLine[0])-1 == b && Integer.parseInt(nextLine[1])-1 == a)
                {        
                   // con.errores(nextLine[2]);
                    if(Integer.parseInt(nextLine[2]) == 0)
                    {
                        %> o <%
                    }
                    else{
                        %> x <%
                    }
        nextLine = reader.readNext();
                }

        }


        }catch(Exception ex)
        {

        out.println(ex.toString());
        System.out.println(ex.toString());
        con.errores(ex.toString());
        }

                %>
                </td>
                <%
                    }%>
            </tr>
            <%
            }%>
       
    </tbody>
    </table>
</div>
</div>
</div>            

            <div id="Barcos2" class="tabcontent">
  <h3>Barcos 2</h3>

  <div class="container">
  <div class="col-sm-2">
      <table class="table table-responsive table-bordered table-he" >
        
          <%
            try{
                 StringReader read = new StringReader(con.tablero("3", con.enemigo(session.getAttribute("nickname").toString())));
                 reader = new CSVReader(read);
                 nextLine = reader.readNext();
            }catch(Exception ex)
            {
            out.println(ex.toString());
            }
           %>
          
          <thead>  <!--acá las cabezeras-->
    <tr> 
      <th>1</th>
    </tr>
  </thead>
    <tbody>

                <% for(int a=0;a<Integer.parseInt(coordenadas[1]);a++)
            {  
                %>
            <tr>
                 <% for(int b=0;b<Integer.parseInt(coordenadas[0]);b++)
            {  
                %>
                <td> <%
        try{
          //eliminar el ciclo, leer de forma más eficiente
             //con.errores("entrando al ciclo");
            // con.errores(String.valueOf(Integer.parseInt(nextLine[0])-1) + " = " + String);

                   if(nextLine != null)
        {
            //con.errores(nextLine[0] + " = " + b + nextLine[1]);

        if(Integer.parseInt(nextLine[0])-1 == b && Integer.parseInt(nextLine[1])-1 == a)
                {        
                   // con.errores(nextLine[2]);
                    if(Integer.parseInt(nextLine[2]) == 0)
                    {
                        %> o <%
                    }
                    else{
                        %> x <%
                    }
        nextLine = reader.readNext();
                }

        }


        }catch(Exception ex)
        {

        out.println(ex.toString());
        System.out.println(ex.toString());
        con.errores(ex.toString());
        }

                %>
                </td>
                <%
                    }%>
            </tr>
            <%
            }%>
       
    </tbody>
    </table>
</div>
</div>
</div>
            
            
             <div id="Submarinos2" class="tabcontent">
  <h3>Submarinos 2</h3>

  <div class="container">
  <div class="col-sm-2">
      <table class="table table-responsive table-bordered table-he" >
        
          <%
            try{
                 StringReader read = new StringReader(con.tablero("4", con.enemigo(session.getAttribute("nickname").toString())));
                 reader = new CSVReader(read);
                 nextLine = reader.readNext();
            }catch(Exception ex)
            {
            out.println(ex.toString());
            }
           %>
          
          <thead>  <!--acá las cabezeras-->
    <tr> 
      <th>1</th>
    </tr>
  </thead>
    <tbody>

                <% for(int a=0;a<Integer.parseInt(coordenadas[1]);a++)
            {  
                %>
            <tr>
                 <% for(int b=0;b<Integer.parseInt(coordenadas[0]);b++)
            {  
                %>
                <td> <%
        try{
          //eliminar el ciclo, leer de forma más eficiente
             //con.errores("entrando al ciclo");
            // con.errores(String.valueOf(Integer.parseInt(nextLine[0])-1) + " = " + String);

                   if(nextLine != null)
        {
            //con.errores(nextLine[0] + " = " + b + nextLine[1]);

        if(Integer.parseInt(nextLine[0])-1 == b && Integer.parseInt(nextLine[1])-1 == a)
                {        
                   // con.errores(nextLine[2]);
                    if(Integer.parseInt(nextLine[2]) == 0)
                    {
                        %> o <%
                    }
                    else{
                        %> x <%
                    }
        nextLine = reader.readNext();
                }

        }


        }catch(Exception ex)
        {

        out.println(ex.toString());
        System.out.println(ex.toString());
        con.errores(ex.toString());
        }

                %>
                </td>
                <%
                    }%>
            </tr>
            <%
            }%>
       
    </tbody>
    </table>
</div>
</div>
</div>
            
 
    <script src="js/scripts1.js"></script>
    <script type="text/javascript">
        document.getElementById("defaultOpen").click();
    </script>
    
    </body>
</html>

<%-- 
    Document   : tableros
    Created on : 19/06/2017, 08:22:16 PM
    Author     : Oscar
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import = "conexion.Conexion"  %>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Tableros</title>
        <%Conexion con = new Conexion();%>
    <%String[] coordenadas = con.parametros().split(",");%>
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
        Columna:  <input type = "text" name = "x" size = "50" />
         <br />
        Fila:  <input type = "text" name = "y" size = "50" />     
         
         <br />
         <br />
         <input type = "submit" value = "Disparar" />
      </form>
    
    <br>
    <br>
    <t2>Naves Propias</t2>
    <br>
    <h3>Satelites</h3>
    <table border="1" cellpadding="8">
    <% for(int a=0;a<Integer.parseInt(coordenadas[1]);a++)
    {  
        %>
    <tr>
         <% for(int b=0;b<Integer.parseInt(coordenadas[0]);b++)
    {  
        %>
        <th></th>
        <%
            }%>
    </tr>
    <%
    }%>
    </table>
    
        <br>
    <br>
    
    <h3>Aviones</h3>
    <table border="1" cellpadding="8">
    <% for(int a=0;a<Integer.parseInt(coordenadas[1]);a++)
    {  
        %>
    <tr>
         <% for(int b=0;b<Integer.parseInt(coordenadas[0]);b++)
    {  
        %>
        <th></th>
        <%
            }%>
    </tr>
    <%
    }%>
    </table>
    
        <br>
    <br>
    
    
    <h3>Barcos</h3>
    <table border="1" cellpadding="8">
    <% for(int a=0;a<Integer.parseInt(coordenadas[1]);a++)
    {  
        %>
    <tr>
         <% for(int b=0;b<Integer.parseInt(coordenadas[0]);b++)
    {  
        %>
        <th></th>
        <%
            }%>
    </tr>
    <%
    }%>
    </table>
    
        <br>
    <br>
    
    
    <h3>Submarinos</h3>
    <table border="1" cellpadding="8">
    <% for(int a=0;a<Integer.parseInt(coordenadas[1]);a++)
    {  
        %>
    <tr>
         <% for(int b=0;b<Integer.parseInt(coordenadas[0]);b++)
    {  
        %>
        <th></th>
        <%
            }%>
    </tr>
    <%
    }%>
    </table>
    
    <br>
    <br>
    <t2>Naves Enemigas</t2>
    <br>
        <h3>Satelites</h3>
    <table border="1" cellpadding="8">
    <% for(int a=0;a<Integer.parseInt(coordenadas[1]);a++)
    {  
        %>
    <tr>
         <% for(int b=0;b<Integer.parseInt(coordenadas[0]);b++)
    {  
        %>
        <th></th>
        <%
            }%>
    </tr>
    <%
    }%>
    </table>
    
        <br>
    <br>
    
    <h3>Aviones</h3>
    <table border="1" cellpadding="8">
    <% for(int a=0;a<Integer.parseInt(coordenadas[1]);a++)
    {  
        %>
    <tr>
         <% for(int b=0;b<Integer.parseInt(coordenadas[0]);b++)
    {  
        %>
        <th></th>
        <%
            }%>
    </tr>
    <%
    }%>
    </table>
    
        <br>
    <br>
    
    
    <h3>Barcos</h3>
    <table border="1" cellpadding="8">
    <% for(int a=0;a<Integer.parseInt(coordenadas[1]);a++)
    {  
        %>
    <tr>
         <% for(int b=0;b<Integer.parseInt(coordenadas[0]);b++)
    {  
        %>
        <th></th>
        <%
            }%>
    </tr>
    <%
    }%>
    </table>
    
        <br>
    <br>
    
    
    <h3>Submarinos</h3>
    <table border="1" cellpadding="8">
    <% for(int a=0;a<Integer.parseInt(coordenadas[1]);a++)
    {  
        %>
    <tr>
         <% for(int b=0;b<Integer.parseInt(coordenadas[0]);b++)
    {  
        %>
        <th></th>
        <%
            }%>
    </tr>
    <%
    }%>
    </table>
    
    
    </body>
</html>

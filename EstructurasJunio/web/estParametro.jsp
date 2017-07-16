<%-- 
    Document   : estParametro
    Created on : 15/07/2017, 08:46:30 PM
    Author     : Abraham Jelkmann
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Parametro B</title>
    </head>
    <body>
        <h3>Establecer parámetro árbol B</h3>
        <form action="param.jsp">
                  
        <div class="row">
            <div class="col-sm-9">
                <div class="row form-group">
                    <div class="col-sm-6">
                        <input type="text" class="form-control" id="parametro" name="parametro" placeholder="Parametro">
                    </div>
                </div>
                <div class="row form-group">
                    <div class="col-sm-6">
                        <button class="btn btn-default btn-lg pull-left">Establecer</button>
                    </div>
                </div>
            </div>
        </div>
        <br>
        </form>
    </body>
</html>

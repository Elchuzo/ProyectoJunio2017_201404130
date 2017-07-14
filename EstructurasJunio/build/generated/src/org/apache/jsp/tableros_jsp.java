package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import java.io.StringReader;
import java.io.FileReader;
import java.nio.charset.StandardCharsets;
import java.io.ByteArrayInputStream;
import java.io.InputStream;
import conexion.Conexion;
import com.opencsv.*;;

public final class tableros_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final JspFactory _jspxFactory = JspFactory.getDefaultFactory();

  private static java.util.List<String> _jspx_dependants;

  private org.glassfish.jsp.api.ResourceInjector _jspx_resourceInjector;

  public java.util.List<String> getDependants() {
    return _jspx_dependants;
  }

  public void _jspService(HttpServletRequest request, HttpServletResponse response)
        throws java.io.IOException, ServletException {

    PageContext pageContext = null;
    HttpSession session = null;
    ServletContext application = null;
    ServletConfig config = null;
    JspWriter out = null;
    Object page = this;
    JspWriter _jspx_out = null;
    PageContext _jspx_page_context = null;

    try {
      response.setContentType("text/html;charset=UTF-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;
      _jspx_resourceInjector = (org.glassfish.jsp.api.ResourceInjector) application.getAttribute("com.sun.appserv.jsp.resource.injector");

      out.write(" \n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("<!DOCTYPE html>\n");
      out.write("<html>\n");
      out.write("    <head>\n");
      out.write("        <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n");
      out.write("        <link href=\"css/bootstrap.css\" rel=\"stylesheet\">\n");
      out.write("        <title>Tableros</title>\n");
      out.write("\n");
      out.write("   </head>\n");
      out.write("   \n");
      out.write("   <body>\n");
      out.write("               <nav class=\"navbar navbar-inverse\">\n");
      out.write("  <div class=\"container-fluid\">\n");
      out.write("    <div class=\"navbar-header\">\n");
      out.write("      <a class=\"navbar-brand\" href=\"#\">Battleship</a>\n");
      out.write("    </div>\n");
      out.write("    <ul class=\"nav navbar-nav\">\n");
      out.write("      <li><a href=\"#\">Home</a></li>\n");
      out.write("      <li class=\"active\"><a href=\"carga.jsp\">Cargar Archivo</a></li>\n");
      out.write("      <li><a href=\"menugraficas.jsp\">Reportes</a></li>\n");
      out.write("      <li><a href=\"consultas.jsp\">Consultas</a></li>\n");
      out.write("      <li><a href=\"tableros.jsp\">Juego Actual</a></li>\n");
      out.write("      <li><a href=\"Cerrar.jsp\">Cerrar Sesión</a></li>\n");
      out.write("    </ul>\n");
      out.write("  </div>\n");
      out.write("</nav>\n");
      out.write("        ");
Conexion con = new Conexion();
      out.write("\n");
      out.write("    ");
String[] coordenadas = con.parametros().split(",");
      CSVReader reader = null;
      String[] nextLine = null;
      String res = "..."; 
      res = request.getParameter("resultado");
    
      out.write("\n");
      out.write("    </head>\n");
      out.write("    \n");
      out.write("    \n");
      out.write("    <form action = \"disparar.jsp\" method = \"post\">\n");
      out.write("        Nivel:\n");
      out.write("        <select name = \"nivel\">\n");
      out.write("            <option value=\"1\">1. Satelites</option>\n");
      out.write("            <option value=\"2\">2. Aviones</option>\n");
      out.write("            <option value=\"3\">3. Barcos</option>\n");
      out.write("            <option value=\"4\">4. Submarinos</option>\n");
      out.write("          </select>\n");
      out.write("        <br />\n");
      out.write("        \n");
      out.write("         <div class=\"form-group col-xs-12 floating-label-form-group controls\">\n");
      out.write("                                <label for=\"name\">Columna</label>\n");
      out.write("                                <input type=\"text\" class=\"form-control\" placeholder=\"Columna\" name=\"x\" size=\"50\" required data-validation-required-message=\"Por favor ingrese una columna.\">\n");
      out.write("        </div>\n");
      out.write("        <div class=\"form-group col-xs-12 floating-label-form-group controls\">\n");
      out.write("                                <label for=\"name\">Fila</label>\n");
      out.write("                                <input type=\"text\" class=\"form-control\" placeholder=\"Fila\" name=\"y\" size=\"50\" required data-validation-required-message=\"Por favor ingrese una fila.\">\n");
      out.write("        </div>\n");
      out.write("\n");
      out.write("        <div class=\"form-group col-xs-12\" align=\"center\">\n");
      out.write("            <button type=\"submit\" class=\"btn btn-success btn-lg\">Disparar</button>\n");
      out.write("        </div>\n");
      out.write("         \n");
      out.write("      </form>\n");
      out.write("    ");
if(res != null)
    {      
        out.print(res);
}
      out.write("\n");
      out.write("    <br>\n");
      out.write("    <br>\n");
      out.write("    \n");
      out.write("    <div class=\"container\">\n");
      out.write("    <div class=\"col-sm-6\">                \n");
      out.write("\n");
      out.write("    <h2>Naves Propias</h2>\n");
      out.write("\n");
      out.write("    <div class=\"tab\">\n");
      out.write("      <button class=\"tablinks\" onclick=\"openMap(event, 'Satelites1')\" id=\"defaultOpen\">Satelites</button>\n");
      out.write("      <button class=\"tablinks\" onclick=\"openMap(event, 'Aviones1')\">Aviones</button>\n");
      out.write("      <button class=\"tablinks\" onclick=\"openMap(event, 'Barcos1')\">Barcos</button>\n");
      out.write("      <button class=\"tablinks\" onclick=\"openMap(event, 'Submarinos1')\">Submarinos</button>\n");
      out.write("    </div>\n");
      out.write("\n");
      out.write("    </div>\n");
      out.write("    <div class=\"col-sm-6\">\n");
      out.write("\n");
      out.write("    <h2>Naves Enemigas</h2>  \n");
      out.write("\n");
      out.write("    <div class=\"tab\">\n");
      out.write("      <button class=\"tablinks\" onclick=\"openMap(event, 'Satelites2')\">Satelites</button>\n");
      out.write("      <button class=\"tablinks\" onclick=\"openMap(event, 'Aviones2')\">Aviones</button>\n");
      out.write("      <button class=\"tablinks\" onclick=\"openMap(event, 'Barcos2')\">Barcos</button>\n");
      out.write("      <button class=\"tablinks\" onclick=\"openMap(event, 'Submarinos2')\">Submarinos</button>\n");
      out.write("    </div>\n");
      out.write("\n");
      out.write("    </div>\n");
      out.write("    </div>\n");
      out.write("    \n");
      out.write("      <hr>\n");
      out.write("      \n");
      out.write("      <div id=\"Satelites1\" class=\"tabcontent\">\n");
      out.write("  <h3>Satelites 1</h3>\n");
      out.write("\n");
      out.write("  <div class=\"container\">\n");
      out.write("  <div class=\"col-sm-2\">\n");
      out.write("      <table class=\"table table-responsive table-bordered table-he\" >\n");
      out.write("        \n");
      out.write("          ");

            try{
                 StringReader read = new StringReader(con.tablero("1", session.getAttribute("nickname").toString()));
                 reader = new CSVReader(read);
                 nextLine = reader.readNext();
            }catch(Exception ex)
            {
            out.println(ex.toString());
            }
           
      out.write("\n");
      out.write("          \n");
      out.write("          <thead>  <!--acá las cabezeras-->\n");
      out.write("    <tr> \n");
      out.write("      <th>1</th>\n");
      out.write("    </tr>\n");
      out.write("  </thead>\n");
      out.write("    <tbody>\n");
      out.write("\n");
      out.write("                ");
 for(int a=0;a<Integer.parseInt(coordenadas[1]);a++)
            {  
                
      out.write("\n");
      out.write("            <tr>\n");
      out.write("                 ");
 for(int b=0;b<Integer.parseInt(coordenadas[0]);b++)
            {  
                
      out.write("\n");
      out.write("                <td> ");

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
                        
      out.write(" o ");

                    }
                    else{
                        
      out.write(" x ");

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

                
      out.write("\n");
      out.write("                </td>\n");
      out.write("                ");

                    }
      out.write("\n");
      out.write("            </tr>\n");
      out.write("            ");

            }
      out.write("\n");
      out.write("       \n");
      out.write("    </tbody>\n");
      out.write("    </table>\n");
      out.write("</div>\n");
      out.write("</div>\n");
      out.write("</div>\n");
      out.write("            \n");
      out.write("      <div id=\"Aviones1\" class=\"tabcontent\">\n");
      out.write("  <h3>Aviones 1</h3>\n");
      out.write("\n");
      out.write("  <div class=\"container\">\n");
      out.write("  <div class=\"col-sm-2\">\n");
      out.write("      <table class=\"table table-responsive table-bordered table-he\" >\n");
      out.write("        \n");
      out.write("          ");

            try{
                 StringReader read = new StringReader(con.tablero("2", session.getAttribute("nickname").toString()));
                 reader = new CSVReader(read);
                 nextLine = reader.readNext();
            }catch(Exception ex)
            {
            out.println(ex.toString());
            }
           
      out.write("\n");
      out.write("          \n");
      out.write("          <thead>  <!--acá las cabezeras-->\n");
      out.write("    <tr> \n");
      out.write("      <th>1</th>\n");
      out.write("    </tr>\n");
      out.write("  </thead>\n");
      out.write("    <tbody>\n");
      out.write("\n");
      out.write("                ");
 for(int a=0;a<Integer.parseInt(coordenadas[1]);a++)
            {  
                
      out.write("\n");
      out.write("            <tr>\n");
      out.write("                 ");
 for(int b=0;b<Integer.parseInt(coordenadas[0]);b++)
            {  
                
      out.write("\n");
      out.write("                <td> ");

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
                        
      out.write(" o ");

                    }
                    else{
                        
      out.write(" x ");

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

                
      out.write("\n");
      out.write("                </td>\n");
      out.write("                ");

                    }
      out.write("\n");
      out.write("            </tr>\n");
      out.write("            ");

            }
      out.write("\n");
      out.write("       \n");
      out.write("    </tbody>\n");
      out.write("    </table>\n");
      out.write("</div>\n");
      out.write("</div>\n");
      out.write("</div>\n");
      out.write("            \n");
      out.write("    \n");
      out.write("    ");
 nextLine=null;
      out.write("\n");
      out.write("    \n");
      out.write("        <br>\n");
      out.write("    <br>\n");
      out.write("    \n");
      out.write("       <div id=\"Barcos1\" class=\"tabcontent\">\n");
      out.write("  <h3>Barcos 1</h3>\n");
      out.write("\n");
      out.write("  <div class=\"container\">\n");
      out.write("  <div class=\"col-sm-2\">\n");
      out.write("      <table class=\"table table-responsive table-bordered table-he\" >\n");
      out.write("        \n");
      out.write("          ");

            try{
                 StringReader read = new StringReader(con.tablero("3", session.getAttribute("nickname").toString()));
                 reader = new CSVReader(read);
                 nextLine = reader.readNext();
            }catch(Exception ex)
            {
            out.println(ex.toString());
            }
           
      out.write("\n");
      out.write("          \n");
      out.write("          <thead>  <!--acá las cabezeras-->\n");
      out.write("    <tr> \n");
      out.write("      <th>1</th>\n");
      out.write("    </tr>\n");
      out.write("  </thead>\n");
      out.write("    <tbody>\n");
      out.write("\n");
      out.write("                ");
 for(int a=0;a<Integer.parseInt(coordenadas[1]);a++)
            {  
                
      out.write("\n");
      out.write("            <tr>\n");
      out.write("                 ");
 for(int b=0;b<Integer.parseInt(coordenadas[0]);b++)
            {  
                
      out.write("\n");
      out.write("                <td> ");

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
                        
      out.write(" o ");

                    }
                    else{
                        
      out.write(" x ");

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

                
      out.write("\n");
      out.write("                </td>\n");
      out.write("                ");

                    }
      out.write("\n");
      out.write("            </tr>\n");
      out.write("            ");

            }
      out.write("\n");
      out.write("       \n");
      out.write("    </tbody>\n");
      out.write("    </table>\n");
      out.write("</div>\n");
      out.write("</div>\n");
      out.write("</div>\n");
      out.write("    \n");
      out.write("        <br>\n");
      out.write("    <br>\n");
      out.write("    \n");
      out.write(" <div id=\"Submarinos1\" class=\"tabcontent\">\n");
      out.write("  <h3>Submarinos 1</h3>\n");
      out.write("\n");
      out.write("  <div class=\"container\">\n");
      out.write("  <div class=\"col-sm-2\">\n");
      out.write("      <table class=\"table table-responsive table-bordered table-he\" >\n");
      out.write("        \n");
      out.write("          ");

            try{
                 StringReader read = new StringReader(con.tablero("4", session.getAttribute("nickname").toString()));
                 reader = new CSVReader(read);
                 nextLine = reader.readNext();
            }catch(Exception ex)
            {
            out.println(ex.toString());
            }
           
      out.write("\n");
      out.write("          \n");
      out.write("          <thead>  <!--acá las cabezeras-->\n");
      out.write("    <tr> \n");
      out.write("      <th>1</th>\n");
      out.write("    </tr>\n");
      out.write("  </thead>\n");
      out.write("    <tbody>\n");
      out.write("\n");
      out.write("                ");
 for(int a=0;a<Integer.parseInt(coordenadas[1]);a++)
            {  
                
      out.write("\n");
      out.write("            <tr>\n");
      out.write("                 ");
 for(int b=0;b<Integer.parseInt(coordenadas[0]);b++)
            {  
                
      out.write("\n");
      out.write("                <td> ");

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
                        
      out.write(" o ");

                    }
                    else{
                        
      out.write(" x ");

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

                
      out.write("\n");
      out.write("                </td>\n");
      out.write("                ");

                    }
      out.write("\n");
      out.write("            </tr>\n");
      out.write("            ");

            }
      out.write("\n");
      out.write("       \n");
      out.write("    </tbody>\n");
      out.write("    </table>\n");
      out.write("</div>\n");
      out.write("</div>\n");
      out.write("</div>\n");
      out.write("    \n");
      out.write("    <br>\n");
      out.write("    <br>\n");
      out.write("\n");
      out.write("\n");
      out.write("    \n");
      out.write("    \n");
      out.write("    <script src=\"js/scripts1.js\"></script>\n");
      out.write("    <script type=\"text/javascript\">\n");
      out.write("        document.getElementById(\"defaultOpen\").click();\n");
      out.write("    </script>\n");
      out.write("    \n");
      out.write("    </body>\n");
      out.write("</html>\n");
    } catch (Throwable t) {
      if (!(t instanceof SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          out.clearBuffer();
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}

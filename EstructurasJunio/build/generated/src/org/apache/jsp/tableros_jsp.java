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
      out.write("        <title>Tableros</title>\n");
      out.write("        ");
Conexion con = new Conexion();
      out.write("\n");
      out.write("    ");
String[] coordenadas = con.parametros().split(",");
      CSVReader reader = null;
      String[] nextLine = null;
    
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
      out.write("        Columna:  <input type = \"text\" name = \"x\" size = \"50\" />\n");
      out.write("         <br />\n");
      out.write("        Fila:  <input type = \"text\" name = \"y\" size = \"50\" />     \n");
      out.write("         \n");
      out.write("         <br />\n");
      out.write("         <br />\n");
      out.write("         <input type = \"submit\" value = \"Disparar\" />\n");
      out.write("      </form>\n");
      out.write("    \n");
      out.write("    <br>\n");
      out.write("    <br>\n");
      out.write("    <t2>Naves Propias</t2>\n");
      out.write("    <br>\n");
      out.write("    <h3>Satelites</h3>\n");
      out.write("    <table border=\"1\" cellpadding=\"8\">\n");
      out.write("        \n");
      out.write("        ");

            try{
                 StringReader read = new StringReader(con.tablero("1", session.getAttribute("nickname").toString()));
                 reader = new CSVReader(read);
                 nextLine = reader.readNext();
            }catch(Exception ex)
            {
            out.println(ex.toString());
            }
           
      out.write("\n");
      out.write("           \n");
      out.write("    ");
 for(int a=0;a<Integer.parseInt(coordenadas[1]);a++)
    {  
        
      out.write("\n");
      out.write("    <tr>\n");
      out.write("         ");
 for(int b=0;b<Integer.parseInt(coordenadas[0]);b++)
    {  
        
      out.write("\n");
      out.write("        <th> ");

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
      out.write("        </th>\n");
      out.write("        ");

            }
      out.write("\n");
      out.write("    </tr>\n");
      out.write("    ");

    }
      out.write("\n");
      out.write("    </table>\n");
      out.write("    \n");
      out.write("        <br>\n");
      out.write("    <br>\n");
      out.write("    ");
 nextLine=null;
      out.write("\n");
      out.write("    <h3>Aviones</h3>\n");
      out.write("    <table border=\"1\" cellpadding=\"8\">\n");
      out.write("        \n");
      out.write("        ");

            try{
                 StringReader read = new StringReader(con.tablero("2", session.getAttribute("nickname").toString()));
                 reader = new CSVReader(read);
                 nextLine = reader.readNext();
            }catch(Exception ex)
            {
            out.println(ex.toString());
            }
           
      out.write("\n");
      out.write("    ");
 for(int y=0;y<Integer.parseInt(coordenadas[1]);y++)
    {  
        
      out.write("\n");
      out.write("    <tr>\n");
      out.write("         ");
 for(int x=0;x<Integer.parseInt(coordenadas[0]);x++)
    {  
        
      out.write("\n");
      out.write("        <th>\n");
      out.write("            ");

try{
           if(nextLine != null)
{   
if(Integer.parseInt(nextLine[0])-1 == x && Integer.parseInt(nextLine[1])-1 == y)
        {        
            //con.errores(nextLine[2]);
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
      out.write("        </th>\n");
      out.write("        ");

            }
      out.write("\n");
      out.write("    </tr>\n");
      out.write("    ");

    }
      out.write("\n");
      out.write("    </table>\n");
      out.write("    \n");
      out.write("        <br>\n");
      out.write("    <br>\n");
      out.write("    \n");
      out.write("    ");
 nextLine=null;
      out.write("\n");
      out.write("    <h3>Barcos</h3>\n");
      out.write("    <table border=\"1\" cellpadding=\"8\">\n");
      out.write("         ");

            try{
                 StringReader read = new StringReader(con.tablero("3", session.getAttribute("nickname").toString()));
                 reader = new CSVReader(read);
                 nextLine = reader.readNext();
            }catch(Exception ex)
            {
            out.println(ex.toString());
            }
           
      out.write("\n");
      out.write("    ");
 for(int j=0;j<Integer.parseInt(coordenadas[1]);j++)
    {  
        
      out.write("\n");
      out.write("    <tr>\n");
      out.write("         ");
 for(int i=0;i<Integer.parseInt(coordenadas[0]);i++)
    {  
        
      out.write("\n");
      out.write("        <th>\n");
      out.write("            \n");
      out.write("            ");

try{
           if(nextLine != null)
{   
if(Integer.parseInt(nextLine[0])-1 == i && Integer.parseInt(nextLine[1])-1 == j)
        {        
            //con.errores(nextLine[2]);
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
      out.write("        </th>\n");
      out.write("        ");

            }
      out.write("\n");
      out.write("    </tr>\n");
      out.write("    ");

    }
      out.write("\n");
      out.write("    </table>\n");
      out.write("    \n");
      out.write("        <br>\n");
      out.write("    <br>\n");
      out.write("    \n");
      out.write("    ");
 nextLine=null;
      out.write("\n");
      out.write("    <h3>Submarinos</h3>\n");
      out.write("    <table border=\"1\" cellpadding=\"8\">\n");
      out.write("         ");

            try{
                 StringReader read = new StringReader(con.tablero("4", session.getAttribute("nickname").toString()));
                 reader = new CSVReader(read);
                 nextLine = reader.readNext();
            }catch(Exception ex)
            {
            out.println(ex.toString());
            }
           
      out.write("\n");
      out.write("    ");
 for(int yy=0;yy<Integer.parseInt(coordenadas[1]);yy++)
    {  
        
      out.write("\n");
      out.write("    <tr>\n");
      out.write("         ");
 for(int xx=0;xx<Integer.parseInt(coordenadas[0]);xx++)
    {  
        
      out.write("\n");
      out.write("        <th>\n");
      out.write("            ");

try{
           if(nextLine != null)
{   
if(Integer.parseInt(nextLine[0])-1 == xx && Integer.parseInt(nextLine[1])-1 == yy)
        {        
            //con.errores(nextLine[2]);
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
      out.write("        </th>\n");
      out.write("        ");

            }
      out.write("\n");
      out.write("    </tr>\n");
      out.write("    ");

    }
      out.write("\n");
      out.write("    </table>\n");
      out.write("    \n");
      out.write("    <br>\n");
      out.write("    <br>\n");
      out.write("    <t2>Naves Enemigas</t2>\n");
      out.write("    <br>\n");
      out.write("        <h3>Satelites</h3>\n");
      out.write("    <table border=\"1\" cellpadding=\"8\">\n");
      out.write("    ");
 for(int y=0;y<Integer.parseInt(coordenadas[1]);y++)
    {  
        
      out.write("\n");
      out.write("    <tr>\n");
      out.write("         ");
 for(int x=0;x<Integer.parseInt(coordenadas[0]);x++)
    {  
        
      out.write("\n");
      out.write("        <th></th>\n");
      out.write("        ");

            }
      out.write("\n");
      out.write("    </tr>\n");
      out.write("    ");

    }
      out.write("\n");
      out.write("    </table>\n");
      out.write("    \n");
      out.write("        <br>\n");
      out.write("    <br>\n");
      out.write("    \n");
      out.write("    <h3>Aviones</h3>\n");
      out.write("    <table border=\"1\" cellpadding=\"8\">\n");
      out.write("    ");
 for(int y=0;y<Integer.parseInt(coordenadas[1]);y++)
    {  
        
      out.write("\n");
      out.write("    <tr>\n");
      out.write("         ");
 for(int x=0;x<Integer.parseInt(coordenadas[0]);x++)
    {  
        
      out.write("\n");
      out.write("        <th></th>\n");
      out.write("        ");

            }
      out.write("\n");
      out.write("    </tr>\n");
      out.write("    ");

    }
      out.write("\n");
      out.write("    </table>\n");
      out.write("    \n");
      out.write("        <br>\n");
      out.write("    <br>\n");
      out.write("    \n");
      out.write("    \n");
      out.write("    <h3>Barcos</h3>\n");
      out.write("    <table border=\"1\" cellpadding=\"8\">\n");
      out.write("    ");
 for(int y=0;y<Integer.parseInt(coordenadas[1]);y++)
    {  
        
      out.write("\n");
      out.write("    <tr>\n");
      out.write("         ");
 for(int x=0;x<Integer.parseInt(coordenadas[0]);x++)
    {  
        
      out.write("\n");
      out.write("        <th></th>\n");
      out.write("        ");

            }
      out.write("\n");
      out.write("    </tr>\n");
      out.write("    ");

    }
      out.write("\n");
      out.write("    </table>\n");
      out.write("    \n");
      out.write("        <br>\n");
      out.write("    <br>\n");
      out.write("    \n");
      out.write("    \n");
      out.write("    <h3>Submarinos</h3>\n");
      out.write("    <table border=\"1\" cellpadding=\"8\">\n");
      out.write("    ");
 for(int y=0;y<Integer.parseInt(coordenadas[1]);y++)
    {  
        
      out.write("\n");
      out.write("    <tr>\n");
      out.write("         ");
 for(int x=0;x<Integer.parseInt(coordenadas[0]);x++)
    {  
        
      out.write("\n");
      out.write("        <th></th>\n");
      out.write("        ");

            }
      out.write("\n");
      out.write("    </tr>\n");
      out.write("    ");

    }
      out.write("\n");
      out.write("    </table>\n");
      out.write("    \n");
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

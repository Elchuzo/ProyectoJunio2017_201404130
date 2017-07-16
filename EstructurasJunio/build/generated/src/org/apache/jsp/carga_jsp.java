package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;

public final class carga_jsp extends org.apache.jasper.runtime.HttpJspBase
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

      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("<!DOCTYPE html>\n");
      out.write("<html>\n");
      out.write("   <head>\n");
      out.write("      <title>Cargar Archivos</title>\n");
      out.write("      <meta charset=\"utf-8\">\n");
      out.write("  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n");
      out.write("  <link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css\">\n");
      out.write("  <script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js\"></script>\n");
      out.write("  <script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js\"></script>\n");
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
      out.write("      <li><a href=\"historialjuego.jsp\">Historial</a></li>\n");
      out.write("      <li><a href=\"menugraficas.jsp\">Reportes</a></li>\n");
      out.write("      <li><a href=\"consultas.jsp\">Consultas</a></li>\n");
      out.write("      <li><a href=\"tableros.jsp\">Juego Actual</a></li>\n");
      out.write("      <li><a href=\"Cerrar.jsp\">Cerrar Sesión</a></li>\n");
      out.write("    </ul>\n");
      out.write("  </div>\n");
      out.write("</nav>\n");
      out.write("       \n");
      out.write("      <h1>Cargar</h1>\n");
      out.write("      <br/>\n");
      out.write("      <h3>Usuarios: </h3>\n");
      out.write("      <form action = \"file.jsp\" method = \"post\"\n");
      out.write("         enctype = \"multipart/form-data\">\n");
      out.write("         <input type = \"file\" name = \"usuarios\" size = \"50\" />\n");
      out.write("         <br />\n");
      out.write("         <br />\n");
      out.write("         <input type = \"submit\" value = \"Cargar\" />\n");
      out.write("      </form>\n");
      out.write("      <h3>Naves: </h3>\n");
      out.write("      <form action = \"file.jsp\" method = \"post\"\n");
      out.write("         enctype = \"multipart/form-data\">\n");
      out.write("         <input type = \"file\" name = \"naves\" size = \"50\" />\n");
      out.write("         <br />\n");
      out.write("         <br />\n");
      out.write("         <input type = \"submit\" value = \"Cargar\" />\n");
      out.write("      </form>\n");
      out.write("      <h3>Partidas: </h3>\n");
      out.write("      <form action = \"file.jsp\" method = \"post\"\n");
      out.write("         enctype = \"multipart/form-data\">\n");
      out.write("         <input type = \"file\" name = \"partidas\" size = \"50\" />\n");
      out.write("         <br />\n");
      out.write("         <br />\n");
      out.write("         <input type = \"submit\" value = \"Cargar\" />\n");
      out.write("      </form>\n");
      out.write("      <h3>Juego Actual: </h3>\n");
      out.write("      <form action = \"file.jsp\" method = \"post\"\n");
      out.write("         enctype = \"multipart/form-data\">\n");
      out.write("         <input type = \"file\" name = \"juego\" size = \"50\" />\n");
      out.write("         <br />\n");
      out.write("         <br />\n");
      out.write("         <input type = \"submit\" value = \"Cargar\" />\n");
      out.write("      </form>\n");
      out.write("      <h3>Tiros: </h3>\n");
      out.write("      <form action = \"file.jsp\" method = \"post\"\n");
      out.write("         enctype = \"multipart/form-data\">\n");
      out.write("         <input type = \"file\" name = \"tiros\" size = \"50\" />\n");
      out.write("         <br />\n");
      out.write("         <br />\n");
      out.write("         <input type = \"submit\" value = \"Cargar\" />\n");
      out.write("      </form>\n");
      out.write("      <h3>Contactos: </h3>\n");
      out.write("      <form action = \"file.jsp\" method = \"post\"\n");
      out.write("         enctype = \"multipart/form-data\">\n");
      out.write("         <input type = \"file\" name = \"contactos\" size = \"50\" />\n");
      out.write("         <br />\n");
      out.write("         <br />\n");
      out.write("         <input type = \"submit\" value = \"Cargar\" />\n");
      out.write("      </form>\n");
      out.write("\n");
      out.write("      \n");
      out.write("      \n");
      out.write("      \n");
      out.write("   </body>\n");
      out.write("   \n");
      out.write("</html>");
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

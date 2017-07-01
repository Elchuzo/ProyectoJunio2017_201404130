package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;

public final class Inicio_jsp extends org.apache.jasper.runtime.HttpJspBase
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
      out.write("<!DOCTYPE html>\n");
      out.write("<html>\n");
      out.write("    <head>\n");
      out.write("<meta charset=\"utf-8\">\n");
      out.write("    <title>Iniciar Sesión</title>\n");
      out.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n");
      out.write("    <meta name=\"generator\" content=\"Codeply\">\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("    <link rel=\"stylesheet\" href=\"//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css\" />\n");
      out.write("    <link href=\"//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css\" rel=\"stylesheet\" />\n");
      out.write("    <link href=\"//cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.1/animate.min.css\" rel=\"stylesheet\" />\n");
      out.write("\n");
      out.write("    <link rel=\"stylesheet\" href=\"css/styles.css\" />\n");
      out.write("  </head>\n");
      out.write("  <body >\n");
      out.write("\n");
      out.write("<section id=\"section4\">\n");
      out.write("    <div class=\"container\">\n");
      out.write("        <div class=\"row\">\n");
      out.write("            <div class=\"col-md-12\">\n");
      out.write("                <h1 class=\"text-center\">Iniciar Sesión</h1>\n");
      out.write("                <hr>\n");
      out.write("            </div>\n");
      out.write("        </div>\n");
      out.write("        <form action=\"login.jsp\">\n");
      out.write("        <div class=\"row\">\n");
      out.write("            <div class=\"col-sm-9\">\n");
      out.write("                <div class=\"row form-group\">\n");
      out.write("                    <div class=\"col-sm-6\">\n");
      out.write("                        <input type=\"text\" class=\"form-control\" id=\"usuario\" name=\"usuario\" placeholder=\"Usuario\">\n");
      out.write("                    </div>\n");
      out.write("                </div>\n");
      out.write("                <div class=\"row form-group\">\n");
      out.write("                    <div class=\"col-sm-6\">\n");
      out.write("                        <input type=\"text\" class=\"form-control\" id=\"contrasena\" name=\"contrasena\" placeholder=\"Contraseña\">\n");
      out.write("                    </div>\n");
      out.write("                </div>\n");
      out.write("                <div class=\"row form-group\">\n");
      out.write("                    <div class=\"col-sm-6\">\n");
      out.write("                        <button class=\"btn btn-default btn-lg pull-left\">Iniciar Sesión</button>\n");
      out.write("                    </div>\n");
      out.write("                </div>\n");
      out.write("            </div>\n");
      out.write("        </div>\n");
      out.write("        <br>\n");
      out.write("        </form>\n");
      out.write("        \n");
      out.write("        <form action=\"Registro.jsp\">\n");
      out.write("        <button class=\"btn btn-default btn-lg pull-left\">Registrar Usuario</button>\n");
      out.write("        </form>\n");
      out.write("        \n");
      out.write("    </div>\n");
      out.write("</section>\n");
      out.write("\n");
      out.write("    <!--scripts loaded here-->\n");
      out.write("    \n");
      out.write("    <script src=\"//ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js\"></script>\n");
      out.write("    <script src=\"//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js\"></script>\n");
      out.write("    <script src=\"js/scripts.js\"></script>\n");
      out.write("  </body>\n");
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

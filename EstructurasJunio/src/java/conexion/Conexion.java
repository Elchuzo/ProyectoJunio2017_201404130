package conexion;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import com.opencsv.*;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.List;
import java.util.logging.Level;
import javax.imageio.ImageIO;
import sun.misc.BASE64Decoder;
/**
 *
 * @author Oscar
 */
public class Conexion {
    public Conexion()
    {
        
    }
    public static OkHttpClient webClient = new OkHttpClient();
    
    public String parametros() throws FileNotFoundException, IOException {
        RequestBody formBody = new FormEncodingBuilder()
                .add("hola", "adios")
                .build();
        String r = getString("parametros", formBody);
        return r;
    }
    public boolean registrar(String nombre,String contra) throws FileNotFoundException, IOException
    {
        RequestBody formBody = new FormEncodingBuilder()
                .add("nombre",nombre)
                .add("contra",contra)
                .build();
        String r = getString("registrar", formBody);
        return (r.equals("True"));
    }
    public boolean iniciar(String nombre,String contra) throws FileNotFoundException,IOException
    {
         RequestBody formBody = new FormEncodingBuilder()
                .add("nombre",nombre)
                .add("contra",contra)
                .build();
        String r = getString("iniciar", formBody);
        return (r.equals("True"));
    }
    
    public void cargar(String archivo,String tipo) throws FileNotFoundException,IOException
    {
        CSVReader reader = new CSVReader(new FileReader(archivo));
        reader.readNext();
        String [] nextLine;
     if ("usuarios".equals(tipo))
             {
                 while ((nextLine = reader.readNext()) != null) {            
                     RequestBody formBody = new FormEncodingBuilder()
                         .add("tipo","usuarios")
                         .add("nombre",nextLine[0])
                         .add("contra",nextLine[1])
                         .add("conectado",nextLine[2])
                         .build();
                         String r;
                         r = getString("carga", formBody);
                 }
             }
     else if("naves".equals(tipo))
                      {
                          while ((nextLine = reader.readNext()) != null) {
                              if(nextLine.length > 4 )
                              {
                          RequestBody formBody = new FormEncodingBuilder()
                         .add("tipo","naves")
                         .add("jugador",nextLine[0])
                         .add("columna",nextLine[1])
                         .add("fila",nextLine[2])
                         .add("nivel",nextLine[3])
                         .add("modo",nextLine[4])
                         .add("direccion",nextLine[5])
                         .build();
                         String r;
                         r = getString("carga", formBody);
                              }
                              else
                              {
                                  RequestBody formBody = new FormEncodingBuilder()
                         .add("tipo","naves")
                         .add("jugador",nextLine[0])
                         .add("columna",nextLine[1])
                         .add("fila",nextLine[2])
                         .add("nivel",nextLine[3])
                         .add("modo",nextLine[4])                        
                         .build();
                         String r;
                         r = getString("carga", formBody);
                              }
                     
                 }
                         
                         }
     else if("partidas".equals(tipo))
     {
         while ((nextLine = reader.readNext()) != null) {            
                     RequestBody formBody = new FormEncodingBuilder()
                         .add("tipo","partidas")
                         .add("usuario",nextLine[0])
                         .add("oponente",nextLine[1])
                         .add("tiros",nextLine[2])
                          .add("acertados",nextLine[3])
                             .add("fallados",nextLine[4])
                             .add("ganada",nextLine[5])
                             .add("danio",nextLine[6])
                         .build();
                         String r;
                         r = getString("carga", formBody);
                 }
     
     }
         else if("juego".equals(tipo))
                 {
                 while ((nextLine = reader.readNext()) != null) {            
                     
                             if(nextLine.length == 8)
                             {
                             String[] tiempo = nextLine[5].split(":");
                             int mins = Integer.parseInt(tiempo[0]);
                             int seg = Integer.parseInt(tiempo[1]);
                             int total = mins*60 + seg;
                             RequestBody formBody = new FormEncodingBuilder()    
                             .add("tipo","juego")
                             .add("usuario1",nextLine[0])
                             .add("usuario2",nextLine[1])
                             .add("tamx",nextLine[2])
                             .add("tamy",nextLine[3])
                             .add("variante",nextLine[4])                           
                             .add("tiempo",String.valueOf(total))
                             .add("tipodisparo",nextLine[6])
                             .add("numerodisparos",nextLine[7])                          
                         .build();
                             String r;
                         r = getString("carga", formBody);
                             }
                        else
                             {
                             RequestBody formBody = new FormEncodingBuilder()    
                             .add("tipo","juego")
                             .add("usuario1",nextLine[0])
                             .add("usuario2",nextLine[1])
                             .add("tamx",nextLine[2])
                             .add("tamy",nextLine[3])
                             .add("variante",nextLine[4])                           
                             .add("tipodisparo",nextLine[5])
                             .add("numerodisparos",nextLine[6])    
                                     .add("tiempo","0")
                         .build();
                             String r;
                         r = getString("carga", formBody);    
                             }         
                         
                         
                         
                 }
                 }
            }
       

        //codigo para leer el archivo
   public String disparar(String nombre, String nivel, String posx, String posy)   throws FileNotFoundException,IOException
    {
         RequestBody formBody = new FormEncodingBuilder()
                .add("jugador",nombre)
                .add("nivel",nivel)
                 .add("posx",posx)
                 .add("posy",posy)
                .build();
        String r = getString("disparar", formBody);
        return (r);
    }
   
   
    public String graficar(String parametro,String nickname,String imagen) throws IOException{
        RequestBody formBody = new FormEncodingBuilder()
                .add("nombre",parametro)
                .add("nickname",nickname)
                .add("imagen",imagen)
                .build();
        String r = getString("graficar", formBody);        
        return decodeToImage(r,imagen);
    }
    
    public String errores(String error) throws IOException{
        RequestBody formBody = new FormEncodingBuilder()
                .add("error",error)
                .build();
        String r = getString("errores", formBody);
        
        return r;
    }
    
    
    public String tablero(String nivel,String nickname) throws IOException{
        RequestBody formBody = new FormEncodingBuilder()
                .add("nivel",nivel)
                .add("usuario",nickname)
                .build();
        String r = getString("tableros", formBody);
        
        return r;
    }
    
     public String tableroen(String nivel,String nickname) throws IOException{
        RequestBody formBody = new FormEncodingBuilder()
                .add("nivel",nivel)
                .add("usuario",nickname)
                .build();
        String r = getString("tablerosen", formBody);
        
        return r;
    }
    
    public String enemigo(String nickname) throws IOException{
        RequestBody formBody = new FormEncodingBuilder()
                .add("jugador",nickname)
                .build();
        String r = getString("jugadores", formBody);
        return r;
    }
    
    public static String decodeToImage(String imageString,String imagen) throws IOException {
 
        BufferedImage image = null;
        byte[] imageByte;
        try {
            BASE64Decoder decoder = new BASE64Decoder();
            imageByte = decoder.decodeBuffer(imageString);
            try (ByteArrayInputStream bis = new ByteArrayInputStream(imageByte)) {
                image = ImageIO.read(bis);
            }
        } catch (IOException e) {
            System.out.println(e);
        }
        File outputfile = new File("C:\\Users\\Abraham Jelkmann\\Desktop\\ProyectoJunio2017_201404130\\EstructurasJunio\\web\\"+imagen+".png");
        ImageIO.write(image, "png", outputfile);
        return imagen+".png";
    }
    
public static String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://0.0.0.0:5000/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(conexion.Conexion.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(conexion.Conexion.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
    
}

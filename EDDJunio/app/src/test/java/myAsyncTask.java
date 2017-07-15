/**
 * Created by Abraham Jelkmann on 10/07/2017.
 */

private class myAsyncTask extends AsyncTask<Void, Void, Void> {


    @Override
    protected Void doInBackground(Void... params) {

        String URL = "http://www.w3schools.com/webservices/tempconvert.asmx";

        //for linear parameter
        SoapObject request = new SoapObject(NAMESPACE, METHOD_NAME);
        request.addProperty("Celsius", "48"); // adding method property here serially

        SoapSerializationEnvelope envelope = new      SoapSerializationEnvelope(SoapEnvelope.VER11);
        envelope.implicitTypes = true;
        envelope.setOutputSoapObject(request);
        envelope.dotNet = true;

        HttpTransportSE httpTransport = new HttpTransportSE(URL);
        httpTransport.debug = true;

        try {
            httpTransport.call(SOAP_ACTION, envelope);
        } catch (HttpResponseException e) {
            // TODO Auto-generated catch block
            Log.e("HTTPLOG", e.getMessage());
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            Log.e("IOLOG", e.getMessage());
            e.printStackTrace();
        } catch (XmlPullParserException e) {
            // TODO Auto-generated catch block
            Log.e("XMLLOG", e.getMessage());
            e.printStackTrace();
        } //send request

        Object  result = null;
        try {
            result = (Object )envelope.getResponse();
            Log.i("RESPONSE",String.valueOf(result)); // see output in the console
        } catch (SoapFault e) {
            // TODO Auto-generated catch block
            Log.e("SOAPLOG", e.getMessage());
            e.printStackTrace();
        }
        return null;
    }
}
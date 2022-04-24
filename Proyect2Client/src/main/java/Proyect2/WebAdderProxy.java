package Proyect2;

public class WebAdderProxy implements Proyect2.WebAdder {
  private String _endpoint = null;
  private Proyect2.WebAdder webAdder = null;
  
  public WebAdderProxy() {
    _initWebAdderProxy();
  }
  
  public WebAdderProxy(String endpoint) {
    _endpoint = endpoint;
    _initWebAdderProxy();
  }
  
  private void _initWebAdderProxy() {
    try {
      webAdder = (new Proyect2.WebAdderServiceLocator()).getwebAdder();
      if (webAdder != null) {
        if (_endpoint != null)
          ((javax.xml.rpc.Stub)webAdder)._setProperty("javax.xml.rpc.service.endpoint.address", _endpoint);
        else
          _endpoint = (String)((javax.xml.rpc.Stub)webAdder)._getProperty("javax.xml.rpc.service.endpoint.address");
      }
      
    }
    catch (javax.xml.rpc.ServiceException serviceException) {}
  }
  
  public String getEndpoint() {
    return _endpoint;
  }
  
  public void setEndpoint(String endpoint) {
    _endpoint = endpoint;
    if (webAdder != null)
      ((javax.xml.rpc.Stub)webAdder)._setProperty("javax.xml.rpc.service.endpoint.address", _endpoint);
    
  }
  
  public Proyect2.WebAdder getWebAdder() {
    if (webAdder == null)
      _initWebAdderProxy();
    return webAdder;
  }
  
  public int addition(int nm1, int nm2) throws java.rmi.RemoteException{
    if (webAdder == null)
      _initWebAdderProxy();
    return webAdder.addition(nm1, nm2);
  }
  
  
}
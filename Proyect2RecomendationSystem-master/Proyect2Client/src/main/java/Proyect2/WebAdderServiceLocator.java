/**
 * WebAdderServiceLocator.java
 *
 * This file was auto-generated from WSDL
 * by the Apache Axis 1.4 Apr 22, 2006 (06:55:48 PDT) WSDL2Java emitter.
 */

package Proyect2;

public class WebAdderServiceLocator extends org.apache.axis.client.Service implements Proyect2.WebAdderService {

    public WebAdderServiceLocator() {
    }


    public WebAdderServiceLocator(org.apache.axis.EngineConfiguration config) {
        super(config);
    }

    public WebAdderServiceLocator(java.lang.String wsdlLoc, javax.xml.namespace.QName sName) throws javax.xml.rpc.ServiceException {
        super(wsdlLoc, sName);
    }

    // Use to get a proxy class for webAdder
    private java.lang.String webAdder_address = "http://localhost:8080/Proyect2/services/webAdder";

    public java.lang.String getwebAdderAddress() {
        return webAdder_address;
    }

    // The WSDD service name defaults to the port name.
    private java.lang.String webAdderWSDDServiceName = "webAdder";

    public java.lang.String getwebAdderWSDDServiceName() {
        return webAdderWSDDServiceName;
    }

    public void setwebAdderWSDDServiceName(java.lang.String name) {
        webAdderWSDDServiceName = name;
    }

    public Proyect2.WebAdder getwebAdder() throws javax.xml.rpc.ServiceException {
       java.net.URL endpoint;
        try {
            endpoint = new java.net.URL(webAdder_address);
        }
        catch (java.net.MalformedURLException e) {
            throw new javax.xml.rpc.ServiceException(e);
        }
        return getwebAdder(endpoint);
    }

    public Proyect2.WebAdder getwebAdder(java.net.URL portAddress) throws javax.xml.rpc.ServiceException {
        try {
            Proyect2.WebAdderSoapBindingStub _stub = new Proyect2.WebAdderSoapBindingStub(portAddress, this);
            _stub.setPortName(getwebAdderWSDDServiceName());
            return _stub;
        }
        catch (org.apache.axis.AxisFault e) {
            return null;
        }
    }

    public void setwebAdderEndpointAddress(java.lang.String address) {
        webAdder_address = address;
    }

    /**
     * For the given interface, get the stub implementation.
     * If this service has no port for the given interface,
     * then ServiceException is thrown.
     */
    public java.rmi.Remote getPort(Class serviceEndpointInterface) throws javax.xml.rpc.ServiceException {
        try {
            if (Proyect2.WebAdder.class.isAssignableFrom(serviceEndpointInterface)) {
                Proyect2.WebAdderSoapBindingStub _stub = new Proyect2.WebAdderSoapBindingStub(new java.net.URL(webAdder_address), this);
                _stub.setPortName(getwebAdderWSDDServiceName());
                return _stub;
            }
        }
        catch (java.lang.Throwable t) {
            throw new javax.xml.rpc.ServiceException(t);
        }
        throw new javax.xml.rpc.ServiceException("There is no stub implementation for the interface:  " + (serviceEndpointInterface == null ? "null" : serviceEndpointInterface.getName()));
    }

    /**
     * For the given interface, get the stub implementation.
     * If this service has no port for the given interface,
     * then ServiceException is thrown.
     */
    public java.rmi.Remote getPort(javax.xml.namespace.QName portName, Class serviceEndpointInterface) throws javax.xml.rpc.ServiceException {
        if (portName == null) {
            return getPort(serviceEndpointInterface);
        }
        java.lang.String inputPortName = portName.getLocalPart();
        if ("webAdder".equals(inputPortName)) {
            return getwebAdder();
        }
        else  {
            java.rmi.Remote _stub = getPort(serviceEndpointInterface);
            ((org.apache.axis.client.Stub) _stub).setPortName(portName);
            return _stub;
        }
    }

    public javax.xml.namespace.QName getServiceName() {
        return new javax.xml.namespace.QName("http://Proyect2", "webAdderService");
    }

    private java.util.HashSet ports = null;

    public java.util.Iterator getPorts() {
        if (ports == null) {
            ports = new java.util.HashSet();
            ports.add(new javax.xml.namespace.QName("http://Proyect2", "webAdder"));
        }
        return ports.iterator();
    }

    /**
    * Set the endpoint address for the specified port name.
    */
    public void setEndpointAddress(java.lang.String portName, java.lang.String address) throws javax.xml.rpc.ServiceException {
        
if ("webAdder".equals(portName)) {
            setwebAdderEndpointAddress(address);
        }
        else 
{ // Unknown Port Name
            throw new javax.xml.rpc.ServiceException(" Cannot set Endpoint Address for Unknown Port" + portName);
        }
    }

    /**
    * Set the endpoint address for the specified port name.
    */
    public void setEndpointAddress(javax.xml.namespace.QName portName, java.lang.String address) throws javax.xml.rpc.ServiceException {
        setEndpointAddress(portName.getLocalPart(), address);
    }

}

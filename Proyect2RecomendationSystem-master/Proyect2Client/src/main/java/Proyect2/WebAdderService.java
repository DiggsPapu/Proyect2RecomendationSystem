/**
 * WebAdderService.java
 *
 * This file was auto-generated from WSDL
 * by the Apache Axis 1.4 Apr 22, 2006 (06:55:48 PDT) WSDL2Java emitter.
 */

package Proyect2;

public interface WebAdderService extends javax.xml.rpc.Service {
    public java.lang.String getwebAdderAddress();

    public Proyect2.WebAdder getwebAdder() throws javax.xml.rpc.ServiceException;

    public Proyect2.WebAdder getwebAdder(java.net.URL portAddress) throws javax.xml.rpc.ServiceException;
}

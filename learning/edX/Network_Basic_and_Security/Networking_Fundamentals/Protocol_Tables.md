## Protocols
A network protocol is an established set of rules that determine how data is transmitted between different devices in the same network. Network protocols are typically created according to industry standards. There are thousands of different network protocols, but they all perform one of three primary security, communication, and network management.

## Ports
Ports are the first and last stops for information sent across a network. A port is a communication endpoint. A port always has an associated protocol and application. The protocol is the path that leads to the application's port. A network device can have up to 65,536 port and default port numbers do not change.

## TCP vs UDP
Transmission control protocol, or TCP, and user datagram protocol, or UDP, are two primary Internet protocols.

TCP guarantees that sent data makes it to its intended recipient. It's slower and requires more resources. Typical applications include file transfer protocol, or FTP, web browsing, and email.

UDP doesn't guarantee that all packets will arrive, but it's fast and requires fewer resources. Typical applications live streaming, online gaming, and calls over the Internet. 

Ports send and receive data using TCP, UDP, and sometimes both.

## Web page protocols
Web page protocols control access and connection between Internet users and the sites they visit. 

Hypertext transfer protocol, or HTTP, is responsible for standard Internet or webpage access. The default port for HTTP is 80.

And hypertext transfer protocol secure, or HTTPS, is responsible for encrypted Internet or web page access. HTTPS should be used on a web page that prompts for sensitive data, such as credit card numbers. The default port for HTTPS is 443.

## File transfer protocols
File transfer protocols control how data is managed when sent from one location to another.

File transfer protocol, or FTP, is responsible for file transfer. FTP transfers files to and from an FTP server or client. The default port for FTP is 21.

And secure file transfer protocol, or SFTP, is responsible for encrypted file transfer. The default port for SFTP is 22.

## Remote access protocols
Remote access protocols enable device control from a remote location. 

Teletype network, or Telnet, is used to remotely control another device via console or command shell. Telnet lets users configure network devices from almost anywhere worldwide, so long as both devices have network connectivity. However, Telnet should not be used due to data being in clear text, no encryption. The default port for Telnet is 23.

Secure shell, or SSH, is used to remotely control another device via console or command shell securely with encryption. SSH uses encryption to secure remote data. The default port for SSH is 22, which is the same port that SFTP uses, since they both offer similar secured services.

And remote desktop protocol, or RDP, is used to remotely control another computer via a graphical user interface, also called GUI or GUI for short.

## Email protocols
Email protocols determine how email messages are received, stored, downloaded, removed, or retained.

Post office protocol, version three, or POP3, is an older protocol that was the standard for receiving email. With POP3, email is downloaded from an email server to a single device, and then the email is deleted from the server. The default port for POP3 is 110.

Internet message Access Protocol, version four, or IMAP4, is a protocol responsible for receiving email. With IMAP4, email is stored on the server and synchronized to multiple devices like laptops and mobile phones. The default port for IMAP4 is 143,

Simple mail transfer protocol, or SMTP, is responsible for sending email. The default port for SMTP is 25.

## Network protocols
Network protocols monitor, control, and help the network locate, share, and transfer data. 

Dynamic host configuration protocol, or DHCP, automatically assigns IP addresses to devices. The default ports for DHCP are 67 and 68.

Domain name system, or DNS, resolves or translates domain names to IP addresses. The default port for DNS is 53. 

Server message block, or SMB, enables sharing files and printers on the network. The default ports for SMB are 137 through 139.

Simple network management protocol, or SNMP, monitors the network. The default port for SNMP is 161. 

And lightweight directory access protocol, or LDAP, allows directory services to store and authenticate passwords, usernames, and accounts, and share them over the network. The default port for LDAP is 389.

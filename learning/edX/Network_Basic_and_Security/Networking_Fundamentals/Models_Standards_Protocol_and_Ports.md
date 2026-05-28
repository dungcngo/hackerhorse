## Network Models
A networking model describes the architecture, components, and design used to establish communication between the source and destination systems.

Data packets follow the protocols of network models. There are two types of networking models:
- The OSI or Open Systems Interconnection model is a conceptual framework used to describe the functions of a networking system.
- The TCP/IP or Transmission Control Protocol/Internet Protocol model is a set of standards that allow computers to communicate on a network. TCP/IP is based on the OSI model.

The OSI model is a conceptual framework used to describe the functions of a networking system. Data flows across these layers when communicating over a network. The seven layers of the OSI model include:
- Application: Users and applications interact directly with the software application.
- Presentation: ensures that data is in a usable format and is where data encryption occurs.
- Session: controls the flow of information between different computers, including authentication and reconnections.
- Transport: manages the delivery and error checking of data packets. Data is commonly transported using Transmission Control Protocol or TCP
- Network: responsible for interpreting the addresses and directing the path the data will take.
- Data link: defines the format of data on the network. This layer also corrects errors that may have happened at the physical layer.
- Physical: electrically or optically transmits raw, unstructured data over a physical medium.

The TCP/IP model is a set of standards that allow computers to communicate on a network. TCP/IP is based on the OSI model and functions similarly. The background protocols are still in place, but the way they are organized is slightly different.  The data travels through fewer layers on both ends.

## Networks Standards and their importance
Networking standards define the rules for data communications that are needed for interoperability of networking technologies and processes. Standards are widely accepted protocols that engineers use to make sure the things they build integrate with existing devices and technology.

There are two types of network standards:
- De jure or formal standards: are formal standards developed by an official industry or government body. Formal standards have gone through formal processes to obtain consensus, including publicly available documentation. Examples include HTTP HTML, IP, and Ethernet 802.3d.
- De facto standards: De facto standards result from marketplace domination or practice. De facto standards are accepted in practice but have not undergone any formal process to obtain consensus and may not have publicly available documentation. Typically, de facto standards result from marketplace domination or practice. Examples include Microsoft Windows and QWERTY keyboard.

Standards are usually created by government or non-profit organizations for the betterment of an entire industry. This ensures a broader compatibility across vendors and industries. Some of the well-known organizations that have created network standards are international standards organization:
- ISO, established the well-known OSI reference networking model.
- International Telecommunication Union or ITU, standardized international telecom, and set standards for fair use in radio frequency.
- Defense Advanced Research Projects Agency or DARPA, established the TCP/IP protocol suite.
- Institute of Electronics and Electrical Engineers, or IEEE, established the IEEE 802 standards.
- The World Wide Web Consortium or W3C, established the World Wide Web (www) standard.
- Finally, the Internet Engineering Task Force or IETF maintains the TCP/IP protocol suites. IETF also developed the Request for Comment, or RFC, standard.

## Protocols
A network protocol is an established set of rules that determine how data is transmitted between different devices in the same network. Network protocols are typically created according to industry standards. There are thousands of different network protocols, but they all perform one of three primary actions: security, communication, and network management.

Transmission Control Protocol or TCP, and User Datagram Protocol or UDP are two primary internet protocols.
- TCP guarantees sent data makes it to its intended recipient. It's slower and requires more resources. File transfer protocol, or FTP, web browsing, and email are typical applications of TCP.
- UDP doesn't guarantee all packets will arrive, but it's fast and needs fewer resources. Good for live streaming, online gaming, and calls over the internet.
  
The TCP/IP suite is a collection of protocols. Together, these protocols provide a complete networking solution.

The Internet of Things, or IoT, network model comprises diverse protocols for communication, which include data collection, data package, data transfer, and data control.

The Crypto Classic protocol is designed to serve as one of the most efficient, effective, and secure payment methods built on the blockchain network. It ensures privacy and transparency of payments directly transferred between two parties who have an address on the blockchain network.

## Ports
Ports are the first and last stop for information sent across a network. 

A port is a communication endpoint A port always has an associated protocol and application. The protocol is the path that leads to the application's port.

A network device can have up to 65,536 ports. Port numbers do not change.

## Socket
A socket is a two-way communication channel. Each socket is made up of: a source IP address, a protocol, a port number, a destination IP address.

You use a socket whenever you send data over your local network or over the internet. For example, whenever you use a web browser, send an email, or watch a video online, a socket is used over the network in order to make that communication possible.

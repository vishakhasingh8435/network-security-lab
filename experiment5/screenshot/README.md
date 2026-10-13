# Capture and Analyze TLS Handshake Using Wireshark

## 1. Aim
To capture and analyze the TLS handshake process during HTTPS communication using Wireshark.

## 2. Context / Theory
TLS (Transport Layer Security) is a security protocol that protects communication between a web browser and a web server. It provides encryption, authentication, and data integrity.

During the TLS handshake, the client and server negotiate security settings and establish keys for secure communication.

### TLS Handshake Diagram

```text
Client (Web Browser)          Server (Website)
        |                            |
        | ------ Client Hello -----> |
        | <----- Server Hello ------ |
        | <----- Certificate ------- |
        |     Key Establishment     |
        |                            |
        | === Secure Connection === |
```

*Note: This is a simplified diagram. The handshake messages differ between TLS 1.2 and TLS 1.3.*

## 3. Tools Required
- Wireshark
- Web browser
- Internet connection

## 4. Methodology
1. Open Wireshark and select the active network interface.
2. Start capturing network traffic.
3. Open an HTTPS website, such as `https://www.google.com`.
4. Stop the capture after the website loads.
5. Apply the display filter `tls` to identify TLS packets.
6. Inspect Client Hello and Server Hello messages.
7. Examine certificate information wherever it is visible in the captured packets.

### Wireshark Display Filters

**Display TLS packets:**
```text
tls
```

**Display TLS handshake packets:**
```text
tls.handshake
```

**Display Client Hello packets:**
```text
tls.handshake.type == 1
```

**Display Server Hello packets:**
```text
tls.handshake.type == 2
```

**Display Certificate messages, where visible:**
```text
tls.handshake.type == 11
```

**Display TCP traffic on port 443:**
```text
tcp.port == 443
```

*Note: These are Wireshark display filters, not programming code. Some TLS 1.3 handshake messages are encrypted and may not be visible without decryption.*

## 5. Results
- TLS handshake packets were captured successfully.
- Client Hello and Server Hello messages were observed.
- Certificate information was visible where available.
- HTTPS communication was identified.

## 6. Discussion
The captured packets demonstrated how the browser and server negotiate security settings and establish a secure connection. The TLS handshake helps authenticate the server and establish encryption keys. After the handshake, application data is encrypted and generally cannot be read without the required decryption secrets.

## 7. Improvement
Used Wireshark display filters to identify TLS handshake packets and analyzed Client Hello, Server Hello, and certificate messages to understand the secure communication process.

## 8. Conclusion
The TLS handshake was captured and analyzed successfully using Wireshark. The practical helped in understanding how TLS establishes a secure connection for HTTPS communication.

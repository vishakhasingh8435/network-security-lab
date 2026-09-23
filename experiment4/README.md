# Experiment 4: Generate and Verify X.509 Self-Signed Digital Certificate

## Aim
To generate and verify a self-signed X.509 digital certificate using OpenSSL.

## Context / Theory
An X.509 certificate is a digital certificate that connects an identity with a public key. A self-signed certificate is signed by the same entity that creates it. It can be used for testing and secure communication.

## Tools
- OpenSSL
- Kali Linux

## Methodology
1. Generated a 3072-bit RSA private key.
2. Created a self-signed X.509 certificate.
3. Added Subject Alternative Name (SAN).
4. Inspected the certificate structure.
5. Verified the certificate using OpenSSL.

## Result
The X.509 self-signed certificate was successfully generated and verified. The verification result was `OK`.

## Discussion
The certificate contained the required identity, public key, validity period, and digital signature. The successful verification confirmed that the certificate was valid when explicitly trusted.

## Improvement
The certificate was improved using a 3072-bit RSA key, SHA-256, SAN, and server authentication extensions.

## Specific Instance
The certificate can be used for testing HTTPS communication on a localhost server.

## Screenshots

### Certificate Generation
![Certificate Generation](screenshots/screenshot1.png)

### Certificate Details
![Certificate Details](screenshots/screenshot2.png)

### Certificate Verification
![Certificate Verification](screenshots/screenshot3.png)
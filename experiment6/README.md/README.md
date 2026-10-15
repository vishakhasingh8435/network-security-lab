# Experiment 6: Establish Secure Remote Login Using SSH

## Aim
To establish secure remote server access using SSH and demonstrate password-based and key-based authentication.

## Context / Theory
SSH (Secure Shell) is a network protocol used to securely access a remote computer over a network. It encrypts communication between the client and server.

**Password-Based Authentication:** The user logs in using a username and password.

**Key-Based Authentication:** The user uses a private key, and the server verifies it using the corresponding public key.

### Architecture Diagram

```text
+----------------------+
|    Client Computer   |
|      Kali Linux      |
+----------------------+
           |
           | SSH Connection
           | Port 22
           |
           v
+----------------------+
|    Remote Server     |
|    OpenSSH Server    |
+----------------------+
```

## Tools Required
- Kali Linux
- Remote Linux server or virtual machine
- OpenSSH client and server
- Wireshark (optional, for traffic analysis)

## Methodology / Procedure

### Step 1: Start SSH Service
Run on the server:

```bash
sudo systemctl start ssh
```

Check the service:

```bash
sudo systemctl status ssh
```

### Step 2: Find the Server IP Address

```bash
ip addr
```

Note the server's IP address.

### Step 3: Test Password-Based Authentication

```bash
ssh username@server_ip
```

Enter the password when prompted.

### Step 4: Generate an SSH Key Pair

```bash
ssh-keygen
```

This creates a public key and a private key.

### Step 5: Copy the Public Key to the Server

```bash
ssh-copy-id username@server_ip
```

Enter the password if prompted.

### Step 6: Test Key-Based Authentication

```bash
ssh username@server_ip
```

Verify that the login succeeds using the configured SSH key.

### Step 7: Verify Remote Access

```bash
whoami
```

This displays the username of the account on the remote server.

## Results
- SSH service was started and checked.
- Password-based authentication was tested.
- An SSH key pair was generated.
- The public key was configured on the server.
- Key-based authentication was tested.
- Remote login was verified when the server and authentication were configured correctly.

## Discussion
SSH provides encrypted communication between the client and server. Password-based authentication uses a password, while key-based authentication uses a public-private key pair. Key-based authentication can improve security when private keys are properly protected.

## Conclusion
The experiment demonstrated secure remote login using SSH through password-based and key-based authentication. It helped us understand encrypted communication and the use of SSH keys for secure remote access.

## Improvements
- Use key-based authentication with a strong passphrase.
- Disable password login only after verifying key-based login.
- Keep SSH software updated.
- Allow access only to authorized users.
- Protect private keys and monitor login attempts.

## Precautions
- Use only authorized systems.
- Never share the private key.
- Verify the server's host key.
- Use strong passwords.
- Do not disable password authentication before testing key-based login.

## References
- OpenSSH: https://www.openssh.com/
- SSH Manual: https://man.openbsd.org/ssh

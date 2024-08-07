# Infrastructure Setup for www.foobar.com

## Overview

This document describes the setup of a web infrastructure for hosting `www.foobar.com` using a combination of load balancers, web servers, application servers, a database, and security measures. The infrastructure includes:

- **Load Balancers**: HAproxy configured in a cluster.
- **Web Server**: Nginx.
- **Application Server**: Hosts application code.
- **Database**: MySQL.
- **Security**: Firewalls, SSL certificate.
- **Monitoring**: Data collection and logging.

## Components

### 1. Load Balancer Cluster

- **Server 4**: HAproxy Node 1
- **Server 5**: HAproxy Node 2

**Purpose**: The HAproxy cluster handles incoming traffic and distributes it across the web server and application servers, providing load balancing and redundancy.

**Configuration**:
- **Distribution Algorithm**: Round-Robin.
- **Setup**: Active-Active, both nodes share the load and are active simultaneously.

### 2. Web Server

- **Server 1**: Nginx

**Purpose**: Serves static files and handles HTTP requests from clients.

**Configuration**:
- Configured to receive traffic from the HAproxy cluster.
- Serves content over HTTP/HTTPS.

### 3. Application Server

- **Server 2**: Application Server

**Purpose**: Hosts and processes dynamic content and application logic.

**Configuration**:
- Receives requests from the web server.
- Processes application-specific logic and responses.

### 4. Database

- **Server 3**: MySQL

**Purpose**: Stores and manages application data.

**Configuration**:
- **Primary (Master) Node**: Handles write operations and replication.
- **Replica (Slave) Nodes** (if applicable): Handles read operations to distribute the load.

### 5. Security

- **Firewalls**:
  - **Firewall 1**: Protects the HAproxy cluster.
  - **Firewall 2**: Protects the Web Server (Nginx).
  - **Firewall 3**: Protects the Application Server and Database.

- **SSL Certificate**:
  - Installed on the HAproxy nodes to serve `www.foobar.com` over HTTPS, ensuring encrypted communication.

### 6. Monitoring

- **Monitoring Clients**:
  - Installed on all servers to collect data for performance tracking and logging (e.g., Sumologic).

## Traffic Flow

1. **DNS Resolution**:
   - `www.foobar.com` resolves to the IP address of the HAproxy cluster.

2. **Load Balancer**:
   - HAproxy nodes distribute incoming traffic between the web server and application server.

3. **Web Server**:
   - Handles static file requests and forwards dynamic requests to the application server.

4. **Application Server**:
   - Processes dynamic content and communicates with the database.

5. **Database**:
   - Stores and retrieves application data.

6. **Monitoring**:
   - Data is collected and sent to monitoring services for analysis and alerts.

## Diagram

![Infrastructure Diagram](link-to-your-diagram.png)

## Additional Notes

- **HAproxy Configuration**: Ensure that HAproxy is properly configured with the Round-Robin algorithm for load balancing.
- **Firewalls**: Configure firewalls to restrict access and ensure only legitimate traffic reaches the servers.
- **SSL/TLS**: Verify SSL certificates are properly installed and valid.
- **Monitoring**: Regularly review monitoring data to detect and address performance issues promptly.

## Troubleshooting

- **HAproxy Issues**: Check logs for load balancing issues and ensure both nodes are functioning.
- **Web Server Errors**: Verify Nginx configuration and check for connectivity issues.
- **Application Server**: Monitor for application errors and performance bottlenecks.
- **Database**: Ensure replication is working and check for database performance.

## Contributing

If you have suggestions for improvements or encounter issues, please open an issue or submit a pull request.

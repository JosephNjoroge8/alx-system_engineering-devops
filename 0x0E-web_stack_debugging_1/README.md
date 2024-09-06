# 0x0E. Web stack debugging #1

This project contains Bash scripts for debugging and configuring Nginx to listen on port 80.

## Files

- `0-nginx_likes_port_80`: Script to configure Nginx to listen on port 80 of all active IPv4 IPs.
- `1-debugging_made_short`: A shorter version of the script to configure Nginx (5 lines or less).

## Usage

Make the scripts executable and run them with root privileges:

```
chmod +x 0-nginx_likes_port_80
sudo ./0-nginx_likes_port_80

chmod +x 1-debugging_made_short
sudo ./1-debugging_made_short
```

After running either script, Nginx should be configured to listen on port 80.

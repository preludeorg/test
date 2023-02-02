# Attempt to write data to a foreign country

Endpoints are typically configured, by default, with outbound internet access fully enabled. This means that - while a firewall may be protecting malicious traffic from getting in - there is no protection for things going out. If an adversary breaches an endpoint like this they can exfiltrate data unnoticed. There is a balance, however. If all outbound traffic were blocked, the endpoint could no longer receive updates, install software or do basic functions like use a web browser. One recommended tactic is to limit the geographic locations an endpoint can send outbound requests. IP addresses correlate to physical locations, so by limiting the countries an endpoint can talk to, it immediately becomes more secure with no adverse effects.

Example output:
```
[+] Starting test
[+] Connection opening to 77.88.55.80:443
[+] Client connection closing
[+] Message sent successfully to  77.88.55.80:443
[+] Connection opening to 104.193.88.77:443
[+] Client connection closing
[+] Message sent successfully to  104.193.88.77:443
[+] Completed with code: 101
```

Attempts to write data over the network to specific countries should be blocked.

## How

> Safety: only the string "hello" is sent over the network

This test opens a connection to https://yandex.com and https://www.baidu.cn, which are Russian and Chinese search engines, and writes the byte stream "hello". The connection is done through a raw TCP socket (write) directly against both IP address, bypassing any DNS resolution that may occur otherwise. If the write is allowed to complete and the connection is closed properly, the test is marked failed. Some assumptions are made with this test such as the search engines being online and reasonable latency with the connection attempts.

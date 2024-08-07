# Proxy settings

We highly recommend excluding all traffic to Microsoft 365 from proxy usage. For more details, please have a look at [Microsoft's network connectivity principles](https://docs.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-network-connectivity-principles?view=o365-worldwide).

However, KONNEKT is using the proxy settings of the Windows OS. If a proxy server is set, KONNEKT will use this proxy server.

In detail, KONNEKT calls [`WinHttpGetProxyForUrl`](https://docs.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpgetproxyforurl) with the URI `https://graph.microsoft.com` to examine, if a proxy must be used.

{% hint style="success" %}
To bypass your proxy server with traffic from KONNEKT, please make sure, that Windows OS will exclude the URI `https://graph.microsoft.com` from proxy usage.

You may do this by putting this URI on the exclude list in your proxy PAC file.

You should also make sure, that the KONNEKT client can reach [Microsoft Entra ID (Azure AD) and SharePoint Online](https://docs.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges?view=o365-worldwide) without being interfered by proxy servers or other application layer gateways (ALG).
{% endhint %}

{% hint style="warning" %}
KONNEKT can use proxy servers. However, we offer limited support for clients that are experiencing network connectivity-related issues while connecting to Microsoft 365 via proxy server or other application layer gateways (ALG).
{% endhint %}

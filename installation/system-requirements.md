# System requirements

## Client Machine

### Operating System

* **Windows** or \
  **Windows Server**
  * with current and complete system updates and
  * supported by Microsoft via Mainstream Support.
  * Older Windows versions may work - we offer limited support for those systems.

{% hint style="success" %}
KONNEKT runs in different **VDI** environments:

* Hypervisor systems (e.g. Citrix XenDesktop, VMware Horizon),
* Multi-session systems (e.g. Citrix XenApp, Microsoft Terminal server/RDS) and
* Microsoft Azure Virtual Desktop (VVD)
* Microsoft Windows 365 Cloud PC
{% endhint %}

{% hint style="success" %}
KONNEKT works **independently** from:

* .NET
* specific Citrix versions
* Microsoft365 Apps (fka Office365 ProPlus)
* OneDrive Sync Client
{% endhint %}

### Processor Platform

* 64 Bit X86 (Intel & AMD)
* 32 Bit X86 (Intel & AMD)
* 64 Bit ARM

## Office 365 Licensing

* **OneDrive for Business** or **SharePoint Online** subscriptions are required for KONNEKT users.

## Proxy Settings

We highly recommend excluding all traffic to Microsoft 365 from proxy usage. For more details, please have a look at [Microsoft's network connectivity principles](https://learn.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-network-connectivity-principles?view=o365-worldwide).&#x20;

However, KONNEKT is using the proxy settings of the Windows OS. If a proxy server is set, KONNEKT will use this proxy server.&#x20;

In detail, KONNEKT calls [WinHttpGetProxyForUrl](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpgetproxyforurl) with the URI https://graph.microsoft.com to examine, if a proxy must be used.



{% hint style="success" %}
To bypass your proxy server with traffic from KONNEKT, please make sure, that Windows OS will exclude the URI https://graph.microsoft.com from proxy usage.&#x20;

You may do this by putting this URI on the exclude list in your proxy PAC file.&#x20;

You should also make sure, that the KONNEKT client can reach [Microsoft Entra ID (Azure AD) and SharePoint Online](https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges?view=o365-worldwide) without being interfered by proxy servers or other application layer gateways (ALG) such as firewalls etc.
{% endhint %}



{% hint style="warning" %}
KONNEKT can use proxy servers. However, we offer limited support for clients that are experiencing network connectivity-related issues while connecting to Microsoft 365 via proxy server or other application layer gateways (ALG).
{% endhint %}

## Firewall and Network settings

It is recommended to "Bypass Allow endpoints on network devices and services that perform traffic interception, SSL decryption, deep packet inspection, and content filtering"



**Whitelist Graph API URL**

* The Graph API is a RESTful API that uses HTTPS calls. Each API call technically has a unique UR
* To allow for use of different versions of the API, whitelist [https://graph.microsoft.com](https://graph.microsoft.com)



**Whitelist KONNEKT**

* Mandatory for licensing purposes, whitelist [https://license.c4a8.net](https://license.c4a8.net/)
* Users can send us details, when errors occur -  [https://crashguard.konnekt.io](https://crashguard.konnekt.io)



**Microsoft EntraID (Azure AD)**

* Whitelist both endpoints \*.portal.azure.com and portal.azure.com to ensure access to the domain and the subdomains
* [Azure portal URLs for proxy bypass](https://learn.microsoft.com/en-us/azure/azure-portal/azure-portal-safelist-urls?tabs=public-cloud#azure-portal-urls-for-proxy-bypass)
* To troubleshoot network connection issues, check [https://portal.azure.com/selfhelp](https://portal.azure.com/selfhelp)

# Grant tenant-wide admin consent

{% hint style="warning" %}
You have to do the admin consent **before** using KONNEKT with regular users.
{% endhint %}

## Background

KONNEKT is an application that interacts with several Microsoft 365 APIs. Therefore it needs permission to do so in each Microsoft365 tenant, KONNEKT wants to connect to. One level (but not the only one) of this permission is the Enterprise App Consent in Microsoft Entra ID (Azure AD). It is a major advantage over legacy approaches such as network- or proxy-based access controls for client types, since it is working at every place and allows very granular permissions.

The admin consent for KONNEKT is for "delegated access", only (please see [Microsoft docs](https://learn.microsoft.com/en-us/azure/active-directory/develop/permissions-consent-overview#access-scenarios) for more details on permissions and consent). This basically means that users in this tenant are allowed to use this app to access the requested M365 services/APIs. This does **not** enable the app to access without the user.

### Permission Set: Before Version 2.10

KONNEKT requests the following permissions to be consented:

<table><thead><tr><th width="146.5">API Name</th><th>Claim value</th><th>Permission</th></tr></thead><tbody><tr><td>Microsoft Graph</td><td>User.Read</td><td>Sign in and read user profile</td></tr><tr><td>Office 365 SharePoint Online</td><td>AllSites.Write</td><td>Read and write items in all site collections</td></tr><tr><td>Office 365 SharePoint Online</td><td>MyFiles.Write</td><td>Read and write user files</td></tr><tr><td>Windows Azure Active Directory</td><td>Directory.AccessAsUser.All</td><td>Access the directory as the signed-in user</td></tr><tr><td>Windows Azure Active Directory</td><td>User.Read</td><td>Sign in and read user profile</td></tr></tbody></table>

### Permission Set: Post Version 2.10

{% hint style="warning" %}
Functions exclusively when the setting "[**EnhancedOAuth**](../../configuration/system-settings/enhanced-authentication.md)" is enabled!
{% endhint %}

<table><thead><tr><th width="146.5">API Name</th><th>Claim value</th><th>Permission</th></tr></thead><tbody><tr><td>Microsoft Graph</td><td>Files.ReadWrite.All</td><td>Have full access to all files user can access</td></tr><tr><td>Microsoft Graph</td><td>Sites.Read.All</td><td>Read items in all site collections</td></tr><tr><td>Microsoft Graph</td><td>User.Read</td><td>Sign in and read user profile</td></tr><tr><td>Office 365 SharePoint Online</td><td>AllSites.Read</td><td>Read items in all site collections</td></tr></tbody></table>

[Since some of the permissions require to be consented by an admin](https://learn.microsoft.com/en-us/graph/permissions-reference), you have to do the admin consent before using KONNEKT with regular users.

You can learn more about [managing consent to applications and evaluate consent requests in the Microsoft docs](https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/manage-consent-requests).

## Add KONNEKT permissions in Microsoft Entra ID (Azure AD) Enterprise Applications

As an admin (or having a role that allows granting admin consent) you can grant tenant-wide admin consent to **KONNEKT** by using the following "Magic URL":

App registration URL till KONNEKT version **2.9.1** and below:

```
https://login.microsoftonline.com/{tenant-id}/adminconsent?client_id=fbaaaa6a-1ad0-4ac5-9c4c-4ce9353dc6cf
```

App registration URL from KONNEKT version **2.10** and later:

```
https://login.microsoftonline.com/{tenant-id}/adminconsent?client_id=11fa31bb-2024-4f49-8b38-f458d596a81a
```



Therefore you need your`tenant-id`which you get from **Azure Portal** under **Azure Active Directory:**

![](<../../.gitbook/assets/2021-08-09 11_36_25-Contoso - Microsoft Azure - TestTenant - Microsoft​ Edge.png>)

{% hint style="info" %}
Don't forget to delete the `{}` from the link
{% endhint %}

**After that:**

1. Open the link.
2. Login using your admin account (or account with role allows granting admin consent).
3. Accept the KONNEKT permissions request.
4. Done!

{% hint style="info" %}
If you get **Page Not Found** after accepting the consent, please ignore it. It has no meaning here.
{% endhint %}

To check **KONNEKT** permissions you can find it in your **Azure Active Directory** under **Enterprise applications** -> **Permissions**

<figure><img src="../../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

For more Info about admin consent visit [MS.Docs](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/grant-admin-consent)

## Delete KONNEKT permissions from Microsoft Entra ID (Azure AD) Enterprise Applications

In case you want to remove the admin-consent for KONNEKT, please proceed the following steps:

1. Sign in to the **Azure portal** with a role that allows deleting admin consent.
2. Select **Azure Active Directory** then **Enterprise applications.**
3. Look for **Konnekt** and click on it.
4. Select **properties.**
5. **Delete**, and confirm the delete.

<figure><img src="../../.gitbook/assets/image (65).png" alt=""><figcaption></figcaption></figure>

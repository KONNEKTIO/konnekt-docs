# Grant tenant-wide admin consent

KONNEKT is an application that interacts with several Microsoft365 APIs. Therefore it needs the permission to do so in each Microsoft365 tenant, KONNEKT wants to connect to. Giving this permission for a single user is called "consent", giving this permission for all users in the tenant is called "admin consent".

The user consent automatically shows up, if a user logs in with KONNEKT the first time. As an admin, you can do that work for all your users by following the procedure in the next chapter.

## Add KONNEKT permissions in AAD Enterprise Applications

As an admin (or having a role that allows granting admin consent) you can grant tenant-wide admin consent to **KONNEKT** by using the following "Magic URL":

```
https://login.microsoftonline.com/{tenant-id}/adminconsent?client_id=fbaaaa6a-1ad0-4ac5-9c4c-4ce9353dc6cf
```

Therefore you need your`tenant-id`which you get from **Azure Portal** under **Azure Active Directory:**

![](<../.gitbook/assets/2021-08-09 11\_36\_25-Contoso - Microsoft Azure - TestTenant - Microsoft​ Edge.png>)

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

![](<../.gitbook/assets/2021-06-29 17\_17\_45-Konnekt - Microsoft Azure and 2 more pages - TestTenant - Microsoft​ Edge.png>)

For more Info about admin consent visit [MS.Docs](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/grant-admin-consent)

## Delete KONNEKT permissions from AAD Enterprise Applications

In case you want to remove the admin-consent for KONNEKT, please proceed the following steps:

1. Sign in to the **Azure portal** with a role that allows deleting admin consent.
2. Select **Azure Active Directory** then **Enterprise applications.**
3. Look for **Konnekt** and click on it.
4. Select **properties.**
5. **Delete**, **** and confirm the delete.

![](<../.gitbook/assets/2021-06-29 15\_54\_57-Konnekt - Microsoft Azure and 2 more pages - TestTenant - Microsoft​ Edge.png>)

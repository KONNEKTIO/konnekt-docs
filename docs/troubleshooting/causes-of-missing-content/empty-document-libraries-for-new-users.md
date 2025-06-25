# Empty Document Libraries for new users

## Situation

Currently, some customers are experiencing issues where Document Libraries don't show any content for specific users KONNEKT. Permissions for these users didn't change and are displayed properly via the Edge browser.

KONNEKT uses the GraphAPI to get these data from SharePoint Online. The query responsible for this can be located in the KONNEKT logs preceding this line:

```
[RESTkitClient] Http request (OneDriveClient::GetItemByPath) GET:
```

The structure is similar to this:

```
https://graph.microsoft.com/v1.0/sites/TenantName.sharepoint.com:/sites/SiteName:/drive/root?$select=name
```

## **Temporary workaround to get content displayed**

*   Manually enable the setting "Automatically add all SharePoint document libraries" in the preferences menu\


    <figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>
* Enable the setting "[AddAllSharepointLibraries](https://docs.konnekt.io/configuration/mappings/auto-mapping#map-all-document-libraries)**"** via a policy for all users

{% hint style="warning" %}
Unfortunately, a side effect is that an additional layer for document libraries is added within KONNEKT.
{% endhint %}

## GitHub issue

{% @github-files/github-code-block url="https://github.com/SharePoint/sp-dev-docs/issues/10313" %}


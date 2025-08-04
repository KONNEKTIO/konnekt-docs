# Empty document libraries for managed mappings

## Situation

Currently, some customers are experiencing issues where Document Libraries don't show any content for volumes that were mapped by managed mappings. Permissions for these users didn't change and are displayed properly via the Edge browser.

KONNEKT uses the GraphAPI to get these data from SharePoint Online. The query responsible for this can be located in the KONNEKT logs preceding this line:

```
[RESTkitClient] Http request (OneDriveClient::GetItemByPath) GET:
```

The structure is similar to this:

```
https://graph.microsoft.com/v1.0/sites/TenantName.sharepoint.com:/sites/SiteName:/drive/root?$select=name
```

Issue in the [Microsoft SharePoint Github repo](https://github.com/SharePoint/sp-dev-docs/issues/10313).

## **Solution**

Please upgrade to [KONNEKT 2.11.2](../../../changelog.md#id-2.11.2-published-2025-08-04) or later.

We added a mitigation in KONNEKT 2.11.2 that does not use the affected Graph API calls.

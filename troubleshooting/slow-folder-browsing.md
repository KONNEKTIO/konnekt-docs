# Slow Folder Browsing

### Problem

Browsing folders in Windows Files Explorer may be slow. Opening a single folder sometimes takes more than 20 seconds (up to several minutes).

### Cause

KONNEKT requests details (e.g. file names etc.) about the content of a folder once you are accessing the folder via KONNEKT. To do so, KONNEKT leverages the SharePoint Online REST API.

Currently it seems if SharePoint Online response performance for the corresponding queries is degraded in several environments.

The number of files & folders in one folder seems to have the major effect. The volume of data used by the whole site, may also be a driver.

### Workaround&#x20;

#### Small folders

Segment your data in folders. Having a maximum of 250 files/folders in one folder seems to be a good rule of thumb for affected environments.

#### Direct Links

Try to avoid browsing through KONNEKT folders, by using direct links to your most used folders (e.g. by leveraging the [Quick Access feature of Windows Files Explorer](https://support.microsoft.com/en-us/windows/pin-remove-and-customize-in-quick-access-7344ff13-bdf4-9f40-7f76-0b1092d2495b)).

#### Caching

You could also try our [current preview version](https://docs.konnekt.io/changelog#2.1.4-preview-for-v2.2-published-2022-09-19), that introduces throttling prevention mechanisms. One of those is to cache the data, that is requested for browsing through folders for a small amount of time. This will not lower the amount of time for the first access, but it may make the second access faster, if you access the same folder again within a small amount of time.

If you want to try the preview version, please use the setting "high" for the throttling prevention policy.

### Solution

Please contact your Microsoft support and report, that your SharePoint Online REST API performance is degraded.

KONNEKT uses the following SharePoint Online REST API call to browse a folder:

```
https://<yourTenant>.sharepoint.com/sites/<siteName>/_api/v2.0/drive/items/<ID>/children
```

If you want us to help to name the corresponding site name and ID for your incident with Microsoft, please [contact our support team](https://www.konnekt.io/help/).

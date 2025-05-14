# Slow Folder Browsing

## Problem

Browsing folders in Windows Files Explorer may be slow. Opening a single folder sometimes takes more than 20 seconds (up to several minutes).

## Cause

KONNEKT requests details (e.g. file names etc.) about the content of a folder once you are accessing the folder via KONNEKT. To do so, KONNEKT leverages the SharePoint Online REST API.

Currently it seems if SharePoint Online response performance for the corresponding queries is degraded in several environments.

The number of files & folders in one folder seems to have the major effect. The volume of data used by the whole site, may also be a driver.

## Solution

#### KONNEKT update

We were redesigning the search strategy for folder browsing to work without the performance degraded properties in KONNEKT 2.2.0.

You can find details and download options for available releases in our [changelog](../changelog.md).

#### Contact Microsoft (to work with KONNEKT Version < 2.2.0)

If you cannot update to KONNEKT 2.2, please contact your Microsoft support and report, that your SharePoint Online REST API performance is degraded.

KONNEKT uses the following SharePoint Online REST API call to browse a folder:

```
https://<yourTenant>.sharepoint.com/sites/<siteName>/_api/v2.0/drive/items/<ID>/children
```

The property "createdBy" is the main driver of the delay.

If you want us to help to name the corresponding site name and ID for your incident with Microsoft, please:

* [Contact our support team](https://www.konnekt.io/help/)&#x20;
* Tell us a folder name (including site & library name) where you can reproduce the issue
* Send us a [debug log](debug-log-preparation.md) (if not already sent), where you were trying to access the folder.

####

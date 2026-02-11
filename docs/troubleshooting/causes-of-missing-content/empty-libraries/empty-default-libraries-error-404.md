# Empty default libraries - error 404

## Problem

All document libraries in KONNEKT and mapped drives are empty.

## Background

There are glitches in certain data centers hosting SharePoint Online on Microsoft's site. KONNEKT uses Microsoft's GraphAPI to access all information related to document libraries and their content.

Especially the request to get the default document library from a Site Collection ([Get drive](https://learn.microsoft.com/en-us/graph/api/drive-get)). KONNEKT's logs should contain entries if the default library operations fail:&#x20;

```
[2025-05-07 11:31:28.957] [30304] [error] [RESTkitClient] Http request (OneDriveClient::GetDefaultDrive) GET: https://graph.microsoft.com/v1.0/sites/<TenantName>.sharepoint.com,8fd7d761-4f99-4fdc-a0aa-de6b685e5306,56d1fa73-2339-4329-9df3-61100d751650/drive - 404
    error: Item not found: The resource could not be found.(404)
   "{"error":{"code":"itemNotFound","message":"The resource could not be found.","innerError":{"date":"2025-05-07T09:31:28","request-id":"17a44641-4204-4811-b176-58a379125b5d","client-request-id":"17a44641-4204-4811-b176-58a379125b5d"}}}"
    Response Header:
Cache-Control: no-store, no-cache
client-request-id: 17a44641-4204-4811-b176-58a379125b5d
Content-Type: application/json
Date: Wed, 07 May 2025 09:31:27 GMT
request-id: 17a44641-4204-4811-b176-58a379125b5d
Strict-Transport-Security: max-age=31536000
Transfer-Encoding: chunked
x-ms-ags-diagnostic: {"ServerInfo":{"DataCenter":"France Central","Slice":"E","Ring":"5","ScaleUnit":"004","RoleInstance":"PA2PEPF00011C65"}}
    Response:
{"error":{"code":"itemNotFound","message":"The resource could not be found.","innerError":{"date":"2025-05-07T09:31:28","request-id":"17a44641-4204-4811-b176-58a379125b5d","client-request-id":"17a44641-4204-4811-b176-58a379125b5d"}}}
```

or

```
[2025-05-09 08:43:36.353] [23796] [error] [RESTkitClient] Http request (OneDriveClient::GetDefaultDrive) GET: https://graph.microsoft.com/v1.0/sites/<TenantName>.sharepoint.com,8fd7d761-4f99-4fdc-a0aa-de6b685e5306,56d1fa73-2339-4329-9df3-61100d751650/drive - 404
    error: Item not found: The resource could not be found.(404)
   "{"error":{"code":"itemNotFound","message":"The resource could not be found.","innerError":{"date":"2025-05-09T06:43:36","request-id":"17a44641-4204-4811-b176-58a379125b5d","client-request-id":"17a44641-4204-4811-b176-58a379125b5d"}}}"
```



To investigate, use GraphExplorer to check the get request for this document library:

[https://developer.microsoft.com/en-us/graph/graph-explorer](https://developer.microsoft.com/en-us/graph/graph-explorer)

## Workarounds

1\) Enable the setting "[Add all SharePoint document libraries](https://docs.konnekt.io/configuration/mappings/auto-mapping#map-all-document-libraries)".

If enabled KONNEKT will use the [List drives](https://learn.microsoft.com/en-us/graph/api/drive-list?view=graph-rest-1.0\&tabs=http) request to retrieve all document libraries from Site Collections.

{% hint style="info" %}
Please be aware that enabling this setting will cause existing file links to break.
{% endhint %}

2\) Use "[Managed Mappings](../../../configuration/mappings/managed-mappings.md)" to map the important document libraries and disable the setting "[Sharepoint Sites Autodiscovery](https://docs.konnekt.io/configuration/mappings/auto-mapping#map-all-document-libraries)".

## GitHub issue

[https://github.com/SharePoint/sp-dev-docs/issues/10241](https://github.com/SharePoint/sp-dev-docs/issues/10241)

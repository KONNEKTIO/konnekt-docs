# Reproduce file issues with Graph Explorer

When users report slow browsing, failed file opens, or other file operation errors and KONNEKT debug logs show Graph API errors, Microsoft Graph Explorer lets you reproduce the failing request directly in the browser. This isolates whether the root cause is on the Microsoft 365 backend or in KONNEKT, and produces clean evidence for a Microsoft support ticket.

{% hint style="info" %}
Microsoft Graph Explorer is a free, browser-based tool from Microsoft. It sends requests to the Microsoft Graph API, which is the same interface KONNEKT, the Microsoft OneDrive sync app, Microsoft Teams, and Microsoft 365 itself use to read and write SharePoint Online and OneDrive files. No installation is required.
{% endhint %}

## When to use this guide

Use this procedure when:

* Multiple users report the same issue at the same time (often a sign of a backend problem).
* KONNEKT debug logs show Graph API errors (HTTP 429, 500, 503, 504, or `UnknownError`).
* You need to prove to Microsoft support that the issue is not caused by third-party software.
* Intermittent slowness persists after the usual KONNEKT checks have been ruled out.

### Collect and inspect the debug log

The normal way to get KONNEKT logs to support is by running `crashguard.exe` from `C:\Program Files\Konnekt`. That flow packages the logs and uploads them silently in the background - in most cases, neither the user nor the admin notices anything happening. See [Debug log preparation](https://docs.konnekt.io/troubleshooting/debug-log-preparation) for the standard support workflow.

The Graph Explorer workflow is different: you need to open the log file yourself, locally, to copy the failing request URL and `request-id` into Graph Explorer. The log files are located at:

```
%LOCALAPPDATA%\Konnekt
```

KONNEKT keeps up to six rotating log files of about 1 MB each. Sort by modification time and start with the most recent file. Open it in a text editor and search for `error` or for the HTTP status code you are investigating (for example, `504`).

Before reproducing the issue, set the log level to **Debug** so that full Graph API request URLs and responses are captured. See [Logging](https://docs.konnekt.io/configuration/system-settings/logging) for how to change the log level via the Preferences UI, the registry, or a managed policy.

### What a Graph API error looks like in the KONNEKT log

A typical error entry:

```
[2026-04-22 14:14:25.281] [22380] [error] [RESTkitClient] Http request (OneDriveClient::GetItemByPath)
GET: https://graph.microsoft.com/v1.0/drives/b!YbLv.../root:%2F...%2F03:?$select=remoteItem,id,name,... - 504
    error: Unrecognized response(504)
    "{"error":{"code":"UnknownError","message":"","innerError":{
      "date":"2026-04-22T12:14:25",
      "request-id":"dc38b1d9-cd9d-4f3d-b75a-5448695fa719",
      "client-request-id":"dc38b1d9-cd9d-4f3d-b75a-5448695fa719"
    }}}"
```

Note these values for later steps:

* The full `GET` URL (copy everything up to, but not including, the HTTP status code).
* The HTTP status code (504 in this example).
* The `request-id` value. Microsoft support can trace the failed request using this ID.

## Prerequisites

* Access to the affected user's Microsoft 365 account, or the user available to sign in themselves.
* A modern web browser (Microsoft Edge, Chrome, Firefox, or Safari).
* The exact file path and file name reported by the user, or the Graph API URL from the debug log.
* Global Administrator access to the Microsoft 365 admin center (only if you plan to open a Microsoft support ticket).

{% hint style="warning" %}
You must sign in as the user who is experiencing the issue, not as an administrator. Using a different account changes the permissions and file access, which invalidates the test.
{% endhint %}

## Step 1: Open Graph Explorer

1. Open your browser and navigate to `https://developer.microsoft.com/graph/graph-explorer`.
2. Click **Sign in** in the top-left corner.
3. Sign in with the credentials of the affected user.

## Step 2: Grant the required permissions

Graph Explorer uses delegated permissions. For file-related tests, grant the following scopes:

| Scope            | Purpose                                                 |
| ---------------- | ------------------------------------------------------- |
| `User.Read`      | Read the signed-in user's profile                       |
| `Files.Read`     | Read the user's OneDrive files                          |
| `Files.Read.All` | Read all files the user has access to                   |
| `Sites.Read.All` | Read items from SharePoint sites the user has access to |

To grant the scopes:

1. In Graph Explorer, click the **Modify permissions** tab below the query input.
2. Locate each scope in the list.
3. Click **Consent** next to each scope.
4. Accept the consent prompt.

For the full scope reference, see [Microsoft's permissions reference](https://learn.microsoft.com/graph/permissions-reference).

## Step 3: Run a test query

Set the HTTP method to `GET` and enter one of the queries below in the request URL field. Replace placeholder values in curly braces with real values.

### Option A: Reuse the URL from the KONNEKT debug log

Copy the full URL from the log line that starts with `GET: https://graph.microsoft.com/...`. Paste everything up to (but not including) the HTTP status code into the Graph Explorer URL field.

This is the preferred option because it reproduces the exact request that failed.

### Option B: Build the query manually

To list the user's OneDrive root folder:

```
GET https://graph.microsoft.com/v1.0/me/drive/root/children
```

To access a specific file by path:

```
GET https://graph.microsoft.com/v1.0/me/drive/root:/Documents/Reports/example.pdf
```

To access a file on a SharePoint site, first get the site ID:

```
GET https://graph.microsoft.com/v1.0/sites/{hostname}:/{site-path}
```

Then query the file using that site ID:

```
GET https://graph.microsoft.com/v1.0/sites/{site-id}/drive/root:/Shared Documents/Folder/example.pdf
```

Click **Run query** and review the response panel.

## Step 4: Interpret the result

The response pane shows an HTTP status code and a JSON body. Use the table below to classify the result and decide the next step.

| Status code                                                                   | Meaning                                                                | Next step                                                                                                                                                    |
| ----------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `200 OK`                                                                      | The Graph API call succeeded. The file is accessible at the API level. | The issue is on the KONNEKT side or in the client environment. Return to the [Troubleshooting hub](https://docs.konnekt.io/troubleshooting).                 |
| `401 Unauthorized`                                                            | The token is missing, expired, or invalid.                             | Sign out of Graph Explorer and sign in again. If the error persists, see [Access token issues](https://docs.konnekt.io/troubleshooting/access-token-issues). |
| `403 Forbidden`                                                               | The signed-in user does not have permission for this file or site.     | Not a KONNEKT or Microsoft backend issue. Verify permissions in the SharePoint web interface.                                                                |
| `404 Not Found`                                                               | The file or folder does not exist at the given path.                   | Verify the path. The file may have been moved, renamed, or deleted.                                                                                          |
| `429 Too Many Requests`                                                       | SharePoint Online throttling.                                          | Microsoft-side rate limiting. Check the `Retry-After` header, wait, and retry. Throttling prevention settings can reduce recurrence.                         |
| `500 Internal Server Error`, `503 Service Unavailable`, `504 Gateway Timeout` | Microsoft backend error.                                               | The issue is on the Microsoft side. Continue with the next steps.                                                                                            |
| `UnknownError` in the response body                                           | Microsoft backend error without a specific code.                       | Same as above. Capture the `request-id` and open a Microsoft support ticket.                                                                                 |

## Step 5: Capture evidence

Before closing Graph Explorer, document the test. Good evidence makes support tickets faster to resolve.

Collect:

* A screenshot of the Graph Explorer window showing the query URL, the HTTP status code, and the response body.
* The date and time of the test, including time zone.
* The signed-in user's UPN (for example, `user@contoso.com`).
* The exact file path that was tested.
* The `request-id` value from the JSON response body.
* For intermittent errors, repeat the query several times and capture each result.

## Step 6: Open a Microsoft support ticket

Only follow this step if Graph Explorer returned a 500, 503, 504, or `UnknownError` response.

1. Navigate to `https://admin.microsoft.com` and sign in with a Global Administrator account.
2. Go to **Support** -> **New service request**.
3. Select **SharePoint Online** or **OneDrive for Business** as the affected service, matching the endpoint that failed.
4. Describe the issue and attach the screenshots from the previous step.
5. Include the `request-id` from both the KONNEKT debug log and the Graph Explorer response. This allows Microsoft to trace the exact failed requests.
6. State explicitly that the issue was reproduced in Microsoft Graph Explorer.

{% hint style="info" %}
Including Graph Explorer evidence signals that third-party causes have already been ruled out. Microsoft support typically routes these tickets faster.
{% endhint %}

## Common Graph API endpoints

Quick reference for the endpoints most often seen in KONNEKT debug logs:

| Operation                   | Endpoint                                         |
| --------------------------- | ------------------------------------------------ |
| User profile                | `GET /me`                                        |
| OneDrive root listing       | `GET /me/drive/root/children`                    |
| File by path (OneDrive)     | `GET /me/drive/root:/{path}`                     |
| File by item ID             | `GET /drives/{drive-id}/items/{item-id}`         |
| Site by hostname and path   | `GET /sites/{hostname}:/{site-path}`             |
| SharePoint drives on a site | `GET /sites/{site-id}/drives`                    |
| File content download       | `GET /drives/{drive-id}/items/{item-id}/content` |
| Delta query                 | `GET /drives/{drive-id}/root/delta`              |

For the full reference, see the [Microsoft Graph Drive API](https://learn.microsoft.com/graph/api/resources/drive).

### Similar Problems

* [Sites missing or folders empty](https://docs.konnekt.io/troubleshooting/causes-of-missing-content/sites-missing-or-folders-empty) - for SharePoint Search backend errors
* [Access token issues](https://docs.konnekt.io/troubleshooting/access-token-issues) - for 401 Unauthorized responses
* [How to deal with error(s)](https://docs.konnekt.io/troubleshooting/how-to-deal-with-error-s) - for errors on specific files
* [Debug log preparation](https://docs.konnekt.io/troubleshooting/debug-log-preparation) - how to collect logs with Graph API details

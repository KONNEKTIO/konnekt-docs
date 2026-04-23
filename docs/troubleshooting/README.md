---
description: >-
  here you can find some warning or error messages and the reason and solution
  for each one.
---

# Troubleshooting

Start here when something isn't working. Follow these steps to identify your issue and jump to the relevant resolution page.

## Before you start

If **multiple users report the same issue at the same time**, or if KONNEKT debug logs show Graph API errors (HTTP 429, 500, 503, 504, or `UnknownError`), the root cause may be on the Microsoft 365 backend rather than in KONNEKT. Confirm this first: [Reproduce file issues with Graph Explorer](https://docs.konnekt.io/troubleshooting/reproduce-file-issues-with-graph-explorer).

## What's the problem?

### KONNEKT drives or shares are not visible

1. **Is KONNEKT installed?**
   * Check: `Get-WmiObject -Class Win32_Product | Where-Object { $_.Name -like "*Konnekt*" }`
   * Not installed → [Install KONNEKT](https://docs.konnekt.io/installation/setup)
   * On ARM64 devices, make sure you installed the ARM64 version. An x64 install on ARM64 will appear successful but the driver will fail to load. → [Failed to open Device](https://docs.konnekt.io/troubleshooting/failed-to-open-device)
2. **Has the device been rebooted after installation?**
   * KONNEKT requires a reboot to load its kernel-mode driver. Reboot and check again.
3. **Is the KONNEKT service running?**
   * Check: `Get-Service -Name "Konnekt*"`
   * Not running → restart the service or reinstall.
4. **Is the user signed in?**
   * Right-click the KONNEKT tray icon → **Accounts**. If no account is listed, sign in.
   * "Admin approval required" → [Grant tenant-wide admin consent](https://docs.konnekt.io/installation/security/grant-admin-consent-in-enterprise-applications)
5. **Drive or share is visible but clicking does nothing?**
   * → [Clicking a share does nothing](https://docs.konnekt.io/troubleshooting/clicking-a-share-does-nothing)

### Sites or libraries are missing

1. **Using auto-mapping?**
   * Check that `O365SharepointUsage = 1` in the registry.
   * Verify the user has access to the site in the SharePoint web interface.
   * Check the KQL site query - a restrictive query may exclude the site. See [Auto mapping](https://docs.konnekt.io/configuration/mappings/auto-mapping).
   * Verify the user's Microsoft Entra ID group membership if sites are filtered by group.
   * Site owner but not member? KONNEKT's discovery only finds sites the user is a **member** of. → [Some sites or libraries do not appear in KONNEKT](https://docs.konnekt.io/troubleshooting/causes-of-missing-content/some-sites-or-libraries-do-not-appear-in-konnekt)
2. **Using managed mappings?**
   * Check that the `SharepointSites` policy is applied: `gpresult /r` or check the registry.
   * Verify the SharePoint URL in the policy is correct and accessible.
3. **Trying to add a share manually and getting "Failed to open site: Key not found"?**
   * → [Add Share: "Key not found"](https://docs.konnekt.io/troubleshooting/add-share-key-not-found)
4. **Site exists in SharePoint but not in KONNEKT?**
   * The user may lack permission to the site. Test access via the SharePoint web interface.
   * The site type may not match the KQL query (for example, personal OneDrive sites are not discovered by the default query).

→ [Sites missing or folders empty](https://docs.konnekt.io/troubleshooting/causes-of-missing-content/sites-missing-or-folders-empty) | [Some sites or libraries do not appear](https://docs.konnekt.io/troubleshooting/causes-of-missing-content/some-sites-or-libraries-do-not-appear-in-konnekt)

### Folders are empty

1. **All libraries empty?**
   * Admin consent may not be granted, or the API permissions may be incomplete.
   * → [Grant tenant-wide admin consent](https://docs.konnekt.io/installation/security/grant-admin-consent-in-enterprise-applications)
   * → [Empty libraries](https://docs.konnekt.io/troubleshooting/causes-of-missing-content/empty-libraries)
2. **Specific library empty?**
   * The user may not have permission to the library's content. Check SharePoint permissions.
   * The library may genuinely be empty.
3. **Managed mapping shows an empty folder?**
   * The site URL in the policy may be incorrect. Verify it by opening the URL in a browser.

→ [Empty libraries](https://docs.konnekt.io/troubleshooting/causes-of-missing-content/empty-libraries) | [Sites missing or folders empty](https://docs.konnekt.io/troubleshooting/causes-of-missing-content/sites-missing-or-folders-empty)

### Authentication errors

1. **"Failed to obtain access token"**
   * → [Access token issues](https://docs.konnekt.io/troubleshooting/access-token-issues)
2. **MFA prompt loop (repeated MFA prompts)**
   * Conditional Access policy conflict or WAM broker issue.
   * → [Conditional Access](https://docs.konnekt.io/installation/security/conditional-access)
3. **Wrong account signed in**
   * Right-click tray icon → **Accounts** → remove the wrong account → add the correct one.
4. **"Admin approval required"**
   * → [Grant tenant-wide admin consent](https://docs.konnekt.io/installation/security/grant-admin-consent-in-enterprise-applications)

→ [Access token issues](https://docs.konnekt.io/troubleshooting/access-token-issues)

### File operation errors

1. **Upload failed**
   * Check the error details via tray icon → **Errors**.
   * Verify network connectivity.
   * Check if SharePoint throttling is occurring (look for HTTP 429 in debug logs). If you see throttling or backend errors, [reproduce with Graph Explorer](https://docs.konnekt.io/troubleshooting/reproduce-file-issues-with-graph-explorer) to confirm Microsoft-side issues.
   * → [How to deal with error(s)](https://docs.konnekt.io/troubleshooting/how-to-deal-with-error-s)
2. **File locked / read-only unexpectedly**
   * Another user may have the file open without co-authoring enabled.
   * File may exceed the read-only size threshold. → [Open file size limitations](https://docs.konnekt.io/configuration/system-settings/open-file-size-limitations)
3. **Permission denied**
   * The user lacks write permission in SharePoint. Verify via the web interface.
4. **"Path too long" or filename errors**
   * Check path and filename length against the limits. → [What is the maximum path and file name length?](https://docs.konnekt.io/troubleshooting/what-is-the-maximum-path-and-file-name-length)

→ [How to deal with error(s)](https://docs.konnekt.io/troubleshooting/how-to-deal-with-error-s)

### Opening Office files fails

1. **Office shows a warning on open ("could harm your computer")**
   * Mark of the Web (MOTW) is applied to files from network locations. → [Opening MS Office documents display a warning message](https://docs.konnekt.io/troubleshooting/opening-ms-office-documents-displays-a-warning-message)
   * Often resolved by adding KONNEKT paths to trusted sites. → [Add KONNEKT paths as Trusted sites](https://docs.konnekt.io/troubleshooting/add-konnekt-paths-as-trusted-sites)
2. **Double-clicking an Office file does nothing or Excel macro files won't open**
   * KONNEKT paths need to be in the Trusted Sites zone. → [Add KONNEKT paths as Trusted sites](https://docs.konnekt.io/troubleshooting/add-konnekt-paths-as-trusted-sites)
3. **KONNEKT crashes when opening or previewing Office files**
   * Attack Surface Reduction (ASR) rules may be blocking KONNEKT. Exclude `Konnekt.exe` and `KonnektStarter.exe` from the "Office Child Process" ASR rule. → [Risky action blocked](https://docs.konnekt.io/troubleshooting/risky-action-blocked)
4. **Office shows an outdated version of a file**
   * → [Office shows outdated versions](https://docs.konnekt.io/troubleshooting/office-shows-outdated-versions)

### Performance issues

1. **Slow folder browsing**
   * Check item count in the folder (>1,000 items slows browsing).
   * Check cache settings - a very low TTL causes more API calls.
   * If slowness correlates with Graph API 429 or 5xx errors in the debug log, [reproduce with Graph Explorer](https://docs.konnekt.io/troubleshooting/reproduce-file-issues-with-graph-explorer) to confirm throttling or backend issues.
2. **Slow file open**
   * Check file size and network bandwidth.
   * Check for throttling (HTTP 429 in logs). If present, [reproduce with Graph Explorer](https://docs.konnekt.io/troubleshooting/reproduce-file-issues-with-graph-explorer).
3. **Intermittent slowness (especially mornings)**
   * Likely antivirus scanning KONNEKT drives.
   * → [Slow performance or errors caused by antivirus scanning](https://docs.konnekt.io/troubleshooting/slow-performance-or-errors-caused-by-antivirus-scanning)

### Other issues

| Issue                           | Resolution                                                                                                                                                                                                                                 |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| PDF preview broken (Windows 11) | → [PDF preview broken after Windows 11 update](https://docs.konnekt.io/troubleshooting/pdf-preview-broken-after-windows-11-update)                                                                                                         |
| Grey X on files                 | Expected behavior - KONNEKT marks files as `FILE_ATTRIBUTE_OFFLINE` to save bandwidth. Not an error. See [Why is there a grey X or brown suitcase](https://docs.konnekt.io/troubleshooting/why-is-there-a-grey-x-on-my-files-and-folders). |
| Brown suitcase overlay on files | File is marked for offline use. Expected behavior.                                                                                                                                                                                         |
| KONNEKT tray icon missing       | Reboot the device. If still missing, reinstall KONNEKT.                                                                                                                                                                                    |
| Can't resolve the issue         | → [Prepare debug logs](https://docs.konnekt.io/troubleshooting/debug-log-preparation) and [contact support](https://docs.konnekt.io/support)                                                                                               |

## Related pages

* [Reproduce file issues with Graph Explorer](https://docs.konnekt.io/troubleshooting/reproduce-file-issues-with-graph-explorer) - isolate KONNEKT issues from Microsoft 365 backend issues
* [Changelog](https://docs.konnekt.io/changelog) - recent fixes and resolved issues
* [Debug log preparation](https://docs.konnekt.io/troubleshooting/debug-log-preparation) - how to collect logs for support
* [Support](https://docs.konnekt.io/support) - how to reach KONNEKT support

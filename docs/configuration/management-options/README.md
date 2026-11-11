# Management options

KONNEKT is configured through one ADMX template that works the same in Group Policy and in Microsoft Intune. This page lists every setting, its registry value and default, and links to the page that describes it.

{% content-ref url="setting-for-intune-managed-devices/" %}
[setting-for-intune-managed-devices](setting-for-intune-managed-devices/)
{% endcontent-ref %}

{% content-ref url="setting-for-intune-managed-devices-1/" %}
[setting-for-intune-managed-devices-1](setting-for-intune-managed-devices-1/)
{% endcontent-ref %}

{% content-ref url="settings-via-gpo.md" %}
[settings-via-gpo.md](settings-via-gpo.md)
{% endcontent-ref %}

## ADMX / ADML files

You can download the ADMX / ADML files here:

{% file src="../../.gitbook/assets/KONNEKT-ADMX-ADML-2-12-0-0.zip" %}

## Where KONNEKT reads settings

ADMX policies write to the policy keys. KONNEKT reads each setting from the first of these locations that holds it:

1. `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`
2. `HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`
3. `HKEY_LOCAL_MACHINE\SOFTWARE\GlueckKanja\Konnekt`
4. `HKEY_CURRENT_USER\SOFTWARE\GlueckKanja\Konnekt`

A computer policy therefore always wins over a user policy.

## All settings

Settings marked **Registry** have no ADMX policy. Set them with a script or with Group Policy Preferences.

<details>

<summary>Mappings</summary>

| Setting | Registry value | Default | Set via | Details |
|---|---|---|---|---|
| SharePoint Sites | `SharepointSites` | Not set | ADMX | [Managed mappings](../mappings/managed-mappings.md) |
| SharePoint Sites Query | `SharepointSiteQuery` | See Auto mapping | ADMX | [Auto mapping](../mappings/auto-mapping.md) |
| SharePoint Sites Autodiscovery | `O365SharepointUsage` | 1 | ADMX | [Auto mapping](../mappings/auto-mapping.md) |
| Add all SharePoint libraries | `AddAllSharepointLibraries` | 0 | ADMX | [Additional document libraries](../mappings/add-a-document-library.md) |
| Connect drive | `ConnectDrivePolicy`, `ConnectDrive` | `H:` | ADMX | [Assign drive letters](../mappings/assign-drive-letters.md) |
| Multi-Geo | `SharepointMultiGeo` | Not set | Registry | [Multi-Geo](../mappings/multi-geo.md) |

</details>

<details>

<summary>Office and files</summary>

| Setting | Registry value | Default | Set via | Details |
|---|---|---|---|---|
| Co-Authoring | `EnableCoAuthoring` | 1 | ADMX | [Office365 Co-Authoring](../system-settings/office365-co-authoring.md) |
| Offline Attribute | `EnableOfflineAttribute` | 1 | ADMX | [Offline attribute](../system-settings/offline-attribute.md) |
| Offline Attribute Filter | `OfflineAttributeFilter` | `pdf` | ADMX | [Offline attribute](../system-settings/offline-attribute.md) |
| Open file size limitations | `OneDriveOpenFilesLargerThanReadOnly`, `OneDriveDoNotOpenFilesLargerThan` | 512 MB, 1 GB | ADMX | [Open file size limitations](../system-settings/open-file-size-limitations.md) |
| File Size Check Filter | `FileSizeCheckFilter` | All Word, Excel and PowerPoint extensions | ADMX | [Open file size limitations](../system-settings/open-file-size-limitations.md) |
| Default SharePoint link scope | `SharepointLinkScope` | 0 | ADMX | [Link scope](../system-settings/link-scope.md) |
| Download Directory | `DownloadDirectory` | `%USERPROFILE%\Downloads` | ADMX | [Download Directory](../system-settings/download-directory.md) |

</details>

<details>

<summary>Performance</summary>

| Setting | Registry value | Default | Set via | Details |
|---|---|---|---|---|
| Cache | `CachePolicy`, `CacheTTL`, `CacheSize` | 60 minutes, automatic size | ADMX | [Cache settings](../system-settings/cache-setting.md) |
| SharePoint Throttling Prevention | `SharepointThrottling` | 0 (autodetect) | ADMX | [SharePoint throttling prevention](../system-settings/throttling-prevention/sharepoint-throttling-prevention.md) |
| Client side throttling | `ClientThrottling`, `ClientThrottlingTimeWindow`, `ClientThrottlingSoftLimit`, `ClientThrottlingHardLimit` | Off | ADMX | [Throttling prevention (client side)](../system-settings/throttling-prevention/throttling-prevention-client-side.md) |

</details>

<details>

<summary>Sign-in</summary>

| Setting | Registry value | Default | Set via | Details |
|---|---|---|---|---|
| Enhanced OAuth | `EnhancedOAuth` | 0 | ADMX | [Enhanced Authentication](../system-settings/enhanced-authentication.md) |
| Disable Edge Browser Component (WebView2) | `DisableWebView2` | 0 | ADMX | [Authentication browser engine](../system-settings/authentication-browser-engine.md) |
| SkipAccountWizard | `SkipAccountWizard` | 0 | ADMX | [Skip Account Wizard](../system-settings/configure-konnekt-for-a-subset-of-users.md) |
| Account Reauthentication UI | `PopupReauthenticateAccount` | 1 | ADMX | [Account re-authentication](../gui-behavior/account-reauthentication.md) |

</details>

<details>

<summary>Explorer and tray</summary>

| Setting | Registry value | Default | Set via | Details |
|---|---|---|---|---|
| Konnekt Explorer UI | `ShellRestricted`, `ShellUploads`, `ShellHistory`, `ShellOfflineFiles`, `ShellAccounts` | All items shown | ADMX | [Explorer UI](../gui-behavior/konnekt-explorer-ui.md) |
| Tray Icon | `ShowTrayIcon` | Shown | ADMX | [Hide tray icon](../gui-behavior/hide-tray-icon.md) |
| Language | `Language` | Windows display language | ADMX | [Intune GUI settings](setting-for-intune-managed-devices-1/intune-gui-settings.md) |

</details>

<details>

<summary>Operations</summary>

| Setting | Registry value | Default | Set via | Details |
|---|---|---|---|---|
| License Key | `License` | Not set (evaluation) | ADMX, MSI property `LICENSE_KEY` | [Set license key](../other/license-key-on-multi-user-environments.md) |
| Update check | `UpdateInterval` | 120 minutes | ADMX | [Update checker](../system-settings/update-checker.md) |
| Logging Level | `LogLevel` | 2 | ADMX | [Logging](../system-settings/logging.md#log-level) |
| Log Rotation | `LogRotation` | 1 MB | Registry | [Logging](../system-settings/logging.md#log-rotation) |

</details>

## Related pages

- [Deployment](../../installation/README.md)
- [Deploy on session hosts and VDI](../../installation/deploy-on-session-hosts-and-vdi.md)

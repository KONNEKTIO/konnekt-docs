# Changelog

{% hint style="success" %}
If you'd like to **stay up to date on the latest changes and news in the KONNEKT changelog**, you can subscribe to our email update service. Subscribers will receive **email notifications** when there are new updates to the changelog.

[**Please click here to sign up for email notifications**](https://feedback.konnekt.io/)**.**
{% endhint %}

## Versions

### 2.11 (Published 2025-05-19)

Add:

* Enhanced SharePoint throttling prevention by introducing local limits based on the number of requests per time (client side throttling)
* Support for Sensitivity Labels with Microsoft Purview Information Protection (fka Microsoft Information Protection MIP) in non-co-authoring scenarios (e.g. PDF files)
* Improved handling when multiple files are selected in explorer

Fix:

* Renaming files mapped on a drive letter may result in an error: "Can't read from the source file"
* Direcories may disappear when client has network issues
* Account creation may fail if user name contains multibyte characters (e.g. kanji)

**Downloads**

* [KONNEKT 2.11.0.0 Windows X64 64 Bit](https://trial.konnekt.io/releases/Konnekt-X64-2.11.0.0.Msi)
* [KONNEKT 2.11.0.0 Windows X86 32 Bit](https://trial.konnekt.io/releases/Konnekt-X86-2.11.0.0.Msi)
* [KONNEKT 2.11.0.0 Windows ARM 64 Bit](https://trial.konnekt.io/releases/Konnekt-Arm64-2.11.0.0.Msi)
* [KONNEKT ADMX-ADML 2.11.0.0](configuration/management-options/#admx-adml-files)

### 2.10.2 (Published 2024-12-12)

Add:

* Silent authentication for SSO-enabled environments (80)

Fix:

* Improved proxy detection (9669)
* Moving and renaming files sometimes not stable (9594)
* Stability improvements

**Downloads**

* [KONNEKT 2.10.2.0 Windows X64 64 Bit](https://trial.konnekt.io/releases/Konnekt-X64-2.10.2.0.Msi)
* [KONNEKT 2.10.2.0 Windows X86 32 Bit](https://trial.konnekt.io/releases/Konnekt-X86-2.10.2.0.Msi)
* [KONNEKT 2.10.2.0 Windows ARM 64 Bit](https://trial.konnekt.io/releases/Konnekt-Arm64-2.10.2.0.Msi)

### 2.10.1 (Published 2024-11-22)

Fix:

* Improved SharePoint throttling management
* Parsing errors when checking `IsSiteReadOnly` on some SharePoint sites
* Opening Microsoft Office templates files from some drives opens the template instead of creating new document from template
* Shellext.dll might cause crashes
* Stability improvements

### 2.10 (Published 2024-08-28)

Add:

* Opt-in to [new OAuth component](configuration/system-settings/enhanced-authentication.md) (EnhancedOAuth)
  * New Azure app registration
  * New permissions set with fewer permissions required
  * Uses OAuth 2.0 API routes
  * Namespaces are built from [default domain](https://learn.microsoft.com/en-us/microsoft-365/admin/setup/domains-faq?view=o365-worldwide#how-do-i-set-or-change-the-default-domain-in-microsoft-365) (\\\onedrive-\<DefaultDomainName>\\...), no longer from [initial domain](https://learn.microsoft.com/en-us/microsoft-365/admin/setup/domains-faq?view=o365-worldwide#how-do-i-set-or-change-the-default-domain-in-microsoft-365) (\\\onedrive-\<InitialDomainName>\\...).
  * Intune DeviceIDs are sent during authentication
  * Works with Conditional Access policies, when using excluded apps (743)
* Improved lock and read-only check for files and directories (725)
* Added Co-Authoring for editing (="open") Microsoft Office templates in Windows File Explorer context menu. (68)

Fix:

* File Explorer cannot handle sites ending with a blank character (63)
* Adobe Acrobat might crash if not run in compatibility mode (67)
* New Notepad cannot save files (invalid function) (8599)
* Stability improvements

### 2.9.1 (Published 2024-02-15)

Add:

* Support for more than 10 KONNEKT Accounts

Fix:

* Account deletion may leave ghost volumes
* Explorer freezes if KONNEKT account or share is removed
* KONNEKT cannot find sites with dot in name when adding shares or managed mappings
* Windows Terminal Servers (Windows Server 2019) may freeze due to konnektrx.sys timeout after Windows Update
* Stability improvements

**Downloads**

* [KONNEKT 2.9.1.0 Windows X64 64 Bit](https://trial.konnekt.io/releases/Konnekt-X64-2.9.1.0.Msi)
* [KONNEKT 2.9.1.0 Windows X86 32 Bit](https://trial.konnekt.io/releases/Konnekt-X86-2.9.1.0.Msi)
* [KONNEKT 2.9.1.0 Windows ARM 64 Bit](https://trial.konnekt.io/releases/Konnekt-Arm64-2.9.1.0.Msi)

### 2.9.0 (Published 2023-11-16)

Add:

* Policy to disable Edge Browser component (WebView2)&#x20;
* Full support of x64 Processes on ARM64 machines

Fix:

* SharePoint throttling: Parsing issues in Retry-After header&#x20;
* Possible loss of delayed write data if disk IO pressure is high&#x20;
* ARM64 setup may show a warning&#x20;
* Gray login window due to failed browser component negotiation&#x20;
* Stability improvements

### 2.8.0 (Published 2023-10-11)

Add:

* New document from office template in CoAuthoring mode (#30)

Fix:

* Security fix for [libcurl CVE-2023-38545 (HIGH) SOCKS5 heap buffer overflow](https://curl.se/docs/CVE-2023-38545.html)
* Security fix for [libcurl CVE-2023-38546 (LOW)](https://curl.se/docs/CVE-2023-38546.html)
* Malware alarm on konnektUpdate.exe due to missing digital signature (#31)
* Re-authentication not triggered after password reset (#23)
* Uninstall and install with suppressed reboot may lead to uninstalled driver after next reboot (#3855)
* SharePoint mapping might be shown empty when cache TTL is very long (#6)
* Stability improvements

### 2.7.2 (Published 2023-09-07)

Fix:

* Authentication window may be shown without content
* Stability improvements

### 2.7.0 (Published 2023-08-10)

Add:

* "View Online" for a folder directs to corresponding subfolder in SharePoint (591)
* [Managed Mapping supports root site URLs and Teams URLs](configuration/mappings/administrative-mappings.md#policy-definition) (741)
* Login prompt negotiates for Edge Browser (791)
* File support for OneNote notebooks (2730)
* CoAuthoring for OneNote documents (2730)

Fix:

* "View SharePoint Site" context-menu broken for OneDrive (1509)
* Added favorites lost after log off (2894)
* Stability improvements

### 2.6.0 (Published 2023-07-13)

Add:

* [Circumvent error/outage of SharePoint Search](troubleshooting/sites-missing-or-folders-empty.md) (703)
* [Extend Cache TTL range in policy](configuration/system-settings/cache-setting.md#cache-ttl-time-to-live) (756)
* [Policy to configure downloads directory](configuration/system-settings/download-directory.md) (792)
* CoAuthoring support for additional file types including .xslb and office template files
* [Ready for new Intune ADMX and ADML administrative templates import (public preview)](configuration/management-options/setting-for-intune-managed-devices/) (753)
  * [New configuration & behavior for "Connect drive" policy](configuration/mappings/assign-drive-letters.md#konnekt-2.6.0-and-newer) (753)
* New Policies (754)
  * [Skip Account Wizard](configuration/system-settings/configure-konnekt-for-a-subset-of-users.md)
  * [Open File Size Limitations](configuration/system-settings/open-file-size-limitations.md)

Fix:

* Error when opening certain office files (e.g. XLSB) with sensitivity/encryption enabled (768)
* Kernel driver misinterprets modern standby as deadlocked userland (809)
* Files and Folders named with a single character cause problems in searches (866)
* Stability issues

### 2.5.8 (Published 2023-06-28)

Fix:

* Copy Link To Clipboard fails on SharePoint libraries (1271)
* Konnekt read operations may fail if content-range directive is ignored by SharePoint.
* Error logged when accessing root of document library
* File lock/checkout checks produce parsing erros in log
* Stability issues

### 2.5.7 (Published 2023-05-30)

Fix: App may crash if the access token cannot be obtained

### 2.5.6 (Published 2023-05-25)

Fix: App may crash during SSO login attempt (1046)

### 2.5.4 (Published 2023-05-16)

Fix:

* Poor response times when trying to negotiate HTTP/2 multiplexing (836)
* Managed Mappings showing empty drives  when the policy "Add all SharePoint libraries" is disabled (932)

### 2.5.2 (Published 2023-05-11)

Fix:&#x20;

* Volume free and total size is wrong (896)
* Stability issues

### 2.5.1 (Published 2023-05-10)

Fix: An invalid account token may cause issues (895)

### 2.5.0 (Published 2023-05-08)

* Add
  * Updated API handling
  * Support for [SharePoint Domain Name Change](https://learn.microsoft.com/en-us/sharepoint/change-your-sharepoint-domain-name) (765)
  * Support for Custom/Vanity SharePoint Domain Names (780)
  * [Multi-Geo support ](configuration/mappings/multi-geo.md)is always active - no dedicated config needed anymore.
* Fix
  * Unable to install MSI file located in Konnekt share (748)
  * Cannot access sites with names ending on a dot (761)
  * Failed to open .XLSB files when sensitivity/encryption is enabled (768)
  * Move Folder within a library is reversed after some seconds (775)

{% hint style="info" %}
KONNEKT version numbers 2.3 and 2.4 were skipped due to major code rework.
{% endhint %}

### 2.2.1 (2022-12-30 - Bugfix release for KONNEKT 2.2.0)

* Fix
  * Explorer may get unresponsive when creating new folder in SharePoint root - part 2 (648)
  * Deleted folders may re-appear in some scenarios (738)
  * Managed Mapping sometimes not working after machine reboot (763)
  * License check issue in version 2.2.0 (766)

#### Downloads

{% file src="../.gitbook/assets/Konnekt 2.2.1.0-Preview.zip" %}
KONNEKT 2.2.1.0 (64-Bit, 32-Bit, Arm64 versions are available)
{% endfile %}

### 2.2.0 (Published 2022-11-17)

* ADD
  * [ARM64 processor platform support ](installation/system-requirements.md#processor-platform)(662)
  * [SharePoint Throttling Prevention policy](configuration/system-settings/sharepoint-throttling-prevention.md) (730)
  * [Add to favorites in Managed Mappings](configuration/mappings/administrative-mappings.md#make-mapping-a-konnekt-favorite) (733)
  * Changed search strategy for folder browsing to work around [performance degradation of Microsoft SharePoint Online REST API](troubleshooting/slow-folder-browsing.md) (736)
* FIX
  * Explorer may get unresponsive when creating new folder in SharePoint root - part 1 (648)
  * "This file does not exist" after re-install or uninstall (649)
  * Save new file not working in special conditions, e.g. substring of existing file (651)
  * Prevent blue screen during driver update in some environments (672)
  * History misses one backslash in UNC for some entries (721)
  * Deleted folders may re-appear in some scenarios (738)

### 2.1.1 (Published 2022-07-05)

* FIX: Machine policy may not be applied correctly

### 2.1.0 (Published 2022-05-12)

* ADD
  * Multi-Geo support for OneDrive and SharePoint Online&#x20;
  * Improvements for heavy load environments
  * Remove the limit of 192 libraries per site
  * Logging level policy
* FIX
  * Pinned links in taskbar lead to SPO site instead of UNC
  * CoAuthoring setting in [ADMX](configuration/management-options/settings-via-gpo.md#admx-file) not working
  * Installer coordinator issue during setup on some RDS environments
  * Unwanted policy changes after hibernation in some environments&#x20;
  * "Enable Sharepoint Sites" option not grayed out after applying GPO/Intune policy.
  * Handling of error responses from SharePoint Online causing empty folders
  * "Add site favorite" feature

### 2.0.0 (Published 2021-12-03)

* ADD
  * Customize explorer UI ([Hide several options](configuration/gui-behavior/konnekt-explorer-ui.md), [hide tray icon](configuration/gui-behavior/hide-tray-icon.md))
  * Custom site scope ([individual search string](configuration/mappings/auto-mapping.md))
  * Automatic mappings ([Managed mappings](configuration/mappings/administrative-mappings.md))
  * [Cache settings](configuration/system-settings/cache-setting.md) (individual write handling to SharePoint Online e.g. for VDI environments)
  * [Intune Management](configuration/management-options/setting-for-intune-managed-devices-1/)
  * Offline Attribute Filter to enable explorer previews on certain file types
  * [ADMX & ADML files ](configuration/management-options/settings-via-gpo.md#admx-file)got new policies & structure
* FIX
  * Broken file links when resolving mapped drives (e.g. copy path in Outlook)
  * Stability issue when uploading files larger than 1 GB
  * Cache directory may be filled up
  * SharePoint document libraries may be shown empty

### 1.20.0 (Published 2021-04-21)

* ADD: Advanced SharePoint throttle handling
* FIX: Handling of multiple accounts in the same tenant
* FIX: Stability issues under write pressure

### 1.19.0 (Published 2021-04-06)

* ADD: Improve dialog to add shares
* FIX: Konnekt cannot reach driver after upgrade
* FIX: Konnekt needs to be restarted after hibernate

### 1.18.0 (Published 2021-02-10)

* ADD: Improve SSO flow
* FIX: SharePoint token may expire
* FIX: Proxy settings are not reevaluated on network connection changes
* FIX: Path issues if profile path contains umlauts

### 1.16.0 (Published 2020-10-22)

* FIX: Cannot access foreign tenant on Azure AD joined clients
* ADD: Reduce reauthentication frequency

### 1.15.1 (Published 2020-09-24)

* FIX: Explorer unresponsive during move/copy operations
* FIX: Cannot add or remove favorites

### 1.15.0 (Published 2020-09-03)

* FIX: Cannot save as PDF from Google Chrome

### 1.14.1 (Published 2020-07-25)

* FIX: Manually added shares always open default document library

### 1.14.0 (Published 2019-05-14)

* FIX: Cannot save PDF files in several Adobe products
* ADD: Manually add private channels from Teams

### 1.12.6 (Published 2019-04-20)

* FIX: Login issues

### 1.12.4 (Published 2019-02-26)

* FIX: Wild card matching

### 1.12.3 (Published 2019-12-19)

* FIX: Cannot create account (key not found)
* FIX: SharePoint link scope policy
* FIX: License policy order

### 1.12.0 (Published 2019-11-18)

* ADD: Improved handling of additional SharePoint document libraries
* ADD: Configure drive letter for personal OneDrive volume
* ADD: Configure SharePoint link scope (default, organization, anonymous, disabled)
* FIX: Wrong SharePoint sub-group grouping

### 1.10.1 (Published 2019-09-02)

* ADD: Better visualization of upload errors
* FIX: Shell extension does not display any shares if an upload error occurs

### 1.10.0 (Published 2019-08-30)

* ADD: Add account endpoint to sharename if displayed one left side of explorer
* FIX: Double menu in Windows Explorer
* FIX: Account context menu is not completely visible in German language
* FIX: Crash in kernel driver

### 1.9.0 (Published 2019-04-17)

* ADD: Office co-authoring support for old office file formats
* ADD: Add additional SharePoint document libraries as shares
* ADD: Option to remove manually added shares
* ADD: Policy to rename "Konnekt" in the Windows Explorer
* ADD: Rename "Personal" in OneDrive to "OneDrive"
* ADD: Registry setting to set personal folder name in OneDrive

### 1.8.2 (Published 2019-04-02)

* ADD: German localization
* ADD: Display message during volume update
* FIX: Cannot open PDF files in Adobe Acrobat and Acrobat Reader

### 1.8.0 (Published 2019-02-20)

* ADD: Policy for disabling FILE\_ATTRIBUTE\_OFFLINE
* FIX: Improved performance during start-up on terminal servers
* FIX: Office Co-authoring opens wrong URL in personal OneDrive if user was re-created (#366)
* FIX: Co-authoring does not work on mapped network drives
* FIX: Co-authoring does not work for macro enabled Excel files (#360)
* FIX: Remove add account entries for German cloud (#342)
* FIX: Race condition during start-up
* FIX: Driver does not work on Windows 7 x64
* FIX: Improved logging

### 1.7.4 (Published 2018-11-23)

* FIX: Slow performance on terminal service while browsing available site in the shell extension (#304)
* FIX: Co-Authoring not working when using Excel macro enabled files (#360)

### 1.7.1 (Published 2018-10-18)

* FIX: TMP-file creation by MS Office applications (#336)
* FIX: Cannot open PDF files from UNC paths (#340)

### 1.7.0 (Published 2018-09-27)

* ADD: Improved proxy authentication support
* FIX: TMP-file creation by MS Office applications (#336)
* FIX: Improved wild card match of file names
* FIX: Cannot delete account if it is in error state
* FIX: Cannot open PDF files from UNC paths (#340)
* FIX: Enable SharePoint sites is greyed out in settings (#347)
* FIX: Crash in kernel driver

### 1.6.0 (Published 2018-06-15)

* FIX: Personal OneDrive is not updated if it was changed outside of Konnekt
* FIX: Improved rename operations
* FIX: Fixed a race condition during delete

### 1.5.0 (Published 2018-06-05)

* ADD: Support SharePoint sites without any default document library
* ADD: Improve OneDrive provider
* ADD: Set default log level to INFO
* FIX: Race condition during rename operation
* FIX: Crash during startup

### 1.4.15 (Published 2018-05-14)

* ADD: Evaluation version enables SharePoint sites by default
* FIX: Setup fails on Windows Server 2008

### 1.4.10 (Published 2018-05-02)

* FIX: Konnekt creates 0-byte files
* FIX: Potential deadlock in OneDrive provider
* FIX: Update window is not DPI aware

### 1.4.4 (Published 2018-04-09)

* FIX: Update window is not closed after clicking the version number
* FIX: Cannot open multiple PDF files in Acrobat Reader

### 1.4.2 (Published 2018-03-05)

* FIX: Context menu for localized SharePoint sites

### 1.4.1 (Published 2018-02-16)

* FIX: Office co-authoring fails to open url if the UPN contains minus characters

### 1.4.0 (Published 2018-01-30)

* ADD: Faster startup on terminal servers
* ADD: Improve SharePoint volume handling
* ADD: Group policy setting for co-authoring

### 1.3.3 (Published 2017-12-19)

* FIX: Race condition (#303)

### 1.3.2 (Published 2017-12-08)

* FIX: Acrobat Reader not working on Konnekt-UNC path (#216)
* FIX: Cannot save outlook attachments in Konnekt-UNC path on Windows 10 anniversary update (#301, #302)

### 1.3.0 (Published 2017-11-06)

* ADD: Display private SharePoint groups

### 1.2.4 (Published 2017-09-13)

* FIX: Crash during automatic update

### 1.2.0 (Published 2017-09-08)

* FIX: Crash after adding an account
* FIX: Rename open file

### 1.1.0 (Published 2017-08-25)

* ADD: Settings dialog
* ADD: Show favorite and personal shares in explorer's left side
* ADD: Remove chromium embedded framework in favor of MSHTML
* ADD: Automatically create account on first start if computer is joined to an Azure AD
* ADD: Setting to connect first personal volume to drive H:
* FIX: Cannot access SharePoint site if its name contains special characters (#258)
* FIX: Cannot open OneNote file in Konnekt (#261)
* FIX: No content is shown after folder rename (#255)
* FIX: Cannot add O365 account when proxy is used

### 1.0.2 (Published 2017-05-17)

* ADD: License key management
* ADD: Crash dump collects more information

### 1.0.1 (Published 2017-05-15)

* FIX: Cannot save document from website to SharePoint site using MS Edge

### 1.0.0 (Published 2017-05-12)

* FIX: Cannot delete directory if it contains files

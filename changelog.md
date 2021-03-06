# Changelog

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
  * [Intune Management](configuration/management-options/setting-for-intune-managed-devices/)
  * Offline Attribute Filter to enable explorer previews on certain file types
  * [ADMX & ADML files ](configuration/management-options/settings-via-gpo.md#admx-file)got new policies & structure
* FIX
  * Broken file links when resolving mapped drives (e.g. copy path in Outlook)
  * Stability issue when uploading files lager than 1 GB
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
* FIX: Account context menu not completely visible in german language
* FIX: Crash in kernel driver

### 1.9.0 (Published 2019-04-17)

* ADD: Office co-authoring support for old office file formats
* ADD: Add additional SharePoint document libraries as shares
* ADD: Option to remove manually added shares
* ADD: Policy to rename "Konnekt" in the Windows Explorer
* ADD: Rename "Personal" in OneDrive to "OneDrive"
* ADD: Registry setting to to set personal folder name in OneDrive

### 1.8.2 (Published 2019-04-02)

* ADD: German localization
* ADD: Display message during volume update
* FIX: Cannot open PDF files in Adobe Acrobat and Acrobat Reader

### 1.8.0 (Published 2019-02-20)

* ADD: Policy for disabling FILE\_ATTRIBUTE\_OFFLINE
* FIX: Improved performance during start-up on terminal servers
* FIX: Office Co-authoring opens wrong URL in personal OneDrive if user was re-created (#366)
* FIX: Co-authoring does not work on mapped network drives
* FIX: Co-authoring does not work for macro enabled excel files (#360)
* FIX: Remove add account entries for german cloud (#342)
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
* ADD: Support for german and chinese O365 cloud (#245)
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

# Manual uninstallation

1. If Konnekt is listed under programs you can uninstall it, but if the uninstall process fails or it's not available:
   * Open **Regedit** and go to`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall`
   * Check the GUID-named subkeys for the one that belongs to KONNEKT
     * Check the DisplayName for '**Konnekt xy'**
     * Check the Publisher for '**Glück & Kanja Consulting'**
   * Delete the whole key
2.  Remove the driver

    * Delete the following registry keys&#x20;

    `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\konnekt`

    `Computer\HKEY_CURRENT_USER\SOFTWARE\Classes\Access.Application.16`

    `Computer\HKEY_USERS\S-1-5-21-83704801-2950256748-3048643274-500\SOFTWARE\Classes\Excel.Sheet.12`

    `Computer\HKEY_USERS\S-1-5-21-83704801-2950256748-3048643274-500\SOFTWARE\Classes\Excel.Sheet.8`

    `Computer\HKEY_USERS\S-1-5-21-83704801-2950256748-3048643274-500\SOFTWARE\Classes\Excel.SheetMacroEnabled.12`

    `Computer\HKEY_USERS\S-1-5-21-83704801-2950256748-3048643274-500\SOFTWARE\Classes\PowerPoint.Show.12`

    `Computer\HKEY_USERS\S-1-5-21-83704801-2950256748-3048643274-500\SOFTWARE\Classes\PowerPoint.Show.8`

    `Computer\HKEY_USERS\S-1-5-21-83704801-2950256748-3048643274-500\SOFTWARE\Classes\PowerPoint.ShowMacroEnabled.12`

    `Computer\HKEY_USERS\S-1-5-21-83704801-2950256748-3048643274-500\SOFTWARE\Classes\Word.Document.12`

    `Computer\HKEY_USERS\S-1-5-21-83704801-2950256748-3048643274-500\SOFTWARE\Classes\Word.Document.8`

    `Computer\HKEY_USERS\S-1-5-21-83704801-2950256748-3048643274-500\SOFTWARE\Classes\Word.DocumentMacroEnabled.12`

    * Run `net stop konnekt`
    * Delete `c:\windows\system32\drivers\konnektrx.sys`
3. Remove shell extensions:
   * Run `regsvr32 /unregister "C:\Program Files\Konnekt\shellext.dll`
   * Restart the explorer&#x20;
     * Navigate to Task Manager
     * Search for Explorer
     * Right-click on it
     * Restart or logoff/logon
4. Delete Konnekt folder under `%localappdata%`
5. Delete `C:\Program Files\Konnekt`
6.  Delete the following keys in the Windows Registry

    `HKEY_CURRENT_USER\SOFTWARE\GlueckKanja\Konnekt`

    `HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`

    `HKEY_LOCAL_MACHINE\SOFTWARE\GlueckKanja\Konnekt`

    `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`


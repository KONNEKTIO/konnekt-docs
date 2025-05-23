# Manual uninstallation

{% hint style="info" %}
To uninstall KONNEKT from your system, we recommend to use the uninstaller that is part of KONNNEKT and can be activated via the _add remove software_ dialog of Windows.
{% endhint %}

However, if you can not leverage the uninstaller or there are settings left on your system after running the uninstaller, you may use the information given on this site, to remove KONNEKT from your system.&#x20;

{% hint style="danger" %}
This procedure is for IT pros, only. It is not supported by our service team.
{% endhint %}

## Remove Installer

* Open **Regedit** and go to\
  `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall`
* Check the GUID-named subkeys for the one that belongs to KONNEKT
  * Check the DisplayName for '**Konnekt'**
  * Check the Publisher for '**glueckkanja-gab AG'**
* Delete the whole key

## Remove Driver

* Run `net stop konnekt`
* Delete `c:\windows\system32\drivers\konnektrx.sys`
* Delete `C:\Windows\System32\konnektnp.dll`

## Remove the shell extensions

* Run `regsvr32 /unregister "C:\Program Files\Konnekt\shellext.dll`
*   Remove the following Windows Registry keys for **every user** on the machine:

    ```
    HKCU\SOFTWARE\Classes\Access.Application.16\shell\konnekt
    HKCU\SOFTWARE\Classes\Excel.Sheet.12\shell\konnekt
    HKCU\SOFTWARE\Classes\Excel.Sheet.8\shell\konnekt
    HKCU\SOFTWARE\Classes\Excel.SheetMacroEnabled.12\shell\konnekt
    HKCU\SOFTWARE\Classes\PowerPoint.Show.12\shell\konnekt
    HKCU\SOFTWARE\Classes\PowerPoint.Show.8\shell\konnekt
    HKCU\SOFTWARE\Classes\PowerPoint.ShowMacroEnabled.12\shell\konnekt
    HKCU\SOFTWARE\Classes\Word.Document.12\shell\konnekt
    HKCU\SOFTWARE\Classes\Word.Document.8\shell\konnekt
    HKCU\SOFTWARE\Classes\Word.DocumentMacroEnabled.12\shell\konnekt
    ```

## Clean the registry

Remove the following Windows Registry keys on the **machine**:

```
HKLM\SYSTEM\CurrentControlSet\Services\konnekt
HKLM\SOFTWARE\GlueckKanja\Konnekt
HKLM\SOFTWARE\Policies\GlueckKanja\Konnekt
```

Remove the following Windows Registry keys for **every user** on the machine:

```
HKCU\SOFTWARE\GlueckKanja\Konnekt
HKCU\SOFTWARE\Policies\GlueckKanja\Konnekt
```

## Clean Folders

* Delete the "Konnekt" folder under `%localappdata%`
* Delete `C:\Program Files\Konnekt`

## Restart

Some of the changes (like driver or the shell extensions) may need&#x20;

* a reboot\
  or
* log-off & log-on\
  or
* restart the explorer with this procedure:
  * Navigate to Task Manager
  * Search for Explorer
  * Right-click on it
  * Click Restart.

If you are unsure, please reboot.

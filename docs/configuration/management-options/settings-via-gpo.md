# Settings via GPO

## Registry key location

**Settings** are stored in:\
\
`HKEY_CURRENT_USER\SOFTWARE\GlueckKanja\Konnekt`

`HKEY_LOCAL_MACHINE\SOFTWARE\GlueckKanja\Konnekt`

**Policies** are stored in:

`HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`

`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`

## ADMX file

To use group policies for KONNEKT please use the attached ADMX Template. For scenarios where a language file is needed please see the language folder in the ZIP file.

With the ADMX Template the following settings can be set:

![](<../../.gitbook/assets/image (51).png>)

You can **download** the ADMX/ADML files [here](./#admx-adml-files).

## **GPO / Registry key priorities**

KONNEKT evaluates the settings of the GPO / registry in this order:

1. HKEY\_LOCAL\_MACHINE (HKLM)
2. HKEY\_CURRENT\_USER (HKCU)

## Preferences Menu Behavior

Some of the settings are also available in the preferences menu:

![](<../../.gitbook/assets/2022-08-02 15_37_07-Window.png>)

If a GPO is enforced, the corresponding setting in the preferences menu will still be shown but disabled for user change.

# What is the maximum path and file name length?

KONNEKT has to respect the path and file name length limits of both worlds:

* **SharePoint Online** \
  and
* **Windows**.

The maximum length of a filename including path is **260 characters** in total.

It consists of path and file name:

* **path** is: `\\onedrive-<yourTenant>\<site>\<library>\<foldernames>\`\
  It is limited to 248 characters.
* **file name** is: `<name>.<extension>`\
  12 characters are always preserved for the file name (8.3). Path and file name together must not exceed the limit of 260 characters in total.

These limits are mainly caused by Windows OS and File Explorer restrictions. Details can be found [here](https://docs.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=cmd).

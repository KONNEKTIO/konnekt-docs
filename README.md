---
description: Access OneDrive, SharePoint and Teams lightning fast with Windows Explorer
---

# Welcome

KONNEKT brings files that are stored in SharePoint Online document libraries to your Windows File Explorer.&#x20;

KONNEKT works **online**. It does not sync files to your local disk and waste space there. That is why KONNEKT does a great job in **VDI** environments like **Citrix** or **Azure Virtual Desktop** (AVD - fka Windows Virtual Desktop WVD).

![](.gitbook/assets/konnekt-explorer-menu.webp)

The **main differences** between **OneDrive Sync Client** and **KONNEKT** are:

| Feature                                                           |                     OneDrive Sync Client                     |                                                                                  KONNEKT                                                                                  |
| ----------------------------------------------------------------- | :----------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Are the files **synced** to the local machine?                    |             <p>Yes</p><p>(at least partially)</p>            |                                                                                     No                                                                                    |
| Automatically map the SharePoint volumes, the user has access to  | <p>No</p><p>(Users mark libraries to be synced manually)</p> |                                                               [Yes](configuration/mappings/auto-mapping.md)                                                               |
| **Drive-Letter** support                                          |                              No                              |                                                           [Yes](configuration/mappings/assign-drive-letters.md)                                                           |
| Can Administrators define which volumes and drive-letters to map? |                              No                              | <p>Yes</p><p>(<a href="configuration/mappings/auto-mapping.md">Auto-Mapping</a> and <a href="configuration/mappings/administrative-mappings.md">Managed Mappings</a>)</p> |
| Works in **VDI** environments (e.g. Citrix or AVD/WVD)            |                            limited                           |                                                                                    Yes                                                                                    |
| Support for **UNC** addressing                                    |                              No                              |                                                                                    Yes                                                                                    |

You have the option to use KONNEKT side-by-side with Microsoft 365 or stand-alone by replacing the OneDrive client. But in every configuration KONNEKT is a helpful leap to the Office 365 ecosytem (Office, Outlook, SharePoint,...) by providing not only the documents and data but also the right options to jump directly to the Sharepoint Online Site, providing the links to share or make the versions of a file accessible.

## Architecture

KONNEKT is a client-side tool - there is no backend. **Data is transferred directly between the KONNEKT client and the SharePoint Online services**. Thus, the data neither run over external systems, nor are they stored on the publisher systems. KONNEKT uses the **native Microsoft APIs** (Microsoft SharePoint and Microsoft Graph) with standard Microsoft authentication to access Microsoft 365. This means that **conditional access** is also effective for access from KONNEKT to SharePoint Online.

## Features

| Features                                | Explanation                                                                                                                     |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Drive Letter Mapping and Network Shares | Uses a deeply integrated network provider technology. A sophisticated implementation allows UNC paths and drive letter mapping. |
| Explorer Integrated                     | Integrates into the Windows File Explorer structure.                                                                            |
| Citrix and Terminal Services Support    | Transparent access to any SharePoint from Citrix and Terminal Services                                                          |
| Multitenancy                            | Connects to multiple tenants simultaneously                                                                                     |
| Co-authoring                            | Supports the co-authoring of Microsoft Office 365                                                                               |

These docs cover the technical aspects of KONNEKT. All other information can be found on [https://konnekt.io/](https://konnekt.io)

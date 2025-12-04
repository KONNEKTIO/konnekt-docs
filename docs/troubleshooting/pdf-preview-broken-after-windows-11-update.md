# PDF preview broken after Windows 11 update

## Situation

After installing the October 2025 cumulative update ([KB5066835](https://support.microsoft.com/en-us/topic/october-14-2025-kb5066835-os-builds-26200-6899-and-26100-6899-1db237d8-9f3b-4218-9515-3e0a32729685)), many users noticed that PDF files no longer render in File Explorer’s preview pane. Instead, a warning appears:

> "The file you are attempting to preview could harm your computer. If you trust the file and the source you received it from, open it to view its contents."

This behavior is **intentional** in 25H2. Windows now enforces stricter handling of files tagged with **Mark of the Web (MOTW) -** a security label applied to files downloaded from the internet or network shares. The preview pane refuses to render such files unless they are explicitly trusted.

## Solution

Users can add the UNC path of their KONNEKT to the list of trusted sites:

```
\\OneDrive-<TenantDefaultName>
```

<figure><img src="../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Registry Path**:

```
Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains\onedrive-<TenantDefaultName>
```

Add an entry named "file" as a REG\_DWORD and set its value to 2.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Recommendation

It is generally recommended to set this entry via an Intune policy or GPO; either per user or per device.

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>


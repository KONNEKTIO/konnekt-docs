# Slow performance or errors caused by antivirus scanning

## Problem

After deploying KONNEKT, users experience one or more of the following symptoms on mapped drives:

* Browsing folders is noticeably slow or times out
* Opening files takes much longer than expected
* File uploads fail intermittently (errors appear under **Errors** in the KONNEKT Explorer window)
* The KONNEKT tray icon briefly turns red during normal usage

These symptoms are often **intermittent,** they appear during certain times of the day (typically mornings) and resolve on their own after some time.

## Background

KONNEKT works online. Every file read on a KONNEKT mapped drive results in a request to SharePoint Online via the Microsoft Graph API. Microsoft applies **throttling limits** to these requests. When the limit is exceeded, SharePoint Online responds with HTTP 429 (Too Many Requests) and KONNEKT must wait before retrying.

Real-time antivirus (AV) scanning is one of the most common causes of unexpected throttling. When AV software scans a KONNEKT drive letter, it reads every file it encounters. Each file read consumes API capacity (called **Resource Units**). A single AV sweep of a library with 5,000 files can consume significant API capacity in a very short time, leaving little room for actual user activity.

This affects all real-time AV products, including:

* Microsoft Defender for Endpoint
* CrowdStrike Falcon
* SentinelOne
* Sophos
* Other endpoint protection platforms

> **Note:** This is not a bug in KONNEKT or in your AV software. It is expected behavior when real-time scanning is applied to an online-only drive. The solution is to exclude KONNEKT paths from real-time scanning.

## Solution

Add exclusions for KONNEKT drive letters and processes in your AV product. The exact steps depend on your AV solution and management method.

### Microsoft Defender via Intune (recommended)

If **Tamper Protection** is managed via Intune, you must configure exclusions through Intune Endpoint Security policy. PowerShell commands will not work when Tamper Protection is enabled.

1. Open the **Microsoft Intune admin center**
2. Navigate to **Endpoint security** > **Antivirus**
3. Create or edit a **Microsoft Defender Antivirus** policy
4. Under **Configuration settings**, add the following:

**Path exclusions:** add each KONNEKT drive letter your organization uses, e.g.:

```
M:\
S:\
K:\
```

**Process exclusions:**

```
C:\Program Files\Konnekt\Konnekt.exe
C:\Program Files\Konnekt\KonnektStarter.exe
```

5. Assign the policy to the appropriate device or user groups
6. Allow time for the policy to sync to endpoints

### Microsoft Defender via PowerShell (fallback)

If Tamper Protection is **not** managed via Intune, you can use PowerShell:

```powershell
Add-MpPreference -ExclusionPath "M:\"
Add-MpPreference -ExclusionPath "S:\"
Add-MpPreference -ExclusionProcess "C:\Program Files\Konnekt\Konnekt.exe"
Add-MpPreference -ExclusionProcess "C:\Program Files\Konnekt\KonnektStarter.exe"
```

> **Important:** Replace `M:\` and `S:\` with the actual drive letters used in your KONNEKT deployment. If you use auto-mapping, consider which drive letters are assigned to your users.

### Microsoft Defender - Attack Surface Reduction (ASR) rules

If you use ASR rules, also see "[Risky action blocked](risky-action-blocked.md)" for additional KONNEKT exclusions required for ASR.

### CrowdStrike Falcon

1. Open the **Falcon console**
2. Navigate to **Endpoint security** > **Prevention policies**
3. Under **Machine Learning** and / or **Sensor Visibility Exclusions**, add:

**Directory exclusions:** Your KONNEKT drive letters (e.g. `M:\`, `S:\`)

**Process exclusions:** `Konnekt.exe`, `KonnektStarter.exe`

### SentinelOne

1. Open the **SentinelOne Management Console**
2. Navigate to **Sentinels** > **Exclusions**
3. Add **Path Exclusions** for your KONNEKT drive letters
4. Add **Process Path** exclusions for:

```
C:\Program Files\Konnekt\Konnekt.exe
C:\Program Files\Konnekt\KonnektStarter.exe
```

### Other AV products

For any other AV product, configure the following exclusions in your endpoint protection management console:

| Exclusion type   | Value                                         |
| ---------------- | --------------------------------------------- |
| Path / Directory | Each KONNEKT drive letter, e.g. `M:\`, `S:\`  |
| Process          | `C:\Program Files\Konnekt\Konnekt.exe`        |
| Process          | `C:\Program Files\Konnekt\KonnektStarter.exe` |

## How to verify the issue

If you are unsure whether AV scanning is causing the problem, you can check using the following steps:

1. Open the KONNEKT **Preferences** (right-click the KONNEKT tray icon)
2. Set **Log-Level** to **Debug** (see also Debug log preparation)
3. Reproduce the slow behavior
4. In the debug log, look for repeated entries indicating throttling (HTTP 429 responses or retry messages) during periods when no user is actively working with files

If you see throttling entries occurring at regular intervals or during times when AV scheduled scans are configured, this strongly indicates AV scanning as the cause.

## Recommendation

We recommend configuring AV exclusions for KONNEKT drive letters and processes **before** deploying KONNEKT to end users. This prevents throttling incidents from occurring during rollout and avoids user-facing errors that may generate unnecessary support tickets.

It is generally recommended to deploy these exclusions via **Intune policy** or **GPO** to ensure they are applied consistently across all devices.

See also: [Offline attribute](../configuration/system-settings/offline-attribute.md), KONNEKT's built-in mechanism to reduce bandwidth usage from previews and indexing.

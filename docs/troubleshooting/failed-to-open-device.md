# Failed to open Device

## Problem

#### Issue with ARM-based Systems and KONNEKT Installation

If you notice the tray icon turning red and see log entries like the following, it indicates the issue:

<pre><code><strong>[error][Core_DriverControl] Failed to open Device "\.\konnektDevice"
</strong></code></pre>

The problem occurs on some devices that operate on ARM processors. When KONNEKT's x64 version is installed or deployed on such a system, the installation may succeed. However, KONNEKT will not work as expected.&#x20;

## Solution

Install KONNEKT's ARM64 version.

{% embed url="https://trial.konnekt.io/" %}

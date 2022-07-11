# Intune system settings

## Cache

**Name:** Konnekt-Cache

**OMA-URI**

User context:

```
./User/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~SystemSettings/Cache
```

Device context:

```
./Device/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~SystemSettings/Cache
```

**Data type:** String

**Value**&#x20;

```
<enabled/>
<data id="CacheTTL" value="60"/>
<data id="CacheSize" value="1000"/>
```

**Note**

For more information about the policy and setting the value, see [Cache settings](../../system-settings/cache-setting.md)

## Co-Authoring

**Name:** Konnekt-Co-Authoring

**OMA-URI**

User context:

```
./User/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~SystemSettings/CoAuthoring
```

Device context:

```
./Device/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~SystemSettings/CoAuthoring
```

**Data type:** String

**Value options**

```
<enabled/>
```

```
<disabled/
```

**Note**

For more information about the policy, see [Office365 Co-Authoring](../../system-settings/office365-co-authoring.md)

## Offline attribute

**Name:** Konnekt-Offline-Attribute

**OMA-URI**

User context:

```
./User/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~SystemSettings/OfflineAttribute
```

Device context:

```
./Device/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~SystemSettings/OfflineAttribute
```

**Data type:** String

**Value options**

```
<enabled/>
```

```
<disabled/>
```

**Note**

For more information about the policy, see [Offline attribute](../../system-settings/offline-attribute.md)

## Offline attribute filter

**Name:** Konnekt-Offline-Attribute-Filter

**OMA-URI**

User context:

```
./User/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~SystemSettings/OfflineAttributeFilter
```

Device context:

```
./Device/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~SystemSettings/OfflineAttributeFilter
```

**Data type:** String

**Value**&#x20;

```
<enabled/>
<data id="OfflineAttributeFilter" value="your list of extensions, see Note"/>
```

**Note**

For more information about the policy and setting the value, see [Offline attribute filter](../../system-settings/offline-attribute.md#exclude-dedicated-file-types-from-offline-attribute-filter)

## Link scope

**Name:** Konnekt-Link-Scope

**OMA-URI**

User context:

```
./User/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~SystemSettings/SharePointLinkScope
```

Device context:

```
./Device/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~SystemSettings/SharePointLinkScope
```

**Data type:** String

**Value**&#x20;

```
<enabled/>
<data id="SharepointLinkScopeSelect" value="see Note"/>
```

**Note**

For more information about the policy and setting the value, see [Link scope](../../system-settings/link-scope.md)

## Log level

{% hint style="info" %}
Available for KONNEKT 2.1 or newer
{% endhint %}

**Name:** Konnekt-Log-Level

**OMA-URI**

User context:

```
./User/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~SystemSettings/LogLevel
```

Device context:

```
./Device/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~SystemSettings/LogLevel
```

**Data type:** String

**Value**&#x20;

```
<enabled/>
<data id="LogLevelSelect" value="see Note"/>
```

**Note**

For more information about the policy and setting the value, see [Log level](../../system-settings/logging.md)

## Update check

{% hint style="info" %}
Available for KONNEKT 2.1 or newer
{% endhint %}

**Name:** Konnekt-Update-Check

**OMA-URI**

User context:

```
./User/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~SystemSettings/UpdateInterval
```

Device context:

```
./Device/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~SystemSettings/UpdateInterval
```

**Data type:** String

**Value options**

```
<enabled/>
<data value="120"/>
```

```
<disabled/>
```

**Note**

For more information about the policy, see [Update checker](../../system-settings/update-checker.md)

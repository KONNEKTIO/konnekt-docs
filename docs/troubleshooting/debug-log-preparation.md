# Debug log preparation

Our support team may ask you to provide debug logs to analyze issues. To do so, please follow these steps:

{% stepper %}
{% step %}
## **Set Log-Level to Debug:**

* Right-Click on the KONNEKT Tray Icon and choose "Preferences"

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

* Set Log-Level to "Debug":

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
## Restart the affected machine
{% endstep %}

{% step %}
## Try to reproduce the Issue

When trying to reproduce the problem, please note the use case you are trying. A description of the steps with details of the path, file name, and timestamp is very helpful when troubleshooting.
{% endstep %}

{% step %}
## Wait a moment and close KONNEKT

Wait up to a minute, then close KONNEKT via the Taskbar Tray icon.

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
## Collect the logs

{% hint style="info" %}
Since Windows version `10.0.26100.8737` and `10.0.22621.6931` crashguard.exe can't export KONNEKT's logs and Event Logs at the same time. We are working on a fix. In the meantime "run as administrator" is only needed to provide Event logs.
{% endhint %}

Run crashguard.exe and click "Send report":

"C:\Program Files\Konnekt\crashguard.exe"

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
In certain situations, a report cannot be sent due to company restrictions. In such cases, an email window may appear, or the new zipped folder will be saved on your Desktop.
{% endhint %}
{% endstep %}

{% step %}
## Send to us

After submitting the report, please send us a brief email (support@konnekt.io):

* Use case / what went wrong?
* Timestamp / when did it happen?
* Path / file name
{% endstep %}
{% endstepper %}

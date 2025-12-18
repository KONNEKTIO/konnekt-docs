# Office shows outdated versions

## Situation

When using Microsoft Office with KONNEKT on various platforms, the latest version may not appear in applications like Word.

A message may also be displayed:  "Recommended update: a newer version of this file is available on the server".

## Problem

Occasionally, Word, Excel, and PowerPoint may show a cached file version instead of the most recent version from SharePoint Online (SPO).

## Solution

There are two methods to resolve these issues:

1. Manually clear the Office cache at `%localappdata%\Microsoft\Office\16.0\OfficeFileCache`.
2. Enable "Delete files from the Office Document Cache when they are closed" in an Office app per user.

<figure><img src="../.gitbook/assets/image (2).png" alt="Excel Options \ Save \ Cache Settings"><figcaption></figcaption></figure>

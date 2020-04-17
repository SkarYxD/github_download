# github_download
Download Github repositories with python


## CONFIG

```
author = 'SkarYxD'
repository = 'github_download'
branch = 'master'
output_dir = 'C:\/Users\/JkDev\/Desktop'
```

*Download the repository and unzip it to the set address.*

```
with zipfile.ZipFile(download_path, 'r') as zip_ref:
    zip_ref.extractall(output_dir)
```

*Delete Zip File*
```
os.remove(download_path)
```

### Created by JkDev🇦🇷 . All rights reserved

Contact me:
 * Telegram: https://t.me/MrPopos2

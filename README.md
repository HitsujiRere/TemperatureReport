# TemperatureReport

**raspberrypi**上で，ある高専のwebclassによる検温報告を自動で行うプログラムです

crontabなどで自動化するのも良いと思います．

WindowsやMacでも，調べたりすればできると思います．

## How To Use

.envファイルを開き，USER_ID，PASSWORD，MAIL_TO，MAIL_ADDRESS，MAIL_PASSWORDを入力します．
そして，main.pyを実行すると，検温報告が行われる思います．

MAIL_ADDRESS（パスワード : MAIL_PASSWORD）からMAIL_TOへ，検温報告を失敗した時にその旨を送信します．

> MAIL_ADDRESSがGoogleアカウントの場合，「安全性の低いアプリのアクセス」を許可する必要があります．
Googleアカウント「セキュリティ」の下部にて設定できます．
https://myaccount.google.com/security

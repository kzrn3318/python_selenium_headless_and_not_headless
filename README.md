# python_selenium_headless_and_not_headless
pythonのseleniumを用いてgoogleformの自動入力を作成しました。googleformの操作はpythonで、自動実行をdaemon化ではなくawsで行った。
googleformは組織内のみの閲覧に指定されていたので、具体的な内容は載せられないのですがchromeの構造は以下のようになっておりました。

###### version及びパッケージ
 + python 3.7
 + chrome 85.0.4183.102
 + chromedriver-binary 85の最新版
 + select
 + (aws ec2 ： amazon linux2)

###### 入力内容
 + その日の体温(整数部)        　   -> select tagを使わず、div tagとspan tagで作成された選択形式
 + その日の体温(書数点以下1桁)      -> select tagを使わず、div tagとspan tagで作成された選択形式
 + 前日との体調に差があるか         -> select tagを使わず、div tagとspan tagで作成された選択形式(idに指定あり)


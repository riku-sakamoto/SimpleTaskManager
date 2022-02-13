# Simple Task Manager

## 概要

AtCoderやLPICなどWeb上の各種問題を繰り返し解くためのとてもシンプルな管理ツール

## HOW TO USE

### 1. 問題の登録

`data/tasks.json`にて下記のように問題を登録。

- url: 問題のURL
- star: 重要度
- count: 解いた回数（最初は０にする。自動で更新される。）

```json
[
    {
        "url": "sample.url",
        "star": 1,
        "count": 0
    },
]
```

### 2. ブラウザの登録

`setting.yaml`にて起動するブラウザのパスを設定する（デフォルトはChrome）

```yaml
BROWSER_PATH: 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
```

### 3. 起動

以下のコマンドで起動する。各設問に回答することで問題を進める。なお，問題は'star - count'を降順に並べ替えた優先度で出題される。

```python
pipenv run python main.py
```

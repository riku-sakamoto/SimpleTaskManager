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

### 2. 起動

以下のコマンドで起動する。各設問に回答することで問題を進める。なお，問題は'star - count'を降順に並べ替えた優先度で出題され，デフォルトのブラウザによって対象のURLを自動で開く。

```python
pipenv run python main.py
```

以下のようにコマンドプロンプト上で対話的に実行する。

```
Number of tasks: 3
Problems : 1/3
https://atcoder.jp/contests/typical90/tasks/typical90_f, star: 2, count: 0
Solved? (y or n): n
Problems : 2/3
https://atcoder.jp/contests/typical90/tasks/typical90_g, star: 2, count: 0
Solved? (y or n): n
Problems : 3/3
https://atcoder.jp/contests/typical90/tasks/typical90_t, star: 2, count: 0
Solved? (y or n): n
Continue? (y or n): n
```

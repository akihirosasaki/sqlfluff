# sqlfluff
## 実行方法
- docker pull sqlfluff/sqlfluff:latest
- alias sqlfluff='docker run -it --rm -v $PWD:/sql sqlfluff/sqlfluff:<version_tag>'
- sqlfluff lint test.sql

## 要件
- 全て小文字
- 不必要な空行や小文字をいれない
- インデントはスペース二つ
- カンマは文頭
- エイリアスのAS句は省略しない
- JOINのOUTERは省略する(未対応)
- 2項演算子は前後にスペースを入れる
- 文字列はダブルクォートで、シングルクォートは使わない
- 単一行コメントは--のみ。#は非推奨(未対応)
- and,orは文頭に書く(未対応)

## 設計
- L001: 不必要なホワイトスペース
- L002: 1行の中にタブとスペースが混ざっている
- L003: インデントはスペース2つ
  - tab_space_size = 2
- L006: 2項演算子は前後にスペースを入れる
- L010: 予約語/関数は小文字
  - capitalisation_policy = lower
- L011: テーブルのエイリアスのAS句は省略しない
  - aliasing = explicit
- L012: 列のエイリアスのAS句は省略しない
  - aliasing = explicit
- L013: エイリアスのない列式。明示的なAS句を使用します。
- L016: 1行の行数制限
  - ignore_comment_lines = True
  - indent_unit = space
  - max_line_length = 120
  - tab_space_size = 2
- L017: 関数名の直後に括弧が付いていません。
- L018: WITH句の閉じ括弧はキーワードと揃える必要があります。
  - tab_space_size = 0
- L019: カンマは文頭
  - comma_style = leading
- L022: WITH句のあとに1行空行をあけているか
- L023: WITH句のasの後ろに空白が入っているか
- L027: selectに複数の参照テーブル/ビューがある場合は、参照を修飾する必要があります。
- L030: 関数名も大文字小文字を統一する
- L033: UNIONには、DISTINCTかALLをつけるべし
- L036: SELECT句の複数カラム指定は改行すべし
- L039: 不要な空白は除去しましょう
- L040: null, true, falseは小文字に揃えるべし
- L044: クエリは、不明な数の結果列を生成します。
- L048: 引用符「'」の前後に空白一文字必要
- L049: NULLとの比較では、「IS」または「ISNOT」を使用する必要があります。
- L050: ファイルは改行または空白で始めてはなりません。
- L055:  RIGHT JOINは使わない、LEFT JOINにする
- L064: 引用符で囲まれたリテラルの優先引用符の一貫した使用法。
  - preferred_quoted_literal_style = 'double_quotes'


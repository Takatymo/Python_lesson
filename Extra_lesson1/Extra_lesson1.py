# -*- coding: utf-8 -*-

import sys
import urllib.request, urllib.parse, urllib.error
import json

####
# 変数の型が文字列かどうかチェック
####
def is_str(data=None):
  if isinstance(data, str):
    return True
  else :
    return False

if __name__ == '__main__':
  ####
  # 初期値設定
  ####
  # APIアクセスキー
  keyid="7e1482b944601e2fa3d2916c80f30072"
  # エンドポイントURL
  url= "http://api.gnavi.co.jp/ver1/RestSearchAPI/"
  # 検索ワード（コマンドライン引数）
  freeword=sys.argv[1]
  ####
  # APIアクセス
  ####
  # URLに続けて入れるパラメータを組立
  query = [
    ( "format",    "json"    ),
    ( "keyid",     keyid     ),
    ( "freeword",     freeword     )
  ]
  # URL生成
  url += "?{0}".format( urllib.parse.urlencode( query ) )
  # API実行
  try :
    result = urllib.request.urlopen(url).read()
  except ValueError:
    print('APIアクセスに失敗しました。')
    sys.exit()

  ####
  # 取得した結果を解析
  ####
  result = result.decode()
  data = json.loads(result)

  # エラーの場合
  if "error" in data :
    if "message" in data :
      print ("{0}".format( data["message"] ))
    else :
      print ("データ取得に失敗しました。")
    sys.exit()

  # ヒット件数取得
  total_hit_count = None
  if "total_hit_count" in data :
    total_hit_count = int(data["total_hit_count"])

  # ヒット件数が0以下、または、ヒット件数がなかったら終了
  if total_hit_count is None or total_hit_count <= 0 :
    print ("指定した内容ではヒットしませんでした。")
    sys.exit()

  # レストランデータがなかったら終了
  if not "rest" in data :
    print ("レストランデータが見つからなかったため終了します。")
    sys.exit()

  # ヒット件数表示
  print ("{0}件ヒットしました。".format( total_hit_count ))
  print ("----")

  # 出力件数
  disp_count = 0

  # レストランデータ取得
  for rest in data["rest"] :
    line                 = []
    name                 = ""
    code_category_name_s = []
    # 店舗名
    if 'name' in rest and is_str( rest["name"] ) :
      name = "{0}".format( rest["name"] )
    line.append( name )
    # タブ区切りで出力
    print ("\t".join( line ))
    disp_count += 1

  # 出力件数を表示して終了
  print ("----")
  print ("{0}件出力しました。".format( disp_count ))
  sys.exit()
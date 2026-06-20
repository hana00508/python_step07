from models import MeshAsset, CharacterAsset
from utils import make_lod_name, is_valid_name

def main():
    # ① メッシュを何個か作る
    body = MeshAsset("body", 8500)
    hair = MeshAsset("hair", 3200)
    eye = MeshAsset("eye", 400)

    # ② キャラクターアセットにまとめる
    hero = CharacterAsset("hero", [body, hair, eye], 2048)

    #   - 合計ポリゴン数を表示する
    print(hero.total_poly())   # 12100

    #   - 重いメッシュ一覧を表示する（infoを使うときれい）
    for m in hero.heavy_meshes():
        m.info()   # chr_body_LOD0 | 8500poly | HEAVY

if __name__ == '__main__':
    main()
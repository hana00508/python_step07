# utils.py … 命名・検証ヘルパー


def make_lod_name(base, lod):
    return f"chr_{base}_LOD{lod}"


def is_valid_name(name):
    return name.startswith("chr_")

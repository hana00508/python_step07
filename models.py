class MeshAsset:
    def __init__(self, name, poly_count, lod=0):
        self.name = name
        self.poly_count = poly_count
        self.lod = lod

    def get_full_name(self):
        return f"chr_{self.name}_LOD{self.lod}"

    def is_heavy(self, limit=5000):
        return self.poly_count > limit

    def info(self):
        status = "HEAVY" if self.is_heavy() else "OK"
        print(f"{self.get_full_name()} | {self.poly_count}poly | {status}")

class CharacterAsset:
    def __init__(self, name, meshes, texture_res):
        self.name = name
        self.meshes = meshes
        self.texture_res = texture_res

    def total_poly(self):
        total = 0
        for mesh in self.meshes:
            total += mesh.poly_count
        return total

    def heavy_meshes(self):
        return [m for m in self.meshes if m.is_heavy()]
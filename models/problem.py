
class Problem():
    def __init__(self,
                 url: str,
                 star: int,
                 count: int = 0):
        self.url = url
        self.star = star
        self.count = count
    
    def __repr__(self):
        return f"{self.url}, star: {self.star}, count: {self.count}"

    @property
    def priority(self):
        return self.star - self.count

    def solve(self) -> int:
        self.count += 1
    
    def change_star(self, new_star: int) -> int:
        self.star = new_star

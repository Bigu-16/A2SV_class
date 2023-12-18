class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        path_dict = defaultdict(lambda : [])

        for path in paths:
            files = path.split(" ")
            directory = files[0]
        
            for file_ in files[1:]:
                name, content = file_.split("(")
                path_dict[content[:-1]].append(directory + "/" + name)

        return [path_dict[content] for content in path_dict if len(path_dict[content]) > 1]


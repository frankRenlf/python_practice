class Solution:
    def capitalizeTitle(self, title: str) -> str:
        subs = title.split(" ")
        for i, sub in enumerate(subs):
            if len(sub) > 2:
                subs[i] = sub[0].upper() + sub[1:].lower()
            else:
                subs[i] = sub.lower()
        return "".join(subs)

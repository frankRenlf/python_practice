# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/10/11 09:09 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:

    def topStudents_fast(self, positive_feedback, negative_feedback, report, student_id, k):
        words = {}
        for w in positive_feedback:
            words[w] = 3
        for w in negative_feedback:
            words[w] = -1
        A = []
        for s, i in zip(report, student_id):
            score = sum(words.get(w, 0) for w in s.split())
            A.append([-score, i])
        A.sort()
        return [i for v, i in A[:k]]

    def topStudents(self,
                    positive_feedback: List[str],
                    negative_feedback: List[str],
                    report: List[str],
                    student_id: List[int], k: int) -> List[int]:
        n = len(student_id)
        scores = list(map(list, zip(student_id, [0] * n)))
        for i, sentence in enumerate(report):
            for word in sentence.split():
                if word in positive_feedback:
                    scores[i][1] += 3
                elif word in negative_feedback:
                    scores[i][1] -= 1
        return [item[0] for item in sorted(scores, key=lambda x: (-x[1], x[0]))][:k]


if __name__ == "__main__":
    sol = Solution()
    print(sol.topStudents(positive_feedback=["smart", "brilliant", "studious"], negative_feedback=["not"],
                          report=["this student is not studious", "the student is smart"], student_id=[1, 2], k=2))

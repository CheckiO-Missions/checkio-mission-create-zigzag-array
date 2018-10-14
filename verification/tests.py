"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [3, 5],
            "answer": [[1,2,3,4,5],[10,9,8,7,6],[11,12,13,14,15]]
        },
        {
            "input": [5, 1],
            "answer": [
                    [1],
                    [2],
                    [3],
                    [4],
                    [5]
                ]
        },
        {
            "input": [3, 3, 5],
            "answer": [
                [5, 6, 7],
                [10, 9, 8],
                [11, 12, 13]
            ]
        }
    ],
    "Extra": [
        {
            "input": [0, 3],
            "answer": [],
            "explanation": "no rows no data"
        },
        {
            "input": [3, 0],
            "answer": [[], [], []],
            "explanation": "no cols but empty rows"
        },
        {
            "input": [0, 0],
            "answer": []
        },
        {
            "input": [10, 1],
            "answer": [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
        },
        {
            "input": [4, 2],
            "answer": [[1,2],[4,3],[5,6],[8,7]]
        }
    ]
}

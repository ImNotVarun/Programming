meanings = {
    "table": "a piece of furniture && list of facts and figures",
    "cat": "a small animal"
}

print(meanings["table"])
print(meanings["cat"])

# sets question

Subjects = {"python", "java", "c++", "python",
            "javascript", "java", "python", "java", "c++", "c"}
print("Number of classrooms required id :",
      len(Subjects.intersection(Subjects)))

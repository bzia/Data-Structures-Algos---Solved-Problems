def countMatches(items, ruleKey, ruleValue):
    # O(n) time, O(1) space
    matches = 0

    for i in range(len(items)):
        if ruleKey == "type" and ruleValue == items[i][0]:
            matches += 1
        elif ruleKey == "color" and ruleValue == items[i][1]:
            matches += 1
        elif ruleKey == "name" and ruleValue == items[i][2]:
            matches += 1
    return matches


print(countMatches([["phone", "blue", "pixel"], [
      "computer", "silver", "phone"], ["phone", "gold", "iphone"]], "type", "phone"))

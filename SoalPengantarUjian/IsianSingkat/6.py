#6.json.loads(json_string)[1][2]
import json
json_string = '[["a", "b", "c"], ["d", "e", "f"]]'
result_6 = json.loads(json_string)[1][2]
print(result_6)
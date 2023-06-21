from datetime import datetime, timezone
​
def build_response(data, limit, cursor_value):
    response = dict()
​
    response['insert'] = {"boards": []}  # If we had more endpoints we could add them here
    # and we would need to add them to the 'insert' section of the response below
    for row in data:
        response['insert']["boards"].append(row)
​
    response['state'] = {'cursor': cursor_value} if len(data) == 0 else {
        'cursor': datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")}
    response['schema'] = {"boards": {'primary_key': [
        "id"]}}  # If we had more endpoints, we would need to add the schemas / primary keys here as well
    response['hasMore'] = False if len(data) < limit else True
    return response
​
​
def lambda_handler(request, context):
    boards_data = {
        "boards": [{
            "id": 1,
            "value": "board 1"
        }, {
            "id": 2,
            "value": "board 2"
        }]
    };

    try:
        cursor_value = request['state']['cursor']
    except KeyError:
        cursor_value = '1970-01-01T00:00:00'
​
    limit = int(request['secrets']['limit'])
​
    if len(boards_data) == 0:
        return {}
​
    response = build_response(boards_data["boards"], limit, cursor_value)
​
    # print(response)
​
    return response
​
def printad():
    print("hosdifs");

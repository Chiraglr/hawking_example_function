from datetime import datetime, timezone
def build_response(data, limit, cursor_value):
    response = dict()

    response['insert'] = {"boards": []}  # If we had more endpoints we could add them here
    # and we would need to add them to the 'insert' section of the response below
    for row in data:
        response['insert']["boards"].append(row)

    response['state'] = {'cursor': cursor_value} if len(data) == 0 else {
        'cursor': datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")}
    response['schema'] = {"boards": {'primary_key': [
        "id"]}}  # If we had more endpoints, we would need to add the schemas / primary keys here as well
    response['hasMore'] = False if len(data) < limit else True
    return response


def lambda_handler(request, context):
    # Import credentials
    # These and other parameters should be wrapped up in 'request,' which is relayed from the connector's 'secrets'
    # api_key = request['secrets']['apiKey']

    # Get data
    # api_url = "https://api.monday.com/v2"
    # boards_query = '{ boards {id name state board_folder_id } }'
    # boards_data = get_request(boards_query, api_key=api_key, api_url=api_url)
    boards_data = {
        "boards": [{
            "id": 1,
            "value": "board 1"
        }, {
            "id": 2,
            "value": "board 2"
        }]
    };

    # Get json from request
    # request = requests.get(url=api_url, auth=api_key).json()
    # Note that get_json above is a flask function, which seems to work because google cloud functions are run
    # in a flask based environment, even though we didn't import it explicitly or add it to requirements.txt

    # Set state
    try:
        cursor_value = request['state']['cursor']
    except KeyError:
        cursor_value = '1970-01-01T00:00:00'

    # Set the 'limit' according to your estimates of the table's size and row count
    # Again, these can also be stored in 'request'
    limit = int(request['secrets']['limit'])

    if len(boards_data) == 0:
        return {}

    response = build_response(boards_data["boards"], limit, cursor_value)

    # print(response)

    return response

def printad():
    print("hosdifs");

import http.client


def download():
    connection = http.client.HTTPSConnection('www.deltaconnected.com')

    connection.request("GET", '/arcdps/x64/d3d11.dll')

    response = connection.getresponse()

    if response.status == 200:
        return response.read()

    print('Something done gone wrong')
    print(response.status, response.reason)
    return ''

import asyncio
import aiohttp
import xmltodict
import json

async def main():
    try:
        client = await create_client()

        # response = await get_method(client, 'https://jsonplaceholder.typicode.com/todos/1')
        # print(response.headers['Content-Type'])
        # print(response.status)
        # print(await response.json())

        response = await get_method_other_way(client, '''https://secure.shippingapis.com/ShippingAPI.dll?API=Verify&XML=
                <AddressValidateRequest USERID="382HEALT2233">
                <Revision>1</Revision>
                <Address ID="0">
                <Address1>1648 SW 148TH TER</Address1>
                <Address2></Address2>
                <City/>
                <State></State>
                <Zip5>33027</Zip5>
                <Zip4/>
                </Address>
                </AddressValidateRequest>''')

        # print(response.status)
        # res = await response.text()
        print(response)
        response = xmltodict.parse(response)
        json_data = json.dumps(response)
        print(json_data)
        # print(response.headers['Content-Type'])
        # print(response)
        # print(await response.text())
        client.close()
    except Exception as ex:
        print(ex)

async def other_main():
    try:
        async with aiohttp.ClientSession() as client:
            response = await get_method_other_way(client, '''https://secure.shippingapis.com/ShippingAPI.dll?API=Verify&XML=
                            <AddressValidateRequest USERID="382HEALT2233">
                            <Revision>1</Revision>
                            <Address ID="0">
                            <Address1>1648 SW 148TH TER</Address1>
                            <Address2></Address2>
                            <City/>
                            <State></State>
                            <Zip5>33027</Zip5>
                            <Zip4/>
                            </Address>
                            </AddressValidateRequest>''')

            # print(response.status)
            # res = await response.text()
            print(response)
            response = xmltodict.parse(response)
            json_data = json.dumps(response)
            print(json_data)
    except Exception as ex:
        print(ex)




async def get_method(client, url):
    return await client.get(url)


async def get_method_other_way(client, url):
    async with client.get(url) as resp:
        print('===== response =========')
        print(await resp.text())
        return await resp.text()

async def create_client():
    client = aiohttp.ClientSession()
    return client




loop = asyncio.get_event_loop()
# loop.run_until_complete(other_main())
loop.run_until_complete(main())
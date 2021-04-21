import logging
import asyncio
import boto3
import concurrent.futures

logging.warning('test')

def blocking_io():
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('hc-qa-lead-validation-worker-rules-engine-dynamodb-table')
    response = table.get_item(
        Key={'validation_id': 'validation_email'}
    )

    return response['Item']

async def main():
    loop = asyncio.get_running_loop()

    ## Options:

    # 1. Run in the default loop's executor:
    logging.info('start None')
    result = await loop.run_in_executor(
        None, blocking_io)
    print('default thread pool')
    logging.info(result)

    # 2. Run in a custom thread pool:
    logging.info('start Pool')
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, blocking_io)
        print('custom thread pool')
        logging.info(result)

    # 3. Run in a custom process pool:
    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, blocking_io)
        print('custom process pool', result)


asyncio.run(main())
from datetime import datetime
import time
import asyncio


async def drink_coffee():
    print('Start Drinking Coffee')
    await asyncio.sleep(3)
    print('End Drinking Coffee')
    return 'Coffee'


async def eat_breakfast():
    print('Start Eating Breakfast')
    await asyncio.sleep(5)
    print('End Eating Breakfast')
    return 'Breakfast'


async def main():
    start_time = datetime.now()
    # coffee = asyncio.create_task(drink_coffee())
    # breakfast = asyncio.create_task(eat_breakfast())
    #
    # await coffee
    # await breakfast
    #
    # print(coffee.result())
    # print(breakfast.result())


    coroutines = asyncio.gather(drink_coffee(), eat_breakfast())

    await coroutines

    # print(coroutines)

    coffee, breakfast = coroutines.result()

    print(coffee)
    print(breakfast)

    end_time = datetime.now()

    print(f'Estimated Time: {end_time - start_time}')


# name = __name__
#
# print(f'From Asynchronous.py: {name}')

if __name__ == '__main__':
    asyncio.run(main())

#################################################################################

import asyncio
import random
import time
from datetime import datetime


async def task(name, delay):
    print(f'{name} started, delay: {delay}')
    await asyncio.sleep(delay)
    # time.sleep(delay)
    print(f'{name} finished')
    return name


async def main():
    tasks = []

    for i in range(1, 11):
        task_name = f'Task {i}'
        delay = random.randint(1, 5)
        tasks.append(task(task_name, delay))

    print(tasks)
    print('Tasks scheduled...')
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    start_time = datetime.now()
    asyncio.run(main())
    end_time = datetime.now()

    print(f'Estimated Time: {end_time - start_time}')
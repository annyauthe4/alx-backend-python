<h1>Basic async/await</h1>
<br></br>
<ul>
  <li><code>async def</code>defines a coroutine (a special kind of function that can pause and resume).

  </li>
  <li><code>await</code>pauses the coroutine until the awaited task is finished.</li>
</ul>
Think of it like "waiting for a pizza" — you place the order and do something else until it's ready.

<code>
import asyncio

async def order_pizza():
    print("Ordering pizza...")
    await asyncio.sleep(2)  # pretend it takes 2 seconds
    print("Pizza is ready!")

async def main():
    await order_pizza()

asyncio.run(main())
</code>

Output:

Ordering pizza...
(wait 2 seconds)
Pizza is ready!

<h1>Running Multiple Tasks Concurrently</h1>
Imagine delivering pizzas to many customers at the same time instead of waiting for one, then the next, and so on.
<code>
import asyncio

async def task(name, seconds):
    print(f"Task {name} started")
    await asyncio.sleep(seconds)
    print(f"Task {name} finished after {seconds} seconds")

async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 3),
        task("C", 1)
    )

asyncio.run(main())
</code>

OUTPUT:
Task A started
Task B started
Task C started
(wait 1 second)
Task C finished after 1 seconds
(wait 1 more second)
Task A finished after 2 seconds
(wait 1 more second)
Task B finished after 3 seconds

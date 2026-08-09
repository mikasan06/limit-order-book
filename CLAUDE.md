# Limit Order Book — project context

## What this is
A limit order book and matching engine in Python. Built from scratch to
learn market microstructure, and as groundwork for a final-year dissertation
on multi-agent market simulation (the agents will need a matching engine to
trade in).

## How I want you to work with me — read this first
I am building this to LEARN, not to ship fast. Do NOT write implementations
for me.
- Explain concepts, review code I've written, and point me at the decision
  I need to make and the tradeoffs involved.
- When I'm stuck, give a hint or a question, not the finished code.
- If I ask "how do I do X", explain the approach and let me write it.
- Writing the logic myself — especially the matching engine — is the whole
  point. Handing me a working order book defeats it.
- Exception: boilerplate I've already understood (test scaffolding, project
  config) is fine to help with directly.

## Architecture — four layers, built in this order
1. Order — a data holder: side, price, quantity, id, arrival sequence. (current)
2. OrderBook — stores resting orders by price level; add, cancel by id,
   best bid / best ask. Enforces price-time priority.
3. Matching engine — decides whether an incoming order rests or crosses and
   trades; handles partial fills sweeping across levels. The core.
4. Simulation & analysis — synthetic order flow through the book; measure
   mid-price, spread, fill rates; chart with NumPy/pandas/matplotlib.

Build and test each layer before starting the next. The engine must be
correct and testable with no graphics before any display is added — keep the
engine and any display strictly separate.

## Conventions
- Python 3.x, standard library first.
- pytest; write tests alongside each piece, not at the end.
- Small, readable commits — one logical change each. Clean history matters
  (this is a portfolio repo).
- `side` represented as an enum, not a raw string.
- Prefer clarity over cleverness; this is code I need to explain in interviews.

## Design decisions (update as I make them)
- Order side: enum.
- Quantity mutability: [decide and record]
- Order ID generation: [decide and record — who assigns it, how uniqueness holds]
- Arrival-order / time priority: [decide and record]
- Price-level data structure: [decide when I reach the OrderBook layer]

## Open questions / not yet decided
- Which order types beyond limit and market (IOC, FOK) — later, not now.
- Real data replay (e.g. LOBSTER) vs synthetic flow — synthetic first.
I'm trying to get GPT agents to bargain by giving this kind of scenario: 

https://en.wikipedia.org/wiki/Myerson%E2%80%93Satterthwaite_theorem

where Alice and Bob are negotiating over a mug.
It needs some work, as they don't quite get the idea that valuing something at $20 means you'd take offers for more than $20. 

To run this yourself, you need to create a `.env` file that has your OpenAI API key e.g.,

```
OPENAI_API_KEY=XXXXXXXXXXXXXXXXXXXXX
```

This is what it looks like when you run it. Note that the bargain parsing doens't quite work either. 

```
>>> 
{'sale_price': None, 'offers': {'Alice': 'between $20 and $40', 'Bob': '$25', 'Alice': '$30'}}
{'sale_price': 28.5, 'offers': {'Alice': 30, 'Bob': 25, 'Alice': 28.5, 'Bob': 27.5}}
{'sale_price': 27.5, 'offers': {'Alice': 30, 'Bob': 25, 'Alice': 27.5}}

```
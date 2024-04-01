# Cerealized
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
Python pickle deserialization
```

<br>

## Requirements
- Data serialization
- Python's object-oriented features 
- Cookie manipulation

<br>

## Solve
Python saves (serializes) and loads (deserializes) data using its `pickle` module, which is [NOT SECURE](https://docs.python.org/3/library/pickle.html).

When a Python application utilizes the pickle module to serialize and deserialize objects, 
it essentially converts Python objects into a byte stream to save them to a file or transmit 
over a network and then reconstructs the object from the byte stream. 
While powerful for preserving state and facilitating object-oriented storage and transmission, 
this mechanism can be subverted if untrusted data is deserialized without proper sanitization.

<img src="./solve/pickle module.png" width="500">

The vulnerability arises from the application's handling of serialized data received via cookies. 
By crafting malicious serialized objects—pickle bombs—that include arbitrary code execution payloads, 
an attacker can trigger unintended actions within the application context, 
such as revealing sensitive information or executing commands on the server.

<br>

The server serializes each item that is added to it through the cookies.

Because it uses the exploitable method of data serialization, 
we can craft a special payload that, when loaded, executes arbitrary commands.

<br>

More info is available at the following sites:
- [**here**](https://docs.python.org/3/library/pickle.html)
- [**here as well**](https://frichetten.com/blog/escalating-deserialization-attacks-python/)
- [**or even here**](htttp://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Insecure%20Deserialization/Python.md).

<br>

Run the [solve.py](./solve/solve.py) script to create a payload that 
retrieves the `FLAG` environment variable from the server and 
makes a request that includes it in the `Cookie`.

<br>

> Flag: `CSCTF{3xeCUTE_c0mm@nds_w1th_dec3r32lized_PIckles}`
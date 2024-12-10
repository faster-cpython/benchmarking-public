# Results

- fork: python/f4b5588bde656d8ad048
- version: 3.13.0a1+
- config: 
- commit hash: [f4b5588](https://github.com/python/cpython/commit/f4b5588)
- commit date: 2023-11-02T16:38:08+00:00
- commit merge base: [0887b9ce8b5b4f9ecdef014b9329da78a46c9f42](https://github.com/python/cpython/commit/0887b9ce8b5b4f9ecdef014b9329da78a46c9f42)
- ref: f4b5588bde656d8ad048

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12171263939)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20231102-linux-x86_64-python-f4b5588bde656d8ad048-3.13.0a1%2B-f4b5588.json)

### vs. 3.10.4

- Geometric mean: 1.364x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, djangocms, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20231102-linux-x86_64-python-f4b5588bde656d8ad048-3.13.0a1%2B-f4b5588-vs-3.10.4.md)
- [📈time plot](bm-20231102-linux-x86_64-python-f4b5588bde656d8ad048-3.13.0a1%2B-f4b5588-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.020x faster (HPT: reliability of 99.93%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20231102-linux-x86_64-python-f4b5588bde656d8ad048-3.13.0a1%2B-f4b5588-vs-3.12.0.md)
- [📈time plot](bm-20231102-linux-x86_64-python-f4b5588bde656d8ad048-3.13.0a1%2B-f4b5588-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.046x slower (HPT: reliability of 99.99%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: djangocms, gevent_hub
- [📄table](bm-20231102-linux-x86_64-python-f4b5588bde656d8ad048-3.13.0a1%2B-f4b5588-vs-3.13.0.md)
- [📈time plot](bm-20231102-linux-x86_64-python-f4b5588bde656d8ad048-3.13.0a1%2B-f4b5588-vs-3.13.0.svg)


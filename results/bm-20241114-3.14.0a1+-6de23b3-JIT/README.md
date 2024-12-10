# Results

- fork: brandtbucher/6de23b358e9e3dd796a2
- version: 3.14.0a1+
- config: JIT
- commit hash: [6de23b3](https://github.com/brandtbucher/cpython/commit/6de23b3)
- commit date: 2024-11-14T08:35:17-08:00
- commit merge base: [09d6f5dc7824c74672add512619e978844ff8051](https://github.com/python/cpython/commit/09d6f5dc7824c74672add512619e978844ff8051)
- ref: 6de23b358e9e3dd796a2

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11846985972)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1%2B-6de23b3.json)

### vs. 3.10.4

- Geometric mean: 1.222x faster (HPT: reliability of 99.99%, 1.11x faster at 99th %ile)
- Memory usage: 1.39x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1%2B-6de23b3-vs-3.10.4.md)
- [📈time plot](bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1%2B-6de23b3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.044x slower (HPT: reliability of 95.43%, 1.00x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1%2B-6de23b3-vs-3.12.0.md)
- [📈time plot](bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1%2B-6de23b3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.119x slower (HPT: reliability of 96.91%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1%2B-6de23b3-vs-3.13.0.md)
- [📈time plot](bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1%2B-6de23b3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.111x slower (HPT: reliability of 99.80%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: 🔴 many_optionals, subparsers
- [🧠memory plot](bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1%2B-6de23b3-vs-base-mem.svg)
- [📄table](bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1%2B-6de23b3-vs-base.md)
- [📈time plot](bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1%2B-6de23b3-vs-base.svg)


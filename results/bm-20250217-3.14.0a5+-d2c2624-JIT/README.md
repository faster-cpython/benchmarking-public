# Results

- fork: brandtbucher/trace_generators
- version: 3.14.0a5+
- config: JIT
- commit hash: [d2c2624](https://github.com/brandtbucher/cpython/commit/d2c2624)
- commit date: 2025-02-17T21:16:33-08:00
- commit merge base: [05e89c34bd8389f87bd6c9462d5a06ef9e1a65ab](https://github.com/python/cpython/commit/05e89c34bd8389f87bd6c9462d5a06ef9e1a65ab)
- ref: trace_generators

## linux x86_64 (azure)

- [pystats raw](bm-20250217-azure-x86_64-brandtbucher-trace_generators-3.14.0a5%2B-d2c2624-pystats.json)
- [pystats table](bm-20250217-azure-x86_64-brandtbucher-trace_generators-3.14.0a5%2B-d2c2624-pystats.md)

### vs. base

- [pystats diff](bm-20250217-azure-x86_64-brandtbucher-trace_generators-3.14.0a5%2B-d2c2624-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13383766542)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5%2B-d2c2624.json)

### vs. 3.10.4

- Geometric mean: 1.435x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5%2B-d2c2624-vs-3.10.4.md)
- [📈time plot](bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5%2B-d2c2624-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.104x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5%2B-d2c2624-vs-3.12.0.md)
- [📈time plot](bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5%2B-d2c2624-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.035x faster (HPT: reliability of 99.76%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5%2B-d2c2624-vs-3.13.0.md)
- [📈time plot](bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5%2B-d2c2624-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.013x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5%2B-d2c2624-vs-base-mem.svg)
- [📄table](bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5%2B-d2c2624-vs-base.md)
- [📈time plot](bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5%2B-d2c2624-vs-base.svg)


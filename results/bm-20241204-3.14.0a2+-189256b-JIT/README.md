# Results

- fork: brandtbucher/justin_cold_16
- version: 3.14.0a2+
- config: JIT
- commit hash: [189256b](https://github.com/brandtbucher/cpython/commit/189256b)
- commit date: 2024-12-04T15:53:28-08:00
- commit merge base: [94b8f8b40943bf38cf5c454773a3fb8f4ff71e01](https://github.com/python/cpython/commit/94b8f8b40943bf38cf5c454773a3fb8f4ff71e01)
- ref: justin_cold_16

## linux x86_64 (azure)

- [pystats raw](bm-20241204-azure-x86_64-brandtbucher-justin_cold_16-3.14.0a2%2B-189256b-pystats.json)
- [pystats table](bm-20241204-azure-x86_64-brandtbucher-justin_cold_16-3.14.0a2%2B-189256b-pystats.md)

### vs. base

- [pystats diff](bm-20241204-azure-x86_64-brandtbucher-justin_cold_16-3.14.0a2%2B-189256b-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12170451784)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2%2B-189256b.json)

### vs. 3.10.4

- Geometric mean: 1.431x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2%2B-189256b-vs-3.10.4.md)
- [📈time plot](bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2%2B-189256b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.102x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2%2B-189256b-vs-3.12.0.md)
- [📈time plot](bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2%2B-189256b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x faster (HPT: reliability of 97.80%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2%2B-189256b-vs-3.13.0.md)
- [📈time plot](bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2%2B-189256b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x slower (HPT: reliability of 99.90%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 mypy2
- [🧠memory plot](bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2%2B-189256b-vs-base-mem.svg)
- [📄table](bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2%2B-189256b-vs-base.md)
- [📈time plot](bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2%2B-189256b-vs-base.svg)


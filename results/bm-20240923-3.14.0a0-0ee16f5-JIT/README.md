# Results

- fork: savannahostrowski/jit_inv_cold_100
- version: 3.14.0a0
- config: JIT
- commit hash: [0ee16f5](https://github.com/savannahostrowski/cpython/commit/0ee16f5)
- commit date: 2024-09-23T10:25:22-07:00
- commit merge base: [33eeccf6d4f16e483b4c8a180bad718545aeaeaf](https://github.com/python/cpython/commit/33eeccf6d4f16e483b4c8a180bad718545aeaeaf)
- ref: jit_inv_cold_100

## linux x86_64 (azure)

- [pystats raw](bm-20240923-azure-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5-pystats.json)
- [pystats table](bm-20240923-azure-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5-pystats.md)

### vs. base

- [pystats diff](bm-20240923-azure-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10999327046)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5.json)

### vs. 3.10.4

- Geometric mean: 1.384x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5-vs-3.10.4.md)
- [📈time plot](bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.057x faster (HPT: reliability of 99.88%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5-vs-3.12.0.md)
- [📈time plot](bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.001x faster (HPT: reliability of 92.88%, 1.00x slower at 99th %ile)
- Memory usage: 0.94x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5-vs-3.13.0.md)
- [📈time plot](bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.026x slower (HPT: reliability of 99.99%, 1.00x slower at 99th %ile)
- Memory usage: 0.96x
- [🧠memory plot](bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5-vs-base-mem.svg)
- [📄table](bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5-vs-base.md)
- [📈time plot](bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5-vs-base.svg)


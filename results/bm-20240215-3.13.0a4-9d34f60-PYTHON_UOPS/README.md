# Results

- fork: python/v3.13.0a4
- version: 3.13.0a4
- config: T2
- commit hash: [9d34f60](https://github.com/python/cpython/commit/9d34f60)
- commit date: 2024-02-15T14:38:42+01:00
- commit merge base: [b0e5c35ded6d4a16d7a021c10c99bac94250edd0](https://github.com/python/cpython/commit/b0e5c35ded6d4a16d7a021c10c99bac94250edd0)
- ref: v3.13.0a4

## linux x86_64 (azure)

- [pystats raw](bm-20240215-azure-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-pystats.json)
- [pystats table](bm-20240215-azure-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10796118896)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json)

### vs. 3.10.4

- Geometric mean: 1.335x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.10.4.md)
- [📈time plot](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.010x faster (HPT: reliability of 81.69%, 1.00x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.12.0.md)
- [📈time plot](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.035x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: connected_components, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.13.0.md)
- [📈time plot](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.019x slower (HPT: reliability of 87.78%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- new benchmarks: bpe_tokeniser, unpack_sequence
- [🧠memory plot](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-base-mem.svg)
- [📄table](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-base.md)
- [📈time plot](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-base.svg)


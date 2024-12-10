# Results

- fork: python/v3.13.0a5
- version: 3.13.0a5
- config: NOGIL
- commit hash: [076d169](https://github.com/python/cpython/commit/076d169)
- commit date: 2024-03-12T21:11:08+01:00
- commit merge base: [f6e7a6ce651b43c6e060608a4bb20685f39e9eaa](https://github.com/python/cpython/commit/f6e7a6ce651b43c6e060608a4bb20685f39e9eaa)
- ref: v3.13.0a5

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9038496952)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json)

### vs. 3.10.4

- Geometric mean: 1.079x slower (HPT: reliability of 99.98%, 1.01x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: dask, djangocms, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.md)
- [📈time plot](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.264x slower (HPT: reliability of 100.00%, 1.24x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.md)
- [📈time plot](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.318x slower (HPT: reliability of 100.00%, 1.30x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0.md)
- [📈time plot](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.306x slower (HPT: reliability of 100.00%, 1.30x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: 🔴 dask, djangocms
- [🧠memory plot](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-base-mem.svg)
- [📄table](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-base.md)
- [📈time plot](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-base.svg)


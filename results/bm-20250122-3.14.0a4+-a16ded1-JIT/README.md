# Results

- fork: python/a16ded10ad3952406280
- version: 3.14.0a4+
- config: JIT
- commit hash: [a16ded1](https://github.com/python/cpython/commit/a16ded1)
- commit date: 2025-01-22T12:47:03+00:00
- commit merge base: [a9f5edbf5fb141ad172978b25483342125184ed2](https://github.com/python/cpython/commit/a9f5edbf5fb141ad172978b25483342125184ed2)
- ref: a16ded10ad3952406280

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12915980087)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250122-arminc-aarch64-python-a16ded10ad3952406280-3.14.0a4%2B-a16ded1.json)

### vs. 3.10.4

- Geometric mean: 1.216x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250122-arminc-aarch64-python-a16ded10ad3952406280-3.14.0a4%2B-a16ded1-vs-3.10.4.md)
- [📈time plot](bm-20250122-arminc-aarch64-python-a16ded10ad3952406280-3.14.0a4%2B-a16ded1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.038x slower (HPT: reliability of 98.31%, 1.00x slower at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250122-arminc-aarch64-python-a16ded10ad3952406280-3.14.0a4%2B-a16ded1-vs-3.12.0.md)
- [📈time plot](bm-20250122-arminc-aarch64-python-a16ded10ad3952406280-3.14.0a4%2B-a16ded1-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x slower (HPT: reliability of 97.47%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250122-arminc-aarch64-python-a16ded10ad3952406280-3.14.0a4%2B-a16ded1-vs-3.13.0.md)
- [📈time plot](bm-20250122-arminc-aarch64-python-a16ded10ad3952406280-3.14.0a4%2B-a16ded1-vs-3.13.0.svg)


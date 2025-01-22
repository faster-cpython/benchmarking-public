# Results

- fork: diegorusso/fplt
- version: 3.14.0a4+
- config: JIT
- commit hash: [707b019](https://github.com/diegorusso/cpython/commit/707b019)
- commit date: 2025-01-22T12:48:58+00:00
- commit merge base: [a16ded10ad3952406280be5ab9ff86a476867b08](https://github.com/python/cpython/commit/a16ded10ad3952406280be5ab9ff86a476867b08)
- ref: fplt

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12915980087)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4%2B-707b019.json)

### vs. 3.10.4

- Geometric mean: 1.204x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4%2B-707b019-vs-3.10.4.md)
- [📈time plot](bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4%2B-707b019-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.047x slower (HPT: reliability of 99.79%, 1.00x slower at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4%2B-707b019-vs-3.12.0.md)
- [📈time plot](bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4%2B-707b019-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.042x slower (HPT: reliability of 99.54%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4%2B-707b019-vs-3.13.0.md)
- [📈time plot](bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4%2B-707b019-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x slower (HPT: reliability of 99.99%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4%2B-707b019-vs-base-mem.svg)
- [📄table](bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4%2B-707b019-vs-base.md)
- [📈time plot](bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4%2B-707b019-vs-base.svg)


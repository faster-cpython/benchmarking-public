# Results

- fork: python/4cd10762b06ec57252e3
- version: 3.14.0a1+
- config: JIT
- commit hash: [4cd1076](https://github.com/python/cpython/commit/4cd1076)
- commit date: 2024-11-18T11:11:23-08:00
- commit merge base: [933f21c3c92f758fb0615d6a4cca10249c686ae7](https://github.com/python/cpython/commit/933f21c3c92f758fb0615d6a4cca10249c686ae7)
- ref: 4cd10762b06ec57252e3

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11936426410)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241118-arminc-aarch64-python-4cd10762b06ec57252e3-3.14.0a1%2B-4cd1076.json)

### vs. 3.10.4

- Geometric mean: 1.216x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241118-arminc-aarch64-python-4cd10762b06ec57252e3-3.14.0a1%2B-4cd1076-vs-3.10.4.md)
- [📈time plot](bm-20241118-arminc-aarch64-python-4cd10762b06ec57252e3-3.14.0a1%2B-4cd1076-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.038x slower (HPT: reliability of 99.99%, 1.02x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241118-arminc-aarch64-python-4cd10762b06ec57252e3-3.14.0a1%2B-4cd1076-vs-3.12.0.md)
- [📈time plot](bm-20241118-arminc-aarch64-python-4cd10762b06ec57252e3-3.14.0a1%2B-4cd1076-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.049x slower (HPT: reliability of 99.96%, 1.01x slower at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20241118-arminc-aarch64-python-4cd10762b06ec57252e3-3.14.0a1%2B-4cd1076-vs-3.13.0.md)
- [📈time plot](bm-20241118-arminc-aarch64-python-4cd10762b06ec57252e3-3.14.0a1%2B-4cd1076-vs-3.13.0.svg)


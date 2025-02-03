# Results

- fork: python/cf4c4ecc26c7e3b89f2e
- version: 3.14.0a4+
- config: NOGIL
- commit hash: [cf4c4ec](https://github.com/python/cpython/commit/cf4c4ec)
- commit date: 2025-02-01T18:49:45+02:00
- commit merge base: [71ae93374defd192e5e88fe0912eff4f8e56f286](https://github.com/python/cpython/commit/71ae93374defd192e5e88fe0912eff4f8e56f286)
- ref: cf4c4ecc26c7e3b89f2e

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13093635868)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec.json)

### vs. 3.10.4

- Geometric mean: 1.109x faster (HPT: reliability of 99.95%, 1.02x faster at 99th %ile)
- Memory usage: 1.57x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence
- [📄table](bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.10.4.md)
- [📈time plot](bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.119x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence
- [📄table](bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.12.0.md)
- [📈time plot](bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.120x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.13.0.md)
- [📈time plot](bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.158x slower (HPT: reliability of 100.00%, 1.15x slower at 99th %ile)
- Memory usage: 1.20x
- [🧠memory plot](bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base-mem.svg)
- [📄table](bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base.md)
- [📈time plot](bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13093635868)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec.json)

### vs. 3.10.4

- Geometric mean: 1.262x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.50x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.10.4.md)
- [📈time plot](bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.019x slower (HPT: reliability of 99.86%, 1.01x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.12.0.md)
- [📈time plot](bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.082x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.13.0.md)
- [📈time plot](bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.121x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.19x
- [🧠memory plot](bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base-mem.svg)
- [📄table](bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base.md)
- [📈time plot](bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13093635868)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec.json)

### vs. 3.10.4

- Geometric mean: 1.204x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.53x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.10.4.md)
- [📈time plot](bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.058x slower (HPT: reliability of 99.92%, 1.03x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.12.0.md)
- [📈time plot](bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.049x slower (HPT: reliability of 99.83%, 1.00x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.13.0.md)
- [📈time plot](bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.115x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.20x
- [🧠memory plot](bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base-mem.svg)
- [📄table](bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base.md)
- [📈time plot](bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base.svg)


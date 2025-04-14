# Results

- fork: python/313b96eb8b8d0ad3bac5
- version: 3.14.0a4+
- config: 
- commit hash: [313b96e](https://github.com/python/cpython/commit/313b96e)
- commit date: 2025-01-16T11:17:03+01:00
- commit merge base: [d05140f9f77d7dfc753dd1e5ac3a5962aaa03eff](https://github.com/python/cpython/commit/d05140f9f77d7dfc753dd1e5ac3a5962aaa03eff)
- ref: 313b96eb8b8d0ad3bac5

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12811335920)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e.json)

### vs. 3.10.4

- Geometric mean: 1.238x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.10.4.md)
- [📈time plot](bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.023x slower (HPT: reliability of 96.04%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.12.0.md)
- [📈time plot](bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.018x slower (HPT: reliability of 96.22%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.13.0.md)
- [📈time plot](bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12811326822)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e.json)

### vs. 3.10.4

- Geometric mean: 1.308x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.10.4.md)
- [📈time plot](bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.014x faster (HPT: reliability of 77.72%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.12.0.md)
- [📈time plot](bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x faster (HPT: reliability of 99.36%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.13.0.md)
- [📈time plot](bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12811331877)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e.json)

### vs. 3.10.4

- Geometric mean: 1.310x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.10.4.md)
- [📈time plot](bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.048x faster (HPT: reliability of 93.13%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.12.0.md)
- [📈time plot](bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.051x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.13.0.md)
- [📈time plot](bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.13.0.svg)


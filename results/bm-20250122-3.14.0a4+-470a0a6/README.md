# Results

- fork: python/470a0a68ebbbb4254f1a
- version: 3.14.0a4+
- config: 
- commit hash: [470a0a6](https://github.com/python/cpython/commit/470a0a6)
- commit date: 2025-01-22T10:51:37+00:00
- commit merge base: [a65f802692bd04e1ad18e467d4ccb033b049c2a7](https://github.com/python/cpython/commit/a65f802692bd04e1ad18e467d4ccb033b049c2a7)
- ref: 470a0a68ebbbb4254f1a

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12908210573)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4%2B-470a0a6.json)

### vs. 3.10.4

- Geometric mean: 1.352x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4%2B-470a0a6-vs-3.10.4.md)
- [📈time plot](bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4%2B-470a0a6-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.050x faster (HPT: reliability of 99.95%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4%2B-470a0a6-vs-3.12.0.md)
- [📈time plot](bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4%2B-470a0a6-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.061x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4%2B-470a0a6-vs-3.13.0.md)
- [📈time plot](bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4%2B-470a0a6-vs-3.13.0.svg)


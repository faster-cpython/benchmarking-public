# Results

- fork: mdboom/specialize_compact_i
- version: 3.14.0a4+
- config: 
- commit hash: [1cbd7aa](https://github.com/mdboom/cpython/commit/1cbd7aa)
- commit date: 2025-02-03T11:51:48-05:00
- commit merge base: [5ff2fbc026b14eadd41b8c14d83bb1eb832292dd](https://github.com/python/cpython/commit/5ff2fbc026b14eadd41b8c14d83bb1eb832292dd)
- ref: specialize_compact_i

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13118576405)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4%2B-1cbd7aa.json)

### vs. 3.10.4

- Geometric mean: 1.367x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4%2B-1cbd7aa-vs-3.10.4.md)
- [📈time plot](bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4%2B-1cbd7aa-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.057x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4%2B-1cbd7aa-vs-3.12.0.md)
- [📈time plot](bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4%2B-1cbd7aa-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.070x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4%2B-1cbd7aa-vs-3.13.0.md)
- [📈time plot](bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4%2B-1cbd7aa-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 64.72%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4%2B-1cbd7aa-vs-base-mem.svg)
- [📄table](bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4%2B-1cbd7aa-vs-base.md)
- [📈time plot](bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4%2B-1cbd7aa-vs-base.svg)


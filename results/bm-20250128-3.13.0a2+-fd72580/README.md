# Results

- fork: mdboom/specialize_compact_i
- version: 3.13.0a2+
- config: 
- commit hash: [fd72580](https://github.com/mdboom/cpython/commit/fd72580)
- commit date: 2025-01-28T14:28:47-05:00
- commit merge base: [05a370abd6cdfe4b54be60b3b911f3a441026bb2](https://github.com/python/cpython/commit/05a370abd6cdfe4b54be60b3b911f3a441026bb2)
- ref: specialize_compact_i

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13018167663)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2%2B-fd72580.json)

### vs. 3.10.4

- Geometric mean: 1.356x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, djangocms, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2%2B-fd72580-vs-3.10.4.md)
- [📈time plot](bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2%2B-fd72580-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.015x faster (HPT: reliability of 99.58%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2%2B-fd72580-vs-3.12.0.md)
- [📈time plot](bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2%2B-fd72580-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.052x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: djangocms, gevent_hub
- [📄table](bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2%2B-fd72580-vs-3.13.0.md)
- [📈time plot](bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2%2B-fd72580-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 50.59%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2%2B-fd72580-vs-base-mem.svg)
- [📄table](bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2%2B-fd72580-vs-base.md)
- [📈time plot](bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2%2B-fd72580-vs-base.svg)


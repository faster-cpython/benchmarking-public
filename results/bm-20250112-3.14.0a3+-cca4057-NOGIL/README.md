# Results

- fork: kumaraditya303/per_thread_tasks
- version: 3.14.0a3+
- config: NOGIL
- commit hash: [cca4057](https://github.com/kumaraditya303/cpython/commit/cca4057)
- commit date: 2025-01-12T06:59:22+00:00
- commit merge base: [3a570c6d58bd5ad7d7c13b24dafccc2701081d9f](https://github.com/python/cpython/commit/3a570c6d58bd5ad7d7c13b24dafccc2701081d9f)
- ref: per_thread_tasks

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12753597094)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3%2B-cca4057.json)

### vs. 3.10.4

- Geometric mean: 1.136x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.50x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3%2B-cca4057-vs-3.10.4.md)
- [📈time plot](bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3%2B-cca4057-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.121x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3%2B-cca4057-vs-3.12.0.md)
- [📈time plot](bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3%2B-cca4057-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.172x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3%2B-cca4057-vs-3.13.0.md)
- [📈time plot](bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3%2B-cca4057-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 99.89%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3%2B-cca4057-vs-base-mem.svg)
- [📄table](bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3%2B-cca4057-vs-base.md)
- [📈time plot](bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3%2B-cca4057-vs-base.svg)


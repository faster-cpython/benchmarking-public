# Results

- fork: kumaraditya303/per_thread_cur_task
- version: 3.14.0a4+
- config: NOGIL
- commit hash: [ba92dfb](https://github.com/kumaraditya303/cpython/commit/ba92dfb)
- commit date: 2025-02-10T17:08:48+05:30
- commit merge base: [94cd2e0ddeff83dee3254ca356d9e4396927d075](https://github.com/python/cpython/commit/94cd2e0ddeff83dee3254ca356d9e4396927d075)
- ref: per_thread_cur_task

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13253393110)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4%2B-ba92dfb.json)

### vs. 3.10.4

- Geometric mean: 1.265x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.51x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4%2B-ba92dfb-vs-3.10.4.md)
- [📈time plot](bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4%2B-ba92dfb-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.016x slower (HPT: reliability of 99.79%, 1.01x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4%2B-ba92dfb-vs-3.12.0.md)
- [📈time plot](bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4%2B-ba92dfb-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.081x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4%2B-ba92dfb-vs-3.13.0.md)
- [📈time plot](bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4%2B-ba92dfb-vs-3.13.0.svg)


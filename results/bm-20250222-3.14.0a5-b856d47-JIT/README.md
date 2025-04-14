# Results

- fork: brandtbucher/hack_night
- version: 3.14.0a5
- config: JIT
- commit hash: [b856d47](https://github.com/brandtbucher/cpython/commit/b856d47)
- commit date: 2025-02-22T15:39:18-08:00
- commit merge base: [3ae91014827f41846432995472b08f89061b0c1c](https://github.com/python/cpython/commit/3ae91014827f41846432995472b08f89061b0c1c)
- ref: hack_night

## linux x86_64 (azure)

- [pystats raw](bm-20250222-azure-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47-pystats.json)
- [pystats table](bm-20250222-azure-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47-pystats.md)

### vs. base

- [pystats diff](bm-20250222-azure-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13477588677)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47.json)

### vs. 3.10.4

- Geometric mean: 1.442x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47-vs-3.10.4.md)
- [📈time plot](bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.107x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47-vs-3.12.0.md)
- [📈time plot](bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.040x faster (HPT: reliability of 99.85%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47-vs-3.13.0.md)
- [📈time plot](bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 66.15%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47-vs-base-mem.svg)
- [📄table](bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47-vs-base.md)
- [📈time plot](bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13502039810)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47.json)

### vs. 3.10.4

- Geometric mean: 1.332x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47-vs-3.10.4.md)
- [📈time plot](bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.033x faster (HPT: reliability of 99.14%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47-vs-3.12.0.md)
- [📈time plot](bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.046x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47-vs-3.13.0.md)
- [📈time plot](bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 60.59%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47-vs-base-mem.svg)
- [📄table](bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47-vs-base.md)
- [📈time plot](bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47-vs-base.svg)


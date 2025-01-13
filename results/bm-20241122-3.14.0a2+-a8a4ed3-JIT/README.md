# Results

- fork: brandtbucher/warmup_side_4096
- version: 3.14.0a2+
- config: JIT
- commit hash: [a8a4ed3](https://github.com/brandtbucher/cpython/commit/a8a4ed3)
- commit date: 2024-11-22T07:45:34-08:00
- commit merge base: [615abb99a4538520f380ab26a42f1506e08ffd09](https://github.com/python/cpython/commit/615abb99a4538520f380ab26a42f1506e08ffd09)
- ref: warmup_side_4096

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11975780307)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3.json)

### vs. 3.10.4

- Geometric mean: 1.219x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.10.4.md)
- [📈time plot](bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.044x slower (HPT: reliability of 99.84%, 1.00x slower at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.12.0.md)
- [📈time plot](bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.055x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.13.0.md)
- [📈time plot](bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.014x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-base-mem.svg)
- [📄table](bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-base.md)
- [📈time plot](bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241122-azure-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-pystats.json)
- [pystats table](bm-20241122-azure-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-pystats.md)

### vs. base

- [pystats diff](bm-20241122-azure-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11975780307)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3.json)

### vs. 3.10.4

- Geometric mean: 1.415x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.10.4.md)
- [📈time plot](bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.076x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.12.0.md)
- [📈time plot](bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.018x faster (HPT: reliability of 94.40%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.13.0.md)
- [📈time plot](bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 97.27%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-base-mem.svg)
- [📄table](bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-base.md)
- [📈time plot](bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11975780307)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3.json)

### vs. 3.10.4

- Geometric mean: 1.284x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.10.4.md)
- [📈time plot](bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.009x slower (HPT: reliability of 75.66%, 1.00x slower at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.12.0.md)
- [📈time plot](bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.003x slower (HPT: reliability of 67.29%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.13.0.md)
- [📈time plot](bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-base-mem.svg)
- [📄table](bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-base.md)
- [📈time plot](bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11975780307)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3.json)

### vs. 3.10.4

- Geometric mean: 1.229x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.10.4.md)
- [📈time plot](bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.038x faster (HPT: reliability of 97.77%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.12.0.md)
- [📈time plot](bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.018x faster (HPT: reliability of 95.94%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.13.0.md)
- [📈time plot](bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 64.66%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-base.md)
- [📈time plot](bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11975780307)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3.json)

### vs. 3.10.4

- Geometric mean: 1.054x faster (HPT: reliability of 80.63%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.10.4.md)
- [📈time plot](bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.062x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.12.0.md)
- [📈time plot](bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.044x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.13.0.md)
- [📈time plot](bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 99.76%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-base.md)
- [📈time plot](bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11975780307)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3.json)

### vs. 3.10.4

- Geometric mean: 1.234x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.10.4.md)
- [📈time plot](bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.035x faster (HPT: reliability of 99.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.12.0.md)
- [📈time plot](bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x faster (HPT: reliability of 99.95%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.13.0.md)
- [📈time plot](bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 99.78%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-base-mem.svg)
- [📄table](bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-base.md)
- [📈time plot](bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2%2B-a8a4ed3-vs-base.svg)


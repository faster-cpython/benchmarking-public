# Results

- fork: nascheme/pgo_benchmark_task
- version: 3.14.0a5+
- config: 
- commit hash: [8dd8862](https://github.com/nascheme/cpython/commit/8dd8862)
- commit date: 2025-02-28T10:31:26-08:00
- commit merge base: [9e474a98af4184615540467dea16da05f4d284d8](https://github.com/python/cpython/commit/9e474a98af4184615540467dea16da05f4d284d8)
- ref: pgo_benchmark_task

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13632571678)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862.json)

### vs. 3.10.4

- Geometric mean: 1.356x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.10.4.md)
- [📈time plot](bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.064x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.12.0.md)
- [📈time plot](bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.063x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.13.0.md)
- [📈time plot](bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.016x faster (HPT: reliability of 99.97%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-base-mem.svg)
- [📄table](bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-base.md)
- [📈time plot](bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13632571678)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862.json)

### vs. 3.10.4

- Geometric mean: 1.470x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.10.4.md)
- [📈time plot](bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.133x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.12.0.md)
- [📈time plot](bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.060x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.13.0.md)
- [📈time plot](bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.013x faster (HPT: reliability of 92.07%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- [🧠memory plot](bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-base-mem.svg)
- [📄table](bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-base.md)
- [📈time plot](bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13632571678)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862.json)

### vs. 3.10.4

- Geometric mean: 1.368x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.10.4.md)
- [📈time plot](bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.064x faster (HPT: reliability of 99.90%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.12.0.md)
- [📈time plot](bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.073x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.13.0.md)
- [📈time plot](bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.020x faster (HPT: reliability of 99.57%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-base-mem.svg)
- [📄table](bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-base.md)
- [📈time plot](bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13632571678)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862.json)

### vs. 3.10.4

- Geometric mean: 1.229x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.10.4.md)
- [📈time plot](bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.043x faster (HPT: reliability of 68.25%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.12.0.md)
- [📈time plot](bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.010x faster (HPT: reliability of 99.96%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.13.0.md)
- [📈time plot](bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.016x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-base.md)
- [📈time plot](bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13632571678)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862.json)

### vs. 3.10.4

- Geometric mean: 1.134x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.10.4.md)
- [📈time plot](bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.144x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.12.0.md)
- [📈time plot](bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.014x faster (HPT: reliability of 99.88%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.13.0.md)
- [📈time plot](bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.008x faster (HPT: reliability of 99.12%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-base.md)
- [📈time plot](bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13632571678)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862.json)

### vs. 3.10.4

- Geometric mean: 1.444x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.10.4.md)
- [📈time plot](bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.135x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.12.0.md)
- [📈time plot](bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.139x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.13.0.md)
- [📈time plot](bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.149x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 0.98x
- [🧠memory plot](bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-base-mem.svg)
- [📄table](bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-base.md)
- [📈time plot](bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5%2B-8dd8862-vs-base.svg)


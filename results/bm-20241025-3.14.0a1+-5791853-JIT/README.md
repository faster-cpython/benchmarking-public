# Results

- fork: brandtbucher/justin_no_externs
- version: 3.14.0a1+
- config: JIT
- commit hash: [5791853](https://github.com/brandtbucher/cpython/commit/5791853)
- commit date: 2024-10-25T11:14:20-07:00
- commit merge base: [34653bba644aa5481613f398153757d7357e39ea](https://github.com/python/cpython/commit/34653bba644aa5481613f398153757d7357e39ea)
- ref: justin_no_externs

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11526508734)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853.json)

### vs. 3.10.4

- Geometric mean: 1.160x faster (HPT: reliability of 99.98%, 1.03x faster at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.10.4.md)
- [📈time plot](bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.090x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, sphinx
- [📄table](bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.12.0.md)
- [📈time plot](bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.099x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- new benchmarks: dulwich_log
- [📄table](bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.13.0.md)
- [📈time plot](bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x slower (HPT: reliability of 76.80%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-base-mem.svg)
- [📄table](bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-base.md)
- [📈time plot](bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241025-azure-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-pystats.json)
- [pystats table](bm-20241025-azure-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-pystats.md)

### vs. base

- [pystats diff](bm-20241025-azure-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11526508734)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853.json)

### vs. 3.10.4

- Geometric mean: 1.362x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.10.4.md)
- [📈time plot](bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.038x faster (HPT: reliability of 99.42%, 1.00x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.12.0.md)
- [📈time plot](bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.017x slower (HPT: reliability of 99.51%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- [📄table](bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.13.0.md)
- [📈time plot](bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.020x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-base-mem.svg)
- [📄table](bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-base.md)
- [📈time plot](bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11526508734)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853.json)

### vs. 3.10.4

- Geometric mean: 1.263x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.10.4.md)
- [📈time plot](bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.023x slower (HPT: reliability of 90.40%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.12.0.md)
- [📈time plot](bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.021x slower (HPT: reliability of 84.81%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- [📄table](bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.13.0.md)
- [📈time plot](bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.010x slower (HPT: reliability of 97.40%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-base-mem.svg)
- [📄table](bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-base.md)
- [📈time plot](bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11526508734)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853.json)

### vs. 3.10.4

- Geometric mean: 1.180x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.10.4.md)
- [📈time plot](bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.003x slower (HPT: reliability of 59.14%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.12.0.md)
- [📈time plot](bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.023x slower (HPT: reliability of 99.98%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.13.0.md)
- [📈time plot](bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.018x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-base.md)
- [📈time plot](bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11526508734)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853.json)

### vs. 3.10.4

- Geometric mean: 1.154x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.10.4.md)
- [📈time plot](bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.166x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.12.0.md)
- [📈time plot](bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.045x faster (HPT: reliability of 84.76%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.13.0.md)
- [📈time plot](bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.021x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-base.md)
- [📈time plot](bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11526508734)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853.json)

### vs. 3.10.4

- Geometric mean: 1.224x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.42x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.10.4.md)
- [📈time plot](bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.025x faster (HPT: reliability of 86.08%, 1.00x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- [📄table](bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.12.0.md)
- [📈time plot](bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.027x faster (HPT: reliability of 98.25%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- [📄table](bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.13.0.md)
- [📈time plot](bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.008x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-base-mem.svg)
- [📄table](bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-base.md)
- [📈time plot](bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-5791853-vs-base.svg)


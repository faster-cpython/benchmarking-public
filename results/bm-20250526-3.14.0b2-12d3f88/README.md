# Results

- fork: python/v3.14.0b2
- version: 3.14.0b2
- config: 
- commit hash: [12d3f88](https://github.com/python/cpython/commit/12d3f88)
- commit date: 2025-05-26T16:26:47+03:00
- ref: v3.14.0b2

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15534738803)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88.json)

### vs. 3.10.4

- Geometric mean: 1.341x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.10.4.md)
- [📈time plot](bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.058x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.12.0.md)
- [📈time plot](bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.056x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.13.0.md)
- [📈time plot](bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15534738803)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88.json)

### vs. 3.10.4

- Geometric mean: 1.441x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.10.4.md)
- [📈time plot](bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.112x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.12.0.md)
- [📈time plot](bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.040x faster (HPT: reliability of 99.45%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.13.0.md)
- [📈time plot](bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.13.0.svg)

## linux x86_64 (linux_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15534738803)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250526-linux_clang-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88.json)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15534738803)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88.json)

### vs. 3.10.4

- Geometric mean: 1.353x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.10.4.md)
- [📈time plot](bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.052x faster (HPT: reliability of 99.93%, 1.01x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.12.0.md)
- [📈time plot](bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.061x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.13.0.md)
- [📈time plot](bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.13.0.svg)

## linux x86_64 (pythonperf2_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15534738803)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250526-pythonperf2_clang-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88.json)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15534738803)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88.json)

### vs. 3.10.4

- Geometric mean: 1.266x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.10.4.md)
- [📈time plot](bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.077x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.12.0.md)
- [📈time plot](bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.014x faster (HPT: reliability of 99.23%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.13.0.md)
- [📈time plot](bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.13.0.svg)

## windows amd64 (pythonperf1_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15534738803)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250526-pythonperf1_clang-amd64-python-v3.14.0b2-3.14.0b2-12d3f88.json)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15534738803)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88.json)

### vs. 3.10.4

- Geometric mean: 1.418x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.10.4.md)
- [📈time plot](bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.439x faster (HPT: reliability of 100.00%, 1.40x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.12.0.md)
- [📈time plot](bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.217x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.13.0.md)
- [📈time plot](bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.13.0.svg)

## windows amd64 (pythonperf1_win32_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15534738803)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250526-pythonperf1_win32_clang-amd64-python-v3.14.0b2-3.14.0b2-12d3f88.json)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15534738803)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88.json)

### vs. 3.10.4

- Geometric mean: 1.230x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.10.4.md)
- [📈time plot](bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.031x slower (HPT: reliability of 98.72%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.12.0.md)
- [📈time plot](bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x slower (HPT: reliability of 84.54%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.13.0.md)
- [📈time plot](bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88-vs-3.13.0.svg)

## darwin arm64 (darwin_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15534738803)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250526-darwin_clang-arm64-python-v3.14.0b2-3.14.0b2-12d3f88.json)


# Results

- fork: Fidget-Spinner/trace_function_entry
- version: 3.14.0a2+
- config: JIT
- commit hash: [fcc6f57](https://github.com/Fidget%2dSpinner/cpython/commit/fcc6f57)
- commit date: 2024-12-16T20:18:19+08:00
- commit merge base: [2de048ce79e621f5ae0574095b9600fe8595f607](https://github.com/python/cpython/commit/2de048ce79e621f5ae0574095b9600fe8595f607)
- ref: trace_function_entry

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12356877260)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241216-arminc-aarch64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57.json)

### vs. 3.10.4

- Geometric mean: 1.254x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241216-arminc-aarch64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.10.4.md)
- [📈time plot](bm-20241216-arminc-aarch64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.010x slower (HPT: reliability of 51.12%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241216-arminc-aarch64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.12.0.md)
- [📈time plot](bm-20241216-arminc-aarch64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.002x slower (HPT: reliability of 74.97%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log, mypy2
- [📄table](bm-20241216-arminc-aarch64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.13.0.md)
- [📈time plot](bm-20241216-arminc-aarch64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.014x faster (HPT: reliability of 99.85%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241216-arminc-aarch64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-base-mem.svg)
- [📄table](bm-20241216-arminc-aarch64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-base.md)
- [📈time plot](bm-20241216-arminc-aarch64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241216-azure-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-pystats.json)
- [pystats table](bm-20241216-azure-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12356877260)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241216-linux-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57.json)

### vs. 3.10.4

- Geometric mean: 1.449x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241216-linux-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.10.4.md)
- [📈time plot](bm-20241216-linux-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.114x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241216-linux-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.12.0.md)
- [📈time plot](bm-20241216-linux-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.048x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241216-linux-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.13.0.md)
- [📈time plot](bm-20241216-linux-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.008x faster (HPT: reliability of 99.82%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241216-linux-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-base-mem.svg)
- [📄table](bm-20241216-linux-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-base.md)
- [📈time plot](bm-20241216-linux-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12356877260)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241216-pythonperf2-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57.json)

### vs. 3.10.4

- Geometric mean: 1.307x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241216-pythonperf2-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.10.4.md)
- [📈time plot](bm-20241216-pythonperf2-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.016x faster (HPT: reliability of 78.62%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241216-pythonperf2-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.12.0.md)
- [📈time plot](bm-20241216-pythonperf2-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.031x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241216-pythonperf2-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.13.0.md)
- [📈time plot](bm-20241216-pythonperf2-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 53.23%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241216-pythonperf2-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-base-mem.svg)
- [📄table](bm-20241216-pythonperf2-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-base.md)
- [📈time plot](bm-20241216-pythonperf2-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12356877260)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241216-pythonperf1-amd64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57.json)

### vs. 3.10.4

- Geometric mean: 1.253x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241216-pythonperf1-amd64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.10.4.md)
- [📈time plot](bm-20241216-pythonperf1-amd64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.065x faster (HPT: reliability of 99.47%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241216-pythonperf1-amd64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.12.0.md)
- [📈time plot](bm-20241216-pythonperf1-amd64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x faster (HPT: reliability of 57.74%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241216-pythonperf1-amd64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.13.0.md)
- [📈time plot](bm-20241216-pythonperf1-amd64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.006x faster (HPT: reliability of 96.60%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241216-pythonperf1-amd64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-base.md)
- [📈time plot](bm-20241216-pythonperf1-amd64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12356877260)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241216-pythonperf1_win32-x86-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57.json)

### vs. 3.10.4

- Geometric mean: 1.104x faster (HPT: reliability of 99.91%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241216-pythonperf1_win32-x86-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.10.4.md)
- [📈time plot](bm-20241216-pythonperf1_win32-x86-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.114x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241216-pythonperf1_win32-x86-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.12.0.md)
- [📈time plot](bm-20241216-pythonperf1_win32-x86-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.010x slower (HPT: reliability of 99.99%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241216-pythonperf1_win32-x86-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.13.0.md)
- [📈time plot](bm-20241216-pythonperf1_win32-x86-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.032x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241216-pythonperf1_win32-x86-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-base.md)
- [📈time plot](bm-20241216-pythonperf1_win32-x86-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12356877260)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241216-darwin-arm64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57.json)

### vs. 3.10.4

- Geometric mean: 1.268x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, mypy2
- [📄table](bm-20241216-darwin-arm64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.10.4.md)
- [📈time plot](bm-20241216-darwin-arm64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.069x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241216-darwin-arm64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.12.0.md)
- [📈time plot](bm-20241216-darwin-arm64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.087x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241216-darwin-arm64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.13.0.md)
- [📈time plot](bm-20241216-darwin-arm64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.013x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241216-darwin-arm64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-base-mem.svg)
- [📄table](bm-20241216-darwin-arm64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-base.md)
- [📈time plot](bm-20241216-darwin-arm64-Fidget%252dSpinner-trace_function_entry-3.14.0a2%2B-fcc6f57-vs-base.svg)


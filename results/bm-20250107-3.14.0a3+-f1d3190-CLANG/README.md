# Results

- fork: Fidget-Spinner/tail_call
- version: 3.14.0a3+
- config: CLANG
- commit hash: [f1d3190](https://github.com/Fidget%2dSpinner/cpython/commit/f1d3190)
- commit date: 2025-01-07T07:37:13+08:00
- commit merge base: [2228e92da31ca7344a163498f848973a1b356597](https://github.com/python/cpython/commit/2228e92da31ca7344a163498f848973a1b356597)
- ref: tail_call

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12679934038)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250107-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190.json)

### vs. 3.10.4

- Geometric mean: 1.363x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.10.4.md)
- [📈time plot](bm-20250107-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.069x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.12.0.md)
- [📈time plot](bm-20250107-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.066x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250107-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.13.0.md)
- [📈time plot](bm-20250107-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.092x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250107-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-base-mem.svg)
- [📄table](bm-20250107-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-base.md)
- [📈time plot](bm-20250107-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12677798960)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250107-linux-x86_64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190.json)

### vs. 3.10.4

- Geometric mean: 1.499x faster (HPT: reliability of 100.00%, 1.36x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-linux-x86_64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.10.4.md)
- [📈time plot](bm-20250107-linux-x86_64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.154x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250107-linux-x86_64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.12.0.md)
- [📈time plot](bm-20250107-linux-x86_64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.080x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250107-linux-x86_64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.13.0.md)
- [📈time plot](bm-20250107-linux-x86_64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.074x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250107-linux-x86_64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-base-mem.svg)
- [📄table](bm-20250107-linux-x86_64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-base.md)
- [📈time plot](bm-20250107-linux-x86_64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12696190243)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250107-pythonperf1-amd64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190.json)

### vs. 3.10.4

- Geometric mean: 1.276x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-pythonperf1-amd64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.10.4.md)
- [📈time plot](bm-20250107-pythonperf1-amd64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.081x faster (HPT: reliability of 99.98%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250107-pythonperf1-amd64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.12.0.md)
- [📈time plot](bm-20250107-pythonperf1-amd64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.042x faster (HPT: reliability of 66.44%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250107-pythonperf1-amd64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.13.0.md)
- [📈time plot](bm-20250107-pythonperf1-amd64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.108x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250107-pythonperf1-amd64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-base.md)
- [📈time plot](bm-20250107-pythonperf1-amd64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12696193623)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250107-pythonperf1_win32-x86-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190.json)

### vs. 3.10.4

- Geometric mean: 1.064x faster (HPT: reliability of 97.06%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-pythonperf1_win32-x86-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.10.4.md)
- [📈time plot](bm-20250107-pythonperf1_win32-x86-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.072x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250107-pythonperf1_win32-x86-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.12.0.md)
- [📈time plot](bm-20250107-pythonperf1_win32-x86-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.043x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250107-pythonperf1_win32-x86-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.13.0.md)
- [📈time plot](bm-20250107-pythonperf1_win32-x86-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.144x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250107-pythonperf1_win32-x86-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-base.md)
- [📈time plot](bm-20250107-pythonperf1_win32-x86-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12677795342)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250107-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190.json)

### vs. 3.10.4

- Geometric mean: 1.395x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250107-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.10.4.md)
- [📈time plot](bm-20250107-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.179x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250107-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.12.0.md)
- [📈time plot](bm-20250107-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.186x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250107-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.13.0.md)
- [📈time plot](bm-20250107-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.147x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250107-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-base-mem.svg)
- [📄table](bm-20250107-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-base.md)
- [📈time plot](bm-20250107-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-f1d3190-vs-base.svg)


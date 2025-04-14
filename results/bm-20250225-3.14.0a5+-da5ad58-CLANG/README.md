# Results

- fork: Fidget-Spinner/disable_tailcall
- version: 3.14.0a5+
- config: CLANG
- commit hash: [da5ad58](https://github.com/Fidget%2dSpinner/cpython/commit/da5ad58)
- commit date: 2025-02-25T23:32:59+08:00
- commit merge base: [5ec4bf86b7f4455432aebace996ef390ae3e9302](https://github.com/python/cpython/commit/5ec4bf86b7f4455432aebace996ef390ae3e9302)
- ref: disable_tailcall

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13525064046)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250225-arminc-aarch64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58.json)

### vs. 3.10.4

- Geometric mean: 1.181x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.39x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250225-arminc-aarch64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.10.4.md)
- [📈time plot](bm-20250225-arminc-aarch64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.067x slower (HPT: reliability of 99.99%, 1.03x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250225-arminc-aarch64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.12.0.md)
- [📈time plot](bm-20250225-arminc-aarch64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.063x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250225-arminc-aarch64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.13.0.md)
- [📈time plot](bm-20250225-arminc-aarch64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.119x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250225-arminc-aarch64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-base-mem.svg)
- [📄table](bm-20250225-arminc-aarch64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-base.md)
- [📈time plot](bm-20250225-arminc-aarch64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13525064046)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250225-linux-x86_64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58.json)

### vs. 3.10.4

- Geometric mean: 1.310x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250225-linux-x86_64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.10.4.md)
- [📈time plot](bm-20250225-linux-x86_64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.008x faster (HPT: reliability of 73.67%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250225-linux-x86_64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.12.0.md)
- [📈time plot](bm-20250225-linux-x86_64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.051x slower (HPT: reliability of 99.99%, 1.02x slower at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250225-linux-x86_64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.13.0.md)
- [📈time plot](bm-20250225-linux-x86_64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.116x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250225-linux-x86_64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-base-mem.svg)
- [📄table](bm-20250225-linux-x86_64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-base.md)
- [📈time plot](bm-20250225-linux-x86_64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13525064046)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250225-pythonperf2-x86_64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58.json)

### vs. 3.10.4

- Geometric mean: 1.186x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250225-pythonperf2-x86_64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.10.4.md)
- [📈time plot](bm-20250225-pythonperf2-x86_64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.082x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250225-pythonperf2-x86_64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.12.0.md)
- [📈time plot](bm-20250225-pythonperf2-x86_64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.064x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250225-pythonperf2-x86_64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.13.0.md)
- [📈time plot](bm-20250225-pythonperf2-x86_64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.153x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250225-pythonperf2-x86_64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-base-mem.svg)
- [📄table](bm-20250225-pythonperf2-x86_64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-base.md)
- [📈time plot](bm-20250225-pythonperf2-x86_64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13525064046)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250225-pythonperf1-amd64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58.json)

### vs. 3.10.4

- Geometric mean: 1.234x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250225-pythonperf1-amd64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.10.4.md)
- [📈time plot](bm-20250225-pythonperf1-amd64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.046x faster (HPT: reliability of 82.29%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250225-pythonperf1-amd64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.12.0.md)
- [📈time plot](bm-20250225-pythonperf1-amd64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.012x faster (HPT: reliability of 98.95%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250225-pythonperf1-amd64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.13.0.md)
- [📈time plot](bm-20250225-pythonperf1-amd64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 97.94%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250225-pythonperf1-amd64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-base.md)
- [📈time plot](bm-20250225-pythonperf1-amd64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13525064046)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250225-pythonperf1_win32-x86-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58.json)

### vs. 3.10.4

- Geometric mean: 1.287x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250225-pythonperf1_win32-x86-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.10.4.md)
- [📈time plot](bm-20250225-pythonperf1_win32-x86-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.292x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250225-pythonperf1_win32-x86-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.12.0.md)
- [📈time plot](bm-20250225-pythonperf1_win32-x86-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.148x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250225-pythonperf1_win32-x86-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.13.0.md)
- [📈time plot](bm-20250225-pythonperf1_win32-x86-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 78.07%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250225-pythonperf1_win32-x86-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-base.md)
- [📈time plot](bm-20250225-pythonperf1_win32-x86-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13525064046)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250225-darwin-arm64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58.json)

### vs. 3.10.4

- Geometric mean: 1.308x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250225-darwin-arm64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.10.4.md)
- [📈time plot](bm-20250225-darwin-arm64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.030x faster (HPT: reliability of 77.55%, 1.00x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250225-darwin-arm64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.12.0.md)
- [📈time plot](bm-20250225-darwin-arm64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250225-darwin-arm64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.13.0.md)
- [📈time plot](bm-20250225-darwin-arm64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.106x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250225-darwin-arm64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-base-mem.svg)
- [📄table](bm-20250225-darwin-arm64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-base.md)
- [📈time plot](bm-20250225-darwin-arm64-Fidget%252dSpinner-disable_tailcall-3.14.0a5%2B-da5ad58-vs-base.svg)


# Results

- fork: Fidget-Spinner/clang_hot
- version: 3.14.0a5+
- config: CLANG
- commit hash: [37fb620](https://github.com/Fidget%2dSpinner/cpython/commit/37fb620)
- commit date: 2025-03-06T03:29:24+08:00
- commit merge base: [d7bb7c781771650a4edcdee9dfd1ab9c4083e9fd](https://github.com/python/cpython/commit/d7bb7c781771650a4edcdee9dfd1ab9c4083e9fd)
- ref: clang_hot

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13686850367)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250306-arminc-aarch64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620.json)

### vs. 3.10.4

- Geometric mean: 1.356x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250306-arminc-aarch64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.10.4.md)
- [📈time plot](bm-20250306-arminc-aarch64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.057x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250306-arminc-aarch64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.12.0.md)
- [📈time plot](bm-20250306-arminc-aarch64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.058x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250306-arminc-aarch64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.13.0.md)
- [📈time plot](bm-20250306-arminc-aarch64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13686850367)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250306-linux-x86_64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620.json)

### vs. 3.10.4

- Geometric mean: 1.496x faster (HPT: reliability of 100.00%, 1.35x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250306-linux-x86_64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.10.4.md)
- [📈time plot](bm-20250306-linux-x86_64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.148x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250306-linux-x86_64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.12.0.md)
- [📈time plot](bm-20250306-linux-x86_64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.077x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250306-linux-x86_64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.13.0.md)
- [📈time plot](bm-20250306-linux-x86_64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13686850367)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250306-pythonperf2-x86_64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620.json)

### vs. 3.10.4

- Geometric mean: 1.404x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250306-pythonperf2-x86_64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.10.4.md)
- [📈time plot](bm-20250306-pythonperf2-x86_64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.087x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250306-pythonperf2-x86_64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.12.0.md)
- [📈time plot](bm-20250306-pythonperf2-x86_64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.099x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250306-pythonperf2-x86_64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.13.0.md)
- [📈time plot](bm-20250306-pythonperf2-x86_64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13686850367)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250306-pythonperf1-amd64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620.json)

### vs. 3.10.4

- Geometric mean: 1.196x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250306-pythonperf1-amd64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.10.4.md)
- [📈time plot](bm-20250306-pythonperf1-amd64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.014x faster (HPT: reliability of 80.39%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250306-pythonperf1-amd64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.12.0.md)
- [📈time plot](bm-20250306-pythonperf1-amd64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.018x slower (HPT: reliability of 99.99%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250306-pythonperf1-amd64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.13.0.md)
- [📈time plot](bm-20250306-pythonperf1-amd64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13686850367)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250306-pythonperf1_win32-x86-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620.json)

### vs. 3.10.4

- Geometric mean: 1.206x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250306-pythonperf1_win32-x86-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.10.4.md)
- [📈time plot](bm-20250306-pythonperf1_win32-x86-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.212x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250306-pythonperf1_win32-x86-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.12.0.md)
- [📈time plot](bm-20250306-pythonperf1_win32-x86-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.077x faster (HPT: reliability of 93.04%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250306-pythonperf1_win32-x86-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.13.0.md)
- [📈time plot](bm-20250306-pythonperf1_win32-x86-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13686850367)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250306-darwin-arm64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620.json)

### vs. 3.10.4

- Geometric mean: 1.469x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250306-darwin-arm64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.10.4.md)
- [📈time plot](bm-20250306-darwin-arm64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.154x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250306-darwin-arm64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.12.0.md)
- [📈time plot](bm-20250306-darwin-arm64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.157x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250306-darwin-arm64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.13.0.md)
- [📈time plot](bm-20250306-darwin-arm64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.13.0.svg)


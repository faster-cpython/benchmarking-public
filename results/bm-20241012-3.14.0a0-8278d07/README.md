# Results

- fork: Fidget-Spinner/fix_unsafe_refcounti
- version: 3.14.0a0
- config: 
- commit hash: [8278d07](https://github.com/Fidget%2dSpinner/cpython/commit/8278d07)
- commit date: 2024-10-12T22:07:53+08:00
- commit merge base: [b3aa1b5fe260382788a2df416599325ad680a5ee](https://github.com/python/cpython/commit/b3aa1b5fe260382788a2df416599325ad680a5ee)
- ref: fix_unsafe_refcounti

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11318191947)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241012-arminc-aarch64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json)

### vs. 3.10.4

- Geometric mean: 1.330x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20241012-arminc-aarch64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.10.4.md)
- [📈time plot](bm-20241012-arminc-aarch64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.039x faster (HPT: reliability of 99.50%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20241012-arminc-aarch64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.12.0.md)
- [📈time plot](bm-20241012-arminc-aarch64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.90x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241012-arminc-aarch64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.13.0.md)
- [📈time plot](bm-20241012-arminc-aarch64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 98.45%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241012-arminc-aarch64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-base-mem.svg)
- [📄table](bm-20241012-arminc-aarch64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-base.md)
- [📈time plot](bm-20241012-arminc-aarch64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11318191947)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241012-linux-x86_64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json)

### vs. 3.10.4

- Geometric mean: 1.429x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241012-linux-x86_64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.10.4.md)
- [📈time plot](bm-20241012-linux-x86_64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.084x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241012-linux-x86_64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.12.0.md)
- [📈time plot](bm-20241012-linux-x86_64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.032x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241012-linux-x86_64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.13.0.md)
- [📈time plot](bm-20241012-linux-x86_64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 99.81%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241012-linux-x86_64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-base-mem.svg)
- [📄table](bm-20241012-linux-x86_64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-base.md)
- [📈time plot](bm-20241012-linux-x86_64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11318191947)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241012-pythonperf2-x86_64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json)

### vs. 3.10.4

- Geometric mean: 1.335x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241012-pythonperf2-x86_64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.10.4.md)
- [📈time plot](bm-20241012-pythonperf2-x86_64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.027x faster (HPT: reliability of 94.16%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241012-pythonperf2-x86_64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.12.0.md)
- [📈time plot](bm-20241012-pythonperf2-x86_64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241012-pythonperf2-x86_64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.13.0.md)
- [📈time plot](bm-20241012-pythonperf2-x86_64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 85.90%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241012-pythonperf2-x86_64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-base-mem.svg)
- [📄table](bm-20241012-pythonperf2-x86_64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-base.md)
- [📈time plot](bm-20241012-pythonperf2-x86_64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11318191947)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241012-pythonperf1-amd64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json)

### vs. 3.10.4

- Geometric mean: 1.167x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241012-pythonperf1-amd64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.10.4.md)
- [📈time plot](bm-20241012-pythonperf1-amd64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.018x slower (HPT: reliability of 99.80%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241012-pythonperf1-amd64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.12.0.md)
- [📈time plot](bm-20241012-pythonperf1-amd64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241012-pythonperf1-amd64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.13.0.md)
- [📈time plot](bm-20241012-pythonperf1-amd64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 94.84%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241012-pythonperf1-amd64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-base.md)
- [📈time plot](bm-20241012-pythonperf1-amd64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11318191947)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241012-pythonperf1_win32-x86-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json)

### vs. 3.10.4

- Geometric mean: 1.139x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241012-pythonperf1_win32-x86-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.10.4.md)
- [📈time plot](bm-20241012-pythonperf1_win32-x86-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.140x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241012-pythonperf1_win32-x86-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.12.0.md)
- [📈time plot](bm-20241012-pythonperf1_win32-x86-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.035x faster (HPT: reliability of 94.44%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241012-pythonperf1_win32-x86-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.13.0.md)
- [📈time plot](bm-20241012-pythonperf1_win32-x86-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 55.60%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241012-pythonperf1_win32-x86-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-base.md)
- [📈time plot](bm-20241012-pythonperf1_win32-x86-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11318191947)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241012-darwin-arm64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json)

### vs. 3.10.4

- Geometric mean: 1.295x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 0.68x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241012-darwin-arm64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.10.4.md)
- [📈time plot](bm-20241012-darwin-arm64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.079x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 0.67x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241012-darwin-arm64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.12.0.md)
- [📈time plot](bm-20241012-darwin-arm64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.086x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.55x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241012-darwin-arm64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.13.0.md)
- [📈time plot](bm-20241012-darwin-arm64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x slower (HPT: reliability of 96.46%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241012-darwin-arm64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-base-mem.svg)
- [📄table](bm-20241012-darwin-arm64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-base.md)
- [📈time plot](bm-20241012-darwin-arm64-Fidget%252dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07-vs-base.svg)


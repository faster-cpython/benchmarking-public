# Results

- fork: python/2e15a50851da66eb8227
- version: 3.15.0a0
- config: NOGIL
- commit hash: [2e15a50](https://github.com/python/cpython/commit/2e15a50)
- commit date: 2025-06-14T16:04:16+00:00
- commit merge base: [fc413ecb8f4bf1c59b29932695e3538548eb1a8a](https://github.com/python/cpython/commit/fc413ecb8f4bf1c59b29932695e3538548eb1a8a)
- ref: 2e15a50851da66eb8227

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15657347904)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250614-arminc-aarch64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json)

### vs. 3.10.4

- Geometric mean: 1.071x slower (HPT: reliability of 97.24%, 1.00x slower at 99th %ile)
- Memory usage: 1.71x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250614-arminc-aarch64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.md)
- [📈time plot](bm-20250614-arminc-aarch64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.259x slower (HPT: reliability of 100.00%, 1.24x slower at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250614-arminc-aarch64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.md)
- [📈time plot](bm-20250614-arminc-aarch64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.259x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250614-arminc-aarch64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.md)
- [📈time plot](bm-20250614-arminc-aarch64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.049x slower (HPT: reliability of 100.00%, 1.13x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: 🔴 djangocms
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20250614-arminc-aarch64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base-mem.svg)
- [📄table](bm-20250614-arminc-aarch64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.md)
- [📈time plot](bm-20250614-arminc-aarch64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15657347904)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json)

### vs. 3.10.4

- Geometric mean: 1.078x faster (HPT: reliability of 98.48%, 1.00x faster at 99th %ile)
- Memory usage: 1.59x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.md)
- [📈time plot](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.151x slower (HPT: reliability of 99.99%, 1.07x slower at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.md)
- [📈time plot](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.205x slower (HPT: reliability of 100.00%, 1.15x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.md)
- [📈time plot](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.057x slower (HPT: reliability of 100.00%, 1.09x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: 🔴 djangocms
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base-mem.svg)
- [📄table](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.md)
- [📈time plot](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15657347904)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250614-pythonperf2-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json)

### vs. 3.10.4

- Geometric mean: 1.016x faster (HPT: reliability of 89.83%, 1.00x faster at 99th %ile)
- Memory usage: 1.69x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250614-pythonperf2-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.md)
- [📈time plot](bm-20250614-pythonperf2-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.200x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250614-pythonperf2-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.md)
- [📈time plot](bm-20250614-pythonperf2-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.187x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250614-pythonperf2-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.md)
- [📈time plot](bm-20250614-pythonperf2-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250614-pythonperf2-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base-mem.svg)
- [📄table](bm-20250614-pythonperf2-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.md)
- [📈time plot](bm-20250614-pythonperf2-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15657347904)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json)

### vs. 3.10.4

- Geometric mean: 1.309x slower (HPT: reliability of 100.00%, 1.40x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.md)
- [📈time plot](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.403x slower (HPT: reliability of 100.00%, 1.54x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.md)
- [📈time plot](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.415x slower (HPT: reliability of 100.00%, 1.65x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.md)
- [📈time plot](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.138x slower (HPT: reliability of 100.00%, 1.18x slower at 99th %ile)
- Memory usage: unknown
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.md)
- [📈time plot](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15657347904)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json)

### vs. 3.10.4

- Geometric mean: 1.225x slower (HPT: reliability of 100.00%, 1.27x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.md)
- [📈time plot](bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.206x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.md)
- [📈time plot](bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.299x slower (HPT: reliability of 100.00%, 1.35x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.md)
- [📈time plot](bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.svg)

### vs. base

- [📄table](bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.md)
- [📈time plot](bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15657347904)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json)

### vs. 3.10.4

- Geometric mean: 1.160x faster (HPT: reliability of 99.39%, 1.00x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.md)
- [📈time plot](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.064x slower (HPT: reliability of 99.88%, 1.02x slower at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.md)
- [📈time plot](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.063x slower (HPT: reliability of 99.59%, 1.00x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.md)
- [📈time plot](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.014x faster (HPT: reliability of 99.75%, 1.00x slower at 99th %ile)
- Memory usage: 1.18x
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base-mem.svg)
- [📄table](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.md)
- [📈time plot](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.svg)


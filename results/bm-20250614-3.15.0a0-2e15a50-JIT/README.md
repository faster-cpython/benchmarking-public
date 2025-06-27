# Results

- fork: python/2e15a50851da66eb8227
- version: 3.15.0a0
- config: JIT
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

- Geometric mean: 1.038x slower (HPT: reliability of 97.14%, 1.00x faster at 99th %ile)
- Memory usage: 1.41x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250614-arminc-aarch64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.md)
- [📈time plot](bm-20250614-arminc-aarch64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.235x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250614-arminc-aarch64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.md)
- [📈time plot](bm-20250614-arminc-aarch64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.226x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250614-arminc-aarch64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.md)
- [📈time plot](bm-20250614-arminc-aarch64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.009x slower (HPT: reliability of 96.24%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: 🔴 djangocms
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20250614-arminc-aarch64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base-mem.svg)
- [📄table](bm-20250614-arminc-aarch64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.md)
- [📈time plot](bm-20250614-arminc-aarch64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15909436125)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json)

### vs. 3.10.4

- Geometric mean: 1.157x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.md)
- [📈time plot](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.043x slower (HPT: reliability of 70.13%, 1.00x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.md)
- [📈time plot](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.149x slower (HPT: reliability of 99.99%, 1.04x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.md)
- [📈time plot](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.014x faster (HPT: reliability of 89.92%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base-mem.svg)
- [📄table](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.md)
- [📈time plot](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15657347904)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250614-pythonperf2-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json)

### vs. 3.10.4

- Geometric mean: 1.126x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250614-pythonperf2-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.md)
- [📈time plot](bm-20250614-pythonperf2-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.127x slower (HPT: reliability of 99.82%, 1.02x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250614-pythonperf2-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.md)
- [📈time plot](bm-20250614-pythonperf2-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.104x slower (HPT: reliability of 99.88%, 1.02x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250614-pythonperf2-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.md)
- [📈time plot](bm-20250614-pythonperf2-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250614-pythonperf2-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base-mem.svg)
- [📄table](bm-20250614-pythonperf2-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.md)
- [📈time plot](bm-20250614-pythonperf2-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15909436125)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json)

### vs. 3.10.4

- Geometric mean: 1.159x slower (HPT: reliability of 99.93%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.md)
- [📈time plot](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.230x slower (HPT: reliability of 99.99%, 1.15x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.md)
- [📈time plot](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.276x slower (HPT: reliability of 100.00%, 1.16x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.md)
- [📈time plot](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.072x faster (HPT: reliability of 99.88%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.md)
- [📈time plot](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15657347904)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json)

### vs. 3.10.4

- Geometric mean: 1.057x slower (HPT: reliability of 62.39%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.md)
- [📈time plot](bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.024x faster (HPT: reliability of 99.32%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.md)
- [📈time plot](bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.132x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.md)
- [📈time plot](bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.svg)

### vs. base

- [📄table](bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.md)
- [📈time plot](bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15909436125)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json)

### vs. 3.10.4

- Geometric mean: 1.127x faster (HPT: reliability of 99.96%, 1.03x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.md)
- [📈time plot](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.098x slower (HPT: reliability of 99.77%, 1.01x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.md)
- [📈time plot](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.096x slower (HPT: reliability of 97.52%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.md)
- [📈time plot](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.019x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base-mem.svg)
- [📄table](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.md)
- [📈time plot](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-base.svg)


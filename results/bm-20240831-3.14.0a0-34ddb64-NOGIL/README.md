# Results

- fork: python/34ddb64d088dd7ccc321
- version: 3.14.0a0
- config: NOGIL
- commit hash: [34ddb64](https://github.com/python/cpython/commit/34ddb64)
- commit date: 2024-08-31T15:17:05-07:00
- commit merge base: [0cba289870d5cd41f24b2f63b9480e4593aa2330](https://github.com/python/cpython/commit/0cba289870d5cd41f24b2f63b9480e4593aa2330)
- ref: 34ddb64d088dd7ccc321

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10649186889)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json)

### vs. 3.10.4

- Geometric mean: 1.188x slower (HPT: reliability of 100.00%, 1.18x slower at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.md)
- [📈time plot](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.359x slower (HPT: reliability of 100.00%, 1.37x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.md)
- [📈time plot](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.365x slower (HPT: reliability of 100.00%, 1.40x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log
- [📄table](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0.md)
- [📈time plot](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.385x slower (HPT: reliability of 100.00%, 1.44x slower at 99th %ile)
- Memory usage: 1.16x
- [🧠memory plot](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base-mem.svg)
- [📄table](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base.md)
- [📈time plot](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10649186889)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json)

### vs. 3.10.4

- Geometric mean: 1.032x slower (HPT: reliability of 99.87%, 1.01x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.md)
- [📈time plot](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.253x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.md)
- [📈time plot](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.292x slower (HPT: reliability of 100.00%, 1.28x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0.md)
- [📈time plot](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.312x slower (HPT: reliability of 100.00%, 1.29x slower at 99th %ile)
- Memory usage: 1.15x
- [🧠memory plot](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base-mem.svg)
- [📄table](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base.md)
- [📈time plot](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10649186889)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json)

### vs. 3.10.4

- Geometric mean: 1.107x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.md)
- [📈time plot](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.306x slower (HPT: reliability of 100.00%, 1.27x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.md)
- [📈time plot](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.300x slower (HPT: reliability of 100.00%, 1.31x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0.md)
- [📈time plot](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.328x slower (HPT: reliability of 100.00%, 1.34x slower at 99th %ile)
- Memory usage: 1.15x
- [🧠memory plot](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base-mem.svg)
- [📄table](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base.md)
- [📈time plot](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10649186889)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json)

### vs. 3.10.4

- Geometric mean: 1.145x slower (HPT: reliability of 100.00%, 1.14x slower at 99th %ile)
- Memory usage: 0.77x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.md)
- [📈time plot](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.271x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: 0.69x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.md)
- [📈time plot](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.255x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 0.56x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0.md)
- [📈time plot](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.317x slower (HPT: reliability of 100.00%, 1.24x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base-mem.svg)
- [📄table](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base.md)
- [📈time plot](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base.svg)


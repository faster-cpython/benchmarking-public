# Results

- fork: nick-arm/codecache_rwx
- version: 3.14.0a0
- config: JIT
- commit hash: [0442576](https://github.com/nick%2darm/cpython/commit/0442576)
- commit date: 2024-10-07T16:19:31+00:00
- commit merge base: [5e9e50612eb27aef8f74a0ccc234e5cfae50c4d7](https://github.com/python/cpython/commit/5e9e50612eb27aef8f74a0ccc234e5cfae50c4d7)
- ref: codecache_rwx

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11265792093)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241007-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a0-0442576.json)

### vs. 3.10.4

- Geometric mean: 1.198x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20241007-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.10.4.md)
- [📈time plot](bm-20241007-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.058x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20241007-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.12.0.md)
- [📈time plot](bm-20241007-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.067x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241007-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.13.0.md)
- [📈time plot](bm-20241007-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.025x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 0.90x
- missing benchmarks: 🔴 sphinx
- [🧠memory plot](bm-20241007-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-base-mem.svg)
- [📄table](bm-20241007-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-base.md)
- [📈time plot](bm-20241007-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11265792093)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241007-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576.json)

### vs. 3.10.4

- Geometric mean: 1.432x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241007-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.10.4.md)
- [📈time plot](bm-20241007-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.094x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241007-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.12.0.md)
- [📈time plot](bm-20241007-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.035x faster (HPT: reliability of 97.74%, 1.00x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241007-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.13.0.md)
- [📈time plot](bm-20241007-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.021x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: 🔴 sphinx
- [🧠memory plot](bm-20241007-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-base-mem.svg)
- [📄table](bm-20241007-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-base.md)
- [📈time plot](bm-20241007-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11265792093)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241007-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576.json)

### vs. 3.10.4

- Geometric mean: 1.304x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241007-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.10.4.md)
- [📈time plot](bm-20241007-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.011x faster (HPT: reliability of 50.39%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241007-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.12.0.md)
- [📈time plot](bm-20241007-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.014x faster (HPT: reliability of 85.17%, 1.00x faster at 99th %ile)
- Memory usage: 0.96x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241007-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.13.0.md)
- [📈time plot](bm-20241007-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.013x faster (HPT: reliability of 97.91%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: 🔴 sphinx
- [🧠memory plot](bm-20241007-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-base-mem.svg)
- [📄table](bm-20241007-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-base.md)
- [📈time plot](bm-20241007-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11265792093)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241007-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a0-0442576.json)

### vs. 3.10.4

- Geometric mean: 1.282x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241007-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.10.4.md)
- [📈time plot](bm-20241007-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.078x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.95x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241007-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.12.0.md)
- [📈time plot](bm-20241007-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.084x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.86x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241007-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.13.0.md)
- [📈time plot](bm-20241007-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.036x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.73x
- missing benchmarks: 🔴 sphinx
- [🧠memory plot](bm-20241007-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-base-mem.svg)
- [📄table](bm-20241007-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-base.md)
- [📈time plot](bm-20241007-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-base.svg)


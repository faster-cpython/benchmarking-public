# Results

- fork: nick-arm/codecache
- version: 3.14.0a0
- config: JIT
- commit hash: [c2fad93](https://github.com/nick%2darm/cpython/commit/c2fad93)
- commit date: 2024-10-17T13:54:09+00:00
- commit merge base: [5e9e50612eb27aef8f74a0ccc234e5cfae50c4d7](https://github.com/python/cpython/commit/5e9e50612eb27aef8f74a0ccc234e5cfae50c4d7)
- ref: codecache

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11394701974)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241017-arminc-aarch64-nick%252darm-codecache-3.14.0a0-c2fad93.json)

### vs. 3.10.4

- Geometric mean: 1.172x faster (HPT: reliability of 99.99%, 1.03x faster at 99th %ile)
- Memory usage: 1.39x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241017-arminc-aarch64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.10.4.md)
- [📈time plot](bm-20241017-arminc-aarch64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.078x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241017-arminc-aarch64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.12.0.md)
- [📈time plot](bm-20241017-arminc-aarch64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.087x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241017-arminc-aarch64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.13.0.md)
- [📈time plot](bm-20241017-arminc-aarch64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241017-arminc-aarch64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-base-mem.svg)
- [📄table](bm-20241017-arminc-aarch64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-base.md)
- [📈time plot](bm-20241017-arminc-aarch64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241017-azure-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93-pystats.json)
- [pystats table](bm-20241017-azure-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93-pystats.md)

### vs. base

- [pystats diff](bm-20241017-azure-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11394701974)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241017-linux-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93.json)

### vs. 3.10.4

- Geometric mean: 1.401x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241017-linux-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.10.4.md)
- [📈time plot](bm-20241017-linux-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.070x faster (HPT: reliability of 99.97%, 1.02x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241017-linux-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.12.0.md)
- [📈time plot](bm-20241017-linux-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.012x faster (HPT: reliability of 56.70%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241017-linux-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.13.0.md)
- [📈time plot](bm-20241017-linux-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x slower (HPT: reliability of 63.07%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241017-linux-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-base-mem.svg)
- [📄table](bm-20241017-linux-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-base.md)
- [📈time plot](bm-20241017-linux-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11394701974)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241017-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93.json)

### vs. 3.10.4

- Geometric mean: 1.291x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241017-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.10.4.md)
- [📈time plot](bm-20241017-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.000x slower (HPT: reliability of 73.58%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241017-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.12.0.md)
- [📈time plot](bm-20241017-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.003x faster (HPT: reliability of 54.62%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241017-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.13.0.md)
- [📈time plot](bm-20241017-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 99.12%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241017-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-base-mem.svg)
- [📄table](bm-20241017-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-base.md)
- [📈time plot](bm-20241017-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11394701974)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241017-darwin-arm64-nick%252darm-codecache-3.14.0a0-c2fad93.json)

### vs. 3.10.4

- Geometric mean: 1.270x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241017-darwin-arm64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.10.4.md)
- [📈time plot](bm-20241017-darwin-arm64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.067x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241017-darwin-arm64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.12.0.md)
- [📈time plot](bm-20241017-darwin-arm64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.072x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241017-darwin-arm64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.13.0.md)
- [📈time plot](bm-20241017-darwin-arm64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.027x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- [🧠memory plot](bm-20241017-darwin-arm64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-base-mem.svg)
- [📄table](bm-20241017-darwin-arm64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-base.md)
- [📈time plot](bm-20241017-darwin-arm64-nick%252darm-codecache-3.14.0a0-c2fad93-vs-base.svg)


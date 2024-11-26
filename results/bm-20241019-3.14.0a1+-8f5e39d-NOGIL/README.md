# Results

- fork: python
- version: 3.14.0a1+
- config: NOGIL
- commit hash: [8f5e39d](https://github.com/python/cpython/commit/8f5e39d)
- commit date: 2024-10-19T17:46:57-04:00
- commit merge base: [4c53b2577531c77193430cdcd66ad6385fcda81f](https://github.com/python/cpython/commit/4c53b2577531c77193430cdcd66ad6385fcda81f)
- ref: 8f5e39d5c885318e3128

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11421710436)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d.json)

### vs. 3.10.4

- Geometric mean: 1.190x slower (HPT: reliability of 100.00%, 1.17x slower at 99th %ile)
- Memory usage: 1.51x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)
- [📈time plot](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.359x slower (HPT: reliability of 100.00%, 1.37x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)
- [📈time plot](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.368x slower (HPT: reliability of 100.00%, 1.39x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)
- [📈time plot](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.374x slower (HPT: reliability of 100.00%, 1.40x slower at 99th %ile)
- Memory usage: 1.17x
- [🧠memory plot](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base-mem.svg)
- [📄table](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.md)
- [📈time plot](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11421710436)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d.json)

### vs. 3.10.4

- Geometric mean: 1.042x slower (HPT: reliability of 99.91%, 1.02x slower at 99th %ile)
- Memory usage: 1.45x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)
- [📈time plot](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.259x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)
- [📈time plot](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.298x slower (HPT: reliability of 100.00%, 1.28x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)
- [📈time plot](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.307x slower (HPT: reliability of 100.00%, 1.31x slower at 99th %ile)
- Memory usage: 1.15x
- [🧠memory plot](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base-mem.svg)
- [📄table](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.md)
- [📈time plot](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11421710436)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d.json)

### vs. 3.10.4

- Geometric mean: 1.102x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.47x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)
- [📈time plot](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.299x slower (HPT: reliability of 100.00%, 1.26x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)
- [📈time plot](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.295x slower (HPT: reliability of 100.00%, 1.29x slower at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)
- [📈time plot](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.311x slower (HPT: reliability of 100.00%, 1.33x slower at 99th %ile)
- Memory usage: 1.17x
- [🧠memory plot](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base-mem.svg)
- [📄table](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.md)
- [📈time plot](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11421710436)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d.json)

### vs. 3.10.4

- Geometric mean: 1.097x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.45x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)
- [📈time plot](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.229x slower (HPT: reliability of 100.00%, 1.14x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)
- [📈time plot](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.214x slower (HPT: reliability of 100.00%, 1.15x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)
- [📈time plot](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.270x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 1.10x
- [🧠memory plot](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base-mem.svg)
- [📄table](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.md)
- [📈time plot](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.svg)


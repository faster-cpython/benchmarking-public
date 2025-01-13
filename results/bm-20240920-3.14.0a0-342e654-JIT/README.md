# Results

- fork: python/342e654b8eda24c68da6
- version: 3.14.0a0
- config: JIT
- commit hash: [342e654](https://github.com/python/cpython/commit/342e654)
- commit date: 2024-09-20T13:37:49+00:00
- commit merge base: [1a577729e347714eb819fa3a3a00149406c24e5e](https://github.com/python/cpython/commit/1a577729e347714eb819fa3a3a00149406c24e5e)
- ref: 342e654b8eda24c68da6

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10976602788)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json)

### vs. 3.10.4

- Geometric mean: 1.176x faster (HPT: reliability of 99.98%, 1.03x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.10.4.md)
- [📈time plot](bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.075x slower (HPT: reliability of 99.99%, 1.02x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.12.0.md)
- [📈time plot](bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.082x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.13.0.md)
- [📈time plot](bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.110x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.09x
- [🧠memory plot](bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base-mem.svg)
- [📄table](bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base.md)
- [📈time plot](bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10976602788)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240920-linux-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json)

### vs. 3.10.4

- Geometric mean: 1.433x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240920-linux-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.10.4.md)
- [📈time plot](bm-20240920-linux-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.094x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240920-linux-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.12.0.md)
- [📈time plot](bm-20240920-linux-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.036x faster (HPT: reliability of 95.19%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240920-linux-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.13.0.md)
- [📈time plot](bm-20240920-linux-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x slower (HPT: reliability of 90.68%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- [🧠memory plot](bm-20240920-linux-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base-mem.svg)
- [📄table](bm-20240920-linux-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base.md)
- [📈time plot](bm-20240920-linux-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10976602788)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json)

### vs. 3.10.4

- Geometric mean: 1.321x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.10.4.md)
- [📈time plot](bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.022x faster (HPT: reliability of 77.27%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.12.0.md)
- [📈time plot](bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.027x faster (HPT: reliability of 95.23%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.13.0.md)
- [📈time plot](bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.006x slower (HPT: reliability of 79.43%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- [🧠memory plot](bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base-mem.svg)
- [📄table](bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base.md)
- [📈time plot](bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10976602788)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json)

### vs. 3.10.4

- Geometric mean: 1.239x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.10.4.md)
- [📈time plot](bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.051x faster (HPT: reliability of 95.64%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.12.0.md)
- [📈time plot](bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x faster (HPT: reliability of 97.59%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.13.0.md)
- [📈time plot](bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.057x faster (HPT: reliability of 96.70%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base.md)
- [📈time plot](bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10976602788)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654.json)

### vs. 3.10.4

- Geometric mean: 1.222x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.10.4.md)
- [📈time plot](bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.233x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.12.0.md)
- [📈time plot](bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.106x faster (HPT: reliability of 98.48%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.13.0.md)
- [📈time plot](bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.083x faster (HPT: reliability of 99.93%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base.md)
- [📈time plot](bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10976602788)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json)

### vs. 3.10.4

- Geometric mean: 1.243x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 0.56x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.10.4.md)
- [📈time plot](bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.051x faster (HPT: reliability of 98.72%, 1.00x faster at 99th %ile)
- Memory usage: 0.55x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.12.0.md)
- [📈time plot](bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.055x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 0.47x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.13.0.md)
- [📈time plot](bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.043x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base-mem.svg)
- [📄table](bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base.md)
- [📈time plot](bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base.svg)


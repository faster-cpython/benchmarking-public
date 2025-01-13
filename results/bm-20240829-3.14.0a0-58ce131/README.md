# Results

- fork: python/58ce131037ecb34d506a
- version: 3.14.0a0
- config: 
- commit hash: [58ce131](https://github.com/python/cpython/commit/58ce131)
- commit date: 2024-08-29T11:12:37+03:00
- commit merge base: [303f92a9ce0de3667fb6b3ed22fa3bea5f835066](https://github.com/python/cpython/commit/303f92a9ce0de3667fb6b3ed22fa3bea5f835066)
- ref: 58ce131037ecb34d506a

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10707835585)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131.json)

### vs. 3.10.4

- Geometric mean: 1.338x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.10.4.md)
- [📈time plot](bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.042x faster (HPT: reliability of 98.79%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.12.0.md)
- [📈time plot](bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.031x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.13.0.md)
- [📈time plot](bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10707835585)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131.json)

### vs. 3.10.4

- Geometric mean: 1.438x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.10.4.md)
- [📈time plot](bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.088x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.12.0.md)
- [📈time plot](bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x faster (HPT: reliability of 99.88%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: chameleon, connected_components, djangocms, dulwich_log, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.13.0.md)
- [📈time plot](bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10707835585)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131.json)

### vs. 3.10.4

- Geometric mean: 1.344x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.10.4.md)
- [📈time plot](bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.031x faster (HPT: reliability of 93.65%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.12.0.md)
- [📈time plot](bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.040x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, connected_components, djangocms, dulwich_log, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.13.0.md)
- [📈time plot](bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10707835585)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131.json)

### vs. 3.10.4

- Geometric mean: 1.162x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.10.4.md)
- [📈time plot](bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.025x slower (HPT: reliability of 99.90%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.12.0.md)
- [📈time plot](bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.13.0.md)
- [📈time plot](bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10707835585)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131.json)

### vs. 3.10.4

- Geometric mean: 1.127x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.10.4.md)
- [📈time plot](bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.133x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.12.0.md)
- [📈time plot](bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.025x faster (HPT: reliability of 99.68%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.13.0.md)
- [📈time plot](bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10707835585)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131.json)

### vs. 3.10.4

- Geometric mean: 1.305x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 0.68x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.10.4.md)
- [📈time plot](bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.089x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.61x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.12.0.md)
- [📈time plot](bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.095x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.55x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.13.0.md)
- [📈time plot](bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131-vs-3.13.0.svg)


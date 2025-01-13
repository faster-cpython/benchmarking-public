# Results

- fork: python/99400930ac1d4e5e10a5
- version: 3.14.0a0
- config: 
- commit hash: [9940093](https://github.com/python/cpython/commit/9940093)
- commit date: 2024-10-09T16:44:03-07:00
- commit merge base: [942916378aa6a0946b1385c2c7ca6935620d710a](https://github.com/python/cpython/commit/942916378aa6a0946b1385c2c7ca6935620d710a)
- ref: 99400930ac1d4e5e10a5

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11275986568)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241009-linux-x86_64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093.json)

### vs. 3.10.4

- Geometric mean: 1.429x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241009-linux-x86_64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.10.4.md)
- [📈time plot](bm-20241009-linux-x86_64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.084x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241009-linux-x86_64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.12.0.md)
- [📈time plot](bm-20241009-linux-x86_64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.031x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241009-linux-x86_64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.13.0.md)
- [📈time plot](bm-20241009-linux-x86_64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11273331780)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093.json)

### vs. 3.10.4

- Geometric mean: 1.145x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.10.4.md)
- [📈time plot](bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.037x slower (HPT: reliability of 99.98%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.12.0.md)
- [📈time plot](bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.048x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.13.0.md)
- [📈time plot](bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11273317937)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241009-darwin-arm64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093.json)

### vs. 3.10.4

- Geometric mean: 1.315x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 0.79x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241009-darwin-arm64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.10.4.md)
- [📈time plot](bm-20241009-darwin-arm64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.096x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 0.71x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241009-darwin-arm64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.12.0.md)
- [📈time plot](bm-20241009-darwin-arm64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.101x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 0.57x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241009-darwin-arm64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.13.0.md)
- [📈time plot](bm-20241009-darwin-arm64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.13.0.svg)


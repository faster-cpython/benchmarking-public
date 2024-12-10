# Results

- fork: python/faa3272fb8d63d481a13
- version: 3.14.0a1+
- config: 
- commit hash: [faa3272](https://github.com/python/cpython/commit/faa3272)
- commit date: 2024-10-29T11:15:42+00:00
- commit merge base: [67f5c5bd6fcc956a785edef3be67e8cbe470cd31](https://github.com/python/cpython/commit/67f5c5bd6fcc956a785edef3be67e8cbe470cd31)
- ref: faa3272fb8d63d481a13

## linux x86_64 (azure)

- [pystats raw](bm-20241029-azure-x86_64-python-faa3272fb8d63d481a13-3.14.0a1%2B-faa3272-pystats.json)
- [pystats table](bm-20241029-azure-x86_64-python-faa3272fb8d63d481a13-3.14.0a1%2B-faa3272-pystats.md)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11655636132)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1%2B-faa3272.json)

### vs. 3.10.4

- Geometric mean: 1.178x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1%2B-faa3272-vs-3.10.4.md)
- [📈time plot](bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1%2B-faa3272-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.011x slower (HPT: reliability of 97.32%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1%2B-faa3272-vs-3.12.0.md)
- [📈time plot](bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1%2B-faa3272-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.024x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, many_optionals, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- [📄table](bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1%2B-faa3272-vs-3.13.0.md)
- [📈time plot](bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1%2B-faa3272-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11655639777)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1%2B-faa3272.json)

### vs. 3.10.4

- Geometric mean: 1.292x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1%2B-faa3272-vs-3.10.4.md)
- [📈time plot](bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1%2B-faa3272-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.078x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1%2B-faa3272-vs-3.12.0.md)
- [📈time plot](bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1%2B-faa3272-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.078x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, many_optionals, subparsers
- [📄table](bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1%2B-faa3272-vs-3.13.0.md)
- [📈time plot](bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1%2B-faa3272-vs-3.13.0.svg)


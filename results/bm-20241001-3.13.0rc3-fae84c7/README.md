# Results

- fork: python/v3.13.0rc3
- version: 3.13.0rc3
- config: 
- commit hash: [fae84c7](https://github.com/python/cpython/commit/fae84c7)
- commit date: 2024-10-01T04:03:08+02:00
- ref: v3.13.0rc3

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11166022331)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7.json)

### vs. 3.10.4

- Geometric mean: 1.305x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: dulwich_log, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.10.4.md)
- [📈time plot](bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.021x faster (HPT: reliability of 95.19%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: dulwich_log, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, flaskblogging, unpack_sequence
- [📄table](bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.12.0.md)
- [📈time plot](bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.014x faster (HPT: reliability of 99.44%, 1.00x faster at 99th %ile)
- Memory usage: 0.90x
- missing benchmarks: connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.13.0.md)
- [📈time plot](bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11166022331)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7.json)

### vs. 3.10.4

- Geometric mean: 1.394x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.10.4.md)
- [📈time plot](bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.070x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.12.0.md)
- [📈time plot](bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.018x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: connected_components, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.13.0.md)
- [📈time plot](bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11166022331)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7.json)

### vs. 3.10.4

- Geometric mean: 1.292x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.10.4.md)
- [📈time plot](bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.001x slower (HPT: reliability of 61.43%, 1.00x slower at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.12.0.md)
- [📈time plot](bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.009x faster (HPT: reliability of 60.94%, 1.00x slower at 99th %ile)
- Memory usage: 0.90x
- missing benchmarks: connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.13.0.md)
- [📈time plot](bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11166022331)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7.json)

### vs. 3.10.4

- Geometric mean: 1.222x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.10.4.md)
- [📈time plot](bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.068x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.12.0.md)
- [📈time plot](bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.023x faster (HPT: reliability of 98.78%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.13.0.md)
- [📈time plot](bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11166022331)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7.json)

### vs. 3.10.4

- Geometric mean: 1.135x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.10.4.md)
- [📈time plot](bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.178x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.12.0.md)
- [📈time plot](bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.13.0.md)
- [📈time plot](bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11257187178)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7.json)

### vs. 3.10.4

- Geometric mean: 1.177x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 0.73x
- missing benchmarks: connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.10.4.md)
- [📈time plot](bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.009x slower (HPT: reliability of 88.73%, 1.00x slower at 99th %ile)
- Memory usage: 0.57x
- missing benchmarks: connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.12.0.md)
- [📈time plot](bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.025x faster (HPT: reliability of 60.25%, 1.00x slower at 99th %ile)
- Memory usage: 0.33x
- missing benchmarks: connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.13.0.md)
- [📈time plot](bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7-vs-3.13.0.svg)


# Results

- fork: python/9e474a98af4184615540
- version: 3.14.0a5+
- config: 
- commit hash: [9e474a9](https://github.com/python/cpython/commit/9e474a9)
- commit date: 2025-02-26T15:42:39+01:00
- commit merge base: [56e190068177855266f32a7efa329d145b279f94](https://github.com/python/cpython/commit/56e190068177855266f32a7efa329d145b279f94)
- ref: 9e474a98af4184615540

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13632571678)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250226-arminc-aarch64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9.json)

### vs. 3.10.4

- Geometric mean: 1.330x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250226-arminc-aarch64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.10.4.md)
- [📈time plot](bm-20250226-arminc-aarch64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.042x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250226-arminc-aarch64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.12.0.md)
- [📈time plot](bm-20250226-arminc-aarch64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250226-arminc-aarch64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.13.0.md)
- [📈time plot](bm-20250226-arminc-aarch64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13632571678)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250226-linux-x86_64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9.json)

### vs. 3.10.4

- Geometric mean: 1.451x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250226-linux-x86_64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.10.4.md)
- [📈time plot](bm-20250226-linux-x86_64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.115x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250226-linux-x86_64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.12.0.md)
- [📈time plot](bm-20250226-linux-x86_64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.047x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250226-linux-x86_64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.13.0.md)
- [📈time plot](bm-20250226-linux-x86_64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13632571678)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250226-pythonperf2-x86_64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9.json)

### vs. 3.10.4

- Geometric mean: 1.341x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250226-pythonperf2-x86_64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.10.4.md)
- [📈time plot](bm-20250226-pythonperf2-x86_64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.041x faster (HPT: reliability of 99.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250226-pythonperf2-x86_64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.12.0.md)
- [📈time plot](bm-20250226-pythonperf2-x86_64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.052x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250226-pythonperf2-x86_64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.13.0.md)
- [📈time plot](bm-20250226-pythonperf2-x86_64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13632571678)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250226-pythonperf1-amd64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9.json)

### vs. 3.10.4

- Geometric mean: 1.207x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250226-pythonperf1-amd64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.10.4.md)
- [📈time plot](bm-20250226-pythonperf1-amd64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.024x faster (HPT: reliability of 90.62%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250226-pythonperf1-amd64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.12.0.md)
- [📈time plot](bm-20250226-pythonperf1-amd64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.006x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250226-pythonperf1-amd64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.13.0.md)
- [📈time plot](bm-20250226-pythonperf1-amd64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13632571678)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250226-pythonperf1_win32-x86-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9.json)

### vs. 3.10.4

- Geometric mean: 1.124x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250226-pythonperf1_win32-x86-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.10.4.md)
- [📈time plot](bm-20250226-pythonperf1_win32-x86-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.134x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250226-pythonperf1_win32-x86-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.12.0.md)
- [📈time plot](bm-20250226-pythonperf1_win32-x86-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.006x faster (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250226-pythonperf1_win32-x86-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.13.0.md)
- [📈time plot](bm-20250226-pythonperf1_win32-x86-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13632571678)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250226-darwin-arm64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9.json)

### vs. 3.10.4

- Geometric mean: 1.256x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250226-darwin-arm64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.10.4.md)
- [📈time plot](bm-20250226-darwin-arm64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.012x slower (HPT: reliability of 98.73%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250226-darwin-arm64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.12.0.md)
- [📈time plot](bm-20250226-darwin-arm64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.009x slower (HPT: reliability of 62.81%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250226-darwin-arm64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.13.0.md)
- [📈time plot](bm-20250226-darwin-arm64-python-9e474a98af4184615540-3.14.0a5%2B-9e474a9-vs-3.13.0.svg)


# Results

- fork: python/f18b2264929c56360c86
- version: 3.14.0a4+
- config: 
- commit hash: [f18b226](https://github.com/python/cpython/commit/f18b226)
- commit date: 2025-01-21T20:05:19+00:00
- commit merge base: [610584639003317193cdcfe38bbdc8268b612828](https://github.com/python/cpython/commit/610584639003317193cdcfe38bbdc8268b612828)
- ref: f18b2264929c56360c86

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12935110419)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250121-arminc-aarch64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226.json)

### vs. 3.10.4

- Geometric mean: 1.311x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250121-arminc-aarch64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.10.4.md)
- [📈time plot](bm-20250121-arminc-aarch64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.032x faster (HPT: reliability of 98.82%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250121-arminc-aarch64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.12.0.md)
- [📈time plot](bm-20250121-arminc-aarch64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.035x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250121-arminc-aarch64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.13.0.md)
- [📈time plot](bm-20250121-arminc-aarch64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12935110419)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226.json)

### vs. 3.10.4

- Geometric mean: 1.442x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.10.4.md)
- [📈time plot](bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.110x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.12.0.md)
- [📈time plot](bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.042x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.13.0.md)
- [📈time plot](bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12935110419)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226.json)

### vs. 3.10.4

- Geometric mean: 1.353x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.10.4.md)
- [📈time plot](bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.049x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.12.0.md)
- [📈time plot](bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.061x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.13.0.md)
- [📈time plot](bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12935110419)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226.json)

### vs. 3.10.4

- Geometric mean: 1.191x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.10.4.md)
- [📈time plot](bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.011x faster (HPT: reliability of 94.31%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.12.0.md)
- [📈time plot](bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.019x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.13.0.md)
- [📈time plot](bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12935110419)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226.json)

### vs. 3.10.4

- Geometric mean: 1.119x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.10.4.md)
- [📈time plot](bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.128x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.12.0.md)
- [📈time plot](bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.003x faster (HPT: reliability of 99.94%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.13.0.md)
- [📈time plot](bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12935110419)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226.json)

### vs. 3.10.4

- Geometric mean: 1.363x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.10.4.md)
- [📈time plot](bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.072x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.12.0.md)
- [📈time plot](bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.075x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.13.0.md)
- [📈time plot](bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4%2B-f18b226-vs-3.13.0.svg)


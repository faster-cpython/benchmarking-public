# Results

- fork: python/2a66dd33dfc0b845042d
- version: 3.14.0a3+
- config: JIT
- commit hash: [2a66dd3](https://github.com/python/cpython/commit/2a66dd3)
- commit date: 2024-12-20T11:40:58-08:00
- commit merge base: [3879ca0100942ae15a09ac22889cbe3e46d424eb](https://github.com/python/cpython/commit/3879ca0100942ae15a09ac22889cbe3e46d424eb)
- ref: 2a66dd33dfc0b845042d

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12449454953)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3.json)

### vs. 3.10.4

- Geometric mean: 1.224x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.10.4.md)
- [📈time plot](bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.031x slower (HPT: reliability of 99.29%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.12.0.md)
- [📈time plot](bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.024x slower (HPT: reliability of 93.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log, mypy2
- [📄table](bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.13.0.md)
- [📈time plot](bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.050x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-base-mem.svg)
- [📄table](bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-base.md)
- [📈time plot](bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12449454953)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241220-linux-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3.json)

### vs. 3.10.4

- Geometric mean: 1.432x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241220-linux-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.10.4.md)
- [📈time plot](bm-20241220-linux-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.107x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241220-linux-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.12.0.md)
- [📈time plot](bm-20241220-linux-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x faster (HPT: reliability of 98.54%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241220-linux-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.13.0.md)
- [📈time plot](bm-20241220-linux-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 91.42%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241220-linux-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-base-mem.svg)
- [📄table](bm-20241220-linux-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-base.md)
- [📈time plot](bm-20241220-linux-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12449454953)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3.json)

### vs. 3.10.4

- Geometric mean: 1.305x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.10.4.md)
- [📈time plot](bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.017x faster (HPT: reliability of 76.22%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.12.0.md)
- [📈time plot](bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x faster (HPT: reliability of 99.47%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.13.0.md)
- [📈time plot](bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.022x slower (HPT: reliability of 99.93%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-base-mem.svg)
- [📄table](bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-base.md)
- [📈time plot](bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12449454953)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3.json)

### vs. 3.10.4

- Geometric mean: 1.245x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.10.4.md)
- [📈time plot](bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.063x faster (HPT: reliability of 97.72%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.12.0.md)
- [📈time plot](bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.027x faster (HPT: reliability of 52.49%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.13.0.md)
- [📈time plot](bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.046x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-base.md)
- [📈time plot](bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12449454953)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3.json)

### vs. 3.10.4

- Geometric mean: 1.054x faster (HPT: reliability of 75.00%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.10.4.md)
- [📈time plot](bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.064x faster (HPT: reliability of 99.96%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.12.0.md)
- [📈time plot](bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.052x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.13.0.md)
- [📈time plot](bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.080x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-base.md)
- [📈time plot](bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-base.svg)


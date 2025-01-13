# Results

- fork: python/2de048ce79e621f5ae05
- version: 3.14.0a2+
- config: JIT
- commit hash: [2de048c](https://github.com/python/cpython/commit/2de048c)
- commit date: 2024-12-13T10:17:16-08:00
- commit merge base: [292067fbc9db81896c16ff12d51c21d2b0f233e2](https://github.com/python/cpython/commit/292067fbc9db81896c16ff12d51c21d2b0f233e2)
- ref: 2de048ce79e621f5ae05

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12356877260)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c.json)

### vs. 3.10.4

- Geometric mean: 1.231x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.10.4.md)
- [📈time plot](bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.027x slower (HPT: reliability of 97.91%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.12.0.md)
- [📈time plot](bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.019x slower (HPT: reliability of 91.17%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log, mypy2
- [📄table](bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.13.0.md)
- [📈time plot](bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241213-azure-x86_64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-pystats.json)
- [pystats table](bm-20241213-azure-x86_64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12356877260)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241213-linux-x86_64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c.json)

### vs. 3.10.4

- Geometric mean: 1.437x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241213-linux-x86_64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.10.4.md)
- [📈time plot](bm-20241213-linux-x86_64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.110x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241213-linux-x86_64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.12.0.md)
- [📈time plot](bm-20241213-linux-x86_64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x faster (HPT: reliability of 99.04%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241213-linux-x86_64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.13.0.md)
- [📈time plot](bm-20241213-linux-x86_64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12356877260)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c.json)

### vs. 3.10.4

- Geometric mean: 1.300x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.10.4.md)
- [📈time plot](bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.014x faster (HPT: reliability of 67.52%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.12.0.md)
- [📈time plot](bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.027x faster (HPT: reliability of 99.11%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.13.0.md)
- [📈time plot](bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12356877260)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c.json)

### vs. 3.10.4

- Geometric mean: 1.248x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.10.4.md)
- [📈time plot](bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.067x faster (HPT: reliability of 98.64%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.12.0.md)
- [📈time plot](bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.026x faster (HPT: reliability of 52.33%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.13.0.md)
- [📈time plot](bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12356877260)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c.json)

### vs. 3.10.4

- Geometric mean: 1.065x faster (HPT: reliability of 91.21%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.10.4.md)
- [📈time plot](bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.078x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.12.0.md)
- [📈time plot](bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.040x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.13.0.md)
- [📈time plot](bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12356877260)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c.json)

### vs. 3.10.4

- Geometric mean: 1.250x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, mypy2
- [📄table](bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.10.4.md)
- [📈time plot](bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.061x faster (HPT: reliability of 99.91%, 1.00x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.12.0.md)
- [📈time plot](bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.073x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.13.0.md)
- [📈time plot](bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2%2B-2de048c-vs-3.13.0.svg)


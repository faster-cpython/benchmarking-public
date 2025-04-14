# Results

- fork: python/1775091dc163d1fa76c3
- version: 3.14.0a5+
- config: 
- commit hash: [1775091](https://github.com/python/cpython/commit/1775091)
- commit date: 2025-02-14T18:34:32+01:00
- commit merge base: [303043f5062c1e7ffb7907abde61dbf13c98f8e9](https://github.com/python/cpython/commit/303043f5062c1e7ffb7907abde61dbf13c98f8e9)
- ref: 1775091dc163d1fa76c3

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13367754756)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250214-arminc-aarch64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091.json)

### vs. 3.10.4

- Geometric mean: 1.324x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250214-arminc-aarch64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.10.4.md)
- [📈time plot](bm-20250214-arminc-aarch64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.038x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250214-arminc-aarch64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.12.0.md)
- [📈time plot](bm-20250214-arminc-aarch64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250214-arminc-aarch64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.13.0.md)
- [📈time plot](bm-20250214-arminc-aarch64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13367754756)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250214-linux-x86_64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091.json)

### vs. 3.10.4

- Geometric mean: 1.455x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250214-linux-x86_64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.10.4.md)
- [📈time plot](bm-20250214-linux-x86_64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.117x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250214-linux-x86_64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.12.0.md)
- [📈time plot](bm-20250214-linux-x86_64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.049x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250214-linux-x86_64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.13.0.md)
- [📈time plot](bm-20250214-linux-x86_64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13367754756)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250214-pythonperf2-x86_64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091.json)

### vs. 3.10.4

- Geometric mean: 1.349x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250214-pythonperf2-x86_64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.10.4.md)
- [📈time plot](bm-20250214-pythonperf2-x86_64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.045x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250214-pythonperf2-x86_64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.12.0.md)
- [📈time plot](bm-20250214-pythonperf2-x86_64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.058x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250214-pythonperf2-x86_64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.13.0.md)
- [📈time plot](bm-20250214-pythonperf2-x86_64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13367754756)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091.json)

### vs. 3.10.4

- Geometric mean: 1.240x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.10.4.md)
- [📈time plot](bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.052x faster (HPT: reliability of 63.22%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.12.0.md)
- [📈time plot](bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.017x faster (HPT: reliability of 99.73%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.13.0.md)
- [📈time plot](bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13367754756)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250214-pythonperf1_win32-x86-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091.json)

### vs. 3.10.4

- Geometric mean: 1.097x faster (HPT: reliability of 99.93%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250214-pythonperf1_win32-x86-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.10.4.md)
- [📈time plot](bm-20250214-pythonperf1_win32-x86-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.103x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250214-pythonperf1_win32-x86-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.12.0.md)
- [📈time plot](bm-20250214-pythonperf1_win32-x86-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.022x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250214-pythonperf1_win32-x86-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.13.0.md)
- [📈time plot](bm-20250214-pythonperf1_win32-x86-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13367754756)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250214-darwin-arm64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091.json)

### vs. 3.10.4

- Geometric mean: 1.249x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250214-darwin-arm64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.10.4.md)
- [📈time plot](bm-20250214-darwin-arm64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.018x slower (HPT: reliability of 99.52%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250214-darwin-arm64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.12.0.md)
- [📈time plot](bm-20250214-darwin-arm64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.014x slower (HPT: reliability of 89.53%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250214-darwin-arm64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.13.0.md)
- [📈time plot](bm-20250214-darwin-arm64-python-1775091dc163d1fa76c3-3.14.0a5%2B-1775091-vs-3.13.0.svg)


# Results

- fork: eendebakpt/05f479c7b36947e5f3e9
- version: 3.14.0a3+
- config: 
- commit hash: [05f479c](https://github.com/eendebakpt/cpython/commit/05f479c)
- commit date: 2025-01-02T10:56:29+01:00
- commit merge base: [e1baa778f602ede66831eb34b9ef17f21e4d4347](https://github.com/python/cpython/commit/e1baa778f602ede66831eb34b9ef17f21e4d4347)
- fork: eendebakpt/iter_freelists
- ref: 05f479c7b36947e5f3e9, iter_freelists

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12585926978)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c.json)

### vs. 3.10.4

- Geometric mean: 1.319x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.10.4.md)
- [📈time plot](bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.036x faster (HPT: reliability of 99.76%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.12.0.md)
- [📈time plot](bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.041x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log, mypy2
- [📄table](bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.13.0.md)
- [📈time plot](bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 99.79%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-base-mem.svg)
- [📄table](bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-base.md)
- [📈time plot](bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12585926978)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c.json)

### vs. 3.10.4

- Geometric mean: 1.448x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.10.4.md)
- [📈time plot](bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.114x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.12.0.md)
- [📈time plot](bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.049x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.13.0.md)
- [📈time plot](bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.010x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- new benchmarks: mypy2
- [🧠memory plot](bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-base-mem.svg)
- [📄table](bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-base.md)
- [📈time plot](bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12585926978)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c.json)

### vs. 3.10.4

- Geometric mean: 1.359x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.10.4.md)
- [📈time plot](bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.057x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.12.0.md)
- [📈time plot](bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.071x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.13.0.md)
- [📈time plot](bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.013x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-base-mem.svg)
- [📄table](bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-base.md)
- [📈time plot](bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12585926978)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c.json)

### vs. 3.10.4

- Geometric mean: 1.194x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.10.4.md)
- [📈time plot](bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.014x faster (HPT: reliability of 87.96%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.12.0.md)
- [📈time plot](bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.013x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.13.0.md)
- [📈time plot](bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 62.72%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-base.md)
- [📈time plot](bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12585926978)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c.json)

### vs. 3.10.4

- Geometric mean: 1.173x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.10.4.md)
- [📈time plot](bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.184x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.12.0.md)
- [📈time plot](bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.056x faster (HPT: reliability of 97.06%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.13.0.md)
- [📈time plot](bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.014x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-base.md)
- [📈time plot](bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3%2B-05f479c-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12600005891)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3%2B-05f479c.json)

### vs. 3.10.4

- Geometric mean: 1.328x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, mypy2
- [📄table](bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3%2B-05f479c-vs-3.10.4.md)
- [📈time plot](bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3%2B-05f479c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.117x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3%2B-05f479c-vs-3.12.0.md)
- [📈time plot](bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3%2B-05f479c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.133x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3%2B-05f479c-vs-3.13.0.md)
- [📈time plot](bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3%2B-05f479c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.007x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3%2B-05f479c-vs-base-mem.svg)
- [📄table](bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3%2B-05f479c-vs-base.md)
- [📈time plot](bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3%2B-05f479c-vs-base.svg)


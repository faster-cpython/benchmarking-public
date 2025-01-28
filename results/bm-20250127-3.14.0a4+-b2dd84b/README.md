# Results

- fork: eendebakpt/iterator_freelists
- version: 3.14.0a4+
- config: 
- commit hash: [b2dd84b](https://github.com/eendebakpt/cpython/commit/b2dd84b)
- commit date: 2025-01-27T13:33:17+01:00
- commit merge base: [7ec17429d462aee071c067e3b84c8a7e4fcf7263](https://github.com/python/cpython/commit/7ec17429d462aee071c067e3b84c8a7e4fcf7263)
- ref: iterator_freelists

## linux x86_64 (azure)

- [pystats raw](bm-20250127-azure-x86_64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b-pystats.json)
- [pystats table](bm-20250127-azure-x86_64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b-pystats.md)

### vs. base

- [pystats diff](bm-20250127-azure-x86_64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b-pystats-vs-base.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13009997240)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b.json)

### vs. 3.10.4

- Geometric mean: 1.368x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b-vs-3.10.4.md)
- [📈time plot](bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.058x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b-vs-3.12.0.md)
- [📈time plot](bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.071x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b-vs-3.13.0.md)
- [📈time plot](bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.006x faster (HPT: reliability of 99.73%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b-vs-base-mem.svg)
- [📄table](bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b-vs-base.md)
- [📈time plot](bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13014221946)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b.json)

### vs. 3.10.4

- Geometric mean: 1.402x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b-vs-3.10.4.md)
- [📈time plot](bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.100x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b-vs-3.12.0.md)
- [📈time plot](bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.103x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b-vs-3.13.0.md)
- [📈time plot](bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b-vs-base-mem.svg)
- [📄table](bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b-vs-base.md)
- [📈time plot](bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4%2B-b2dd84b-vs-base.svg)


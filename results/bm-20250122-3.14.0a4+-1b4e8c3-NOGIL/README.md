# Results

- fork: nascheme/1b4e8c39e99ce39b39c7
- version: 3.14.0a4+
- config: NOGIL
- commit hash: [1b4e8c3](https://github.com/nascheme/cpython/commit/1b4e8c3)
- commit date: 2025-01-22T15:04:39-08:00
- commit merge base: [3829104ab412a47bf3f36b8c133c886d2cc9a6d4](https://github.com/python/cpython/commit/3829104ab412a47bf3f36b8c133c886d2cc9a6d4)
- ref: 1b4e8c39e99ce39b39c7

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12939809594)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3.json)

### vs. 3.10.4

- Geometric mean: 1.093x faster (HPT: reliability of 99.83%, 1.01x faster at 99th %ile)
- Memory usage: 1.57x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.10.4.md)
- [📈time plot](bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.134x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.12.0.md)
- [📈time plot](bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.137x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- new benchmarks: dulwich_log
- [📄table](bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.13.0.md)
- [📈time plot](bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 97.17%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: 🔴 xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- [🧠memory plot](bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-base-mem.svg)
- [📄table](bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-base.md)
- [📈time plot](bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12939809594)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250122-linux-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3.json)

### vs. 3.10.4

- Geometric mean: 1.241x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.51x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250122-linux-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.10.4.md)
- [📈time plot](bm-20250122-linux-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.041x slower (HPT: reliability of 99.98%, 1.02x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250122-linux-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.12.0.md)
- [📈time plot](bm-20250122-linux-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.102x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- [📄table](bm-20250122-linux-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.13.0.md)
- [📈time plot](bm-20250122-linux-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 57.43%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- [🧠memory plot](bm-20250122-linux-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-base-mem.svg)
- [📄table](bm-20250122-linux-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-base.md)
- [📈time plot](bm-20250122-linux-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12939809594)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3.json)

### vs. 3.10.4

- Geometric mean: 1.181x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.53x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.10.4.md)
- [📈time plot](bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.080x slower (HPT: reliability of 99.98%, 1.05x slower at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.12.0.md)
- [📈time plot](bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.071x slower (HPT: reliability of 99.98%, 1.03x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- [📄table](bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.13.0.md)
- [📈time plot](bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 89.40%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: 🔴 xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- [🧠memory plot](bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-base-mem.svg)
- [📄table](bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-base.md)
- [📈time plot](bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12939809594)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3.json)

### vs. 3.10.4

- Geometric mean: 1.295x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.10.4.md)
- [📈time plot](bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.032x faster (HPT: reliability of 55.38%, 1.00x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- [📄table](bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.12.0.md)
- [📈time plot](bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.035x faster (HPT: reliability of 96.03%, 1.00x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- [📄table](bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.13.0.md)
- [📈time plot](bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.007x slower (HPT: reliability of 83.54%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: 🔴 xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- [🧠memory plot](bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-base-mem.svg)
- [📄table](bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-base.md)
- [📈time plot](bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4%2B-1b4e8c3-vs-base.svg)


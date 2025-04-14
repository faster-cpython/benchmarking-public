# Results

- fork: faster-cpython/use_stackrefs
- version: 3.14.0a5+
- config: 
- commit hash: [3e929d7](https://github.com/faster%2dcpython/cpython/commit/3e929d7)
- commit date: 2025-02-28T11:11:51+00:00
- commit merge base: [fecf8bc8f2fd09a9a4c5177d32dbb42920b4e177](https://github.com/python/cpython/commit/fecf8bc8f2fd09a9a4c5177d32dbb42920b4e177)
- ref: use_stackrefs

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13587420104)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250228-pythonperf2-x86_64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7.json)

### vs. 3.10.4

- Geometric mean: 1.319x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250228-pythonperf2-x86_64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-3.10.4.md)
- [📈time plot](bm-20250228-pythonperf2-x86_64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.022x faster (HPT: reliability of 80.34%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250228-pythonperf2-x86_64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-3.12.0.md)
- [📈time plot](bm-20250228-pythonperf2-x86_64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.035x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250228-pythonperf2-x86_64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-3.13.0.md)
- [📈time plot](bm-20250228-pythonperf2-x86_64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.013x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250228-pythonperf2-x86_64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-base-mem.svg)
- [📄table](bm-20250228-pythonperf2-x86_64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-base.md)
- [📈time plot](bm-20250228-pythonperf2-x86_64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13587426108)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250228-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7.json)

### vs. 3.10.4

- Geometric mean: 1.213x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250228-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-3.10.4.md)
- [📈time plot](bm-20250228-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.030x faster (HPT: reliability of 83.58%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250228-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-3.12.0.md)
- [📈time plot](bm-20250228-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.005x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250228-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-3.13.0.md)
- [📈time plot](bm-20250228-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.009x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250228-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-base.md)
- [📈time plot](bm-20250228-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13587429778)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250228-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7.json)

### vs. 3.10.4

- Geometric mean: 1.287x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250228-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-3.10.4.md)
- [📈time plot](bm-20250228-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.012x faster (HPT: reliability of 85.74%, 1.00x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250228-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-3.12.0.md)
- [📈time plot](bm-20250228-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.015x faster (HPT: reliability of 73.84%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250228-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-3.13.0.md)
- [📈time plot](bm-20250228-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.024x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250228-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-base-mem.svg)
- [📄table](bm-20250228-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-base.md)
- [📈time plot](bm-20250228-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-3e929d7-vs-base.svg)


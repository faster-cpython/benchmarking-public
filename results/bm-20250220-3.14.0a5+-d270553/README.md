# Results

- fork: faster-cpython/use_stackrefs
- version: 3.14.0a5+
- config: 
- commit hash: [d270553](https://github.com/faster%2dcpython/cpython/commit/d270553)
- commit date: 2025-02-20T11:10:02+00:00
- commit merge base: [2498c22fa0a2b560491bc503fa676585c1a603d0](https://github.com/python/cpython/commit/2498c22fa0a2b560491bc503fa676585c1a603d0)
- ref: use_stackrefs

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13441567677)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250220-pythonperf2-x86_64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553.json)

### vs. 3.10.4

- Geometric mean: 1.338x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250220-pythonperf2-x86_64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-3.10.4.md)
- [📈time plot](bm-20250220-pythonperf2-x86_64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.036x faster (HPT: reliability of 99.05%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250220-pythonperf2-x86_64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-3.12.0.md)
- [📈time plot](bm-20250220-pythonperf2-x86_64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.050x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250220-pythonperf2-x86_64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-3.13.0.md)
- [📈time plot](bm-20250220-pythonperf2-x86_64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x slower (HPT: reliability of 99.66%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250220-pythonperf2-x86_64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-base-mem.svg)
- [📄table](bm-20250220-pythonperf2-x86_64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-base.md)
- [📈time plot](bm-20250220-pythonperf2-x86_64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13441581388)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250220-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553.json)

### vs. 3.10.4

- Geometric mean: 1.151x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250220-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-3.10.4.md)
- [📈time plot](bm-20250220-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.024x slower (HPT: reliability of 99.75%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250220-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-3.12.0.md)
- [📈time plot](bm-20250220-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.052x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250220-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-3.13.0.md)
- [📈time plot](bm-20250220-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.064x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250220-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-base.md)
- [📈time plot](bm-20250220-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13441573807)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250220-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553.json)

### vs. 3.10.4

- Geometric mean: 1.278x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250220-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-3.10.4.md)
- [📈time plot](bm-20250220-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.005x faster (HPT: reliability of 92.95%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250220-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-3.12.0.md)
- [📈time plot](bm-20250220-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.008x faster (HPT: reliability of 50.20%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250220-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-3.13.0.md)
- [📈time plot](bm-20250220-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.017x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250220-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-base-mem.svg)
- [📄table](bm-20250220-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-base.md)
- [📈time plot](bm-20250220-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a5%2B-d270553-vs-base.svg)


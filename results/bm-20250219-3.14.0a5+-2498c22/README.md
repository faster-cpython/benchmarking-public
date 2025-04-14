# Results

- fork: python/2498c22fa0a2b560491b
- version: 3.14.0a5+
- config: 
- commit hash: [2498c22](https://github.com/python/cpython/commit/2498c22)
- commit date: 2025-02-19T11:44:57+00:00
- commit merge base: [c637bce20aaaf836ab2cfbb123b9472e5ad0ab47](https://github.com/python/cpython/commit/c637bce20aaaf836ab2cfbb123b9472e5ad0ab47)
- ref: 2498c22fa0a2b560491b

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13441567677)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250219-pythonperf2-x86_64-python-2498c22fa0a2b560491b-3.14.0a5%2B-2498c22.json)

### vs. 3.10.4

- Geometric mean: 1.345x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250219-pythonperf2-x86_64-python-2498c22fa0a2b560491b-3.14.0a5%2B-2498c22-vs-3.10.4.md)
- [📈time plot](bm-20250219-pythonperf2-x86_64-python-2498c22fa0a2b560491b-3.14.0a5%2B-2498c22-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.042x faster (HPT: reliability of 99.97%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250219-pythonperf2-x86_64-python-2498c22fa0a2b560491b-3.14.0a5%2B-2498c22-vs-3.12.0.md)
- [📈time plot](bm-20250219-pythonperf2-x86_64-python-2498c22fa0a2b560491b-3.14.0a5%2B-2498c22-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.055x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250219-pythonperf2-x86_64-python-2498c22fa0a2b560491b-3.14.0a5%2B-2498c22-vs-3.13.0.md)
- [📈time plot](bm-20250219-pythonperf2-x86_64-python-2498c22fa0a2b560491b-3.14.0a5%2B-2498c22-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13441581388)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5%2B-2498c22.json)

### vs. 3.10.4

- Geometric mean: 1.233x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5%2B-2498c22-vs-3.10.4.md)
- [📈time plot](bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5%2B-2498c22-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.045x faster (HPT: reliability of 56.35%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5%2B-2498c22-vs-3.12.0.md)
- [📈time plot](bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5%2B-2498c22-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.013x faster (HPT: reliability of 99.98%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5%2B-2498c22-vs-3.13.0.md)
- [📈time plot](bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5%2B-2498c22-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13441573807)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250219-darwin-arm64-python-2498c22fa0a2b560491b-3.14.0a5%2B-2498c22.json)

### vs. 3.10.4

- Geometric mean: 1.257x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250219-darwin-arm64-python-2498c22fa0a2b560491b-3.14.0a5%2B-2498c22-vs-3.10.4.md)
- [📈time plot](bm-20250219-darwin-arm64-python-2498c22fa0a2b560491b-3.14.0a5%2B-2498c22-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.013x slower (HPT: reliability of 98.43%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250219-darwin-arm64-python-2498c22fa0a2b560491b-3.14.0a5%2B-2498c22-vs-3.12.0.md)
- [📈time plot](bm-20250219-darwin-arm64-python-2498c22fa0a2b560491b-3.14.0a5%2B-2498c22-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.009x slower (HPT: reliability of 62.94%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250219-darwin-arm64-python-2498c22fa0a2b560491b-3.14.0a5%2B-2498c22-vs-3.13.0.md)
- [📈time plot](bm-20250219-darwin-arm64-python-2498c22fa0a2b560491b-3.14.0a5%2B-2498c22-vs-3.13.0.svg)


# Results

- fork: python/fecf8bc8f2fd09a9a4c5
- version: 3.14.0a5+
- config: 
- commit hash: [fecf8bc](https://github.com/python/cpython/commit/fecf8bc)
- commit date: 2025-02-28T08:58:50+00:00
- commit merge base: [24c52cb14c4b044154bd46bd1b2a9c37076caeb9](https://github.com/python/cpython/commit/24c52cb14c4b044154bd46bd1b2a9c37076caeb9)
- ref: fecf8bc8f2fd09a9a4c5

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13587420104)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5%2B-fecf8bc.json)

### vs. 3.10.4

- Geometric mean: 1.336x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5%2B-fecf8bc-vs-3.10.4.md)
- [📈time plot](bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5%2B-fecf8bc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.036x faster (HPT: reliability of 98.44%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5%2B-fecf8bc-vs-3.12.0.md)
- [📈time plot](bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5%2B-fecf8bc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.049x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5%2B-fecf8bc-vs-3.13.0.md)
- [📈time plot](bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5%2B-fecf8bc-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13587426108)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5%2B-fecf8bc.json)

### vs. 3.10.4

- Geometric mean: 1.223x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5%2B-fecf8bc-vs-3.10.4.md)
- [📈time plot](bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5%2B-fecf8bc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.040x faster (HPT: reliability of 58.94%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5%2B-fecf8bc-vs-3.12.0.md)
- [📈time plot](bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5%2B-fecf8bc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.005x faster (HPT: reliability of 99.99%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5%2B-fecf8bc-vs-3.13.0.md)
- [📈time plot](bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5%2B-fecf8bc-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13587429778)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250228-darwin-arm64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5%2B-fecf8bc.json)

### vs. 3.10.4

- Geometric mean: 1.257x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250228-darwin-arm64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5%2B-fecf8bc-vs-3.10.4.md)
- [📈time plot](bm-20250228-darwin-arm64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5%2B-fecf8bc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.012x slower (HPT: reliability of 98.35%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250228-darwin-arm64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5%2B-fecf8bc-vs-3.12.0.md)
- [📈time plot](bm-20250228-darwin-arm64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5%2B-fecf8bc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.009x slower (HPT: reliability of 77.35%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250228-darwin-arm64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5%2B-fecf8bc-vs-3.13.0.md)
- [📈time plot](bm-20250228-darwin-arm64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5%2B-fecf8bc-vs-3.13.0.svg)


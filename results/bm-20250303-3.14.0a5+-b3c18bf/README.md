# Results

- fork: python/b3c18bfd828ba90b9c71
- version: 3.14.0a5+
- config: 
- commit hash: [b3c18bf](https://github.com/python/cpython/commit/b3c18bf)
- commit date: 2025-03-03T15:08:05+01:00
- commit merge base: [4f14b7e30c0243e81407a34968495301e829a033](https://github.com/python/cpython/commit/4f14b7e30c0243e81407a34968495301e829a033)
- ref: b3c18bfd828ba90b9c71

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13718494627)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf.json)

### vs. 3.10.4

- Geometric mean: 1.363x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.10.4.md)
- [📈time plot](bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.070x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.12.0.md)
- [📈time plot](bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.073x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.13.0.md)
- [📈time plot](bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13718494627)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250303-linux-x86_64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf.json)

### vs. 3.10.4

- Geometric mean: 1.454x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250303-linux-x86_64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.10.4.md)
- [📈time plot](bm-20250303-linux-x86_64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.116x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250303-linux-x86_64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.12.0.md)
- [📈time plot](bm-20250303-linux-x86_64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.048x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250303-linux-x86_64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.13.0.md)
- [📈time plot](bm-20250303-linux-x86_64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13718494627)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf.json)

### vs. 3.10.4

- Geometric mean: 1.204x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.10.4.md)
- [📈time plot](bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.021x faster (HPT: reliability of 91.83%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.12.0.md)
- [📈time plot](bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.011x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.13.0.md)
- [📈time plot](bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13718494627)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf.json)

### vs. 3.10.4

- Geometric mean: 1.253x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.10.4.md)
- [📈time plot](bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.015x slower (HPT: reliability of 99.14%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.12.0.md)
- [📈time plot](bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.012x slower (HPT: reliability of 77.55%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.13.0.md)
- [📈time plot](bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5%2B-b3c18bf-vs-3.13.0.svg)


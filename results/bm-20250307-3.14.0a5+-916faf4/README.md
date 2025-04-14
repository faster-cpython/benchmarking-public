# Results

- fork: faster-cpython/use_stackrefs_single
- version: 3.14.0a5+
- config: 
- commit hash: [916faf4](https://github.com/faster%2dcpython/cpython/commit/916faf4)
- commit date: 2025-03-07T10:12:24+00:00
- commit merge base: [b3c18bfd828ba90b9c712da74095c4a052887655](https://github.com/python/cpython/commit/b3c18bfd828ba90b9c712da74095c4a052887655)
- ref: use_stackrefs_single

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13718494627)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250307-arminc-aarch64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4.json)

### vs. 3.10.4

- Geometric mean: 1.290x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250307-arminc-aarch64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.10.4.md)
- [📈time plot](bm-20250307-arminc-aarch64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.014x faster (HPT: reliability of 70.43%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250307-arminc-aarch64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.12.0.md)
- [📈time plot](bm-20250307-arminc-aarch64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.017x faster (HPT: reliability of 84.55%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250307-arminc-aarch64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.13.0.md)
- [📈time plot](bm-20250307-arminc-aarch64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.050x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250307-arminc-aarch64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-base-mem.svg)
- [📄table](bm-20250307-arminc-aarch64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-base.md)
- [📈time plot](bm-20250307-arminc-aarch64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13718494627)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250307-linux-x86_64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4.json)

### vs. 3.10.4

- Geometric mean: 1.439x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250307-linux-x86_64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.10.4.md)
- [📈time plot](bm-20250307-linux-x86_64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.105x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250307-linux-x86_64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.12.0.md)
- [📈time plot](bm-20250307-linux-x86_64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x faster (HPT: reliability of 99.94%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250307-linux-x86_64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.13.0.md)
- [📈time plot](bm-20250307-linux-x86_64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.010x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250307-linux-x86_64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-base-mem.svg)
- [📄table](bm-20250307-linux-x86_64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-base.md)
- [📈time plot](bm-20250307-linux-x86_64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13718494627)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250307-pythonperf1-amd64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4.json)

### vs. 3.10.4

- Geometric mean: 1.219x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250307-pythonperf1-amd64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.10.4.md)
- [📈time plot](bm-20250307-pythonperf1-amd64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.035x faster (HPT: reliability of 62.45%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250307-pythonperf1-amd64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.12.0.md)
- [📈time plot](bm-20250307-pythonperf1-amd64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.001x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250307-pythonperf1-amd64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.13.0.md)
- [📈time plot](bm-20250307-pythonperf1-amd64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.011x faster (HPT: reliability of 78.31%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250307-pythonperf1-amd64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-base.md)
- [📈time plot](bm-20250307-pythonperf1-amd64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13718494627)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250307-darwin-arm64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4.json)

### vs. 3.10.4

- Geometric mean: 1.253x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250307-darwin-arm64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.10.4.md)
- [📈time plot](bm-20250307-darwin-arm64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.014x slower (HPT: reliability of 97.94%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250307-darwin-arm64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.12.0.md)
- [📈time plot](bm-20250307-darwin-arm64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.011x slower (HPT: reliability of 69.96%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250307-darwin-arm64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.13.0.md)
- [📈time plot](bm-20250307-darwin-arm64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 64.09%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20250307-darwin-arm64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-base-mem.svg)
- [📄table](bm-20250307-darwin-arm64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-base.md)
- [📈time plot](bm-20250307-darwin-arm64-faster%252dcpython-use_stackrefs_single-3.14.0a5%2B-916faf4-vs-base.svg)


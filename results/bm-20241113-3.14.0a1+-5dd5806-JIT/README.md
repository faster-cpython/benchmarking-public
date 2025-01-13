# Results

- fork: brandtbucher/jump_backoff
- version: 3.14.0a1+
- config: JIT
- commit hash: [5dd5806](https://github.com/brandtbucher/cpython/commit/5dd5806)
- commit date: 2024-11-13T17:18:19-08:00
- commit merge base: [c695e37a3f95c225ee08d1e882d23fa200b5ec34](https://github.com/python/cpython/commit/c695e37a3f95c225ee08d1e882d23fa200b5ec34)
- ref: jump_backoff

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11828918805)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806.json)

### vs. 3.10.4

- Geometric mean: 1.189x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.10.4.md)
- [📈time plot](bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.066x slower (HPT: reliability of 99.99%, 1.02x slower at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.12.0.md)
- [📈time plot](bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.078x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.13.0.md)
- [📈time plot](bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.021x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: 0.96x
- [🧠memory plot](bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-base-mem.svg)
- [📄table](bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-base.md)
- [📈time plot](bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241113-azure-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-pystats.json)
- [pystats table](bm-20241113-azure-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-pystats.md)

### vs. base

- [pystats diff](bm-20241113-azure-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11828918805)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806.json)

### vs. 3.10.4

- Geometric mean: 1.396x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.10.4.md)
- [📈time plot](bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.066x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.12.0.md)
- [📈time plot](bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.004x faster (HPT: reliability of 79.05%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.13.0.md)
- [📈time plot](bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.012x faster (HPT: reliability of 98.94%, 1.00x faster at 99th %ile)
- Memory usage: 0.97x
- [🧠memory plot](bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-base-mem.svg)
- [📄table](bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-base.md)
- [📈time plot](bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11828918805)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806.json)

### vs. 3.10.4

- Geometric mean: 1.220x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.10.4.md)
- [📈time plot](bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.030x faster (HPT: reliability of 90.36%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.12.0.md)
- [📈time plot](bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.007x faster (HPT: reliability of 92.90%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, many_optionals, sqlalchemy_declarative, sqlalchemy_imperative, subparsers, tornado_http
- [📄table](bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.13.0.md)
- [📈time plot](bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.012x faster (HPT: reliability of 97.62%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-base.md)
- [📈time plot](bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11828918805)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806.json)

### vs. 3.10.4

- Geometric mean: 1.230x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, many_optionals, subparsers, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.10.4.md)
- [📈time plot](bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.030x faster (HPT: reliability of 99.26%, 1.00x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.12.0.md)
- [📈time plot](bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x faster (HPT: reliability of 98.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.13.0.md)
- [📈time plot](bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.012x faster (HPT: reliability of 99.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.95x
- [🧠memory plot](bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-base-mem.svg)
- [📄table](bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-base.md)
- [📈time plot](bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1%2B-5dd5806-vs-base.svg)


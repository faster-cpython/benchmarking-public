# Results

- fork: python/d05053a203d922c8056f
- version: 3.14.0a4+
- config: CLANG
- commit hash: [d05053a](https://github.com/python/cpython/commit/d05053a)
- commit date: 2025-02-09T21:48:11+00:00
- commit merge base: [cda83cade0b684bcb1221a30bfe0b6861abd3b3f](https://github.com/python/cpython/commit/cda83cade0b684bcb1221a30bfe0b6861abd3b3f)
- ref: d05053a203d922c8056f

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13313002500)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250209-linux-x86_64-python-d05053a203d922c8056f-3.14.0a4%2B-d05053a.json)

### vs. 3.10.4

- Geometric mean: 1.497x faster (HPT: reliability of 100.00%, 1.37x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250209-linux-x86_64-python-d05053a203d922c8056f-3.14.0a4%2B-d05053a-vs-3.10.4.md)
- [📈time plot](bm-20250209-linux-x86_64-python-d05053a203d922c8056f-3.14.0a4%2B-d05053a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.147x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250209-linux-x86_64-python-d05053a203d922c8056f-3.14.0a4%2B-d05053a-vs-3.12.0.md)
- [📈time plot](bm-20250209-linux-x86_64-python-d05053a203d922c8056f-3.14.0a4%2B-d05053a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.076x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250209-linux-x86_64-python-d05053a203d922c8056f-3.14.0a4%2B-d05053a-vs-3.13.0.md)
- [📈time plot](bm-20250209-linux-x86_64-python-d05053a203d922c8056f-3.14.0a4%2B-d05053a-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13313006911)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4%2B-d05053a.json)

### vs. 3.10.4

- Geometric mean: 1.481x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4%2B-d05053a-vs-3.10.4.md)
- [📈time plot](bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4%2B-d05053a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.161x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4%2B-d05053a-vs-3.12.0.md)
- [📈time plot](bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4%2B-d05053a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.165x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4%2B-d05053a-vs-3.13.0.md)
- [📈time plot](bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4%2B-d05053a-vs-3.13.0.svg)


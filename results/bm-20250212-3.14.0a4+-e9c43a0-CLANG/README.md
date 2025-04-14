# Results

- fork: mdboom/early_tail_call_load
- version: 3.14.0a4+
- config: 
- commit hash: [e9c43a0](https://github.com/mdboom/cpython/commit/e9c43a0)
- commit date: 2025-02-12T17:09:18-06:00
- commit merge base: [d05053a203d922c8056f12ef3c9338229fdce043](https://github.com/python/cpython/commit/d05053a203d922c8056f12ef3c9338229fdce043)
- ref: early_tail_call_load

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13313002500)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0.json)

### vs. 3.10.4

- Geometric mean: 1.510x faster (HPT: reliability of 100.00%, 1.38x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.10.4.md)
- [📈time plot](bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.157x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.12.0.md)
- [📈time plot](bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.086x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.13.0.md)
- [📈time plot](bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.008x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-base-mem.svg)
- [📄table](bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-base.md)
- [📈time plot](bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13313006911)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0.json)

### vs. 3.10.4

- Geometric mean: 1.479x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.10.4.md)
- [📈time plot](bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.160x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.12.0.md)
- [📈time plot](bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.164x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.13.0.md)
- [📈time plot](bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 99.66%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-base-mem.svg)
- [📄table](bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-base.md)
- [📈time plot](bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-base.svg)


# Results

- fork: Fidget-Spinner/grand_unified_tailca
- version: 3.14.0a5+
- config: JIT
- commit hash: [d07479b](https://github.com/Fidget%2dSpinner/cpython/commit/d07479b)
- commit date: 2025-02-13T02:47:37+08:00
- commit merge base: [1b27f36eb0ef146aa60b261a1cffcc6fd55c0e88](https://github.com/python/cpython/commit/1b27f36eb0ef146aa60b261a1cffcc6fd55c0e88)
- ref: grand_unified_tailca

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13309147339)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250213-linux-x86_64-Fidget%252dSpinner-grand_unified_tailca-3.14.0a5%2B-d07479b.json)

### vs. 3.10.4

- Geometric mean: 1.485x faster (HPT: reliability of 100.00%, 1.34x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250213-linux-x86_64-Fidget%252dSpinner-grand_unified_tailca-3.14.0a5%2B-d07479b-vs-3.10.4.md)
- [📈time plot](bm-20250213-linux-x86_64-Fidget%252dSpinner-grand_unified_tailca-3.14.0a5%2B-d07479b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.138x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250213-linux-x86_64-Fidget%252dSpinner-grand_unified_tailca-3.14.0a5%2B-d07479b-vs-3.12.0.md)
- [📈time plot](bm-20250213-linux-x86_64-Fidget%252dSpinner-grand_unified_tailca-3.14.0a5%2B-d07479b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.067x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250213-linux-x86_64-Fidget%252dSpinner-grand_unified_tailca-3.14.0a5%2B-d07479b-vs-3.13.0.md)
- [📈time plot](bm-20250213-linux-x86_64-Fidget%252dSpinner-grand_unified_tailca-3.14.0a5%2B-d07479b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 97.99%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250213-linux-x86_64-Fidget%252dSpinner-grand_unified_tailca-3.14.0a5%2B-d07479b-vs-base-mem.svg)
- [📄table](bm-20250213-linux-x86_64-Fidget%252dSpinner-grand_unified_tailca-3.14.0a5%2B-d07479b-vs-base.md)
- [📈time plot](bm-20250213-linux-x86_64-Fidget%252dSpinner-grand_unified_tailca-3.14.0a5%2B-d07479b-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13309151630)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250213-darwin-arm64-Fidget%252dSpinner-grand_unified_tailca-3.14.0a5%2B-d07479b.json)

### vs. 3.10.4

- Geometric mean: 1.436x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250213-darwin-arm64-Fidget%252dSpinner-grand_unified_tailca-3.14.0a5%2B-d07479b-vs-3.10.4.md)
- [📈time plot](bm-20250213-darwin-arm64-Fidget%252dSpinner-grand_unified_tailca-3.14.0a5%2B-d07479b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.128x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250213-darwin-arm64-Fidget%252dSpinner-grand_unified_tailca-3.14.0a5%2B-d07479b-vs-3.12.0.md)
- [📈time plot](bm-20250213-darwin-arm64-Fidget%252dSpinner-grand_unified_tailca-3.14.0a5%2B-d07479b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.132x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250213-darwin-arm64-Fidget%252dSpinner-grand_unified_tailca-3.14.0a5%2B-d07479b-vs-3.13.0.md)
- [📈time plot](bm-20250213-darwin-arm64-Fidget%252dSpinner-grand_unified_tailca-3.14.0a5%2B-d07479b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250213-darwin-arm64-Fidget%252dSpinner-grand_unified_tailca-3.14.0a5%2B-d07479b-vs-base-mem.svg)
- [📄table](bm-20250213-darwin-arm64-Fidget%252dSpinner-grand_unified_tailca-3.14.0a5%2B-d07479b-vs-base.md)
- [📈time plot](bm-20250213-darwin-arm64-Fidget%252dSpinner-grand_unified_tailca-3.14.0a5%2B-d07479b-vs-base.svg)


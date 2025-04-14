# Results

- fork: diegorusso/aarch64_trampolines
- version: 3.14.0a5+
- config: JIT
- commit hash: [efdef5f](https://github.com/diegorusso/cpython/commit/efdef5f)
- commit date: 2025-03-10T12:05:48+00:00
- commit merge base: [98fa4a49fecbac3c990a25ce5d300592dad31be0](https://github.com/python/cpython/commit/98fa4a49fecbac3c990a25ce5d300592dad31be0)
- ref: aarch64_trampolines

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13775256285)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5%2B-efdef5f.json)

### vs. 3.10.4

- Geometric mean: 1.301x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5%2B-efdef5f-vs-3.10.4.md)
- [📈time plot](bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5%2B-efdef5f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.031x faster (HPT: reliability of 97.64%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5%2B-efdef5f-vs-3.12.0.md)
- [📈time plot](bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5%2B-efdef5f-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.031x faster (HPT: reliability of 98.77%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5%2B-efdef5f-vs-3.13.0.md)
- [📈time plot](bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5%2B-efdef5f-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x slower (HPT: reliability of 99.97%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5%2B-efdef5f-vs-base-mem.svg)
- [📄table](bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5%2B-efdef5f-vs-base.md)
- [📈time plot](bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5%2B-efdef5f-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13774834929)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5%2B-efdef5f.json)

### vs. 3.10.4

- Geometric mean: 1.389x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5%2B-efdef5f-vs-3.10.4.md)
- [📈time plot](bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5%2B-efdef5f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.093x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5%2B-efdef5f-vs-3.12.0.md)
- [📈time plot](bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5%2B-efdef5f-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.094x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5%2B-efdef5f-vs-3.13.0.md)
- [📈time plot](bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5%2B-efdef5f-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.008x faster (HPT: reliability of 99.97%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- [🧠memory plot](bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5%2B-efdef5f-vs-base-mem.svg)
- [📄table](bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5%2B-efdef5f-vs-base.md)
- [📈time plot](bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5%2B-efdef5f-vs-base.svg)


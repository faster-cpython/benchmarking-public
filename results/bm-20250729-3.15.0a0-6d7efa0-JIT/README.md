# Results

- fork: brandtbucher/macos_10_15
- version: 3.15.0a0
- config: JIT
- commit hash: [6d7efa0](https://github.com/brandtbucher/cpython/commit/6d7efa0)
- commit date: 2025-07-29T09:10:56-07:00
- commit merge base: [0b4e13c2658c5a267fc50ee045ffb7b6408b2e3b](https://github.com/python/cpython/commit/0b4e13c2658c5a267fc50ee045ffb7b6408b2e3b)
- ref: macos_10_15

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16601537596)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0.json)

### vs. 3.10.4

- Geometric mean: 1.348x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0-vs-3.10.4.md)
- [📈time plot](bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.063x faster (HPT: reliability of 99.81%, 1.01x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0-vs-3.12.0.md)
- [📈time plot](bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.065x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0-vs-3.13.0.md)
- [📈time plot](bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0-vs-base-mem.svg)
- [📄table](bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0-vs-base.md)
- [📈time plot](bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0-vs-base.svg)


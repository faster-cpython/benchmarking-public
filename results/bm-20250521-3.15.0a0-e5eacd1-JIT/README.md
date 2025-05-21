# Results

- fork: brandtbucher/macos_10_15
- version: 3.15.0a0
- config: JIT
- commit hash: [e5eacd1](https://github.com/brandtbucher/cpython/commit/e5eacd1)
- commit date: 2025-05-21T11:40:54-04:00
- commit merge base: [1298511b41ec0f9be925c12f3830e94fe8f7e7dc](https://github.com/python/cpython/commit/1298511b41ec0f9be925c12f3830e94fe8f7e7dc)
- ref: macos_10_15

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15166592358)
- cpu model: missing
- platform: macOS-15.4.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1.json)

### vs. 3.10.4

- Geometric mean: 1.273x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1-vs-3.10.4.md)
- [📈time plot](bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.011x faster (HPT: reliability of 99.21%, 1.00x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1-vs-3.12.0.md)
- [📈time plot](bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.013x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1-vs-3.13.0.md)
- [📈time plot](bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 99.69%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1-vs-base-mem.svg)
- [📄table](bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1-vs-base.md)
- [📈time plot](bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1-vs-base.svg)


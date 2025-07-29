# Results

- fork: python/0b4e13c2658c5a267fc5
- version: 3.15.0a0
- config: JIT
- commit hash: [0b4e13c](https://github.com/python/cpython/commit/0b4e13c)
- commit date: 2025-07-29T17:23:44+02:00
- commit merge base: [11a8652e25341e696b06d8dc7a18e8c3ee8059e4](https://github.com/python/cpython/commit/11a8652e25341e696b06d8dc7a18e8c3ee8059e4)
- ref: 0b4e13c2658c5a267fc5

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16601537596)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250729-darwin-arm64-python-0b4e13c2658c5a267fc5-3.15.0a0-0b4e13c.json)

### vs. 3.10.4

- Geometric mean: 1.352x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250729-darwin-arm64-python-0b4e13c2658c5a267fc5-3.15.0a0-0b4e13c-vs-3.10.4.md)
- [📈time plot](bm-20250729-darwin-arm64-python-0b4e13c2658c5a267fc5-3.15.0a0-0b4e13c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.066x faster (HPT: reliability of 99.91%, 1.01x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250729-darwin-arm64-python-0b4e13c2658c5a267fc5-3.15.0a0-0b4e13c-vs-3.12.0.md)
- [📈time plot](bm-20250729-darwin-arm64-python-0b4e13c2658c5a267fc5-3.15.0a0-0b4e13c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.068x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250729-darwin-arm64-python-0b4e13c2658c5a267fc5-3.15.0a0-0b4e13c-vs-3.13.0.md)
- [📈time plot](bm-20250729-darwin-arm64-python-0b4e13c2658c5a267fc5-3.15.0a0-0b4e13c-vs-3.13.0.svg)


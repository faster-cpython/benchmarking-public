# Results

- fork: python/b150b6aca7b17efe1bb1
- version: 3.15.0a0
- config: 
- commit hash: [b150b6a](https://github.com/python/cpython/commit/b150b6a)
- commit date: 2025-06-09T18:33:18+08:00
- commit merge base: [c19e36cc4eabacaacc359e8b2550b10c2965a31a](https://github.com/python/cpython/commit/c19e36cc4eabacaacc359e8b2550b10c2965a31a)
- ref: b150b6aca7b17efe1bb1

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15534208033)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a.json)

### vs. 3.10.4

- Geometric mean: 1.154x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.10.4.md)
- [📈time plot](bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.083x slower (HPT: reliability of 98.60%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.12.0.md)
- [📈time plot](bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.082x slower (HPT: reliability of 87.04%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.13.0.md)
- [📈time plot](bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.13.0.svg)


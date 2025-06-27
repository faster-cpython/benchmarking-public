# Results

- fork: python/7cc89496922b7edb033e
- version: 3.15.0a0
- config: JIT
- commit hash: [7cc8949](https://github.com/python/cpython/commit/7cc8949)
- commit date: 2025-06-19T16:47:35+02:00
- commit merge base: [0243260284d3630d58a11694904476349d14a6ed](https://github.com/python/cpython/commit/0243260284d3630d58a11694904476349d14a6ed)
- ref: 7cc89496922b7edb033e

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15924470342)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949.json)

### vs. 3.10.4

- Geometric mean: 1.266x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949-vs-3.10.4.md)
- [📈time plot](bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.000x slower (HPT: reliability of 87.88%, 1.00x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949-vs-3.12.0.md)
- [📈time plot](bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.001x faster (HPT: reliability of 58.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949-vs-3.13.0.md)
- [📈time plot](bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.013x faster (HPT: reliability of 97.14%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949-vs-base-mem.svg)
- [📄table](bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949-vs-base.md)
- [📈time plot](bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949-vs-base.svg)


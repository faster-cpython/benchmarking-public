# Results

- fork: faster-cpython/explicit_check_perio
- version: 3.15.0a0
- config: JIT
- commit hash: [892a89d](https://github.com/faster%2dcpython/cpython/commit/892a89d)
- commit date: 2025-06-26T15:14:32+01:00
- commit merge base: [7cc89496922b7edb033e2ed47550c7c9e2ae8525](https://github.com/python/cpython/commit/7cc89496922b7edb033e2ed47550c7c9e2ae8525)
- ref: explicit_check_perio

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15924470342)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250626-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-892a89d.json)

### vs. 3.10.4

- Geometric mean: 1.383x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250626-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-892a89d-vs-3.10.4.md)
- [📈time plot](bm-20250626-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-892a89d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.091x faster (HPT: reliability of 99.94%, 1.01x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250626-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-892a89d-vs-3.12.0.md)
- [📈time plot](bm-20250626-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-892a89d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.093x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250626-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-892a89d-vs-3.13.0.md)
- [📈time plot](bm-20250626-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-892a89d-vs-3.13.0.svg)


# Results

- fork: faster-cpython/use_ob_flags_for_gc
- version: 3.15.0a0
- config: 
- commit hash: [53e0c51](https://github.com/faster%2dcpython/cpython/commit/53e0c51)
- commit date: 2025-07-10T14:08:22+01:00
- commit merge base: [c17654334946b232aa296696cf70ec93a09d8156](https://github.com/python/cpython/commit/c17654334946b232aa296696cf70ec93a09d8156)
- ref: use_ob_flags_for_gc

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16196041824)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250710-darwin-arm64-faster%252dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51.json)

### vs. 3.10.4

- Geometric mean: 1.245x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250710-darwin-arm64-faster%252dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51-vs-3.10.4.md)
- [📈time plot](bm-20250710-darwin-arm64-faster%252dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.017x slower (HPT: reliability of 97.13%, 1.00x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250710-darwin-arm64-faster%252dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51-vs-3.12.0.md)
- [📈time plot](bm-20250710-darwin-arm64-faster%252dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.015x slower (HPT: reliability of 79.50%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250710-darwin-arm64-faster%252dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51-vs-3.13.0.md)
- [📈time plot](bm-20250710-darwin-arm64-faster%252dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.006x slower (HPT: reliability of 99.96%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250710-darwin-arm64-faster%252dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51-vs-base-mem.svg)
- [📄table](bm-20250710-darwin-arm64-faster%252dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51-vs-base.md)
- [📈time plot](bm-20250710-darwin-arm64-faster%252dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51-vs-base.svg)


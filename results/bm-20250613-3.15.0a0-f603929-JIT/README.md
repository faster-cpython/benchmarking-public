# Results

- fork: faster-cpython/tier_2_tos_caching
- version: 3.15.0a0
- config: JIT
- commit hash: [f603929](https://github.com/faster%2dcpython/cpython/commit/f603929)
- commit date: 2025-06-13T12:39:39+01:00
- commit merge base: [e6c3039cb39e68ae9af9ddcaca341c5af8f9cf23](https://github.com/python/cpython/commit/e6c3039cb39e68ae9af9ddcaca341c5af8f9cf23)
- ref: tier_2_tos_caching

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15633696543)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250613-darwin-arm64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-f603929.json)

### vs. 3.10.4

- Geometric mean: 1.174x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250613-darwin-arm64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-f603929-vs-3.10.4.md)
- [📈time plot](bm-20250613-darwin-arm64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-f603929-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.067x slower (HPT: reliability of 88.54%, 1.00x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250613-darwin-arm64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-f603929-vs-3.12.0.md)
- [📈time plot](bm-20250613-darwin-arm64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-f603929-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.065x slower (HPT: reliability of 50.89%, 1.00x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250613-darwin-arm64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-f603929-vs-3.13.0.md)
- [📈time plot](bm-20250613-darwin-arm64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-f603929-vs-3.13.0.svg)


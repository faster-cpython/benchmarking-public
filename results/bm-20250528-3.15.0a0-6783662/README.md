# Results

- fork: faster-cpython/specialize_for_iter_
- version: 3.15.0a0
- config: 
- commit hash: [6783662](https://github.com/faster%2dcpython/cpython/commit/6783662)
- commit date: 2025-05-28T10:11:48+01:00
- commit merge base: [f6f4e8a6622d556641799b02aed7ac018d878cdc](https://github.com/python/cpython/commit/f6f4e8a6622d556641799b02aed7ac018d878cdc)
- ref: specialize_for_iter_

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15295821692)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250528-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-6783662.json)

### vs. 3.10.4

- Geometric mean: 1.151x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250528-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-6783662-vs-3.10.4.md)
- [📈time plot](bm-20250528-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-6783662-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.085x slower (HPT: reliability of 98.83%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250528-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-6783662-vs-3.12.0.md)
- [📈time plot](bm-20250528-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-6783662-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.084x slower (HPT: reliability of 90.81%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250528-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-6783662-vs-3.13.0.md)
- [📈time plot](bm-20250528-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-6783662-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 72.82%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250528-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-6783662-vs-base-mem.svg)
- [📄table](bm-20250528-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-6783662-vs-base.md)
- [📈time plot](bm-20250528-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-6783662-vs-base.svg)


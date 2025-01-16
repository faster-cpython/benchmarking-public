# Results

- fork: python/313b96eb8b8d0ad3bac5
- version: 3.14.0a4+
- config: CLANG
- commit hash: [313b96e](https://github.com/python/cpython/commit/313b96e)
- commit date: 2025-01-16T11:17:03+01:00
- commit merge base: [d05140f9f77d7dfc753dd1e5ac3a5962aaa03eff](https://github.com/python/cpython/commit/d05140f9f77d7dfc753dd1e5ac3a5962aaa03eff)
- ref: 313b96eb8b8d0ad3bac5

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12811331877)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e.json)

### vs. 3.10.4

- Geometric mean: 1.310x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.10.4.md)
- [📈time plot](bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.048x faster (HPT: reliability of 93.13%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.12.0.md)
- [📈time plot](bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.051x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.13.0.md)
- [📈time plot](bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.13.0.svg)


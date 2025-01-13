# Results

- fork: python/main
- version: 3.14.0a3+
- config: 
- commit hash: [4c14f03](https://github.com/python/cpython/commit/4c14f03)
- commit date: 2025-01-03T15:51:22+01:00
- commit merge base: [1c9b0204796ddeaee710646871a4404b4cda1f1b](https://github.com/python/cpython/commit/1c9b0204796ddeaee710646871a4404b4cda1f1b)
- ref: main

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12599766188)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250103-darwin-arm64-python-main-3.14.0a3%2B-4c14f03.json)

### vs. 3.10.4

- Geometric mean: 1.309x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, mypy2
- [📄table](bm-20250103-darwin-arm64-python-main-3.14.0a3%2B-4c14f03-vs-3.10.4.md)
- [📈time plot](bm-20250103-darwin-arm64-python-main-3.14.0a3%2B-4c14f03-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.102x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250103-darwin-arm64-python-main-3.14.0a3%2B-4c14f03-vs-3.12.0.md)
- [📈time plot](bm-20250103-darwin-arm64-python-main-3.14.0a3%2B-4c14f03-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.118x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250103-darwin-arm64-python-main-3.14.0a3%2B-4c14f03-vs-3.13.0.md)
- [📈time plot](bm-20250103-darwin-arm64-python-main-3.14.0a3%2B-4c14f03-vs-3.13.0.svg)


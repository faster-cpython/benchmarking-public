# Results

- fork: python/3829104ab412a47bf3f3
- version: 3.14.0a4+
- config: NOGIL
- commit hash: [3829104](https://github.com/python/cpython/commit/3829104)
- commit date: 2025-01-17T16:49:16-08:00
- commit merge base: [8174770d311ba09c07a47cc3ae90a1db2e7d7708](https://github.com/python/cpython/commit/8174770d311ba09c07a47cc3ae90a1db2e7d7708)
- ref: 3829104ab412a47bf3f3

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12939809594)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250117-darwin-arm64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104.json)

### vs. 3.10.4

- Geometric mean: 1.295x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250117-darwin-arm64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.10.4.md)
- [📈time plot](bm-20250117-darwin-arm64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.040x faster (HPT: reliability of 63.32%, 1.00x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250117-darwin-arm64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.12.0.md)
- [📈time plot](bm-20250117-darwin-arm64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.044x faster (HPT: reliability of 98.38%, 1.00x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250117-darwin-arm64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.13.0.md)
- [📈time plot](bm-20250117-darwin-arm64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.13.0.svg)


# Results

- fork: python/3dd3675492a3fc3b7996
- version: 3.14.0a5+
- config: 
- commit hash: [3dd3675](https://github.com/python/cpython/commit/3dd3675)
- commit date: 2025-03-04T17:05:20+00:00
- commit merge base: [885c3d126f39711971d84a2dee04c19df8a301e4](https://github.com/python/cpython/commit/885c3d126f39711971d84a2dee04c19df8a301e4)
- ref: 3dd3675492a3fc3b7996

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13660055920)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250304-darwin-arm64-python-3dd3675492a3fc3b7996-3.14.0a5%2B-3dd3675.json)

### vs. 3.10.4

- Geometric mean: 1.255x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250304-darwin-arm64-python-3dd3675492a3fc3b7996-3.14.0a5%2B-3dd3675-vs-3.10.4.md)
- [📈time plot](bm-20250304-darwin-arm64-python-3dd3675492a3fc3b7996-3.14.0a5%2B-3dd3675-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.013x slower (HPT: reliability of 98.76%, 1.00x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250304-darwin-arm64-python-3dd3675492a3fc3b7996-3.14.0a5%2B-3dd3675-vs-3.12.0.md)
- [📈time plot](bm-20250304-darwin-arm64-python-3dd3675492a3fc3b7996-3.14.0a5%2B-3dd3675-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.010x slower (HPT: reliability of 71.48%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250304-darwin-arm64-python-3dd3675492a3fc3b7996-3.14.0a5%2B-3dd3675-vs-3.13.0.md)
- [📈time plot](bm-20250304-darwin-arm64-python-3dd3675492a3fc3b7996-3.14.0a5%2B-3dd3675-vs-3.13.0.svg)


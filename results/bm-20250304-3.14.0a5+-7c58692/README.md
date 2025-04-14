# Results

- fork: mdboom/aa_test_20250304
- version: 3.14.0a5+
- config: 
- commit hash: [7c58692](https://github.com/mdboom/cpython/commit/7c58692)
- commit date: 2025-03-04T13:06:27-05:00
- commit merge base: [3dd3675492a3fc3b7996613ef75a9044ee7449b0](https://github.com/python/cpython/commit/3dd3675492a3fc3b7996613ef75a9044ee7449b0)
- ref: aa_test_20250304

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13660055920)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5%2B-7c58692.json)

### vs. 3.10.4

- Geometric mean: 1.251x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5%2B-7c58692-vs-3.10.4.md)
- [📈time plot](bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5%2B-7c58692-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.016x slower (HPT: reliability of 99.56%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5%2B-7c58692-vs-3.12.0.md)
- [📈time plot](bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5%2B-7c58692-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.013x slower (HPT: reliability of 86.64%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5%2B-7c58692-vs-3.13.0.md)
- [📈time plot](bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5%2B-7c58692-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5%2B-7c58692-vs-base-mem.svg)
- [📄table](bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5%2B-7c58692-vs-base.md)
- [📈time plot](bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5%2B-7c58692-vs-base.svg)


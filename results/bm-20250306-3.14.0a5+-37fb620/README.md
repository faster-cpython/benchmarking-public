# Results

- fork: Fidget-Spinner/clang_hot
- version: 3.14.0a5+
- config: 
- commit hash: [37fb620](https://github.com/Fidget%2dSpinner/cpython/commit/37fb620)
- commit date: 2025-03-06T03:29:24+08:00
- commit merge base: [d7bb7c781771650a4edcdee9dfd1ab9c4083e9fd](https://github.com/python/cpython/commit/d7bb7c781771650a4edcdee9dfd1ab9c4083e9fd)
- ref: clang_hot

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13703177280)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250306-darwin-arm64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620.json)

### vs. 3.10.4

- Geometric mean: 1.254x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250306-darwin-arm64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.10.4.md)
- [📈time plot](bm-20250306-darwin-arm64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.014x slower (HPT: reliability of 99.16%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250306-darwin-arm64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.12.0.md)
- [📈time plot](bm-20250306-darwin-arm64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.011x slower (HPT: reliability of 70.90%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250306-darwin-arm64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.13.0.md)
- [📈time plot](bm-20250306-darwin-arm64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 99.40%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250306-darwin-arm64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-base-mem.svg)
- [📄table](bm-20250306-darwin-arm64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-base.md)
- [📈time plot](bm-20250306-darwin-arm64-Fidget%252dSpinner-clang_hot-3.14.0a5%2B-37fb620-vs-base.svg)


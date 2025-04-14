# Results

- fork: python/d7bb7c781771650a4edc
- version: 3.14.0a5+
- config: 
- commit hash: [d7bb7c7](https://github.com/python/cpython/commit/d7bb7c7)
- commit date: 2025-03-05T10:42:09-08:00
- commit merge base: [2904ec2273762df58645a8e245b2281884855b8c](https://github.com/python/cpython/commit/2904ec2273762df58645a8e245b2281884855b8c)
- ref: d7bb7c781771650a4edc

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13703177280)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5%2B-d7bb7c7.json)

### vs. 3.10.4

- Geometric mean: 1.257x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5%2B-d7bb7c7-vs-3.10.4.md)
- [📈time plot](bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5%2B-d7bb7c7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.011x slower (HPT: reliability of 98.92%, 1.00x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5%2B-d7bb7c7-vs-3.12.0.md)
- [📈time plot](bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5%2B-d7bb7c7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.009x slower (HPT: reliability of 68.17%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5%2B-d7bb7c7-vs-3.13.0.md)
- [📈time plot](bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5%2B-d7bb7c7-vs-3.13.0.svg)


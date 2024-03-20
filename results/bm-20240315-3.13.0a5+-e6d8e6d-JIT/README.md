# Results

- fork: brandtbucher
- version: 3.13.0a5+
- tier 2: False
- jit: True
- commit hash: [e6d8e6d](https://github.com/brandtbucher/cpython/commit/e6d8e6d)
- commit date: 2024-03-15T12:47:40-07:00
- commit merge base: [8c094c3095feb4de2efebd00f67fb6cc3b2bc240](https://github.com/brandtbucher/cpython/commit/8c094c3095feb4de2efebd00f67fb6cc3b2bc240)
- ref: justin_mprotect

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8359478706)
- cpu model: missing
- platform: macOS-14.4-arm64-arm-64bit-Mach-O
- [raw results](bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5%2B-e6d8e6d.json)

### vs. 3.10.4

- Geometric mean: 1.15x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.61x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5%2B-e6d8e6d-vs-3.10.4.md)
- [📈time plot](bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5%2B-e6d8e6d-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.48x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg
- [📄table](bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5%2B-e6d8e6d-vs-3.11.0.md)
- [📈time plot](bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5%2B-e6d8e6d-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.04x slower (HPT: reliability of 99.83%, 1.00x slower at 99th %ile)
- Memory usage: 1.43x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5%2B-e6d8e6d-vs-3.12.0.md)
- [📈time plot](bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5%2B-e6d8e6d-vs-3.12.0.png)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.80x
- [🧠memory plot](bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5%2B-e6d8e6d-vs-base-mem.png)
- [📄table](bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5%2B-e6d8e6d-vs-base.md)
- [📈time plot](bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5%2B-e6d8e6d-vs-base.png)


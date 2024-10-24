# Results

- fork: Yhg1s
- version: 3.13.0rc2+
- config: 
- commit hash: [1ba3555](https://github.com/Yhg1s/cpython/commit/1ba3555)
- commit date: 2024-09-30T02:49:23+02:00
- ref: 3.13_revert_incremen

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11112544532)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: dulwich_log, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.10.4.md)
- [📈time plot](bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 88.63%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: dulwich_log, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, flaskblogging, unpack_sequence
- [📄table](bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.12.0.md)
- [📈time plot](bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.00x slower (HPT: reliability of 71.73%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [📄table](bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.13.0.md)
- [📈time plot](bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.13.0b2.md)
- [📈time plot](bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11112544532)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.10.4.md)
- [📈time plot](bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x slower (HPT: reliability of 56.82%, 1.00x slower at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.12.0.md)
- [📈time plot](bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.00x slower (HPT: reliability of 99.45%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [📄table](bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.13.0.md)
- [📈time plot](bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.13.0b2.md)
- [📈time plot](bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11112544532)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555.json)

### vs. 3.10.4

- Geometric mean: 1.17x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 0.58x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.10.4.md)
- [📈time plot](bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x faster (HPT: reliability of 63.36%, 1.00x slower at 99th %ile)
- Memory usage: 0.51x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.12.0.md)
- [📈time plot](bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 0.98x
- [📄table](bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.13.0.md)
- [📈time plot](bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.13.0b2.md)
- [📈time plot](bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-1ba3555-vs-3.13.0b2.svg)


# Results

- fork: brandtbucher/keep_stack_pointer
- version: 3.14.0a6+
- config: TAILCALL
- commit hash: [b3d84fd](https://github.com/brandtbucher/cpython/commit/b3d84fd)
- commit date: 2025-03-26T14:29:09-07:00
- commit merge base: [4b3d5b604210f68005ef64d5346ca169385f5acf](https://github.com/python/cpython/commit/4b3d5b604210f68005ef64d5346ca169385f5acf)
- ref: keep_stack_pointer

## linux x86_64 (linux_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14121931128)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250326-linux_clang-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6%2B-b3d84fd.json)

### vs. base

- Geometric mean: 1.007x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250326-linux_clang-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6%2B-b3d84fd-vs-base-mem.svg)
- [📄table](bm-20250326-linux_clang-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6%2B-b3d84fd-vs-base.md)
- [📈time plot](bm-20250326-linux_clang-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6%2B-b3d84fd-vs-base.svg)

### vs. 3.10.4

- [📄table](bm-20250326-linux_clang-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6%2B-b3d84fd-vs-3.10.4.md)
- [📈time plot](bm-20250326-linux_clang-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6%2B-b3d84fd-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250326-linux_clang-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6%2B-b3d84fd-vs-3.12.0.md)
- [📈time plot](bm-20250326-linux_clang-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6%2B-b3d84fd-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250326-linux_clang-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6%2B-b3d84fd-vs-3.13.0.md)
- [📈time plot](bm-20250326-linux_clang-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6%2B-b3d84fd-vs-3.13.0.svg)


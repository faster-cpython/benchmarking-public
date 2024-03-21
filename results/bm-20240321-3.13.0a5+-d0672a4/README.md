# Results

- fork: faster-cpython
- version: 3.13.0a5+
- tier 2: False
- jit: False
- commit hash: [d0672a4](https://github.com/faster%2dcpython/cpython/commit/d0672a4)
- commit date: 2024-03-21T12:41:55+00:00
- commit merge base: [6547330f4e896c6748da23704b617e060e6cc68e](https://github.com/faster%2dcpython/cpython/commit/6547330f4e896c6748da23704b617e060e6cc68e)
- ref: fix_gc_counting

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8376571327)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240321-linux-x86_64-faster%252dcpython-fix_gc_counting-3.13.0a5%2B-d0672a4.json)

### vs. 3.10.4

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240321-linux-x86_64-faster%252dcpython-fix_gc_counting-3.13.0a5%2B-d0672a4-vs-3.10.4.md)
- [📈time plot](bm-20240321-linux-x86_64-faster%252dcpython-fix_gc_counting-3.13.0a5%2B-d0672a4-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.07x faster (HPT: reliability of 99.61%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240321-linux-x86_64-faster%252dcpython-fix_gc_counting-3.13.0a5%2B-d0672a4-vs-3.11.0.md)
- [📈time plot](bm-20240321-linux-x86_64-faster%252dcpython-fix_gc_counting-3.13.0a5%2B-d0672a4-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 0.95x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240321-linux-x86_64-faster%252dcpython-fix_gc_counting-3.13.0a5%2B-d0672a4-vs-3.12.0.md)
- [📈time plot](bm-20240321-linux-x86_64-faster%252dcpython-fix_gc_counting-3.13.0a5%2B-d0672a4-vs-3.12.0.png)

### vs. base

- Geometric mean: 1.27x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20240321-linux-x86_64-faster%252dcpython-fix_gc_counting-3.13.0a5%2B-d0672a4-vs-base-mem.png)
- [📄table](bm-20240321-linux-x86_64-faster%252dcpython-fix_gc_counting-3.13.0a5%2B-d0672a4-vs-base.md)
- [📈time plot](bm-20240321-linux-x86_64-faster%252dcpython-fix_gc_counting-3.13.0a5%2B-d0672a4-vs-base.png)


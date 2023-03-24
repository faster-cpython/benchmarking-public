
# Results vs. 3.11.0

- fork: python
- ref: e2b4e4bab90b69fbd361
- machine: linux-x86_64
- commit hash: e2b4e4b
- commit date: 2021-11-05
- overall geometric mean: 1.09x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 274 ms: 1.07x slower                                                  |
| chameleon      | 6.52 ms                                                             | 7.46 ms: 1.14x slower                                                 |
| docutils       | 2.59 sec                                                            | 2.79 sec: 1.08x slower                                                |
| html5lib       | 64.0 ms                                                             | 71.5 ms: 1.12x slower                                                 |
| tornado_http   | 96.7 ms                                                             | 111 ms: 1.14x slower                                                  |
| Geometric mean | (ref)                                                               | 1.11x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 197 ms                                                              | 188 ms: 1.05x faster                                                  |
| float          | 76.0 ms                                                             | 83.3 ms: 1.10x slower                                                 |
| nbody          | 96.7 ms                                                             | 112 ms: 1.16x slower                                                  |
| Geometric mean | (ref)                                                               | 1.07x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.32 ms                                                             | 3.26 ms: 1.02x faster                                                 |
| regex_compile  | 137 ms                                                              | 145 ms: 1.06x slower                                                  |
| regex_v8       | 22.0 ms                                                             | 23.7 ms: 1.08x slower                                                 |
| regex_dna      | 196 ms                                                              | 219 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                               | 1.06x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_dict          | 30.9 us                                                             | 28.6 us: 1.08x faster                                                 |
| xml_etree_parse      | 162 ms                                                              | 158 ms: 1.03x faster                                                  |
| json_dumps           | 12.5 ms                                                             | 12.4 ms: 1.01x faster                                                 |
| json_loads           | 26.2 us                                                             | 25.9 us: 1.01x faster                                                 |
| xml_etree_iterparse  | 108 ms                                                              | 110 ms: 1.03x slower                                                  |
| pickle               | 9.79 us                                                             | 10.1 us: 1.03x slower                                                 |
| unpickle_list        | 4.96 us                                                             | 5.13 us: 1.03x slower                                                 |
| unpickle             | 13.2 us                                                             | 13.7 us: 1.04x slower                                                 |
| xml_etree_generate   | 76.5 ms                                                             | 81.6 ms: 1.07x slower                                                 |
| xml_etree_process    | 54.1 ms                                                             | 59.6 ms: 1.10x slower                                                 |
| pickle_list          | 4.03 us                                                             | 4.68 us: 1.16x slower                                                 |
| pickle_pure_python   | 307 us                                                              | 364 us: 1.19x slower                                                  |
| unpickle_pure_python | 228 us                                                              | 271 us: 1.19x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.05x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 5.98 ms                                                             | 5.77 ms: 1.04x faster                                                 |
| python_startup         | 8.49 ms                                                             | 14.6 ms: 1.71x slower                                                 |
| Geometric mean         | (ref)                                                               | 1.29x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 56.1 ms: 1.08x slower                                                 |
| genshi_text     | 21.8 ms                                                             | 24.6 ms: 1.13x slower                                                 |
| django_template | 32.9 ms                                                             | 37.9 ms: 1.15x slower                                                 |
| mako            | 9.82 ms                                                             | 12.1 ms: 1.23x slower                                                 |
| Geometric mean  | (ref)                                                               | 1.15x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| coverage                | 101 ms                                                              | 75.8 ms: 1.33x faster                                                 |
| generators              | 73.4 ms                                                             | 57.4 ms: 1.28x faster                                                 |
| unpack_sequence         | 49.5 ns                                                             | 43.6 ns: 1.13x faster                                                 |
| pickle_dict             | 30.9 us                                                             | 28.6 us: 1.08x faster                                                 |
| pidigits                | 197 ms                                                              | 188 ms: 1.05x faster                                                  |
| python_startup_no_site  | 5.98 ms                                                             | 5.77 ms: 1.04x faster                                                 |
| xml_etree_parse         | 162 ms                                                              | 158 ms: 1.03x faster                                                  |
| regex_effbot            | 3.32 ms                                                             | 3.26 ms: 1.02x faster                                                 |
| telco                   | 6.59 ms                                                             | 6.50 ms: 1.01x faster                                                 |
| async_tree_none         | 525 ms                                                              | 518 ms: 1.01x faster                                                  |
| json_dumps              | 12.5 ms                                                             | 12.4 ms: 1.01x faster                                                 |
| json_loads              | 26.2 us                                                             | 25.9 us: 1.01x faster                                                 |
| logging_format          | 6.64 us                                                             | 6.71 us: 1.01x slower                                                 |
| json                    | 4.86 ms                                                             | 4.91 ms: 1.01x slower                                                 |
| sympy_sum               | 167 ms                                                              | 170 ms: 1.02x slower                                                  |
| gunicorn                | 1.13 ms                                                             | 1.15 ms: 1.02x slower                                                 |
| xml_etree_iterparse     | 108 ms                                                              | 110 ms: 1.03x slower                                                  |
| pickle                  | 9.79 us                                                             | 10.1 us: 1.03x slower                                                 |
| mdp                     | 2.64 sec                                                            | 2.71 sec: 1.03x slower                                                |
| unpickle_list           | 4.96 us                                                             | 5.13 us: 1.03x slower                                                 |
| unpickle                | 13.2 us                                                             | 13.7 us: 1.04x slower                                                 |
| sqlalchemy_imperative   | 18.0 ms                                                             | 18.8 ms: 1.04x slower                                                 |
| pathlib                 | 18.2 ms                                                             | 19.1 ms: 1.05x slower                                                 |
| sqlalchemy_declarative  | 138 ms                                                              | 145 ms: 1.05x slower                                                  |
| sympy_str               | 291 ms                                                              | 306 ms: 1.05x slower                                                  |
| flaskblogging           | 7.09 ms                                                             | 7.46 ms: 1.05x slower                                                 |
| sympy_integrate         | 21.0 ms                                                             | 22.2 ms: 1.06x slower                                                 |
| regex_compile           | 137 ms                                                              | 145 ms: 1.06x slower                                                  |
| sympy_expand            | 477 ms                                                              | 505 ms: 1.06x slower                                                  |
| spectral_norm           | 99.5 ms                                                             | 106 ms: 1.06x slower                                                  |
| 2to3                    | 257 ms                                                              | 274 ms: 1.07x slower                                                  |
| xml_etree_generate      | 76.5 ms                                                             | 81.6 ms: 1.07x slower                                                 |
| thrift                  | 766 us                                                              | 821 us: 1.07x slower                                                  |
| dulwich_log             | 63.6 ms                                                             | 68.3 ms: 1.07x slower                                                 |
| docutils                | 2.59 sec                                                            | 2.79 sec: 1.08x slower                                                |
| regex_v8                | 22.0 ms                                                             | 23.7 ms: 1.08x slower                                                 |
| genshi_xml              | 51.8 ms                                                             | 56.1 ms: 1.08x slower                                                 |
| scimark_fft             | 328 ms                                                              | 355 ms: 1.08x slower                                                  |
| nqueens                 | 84.0 ms                                                             | 91.4 ms: 1.09x slower                                                 |
| pprint_pformat          | 1.45 sec                                                            | 1.58 sec: 1.09x slower                                                |
| async_tree_memoization  | 621 ms                                                              | 676 ms: 1.09x slower                                                  |
| pprint_safe_repr        | 701 ms                                                              | 763 ms: 1.09x slower                                                  |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.86 ms: 1.09x slower                                                 |
| bench_thread_pool       | 820 us                                                              | 892 us: 1.09x slower                                                  |
| sqlglot_optimize        | 53.4 ms                                                             | 58.4 ms: 1.09x slower                                                 |
| coroutines              | 26.3 ms                                                             | 28.8 ms: 1.09x slower                                                 |
| float                   | 76.0 ms                                                             | 83.3 ms: 1.10x slower                                                 |
| sqlite_synth            | 2.51 us                                                             | 2.76 us: 1.10x slower                                                 |
| async_tree_io           | 1.28 sec                                                            | 1.41 sec: 1.10x slower                                                |
| pycparser               | 1.14 sec                                                            | 1.26 sec: 1.10x slower                                                |
| xml_etree_process       | 54.1 ms                                                             | 59.6 ms: 1.10x slower                                                 |
| sqlglot_normalize       | 108 ms                                                              | 119 ms: 1.10x slower                                                  |
| deepcopy_reduce         | 2.96 us                                                             | 3.27 us: 1.11x slower                                                 |
| deepcopy_memo           | 36.4 us                                                             | 40.4 us: 1.11x slower                                                 |
| async_tree_cpu_io_mixed | 736 ms                                                              | 818 ms: 1.11x slower                                                  |
| regex_dna               | 196 ms                                                              | 219 ms: 1.11x slower                                                  |
| fannkuch                | 384 ms                                                              | 427 ms: 1.11x slower                                                  |
| raytrace                | 292 ms                                                              | 326 ms: 1.12x slower                                                  |
| html5lib                | 64.0 ms                                                             | 71.5 ms: 1.12x slower                                                 |
| deepcopy                | 339 us                                                              | 382 us: 1.13x slower                                                  |
| genshi_text             | 21.8 ms                                                             | 24.6 ms: 1.13x slower                                                 |
| chaos                   | 68.0 ms                                                             | 77.1 ms: 1.13x slower                                                 |
| tornado_http            | 96.7 ms                                                             | 111 ms: 1.14x slower                                                  |
| chameleon               | 6.52 ms                                                             | 7.46 ms: 1.14x slower                                                 |
| hexiom                  | 6.48 ms                                                             | 7.42 ms: 1.15x slower                                                 |
| django_template         | 32.9 ms                                                             | 37.9 ms: 1.15x slower                                                 |
| scimark_monte_carlo     | 67.8 ms                                                             | 78.4 ms: 1.16x slower                                                 |
| nbody                   | 96.7 ms                                                             | 112 ms: 1.16x slower                                                  |
| pickle_list             | 4.03 us                                                             | 4.68 us: 1.16x slower                                                 |
| logging_silent          | 98.7 ns                                                             | 117 ns: 1.18x slower                                                  |
| pickle_pure_python      | 307 us                                                              | 364 us: 1.19x slower                                                  |
| unpickle_pure_python    | 228 us                                                              | 271 us: 1.19x slower                                                  |
| go                      | 138 ms                                                              | 167 ms: 1.21x slower                                                  |
| richards                | 45.7 ms                                                             | 55.7 ms: 1.22x slower                                                 |
| crypto_pyaes            | 73.8 ms                                                             | 90.2 ms: 1.22x slower                                                 |
| mako                    | 9.82 ms                                                             | 12.1 ms: 1.23x slower                                                 |
| scimark_lu              | 108 ms                                                              | 136 ms: 1.26x slower                                                  |
| pyflate                 | 414 ms                                                              | 541 ms: 1.31x slower                                                  |
| deltablue               | 3.66 ms                                                             | 4.86 ms: 1.33x slower                                                 |
| scimark_sor             | 115 ms                                                              | 156 ms: 1.36x slower                                                  |
| sqlglot_transpile       | 1.65 ms                                                             | 2.37 ms: 1.43x slower                                                 |
| sqlglot_parse           | 1.36 ms                                                             | 2.06 ms: 1.51x slower                                                 |
| python_startup          | 8.49 ms                                                             | 14.6 ms: 1.71x slower                                                 |
| Geometric mean          | (ref)                                                               | 1.09x slower                                                          |

Benchmark hidden because not significant (5): pylint, logging_simple, async_generators, bench_mp_pool, meteor_contest
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, djangocms, gc_traversal, mypy2

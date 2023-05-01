
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2d526cd
- commit date: 2023-05-01
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 268 ms: 1.04x slower                                   |
| docutils       | 2.59 sec                                                            | 2.73 sec: 1.06x slower                                 |
| html5lib       | 64.0 ms                                                             | 65.2 ms: 1.02x slower                                  |
| tornado_http   | 96.7 ms                                                             | 99.2 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                               | 1.04x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 88.6 ms: 1.09x faster                                  |
| pidigits       | 197 ms                                                              | 189 ms: 1.04x faster                                   |
| float          | 76.0 ms                                                             | 81.3 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                               | 1.02x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| regex_dna      | 196 ms                                                              | 200 ms: 1.02x slower                                   |
| regex_compile  | 137 ms                                                              | 145 ms: 1.06x slower                                   |
| regex_effbot   | 3.32 ms                                                             | 3.67 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                               | 1.05x slower                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.99 ms: 1.26x faster                                  |
| xml_etree_parse      | 162 ms                                                              | 151 ms: 1.07x faster                                   |
| unpickle_pure_python | 228 us                                                              | 216 us: 1.06x faster                                   |
| xml_etree_iterparse  | 108 ms                                                              | 102 ms: 1.06x faster                                   |
| json_loads           | 26.2 us                                                             | 25.8 us: 1.02x faster                                  |
| unpickle_list        | 4.96 us                                                             | 4.93 us: 1.01x faster                                  |
| pickle_pure_python   | 307 us                                                              | 314 us: 1.02x slower                                   |
| pickle_dict          | 30.9 us                                                             | 31.8 us: 1.03x slower                                  |
| pickle               | 9.79 us                                                             | 10.6 us: 1.08x slower                                  |
| xml_etree_process    | 54.1 ms                                                             | 59.1 ms: 1.09x slower                                  |
| xml_etree_generate   | 76.5 ms                                                             | 84.6 ms: 1.11x slower                                  |
| unpickle             | 13.2 us                                                             | 14.7 us: 1.11x slower                                  |
| pickle_list          | 4.03 us                                                             | 4.51 us: 1.12x slower                                  |
| Geometric mean       | (ref)                                                               | 1.01x slower                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-main-3.12.0a7+-2d526cd |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 9.07 ms: 1.07x slower                                  |
| python_startup_no_site | 5.98 ms                                                             | 6.65 ms: 1.11x slower                                  |
| Geometric mean         | (ref)                                                               | 1.09x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                             | 50.2 ms: 1.03x faster                                  |
| genshi_text    | 21.8 ms                                                             | 22.4 ms: 1.03x slower                                  |
| mako           | 9.82 ms                                                             | 10.8 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                               | 1.03x slower                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-main-3.12.0a7+-2d526cd |
|-------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 30.7 ms: 2.39x faster                                  |
| asyncio_tcp             | 888 ms                                                              | 509 ms: 1.74x faster                                   |
| json_dumps              | 12.5 ms                                                             | 9.99 ms: 1.26x faster                                  |
| mypy2                   | 422 ms                                                              | 351 ms: 1.20x faster                                   |
| coroutines              | 26.3 ms                                                             | 22.1 ms: 1.19x faster                                  |
| nbody                   | 96.7 ms                                                             | 88.6 ms: 1.09x faster                                  |
| xml_etree_parse         | 162 ms                                                              | 151 ms: 1.07x faster                                   |
| async_tree_none         | 525 ms                                                              | 495 ms: 1.06x faster                                   |
| unpickle_pure_python    | 228 us                                                              | 216 us: 1.06x faster                                   |
| xml_etree_iterparse     | 108 ms                                                              | 102 ms: 1.06x faster                                   |
| async_tree_io           | 1.28 sec                                                            | 1.22 sec: 1.05x faster                                 |
| richards                | 45.7 ms                                                             | 43.7 ms: 1.05x faster                                  |
| pidigits                | 197 ms                                                              | 189 ms: 1.04x faster                                   |
| hexiom                  | 6.48 ms                                                             | 6.22 ms: 1.04x faster                                  |
| genshi_xml              | 51.8 ms                                                             | 50.2 ms: 1.03x faster                                  |
| unpack_sequence         | 49.5 ns                                                             | 47.9 ns: 1.03x faster                                  |
| sqlglot_parse           | 1.36 ms                                                             | 1.33 ms: 1.03x faster                                  |
| async_tree_cpu_io_mixed | 736 ms                                                              | 718 ms: 1.02x faster                                   |
| deltablue               | 3.66 ms                                                             | 3.57 ms: 1.02x faster                                  |
| pathlib                 | 18.2 ms                                                             | 17.8 ms: 1.02x faster                                  |
| mdp                     | 2.64 sec                                                            | 2.59 sec: 1.02x faster                                 |
| fannkuch                | 384 ms                                                              | 377 ms: 1.02x faster                                   |
| async_tree_memoization  | 621 ms                                                              | 611 ms: 1.02x faster                                   |
| json_loads              | 26.2 us                                                             | 25.8 us: 1.02x faster                                  |
| go                      | 138 ms                                                              | 137 ms: 1.01x faster                                   |
| create_gc_cycles        | 1.48 ms                                                             | 1.46 ms: 1.01x faster                                  |
| coverage                | 101 ms                                                              | 100 ms: 1.01x faster                                   |
| nqueens                 | 84.0 ms                                                             | 83.4 ms: 1.01x faster                                  |
| unpickle_list           | 4.96 us                                                             | 4.93 us: 1.01x faster                                  |
| json                    | 4.86 ms                                                             | 4.93 ms: 1.02x slower                                  |
| regex_dna               | 196 ms                                                              | 200 ms: 1.02x slower                                   |
| html5lib                | 64.0 ms                                                             | 65.2 ms: 1.02x slower                                  |
| spectral_norm           | 99.5 ms                                                             | 101 ms: 1.02x slower                                   |
| bench_thread_pool       | 820 us                                                              | 836 us: 1.02x slower                                   |
| chaos                   | 68.0 ms                                                             | 69.4 ms: 1.02x slower                                  |
| logging_simple          | 6.09 us                                                             | 6.22 us: 1.02x slower                                  |
| pickle_pure_python      | 307 us                                                              | 314 us: 1.02x slower                                   |
| sqlglot_optimize        | 53.4 ms                                                             | 54.7 ms: 1.03x slower                                  |
| tornado_http            | 96.7 ms                                                             | 99.2 ms: 1.03x slower                                  |
| genshi_text             | 21.8 ms                                                             | 22.4 ms: 1.03x slower                                  |
| pickle_dict             | 30.9 us                                                             | 31.8 us: 1.03x slower                                  |
| sqlglot_normalize       | 108 ms                                                              | 112 ms: 1.03x slower                                   |
| scimark_lu              | 108 ms                                                              | 112 ms: 1.03x slower                                   |
| raytrace                | 292 ms                                                              | 303 ms: 1.04x slower                                   |
| pprint_pformat          | 1.45 sec                                                            | 1.51 sec: 1.04x slower                                 |
| thrift                  | 766 us                                                              | 797 us: 1.04x slower                                   |
| 2to3                    | 257 ms                                                              | 268 ms: 1.04x slower                                   |
| logging_format          | 6.64 us                                                             | 6.93 us: 1.04x slower                                  |
| telco                   | 6.59 ms                                                             | 6.88 ms: 1.04x slower                                  |
| logging_silent          | 98.7 ns                                                             | 104 ns: 1.05x slower                                   |
| comprehensions          | 22.2 us                                                             | 23.4 us: 1.05x slower                                  |
| pprint_safe_repr        | 701 ms                                                              | 738 ms: 1.05x slower                                   |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.71 ms: 1.05x slower                                  |
| deepcopy_memo           | 36.4 us                                                             | 38.4 us: 1.05x slower                                  |
| docutils                | 2.59 sec                                                            | 2.73 sec: 1.06x slower                                 |
| sqlalchemy_imperative   | 18.0 ms                                                             | 19.1 ms: 1.06x slower                                  |
| sqlalchemy_declarative  | 138 ms                                                              | 147 ms: 1.06x slower                                   |
| regex_compile           | 137 ms                                                              | 145 ms: 1.06x slower                                   |
| python_startup          | 8.49 ms                                                             | 9.07 ms: 1.07x slower                                  |
| float                   | 76.0 ms                                                             | 81.3 ms: 1.07x slower                                  |
| scimark_monte_carlo     | 67.8 ms                                                             | 72.6 ms: 1.07x slower                                  |
| deepcopy                | 339 us                                                              | 364 us: 1.07x slower                                   |
| dulwich_log             | 63.6 ms                                                             | 68.3 ms: 1.07x slower                                  |
| sqlite_synth            | 2.51 us                                                             | 2.70 us: 1.07x slower                                  |
| scimark_sor             | 115 ms                                                              | 123 ms: 1.07x slower                                   |
| crypto_pyaes            | 73.8 ms                                                             | 79.7 ms: 1.08x slower                                  |
| pickle                  | 9.79 us                                                             | 10.6 us: 1.08x slower                                  |
| deepcopy_reduce         | 2.96 us                                                             | 3.21 us: 1.08x slower                                  |
| pyflate                 | 414 ms                                                              | 450 ms: 1.09x slower                                   |
| scimark_fft             | 328 ms                                                              | 357 ms: 1.09x slower                                   |
| xml_etree_process       | 54.1 ms                                                             | 59.1 ms: 1.09x slower                                  |
| meteor_contest          | 106 ms                                                              | 116 ms: 1.10x slower                                   |
| mako                    | 9.82 ms                                                             | 10.8 ms: 1.10x slower                                  |
| regex_effbot            | 3.32 ms                                                             | 3.67 ms: 1.10x slower                                  |
| xml_etree_generate      | 76.5 ms                                                             | 84.6 ms: 1.11x slower                                  |
| python_startup_no_site  | 5.98 ms                                                             | 6.65 ms: 1.11x slower                                  |
| unpickle                | 13.2 us                                                             | 14.7 us: 1.11x slower                                  |
| gc_traversal            | 3.63 ms                                                             | 4.06 ms: 1.12x slower                                  |
| pickle_list             | 4.03 us                                                             | 4.51 us: 1.12x slower                                  |
| async_generators        | 361 ms                                                              | 434 ms: 1.20x slower                                   |
| dask                    | 368 ms                                                              | 539 ms: 1.46x slower                                   |
| Geometric mean          | (ref)                                                               | 1.01x slower                                           |

Benchmark hidden because not significant (4): pycparser, bench_mp_pool, sqlglot_transpile, regex_v8
Ignored benchmarks (11) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, gunicorn, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum

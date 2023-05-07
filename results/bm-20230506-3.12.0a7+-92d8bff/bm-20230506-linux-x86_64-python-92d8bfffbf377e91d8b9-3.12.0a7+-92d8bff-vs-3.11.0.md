
# Results vs. 3.11.0

- fork: python
- ref: 92d8bfffbf377e91d8b9
- machine: linux-x86_64
- commit hash: 92d8bff
- commit date: 2023-05-06
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 270 ms: 1.05x slower                                                   |
| docutils       | 2.59 sec                                                            | 2.73 sec: 1.05x slower                                                 |
| tornado_http   | 96.7 ms                                                             | 103 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                               | 1.06x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 90.6 ms: 1.07x faster                                                  |
| pidigits       | 197 ms                                                              | 189 ms: 1.04x faster                                                   |
| float          | 76.0 ms                                                             | 81.2 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                               | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 196 ms                                                              | 207 ms: 1.06x slower                                                   |
| regex_compile  | 137 ms                                                              | 146 ms: 1.07x slower                                                   |
| regex_effbot   | 3.32 ms                                                             | 3.60 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                               | 1.05x slower                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.87 ms: 1.27x faster                                                  |
| xml_etree_parse      | 162 ms                                                              | 156 ms: 1.04x faster                                                   |
| unpickle_pure_python | 228 us                                                              | 220 us: 1.04x faster                                                   |
| json_loads           | 26.2 us                                                             | 25.3 us: 1.03x faster                                                  |
| xml_etree_iterparse  | 108 ms                                                              | 104 ms: 1.03x faster                                                   |
| pickle_dict          | 30.9 us                                                             | 31.6 us: 1.02x slower                                                  |
| pickle_pure_python   | 307 us                                                              | 316 us: 1.03x slower                                                   |
| pickle               | 9.79 us                                                             | 10.5 us: 1.08x slower                                                  |
| xml_etree_process    | 54.1 ms                                                             | 59.3 ms: 1.10x slower                                                  |
| xml_etree_generate   | 76.5 ms                                                             | 84.9 ms: 1.11x slower                                                  |
| pickle_list          | 4.03 us                                                             | 4.54 us: 1.13x slower                                                  |
| unpickle             | 13.2 us                                                             | 15.0 us: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.01x slower                                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 9.15 ms: 1.08x slower                                                  |
| python_startup_no_site | 5.98 ms                                                             | 6.69 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.10x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|-----------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 9.82 ms                                                             | 10.7 ms: 1.09x slower                                                  |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 30.9 ms: 2.37x faster                                                  |
| asyncio_tcp             | 888 ms                                                              | 507 ms: 1.75x faster                                                   |
| json_dumps              | 12.5 ms                                                             | 9.87 ms: 1.27x faster                                                  |
| mypy2                   | 422 ms                                                              | 353 ms: 1.19x faster                                                   |
| coroutines              | 26.3 ms                                                             | 22.7 ms: 1.16x faster                                                  |
| nbody                   | 96.7 ms                                                             | 90.6 ms: 1.07x faster                                                  |
| hexiom                  | 6.48 ms                                                             | 6.11 ms: 1.06x faster                                                  |
| nqueens                 | 84.0 ms                                                             | 79.5 ms: 1.06x faster                                                  |
| async_tree_io           | 1.28 sec                                                            | 1.23 sec: 1.05x faster                                                 |
| pidigits                | 197 ms                                                              | 189 ms: 1.04x faster                                                   |
| xml_etree_parse         | 162 ms                                                              | 156 ms: 1.04x faster                                                   |
| async_tree_none         | 525 ms                                                              | 505 ms: 1.04x faster                                                   |
| unpickle_pure_python    | 228 us                                                              | 220 us: 1.04x faster                                                   |
| json_loads              | 26.2 us                                                             | 25.3 us: 1.03x faster                                                  |
| xml_etree_iterparse     | 108 ms                                                              | 104 ms: 1.03x faster                                                   |
| deltablue               | 3.66 ms                                                             | 3.57 ms: 1.02x faster                                                  |
| sqlglot_parse           | 1.36 ms                                                             | 1.33 ms: 1.02x faster                                                  |
| richards                | 45.7 ms                                                             | 44.8 ms: 1.02x faster                                                  |
| json                    | 4.86 ms                                                             | 4.77 ms: 1.02x faster                                                  |
| fannkuch                | 384 ms                                                              | 377 ms: 1.02x faster                                                   |
| go                      | 138 ms                                                              | 136 ms: 1.01x faster                                                   |
| async_tree_memoization  | 621 ms                                                              | 613 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed | 736 ms                                                              | 727 ms: 1.01x faster                                                   |
| chaos                   | 68.0 ms                                                             | 68.2 ms: 1.00x slower                                                  |
| create_gc_cycles        | 1.48 ms                                                             | 1.49 ms: 1.01x slower                                                  |
| pycparser               | 1.14 sec                                                            | 1.16 sec: 1.01x slower                                                 |
| bench_thread_pool       | 820 us                                                              | 831 us: 1.01x slower                                                   |
| coverage                | 101 ms                                                              | 102 ms: 1.01x slower                                                   |
| mdp                     | 2.64 sec                                                            | 2.68 sec: 1.02x slower                                                 |
| pickle_dict             | 30.9 us                                                             | 31.6 us: 1.02x slower                                                  |
| telco                   | 6.59 ms                                                             | 6.77 ms: 1.03x slower                                                  |
| pickle_pure_python      | 307 us                                                              | 316 us: 1.03x slower                                                   |
| sqlglot_optimize        | 53.4 ms                                                             | 55.1 ms: 1.03x slower                                                  |
| pathlib                 | 18.2 ms                                                             | 18.8 ms: 1.03x slower                                                  |
| pprint_pformat          | 1.45 sec                                                            | 1.50 sec: 1.04x slower                                                 |
| sqlglot_normalize       | 108 ms                                                              | 112 ms: 1.04x slower                                                   |
| deepcopy_memo           | 36.4 us                                                             | 37.7 us: 1.04x slower                                                  |
| logging_silent          | 98.7 ns                                                             | 102 ns: 1.04x slower                                                   |
| logging_simple          | 6.09 us                                                             | 6.35 us: 1.04x slower                                                  |
| comprehensions          | 22.2 us                                                             | 23.2 us: 1.04x slower                                                  |
| scimark_lu              | 108 ms                                                              | 113 ms: 1.04x slower                                                   |
| pprint_safe_repr        | 701 ms                                                              | 734 ms: 1.05x slower                                                   |
| 2to3                    | 257 ms                                                              | 270 ms: 1.05x slower                                                   |
| sqlalchemy_declarative  | 138 ms                                                              | 146 ms: 1.05x slower                                                   |
| crypto_pyaes            | 73.8 ms                                                             | 77.8 ms: 1.05x slower                                                  |
| docutils                | 2.59 sec                                                            | 2.73 sec: 1.05x slower                                                 |
| regex_dna               | 196 ms                                                              | 207 ms: 1.06x slower                                                   |
| raytrace                | 292 ms                                                              | 310 ms: 1.06x slower                                                   |
| tornado_http            | 96.7 ms                                                             | 103 ms: 1.06x slower                                                   |
| logging_format          | 6.64 us                                                             | 7.05 us: 1.06x slower                                                  |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.75 ms: 1.06x slower                                                  |
| regex_compile           | 137 ms                                                              | 146 ms: 1.07x slower                                                   |
| scimark_sor             | 115 ms                                                              | 123 ms: 1.07x slower                                                   |
| deepcopy                | 339 us                                                              | 362 us: 1.07x slower                                                   |
| pyflate                 | 414 ms                                                              | 442 ms: 1.07x slower                                                   |
| float                   | 76.0 ms                                                             | 81.2 ms: 1.07x slower                                                  |
| dulwich_log             | 63.6 ms                                                             | 68.1 ms: 1.07x slower                                                  |
| spectral_norm           | 99.5 ms                                                             | 107 ms: 1.07x slower                                                   |
| sqlalchemy_imperative   | 18.0 ms                                                             | 19.4 ms: 1.07x slower                                                  |
| pickle                  | 9.79 us                                                             | 10.5 us: 1.08x slower                                                  |
| scimark_monte_carlo     | 67.8 ms                                                             | 72.9 ms: 1.08x slower                                                  |
| python_startup          | 8.49 ms                                                             | 9.15 ms: 1.08x slower                                                  |
| regex_effbot            | 3.32 ms                                                             | 3.60 ms: 1.08x slower                                                  |
| deepcopy_reduce         | 2.96 us                                                             | 3.21 us: 1.08x slower                                                  |
| sqlite_synth            | 2.51 us                                                             | 2.74 us: 1.09x slower                                                  |
| mako                    | 9.82 ms                                                             | 10.7 ms: 1.09x slower                                                  |
| scimark_fft             | 328 ms                                                              | 358 ms: 1.09x slower                                                   |
| xml_etree_process       | 54.1 ms                                                             | 59.3 ms: 1.10x slower                                                  |
| xml_etree_generate      | 76.5 ms                                                             | 84.9 ms: 1.11x slower                                                  |
| python_startup_no_site  | 5.98 ms                                                             | 6.69 ms: 1.12x slower                                                  |
| pickle_list             | 4.03 us                                                             | 4.54 us: 1.13x slower                                                  |
| unpickle                | 13.2 us                                                             | 15.0 us: 1.13x slower                                                  |
| unpack_sequence         | 49.5 ns                                                             | 58.6 ns: 1.18x slower                                                  |
| gc_traversal            | 3.63 ms                                                             | 4.37 ms: 1.21x slower                                                  |
| async_generators        | 361 ms                                                              | 448 ms: 1.24x slower                                                   |
| dask                    | 368 ms                                                              | 539 ms: 1.46x slower                                                   |
| Geometric mean          | (ref)                                                               | 1.01x slower                                                           |

Benchmark hidden because not significant (5): meteor_contest, bench_mp_pool, regex_v8, sqlglot_transpile, unpickle_list
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift

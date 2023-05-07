
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 42f54d1
- commit date: 2023-05-06
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 269 ms: 1.05x slower                                   |
| docutils       | 2.59 sec                                                            | 2.72 sec: 1.05x slower                                 |
| tornado_http   | 96.7 ms                                                             | 99.9 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                               | 1.04x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 88.0 ms: 1.10x faster                                  |
| float          | 76.0 ms                                                             | 81.2 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                               | 1.01x faster                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                             | 22.3 ms: 1.01x slower                                  |
| regex_dna      | 196 ms                                                              | 200 ms: 1.02x slower                                   |
| regex_effbot   | 3.32 ms                                                             | 3.54 ms: 1.07x slower                                  |
| regex_compile  | 137 ms                                                              | 146 ms: 1.07x slower                                   |
| Geometric mean | (ref)                                                               | 1.04x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.94 ms: 1.26x faster                                  |
| unpickle_pure_python | 228 us                                                              | 216 us: 1.06x faster                                   |
| xml_etree_parse      | 162 ms                                                              | 155 ms: 1.05x faster                                   |
| xml_etree_iterparse  | 108 ms                                                              | 104 ms: 1.04x faster                                   |
| json_loads           | 26.2 us                                                             | 25.4 us: 1.03x faster                                  |
| unpickle_list        | 4.96 us                                                             | 4.85 us: 1.02x faster                                  |
| pickle_pure_python   | 307 us                                                              | 311 us: 1.01x slower                                   |
| pickle_dict          | 30.9 us                                                             | 31.4 us: 1.01x slower                                  |
| pickle               | 9.79 us                                                             | 10.6 us: 1.08x slower                                  |
| xml_etree_process    | 54.1 ms                                                             | 59.0 ms: 1.09x slower                                  |
| xml_etree_generate   | 76.5 ms                                                             | 85.3 ms: 1.11x slower                                  |
| unpickle             | 13.2 us                                                             | 15.1 us: 1.14x slower                                  |
| pickle_list          | 4.03 us                                                             | 4.74 us: 1.18x slower                                  |
| Geometric mean       | (ref)                                                               | 1.01x slower                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 9.17 ms: 1.08x slower                                  |
| python_startup_no_site | 5.98 ms                                                             | 6.69 ms: 1.12x slower                                  |
| Geometric mean         | (ref)                                                               | 1.10x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|-----------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 9.82 ms                                                             | 11.0 ms: 1.12x slower                                  |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|-------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 31.3 ms: 2.34x faster                                  |
| asyncio_tcp             | 888 ms                                                              | 512 ms: 1.73x faster                                   |
| json_dumps              | 12.5 ms                                                             | 9.94 ms: 1.26x faster                                  |
| mypy2                   | 422 ms                                                              | 351 ms: 1.20x faster                                   |
| coroutines              | 26.3 ms                                                             | 22.1 ms: 1.19x faster                                  |
| nbody                   | 96.7 ms                                                             | 88.0 ms: 1.10x faster                                  |
| unpack_sequence         | 49.5 ns                                                             | 45.1 ns: 1.10x faster                                  |
| richards                | 45.7 ms                                                             | 43.0 ms: 1.06x faster                                  |
| unpickle_pure_python    | 228 us                                                              | 216 us: 1.06x faster                                   |
| async_tree_none         | 525 ms                                                              | 498 ms: 1.05x faster                                   |
| xml_etree_parse         | 162 ms                                                              | 155 ms: 1.05x faster                                   |
| nqueens                 | 84.0 ms                                                             | 80.2 ms: 1.05x faster                                  |
| async_tree_io           | 1.28 sec                                                            | 1.23 sec: 1.05x faster                                 |
| deltablue               | 3.66 ms                                                             | 3.51 ms: 1.04x faster                                  |
| hexiom                  | 6.48 ms                                                             | 6.22 ms: 1.04x faster                                  |
| xml_etree_iterparse     | 108 ms                                                              | 104 ms: 1.04x faster                                   |
| sqlglot_parse           | 1.36 ms                                                             | 1.32 ms: 1.03x faster                                  |
| json_loads              | 26.2 us                                                             | 25.4 us: 1.03x faster                                  |
| mdp                     | 2.64 sec                                                            | 2.58 sec: 1.02x faster                                 |
| unpickle_list           | 4.96 us                                                             | 4.85 us: 1.02x faster                                  |
| async_tree_cpu_io_mixed | 736 ms                                                              | 721 ms: 1.02x faster                                   |
| async_tree_memoization  | 621 ms                                                              | 613 ms: 1.01x faster                                   |
| go                      | 138 ms                                                              | 137 ms: 1.01x faster                                   |
| json                    | 4.86 ms                                                             | 4.80 ms: 1.01x faster                                  |
| sqlglot_transpile       | 1.65 ms                                                             | 1.64 ms: 1.01x faster                                  |
| fannkuch                | 384 ms                                                              | 380 ms: 1.01x faster                                   |
| create_gc_cycles        | 1.48 ms                                                             | 1.47 ms: 1.00x faster                                  |
| coverage                | 101 ms                                                              | 102 ms: 1.01x slower                                   |
| pycparser               | 1.14 sec                                                            | 1.16 sec: 1.01x slower                                 |
| bench_thread_pool       | 820 us                                                              | 829 us: 1.01x slower                                   |
| pickle_pure_python      | 307 us                                                              | 311 us: 1.01x slower                                   |
| chaos                   | 68.0 ms                                                             | 68.9 ms: 1.01x slower                                  |
| pickle_dict             | 30.9 us                                                             | 31.4 us: 1.01x slower                                  |
| gc_traversal            | 3.63 ms                                                             | 3.68 ms: 1.01x slower                                  |
| regex_v8                | 22.0 ms                                                             | 22.3 ms: 1.01x slower                                  |
| regex_dna               | 196 ms                                                              | 200 ms: 1.02x slower                                   |
| sqlglot_optimize        | 53.4 ms                                                             | 54.7 ms: 1.03x slower                                  |
| pprint_pformat          | 1.45 sec                                                            | 1.49 sec: 1.03x slower                                 |
| sqlglot_normalize       | 108 ms                                                              | 111 ms: 1.03x slower                                   |
| raytrace                | 292 ms                                                              | 301 ms: 1.03x slower                                   |
| tornado_http            | 96.7 ms                                                             | 99.9 ms: 1.03x slower                                  |
| pathlib                 | 18.2 ms                                                             | 18.9 ms: 1.03x slower                                  |
| logging_simple          | 6.09 us                                                             | 6.31 us: 1.04x slower                                  |
| pprint_safe_repr        | 701 ms                                                              | 728 ms: 1.04x slower                                   |
| deepcopy_memo           | 36.4 us                                                             | 37.8 us: 1.04x slower                                  |
| telco                   | 6.59 ms                                                             | 6.88 ms: 1.04x slower                                  |
| scimark_lu              | 108 ms                                                              | 113 ms: 1.05x slower                                   |
| 2to3                    | 257 ms                                                              | 269 ms: 1.05x slower                                   |
| docutils                | 2.59 sec                                                            | 2.72 sec: 1.05x slower                                 |
| comprehensions          | 22.2 us                                                             | 23.4 us: 1.05x slower                                  |
| logging_format          | 6.64 us                                                             | 7.00 us: 1.05x slower                                  |
| deepcopy                | 339 us                                                              | 358 us: 1.06x slower                                   |
| sqlalchemy_declarative  | 138 ms                                                              | 147 ms: 1.06x slower                                   |
| deepcopy_reduce         | 2.96 us                                                             | 3.14 us: 1.06x slower                                  |
| dulwich_log             | 63.6 ms                                                             | 67.7 ms: 1.06x slower                                  |
| pyflate                 | 414 ms                                                              | 441 ms: 1.07x slower                                   |
| regex_effbot            | 3.32 ms                                                             | 3.54 ms: 1.07x slower                                  |
| regex_compile           | 137 ms                                                              | 146 ms: 1.07x slower                                   |
| float                   | 76.0 ms                                                             | 81.2 ms: 1.07x slower                                  |
| sqlalchemy_imperative   | 18.0 ms                                                             | 19.3 ms: 1.07x slower                                  |
| scimark_monte_carlo     | 67.8 ms                                                             | 72.7 ms: 1.07x slower                                  |
| python_startup          | 8.49 ms                                                             | 9.17 ms: 1.08x slower                                  |
| scimark_sor             | 115 ms                                                              | 124 ms: 1.08x slower                                   |
| pickle                  | 9.79 us                                                             | 10.6 us: 1.08x slower                                  |
| spectral_norm           | 99.5 ms                                                             | 108 ms: 1.08x slower                                   |
| crypto_pyaes            | 73.8 ms                                                             | 80.2 ms: 1.09x slower                                  |
| xml_etree_process       | 54.1 ms                                                             | 59.0 ms: 1.09x slower                                  |
| scimark_fft             | 328 ms                                                              | 358 ms: 1.09x slower                                   |
| sqlite_synth            | 2.51 us                                                             | 2.76 us: 1.10x slower                                  |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.91 ms: 1.10x slower                                  |
| xml_etree_generate      | 76.5 ms                                                             | 85.3 ms: 1.11x slower                                  |
| mako                    | 9.82 ms                                                             | 11.0 ms: 1.12x slower                                  |
| python_startup_no_site  | 5.98 ms                                                             | 6.69 ms: 1.12x slower                                  |
| unpickle                | 13.2 us                                                             | 15.1 us: 1.14x slower                                  |
| pickle_list             | 4.03 us                                                             | 4.74 us: 1.18x slower                                  |
| async_generators        | 361 ms                                                              | 451 ms: 1.25x slower                                   |
| dask                    | 368 ms                                                              | 537 ms: 1.46x slower                                   |
| Geometric mean          | (ref)                                                               | 1.01x slower                                           |

Benchmark hidden because not significant (4): meteor_contest, bench_mp_pool, pidigits, logging_silent
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift

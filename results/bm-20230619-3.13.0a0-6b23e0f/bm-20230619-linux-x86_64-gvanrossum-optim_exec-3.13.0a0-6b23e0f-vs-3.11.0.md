
# Results vs. 3.11.0

- fork: gvanrossum
- ref: optim_exec
- machine: linux-x86_64
- commit hash: 6b23e0f
- commit date: 2023-06-19
- overall geometric mean: 1.04x faster
- HPT reliability: 87.56%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.65 sec: 1.01x slower                                          |
| Geometric mean | (ref)                                                  | 1.00x slower                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 89.0 ms: 1.05x faster                                           |
| pidigits       | 198 ms                                                 | 196 ms: 1.01x faster                                            |
| float          | 77.2 ms                                                | 80.5 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                  | 1.00x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.38 ms: 1.18x faster                                           |
| regex_dna      | 204 ms                                                 | 201 ms: 1.01x faster                                            |
| regex_v8       | 22.0 ms                                                | 21.7 ms: 1.01x faster                                           |
| regex_compile  | 138 ms                                                 | 137 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.78 ms: 1.29x faster                                           |
| unpickle_pure_python | 228 us                                                 | 212 us: 1.07x faster                                            |
| json_loads           | 26.5 us                                                | 25.3 us: 1.04x faster                                           |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.04x faster                                            |
| unpickle_list        | 4.91 us                                                | 4.87 us: 1.01x faster                                           |
| pickle_dict          | 31.1 us                                                | 31.5 us: 1.01x slower                                           |
| pickle               | 10.1 us                                                | 10.7 us: 1.06x slower                                           |
| xml_etree_process    | 53.9 ms                                                | 58.2 ms: 1.08x slower                                           |
| pickle_list          | 4.11 us                                                | 4.51 us: 1.10x slower                                           |
| unpickle             | 13.7 us                                                | 15.0 us: 1.10x slower                                           |
| xml_etree_generate   | 76.2 ms                                                | 85.3 ms: 1.12x slower                                           |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                    |

Benchmark hidden because not significant (3): tomli_loads, pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.20 ms: 1.08x slower                                           |
| python_startup_no_site | 6.01 ms                                                | 6.68 ms: 1.11x slower                                           |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.8 ms: 1.07x slower                                           |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 147 us: 3.31x faster                                            |
| generators               | 73.5 ms                                                | 29.8 ms: 2.47x faster                                           |
| asyncio_tcp              | 922 ms                                                 | 506 ms: 1.82x faster                                            |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                          |
| json_dumps               | 12.6 ms                                                | 9.78 ms: 1.29x faster                                           |
| mypy2                    | 420 ms                                                 | 336 ms: 1.25x faster                                            |
| regex_effbot             | 3.99 ms                                                | 3.38 ms: 1.18x faster                                           |
| coroutines               | 25.5 ms                                                | 22.2 ms: 1.15x faster                                           |
| richards_super           | 56.8 ms                                                | 50.2 ms: 1.13x faster                                           |
| chaos                    | 69.2 ms                                                | 61.4 ms: 1.13x faster                                           |
| deltablue                | 3.67 ms                                                | 3.30 ms: 1.11x faster                                           |
| async_tree_none          | 526 ms                                                 | 485 ms: 1.08x faster                                            |
| async_tree_io            | 1.30 sec                                               | 1.20 sec: 1.08x faster                                          |
| gc_traversal             | 4.02 ms                                                | 3.74 ms: 1.07x faster                                           |
| unpickle_pure_python     | 228 us                                                 | 212 us: 1.07x faster                                            |
| sqlglot_parse            | 1.40 ms                                                | 1.30 ms: 1.07x faster                                           |
| logging_silent           | 101 ns                                                 | 94.3 ns: 1.07x faster                                           |
| async_tree_memoization   | 627 ms                                                 | 586 ms: 1.07x faster                                            |
| coverage                 | 100 ms                                                 | 93.8 ms: 1.07x faster                                           |
| sqlglot_transpile        | 1.70 ms                                                | 1.62 ms: 1.05x faster                                           |
| comprehensions           | 22.4 us                                                | 21.4 us: 1.05x faster                                           |
| nbody                    | 93.1 ms                                                | 89.0 ms: 1.05x faster                                           |
| json_loads               | 26.5 us                                                | 25.3 us: 1.04x faster                                           |
| pycparser                | 1.18 sec                                               | 1.13 sec: 1.04x faster                                          |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.04x faster                                            |
| go                       | 140 ms                                                 | 135 ms: 1.04x faster                                            |
| richards                 | 45.7 ms                                                | 44.2 ms: 1.03x faster                                           |
| logging_format           | 6.68 us                                                | 6.50 us: 1.03x faster                                           |
| hexiom                   | 6.37 ms                                                | 6.22 ms: 1.02x faster                                           |
| raytrace                 | 297 ms                                                 | 290 ms: 1.02x faster                                            |
| mdp                      | 2.62 sec                                               | 2.56 sec: 1.02x faster                                          |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 728 ms: 1.01x faster                                            |
| regex_dna                | 204 ms                                                 | 201 ms: 1.01x faster                                            |
| regex_v8                 | 22.0 ms                                                | 21.7 ms: 1.01x faster                                           |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.01x faster                                            |
| logging_simple           | 6.03 us                                                | 5.96 us: 1.01x faster                                           |
| nqueens                  | 83.4 ms                                                | 82.5 ms: 1.01x faster                                           |
| regex_compile            | 138 ms                                                 | 137 ms: 1.01x faster                                            |
| sqlglot_optimize         | 53.1 ms                                                | 52.6 ms: 1.01x faster                                           |
| json                     | 4.94 ms                                                | 4.90 ms: 1.01x faster                                           |
| pidigits                 | 198 ms                                                 | 196 ms: 1.01x faster                                            |
| unpickle_list            | 4.91 us                                                | 4.87 us: 1.01x faster                                           |
| pprint_pformat           | 1.46 sec                                               | 1.47 sec: 1.01x slower                                          |
| docutils                 | 2.63 sec                                               | 2.65 sec: 1.01x slower                                          |
| meteor_contest           | 107 ms                                                 | 108 ms: 1.01x slower                                            |
| pickle_dict              | 31.1 us                                                | 31.5 us: 1.01x slower                                           |
| create_gc_cycles         | 1.49 ms                                                | 1.51 ms: 1.01x slower                                           |
| pprint_safe_repr         | 701 ms                                                 | 713 ms: 1.02x slower                                            |
| bench_thread_pool        | 819 us                                                 | 833 us: 1.02x slower                                            |
| dulwich_log              | 63.7 ms                                                | 64.9 ms: 1.02x slower                                           |
| deepcopy                 | 342 us                                                 | 351 us: 1.03x slower                                            |
| scimark_monte_carlo      | 68.1 ms                                                | 70.0 ms: 1.03x slower                                           |
| deepcopy_memo            | 37.0 us                                                | 38.2 us: 1.03x slower                                           |
| fannkuch                 | 388 ms                                                 | 401 ms: 1.03x slower                                            |
| telco                    | 6.58 ms                                                | 6.81 ms: 1.03x slower                                           |
| float                    | 77.2 ms                                                | 80.5 ms: 1.04x slower                                           |
| crypto_pyaes             | 74.7 ms                                                | 78.5 ms: 1.05x slower                                           |
| pathlib                  | 18.2 ms                                                | 19.3 ms: 1.06x slower                                           |
| pickle                   | 10.1 us                                                | 10.7 us: 1.06x slower                                           |
| pyflate                  | 418 ms                                                 | 444 ms: 1.06x slower                                            |
| deepcopy_reduce          | 2.94 us                                                | 3.13 us: 1.06x slower                                           |
| mako                     | 10.1 ms                                                | 10.8 ms: 1.07x slower                                           |
| scimark_fft              | 328 ms                                                 | 351 ms: 1.07x slower                                            |
| python_startup           | 8.52 ms                                                | 9.20 ms: 1.08x slower                                           |
| xml_etree_process        | 53.9 ms                                                | 58.2 ms: 1.08x slower                                           |
| unpack_sequence          | 43.1 ns                                                | 46.8 ns: 1.09x slower                                           |
| spectral_norm            | 100 ms                                                 | 109 ms: 1.09x slower                                            |
| pickle_list              | 4.11 us                                                | 4.51 us: 1.10x slower                                           |
| unpickle                 | 13.7 us                                                | 15.0 us: 1.10x slower                                           |
| sqlite_synth             | 2.52 us                                                | 2.78 us: 1.10x slower                                           |
| python_startup_no_site   | 6.01 ms                                                | 6.68 ms: 1.11x slower                                           |
| xml_etree_generate       | 76.2 ms                                                | 85.3 ms: 1.12x slower                                           |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 5.07 ms: 1.13x slower                                           |
| async_generators         | 368 ms                                                 | 465 ms: 1.26x slower                                            |
| dask                     | 360 ms                                                 | 519 ms: 1.44x slower                                            |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                    |

Benchmark hidden because not significant (7): scimark_sor, tomli_loads, bench_mp_pool, scimark_lu, pickle_pure_python, tornado_http, xml_etree_iterparse
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 87.56% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

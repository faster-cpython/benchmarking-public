
# Results vs. 3.11.0

- fork: faster-cpython
- ref: deepcopy_demateriali
- machine: linux-x86_64
- commit hash: ab2df81
- commit date: 2023-08-10
- overall geometric mean: 1.04x faster
- HPT reliability: 77.93%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-ab2df81 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tornado_http   | 96.3 ms                                                | 95.2 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-ab2df81 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 89.0 ms: 1.05x faster                                                           |
| pidigits       | 198 ms                                                 | 201 ms: 1.01x slower                                                            |
| float          | 77.2 ms                                                | 80.2 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-ab2df81 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.55 ms: 1.12x faster                                                           |
| regex_compile  | 138 ms                                                 | 137 ms: 1.01x faster                                                            |
| regex_dna      | 204 ms                                                 | 214 ms: 1.05x slower                                                            |
| regex_v8       | 22.0 ms                                                | 23.3 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-ab2df81 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.77 ms: 1.29x faster                                                           |
| unpickle_pure_python | 228 us                                                 | 215 us: 1.06x faster                                                            |
| tomli_loads          | 2.22 sec                                               | 2.10 sec: 1.05x faster                                                          |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                                            |
| json_loads           | 26.5 us                                                | 25.5 us: 1.04x faster                                                           |
| pickle_dict          | 31.1 us                                                | 30.6 us: 1.02x faster                                                           |
| pickle_pure_python   | 306 us                                                 | 303 us: 1.01x faster                                                            |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                            |
| pickle               | 10.1 us                                                | 10.3 us: 1.03x slower                                                           |
| unpickle_list        | 4.91 us                                                | 5.09 us: 1.04x slower                                                           |
| xml_etree_process    | 53.9 ms                                                | 57.3 ms: 1.06x slower                                                           |
| unpickle             | 13.7 us                                                | 14.9 us: 1.09x slower                                                           |
| xml_etree_generate   | 76.2 ms                                                | 83.4 ms: 1.09x slower                                                           |
| pickle_list          | 4.11 us                                                | 4.53 us: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-ab2df81 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.32 ms: 1.09x slower                                                           |
| python_startup_no_site | 6.01 ms                                                | 6.82 ms: 1.14x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-ab2df81 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                           |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-ab2df81 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 148 us: 3.29x faster                                                            |
| generators               | 73.5 ms                                                | 29.3 ms: 2.50x faster                                                           |
| asyncio_tcp              | 922 ms                                                 | 485 ms: 1.90x faster                                                            |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.76x faster                                                          |
| json_dumps               | 12.6 ms                                                | 9.77 ms: 1.29x faster                                                           |
| async_tree_none          | 526 ms                                                 | 440 ms: 1.20x faster                                                            |
| coverage                 | 100 ms                                                 | 85.8 ms: 1.17x faster                                                           |
| coroutines               | 25.5 ms                                                | 21.9 ms: 1.16x faster                                                           |
| chaos                    | 69.2 ms                                                | 60.0 ms: 1.15x faster                                                           |
| regex_effbot             | 3.99 ms                                                | 3.55 ms: 1.12x faster                                                           |
| async_tree_memoization   | 627 ms                                                 | 565 ms: 1.11x faster                                                            |
| sqlglot_parse            | 1.40 ms                                                | 1.28 ms: 1.10x faster                                                           |
| gc_traversal             | 4.02 ms                                                | 3.67 ms: 1.10x faster                                                           |
| comprehensions           | 22.4 us                                                | 20.7 us: 1.09x faster                                                           |
| async_tree_io            | 1.30 sec                                               | 1.20 sec: 1.08x faster                                                          |
| raytrace                 | 297 ms                                                 | 276 ms: 1.08x faster                                                            |
| deltablue                | 3.67 ms                                                | 3.44 ms: 1.07x faster                                                           |
| sqlglot_transpile        | 1.70 ms                                                | 1.60 ms: 1.07x faster                                                           |
| crypto_pyaes             | 74.7 ms                                                | 70.2 ms: 1.06x faster                                                           |
| unpickle_pure_python     | 228 us                                                 | 215 us: 1.06x faster                                                            |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 699 ms: 1.06x faster                                                            |
| tomli_loads              | 2.22 sec                                               | 2.10 sec: 1.05x faster                                                          |
| hexiom                   | 6.37 ms                                                | 6.09 ms: 1.05x faster                                                           |
| nbody                    | 93.1 ms                                                | 89.0 ms: 1.05x faster                                                           |
| nqueens                  | 83.4 ms                                                | 79.7 ms: 1.05x faster                                                           |
| xml_etree_parse          | 158 ms                                                 | 152 ms: 1.04x faster                                                            |
| richards_super           | 56.8 ms                                                | 54.5 ms: 1.04x faster                                                           |
| logging_simple           | 6.03 us                                                | 5.81 us: 1.04x faster                                                           |
| json_loads               | 26.5 us                                                | 25.5 us: 1.04x faster                                                           |
| logging_format           | 6.68 us                                                | 6.44 us: 1.04x faster                                                           |
| sqlglot_normalize        | 108 ms                                                 | 105 ms: 1.03x faster                                                            |
| json                     | 4.94 ms                                                | 4.85 ms: 1.02x faster                                                           |
| pickle_dict              | 31.1 us                                                | 30.6 us: 1.02x faster                                                           |
| fannkuch                 | 388 ms                                                 | 383 ms: 1.01x faster                                                            |
| scimark_monte_carlo      | 68.1 ms                                                | 67.3 ms: 1.01x faster                                                           |
| tornado_http             | 96.3 ms                                                | 95.2 ms: 1.01x faster                                                           |
| pycparser                | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                          |
| pickle_pure_python       | 306 us                                                 | 303 us: 1.01x faster                                                            |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                                            |
| regex_compile            | 138 ms                                                 | 137 ms: 1.01x faster                                                            |
| create_gc_cycles         | 1.49 ms                                                | 1.48 ms: 1.01x faster                                                           |
| go                       | 140 ms                                                 | 139 ms: 1.00x faster                                                            |
| bench_thread_pool        | 819 us                                                 | 816 us: 1.00x faster                                                            |
| pathlib                  | 18.2 ms                                                | 18.4 ms: 1.01x slower                                                           |
| pidigits                 | 198 ms                                                 | 201 ms: 1.01x slower                                                            |
| logging_silent           | 101 ns                                                 | 103 ns: 1.01x slower                                                            |
| mdp                      | 2.62 sec                                               | 2.65 sec: 1.01x slower                                                          |
| deepcopy_memo            | 37.0 us                                                | 37.6 us: 1.02x slower                                                           |
| pprint_pformat           | 1.46 sec                                               | 1.48 sec: 1.02x slower                                                          |
| pickle                   | 10.1 us                                                | 10.3 us: 1.03x slower                                                           |
| scimark_lu               | 110 ms                                                 | 113 ms: 1.03x slower                                                            |
| pprint_safe_repr         | 701 ms                                                 | 724 ms: 1.03x slower                                                            |
| deepcopy                 | 342 us                                                 | 354 us: 1.03x slower                                                            |
| unpickle_list            | 4.91 us                                                | 5.09 us: 1.04x slower                                                           |
| dulwich_log              | 63.7 ms                                                | 66.1 ms: 1.04x slower                                                           |
| float                    | 77.2 ms                                                | 80.2 ms: 1.04x slower                                                           |
| regex_dna                | 204 ms                                                 | 214 ms: 1.05x slower                                                            |
| scimark_sor              | 118 ms                                                 | 125 ms: 1.06x slower                                                            |
| regex_v8                 | 22.0 ms                                                | 23.3 ms: 1.06x slower                                                           |
| richards                 | 45.7 ms                                                | 48.5 ms: 1.06x slower                                                           |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.78 ms: 1.06x slower                                                           |
| xml_etree_process        | 53.9 ms                                                | 57.3 ms: 1.06x slower                                                           |
| mako                     | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                           |
| pyflate                  | 418 ms                                                 | 447 ms: 1.07x slower                                                            |
| deepcopy_reduce          | 2.94 us                                                | 3.15 us: 1.07x slower                                                           |
| sqlite_synth             | 2.52 us                                                | 2.72 us: 1.08x slower                                                           |
| spectral_norm            | 100 ms                                                 | 108 ms: 1.08x slower                                                            |
| unpickle                 | 13.7 us                                                | 14.9 us: 1.09x slower                                                           |
| scimark_fft              | 328 ms                                                 | 358 ms: 1.09x slower                                                            |
| python_startup           | 8.52 ms                                                | 9.32 ms: 1.09x slower                                                           |
| xml_etree_generate       | 76.2 ms                                                | 83.4 ms: 1.09x slower                                                           |
| unpack_sequence          | 43.1 ns                                                | 47.3 ns: 1.10x slower                                                           |
| pickle_list              | 4.11 us                                                | 4.53 us: 1.10x slower                                                           |
| python_startup_no_site   | 6.01 ms                                                | 6.82 ms: 1.14x slower                                                           |
| async_generators         | 368 ms                                                 | 454 ms: 1.23x slower                                                            |
| telco                    | 6.58 ms                                                | 8.19 ms: 1.24x slower                                                           |
| dask                     | 360 ms                                                 | 520 ms: 1.45x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (5): meteor_contest, docutils, sqlglot_optimize, bench_mp_pool, mypy2
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 77.93% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

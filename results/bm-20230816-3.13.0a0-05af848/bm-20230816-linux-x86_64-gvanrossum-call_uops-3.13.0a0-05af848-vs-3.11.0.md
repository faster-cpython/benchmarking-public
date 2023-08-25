
# Results vs. 3.11.0

- fork: gvanrossum
- ref: call_uops
- machine: linux-x86_64
- commit hash: 05af848
- commit date: 2023-08-16
- overall geometric mean: 1.04x faster
- HPT reliability: 85.46%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230816-linux-x86_64-gvanrossum-call_uops-3.13.0a0-05af848 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| tornado_http   | 96.3 ms                                                | 95.1 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230816-linux-x86_64-gvanrossum-call_uops-3.13.0a0-05af848 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 88.3 ms: 1.06x faster                                          |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                           |
| float          | 77.2 ms                                                | 79.8 ms: 1.03x slower                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230816-linux-x86_64-gvanrossum-call_uops-3.13.0a0-05af848 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.74 ms: 1.07x faster                                          |
| regex_compile  | 138 ms                                                 | 136 ms: 1.01x faster                                           |
| regex_dna      | 204 ms                                                 | 217 ms: 1.06x slower                                           |
| regex_v8       | 22.0 ms                                                | 23.5 ms: 1.07x slower                                          |
| Geometric mean | (ref)                                                  | 1.01x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230816-linux-x86_64-gvanrossum-call_uops-3.13.0a0-05af848 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.78 ms: 1.29x faster                                          |
| unpickle_pure_python | 228 us                                                 | 211 us: 1.08x faster                                           |
| tomli_loads          | 2.22 sec                                               | 2.10 sec: 1.06x faster                                         |
| json_loads           | 26.5 us                                                | 25.2 us: 1.05x faster                                          |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.05x faster                                           |
| pickle_pure_python   | 306 us                                                 | 295 us: 1.04x faster                                           |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                           |
| pickle_dict          | 31.1 us                                                | 32.0 us: 1.03x slower                                          |
| unpickle_list        | 4.91 us                                                | 5.12 us: 1.04x slower                                          |
| unpickle             | 13.7 us                                                | 14.3 us: 1.05x slower                                          |
| pickle               | 10.1 us                                                | 10.6 us: 1.05x slower                                          |
| xml_etree_process    | 53.9 ms                                                | 57.6 ms: 1.07x slower                                          |
| xml_etree_generate   | 76.2 ms                                                | 82.9 ms: 1.09x slower                                          |
| pickle_list          | 4.11 us                                                | 4.72 us: 1.15x slower                                          |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230816-linux-x86_64-gvanrossum-call_uops-3.13.0a0-05af848 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.36 ms: 1.10x slower                                          |
| python_startup_no_site | 6.01 ms                                                | 6.86 ms: 1.14x slower                                          |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230816-linux-x86_64-gvanrossum-call_uops-3.13.0a0-05af848 |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.9 ms: 1.08x slower                                          |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230816-linux-x86_64-gvanrossum-call_uops-3.13.0a0-05af848 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 142 us: 3.42x faster                                           |
| generators               | 73.5 ms                                                | 28.3 ms: 2.60x faster                                          |
| asyncio_tcp              | 922 ms                                                 | 488 ms: 1.89x faster                                           |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                         |
| json_dumps               | 12.6 ms                                                | 9.78 ms: 1.29x faster                                          |
| async_tree_none          | 526 ms                                                 | 437 ms: 1.20x faster                                           |
| coverage                 | 100 ms                                                 | 84.6 ms: 1.18x faster                                          |
| coroutines               | 25.5 ms                                                | 22.2 ms: 1.15x faster                                          |
| chaos                    | 69.2 ms                                                | 60.2 ms: 1.15x faster                                          |
| async_tree_memoization   | 627 ms                                                 | 563 ms: 1.12x faster                                           |
| deltablue                | 3.67 ms                                                | 3.29 ms: 1.12x faster                                          |
| comprehensions           | 22.4 us                                                | 20.4 us: 1.10x faster                                          |
| sqlglot_parse            | 1.40 ms                                                | 1.28 ms: 1.09x faster                                          |
| async_tree_io            | 1.30 sec                                               | 1.19 sec: 1.09x faster                                         |
| unpickle_pure_python     | 228 us                                                 | 211 us: 1.08x faster                                           |
| raytrace                 | 297 ms                                                 | 276 ms: 1.07x faster                                           |
| crypto_pyaes             | 74.7 ms                                                | 69.6 ms: 1.07x faster                                          |
| regex_effbot             | 3.99 ms                                                | 3.74 ms: 1.07x faster                                          |
| sqlglot_transpile        | 1.70 ms                                                | 1.61 ms: 1.06x faster                                          |
| tomli_loads              | 2.22 sec                                               | 2.10 sec: 1.06x faster                                         |
| hexiom                   | 6.37 ms                                                | 6.03 ms: 1.06x faster                                          |
| nqueens                  | 83.4 ms                                                | 78.9 ms: 1.06x faster                                          |
| nbody                    | 93.1 ms                                                | 88.3 ms: 1.06x faster                                          |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 702 ms: 1.05x faster                                           |
| pidigits                 | 198 ms                                                 | 189 ms: 1.05x faster                                           |
| json_loads               | 26.5 us                                                | 25.2 us: 1.05x faster                                          |
| xml_etree_parse          | 158 ms                                                 | 152 ms: 1.05x faster                                           |
| richards_super           | 56.8 ms                                                | 54.4 ms: 1.04x faster                                          |
| logging_format           | 6.68 us                                                | 6.41 us: 1.04x faster                                          |
| logging_simple           | 6.03 us                                                | 5.81 us: 1.04x faster                                          |
| pickle_pure_python       | 306 us                                                 | 295 us: 1.04x faster                                           |
| scimark_monte_carlo      | 68.1 ms                                                | 66.0 ms: 1.03x faster                                          |
| sqlglot_normalize        | 108 ms                                                 | 105 ms: 1.03x faster                                           |
| mdp                      | 2.62 sec                                               | 2.54 sec: 1.03x faster                                         |
| xml_etree_iterparse      | 104 ms                                                 | 102 ms: 1.02x faster                                           |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.02x faster                                           |
| regex_compile            | 138 ms                                                 | 136 ms: 1.01x faster                                           |
| tornado_http             | 96.3 ms                                                | 95.1 ms: 1.01x faster                                          |
| sqlglot_optimize         | 53.1 ms                                                | 52.6 ms: 1.01x faster                                          |
| unpack_sequence          | 43.1 ns                                                | 42.7 ns: 1.01x faster                                          |
| bench_thread_pool        | 819 us                                                 | 815 us: 1.00x faster                                           |
| fannkuch                 | 388 ms                                                 | 390 ms: 1.01x slower                                           |
| gc_traversal             | 4.02 ms                                                | 4.06 ms: 1.01x slower                                          |
| pprint_pformat           | 1.46 sec                                               | 1.48 sec: 1.02x slower                                         |
| pathlib                  | 18.2 ms                                                | 18.6 ms: 1.02x slower                                          |
| deepcopy                 | 342 us                                                 | 349 us: 1.02x slower                                           |
| scimark_lu               | 110 ms                                                 | 112 ms: 1.02x slower                                           |
| pycparser                | 1.18 sec                                               | 1.21 sec: 1.02x slower                                         |
| logging_silent           | 101 ns                                                 | 104 ns: 1.02x slower                                           |
| pprint_safe_repr         | 701 ms                                                 | 721 ms: 1.03x slower                                           |
| pickle_dict              | 31.1 us                                                | 32.0 us: 1.03x slower                                          |
| float                    | 77.2 ms                                                | 79.8 ms: 1.03x slower                                          |
| dulwich_log              | 63.7 ms                                                | 65.8 ms: 1.03x slower                                          |
| scimark_sor              | 118 ms                                                 | 122 ms: 1.03x slower                                           |
| unpickle_list            | 4.91 us                                                | 5.12 us: 1.04x slower                                          |
| unpickle                 | 13.7 us                                                | 14.3 us: 1.05x slower                                          |
| pickle                   | 10.1 us                                                | 10.6 us: 1.05x slower                                          |
| richards                 | 45.7 ms                                                | 48.0 ms: 1.05x slower                                          |
| regex_dna                | 204 ms                                                 | 217 ms: 1.06x slower                                           |
| pyflate                  | 418 ms                                                 | 446 ms: 1.07x slower                                           |
| regex_v8                 | 22.0 ms                                                | 23.5 ms: 1.07x slower                                          |
| xml_etree_process        | 53.9 ms                                                | 57.6 ms: 1.07x slower                                          |
| deepcopy_reduce          | 2.94 us                                                | 3.14 us: 1.07x slower                                          |
| spectral_norm            | 100 ms                                                 | 107 ms: 1.07x slower                                           |
| sqlite_synth             | 2.52 us                                                | 2.72 us: 1.08x slower                                          |
| scimark_fft              | 328 ms                                                 | 355 ms: 1.08x slower                                           |
| mako                     | 10.1 ms                                                | 10.9 ms: 1.08x slower                                          |
| xml_etree_generate       | 76.2 ms                                                | 82.9 ms: 1.09x slower                                          |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.94 ms: 1.10x slower                                          |
| python_startup           | 8.52 ms                                                | 9.36 ms: 1.10x slower                                          |
| python_startup_no_site   | 6.01 ms                                                | 6.86 ms: 1.14x slower                                          |
| pickle_list              | 4.11 us                                                | 4.72 us: 1.15x slower                                          |
| telco                    | 6.58 ms                                                | 8.08 ms: 1.23x slower                                          |
| async_generators         | 368 ms                                                 | 452 ms: 1.23x slower                                           |
| dask                     | 360 ms                                                 | 519 ms: 1.44x slower                                           |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                   |

Benchmark hidden because not significant (7): json, go, create_gc_cycles, bench_mp_pool, docutils, deepcopy_memo, mypy2
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 85.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Results vs. 3.11.0

- fork: gvanrossum
- ref: tweak_uops
- machine: linux-x86_64
- commit hash: 5b85a49
- commit date: 2023-07-01
- overall geometric mean: 1.02x faster
- HPT reliability: 99.19%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.71 sec: 1.03x slower                                          |
| tornado_http   | 96.3 ms                                                | 97.1 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                  | 1.02x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                            |
| nbody          | 93.1 ms                                                | 95.8 ms: 1.03x slower                                           |
| float          | 77.2 ms                                                | 82.6 ms: 1.07x slower                                           |
| Geometric mean | (ref)                                                  | 1.03x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.85 ms: 1.04x faster                                           |
| regex_compile  | 138 ms                                                 | 141 ms: 1.02x slower                                            |
| regex_v8       | 22.0 ms                                                | 22.7 ms: 1.03x slower                                           |
| regex_dna      | 204 ms                                                 | 217 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                  | 1.02x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.74 ms: 1.29x faster                                           |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                            |
| json_loads           | 26.5 us                                                | 25.8 us: 1.03x faster                                           |
| unpickle_pure_python | 228 us                                                 | 223 us: 1.02x faster                                            |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                            |
| unpickle_list        | 4.91 us                                                | 5.06 us: 1.03x slower                                           |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                           |
| pickle_dict          | 31.1 us                                                | 32.4 us: 1.04x slower                                           |
| unpickle             | 13.7 us                                                | 15.0 us: 1.10x slower                                           |
| xml_etree_process    | 53.9 ms                                                | 59.2 ms: 1.10x slower                                           |
| pickle_list          | 4.11 us                                                | 4.59 us: 1.12x slower                                           |
| xml_etree_generate   | 76.2 ms                                                | 85.5 ms: 1.12x slower                                           |
| tomli_loads          | 2.22 sec                                               | 2.52 sec: 1.13x slower                                          |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                    |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.24 ms: 1.08x slower                                           |
| python_startup_no_site | 6.01 ms                                                | 6.72 ms: 1.12x slower                                           |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.9 ms: 1.08x slower                                           |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 148 us: 3.29x faster                                            |
| generators               | 73.5 ms                                                | 29.9 ms: 2.46x faster                                           |
| asyncio_tcp              | 922 ms                                                 | 514 ms: 1.79x faster                                            |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                          |
| json_dumps               | 12.6 ms                                                | 9.74 ms: 1.29x faster                                           |
| mypy2                    | 420 ms                                                 | 341 ms: 1.23x faster                                            |
| coroutines               | 25.5 ms                                                | 22.4 ms: 1.14x faster                                           |
| chaos                    | 69.2 ms                                                | 60.9 ms: 1.14x faster                                           |
| deltablue                | 3.67 ms                                                | 3.38 ms: 1.09x faster                                           |
| coverage                 | 100 ms                                                 | 92.2 ms: 1.09x faster                                           |
| raytrace                 | 297 ms                                                 | 274 ms: 1.08x faster                                            |
| async_tree_none          | 526 ms                                                 | 487 ms: 1.08x faster                                            |
| async_tree_io            | 1.30 sec                                               | 1.21 sec: 1.07x faster                                          |
| comprehensions           | 22.4 us                                                | 21.1 us: 1.06x faster                                           |
| async_tree_memoization   | 627 ms                                                 | 596 ms: 1.05x faster                                            |
| richards_super           | 56.8 ms                                                | 54.3 ms: 1.04x faster                                           |
| regex_effbot             | 3.99 ms                                                | 3.85 ms: 1.04x faster                                           |
| sqlglot_parse            | 1.40 ms                                                | 1.36 ms: 1.03x faster                                           |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                            |
| json_loads               | 26.5 us                                                | 25.8 us: 1.03x faster                                           |
| unpickle_pure_python     | 228 us                                                 | 223 us: 1.02x faster                                            |
| logging_format           | 6.68 us                                                | 6.54 us: 1.02x faster                                           |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 726 ms: 1.02x faster                                            |
| json                     | 4.94 ms                                                | 4.87 ms: 1.01x faster                                           |
| sqlglot_transpile        | 1.70 ms                                                | 1.69 ms: 1.01x faster                                           |
| gc_traversal             | 4.02 ms                                                | 3.98 ms: 1.01x faster                                           |
| logging_simple           | 6.03 us                                                | 5.99 us: 1.01x faster                                           |
| nqueens                  | 83.4 ms                                                | 83.0 ms: 1.00x faster                                           |
| pidigits                 | 198 ms                                                 | 197 ms: 1.00x faster                                            |
| tornado_http             | 96.3 ms                                                | 97.1 ms: 1.01x slower                                           |
| pycparser                | 1.18 sec                                               | 1.20 sec: 1.01x slower                                          |
| create_gc_cycles         | 1.49 ms                                                | 1.52 ms: 1.02x slower                                           |
| regex_compile            | 138 ms                                                 | 141 ms: 1.02x slower                                            |
| scimark_sor              | 118 ms                                                 | 120 ms: 1.02x slower                                            |
| bench_thread_pool        | 819 us                                                 | 835 us: 1.02x slower                                            |
| sqlglot_normalize        | 108 ms                                                 | 110 ms: 1.02x slower                                            |
| logging_silent           | 101 ns                                                 | 103 ns: 1.02x slower                                            |
| go                       | 140 ms                                                 | 143 ms: 1.02x slower                                            |
| pprint_pformat           | 1.46 sec                                               | 1.49 sec: 1.02x slower                                          |
| xml_etree_iterparse      | 104 ms                                                 | 106 ms: 1.02x slower                                            |
| nbody                    | 93.1 ms                                                | 95.8 ms: 1.03x slower                                           |
| scimark_lu               | 110 ms                                                 | 113 ms: 1.03x slower                                            |
| deepcopy                 | 342 us                                                 | 352 us: 1.03x slower                                            |
| regex_v8                 | 22.0 ms                                                | 22.7 ms: 1.03x slower                                           |
| docutils                 | 2.63 sec                                               | 2.71 sec: 1.03x slower                                          |
| hexiom                   | 6.37 ms                                                | 6.57 ms: 1.03x slower                                           |
| unpickle_list            | 4.91 us                                                | 5.06 us: 1.03x slower                                           |
| sqlglot_optimize         | 53.1 ms                                                | 54.9 ms: 1.03x slower                                           |
| pprint_safe_repr         | 701 ms                                                 | 726 ms: 1.04x slower                                            |
| pickle                   | 10.1 us                                                | 10.5 us: 1.04x slower                                           |
| deepcopy_memo            | 37.0 us                                                | 38.5 us: 1.04x slower                                           |
| pickle_dict              | 31.1 us                                                | 32.4 us: 1.04x slower                                           |
| dulwich_log              | 63.7 ms                                                | 66.4 ms: 1.04x slower                                           |
| crypto_pyaes             | 74.7 ms                                                | 78.1 ms: 1.05x slower                                           |
| pathlib                  | 18.2 ms                                                | 19.1 ms: 1.05x slower                                           |
| meteor_contest           | 107 ms                                                 | 113 ms: 1.06x slower                                            |
| mdp                      | 2.62 sec                                               | 2.77 sec: 1.06x slower                                          |
| richards                 | 45.7 ms                                                | 48.4 ms: 1.06x slower                                           |
| regex_dna                | 204 ms                                                 | 217 ms: 1.06x slower                                            |
| float                    | 77.2 ms                                                | 82.6 ms: 1.07x slower                                           |
| mako                     | 10.1 ms                                                | 10.9 ms: 1.08x slower                                           |
| python_startup           | 8.52 ms                                                | 9.24 ms: 1.08x slower                                           |
| scimark_monte_carlo      | 68.1 ms                                                | 73.8 ms: 1.08x slower                                           |
| unpack_sequence          | 43.1 ns                                                | 46.9 ns: 1.09x slower                                           |
| pyflate                  | 418 ms                                                 | 458 ms: 1.09x slower                                            |
| sqlite_synth             | 2.52 us                                                | 2.77 us: 1.10x slower                                           |
| unpickle                 | 13.7 us                                                | 15.0 us: 1.10x slower                                           |
| xml_etree_process        | 53.9 ms                                                | 59.2 ms: 1.10x slower                                           |
| deepcopy_reduce          | 2.94 us                                                | 3.25 us: 1.11x slower                                           |
| telco                    | 6.58 ms                                                | 7.30 ms: 1.11x slower                                           |
| pickle_list              | 4.11 us                                                | 4.59 us: 1.12x slower                                           |
| python_startup_no_site   | 6.01 ms                                                | 6.72 ms: 1.12x slower                                           |
| spectral_norm            | 100 ms                                                 | 112 ms: 1.12x slower                                            |
| xml_etree_generate       | 76.2 ms                                                | 85.5 ms: 1.12x slower                                           |
| scimark_fft              | 328 ms                                                 | 370 ms: 1.13x slower                                            |
| fannkuch                 | 388 ms                                                 | 437 ms: 1.13x slower                                            |
| tomli_loads              | 2.22 sec                                               | 2.52 sec: 1.13x slower                                          |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 5.11 ms: 1.14x slower                                           |
| async_generators         | 368 ms                                                 | 466 ms: 1.27x slower                                            |
| dask                     | 360 ms                                                 | 527 ms: 1.46x slower                                            |
| Geometric mean           | (ref)                                                  | 1.02x faster                                                    |

Benchmark hidden because not significant (2): pickle_pure_python, bench_mp_pool
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 99.19% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

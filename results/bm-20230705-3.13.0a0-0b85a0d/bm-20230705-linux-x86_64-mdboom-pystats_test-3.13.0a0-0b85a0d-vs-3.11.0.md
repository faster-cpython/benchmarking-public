
# Results vs. 3.11.0

- fork: mdboom
- ref: pystats_test
- machine: linux-x86_64
- commit hash: 0b85a0d
- commit date: 2023-07-05
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.66 sec: 1.01x slower                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                  |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 89.9 ms: 1.04x faster                                         |
| pidigits       | 198 ms                                                 | 197 ms: 1.01x faster                                          |
| float          | 77.2 ms                                                | 79.7 ms: 1.03x slower                                         |
| Geometric mean | (ref)                                                  | 1.00x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.44 ms: 1.16x faster                                         |
| regex_compile  | 138 ms                                                 | 137 ms: 1.00x faster                                          |
| regex_v8       | 22.0 ms                                                | 22.2 ms: 1.01x slower                                         |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                  | 1.03x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.76 ms: 1.29x faster                                         |
| unpickle_pure_python | 228 us                                                 | 213 us: 1.07x faster                                          |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.04x faster                                          |
| json_loads           | 26.5 us                                                | 25.7 us: 1.03x faster                                         |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                          |
| pickle_dict          | 31.1 us                                                | 31.0 us: 1.00x faster                                         |
| tomli_loads          | 2.22 sec                                               | 2.34 sec: 1.05x slower                                        |
| pickle               | 10.1 us                                                | 10.8 us: 1.07x slower                                         |
| unpickle             | 13.7 us                                                | 14.8 us: 1.08x slower                                         |
| xml_etree_process    | 53.9 ms                                                | 58.3 ms: 1.08x slower                                         |
| pickle_list          | 4.11 us                                                | 4.56 us: 1.11x slower                                         |
| xml_etree_generate   | 76.2 ms                                                | 84.9 ms: 1.11x slower                                         |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                  |

Benchmark hidden because not significant (2): pickle_pure_python, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.19 ms: 1.08x slower                                         |
| python_startup_no_site | 6.01 ms                                                | 6.68 ms: 1.11x slower                                         |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.06x slower                                         |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 146 us: 3.33x faster                                          |
| generators               | 73.5 ms                                                | 29.1 ms: 2.53x faster                                         |
| asyncio_tcp              | 922 ms                                                 | 511 ms: 1.80x faster                                          |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.75x faster                                        |
| json_dumps               | 12.6 ms                                                | 9.76 ms: 1.29x faster                                         |
| mypy2                    | 420 ms                                                 | 338 ms: 1.24x faster                                          |
| chaos                    | 69.2 ms                                                | 59.6 ms: 1.16x faster                                         |
| regex_effbot             | 3.99 ms                                                | 3.44 ms: 1.16x faster                                         |
| coroutines               | 25.5 ms                                                | 22.6 ms: 1.13x faster                                         |
| deltablue                | 3.67 ms                                                | 3.27 ms: 1.12x faster                                         |
| raytrace                 | 297 ms                                                 | 269 ms: 1.10x faster                                          |
| comprehensions           | 22.4 us                                                | 20.4 us: 1.10x faster                                         |
| async_tree_none          | 526 ms                                                 | 482 ms: 1.09x faster                                          |
| coverage                 | 100 ms                                                 | 91.8 ms: 1.09x faster                                         |
| async_tree_io            | 1.30 sec                                               | 1.20 sec: 1.08x faster                                        |
| unpickle_pure_python     | 228 us                                                 | 213 us: 1.07x faster                                          |
| async_tree_memoization   | 627 ms                                                 | 589 ms: 1.07x faster                                          |
| richards_super           | 56.8 ms                                                | 53.3 ms: 1.07x faster                                         |
| sqlglot_parse            | 1.40 ms                                                | 1.34 ms: 1.05x faster                                         |
| nqueens                  | 83.4 ms                                                | 79.8 ms: 1.04x faster                                         |
| mdp                      | 2.62 sec                                               | 2.51 sec: 1.04x faster                                        |
| hexiom                   | 6.37 ms                                                | 6.12 ms: 1.04x faster                                         |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.04x faster                                          |
| nbody                    | 93.1 ms                                                | 89.9 ms: 1.04x faster                                         |
| json_loads               | 26.5 us                                                | 25.7 us: 1.03x faster                                         |
| pycparser                | 1.18 sec                                               | 1.15 sec: 1.03x faster                                        |
| meteor_contest           | 107 ms                                                 | 104 ms: 1.03x faster                                          |
| sqlglot_transpile        | 1.70 ms                                                | 1.66 ms: 1.03x faster                                         |
| logging_format           | 6.68 us                                                | 6.53 us: 1.02x faster                                         |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 724 ms: 1.02x faster                                          |
| go                       | 140 ms                                                 | 138 ms: 1.02x faster                                          |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.02x faster                                          |
| json                     | 4.94 ms                                                | 4.88 ms: 1.01x faster                                         |
| logging_simple           | 6.03 us                                                | 5.96 us: 1.01x faster                                         |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                          |
| pidigits                 | 198 ms                                                 | 197 ms: 1.01x faster                                          |
| regex_compile            | 138 ms                                                 | 137 ms: 1.00x faster                                          |
| pickle_dict              | 31.1 us                                                | 31.0 us: 1.00x faster                                         |
| create_gc_cycles         | 1.49 ms                                                | 1.49 ms: 1.00x slower                                         |
| pprint_pformat           | 1.46 sec                                               | 1.46 sec: 1.00x slower                                        |
| regex_v8                 | 22.0 ms                                                | 22.2 ms: 1.01x slower                                         |
| gc_traversal             | 4.02 ms                                                | 4.06 ms: 1.01x slower                                         |
| docutils                 | 2.63 sec                                               | 2.66 sec: 1.01x slower                                        |
| deepcopy_memo            | 37.0 us                                                | 37.6 us: 1.02x slower                                         |
| richards                 | 45.7 ms                                                | 46.6 ms: 1.02x slower                                         |
| scimark_lu               | 110 ms                                                 | 112 ms: 1.02x slower                                          |
| regex_dna                | 204 ms                                                 | 208 ms: 1.02x slower                                          |
| pprint_safe_repr         | 701 ms                                                 | 717 ms: 1.02x slower                                          |
| deepcopy                 | 342 us                                                 | 350 us: 1.02x slower                                          |
| logging_silent           | 101 ns                                                 | 103 ns: 1.02x slower                                          |
| scimark_sor              | 118 ms                                                 | 121 ms: 1.03x slower                                          |
| fannkuch                 | 388 ms                                                 | 399 ms: 1.03x slower                                          |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.63 ms: 1.03x slower                                         |
| float                    | 77.2 ms                                                | 79.7 ms: 1.03x slower                                         |
| pathlib                  | 18.2 ms                                                | 18.8 ms: 1.03x slower                                         |
| dulwich_log              | 63.7 ms                                                | 65.8 ms: 1.03x slower                                         |
| unpack_sequence          | 43.1 ns                                                | 45.3 ns: 1.05x slower                                         |
| crypto_pyaes             | 74.7 ms                                                | 78.6 ms: 1.05x slower                                         |
| tomli_loads              | 2.22 sec                                               | 2.34 sec: 1.05x slower                                        |
| pyflate                  | 418 ms                                                 | 442 ms: 1.06x slower                                          |
| mako                     | 10.1 ms                                                | 10.7 ms: 1.06x slower                                         |
| pickle                   | 10.1 us                                                | 10.8 us: 1.07x slower                                         |
| python_startup           | 8.52 ms                                                | 9.19 ms: 1.08x slower                                         |
| scimark_monte_carlo      | 68.1 ms                                                | 73.5 ms: 1.08x slower                                         |
| unpickle                 | 13.7 us                                                | 14.8 us: 1.08x slower                                         |
| xml_etree_process        | 53.9 ms                                                | 58.3 ms: 1.08x slower                                         |
| deepcopy_reduce          | 2.94 us                                                | 3.21 us: 1.09x slower                                         |
| telco                    | 6.58 ms                                                | 7.22 ms: 1.10x slower                                         |
| scimark_fft              | 328 ms                                                 | 361 ms: 1.10x slower                                          |
| sqlite_synth             | 2.52 us                                                | 2.78 us: 1.10x slower                                         |
| pickle_list              | 4.11 us                                                | 4.56 us: 1.11x slower                                         |
| python_startup_no_site   | 6.01 ms                                                | 6.68 ms: 1.11x slower                                         |
| xml_etree_generate       | 76.2 ms                                                | 84.9 ms: 1.11x slower                                         |
| spectral_norm            | 100 ms                                                 | 112 ms: 1.12x slower                                          |
| async_generators         | 368 ms                                                 | 451 ms: 1.23x slower                                          |
| dask                     | 360 ms                                                 | 524 ms: 1.46x slower                                          |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                  |

Benchmark hidden because not significant (6): bench_thread_pool, bench_mp_pool, sqlglot_optimize, pickle_pure_python, unpickle_list, tornado_http
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift

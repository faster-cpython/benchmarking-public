
# Results vs. 3.11.0

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: 4591b30
- commit date: 2023-08-11
- overall geometric mean: 1.02x faster
- HPT reliability: 66.89%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-4591b30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                    |
| tornado_http   | 96.3 ms                                                | 103 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-4591b30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                      |
| nbody          | 93.1 ms                                                | 90.0 ms: 1.04x faster                                                     |
| float          | 77.2 ms                                                | 110 ms: 1.43x slower                                                      |
| Geometric mean | (ref)                                                  | 1.10x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-4591b30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.59 ms: 1.11x faster                                                     |
| regex_compile  | 138 ms                                                 | 137 ms: 1.01x faster                                                      |
| regex_v8       | 22.0 ms                                                | 22.3 ms: 1.01x slower                                                     |
| regex_dna      | 204 ms                                                 | 215 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-4591b30 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.75 ms: 1.29x faster                                                     |
| unpickle_pure_python | 228 us                                                 | 213 us: 1.07x faster                                                      |
| json_loads           | 26.5 us                                                | 25.3 us: 1.05x faster                                                     |
| pickle_pure_python   | 306 us                                                 | 294 us: 1.04x faster                                                      |
| unpickle_list        | 4.91 us                                                | 4.88 us: 1.01x faster                                                     |
| pickle_dict          | 31.1 us                                                | 31.6 us: 1.02x slower                                                     |
| tomli_loads          | 2.22 sec                                               | 2.29 sec: 1.03x slower                                                    |
| pickle               | 10.1 us                                                | 10.7 us: 1.06x slower                                                     |
| xml_etree_process    | 53.9 ms                                                | 58.3 ms: 1.08x slower                                                     |
| pickle_list          | 4.11 us                                                | 4.54 us: 1.10x slower                                                     |
| unpickle             | 13.7 us                                                | 15.6 us: 1.14x slower                                                     |
| xml_etree_generate   | 76.2 ms                                                | 93.5 ms: 1.23x slower                                                     |
| xml_etree_parse      | 158 ms                                                 | 570 ms: 3.60x slower                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 516 ms: 4.97x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.25x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-4591b30 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.47 ms: 1.11x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 6.89 ms: 1.15x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-4591b30 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-4591b30 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 147 us: 3.31x faster                                                      |
| generators               | 73.5 ms                                                | 28.7 ms: 2.56x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 480 ms: 1.92x faster                                                      |
| async_tree_io            | 1.30 sec                                               | 700 ms: 1.85x faster                                                      |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.76x faster                                                    |
| async_tree_none          | 526 ms                                                 | 340 ms: 1.55x faster                                                      |
| async_tree_memoization   | 627 ms                                                 | 431 ms: 1.46x faster                                                      |
| json_dumps               | 12.6 ms                                                | 9.75 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 586 ms: 1.26x faster                                                      |
| chaos                    | 69.2 ms                                                | 58.4 ms: 1.18x faster                                                     |
| coroutines               | 25.5 ms                                                | 22.0 ms: 1.16x faster                                                     |
| regex_effbot             | 3.99 ms                                                | 3.59 ms: 1.11x faster                                                     |
| comprehensions           | 22.4 us                                                | 20.4 us: 1.10x faster                                                     |
| deltablue                | 3.67 ms                                                | 3.33 ms: 1.10x faster                                                     |
| gc_traversal             | 4.02 ms                                                | 3.68 ms: 1.09x faster                                                     |
| raytrace                 | 297 ms                                                 | 272 ms: 1.09x faster                                                      |
| crypto_pyaes             | 74.7 ms                                                | 68.9 ms: 1.08x faster                                                     |
| sqlglot_parse            | 1.40 ms                                                | 1.30 ms: 1.08x faster                                                     |
| unpickle_pure_python     | 228 us                                                 | 213 us: 1.07x faster                                                      |
| coverage                 | 100 ms                                                 | 93.5 ms: 1.07x faster                                                     |
| hexiom                   | 6.37 ms                                                | 5.98 ms: 1.07x faster                                                     |
| richards_super           | 56.8 ms                                                | 53.3 ms: 1.06x faster                                                     |
| pycparser                | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                    |
| unpack_sequence          | 43.1 ns                                                | 40.7 ns: 1.06x faster                                                     |
| pidigits                 | 198 ms                                                 | 189 ms: 1.05x faster                                                      |
| nqueens                  | 83.4 ms                                                | 79.5 ms: 1.05x faster                                                     |
| json_loads               | 26.5 us                                                | 25.3 us: 1.05x faster                                                     |
| create_gc_cycles         | 1.49 ms                                                | 1.43 ms: 1.04x faster                                                     |
| docutils                 | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                    |
| pickle_pure_python       | 306 us                                                 | 294 us: 1.04x faster                                                      |
| logging_format           | 6.68 us                                                | 6.43 us: 1.04x faster                                                     |
| nbody                    | 93.1 ms                                                | 90.0 ms: 1.04x faster                                                     |
| json                     | 4.94 ms                                                | 4.79 ms: 1.03x faster                                                     |
| sqlglot_transpile        | 1.70 ms                                                | 1.66 ms: 1.02x faster                                                     |
| logging_simple           | 6.03 us                                                | 5.94 us: 1.02x faster                                                     |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.02x faster                                                      |
| regex_compile            | 138 ms                                                 | 137 ms: 1.01x faster                                                      |
| meteor_contest           | 107 ms                                                 | 106 ms: 1.01x faster                                                      |
| mdp                      | 2.62 sec                                               | 2.59 sec: 1.01x faster                                                    |
| unpickle_list            | 4.91 us                                                | 4.88 us: 1.01x faster                                                     |
| scimark_monte_carlo      | 68.1 ms                                                | 67.7 ms: 1.01x faster                                                     |
| go                       | 140 ms                                                 | 139 ms: 1.00x faster                                                      |
| bench_thread_pool        | 819 us                                                 | 824 us: 1.01x slower                                                      |
| regex_v8                 | 22.0 ms                                                | 22.3 ms: 1.01x slower                                                     |
| pprint_safe_repr         | 701 ms                                                 | 710 ms: 1.01x slower                                                      |
| sqlglot_optimize         | 53.1 ms                                                | 53.8 ms: 1.01x slower                                                     |
| richards                 | 45.7 ms                                                | 46.5 ms: 1.02x slower                                                     |
| logging_silent           | 101 ns                                                 | 103 ns: 1.02x slower                                                      |
| pickle_dict              | 31.1 us                                                | 31.6 us: 1.02x slower                                                     |
| scimark_sor              | 118 ms                                                 | 120 ms: 1.02x slower                                                      |
| scimark_lu               | 110 ms                                                 | 113 ms: 1.03x slower                                                      |
| pathlib                  | 18.2 ms                                                | 18.7 ms: 1.03x slower                                                     |
| deepcopy_memo            | 37.0 us                                                | 38.1 us: 1.03x slower                                                     |
| tomli_loads              | 2.22 sec                                               | 2.29 sec: 1.03x slower                                                    |
| deepcopy                 | 342 us                                                 | 356 us: 1.04x slower                                                      |
| spectral_norm            | 100 ms                                                 | 104 ms: 1.04x slower                                                      |
| dulwich_log              | 63.7 ms                                                | 66.4 ms: 1.04x slower                                                     |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.71 ms: 1.05x slower                                                     |
| pyflate                  | 418 ms                                                 | 438 ms: 1.05x slower                                                      |
| regex_dna                | 204 ms                                                 | 215 ms: 1.06x slower                                                      |
| pickle                   | 10.1 us                                                | 10.7 us: 1.06x slower                                                     |
| tornado_http             | 96.3 ms                                                | 103 ms: 1.07x slower                                                      |
| mako                     | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                     |
| xml_etree_process        | 53.9 ms                                                | 58.3 ms: 1.08x slower                                                     |
| deepcopy_reduce          | 2.94 us                                                | 3.19 us: 1.08x slower                                                     |
| sqlite_synth             | 2.52 us                                                | 2.74 us: 1.09x slower                                                     |
| scimark_fft              | 328 ms                                                 | 361 ms: 1.10x slower                                                      |
| pickle_list              | 4.11 us                                                | 4.54 us: 1.10x slower                                                     |
| python_startup           | 8.52 ms                                                | 9.47 ms: 1.11x slower                                                     |
| unpickle                 | 13.7 us                                                | 15.6 us: 1.14x slower                                                     |
| python_startup_no_site   | 6.01 ms                                                | 6.89 ms: 1.15x slower                                                     |
| async_generators         | 368 ms                                                 | 447 ms: 1.21x slower                                                      |
| telco                    | 6.58 ms                                                | 8.04 ms: 1.22x slower                                                     |
| xml_etree_generate       | 76.2 ms                                                | 93.5 ms: 1.23x slower                                                     |
| float                    | 77.2 ms                                                | 110 ms: 1.43x slower                                                      |
| dask                     | 360 ms                                                 | 520 ms: 1.44x slower                                                      |
| xml_etree_parse          | 158 ms                                                 | 570 ms: 3.60x slower                                                      |
| xml_etree_iterparse      | 104 ms                                                 | 516 ms: 4.97x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (4): fannkuch, bench_mp_pool, pprint_pformat, mypy2
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 66.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

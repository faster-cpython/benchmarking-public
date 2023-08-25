
# Results vs. 3.11.0

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: 58901ff
- commit date: 2023-08-12
- overall geometric mean: 1.08x faster
- HPT reliability: 95.83%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-58901ff |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.39 sec: 1.10x faster                                                    |
| tornado_http   | 96.3 ms                                                | 93.5 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-58901ff |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 71.9 ms: 1.07x faster                                                     |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                      |
| nbody          | 93.1 ms                                                | 89.8 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-58901ff |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.46 ms: 1.15x faster                                                     |
| regex_compile  | 138 ms                                                 | 136 ms: 1.01x faster                                                      |
| regex_v8       | 22.0 ms                                                | 22.7 ms: 1.03x slower                                                     |
| regex_dna      | 204 ms                                                 | 210 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-58901ff |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.75 ms: 1.29x faster                                                     |
| xml_etree_parse      | 158 ms                                                 | 141 ms: 1.13x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 93.8 ms: 1.11x faster                                                     |
| unpickle_pure_python | 228 us                                                 | 212 us: 1.08x faster                                                      |
| pickle_pure_python   | 306 us                                                 | 294 us: 1.04x faster                                                      |
| json_loads           | 26.5 us                                                | 25.6 us: 1.03x faster                                                     |
| pickle_dict          | 31.1 us                                                | 30.9 us: 1.01x faster                                                     |
| tomli_loads          | 2.22 sec                                               | 2.28 sec: 1.03x slower                                                    |
| pickle               | 10.1 us                                                | 10.4 us: 1.03x slower                                                     |
| unpickle_list        | 4.91 us                                                | 5.08 us: 1.03x slower                                                     |
| xml_etree_process    | 53.9 ms                                                | 56.4 ms: 1.05x slower                                                     |
| xml_etree_generate   | 76.2 ms                                                | 80.9 ms: 1.06x slower                                                     |
| pickle_list          | 4.11 us                                                | 4.51 us: 1.10x slower                                                     |
| unpickle             | 13.7 us                                                | 15.0 us: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-58901ff |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.28 ms: 1.09x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 6.81 ms: 1.13x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-58901ff |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-58901ff |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 146 us: 3.34x faster                                                      |
| generators               | 73.5 ms                                                | 28.1 ms: 2.62x faster                                                     |
| async_tree_io            | 1.30 sec                                               | 561 ms: 2.31x faster                                                      |
| async_tree_none          | 526 ms                                                 | 276 ms: 1.90x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 485 ms: 1.90x faster                                                      |
| async_tree_memoization   | 627 ms                                                 | 342 ms: 1.83x faster                                                      |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.78 sec: 1.76x faster                                                    |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 503 ms: 1.47x faster                                                      |
| json_dumps               | 12.6 ms                                                | 9.75 ms: 1.29x faster                                                     |
| mypy2                    | 420 ms                                                 | 338 ms: 1.24x faster                                                      |
| deltablue                | 3.67 ms                                                | 3.12 ms: 1.18x faster                                                     |
| chaos                    | 69.2 ms                                                | 59.0 ms: 1.17x faster                                                     |
| regex_effbot             | 3.99 ms                                                | 3.46 ms: 1.15x faster                                                     |
| coroutines               | 25.5 ms                                                | 22.3 ms: 1.15x faster                                                     |
| xml_etree_parse          | 158 ms                                                 | 141 ms: 1.13x faster                                                      |
| comprehensions           | 22.4 us                                                | 20.1 us: 1.12x faster                                                     |
| raytrace                 | 297 ms                                                 | 267 ms: 1.11x faster                                                      |
| xml_etree_iterparse      | 104 ms                                                 | 93.8 ms: 1.11x faster                                                     |
| sqlglot_parse            | 1.40 ms                                                | 1.28 ms: 1.10x faster                                                     |
| docutils                 | 2.63 sec                                               | 2.39 sec: 1.10x faster                                                    |
| pycparser                | 1.18 sec                                               | 1.09 sec: 1.09x faster                                                    |
| coverage                 | 100 ms                                                 | 92.8 ms: 1.08x faster                                                     |
| unpickle_pure_python     | 228 us                                                 | 212 us: 1.08x faster                                                      |
| crypto_pyaes             | 74.7 ms                                                | 69.4 ms: 1.08x faster                                                     |
| hexiom                   | 6.37 ms                                                | 5.93 ms: 1.08x faster                                                     |
| float                    | 77.2 ms                                                | 71.9 ms: 1.07x faster                                                     |
| sqlglot_transpile        | 1.70 ms                                                | 1.59 ms: 1.07x faster                                                     |
| gc_traversal             | 4.02 ms                                                | 3.78 ms: 1.06x faster                                                     |
| richards_super           | 56.8 ms                                                | 53.8 ms: 1.06x faster                                                     |
| pidigits                 | 198 ms                                                 | 189 ms: 1.05x faster                                                      |
| nqueens                  | 83.4 ms                                                | 79.9 ms: 1.04x faster                                                     |
| create_gc_cycles         | 1.49 ms                                                | 1.43 ms: 1.04x faster                                                     |
| pickle_pure_python       | 306 us                                                 | 294 us: 1.04x faster                                                      |
| nbody                    | 93.1 ms                                                | 89.8 ms: 1.04x faster                                                     |
| logging_format           | 6.68 us                                                | 6.44 us: 1.04x faster                                                     |
| json_loads               | 26.5 us                                                | 25.6 us: 1.03x faster                                                     |
| sqlglot_normalize        | 108 ms                                                 | 104 ms: 1.03x faster                                                      |
| mdp                      | 2.62 sec                                               | 2.53 sec: 1.03x faster                                                    |
| json                     | 4.94 ms                                                | 4.79 ms: 1.03x faster                                                     |
| tornado_http             | 96.3 ms                                                | 93.5 ms: 1.03x faster                                                     |
| logging_simple           | 6.03 us                                                | 5.88 us: 1.03x faster                                                     |
| go                       | 140 ms                                                 | 138 ms: 1.02x faster                                                      |
| regex_compile            | 138 ms                                                 | 136 ms: 1.01x faster                                                      |
| scimark_monte_carlo      | 68.1 ms                                                | 67.1 ms: 1.01x faster                                                     |
| sqlglot_optimize         | 53.1 ms                                                | 52.6 ms: 1.01x faster                                                     |
| pickle_dict              | 31.1 us                                                | 30.9 us: 1.01x faster                                                     |
| bench_thread_pool        | 819 us                                                 | 824 us: 1.01x slower                                                      |
| pprint_pformat           | 1.46 sec                                               | 1.47 sec: 1.01x slower                                                    |
| fannkuch                 | 388 ms                                                 | 392 ms: 1.01x slower                                                      |
| scimark_sor              | 118 ms                                                 | 120 ms: 1.02x slower                                                      |
| deepcopy_memo            | 37.0 us                                                | 37.7 us: 1.02x slower                                                     |
| pprint_safe_repr         | 701 ms                                                 | 716 ms: 1.02x slower                                                      |
| pathlib                  | 18.2 ms                                                | 18.7 ms: 1.02x slower                                                     |
| tomli_loads              | 2.22 sec                                               | 2.28 sec: 1.03x slower                                                    |
| regex_v8                 | 22.0 ms                                                | 22.7 ms: 1.03x slower                                                     |
| regex_dna                | 204 ms                                                 | 210 ms: 1.03x slower                                                      |
| pickle                   | 10.1 us                                                | 10.4 us: 1.03x slower                                                     |
| unpickle_list            | 4.91 us                                                | 5.08 us: 1.03x slower                                                     |
| dulwich_log              | 63.7 ms                                                | 65.9 ms: 1.04x slower                                                     |
| deepcopy                 | 342 us                                                 | 355 us: 1.04x slower                                                      |
| xml_etree_process        | 53.9 ms                                                | 56.4 ms: 1.05x slower                                                     |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.74 ms: 1.05x slower                                                     |
| richards                 | 45.7 ms                                                | 48.2 ms: 1.05x slower                                                     |
| xml_etree_generate       | 76.2 ms                                                | 80.9 ms: 1.06x slower                                                     |
| pyflate                  | 418 ms                                                 | 446 ms: 1.07x slower                                                      |
| mako                     | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                     |
| unpack_sequence          | 43.1 ns                                                | 46.2 ns: 1.07x slower                                                     |
| spectral_norm            | 100 ms                                                 | 108 ms: 1.08x slower                                                      |
| scimark_fft              | 328 ms                                                 | 357 ms: 1.09x slower                                                      |
| python_startup           | 8.52 ms                                                | 9.28 ms: 1.09x slower                                                     |
| sqlite_synth             | 2.52 us                                                | 2.75 us: 1.09x slower                                                     |
| deepcopy_reduce          | 2.94 us                                                | 3.22 us: 1.10x slower                                                     |
| pickle_list              | 4.11 us                                                | 4.51 us: 1.10x slower                                                     |
| unpickle                 | 13.7 us                                                | 15.0 us: 1.10x slower                                                     |
| python_startup_no_site   | 6.01 ms                                                | 6.81 ms: 1.13x slower                                                     |
| async_generators         | 368 ms                                                 | 426 ms: 1.16x slower                                                      |
| telco                    | 6.58 ms                                                | 7.92 ms: 1.20x slower                                                     |
| dask                     | 360 ms                                                 | 489 ms: 1.36x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (4): logging_silent, bench_mp_pool, scimark_lu, meteor_contest
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 95.83% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

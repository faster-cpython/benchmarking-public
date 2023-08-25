
# Results vs. 3.11.0

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: 13cce66
- commit date: 2023-08-12
- overall geometric mean: 1.08x faster
- HPT reliability: 87.85%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-13cce66 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.40 sec: 1.10x faster                                                    |
| tornado_http   | 96.3 ms                                                | 94.4 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-13cce66 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.7 ms: 1.06x faster                                                     |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                      |
| nbody          | 93.1 ms                                                | 89.9 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-13cce66 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.72 ms: 1.07x faster                                                     |
| regex_compile  | 138 ms                                                 | 137 ms: 1.01x faster                                                      |
| regex_v8       | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                     |
| regex_dna      | 204 ms                                                 | 209 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-13cce66 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.84 ms: 1.28x faster                                                     |
| xml_etree_parse      | 158 ms                                                 | 140 ms: 1.13x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 94.5 ms: 1.10x faster                                                     |
| unpickle_pure_python | 228 us                                                 | 214 us: 1.07x faster                                                      |
| pickle_pure_python   | 306 us                                                 | 298 us: 1.03x faster                                                      |
| json_loads           | 26.5 us                                                | 26.1 us: 1.02x faster                                                     |
| unpickle_list        | 4.91 us                                                | 4.94 us: 1.01x slower                                                     |
| pickle_dict          | 31.1 us                                                | 31.8 us: 1.02x slower                                                     |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                                     |
| xml_etree_process    | 53.9 ms                                                | 56.7 ms: 1.05x slower                                                     |
| tomli_loads          | 2.22 sec                                               | 2.34 sec: 1.05x slower                                                    |
| xml_etree_generate   | 76.2 ms                                                | 81.8 ms: 1.07x slower                                                     |
| pickle_list          | 4.11 us                                                | 4.58 us: 1.11x slower                                                     |
| unpickle             | 13.7 us                                                | 15.4 us: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-13cce66 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.36 ms: 1.10x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 6.84 ms: 1.14x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-13cce66 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-13cce66 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 146 us: 3.32x faster                                                      |
| generators               | 73.5 ms                                                | 28.5 ms: 2.58x faster                                                     |
| async_tree_io            | 1.30 sec                                               | 563 ms: 2.30x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 482 ms: 1.91x faster                                                      |
| async_tree_none          | 526 ms                                                 | 276 ms: 1.91x faster                                                      |
| async_tree_memoization   | 627 ms                                                 | 342 ms: 1.84x faster                                                      |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.78 sec: 1.76x faster                                                    |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 500 ms: 1.48x faster                                                      |
| json_dumps               | 12.6 ms                                                | 9.84 ms: 1.28x faster                                                     |
| mypy2                    | 420 ms                                                 | 340 ms: 1.23x faster                                                      |
| deltablue                | 3.67 ms                                                | 3.14 ms: 1.17x faster                                                     |
| chaos                    | 69.2 ms                                                | 59.3 ms: 1.17x faster                                                     |
| coroutines               | 25.5 ms                                                | 22.0 ms: 1.16x faster                                                     |
| gc_traversal             | 4.02 ms                                                | 3.51 ms: 1.15x faster                                                     |
| xml_etree_parse          | 158 ms                                                 | 140 ms: 1.13x faster                                                      |
| raytrace                 | 297 ms                                                 | 269 ms: 1.10x faster                                                      |
| xml_etree_iterparse      | 104 ms                                                 | 94.5 ms: 1.10x faster                                                     |
| comprehensions           | 22.4 us                                                | 20.5 us: 1.10x faster                                                     |
| docutils                 | 2.63 sec                                               | 2.40 sec: 1.10x faster                                                    |
| pycparser                | 1.18 sec                                               | 1.08 sec: 1.10x faster                                                    |
| sqlglot_parse            | 1.40 ms                                                | 1.28 ms: 1.09x faster                                                     |
| crypto_pyaes             | 74.7 ms                                                | 68.4 ms: 1.09x faster                                                     |
| richards_super           | 56.8 ms                                                | 52.7 ms: 1.08x faster                                                     |
| regex_effbot             | 3.99 ms                                                | 3.72 ms: 1.07x faster                                                     |
| coverage                 | 100 ms                                                 | 93.4 ms: 1.07x faster                                                     |
| sqlglot_transpile        | 1.70 ms                                                | 1.59 ms: 1.07x faster                                                     |
| unpickle_pure_python     | 228 us                                                 | 214 us: 1.07x faster                                                      |
| float                    | 77.2 ms                                                | 72.7 ms: 1.06x faster                                                     |
| create_gc_cycles         | 1.49 ms                                                | 1.42 ms: 1.05x faster                                                     |
| pidigits                 | 198 ms                                                 | 189 ms: 1.05x faster                                                      |
| hexiom                   | 6.37 ms                                                | 6.09 ms: 1.05x faster                                                     |
| nbody                    | 93.1 ms                                                | 89.9 ms: 1.04x faster                                                     |
| nqueens                  | 83.4 ms                                                | 81.1 ms: 1.03x faster                                                     |
| pickle_pure_python       | 306 us                                                 | 298 us: 1.03x faster                                                      |
| logging_format           | 6.68 us                                                | 6.52 us: 1.03x faster                                                     |
| logging_simple           | 6.03 us                                                | 5.89 us: 1.02x faster                                                     |
| tornado_http             | 96.3 ms                                                | 94.4 ms: 1.02x faster                                                     |
| go                       | 140 ms                                                 | 137 ms: 1.02x faster                                                      |
| json                     | 4.94 ms                                                | 4.85 ms: 1.02x faster                                                     |
| json_loads               | 26.5 us                                                | 26.1 us: 1.02x faster                                                     |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.02x faster                                                      |
| scimark_monte_carlo      | 68.1 ms                                                | 67.2 ms: 1.01x faster                                                     |
| regex_compile            | 138 ms                                                 | 137 ms: 1.01x faster                                                      |
| sqlglot_optimize         | 53.1 ms                                                | 52.9 ms: 1.00x faster                                                     |
| unpickle_list            | 4.91 us                                                | 4.94 us: 1.01x slower                                                     |
| richards                 | 45.7 ms                                                | 46.2 ms: 1.01x slower                                                     |
| bench_thread_pool        | 819 us                                                 | 829 us: 1.01x slower                                                      |
| pprint_pformat           | 1.46 sec                                               | 1.48 sec: 1.01x slower                                                    |
| fannkuch                 | 388 ms                                                 | 394 ms: 1.02x slower                                                      |
| regex_v8                 | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                     |
| pathlib                  | 18.2 ms                                                | 18.6 ms: 1.02x slower                                                     |
| pickle_dict              | 31.1 us                                                | 31.8 us: 1.02x slower                                                     |
| unpack_sequence          | 43.1 ns                                                | 44.0 ns: 1.02x slower                                                     |
| scimark_sor              | 118 ms                                                 | 121 ms: 1.02x slower                                                      |
| deepcopy_memo            | 37.0 us                                                | 37.9 us: 1.02x slower                                                     |
| deepcopy                 | 342 us                                                 | 351 us: 1.02x slower                                                      |
| regex_dna                | 204 ms                                                 | 209 ms: 1.03x slower                                                      |
| scimark_lu               | 110 ms                                                 | 113 ms: 1.03x slower                                                      |
| mdp                      | 2.62 sec                                               | 2.69 sec: 1.03x slower                                                    |
| pprint_safe_repr         | 701 ms                                                 | 723 ms: 1.03x slower                                                      |
| logging_silent           | 101 ns                                                 | 105 ns: 1.04x slower                                                      |
| pickle                   | 10.1 us                                                | 10.5 us: 1.04x slower                                                     |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.69 ms: 1.04x slower                                                     |
| dulwich_log              | 63.7 ms                                                | 66.8 ms: 1.05x slower                                                     |
| xml_etree_process        | 53.9 ms                                                | 56.7 ms: 1.05x slower                                                     |
| tomli_loads              | 2.22 sec                                               | 2.34 sec: 1.05x slower                                                    |
| pyflate                  | 418 ms                                                 | 444 ms: 1.06x slower                                                      |
| spectral_norm            | 100 ms                                                 | 107 ms: 1.07x slower                                                      |
| deepcopy_reduce          | 2.94 us                                                | 3.15 us: 1.07x slower                                                     |
| xml_etree_generate       | 76.2 ms                                                | 81.8 ms: 1.07x slower                                                     |
| scimark_fft              | 328 ms                                                 | 355 ms: 1.08x slower                                                      |
| mako                     | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                     |
| sqlite_synth             | 2.52 us                                                | 2.74 us: 1.09x slower                                                     |
| python_startup           | 8.52 ms                                                | 9.36 ms: 1.10x slower                                                     |
| pickle_list              | 4.11 us                                                | 4.58 us: 1.11x slower                                                     |
| unpickle                 | 13.7 us                                                | 15.4 us: 1.13x slower                                                     |
| python_startup_no_site   | 6.01 ms                                                | 6.84 ms: 1.14x slower                                                     |
| async_generators         | 368 ms                                                 | 433 ms: 1.18x slower                                                      |
| telco                    | 6.58 ms                                                | 7.89 ms: 1.20x slower                                                     |
| dask                     | 360 ms                                                 | 485 ms: 1.35x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (2): bench_mp_pool, meteor_contest
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 87.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

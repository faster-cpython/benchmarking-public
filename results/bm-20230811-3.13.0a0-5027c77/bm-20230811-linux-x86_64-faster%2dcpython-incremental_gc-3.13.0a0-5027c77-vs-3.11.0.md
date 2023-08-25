
# Results vs. 3.11.0

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: 5027c77
- commit date: 2023-08-11
- overall geometric mean: 1.08x faster
- HPT reliability: 87.66%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-5027c77 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.38 sec: 1.10x faster                                                    |
| tornado_http   | 96.3 ms                                                | 94.1 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-5027c77 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.7 ms: 1.06x faster                                                     |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-5027c77 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.66 ms: 1.09x faster                                                     |
| regex_compile  | 138 ms                                                 | 137 ms: 1.01x faster                                                      |
| regex_v8       | 22.0 ms                                                | 22.4 ms: 1.02x slower                                                     |
| regex_dna      | 204 ms                                                 | 210 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-5027c77 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.76 ms: 1.29x faster                                                     |
| xml_etree_parse      | 158 ms                                                 | 140 ms: 1.14x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 94.0 ms: 1.11x faster                                                     |
| unpickle_pure_python | 228 us                                                 | 212 us: 1.07x faster                                                      |
| json_loads           | 26.5 us                                                | 25.4 us: 1.04x faster                                                     |
| pickle_pure_python   | 306 us                                                 | 299 us: 1.02x faster                                                      |
| pickle_dict          | 31.1 us                                                | 31.5 us: 1.01x slower                                                     |
| tomli_loads          | 2.22 sec                                               | 2.30 sec: 1.04x slower                                                    |
| unpickle_list        | 4.91 us                                                | 5.13 us: 1.04x slower                                                     |
| pickle               | 10.1 us                                                | 10.6 us: 1.05x slower                                                     |
| xml_etree_process    | 53.9 ms                                                | 56.6 ms: 1.05x slower                                                     |
| xml_etree_generate   | 76.2 ms                                                | 80.9 ms: 1.06x slower                                                     |
| unpickle             | 13.7 us                                                | 15.0 us: 1.09x slower                                                     |
| pickle_list          | 4.11 us                                                | 4.61 us: 1.12x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-5027c77 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.30 ms: 1.09x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 6.79 ms: 1.13x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-5027c77 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-5027c77 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 144 us: 3.37x faster                                                      |
| generators               | 73.5 ms                                                | 28.0 ms: 2.62x faster                                                     |
| async_tree_io            | 1.30 sec                                               | 562 ms: 2.31x faster                                                      |
| async_tree_none          | 526 ms                                                 | 274 ms: 1.92x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 483 ms: 1.91x faster                                                      |
| async_tree_memoization   | 627 ms                                                 | 337 ms: 1.86x faster                                                      |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.78 sec: 1.76x faster                                                    |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 498 ms: 1.48x faster                                                      |
| json_dumps               | 12.6 ms                                                | 9.76 ms: 1.29x faster                                                     |
| mypy2                    | 420 ms                                                 | 338 ms: 1.24x faster                                                      |
| deltablue                | 3.67 ms                                                | 3.08 ms: 1.19x faster                                                     |
| chaos                    | 69.2 ms                                                | 58.9 ms: 1.17x faster                                                     |
| gc_traversal             | 4.02 ms                                                | 3.46 ms: 1.16x faster                                                     |
| xml_etree_parse          | 158 ms                                                 | 140 ms: 1.14x faster                                                      |
| coroutines               | 25.5 ms                                                | 22.5 ms: 1.13x faster                                                     |
| raytrace                 | 297 ms                                                 | 266 ms: 1.11x faster                                                      |
| pycparser                | 1.18 sec                                               | 1.06 sec: 1.11x faster                                                    |
| comprehensions           | 22.4 us                                                | 20.3 us: 1.11x faster                                                     |
| xml_etree_iterparse      | 104 ms                                                 | 94.0 ms: 1.11x faster                                                     |
| docutils                 | 2.63 sec                                               | 2.38 sec: 1.10x faster                                                    |
| sqlglot_parse            | 1.40 ms                                                | 1.28 ms: 1.10x faster                                                     |
| regex_effbot             | 3.99 ms                                                | 3.66 ms: 1.09x faster                                                     |
| create_gc_cycles         | 1.49 ms                                                | 1.37 ms: 1.08x faster                                                     |
| unpickle_pure_python     | 228 us                                                 | 212 us: 1.07x faster                                                      |
| sqlglot_transpile        | 1.70 ms                                                | 1.60 ms: 1.07x faster                                                     |
| float                    | 77.2 ms                                                | 72.7 ms: 1.06x faster                                                     |
| coverage                 | 100 ms                                                 | 94.3 ms: 1.06x faster                                                     |
| richards_super           | 56.8 ms                                                | 53.7 ms: 1.06x faster                                                     |
| hexiom                   | 6.37 ms                                                | 6.04 ms: 1.06x faster                                                     |
| pidigits                 | 198 ms                                                 | 189 ms: 1.05x faster                                                      |
| crypto_pyaes             | 74.7 ms                                                | 71.5 ms: 1.05x faster                                                     |
| json_loads               | 26.5 us                                                | 25.4 us: 1.04x faster                                                     |
| logging_format           | 6.68 us                                                | 6.44 us: 1.04x faster                                                     |
| nqueens                  | 83.4 ms                                                | 81.4 ms: 1.02x faster                                                     |
| logging_simple           | 6.03 us                                                | 5.89 us: 1.02x faster                                                     |
| go                       | 140 ms                                                 | 137 ms: 1.02x faster                                                      |
| tornado_http             | 96.3 ms                                                | 94.1 ms: 1.02x faster                                                     |
| pickle_pure_python       | 306 us                                                 | 299 us: 1.02x faster                                                      |
| json                     | 4.94 ms                                                | 4.85 ms: 1.02x faster                                                     |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.02x faster                                                      |
| scimark_monte_carlo      | 68.1 ms                                                | 67.3 ms: 1.01x faster                                                     |
| regex_compile            | 138 ms                                                 | 137 ms: 1.01x faster                                                      |
| sqlglot_optimize         | 53.1 ms                                                | 52.9 ms: 1.00x faster                                                     |
| pprint_pformat           | 1.46 sec                                               | 1.47 sec: 1.01x slower                                                    |
| bench_thread_pool        | 819 us                                                 | 828 us: 1.01x slower                                                      |
| pickle_dict              | 31.1 us                                                | 31.5 us: 1.01x slower                                                     |
| regex_v8                 | 22.0 ms                                                | 22.4 ms: 1.02x slower                                                     |
| richards                 | 45.7 ms                                                | 46.6 ms: 1.02x slower                                                     |
| fannkuch                 | 388 ms                                                 | 395 ms: 1.02x slower                                                      |
| pprint_safe_repr         | 701 ms                                                 | 716 ms: 1.02x slower                                                      |
| scimark_lu               | 110 ms                                                 | 112 ms: 1.02x slower                                                      |
| logging_silent           | 101 ns                                                 | 103 ns: 1.02x slower                                                      |
| pathlib                  | 18.2 ms                                                | 18.7 ms: 1.02x slower                                                     |
| deepcopy_memo            | 37.0 us                                                | 38.0 us: 1.03x slower                                                     |
| regex_dna                | 204 ms                                                 | 210 ms: 1.03x slower                                                      |
| tomli_loads              | 2.22 sec                                               | 2.30 sec: 1.04x slower                                                    |
| scimark_sor              | 118 ms                                                 | 122 ms: 1.04x slower                                                      |
| dulwich_log              | 63.7 ms                                                | 66.0 ms: 1.04x slower                                                     |
| deepcopy                 | 342 us                                                 | 355 us: 1.04x slower                                                      |
| mdp                      | 2.62 sec                                               | 2.72 sec: 1.04x slower                                                    |
| unpickle_list            | 4.91 us                                                | 5.13 us: 1.04x slower                                                     |
| pyflate                  | 418 ms                                                 | 438 ms: 1.05x slower                                                      |
| pickle                   | 10.1 us                                                | 10.6 us: 1.05x slower                                                     |
| xml_etree_process        | 53.9 ms                                                | 56.6 ms: 1.05x slower                                                     |
| xml_etree_generate       | 76.2 ms                                                | 80.9 ms: 1.06x slower                                                     |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.78 ms: 1.06x slower                                                     |
| mako                     | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                     |
| spectral_norm            | 100 ms                                                 | 108 ms: 1.08x slower                                                      |
| sqlite_synth             | 2.52 us                                                | 2.74 us: 1.09x slower                                                     |
| python_startup           | 8.52 ms                                                | 9.30 ms: 1.09x slower                                                     |
| deepcopy_reduce          | 2.94 us                                                | 3.21 us: 1.09x slower                                                     |
| unpickle                 | 13.7 us                                                | 15.0 us: 1.09x slower                                                     |
| scimark_fft              | 328 ms                                                 | 361 ms: 1.10x slower                                                      |
| pickle_list              | 4.11 us                                                | 4.61 us: 1.12x slower                                                     |
| async_generators         | 368 ms                                                 | 416 ms: 1.13x slower                                                      |
| unpack_sequence          | 43.1 ns                                                | 48.7 ns: 1.13x slower                                                     |
| python_startup_no_site   | 6.01 ms                                                | 6.79 ms: 1.13x slower                                                     |
| telco                    | 6.58 ms                                                | 8.00 ms: 1.22x slower                                                     |
| dask                     | 360 ms                                                 | 484 ms: 1.35x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (3): meteor_contest, nbody, bench_mp_pool
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 87.66% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

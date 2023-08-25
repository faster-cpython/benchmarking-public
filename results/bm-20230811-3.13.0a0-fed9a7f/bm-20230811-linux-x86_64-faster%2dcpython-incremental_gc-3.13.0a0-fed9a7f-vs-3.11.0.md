
# Results vs. 3.11.0

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: fed9a7f
- commit date: 2023-08-11
- overall geometric mean: 1.03x faster
- HPT reliability: 51.20%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-fed9a7f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                    |
| tornado_http   | 96.3 ms                                                | 99.6 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-fed9a7f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.7 ms: 1.06x faster                                                     |
| pidigits       | 198 ms                                                 | 201 ms: 1.01x slower                                                      |
| float          | 77.2 ms                                                | 87.7 ms: 1.14x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-fed9a7f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.57 ms: 1.12x faster                                                     |
| regex_compile  | 138 ms                                                 | 137 ms: 1.01x faster                                                      |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                                      |
| regex_v8       | 22.0 ms                                                | 22.8 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-fed9a7f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.68 ms: 1.30x faster                                                     |
| unpickle_pure_python | 228 us                                                 | 211 us: 1.08x faster                                                      |
| json_loads           | 26.5 us                                                | 25.3 us: 1.05x faster                                                     |
| pickle_pure_python   | 306 us                                                 | 293 us: 1.04x faster                                                      |
| pickle_dict          | 31.1 us                                                | 31.6 us: 1.01x slower                                                     |
| unpickle_list        | 4.91 us                                                | 4.99 us: 1.02x slower                                                     |
| tomli_loads          | 2.22 sec                                               | 2.30 sec: 1.04x slower                                                    |
| pickle               | 10.1 us                                                | 10.6 us: 1.05x slower                                                     |
| unpickle             | 13.7 us                                                | 15.0 us: 1.10x slower                                                     |
| xml_etree_process    | 53.9 ms                                                | 60.0 ms: 1.11x slower                                                     |
| pickle_list          | 4.11 us                                                | 4.63 us: 1.13x slower                                                     |
| xml_etree_generate   | 76.2 ms                                                | 88.1 ms: 1.16x slower                                                     |
| xml_etree_parse      | 158 ms                                                 | 346 ms: 2.18x slower                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 323 ms: 3.11x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.16x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-fed9a7f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.52 ms: 1.12x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 6.92 ms: 1.15x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-fed9a7f |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.07x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-fed9a7f |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 146 us: 3.33x faster                                                      |
| generators               | 73.5 ms                                                | 28.2 ms: 2.60x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 484 ms: 1.91x faster                                                      |
| async_tree_io            | 1.30 sec                                               | 706 ms: 1.84x faster                                                      |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                    |
| async_tree_none          | 526 ms                                                 | 327 ms: 1.61x faster                                                      |
| async_tree_memoization   | 627 ms                                                 | 446 ms: 1.41x faster                                                      |
| json_dumps               | 12.6 ms                                                | 9.68 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 578 ms: 1.28x faster                                                      |
| chaos                    | 69.2 ms                                                | 59.4 ms: 1.16x faster                                                     |
| coroutines               | 25.5 ms                                                | 21.9 ms: 1.16x faster                                                     |
| deltablue                | 3.67 ms                                                | 3.21 ms: 1.14x faster                                                     |
| regex_effbot             | 3.99 ms                                                | 3.57 ms: 1.12x faster                                                     |
| raytrace                 | 297 ms                                                 | 269 ms: 1.10x faster                                                      |
| comprehensions           | 22.4 us                                                | 20.5 us: 1.09x faster                                                     |
| richards_super           | 56.8 ms                                                | 52.6 ms: 1.08x faster                                                     |
| unpickle_pure_python     | 228 us                                                 | 211 us: 1.08x faster                                                      |
| coverage                 | 100 ms                                                 | 93.3 ms: 1.07x faster                                                     |
| sqlglot_parse            | 1.40 ms                                                | 1.31 ms: 1.07x faster                                                     |
| nbody                    | 93.1 ms                                                | 87.7 ms: 1.06x faster                                                     |
| crypto_pyaes             | 74.7 ms                                                | 70.4 ms: 1.06x faster                                                     |
| hexiom                   | 6.37 ms                                                | 6.03 ms: 1.06x faster                                                     |
| nqueens                  | 83.4 ms                                                | 79.2 ms: 1.05x faster                                                     |
| sqlglot_transpile        | 1.70 ms                                                | 1.62 ms: 1.05x faster                                                     |
| json_loads               | 26.5 us                                                | 25.3 us: 1.05x faster                                                     |
| pickle_pure_python       | 306 us                                                 | 293 us: 1.04x faster                                                      |
| logging_format           | 6.68 us                                                | 6.43 us: 1.04x faster                                                     |
| json                     | 4.94 ms                                                | 4.76 ms: 1.04x faster                                                     |
| pycparser                | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                    |
| create_gc_cycles         | 1.49 ms                                                | 1.44 ms: 1.03x faster                                                     |
| sqlglot_normalize        | 108 ms                                                 | 105 ms: 1.03x faster                                                      |
| mdp                      | 2.62 sec                                               | 2.55 sec: 1.02x faster                                                    |
| logging_simple           | 6.03 us                                                | 5.89 us: 1.02x faster                                                     |
| docutils                 | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                    |
| go                       | 140 ms                                                 | 137 ms: 1.02x faster                                                      |
| gc_traversal             | 4.02 ms                                                | 3.94 ms: 1.02x faster                                                     |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.02x faster                                                      |
| regex_compile            | 138 ms                                                 | 137 ms: 1.01x faster                                                      |
| bench_thread_pool        | 819 us                                                 | 822 us: 1.00x slower                                                      |
| fannkuch                 | 388 ms                                                 | 389 ms: 1.00x slower                                                      |
| pprint_pformat           | 1.46 sec                                               | 1.46 sec: 1.00x slower                                                    |
| pprint_safe_repr         | 701 ms                                                 | 710 ms: 1.01x slower                                                      |
| scimark_sor              | 118 ms                                                 | 120 ms: 1.01x slower                                                      |
| pickle_dict              | 31.1 us                                                | 31.6 us: 1.01x slower                                                     |
| pidigits                 | 198 ms                                                 | 201 ms: 1.01x slower                                                      |
| scimark_lu               | 110 ms                                                 | 111 ms: 1.01x slower                                                      |
| richards                 | 45.7 ms                                                | 46.4 ms: 1.01x slower                                                     |
| deepcopy                 | 342 us                                                 | 347 us: 1.02x slower                                                      |
| deepcopy_memo            | 37.0 us                                                | 37.6 us: 1.02x slower                                                     |
| logging_silent           | 101 ns                                                 | 103 ns: 1.02x slower                                                      |
| scimark_monte_carlo      | 68.1 ms                                                | 69.1 ms: 1.02x slower                                                     |
| unpickle_list            | 4.91 us                                                | 4.99 us: 1.02x slower                                                     |
| regex_dna                | 204 ms                                                 | 208 ms: 1.02x slower                                                      |
| pathlib                  | 18.2 ms                                                | 18.7 ms: 1.02x slower                                                     |
| unpack_sequence          | 43.1 ns                                                | 44.4 ns: 1.03x slower                                                     |
| regex_v8                 | 22.0 ms                                                | 22.8 ms: 1.03x slower                                                     |
| tornado_http             | 96.3 ms                                                | 99.6 ms: 1.03x slower                                                     |
| dulwich_log              | 63.7 ms                                                | 65.9 ms: 1.04x slower                                                     |
| tomli_loads              | 2.22 sec                                               | 2.30 sec: 1.04x slower                                                    |
| pickle                   | 10.1 us                                                | 10.6 us: 1.05x slower                                                     |
| spectral_norm            | 100 ms                                                 | 105 ms: 1.05x slower                                                      |
| mako                     | 10.1 ms                                                | 10.7 ms: 1.07x slower                                                     |
| deepcopy_reduce          | 2.94 us                                                | 3.15 us: 1.07x slower                                                     |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.82 ms: 1.07x slower                                                     |
| pyflate                  | 418 ms                                                 | 449 ms: 1.07x slower                                                      |
| scimark_fft              | 328 ms                                                 | 356 ms: 1.08x slower                                                      |
| sqlite_synth             | 2.52 us                                                | 2.76 us: 1.09x slower                                                     |
| unpickle                 | 13.7 us                                                | 15.0 us: 1.10x slower                                                     |
| xml_etree_process        | 53.9 ms                                                | 60.0 ms: 1.11x slower                                                     |
| python_startup           | 8.52 ms                                                | 9.52 ms: 1.12x slower                                                     |
| pickle_list              | 4.11 us                                                | 4.63 us: 1.13x slower                                                     |
| float                    | 77.2 ms                                                | 87.7 ms: 1.14x slower                                                     |
| python_startup_no_site   | 6.01 ms                                                | 6.92 ms: 1.15x slower                                                     |
| xml_etree_generate       | 76.2 ms                                                | 88.1 ms: 1.16x slower                                                     |
| async_generators         | 368 ms                                                 | 432 ms: 1.17x slower                                                      |
| telco                    | 6.58 ms                                                | 7.72 ms: 1.17x slower                                                     |
| dask                     | 360 ms                                                 | 524 ms: 1.45x slower                                                      |
| xml_etree_parse          | 158 ms                                                 | 346 ms: 2.18x slower                                                      |
| xml_etree_iterparse      | 104 ms                                                 | 323 ms: 3.11x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (3): mypy2, sqlglot_optimize, bench_mp_pool
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 51.20% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

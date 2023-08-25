
# Results vs. 3.11.0

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: acf9079
- commit date: 2023-08-13
- overall geometric mean: 1.07x faster
- HPT reliability: 92.11%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-acf9079 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.43 sec: 1.08x faster                                                    |
| tornado_http   | 96.3 ms                                                | 93.6 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-acf9079 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                      |
| nbody          | 93.1 ms                                                | 89.6 ms: 1.04x faster                                                     |
| float          | 77.2 ms                                                | 75.4 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-acf9079 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.59 ms: 1.11x faster                                                     |
| regex_compile  | 138 ms                                                 | 137 ms: 1.01x faster                                                      |
| regex_v8       | 22.0 ms                                                | 22.2 ms: 1.01x slower                                                     |
| regex_dna      | 204 ms                                                 | 209 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-acf9079 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.84 ms: 1.28x faster                                                     |
| unpickle_pure_python | 228 us                                                 | 215 us: 1.06x faster                                                      |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.04x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 100 ms: 1.04x faster                                                      |
| json_loads           | 26.5 us                                                | 25.7 us: 1.03x faster                                                     |
| pickle_pure_python   | 306 us                                                 | 299 us: 1.02x faster                                                      |
| pickle_dict          | 31.1 us                                                | 31.6 us: 1.02x slower                                                     |
| pickle               | 10.1 us                                                | 10.4 us: 1.04x slower                                                     |
| unpickle_list        | 4.91 us                                                | 5.11 us: 1.04x slower                                                     |
| tomli_loads          | 2.22 sec                                               | 2.33 sec: 1.05x slower                                                    |
| xml_etree_process    | 53.9 ms                                                | 57.2 ms: 1.06x slower                                                     |
| xml_etree_generate   | 76.2 ms                                                | 83.3 ms: 1.09x slower                                                     |
| pickle_list          | 4.11 us                                                | 4.55 us: 1.11x slower                                                     |
| unpickle             | 13.7 us                                                | 15.2 us: 1.11x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-acf9079 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.25 ms: 1.09x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 6.73 ms: 1.12x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-acf9079 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-acf9079 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 149 us: 3.27x faster                                                      |
| generators               | 73.5 ms                                                | 28.5 ms: 2.57x faster                                                     |
| async_tree_io            | 1.30 sec                                               | 677 ms: 1.91x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 485 ms: 1.90x faster                                                      |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                    |
| async_tree_none          | 526 ms                                                 | 311 ms: 1.69x faster                                                      |
| async_tree_memoization   | 627 ms                                                 | 395 ms: 1.59x faster                                                      |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 562 ms: 1.32x faster                                                      |
| json_dumps               | 12.6 ms                                                | 9.84 ms: 1.28x faster                                                     |
| mypy2                    | 420 ms                                                 | 347 ms: 1.21x faster                                                      |
| chaos                    | 69.2 ms                                                | 58.8 ms: 1.18x faster                                                     |
| deltablue                | 3.67 ms                                                | 3.14 ms: 1.17x faster                                                     |
| coroutines               | 25.5 ms                                                | 22.2 ms: 1.15x faster                                                     |
| regex_effbot             | 3.99 ms                                                | 3.59 ms: 1.11x faster                                                     |
| comprehensions           | 22.4 us                                                | 20.2 us: 1.11x faster                                                     |
| gc_traversal             | 4.02 ms                                                | 3.64 ms: 1.10x faster                                                     |
| raytrace                 | 297 ms                                                 | 270 ms: 1.10x faster                                                      |
| crypto_pyaes             | 74.7 ms                                                | 68.3 ms: 1.09x faster                                                     |
| coverage                 | 100 ms                                                 | 91.8 ms: 1.09x faster                                                     |
| sqlglot_parse            | 1.40 ms                                                | 1.29 ms: 1.09x faster                                                     |
| docutils                 | 2.63 sec                                               | 2.43 sec: 1.08x faster                                                    |
| richards_super           | 56.8 ms                                                | 52.9 ms: 1.07x faster                                                     |
| hexiom                   | 6.37 ms                                                | 5.97 ms: 1.07x faster                                                     |
| unpickle_pure_python     | 228 us                                                 | 215 us: 1.06x faster                                                      |
| sqlglot_transpile        | 1.70 ms                                                | 1.61 ms: 1.06x faster                                                     |
| pidigits                 | 198 ms                                                 | 189 ms: 1.05x faster                                                      |
| nqueens                  | 83.4 ms                                                | 80.2 ms: 1.04x faster                                                     |
| pycparser                | 1.18 sec                                               | 1.14 sec: 1.04x faster                                                    |
| nbody                    | 93.1 ms                                                | 89.6 ms: 1.04x faster                                                     |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.04x faster                                                      |
| xml_etree_iterparse      | 104 ms                                                 | 100 ms: 1.04x faster                                                      |
| json_loads               | 26.5 us                                                | 25.7 us: 1.03x faster                                                     |
| create_gc_cycles         | 1.49 ms                                                | 1.44 ms: 1.03x faster                                                     |
| mdp                      | 2.62 sec                                               | 2.54 sec: 1.03x faster                                                    |
| tornado_http             | 96.3 ms                                                | 93.6 ms: 1.03x faster                                                     |
| float                    | 77.2 ms                                                | 75.4 ms: 1.02x faster                                                     |
| logging_format           | 6.68 us                                                | 6.53 us: 1.02x faster                                                     |
| pickle_pure_python       | 306 us                                                 | 299 us: 1.02x faster                                                      |
| scimark_monte_carlo      | 68.1 ms                                                | 66.8 ms: 1.02x faster                                                     |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.01x faster                                                      |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.01x faster                                                      |
| logging_simple           | 6.03 us                                                | 5.95 us: 1.01x faster                                                     |
| json                     | 4.94 ms                                                | 4.88 ms: 1.01x faster                                                     |
| regex_compile            | 138 ms                                                 | 137 ms: 1.01x faster                                                      |
| go                       | 140 ms                                                 | 139 ms: 1.01x faster                                                      |
| sqlglot_optimize         | 53.1 ms                                                | 52.9 ms: 1.00x faster                                                     |
| bench_thread_pool        | 819 us                                                 | 822 us: 1.00x slower                                                      |
| regex_v8                 | 22.0 ms                                                | 22.2 ms: 1.01x slower                                                     |
| pathlib                  | 18.2 ms                                                | 18.4 ms: 1.01x slower                                                     |
| pickle_dict              | 31.1 us                                                | 31.6 us: 1.02x slower                                                     |
| fannkuch                 | 388 ms                                                 | 394 ms: 1.02x slower                                                      |
| pprint_pformat           | 1.46 sec                                               | 1.48 sec: 1.02x slower                                                    |
| scimark_lu               | 110 ms                                                 | 112 ms: 1.02x slower                                                      |
| deepcopy_memo            | 37.0 us                                                | 37.8 us: 1.02x slower                                                     |
| regex_dna                | 204 ms                                                 | 209 ms: 1.02x slower                                                      |
| richards                 | 45.7 ms                                                | 46.8 ms: 1.02x slower                                                     |
| logging_silent           | 101 ns                                                 | 104 ns: 1.03x slower                                                      |
| deepcopy                 | 342 us                                                 | 351 us: 1.03x slower                                                      |
| scimark_sor              | 118 ms                                                 | 121 ms: 1.03x slower                                                      |
| pprint_safe_repr         | 701 ms                                                 | 725 ms: 1.03x slower                                                      |
| pickle                   | 10.1 us                                                | 10.4 us: 1.04x slower                                                     |
| dulwich_log              | 63.7 ms                                                | 66.3 ms: 1.04x slower                                                     |
| unpickle_list            | 4.91 us                                                | 5.11 us: 1.04x slower                                                     |
| tomli_loads              | 2.22 sec                                               | 2.33 sec: 1.05x slower                                                    |
| pyflate                  | 418 ms                                                 | 444 ms: 1.06x slower                                                      |
| xml_etree_process        | 53.9 ms                                                | 57.2 ms: 1.06x slower                                                     |
| mako                     | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                     |
| spectral_norm            | 100 ms                                                 | 106 ms: 1.06x slower                                                      |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.86 ms: 1.08x slower                                                     |
| scimark_fft              | 328 ms                                                 | 356 ms: 1.08x slower                                                      |
| python_startup           | 8.52 ms                                                | 9.25 ms: 1.09x slower                                                     |
| deepcopy_reduce          | 2.94 us                                                | 3.19 us: 1.09x slower                                                     |
| xml_etree_generate       | 76.2 ms                                                | 83.3 ms: 1.09x slower                                                     |
| pickle_list              | 4.11 us                                                | 4.55 us: 1.11x slower                                                     |
| unpickle                 | 13.7 us                                                | 15.2 us: 1.11x slower                                                     |
| sqlite_synth             | 2.52 us                                                | 2.82 us: 1.12x slower                                                     |
| python_startup_no_site   | 6.01 ms                                                | 6.73 ms: 1.12x slower                                                     |
| async_generators         | 368 ms                                                 | 431 ms: 1.17x slower                                                      |
| telco                    | 6.58 ms                                                | 7.96 ms: 1.21x slower                                                     |
| dask                     | 360 ms                                                 | 494 ms: 1.37x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.07x faster                                                              |

Benchmark hidden because not significant (2): bench_mp_pool, unpack_sequence
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 92.11% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

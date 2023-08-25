
# Results vs. 3.10.4

- fork: faster-cpython
- ref: deepcopy_demateriali
- machine: linux-x86_64
- commit hash: 87a3230
- commit date: 2023-08-10
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-87a3230 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.62 sec: 1.21x faster                                                          |
| tornado_http   | 127 ms                                                 | 95.0 ms: 1.34x faster                                                           |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-87a3230 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 90.5 ms: 1.56x faster                                                           |
| float          | 111 ms                                                 | 80.2 ms: 1.38x faster                                                           |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-87a3230 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                                            |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.15x faster                                                           |
| regex_dna      | 222 ms                                                 | 207 ms: 1.07x faster                                                            |
| regex_effbot   | 3.23 ms                                                | 3.57 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-87a3230 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 300 us: 1.52x faster                                                            |
| unpickle_pure_python | 300 us                                                 | 213 us: 1.41x faster                                                            |
| tomli_loads          | 2.92 sec                                               | 2.08 sec: 1.40x faster                                                          |
| json_dumps           | 13.5 ms                                                | 9.88 ms: 1.37x faster                                                           |
| xml_etree_process    | 74.9 ms                                                | 56.7 ms: 1.32x faster                                                           |
| xml_etree_generate   | 94.2 ms                                                | 82.4 ms: 1.14x faster                                                           |
| json_loads           | 28.8 us                                                | 25.6 us: 1.12x faster                                                           |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                                            |
| pickle_list          | 4.56 us                                                | 4.60 us: 1.01x slower                                                           |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                                           |
| unpickle_list        | 4.82 us                                                | 5.12 us: 1.06x slower                                                           |
| unpickle             | 14.1 us                                                | 15.2 us: 1.07x slower                                                           |
| pickle_dict          | 27.3 us                                                | 32.0 us: 1.17x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-87a3230 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.39 ms: 1.51x faster                                                           |
| python_startup_no_site | 5.82 ms                                                | 6.88 ms: 1.18x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-87a3230 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-87a3230 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 145 us: 3.51x faster                                                            |
| generators               | 76.8 ms                                                | 28.7 ms: 2.67x faster                                                           |
| deltablue                | 7.42 ms                                                | 3.25 ms: 2.29x faster                                                           |
| asyncio_tcp              | 925 ms                                                 | 483 ms: 1.92x faster                                                            |
| chaos                    | 106 ms                                                 | 59.5 ms: 1.78x faster                                                           |
| logging_silent           | 175 ns                                                 | 100 ns: 1.74x faster                                                            |
| crypto_pyaes             | 118 ms                                                 | 69.9 ms: 1.69x faster                                                           |
| raytrace                 | 464 ms                                                 | 274 ms: 1.69x faster                                                            |
| richards_super           | 90.7 ms                                                | 53.7 ms: 1.69x faster                                                           |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                          |
| async_tree_none          | 717 ms                                                 | 435 ms: 1.65x faster                                                            |
| go                       | 229 ms                                                 | 140 ms: 1.63x faster                                                            |
| sqlglot_parse            | 2.06 ms                                                | 1.28 ms: 1.60x faster                                                           |
| scimark_monte_carlo      | 108 ms                                                 | 67.5 ms: 1.60x faster                                                           |
| scimark_sor              | 197 ms                                                 | 123 ms: 1.60x faster                                                            |
| hexiom                   | 9.53 ms                                                | 6.03 ms: 1.58x faster                                                           |
| richards                 | 74.9 ms                                                | 47.8 ms: 1.57x faster                                                           |
| nbody                    | 142 ms                                                 | 90.5 ms: 1.56x faster                                                           |
| sqlglot_transpile        | 2.45 ms                                                | 1.60 ms: 1.53x faster                                                           |
| async_tree_memoization   | 854 ms                                                 | 562 ms: 1.52x faster                                                            |
| pickle_pure_python       | 455 us                                                 | 300 us: 1.52x faster                                                            |
| python_startup           | 14.2 ms                                                | 9.39 ms: 1.51x faster                                                           |
| async_tree_io            | 1.77 sec                                               | 1.18 sec: 1.50x faster                                                          |
| pyflate                  | 673 ms                                                 | 452 ms: 1.49x faster                                                            |
| coroutines               | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                           |
| scimark_lu               | 163 ms                                                 | 113 ms: 1.45x faster                                                            |
| unpack_sequence          | 64.7 ns                                                | 44.9 ns: 1.44x faster                                                           |
| spectral_norm            | 150 ms                                                 | 106 ms: 1.42x faster                                                            |
| deepcopy_memo            | 52.3 us                                                | 37.0 us: 1.42x faster                                                           |
| unpickle_pure_python     | 300 us                                                 | 213 us: 1.41x faster                                                            |
| tomli_loads              | 2.92 sec                                               | 2.08 sec: 1.40x faster                                                          |
| logging_format           | 8.91 us                                                | 6.41 us: 1.39x faster                                                           |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                           |
| float                    | 111 ms                                                 | 80.2 ms: 1.38x faster                                                           |
| logging_simple           | 8.07 us                                                | 5.88 us: 1.37x faster                                                           |
| json_dumps               | 13.5 ms                                                | 9.88 ms: 1.37x faster                                                           |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 697 ms: 1.36x faster                                                            |
| tornado_http             | 127 ms                                                 | 95.0 ms: 1.34x faster                                                           |
| pprint_pformat           | 1.99 sec                                               | 1.48 sec: 1.34x faster                                                          |
| xml_etree_process        | 74.9 ms                                                | 56.7 ms: 1.32x faster                                                           |
| pycparser                | 1.50 sec                                               | 1.14 sec: 1.31x faster                                                          |
| pprint_safe_repr         | 955 ms                                                 | 726 ms: 1.31x faster                                                            |
| sqlglot_normalize        | 135 ms                                                 | 104 ms: 1.30x faster                                                            |
| regex_compile            | 177 ms                                                 | 137 ms: 1.29x faster                                                            |
| comprehensions           | 26.8 us                                                | 20.9 us: 1.28x faster                                                           |
| nqueens                  | 100 ms                                                 | 79.2 ms: 1.26x faster                                                           |
| deepcopy                 | 442 us                                                 | 354 us: 1.25x faster                                                            |
| sqlglot_optimize         | 65.3 ms                                                | 52.6 ms: 1.24x faster                                                           |
| fannkuch                 | 486 ms                                                 | 392 ms: 1.24x faster                                                            |
| docutils                 | 3.17 sec                                               | 2.62 sec: 1.21x faster                                                          |
| deepcopy_reduce          | 3.82 us                                                | 3.19 us: 1.20x faster                                                           |
| scimark_fft              | 424 ms                                                 | 354 ms: 1.20x faster                                                            |
| bench_thread_pool        | 947 us                                                 | 818 us: 1.16x faster                                                            |
| dulwich_log              | 75.9 ms                                                | 65.7 ms: 1.16x faster                                                           |
| regex_v8                 | 25.0 ms                                                | 21.9 ms: 1.15x faster                                                           |
| xml_etree_generate       | 94.2 ms                                                | 82.4 ms: 1.14x faster                                                           |
| json_loads               | 28.8 us                                                | 25.6 us: 1.12x faster                                                           |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.91 ms: 1.11x faster                                                           |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.11x faster                                                           |
| json                     | 5.42 ms                                                | 4.91 ms: 1.10x faster                                                           |
| xml_etree_iterparse      | 111 ms                                                 | 102 ms: 1.09x faster                                                            |
| pathlib                  | 20.0 ms                                                | 18.4 ms: 1.09x faster                                                           |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.09x faster                                                            |
| regex_dna                | 222 ms                                                 | 207 ms: 1.07x faster                                                            |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                                            |
| sqlite_synth             | 2.93 us                                                | 2.75 us: 1.07x faster                                                           |
| mdp                      | 2.82 sec                                               | 2.69 sec: 1.05x faster                                                          |
| pidigits                 | 190 ms                                                 | 189 ms: 1.01x faster                                                            |
| pickle_list              | 4.56 us                                                | 4.60 us: 1.01x slower                                                           |
| gc_traversal             | 3.84 ms                                                | 3.90 ms: 1.01x slower                                                           |
| pickle                   | 10.3 us                                                | 10.6 us: 1.03x slower                                                           |
| async_generators         | 425 ms                                                 | 449 ms: 1.06x slower                                                            |
| unpickle_list            | 4.82 us                                                | 5.12 us: 1.06x slower                                                           |
| unpickle                 | 14.1 us                                                | 15.2 us: 1.07x slower                                                           |
| regex_effbot             | 3.23 ms                                                | 3.57 ms: 1.11x slower                                                           |
| coverage                 | 72.8 ms                                                | 84.7 ms: 1.16x slower                                                           |
| pickle_dict              | 27.3 us                                                | 32.0 us: 1.17x slower                                                           |
| python_startup_no_site   | 5.82 ms                                                | 6.88 ms: 1.18x slower                                                           |
| telco                    | 6.54 ms                                                | 7.80 ms: 1.19x slower                                                           |
| dask                     | 423 ms                                                 | 518 ms: 1.23x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                                    |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.23x

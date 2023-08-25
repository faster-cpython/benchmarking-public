
# Results vs. 3.10.4

- fork: faster-cpython
- ref: deepcopy_demateriali
- machine: linux-x86_64
- commit hash: ab2df81
- commit date: 2023-08-10
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-ab2df81 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.62 sec: 1.21x faster                                                          |
| tornado_http   | 127 ms                                                 | 95.2 ms: 1.34x faster                                                           |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-ab2df81 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.0 ms: 1.59x faster                                                           |
| float          | 111 ms                                                 | 80.2 ms: 1.38x faster                                                           |
| pidigits       | 190 ms                                                 | 201 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-ab2df81 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                                            |
| regex_v8       | 25.0 ms                                                | 23.3 ms: 1.07x faster                                                           |
| regex_dna      | 222 ms                                                 | 214 ms: 1.04x faster                                                            |
| regex_effbot   | 3.23 ms                                                | 3.55 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-ab2df81 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 303 us: 1.50x faster                                                            |
| unpickle_pure_python | 300 us                                                 | 215 us: 1.40x faster                                                            |
| tomli_loads          | 2.92 sec                                               | 2.10 sec: 1.39x faster                                                          |
| json_dumps           | 13.5 ms                                                | 9.77 ms: 1.39x faster                                                           |
| xml_etree_process    | 74.9 ms                                                | 57.3 ms: 1.31x faster                                                           |
| json_loads           | 28.8 us                                                | 25.5 us: 1.13x faster                                                           |
| xml_etree_generate   | 94.2 ms                                                | 83.4 ms: 1.13x faster                                                           |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                                            |
| pickle_list          | 4.56 us                                                | 4.53 us: 1.01x faster                                                           |
| unpickle             | 14.1 us                                                | 14.9 us: 1.05x slower                                                           |
| unpickle_list        | 4.82 us                                                | 5.09 us: 1.06x slower                                                           |
| pickle_dict          | 27.3 us                                                | 30.6 us: 1.12x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                                    |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-ab2df81 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.32 ms: 1.52x faster                                                           |
| python_startup_no_site | 5.82 ms                                                | 6.82 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.14x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-ab2df81 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.37x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-ab2df81 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 148 us: 3.45x faster                                                            |
| generators               | 76.8 ms                                                | 29.3 ms: 2.62x faster                                                           |
| deltablue                | 7.42 ms                                                | 3.44 ms: 2.16x faster                                                           |
| asyncio_tcp              | 925 ms                                                 | 485 ms: 1.91x faster                                                            |
| chaos                    | 106 ms                                                 | 60.0 ms: 1.77x faster                                                           |
| logging_silent           | 175 ns                                                 | 103 ns: 1.71x faster                                                            |
| crypto_pyaes             | 118 ms                                                 | 70.2 ms: 1.69x faster                                                           |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                          |
| raytrace                 | 464 ms                                                 | 276 ms: 1.68x faster                                                            |
| richards_super           | 90.7 ms                                                | 54.5 ms: 1.66x faster                                                           |
| go                       | 229 ms                                                 | 139 ms: 1.64x faster                                                            |
| async_tree_none          | 717 ms                                                 | 440 ms: 1.63x faster                                                            |
| sqlglot_parse            | 2.06 ms                                                | 1.28 ms: 1.61x faster                                                           |
| scimark_monte_carlo      | 108 ms                                                 | 67.3 ms: 1.61x faster                                                           |
| nbody                    | 142 ms                                                 | 89.0 ms: 1.59x faster                                                           |
| scimark_sor              | 197 ms                                                 | 125 ms: 1.57x faster                                                            |
| hexiom                   | 9.53 ms                                                | 6.09 ms: 1.56x faster                                                           |
| richards                 | 74.9 ms                                                | 48.5 ms: 1.54x faster                                                           |
| sqlglot_transpile        | 2.45 ms                                                | 1.60 ms: 1.53x faster                                                           |
| python_startup           | 14.2 ms                                                | 9.32 ms: 1.52x faster                                                           |
| async_tree_memoization   | 854 ms                                                 | 565 ms: 1.51x faster                                                            |
| pyflate                  | 673 ms                                                 | 447 ms: 1.50x faster                                                            |
| pickle_pure_python       | 455 us                                                 | 303 us: 1.50x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 1.20 sec: 1.48x faster                                                          |
| coroutines               | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                           |
| scimark_lu               | 163 ms                                                 | 113 ms: 1.45x faster                                                            |
| unpickle_pure_python     | 300 us                                                 | 215 us: 1.40x faster                                                            |
| deepcopy_memo            | 52.3 us                                                | 37.6 us: 1.39x faster                                                           |
| logging_simple           | 8.07 us                                                | 5.81 us: 1.39x faster                                                           |
| tomli_loads              | 2.92 sec                                               | 2.10 sec: 1.39x faster                                                          |
| json_dumps               | 13.5 ms                                                | 9.77 ms: 1.39x faster                                                           |
| logging_format           | 8.91 us                                                | 6.44 us: 1.38x faster                                                           |
| spectral_norm            | 150 ms                                                 | 108 ms: 1.38x faster                                                            |
| float                    | 111 ms                                                 | 80.2 ms: 1.38x faster                                                           |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.37x faster                                                           |
| unpack_sequence          | 64.7 ns                                                | 47.3 ns: 1.37x faster                                                           |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 699 ms: 1.36x faster                                                            |
| pprint_pformat           | 1.99 sec                                               | 1.48 sec: 1.34x faster                                                          |
| tornado_http             | 127 ms                                                 | 95.2 ms: 1.34x faster                                                           |
| pprint_safe_repr         | 955 ms                                                 | 724 ms: 1.32x faster                                                            |
| xml_etree_process        | 74.9 ms                                                | 57.3 ms: 1.31x faster                                                           |
| comprehensions           | 26.8 us                                                | 20.7 us: 1.30x faster                                                           |
| regex_compile            | 177 ms                                                 | 137 ms: 1.29x faster                                                            |
| sqlglot_normalize        | 135 ms                                                 | 105 ms: 1.29x faster                                                            |
| pycparser                | 1.50 sec                                               | 1.17 sec: 1.29x faster                                                          |
| fannkuch                 | 486 ms                                                 | 383 ms: 1.27x faster                                                            |
| nqueens                  | 100 ms                                                 | 79.7 ms: 1.25x faster                                                           |
| deepcopy                 | 442 us                                                 | 354 us: 1.25x faster                                                            |
| sqlglot_optimize         | 65.3 ms                                                | 53.0 ms: 1.23x faster                                                           |
| deepcopy_reduce          | 3.82 us                                                | 3.15 us: 1.21x faster                                                           |
| docutils                 | 3.17 sec                                               | 2.62 sec: 1.21x faster                                                          |
| scimark_fft              | 424 ms                                                 | 358 ms: 1.18x faster                                                            |
| bench_thread_pool        | 947 us                                                 | 816 us: 1.16x faster                                                            |
| dulwich_log              | 75.9 ms                                                | 66.1 ms: 1.15x faster                                                           |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.78 ms: 1.14x faster                                                           |
| create_gc_cycles         | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                           |
| json_loads               | 28.8 us                                                | 25.5 us: 1.13x faster                                                           |
| xml_etree_generate       | 94.2 ms                                                | 83.4 ms: 1.13x faster                                                           |
| json                     | 5.42 ms                                                | 4.85 ms: 1.12x faster                                                           |
| pathlib                  | 20.0 ms                                                | 18.4 ms: 1.09x faster                                                           |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                            |
| sqlite_synth             | 2.93 us                                                | 2.72 us: 1.08x faster                                                           |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.08x faster                                                            |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                                            |
| regex_v8                 | 25.0 ms                                                | 23.3 ms: 1.07x faster                                                           |
| mdp                      | 2.82 sec                                               | 2.65 sec: 1.06x faster                                                          |
| gc_traversal             | 3.84 ms                                                | 3.67 ms: 1.05x faster                                                           |
| regex_dna                | 222 ms                                                 | 214 ms: 1.04x faster                                                            |
| pickle_list              | 4.56 us                                                | 4.53 us: 1.01x faster                                                           |
| unpickle                 | 14.1 us                                                | 14.9 us: 1.05x slower                                                           |
| unpickle_list            | 4.82 us                                                | 5.09 us: 1.06x slower                                                           |
| pidigits                 | 190 ms                                                 | 201 ms: 1.06x slower                                                            |
| async_generators         | 425 ms                                                 | 454 ms: 1.07x slower                                                            |
| regex_effbot             | 3.23 ms                                                | 3.55 ms: 1.10x slower                                                           |
| pickle_dict              | 27.3 us                                                | 30.6 us: 1.12x slower                                                           |
| python_startup_no_site   | 5.82 ms                                                | 6.82 ms: 1.17x slower                                                           |
| coverage                 | 72.8 ms                                                | 85.8 ms: 1.18x slower                                                           |
| dask                     | 423 ms                                                 | 520 ms: 1.23x slower                                                            |
| telco                    | 6.54 ms                                                | 8.19 ms: 1.25x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                                    |

Benchmark hidden because not significant (3): bench_mp_pool, pickle, mypy2
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

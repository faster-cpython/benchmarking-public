
# Results vs. 3.10.4

- fork: brandtbucher
- ref: not_none
- machine: linux-x86_64
- commit hash: 806df38
- commit date: 2023-07-10
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.67 sec: 1.19x faster                                          |
| tornado_http   | 127 ms                                                 | 97.4 ms: 1.31x faster                                           |
| Geometric mean | (ref)                                                  | 1.25x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.4 ms: 1.58x faster                                           |
| float          | 111 ms                                                 | 78.7 ms: 1.40x faster                                           |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                  | 1.29x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 138 ms: 1.28x faster                                            |
| regex_v8       | 25.0 ms                                                | 23.0 ms: 1.09x faster                                           |
| regex_dna      | 222 ms                                                 | 210 ms: 1.05x faster                                            |
| regex_effbot   | 3.23 ms                                                | 3.57 ms: 1.11x slower                                           |
| Geometric mean | (ref)                                                  | 1.07x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 296 us: 1.54x faster                                            |
| unpickle_pure_python | 300 us                                                 | 211 us: 1.42x faster                                            |
| json_dumps           | 13.5 ms                                                | 9.88 ms: 1.37x faster                                           |
| xml_etree_process    | 74.9 ms                                                | 57.4 ms: 1.31x faster                                           |
| tomli_loads          | 2.92 sec                                               | 2.28 sec: 1.28x faster                                          |
| json_loads           | 28.8 us                                                | 25.7 us: 1.12x faster                                           |
| xml_etree_generate   | 94.2 ms                                                | 84.6 ms: 1.11x faster                                           |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                            |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                            |
| pickle_list          | 4.56 us                                                | 4.49 us: 1.02x faster                                           |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                           |
| unpickle             | 14.1 us                                                | 14.8 us: 1.05x slower                                           |
| unpickle_list        | 4.82 us                                                | 5.12 us: 1.06x slower                                           |
| pickle_dict          | 27.3 us                                                | 31.9 us: 1.17x slower                                           |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.17 ms: 1.54x faster                                           |
| python_startup_no_site | 5.82 ms                                                | 6.67 ms: 1.15x slower                                           |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.38x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 146 us: 3.49x faster                                            |
| generators               | 76.8 ms                                                | 29.0 ms: 2.64x faster                                           |
| deltablue                | 7.42 ms                                                | 3.26 ms: 2.27x faster                                           |
| asyncio_tcp              | 925 ms                                                 | 507 ms: 1.83x faster                                            |
| chaos                    | 106 ms                                                 | 59.7 ms: 1.78x faster                                           |
| logging_silent           | 175 ns                                                 | 102 ns: 1.72x faster                                            |
| raytrace                 | 464 ms                                                 | 271 ms: 1.71x faster                                            |
| crypto_pyaes             | 118 ms                                                 | 69.6 ms: 1.70x faster                                           |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.78 sec: 1.69x faster                                          |
| go                       | 229 ms                                                 | 137 ms: 1.67x faster                                            |
| richards_super           | 90.7 ms                                                | 54.3 ms: 1.67x faster                                           |
| scimark_sor              | 197 ms                                                 | 120 ms: 1.64x faster                                            |
| scimark_monte_carlo      | 108 ms                                                 | 67.4 ms: 1.61x faster                                           |
| hexiom                   | 9.53 ms                                                | 5.95 ms: 1.60x faster                                           |
| sqlglot_parse            | 2.06 ms                                                | 1.30 ms: 1.59x faster                                           |
| nbody                    | 142 ms                                                 | 89.4 ms: 1.58x faster                                           |
| richards                 | 74.9 ms                                                | 47.8 ms: 1.57x faster                                           |
| python_startup           | 14.2 ms                                                | 9.17 ms: 1.54x faster                                           |
| pickle_pure_python       | 455 us                                                 | 296 us: 1.54x faster                                            |
| sqlglot_transpile        | 2.45 ms                                                | 1.61 ms: 1.52x faster                                           |
| pyflate                  | 673 ms                                                 | 446 ms: 1.51x faster                                            |
| async_tree_io            | 1.77 sec                                               | 1.18 sec: 1.50x faster                                          |
| async_tree_none          | 717 ms                                                 | 479 ms: 1.50x faster                                            |
| scimark_lu               | 163 ms                                                 | 110 ms: 1.48x faster                                            |
| async_tree_memoization   | 854 ms                                                 | 584 ms: 1.46x faster                                            |
| spectral_norm            | 150 ms                                                 | 104 ms: 1.45x faster                                            |
| unpickle_pure_python     | 300 us                                                 | 211 us: 1.42x faster                                            |
| coroutines               | 31.8 ms                                                | 22.6 ms: 1.41x faster                                           |
| float                    | 111 ms                                                 | 78.7 ms: 1.40x faster                                           |
| deepcopy_memo            | 52.3 us                                                | 37.4 us: 1.40x faster                                           |
| unpack_sequence          | 64.7 ns                                                | 47.0 ns: 1.38x faster                                           |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.38x faster                                           |
| json_dumps               | 13.5 ms                                                | 9.88 ms: 1.37x faster                                           |
| logging_format           | 8.91 us                                                | 6.54 us: 1.36x faster                                           |
| logging_simple           | 8.07 us                                                | 5.96 us: 1.35x faster                                           |
| pprint_pformat           | 1.99 sec                                               | 1.49 sec: 1.33x faster                                          |
| comprehensions           | 26.8 us                                                | 20.2 us: 1.33x faster                                           |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 717 ms: 1.33x faster                                            |
| pprint_safe_repr         | 955 ms                                                 | 725 ms: 1.32x faster                                            |
| tornado_http             | 127 ms                                                 | 97.4 ms: 1.31x faster                                           |
| xml_etree_process        | 74.9 ms                                                | 57.4 ms: 1.31x faster                                           |
| pycparser                | 1.50 sec                                               | 1.16 sec: 1.30x faster                                          |
| regex_compile            | 177 ms                                                 | 138 ms: 1.28x faster                                            |
| tomli_loads              | 2.92 sec                                               | 2.28 sec: 1.28x faster                                          |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.27x faster                                            |
| mypy2                    | 428 ms                                                 | 338 ms: 1.27x faster                                            |
| nqueens                  | 100 ms                                                 | 79.2 ms: 1.26x faster                                           |
| deepcopy                 | 442 us                                                 | 352 us: 1.25x faster                                            |
| fannkuch                 | 486 ms                                                 | 389 ms: 1.25x faster                                            |
| sqlglot_optimize         | 65.3 ms                                                | 53.0 ms: 1.23x faster                                           |
| scimark_fft              | 424 ms                                                 | 354 ms: 1.20x faster                                            |
| deepcopy_reduce          | 3.82 us                                                | 3.21 us: 1.19x faster                                           |
| docutils                 | 3.17 sec                                               | 2.67 sec: 1.19x faster                                          |
| bench_thread_pool        | 947 us                                                 | 816 us: 1.16x faster                                            |
| dulwich_log              | 75.9 ms                                                | 66.4 ms: 1.14x faster                                           |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.79 ms: 1.14x faster                                           |
| create_gc_cycles         | 1.67 ms                                                | 1.48 ms: 1.13x faster                                           |
| json_loads               | 28.8 us                                                | 25.7 us: 1.12x faster                                           |
| xml_etree_generate       | 94.2 ms                                                | 84.6 ms: 1.11x faster                                           |
| json                     | 5.42 ms                                                | 4.92 ms: 1.10x faster                                           |
| mdp                      | 2.82 sec                                               | 2.58 sec: 1.10x faster                                          |
| regex_v8                 | 25.0 ms                                                | 23.0 ms: 1.09x faster                                           |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.08x faster                                            |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                            |
| pathlib                  | 20.0 ms                                                | 18.5 ms: 1.08x faster                                           |
| sqlite_synth             | 2.93 us                                                | 2.73 us: 1.07x faster                                           |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                            |
| regex_dna                | 222 ms                                                 | 210 ms: 1.05x faster                                            |
| pickle_list              | 4.56 us                                                | 4.49 us: 1.02x faster                                           |
| pickle                   | 10.3 us                                                | 10.6 us: 1.03x slower                                           |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                            |
| async_generators         | 425 ms                                                 | 443 ms: 1.04x slower                                            |
| unpickle                 | 14.1 us                                                | 14.8 us: 1.05x slower                                           |
| gc_traversal             | 3.84 ms                                                | 4.07 ms: 1.06x slower                                           |
| unpickle_list            | 4.82 us                                                | 5.12 us: 1.06x slower                                           |
| regex_effbot             | 3.23 ms                                                | 3.57 ms: 1.11x slower                                           |
| telco                    | 6.54 ms                                                | 7.30 ms: 1.12x slower                                           |
| python_startup_no_site   | 5.82 ms                                                | 6.67 ms: 1.15x slower                                           |
| pickle_dict              | 27.3 us                                                | 31.9 us: 1.17x slower                                           |
| dask                     | 423 ms                                                 | 523 ms: 1.24x slower                                            |
| coverage                 | 72.8 ms                                                | 94.0 ms: 1.29x slower                                           |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                    |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

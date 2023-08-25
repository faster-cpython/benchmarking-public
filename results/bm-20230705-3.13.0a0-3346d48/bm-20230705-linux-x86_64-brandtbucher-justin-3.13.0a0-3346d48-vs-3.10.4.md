
# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin
- machine: linux-x86_64
- commit hash: 3346d48
- commit date: 2023-07-05
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.71 sec: 1.17x faster                                        |
| tornado_http   | 127 ms                                                 | 99.1 ms: 1.29x faster                                         |
| Geometric mean | (ref)                                                  | 1.23x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 93.1 ms: 1.52x faster                                         |
| float          | 111 ms                                                 | 88.9 ms: 1.24x faster                                         |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                  | 1.22x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 142 ms: 1.24x faster                                          |
| regex_v8       | 25.0 ms                                                | 23.4 ms: 1.07x faster                                         |
| regex_dna      | 222 ms                                                 | 212 ms: 1.05x faster                                          |
| regex_effbot   | 3.23 ms                                                | 3.69 ms: 1.14x slower                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 315 us: 1.45x faster                                          |
| json_dumps           | 13.5 ms                                                | 9.83 ms: 1.38x faster                                         |
| unpickle_pure_python | 300 us                                                 | 219 us: 1.37x faster                                          |
| xml_etree_process    | 74.9 ms                                                | 58.9 ms: 1.27x faster                                         |
| tomli_loads          | 2.92 sec                                               | 2.37 sec: 1.23x faster                                        |
| json_loads           | 28.8 us                                                | 25.0 us: 1.15x faster                                         |
| xml_etree_generate   | 94.2 ms                                                | 86.9 ms: 1.08x faster                                         |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                          |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                          |
| unpickle_list        | 4.82 us                                                | 4.87 us: 1.01x slower                                         |
| unpickle             | 14.1 us                                                | 14.8 us: 1.05x slower                                         |
| pickle_dict          | 27.3 us                                                | 32.5 us: 1.19x slower                                         |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                  |

Benchmark hidden because not significant (2): pickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.43 ms: 1.50x faster                                         |
| python_startup_no_site | 5.82 ms                                                | 6.83 ms: 1.17x slower                                         |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 12.6 ms: 1.17x faster                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 145 us: 3.51x faster                                          |
| generators               | 76.8 ms                                                | 29.1 ms: 2.64x faster                                         |
| deltablue                | 7.42 ms                                                | 3.64 ms: 2.04x faster                                         |
| asyncio_tcp              | 925 ms                                                 | 516 ms: 1.79x faster                                          |
| richards_super           | 90.7 ms                                                | 50.8 ms: 1.79x faster                                         |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                        |
| richards                 | 74.9 ms                                                | 44.8 ms: 1.67x faster                                         |
| logging_silent           | 175 ns                                                 | 105 ns: 1.66x faster                                          |
| chaos                    | 106 ms                                                 | 64.8 ms: 1.64x faster                                         |
| go                       | 229 ms                                                 | 143 ms: 1.60x faster                                          |
| raytrace                 | 464 ms                                                 | 297 ms: 1.56x faster                                          |
| scimark_sor              | 197 ms                                                 | 127 ms: 1.55x faster                                          |
| nbody                    | 142 ms                                                 | 93.1 ms: 1.52x faster                                         |
| sqlglot_parse            | 2.06 ms                                                | 1.37 ms: 1.51x faster                                         |
| python_startup           | 14.2 ms                                                | 9.43 ms: 1.50x faster                                         |
| scimark_monte_carlo      | 108 ms                                                 | 72.3 ms: 1.50x faster                                         |
| sqlglot_transpile        | 2.45 ms                                                | 1.69 ms: 1.45x faster                                         |
| pickle_pure_python       | 455 us                                                 | 315 us: 1.45x faster                                          |
| async_tree_none          | 717 ms                                                 | 500 ms: 1.43x faster                                          |
| hexiom                   | 9.53 ms                                                | 6.66 ms: 1.43x faster                                         |
| async_tree_io            | 1.77 sec                                               | 1.25 sec: 1.42x faster                                        |
| unpack_sequence          | 64.7 ns                                                | 45.7 ns: 1.42x faster                                         |
| coroutines               | 31.8 ms                                                | 22.5 ms: 1.41x faster                                         |
| async_tree_memoization   | 854 ms                                                 | 608 ms: 1.41x faster                                          |
| pyflate                  | 673 ms                                                 | 485 ms: 1.39x faster                                          |
| crypto_pyaes             | 118 ms                                                 | 86.0 ms: 1.38x faster                                         |
| json_dumps               | 13.5 ms                                                | 9.83 ms: 1.38x faster                                         |
| unpickle_pure_python     | 300 us                                                 | 219 us: 1.37x faster                                          |
| logging_format           | 8.91 us                                                | 6.51 us: 1.37x faster                                         |
| logging_simple           | 8.07 us                                                | 5.97 us: 1.35x faster                                         |
| spectral_norm            | 150 ms                                                 | 111 ms: 1.35x faster                                          |
| pycparser                | 1.50 sec                                               | 1.14 sec: 1.32x faster                                        |
| pprint_pformat           | 1.99 sec                                               | 1.51 sec: 1.31x faster                                        |
| pprint_safe_repr         | 955 ms                                                 | 741 ms: 1.29x faster                                          |
| tornado_http             | 127 ms                                                 | 99.1 ms: 1.29x faster                                         |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 746 ms: 1.27x faster                                          |
| xml_etree_process        | 74.9 ms                                                | 58.9 ms: 1.27x faster                                         |
| sqlglot_normalize        | 135 ms                                                 | 107 ms: 1.26x faster                                          |
| mypy2                    | 428 ms                                                 | 343 ms: 1.25x faster                                          |
| regex_compile            | 177 ms                                                 | 142 ms: 1.24x faster                                          |
| float                    | 111 ms                                                 | 88.9 ms: 1.24x faster                                         |
| tomli_loads              | 2.92 sec                                               | 2.37 sec: 1.23x faster                                        |
| deepcopy                 | 442 us                                                 | 360 us: 1.23x faster                                          |
| scimark_lu               | 163 ms                                                 | 133 ms: 1.23x faster                                          |
| sqlglot_optimize         | 65.3 ms                                                | 53.6 ms: 1.22x faster                                         |
| nqueens                  | 100 ms                                                 | 83.7 ms: 1.19x faster                                         |
| mako                     | 14.8 ms                                                | 12.6 ms: 1.17x faster                                         |
| deepcopy_reduce          | 3.82 us                                                | 3.26 us: 1.17x faster                                         |
| docutils                 | 3.17 sec                                               | 2.71 sec: 1.17x faster                                        |
| dulwich_log              | 75.9 ms                                                | 65.2 ms: 1.17x faster                                         |
| json_loads               | 28.8 us                                                | 25.0 us: 1.15x faster                                         |
| comprehensions           | 26.8 us                                                | 23.4 us: 1.15x faster                                         |
| bench_thread_pool        | 947 us                                                 | 832 us: 1.14x faster                                          |
| json                     | 5.42 ms                                                | 4.79 ms: 1.13x faster                                         |
| scimark_fft              | 424 ms                                                 | 375 ms: 1.13x faster                                          |
| fannkuch                 | 486 ms                                                 | 437 ms: 1.11x faster                                          |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.11x faster                                         |
| mdp                      | 2.82 sec                                               | 2.56 sec: 1.10x faster                                        |
| xml_etree_generate       | 94.2 ms                                                | 86.9 ms: 1.08x faster                                         |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.08x faster                                          |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 5.06 ms: 1.08x faster                                         |
| sqlite_synth             | 2.93 us                                                | 2.73 us: 1.08x faster                                         |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.07x faster                                          |
| regex_v8                 | 25.0 ms                                                | 23.4 ms: 1.07x faster                                         |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                          |
| deepcopy_memo            | 52.3 us                                                | 49.5 us: 1.06x faster                                         |
| pathlib                  | 20.0 ms                                                | 19.0 ms: 1.06x faster                                         |
| regex_dna                | 222 ms                                                 | 212 ms: 1.05x faster                                          |
| bench_mp_pool            | 24.0 ms                                                | 24.0 ms: 1.00x slower                                         |
| unpickle_list            | 4.82 us                                                | 4.87 us: 1.01x slower                                         |
| pidigits                 | 190 ms                                                 | 198 ms: 1.04x slower                                          |
| unpickle                 | 14.1 us                                                | 14.8 us: 1.05x slower                                         |
| telco                    | 6.54 ms                                                | 6.87 ms: 1.05x slower                                         |
| async_generators         | 425 ms                                                 | 459 ms: 1.08x slower                                          |
| regex_effbot             | 3.23 ms                                                | 3.69 ms: 1.14x slower                                         |
| python_startup_no_site   | 5.82 ms                                                | 6.83 ms: 1.17x slower                                         |
| pickle_dict              | 27.3 us                                                | 32.5 us: 1.19x slower                                         |
| dask                     | 423 ms                                                 | 529 ms: 1.25x slower                                          |
| coverage                 | 72.8 ms                                                | 94.2 ms: 1.29x slower                                         |
| Geometric mean           | (ref)                                                  | 1.26x faster                                                  |

Benchmark hidden because not significant (3): gc_traversal, pickle_list, pickle
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

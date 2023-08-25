
# Results vs. 3.10.4

- fork: gvanrossum
- ref: jump_uops
- machine: linux-x86_64
- commit hash: 8681e0c
- commit date: 2023-07-03
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230703-linux-x86_64-gvanrossum-jump_uops-3.13.0a0-8681e0c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.66 sec: 1.19x faster                                         |
| tornado_http   | 127 ms                                                 | 96.1 ms: 1.33x faster                                          |
| Geometric mean | (ref)                                                  | 1.26x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230703-linux-x86_64-gvanrossum-jump_uops-3.13.0a0-8681e0c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.8 ms: 1.58x faster                                          |
| float          | 111 ms                                                 | 78.9 ms: 1.40x faster                                          |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                  | 1.29x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230703-linux-x86_64-gvanrossum-jump_uops-3.13.0a0-8681e0c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                           |
| regex_v8       | 25.0 ms                                                | 23.0 ms: 1.09x faster                                          |
| regex_dna      | 222 ms                                                 | 217 ms: 1.02x faster                                           |
| regex_effbot   | 3.23 ms                                                | 3.68 ms: 1.14x slower                                          |
| Geometric mean | (ref)                                                  | 1.06x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230703-linux-x86_64-gvanrossum-jump_uops-3.13.0a0-8681e0c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 301 us: 1.51x faster                                           |
| unpickle_pure_python | 300 us                                                 | 212 us: 1.42x faster                                           |
| json_dumps           | 13.5 ms                                                | 9.71 ms: 1.39x faster                                          |
| tomli_loads          | 2.92 sec                                               | 2.17 sec: 1.34x faster                                         |
| xml_etree_process    | 74.9 ms                                                | 57.6 ms: 1.30x faster                                          |
| xml_etree_generate   | 94.2 ms                                                | 83.6 ms: 1.13x faster                                          |
| json_loads           | 28.8 us                                                | 26.0 us: 1.11x faster                                          |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                           |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                           |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                          |
| unpickle_list        | 4.82 us                                                | 4.99 us: 1.04x slower                                          |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                          |
| pickle_dict          | 27.3 us                                                | 31.2 us: 1.14x slower                                          |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                   |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230703-linux-x86_64-gvanrossum-jump_uops-3.13.0a0-8681e0c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.18 ms: 1.54x faster                                          |
| python_startup_no_site | 5.82 ms                                                | 6.67 ms: 1.15x slower                                          |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230703-linux-x86_64-gvanrossum-jump_uops-3.13.0a0-8681e0c |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.37x faster                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230703-linux-x86_64-gvanrossum-jump_uops-3.13.0a0-8681e0c |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 148 us: 3.45x faster                                           |
| generators               | 76.8 ms                                                | 28.7 ms: 2.68x faster                                          |
| deltablue                | 7.42 ms                                                | 3.21 ms: 2.31x faster                                          |
| asyncio_tcp              | 925 ms                                                 | 514 ms: 1.80x faster                                           |
| chaos                    | 106 ms                                                 | 59.2 ms: 1.79x faster                                          |
| richards_super           | 90.7 ms                                                | 50.9 ms: 1.78x faster                                          |
| raytrace                 | 464 ms                                                 | 266 ms: 1.74x faster                                           |
| go                       | 229 ms                                                 | 135 ms: 1.70x faster                                           |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.78 sec: 1.69x faster                                         |
| richards                 | 74.9 ms                                                | 44.8 ms: 1.67x faster                                          |
| logging_silent           | 175 ns                                                 | 105 ns: 1.67x faster                                           |
| scimark_sor              | 197 ms                                                 | 118 ms: 1.66x faster                                           |
| hexiom                   | 9.53 ms                                                | 5.97 ms: 1.60x faster                                          |
| nbody                    | 142 ms                                                 | 89.8 ms: 1.58x faster                                          |
| sqlglot_parse            | 2.06 ms                                                | 1.31 ms: 1.57x faster                                          |
| python_startup           | 14.2 ms                                                | 9.18 ms: 1.54x faster                                          |
| crypto_pyaes             | 118 ms                                                 | 77.7 ms: 1.52x faster                                          |
| pyflate                  | 673 ms                                                 | 442 ms: 1.52x faster                                           |
| pickle_pure_python       | 455 us                                                 | 301 us: 1.51x faster                                           |
| sqlglot_transpile        | 2.45 ms                                                | 1.63 ms: 1.51x faster                                          |
| scimark_monte_carlo      | 108 ms                                                 | 72.4 ms: 1.50x faster                                          |
| async_tree_none          | 717 ms                                                 | 481 ms: 1.49x faster                                           |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.49x faster                                         |
| scimark_lu               | 163 ms                                                 | 111 ms: 1.47x faster                                           |
| async_tree_memoization   | 854 ms                                                 | 587 ms: 1.46x faster                                           |
| unpickle_pure_python     | 300 us                                                 | 212 us: 1.42x faster                                           |
| deepcopy_memo            | 52.3 us                                                | 37.1 us: 1.41x faster                                          |
| spectral_norm            | 150 ms                                                 | 107 ms: 1.41x faster                                           |
| float                    | 111 ms                                                 | 78.9 ms: 1.40x faster                                          |
| json_dumps               | 13.5 ms                                                | 9.71 ms: 1.39x faster                                          |
| logging_format           | 8.91 us                                                | 6.40 us: 1.39x faster                                          |
| logging_simple           | 8.07 us                                                | 5.82 us: 1.39x faster                                          |
| coroutines               | 31.8 ms                                                | 23.2 ms: 1.37x faster                                          |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.37x faster                                          |
| pprint_pformat           | 1.99 sec                                               | 1.47 sec: 1.35x faster                                         |
| tomli_loads              | 2.92 sec                                               | 2.17 sec: 1.34x faster                                         |
| pprint_safe_repr         | 955 ms                                                 | 716 ms: 1.33x faster                                           |
| comprehensions           | 26.8 us                                                | 20.2 us: 1.33x faster                                          |
| tornado_http             | 127 ms                                                 | 96.1 ms: 1.33x faster                                          |
| pycparser                | 1.50 sec                                               | 1.14 sec: 1.32x faster                                         |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 722 ms: 1.32x faster                                           |
| regex_compile            | 177 ms                                                 | 135 ms: 1.31x faster                                           |
| xml_etree_process        | 74.9 ms                                                | 57.6 ms: 1.30x faster                                          |
| unpack_sequence          | 64.7 ns                                                | 50.2 ns: 1.29x faster                                          |
| sqlglot_normalize        | 135 ms                                                 | 105 ms: 1.29x faster                                           |
| mypy2                    | 428 ms                                                 | 334 ms: 1.28x faster                                           |
| deepcopy                 | 442 us                                                 | 346 us: 1.28x faster                                           |
| sqlglot_optimize         | 65.3 ms                                                | 52.5 ms: 1.24x faster                                          |
| deepcopy_reduce          | 3.82 us                                                | 3.10 us: 1.24x faster                                          |
| nqueens                  | 100 ms                                                 | 81.0 ms: 1.23x faster                                          |
| fannkuch                 | 486 ms                                                 | 396 ms: 1.23x faster                                           |
| scimark_fft              | 424 ms                                                 | 351 ms: 1.21x faster                                           |
| docutils                 | 3.17 sec                                               | 2.66 sec: 1.19x faster                                         |
| bench_thread_pool        | 947 us                                                 | 817 us: 1.16x faster                                           |
| dulwich_log              | 75.9 ms                                                | 65.6 ms: 1.16x faster                                          |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.74 ms: 1.15x faster                                          |
| create_gc_cycles         | 1.67 ms                                                | 1.48 ms: 1.13x faster                                          |
| xml_etree_generate       | 94.2 ms                                                | 83.6 ms: 1.13x faster                                          |
| mdp                      | 2.82 sec                                               | 2.53 sec: 1.11x faster                                         |
| json_loads               | 28.8 us                                                | 26.0 us: 1.11x faster                                          |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.10x faster                                           |
| json                     | 5.42 ms                                                | 4.95 ms: 1.09x faster                                          |
| regex_v8                 | 25.0 ms                                                | 23.0 ms: 1.09x faster                                          |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                           |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                           |
| pathlib                  | 20.0 ms                                                | 18.9 ms: 1.06x faster                                          |
| sqlite_synth             | 2.93 us                                                | 2.79 us: 1.05x faster                                          |
| gc_traversal             | 3.84 ms                                                | 3.66 ms: 1.05x faster                                          |
| regex_dna                | 222 ms                                                 | 217 ms: 1.02x faster                                           |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                          |
| unpickle_list            | 4.82 us                                                | 4.99 us: 1.04x slower                                          |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                           |
| async_generators         | 425 ms                                                 | 450 ms: 1.06x slower                                           |
| unpickle                 | 14.1 us                                                | 15.0 us: 1.06x slower                                          |
| telco                    | 6.54 ms                                                | 7.21 ms: 1.10x slower                                          |
| regex_effbot             | 3.23 ms                                                | 3.68 ms: 1.14x slower                                          |
| pickle_dict              | 27.3 us                                                | 31.2 us: 1.14x slower                                          |
| python_startup_no_site   | 5.82 ms                                                | 6.67 ms: 1.15x slower                                          |
| dask                     | 423 ms                                                 | 515 ms: 1.22x slower                                           |
| coverage                 | 72.8 ms                                                | 91.9 ms: 1.26x slower                                          |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                   |

Benchmark hidden because not significant (2): pickle_list, bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.23x

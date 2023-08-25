
# Results vs. 3.10.4

- fork: gvanrossum
- ref: call_uops
- machine: linux-x86_64
- commit hash: 05af848
- commit date: 2023-08-16
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230816-linux-x86_64-gvanrossum-call_uops-3.13.0a0-05af848 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.63 sec: 1.21x faster                                         |
| tornado_http   | 127 ms                                                 | 95.1 ms: 1.34x faster                                          |
| Geometric mean | (ref)                                                  | 1.27x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230816-linux-x86_64-gvanrossum-call_uops-3.13.0a0-05af848 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.3 ms: 1.60x faster                                          |
| float          | 111 ms                                                 | 79.8 ms: 1.38x faster                                          |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                  | 1.31x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230816-linux-x86_64-gvanrossum-call_uops-3.13.0a0-05af848 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                           |
| regex_v8       | 25.0 ms                                                | 23.5 ms: 1.06x faster                                          |
| regex_dna      | 222 ms                                                 | 217 ms: 1.02x faster                                           |
| regex_effbot   | 3.23 ms                                                | 3.74 ms: 1.16x slower                                          |
| Geometric mean | (ref)                                                  | 1.05x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230816-linux-x86_64-gvanrossum-call_uops-3.13.0a0-05af848 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 295 us: 1.54x faster                                           |
| unpickle_pure_python | 300 us                                                 | 211 us: 1.42x faster                                           |
| tomli_loads          | 2.92 sec                                               | 2.10 sec: 1.39x faster                                         |
| json_dumps           | 13.5 ms                                                | 9.78 ms: 1.38x faster                                          |
| xml_etree_process    | 74.9 ms                                                | 57.6 ms: 1.30x faster                                          |
| json_loads           | 28.8 us                                                | 25.2 us: 1.14x faster                                          |
| xml_etree_generate   | 94.2 ms                                                | 82.9 ms: 1.14x faster                                          |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                           |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.08x faster                                           |
| unpickle             | 14.1 us                                                | 14.3 us: 1.01x slower                                          |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                          |
| pickle_list          | 4.56 us                                                | 4.72 us: 1.04x slower                                          |
| unpickle_list        | 4.82 us                                                | 5.12 us: 1.06x slower                                          |
| pickle_dict          | 27.3 us                                                | 32.0 us: 1.17x slower                                          |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230816-linux-x86_64-gvanrossum-call_uops-3.13.0a0-05af848 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.36 ms: 1.51x faster                                          |
| python_startup_no_site | 5.82 ms                                                | 6.86 ms: 1.18x slower                                          |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230816-linux-x86_64-gvanrossum-call_uops-3.13.0a0-05af848 |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.9 ms: 1.35x faster                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230816-linux-x86_64-gvanrossum-call_uops-3.13.0a0-05af848 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 142 us: 3.59x faster                                           |
| generators               | 76.8 ms                                                | 28.3 ms: 2.71x faster                                          |
| deltablue                | 7.42 ms                                                | 3.29 ms: 2.25x faster                                          |
| asyncio_tcp              | 925 ms                                                 | 488 ms: 1.89x faster                                           |
| chaos                    | 106 ms                                                 | 60.2 ms: 1.77x faster                                          |
| crypto_pyaes             | 118 ms                                                 | 69.6 ms: 1.70x faster                                          |
| logging_silent           | 175 ns                                                 | 104 ns: 1.69x faster                                           |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                         |
| raytrace                 | 464 ms                                                 | 276 ms: 1.68x faster                                           |
| richards_super           | 90.7 ms                                                | 54.4 ms: 1.67x faster                                          |
| go                       | 229 ms                                                 | 140 ms: 1.64x faster                                           |
| scimark_monte_carlo      | 108 ms                                                 | 66.0 ms: 1.64x faster                                          |
| async_tree_none          | 717 ms                                                 | 437 ms: 1.64x faster                                           |
| scimark_sor              | 197 ms                                                 | 122 ms: 1.61x faster                                           |
| sqlglot_parse            | 2.06 ms                                                | 1.28 ms: 1.61x faster                                          |
| nbody                    | 142 ms                                                 | 88.3 ms: 1.60x faster                                          |
| hexiom                   | 9.53 ms                                                | 6.03 ms: 1.58x faster                                          |
| richards                 | 74.9 ms                                                | 48.0 ms: 1.56x faster                                          |
| pickle_pure_python       | 455 us                                                 | 295 us: 1.54x faster                                           |
| sqlglot_transpile        | 2.45 ms                                                | 1.61 ms: 1.52x faster                                          |
| async_tree_memoization   | 854 ms                                                 | 563 ms: 1.52x faster                                           |
| unpack_sequence          | 64.7 ns                                                | 42.7 ns: 1.51x faster                                          |
| python_startup           | 14.2 ms                                                | 9.36 ms: 1.51x faster                                          |
| pyflate                  | 673 ms                                                 | 446 ms: 1.51x faster                                           |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.49x faster                                         |
| scimark_lu               | 163 ms                                                 | 112 ms: 1.46x faster                                           |
| coroutines               | 31.8 ms                                                | 22.2 ms: 1.43x faster                                          |
| unpickle_pure_python     | 300 us                                                 | 211 us: 1.42x faster                                           |
| deepcopy_memo            | 52.3 us                                                | 37.0 us: 1.41x faster                                          |
| spectral_norm            | 150 ms                                                 | 107 ms: 1.40x faster                                           |
| logging_format           | 8.91 us                                                | 6.41 us: 1.39x faster                                          |
| tomli_loads              | 2.92 sec                                               | 2.10 sec: 1.39x faster                                         |
| logging_simple           | 8.07 us                                                | 5.81 us: 1.39x faster                                          |
| float                    | 111 ms                                                 | 79.8 ms: 1.38x faster                                          |
| json_dumps               | 13.5 ms                                                | 9.78 ms: 1.38x faster                                          |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 702 ms: 1.35x faster                                           |
| mako                     | 14.8 ms                                                | 10.9 ms: 1.35x faster                                          |
| tornado_http             | 127 ms                                                 | 95.1 ms: 1.34x faster                                          |
| pprint_pformat           | 1.99 sec                                               | 1.48 sec: 1.34x faster                                         |
| pprint_safe_repr         | 955 ms                                                 | 721 ms: 1.32x faster                                           |
| comprehensions           | 26.8 us                                                | 20.4 us: 1.32x faster                                          |
| xml_etree_process        | 74.9 ms                                                | 57.6 ms: 1.30x faster                                          |
| regex_compile            | 177 ms                                                 | 136 ms: 1.30x faster                                           |
| sqlglot_normalize        | 135 ms                                                 | 105 ms: 1.29x faster                                           |
| nqueens                  | 100 ms                                                 | 78.9 ms: 1.27x faster                                          |
| deepcopy                 | 442 us                                                 | 349 us: 1.27x faster                                           |
| fannkuch                 | 486 ms                                                 | 390 ms: 1.25x faster                                           |
| pycparser                | 1.50 sec                                               | 1.21 sec: 1.24x faster                                         |
| sqlglot_optimize         | 65.3 ms                                                | 52.6 ms: 1.24x faster                                          |
| deepcopy_reduce          | 3.82 us                                                | 3.14 us: 1.22x faster                                          |
| docutils                 | 3.17 sec                                               | 2.63 sec: 1.21x faster                                         |
| scimark_fft              | 424 ms                                                 | 355 ms: 1.19x faster                                           |
| bench_thread_pool        | 947 us                                                 | 815 us: 1.16x faster                                           |
| dulwich_log              | 75.9 ms                                                | 65.8 ms: 1.15x faster                                          |
| json_loads               | 28.8 us                                                | 25.2 us: 1.14x faster                                          |
| xml_etree_generate       | 94.2 ms                                                | 82.9 ms: 1.14x faster                                          |
| create_gc_cycles         | 1.67 ms                                                | 1.48 ms: 1.13x faster                                          |
| mdp                      | 2.82 sec                                               | 2.54 sec: 1.11x faster                                         |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.94 ms: 1.10x faster                                          |
| json                     | 5.42 ms                                                | 4.92 ms: 1.10x faster                                          |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.09x faster                                           |
| xml_etree_iterparse      | 111 ms                                                 | 102 ms: 1.09x faster                                           |
| sqlite_synth             | 2.93 us                                                | 2.72 us: 1.08x faster                                          |
| pathlib                  | 20.0 ms                                                | 18.6 ms: 1.08x faster                                          |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.08x faster                                           |
| regex_v8                 | 25.0 ms                                                | 23.5 ms: 1.06x faster                                          |
| regex_dna                | 222 ms                                                 | 217 ms: 1.02x faster                                           |
| pidigits                 | 190 ms                                                 | 189 ms: 1.01x faster                                           |
| bench_mp_pool            | 24.0 ms                                                | 24.0 ms: 1.00x slower                                          |
| unpickle                 | 14.1 us                                                | 14.3 us: 1.01x slower                                          |
| pickle                   | 10.3 us                                                | 10.6 us: 1.03x slower                                          |
| pickle_list              | 4.56 us                                                | 4.72 us: 1.04x slower                                          |
| gc_traversal             | 3.84 ms                                                | 4.06 ms: 1.06x slower                                          |
| unpickle_list            | 4.82 us                                                | 5.12 us: 1.06x slower                                          |
| async_generators         | 425 ms                                                 | 452 ms: 1.06x slower                                           |
| regex_effbot             | 3.23 ms                                                | 3.74 ms: 1.16x slower                                          |
| coverage                 | 72.8 ms                                                | 84.6 ms: 1.16x slower                                          |
| pickle_dict              | 27.3 us                                                | 32.0 us: 1.17x slower                                          |
| python_startup_no_site   | 5.82 ms                                                | 6.86 ms: 1.18x slower                                          |
| dask                     | 423 ms                                                 | 519 ms: 1.23x slower                                           |
| telco                    | 6.54 ms                                                | 8.08 ms: 1.23x slower                                          |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                   |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

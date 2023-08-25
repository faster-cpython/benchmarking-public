
# Results vs. 3.10.4

- fork: gvanrossum
- ref: optim_exec
- machine: linux-x86_64
- commit hash: 121fbad
- commit date: 2023-06-21
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.66 sec: 1.19x faster                                          |
| tornado_http   | 127 ms                                                 | 96.2 ms: 1.32x faster                                           |
| Geometric mean | (ref)                                                  | 1.26x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 90.5 ms: 1.56x faster                                           |
| float          | 111 ms                                                 | 80.7 ms: 1.37x faster                                           |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                  | 1.27x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 138 ms: 1.29x faster                                            |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                           |
| regex_dna      | 222 ms                                                 | 201 ms: 1.10x faster                                            |
| regex_effbot   | 3.23 ms                                                | 3.39 ms: 1.05x slower                                           |
| Geometric mean | (ref)                                                  | 1.12x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 304 us: 1.50x faster                                            |
| json_dumps           | 13.5 ms                                                | 9.81 ms: 1.38x faster                                           |
| unpickle_pure_python | 300 us                                                 | 218 us: 1.38x faster                                            |
| xml_etree_process    | 74.9 ms                                                | 57.4 ms: 1.31x faster                                           |
| tomli_loads          | 2.92 sec                                               | 2.34 sec: 1.25x faster                                          |
| json_loads           | 28.8 us                                                | 25.2 us: 1.14x faster                                           |
| xml_etree_generate   | 94.2 ms                                                | 84.6 ms: 1.11x faster                                           |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                            |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.06x faster                                            |
| pickle_list          | 4.56 us                                                | 4.63 us: 1.02x slower                                           |
| unpickle_list        | 4.82 us                                                | 4.91 us: 1.02x slower                                           |
| unpickle             | 14.1 us                                                | 14.9 us: 1.05x slower                                           |
| pickle               | 10.3 us                                                | 10.9 us: 1.06x slower                                           |
| pickle_dict          | 27.3 us                                                | 31.3 us: 1.15x slower                                           |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.18 ms: 1.54x faster                                           |
| python_startup_no_site | 5.82 ms                                                | 6.66 ms: 1.15x slower                                           |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.9 ms: 1.35x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 149 us: 3.43x faster                                            |
| generators               | 76.8 ms                                                | 29.3 ms: 2.62x faster                                           |
| deltablue                | 7.42 ms                                                | 3.31 ms: 2.24x faster                                           |
| asyncio_tcp              | 925 ms                                                 | 505 ms: 1.83x faster                                            |
| logging_silent           | 175 ns                                                 | 96.7 ns: 1.81x faster                                           |
| richards_super           | 90.7 ms                                                | 50.4 ms: 1.80x faster                                           |
| richards                 | 74.9 ms                                                | 44.1 ms: 1.70x faster                                           |
| chaos                    | 106 ms                                                 | 62.7 ms: 1.69x faster                                           |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                          |
| go                       | 229 ms                                                 | 137 ms: 1.68x faster                                            |
| scimark_sor              | 197 ms                                                 | 119 ms: 1.65x faster                                            |
| raytrace                 | 464 ms                                                 | 291 ms: 1.60x faster                                            |
| sqlglot_parse            | 2.06 ms                                                | 1.31 ms: 1.57x faster                                           |
| nbody                    | 142 ms                                                 | 90.5 ms: 1.56x faster                                           |
| python_startup           | 14.2 ms                                                | 9.18 ms: 1.54x faster                                           |
| hexiom                   | 9.53 ms                                                | 6.23 ms: 1.53x faster                                           |
| scimark_monte_carlo      | 108 ms                                                 | 71.2 ms: 1.52x faster                                           |
| crypto_pyaes             | 118 ms                                                 | 78.4 ms: 1.51x faster                                           |
| sqlglot_transpile        | 2.45 ms                                                | 1.63 ms: 1.50x faster                                           |
| pyflate                  | 673 ms                                                 | 449 ms: 1.50x faster                                            |
| pickle_pure_python       | 455 us                                                 | 304 us: 1.50x faster                                            |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.49x faster                                          |
| async_tree_none          | 717 ms                                                 | 480 ms: 1.49x faster                                            |
| unpack_sequence          | 64.7 ns                                                | 43.8 ns: 1.48x faster                                           |
| scimark_lu               | 163 ms                                                 | 111 ms: 1.48x faster                                            |
| async_tree_memoization   | 854 ms                                                 | 583 ms: 1.46x faster                                            |
| coroutines               | 31.8 ms                                                | 22.1 ms: 1.44x faster                                           |
| logging_format           | 8.91 us                                                | 6.44 us: 1.38x faster                                           |
| json_dumps               | 13.5 ms                                                | 9.81 ms: 1.38x faster                                           |
| unpickle_pure_python     | 300 us                                                 | 218 us: 1.38x faster                                            |
| float                    | 111 ms                                                 | 80.7 ms: 1.37x faster                                           |
| deepcopy_memo            | 52.3 us                                                | 38.3 us: 1.37x faster                                           |
| logging_simple           | 8.07 us                                                | 5.91 us: 1.37x faster                                           |
| pprint_pformat           | 1.99 sec                                               | 1.47 sec: 1.35x faster                                          |
| spectral_norm            | 150 ms                                                 | 111 ms: 1.35x faster                                            |
| mako                     | 14.8 ms                                                | 10.9 ms: 1.35x faster                                           |
| pprint_safe_repr         | 955 ms                                                 | 719 ms: 1.33x faster                                            |
| tornado_http             | 127 ms                                                 | 96.2 ms: 1.32x faster                                           |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 722 ms: 1.32x faster                                            |
| xml_etree_process        | 74.9 ms                                                | 57.4 ms: 1.31x faster                                           |
| pycparser                | 1.50 sec                                               | 1.15 sec: 1.30x faster                                          |
| regex_compile            | 177 ms                                                 | 138 ms: 1.29x faster                                            |
| mypy2                    | 428 ms                                                 | 335 ms: 1.28x faster                                            |
| sqlglot_normalize        | 135 ms                                                 | 107 ms: 1.27x faster                                            |
| deepcopy                 | 442 us                                                 | 349 us: 1.27x faster                                            |
| tomli_loads              | 2.92 sec                                               | 2.34 sec: 1.25x faster                                          |
| sqlglot_optimize         | 65.3 ms                                                | 52.8 ms: 1.24x faster                                           |
| comprehensions           | 26.8 us                                                | 21.7 us: 1.23x faster                                           |
| deepcopy_reduce          | 3.82 us                                                | 3.10 us: 1.23x faster                                           |
| docutils                 | 3.17 sec                                               | 2.66 sec: 1.19x faster                                          |
| nqueens                  | 100 ms                                                 | 84.1 ms: 1.19x faster                                           |
| scimark_fft              | 424 ms                                                 | 363 ms: 1.17x faster                                            |
| dulwich_log              | 75.9 ms                                                | 65.1 ms: 1.17x faster                                           |
| regex_v8                 | 25.0 ms                                                | 21.7 ms: 1.15x faster                                           |
| json_loads               | 28.8 us                                                | 25.2 us: 1.14x faster                                           |
| bench_thread_pool        | 947 us                                                 | 831 us: 1.14x faster                                            |
| fannkuch                 | 486 ms                                                 | 427 ms: 1.14x faster                                            |
| json                     | 5.42 ms                                                | 4.78 ms: 1.13x faster                                           |
| xml_etree_generate       | 94.2 ms                                                | 84.6 ms: 1.11x faster                                           |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.11x faster                                           |
| regex_dna                | 222 ms                                                 | 201 ms: 1.10x faster                                            |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 5.06 ms: 1.08x faster                                           |
| gc_traversal             | 3.84 ms                                                | 3.58 ms: 1.07x faster                                           |
| pathlib                  | 20.0 ms                                                | 18.8 ms: 1.07x faster                                           |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                            |
| xml_etree_iterparse      | 111 ms                                                 | 105 ms: 1.06x faster                                            |
| meteor_contest           | 115 ms                                                 | 109 ms: 1.06x faster                                            |
| sqlite_synth             | 2.93 us                                                | 2.78 us: 1.06x faster                                           |
| mdp                      | 2.82 sec                                               | 2.72 sec: 1.04x faster                                          |
| pickle_list              | 4.56 us                                                | 4.63 us: 1.02x slower                                           |
| unpickle_list            | 4.82 us                                                | 4.91 us: 1.02x slower                                           |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                            |
| telco                    | 6.54 ms                                                | 6.81 ms: 1.04x slower                                           |
| regex_effbot             | 3.23 ms                                                | 3.39 ms: 1.05x slower                                           |
| unpickle                 | 14.1 us                                                | 14.9 us: 1.05x slower                                           |
| pickle                   | 10.3 us                                                | 10.9 us: 1.06x slower                                           |
| async_generators         | 425 ms                                                 | 463 ms: 1.09x slower                                            |
| python_startup_no_site   | 5.82 ms                                                | 6.66 ms: 1.15x slower                                           |
| pickle_dict              | 27.3 us                                                | 31.3 us: 1.15x slower                                           |
| dask                     | 423 ms                                                 | 515 ms: 1.22x slower                                            |
| coverage                 | 72.8 ms                                                | 93.2 ms: 1.28x slower                                           |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                    |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.20x


# Results vs. 3.10.4

- fork: brandtbucher
- ref: to_bool
- machine: linux-x86_64
- commit hash: 757b1cc
- commit date: 2023-06-20
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.67 sec: 1.19x faster                                         |
| tornado_http   | 127 ms                                                 | 97.0 ms: 1.31x faster                                          |
| Geometric mean | (ref)                                                  | 1.25x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 92.2 ms: 1.54x faster                                          |
| float          | 111 ms                                                 | 80.0 ms: 1.38x faster                                          |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                  | 1.28x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                           |
| regex_v8       | 25.0 ms                                                | 22.6 ms: 1.11x faster                                          |
| regex_dna      | 222 ms                                                 | 217 ms: 1.02x faster                                           |
| regex_effbot   | 3.23 ms                                                | 3.56 ms: 1.10x slower                                          |
| Geometric mean | (ref)                                                  | 1.07x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 308 us: 1.48x faster                                           |
| unpickle_pure_python | 300 us                                                 | 215 us: 1.40x faster                                           |
| json_dumps           | 13.5 ms                                                | 9.95 ms: 1.36x faster                                          |
| tomli_loads          | 2.92 sec                                               | 2.27 sec: 1.29x faster                                         |
| xml_etree_process    | 74.9 ms                                                | 58.4 ms: 1.28x faster                                          |
| json_loads           | 28.8 us                                                | 25.1 us: 1.15x faster                                          |
| xml_etree_generate   | 94.2 ms                                                | 84.3 ms: 1.12x faster                                          |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                           |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                           |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                          |
| pickle_list          | 4.56 us                                                | 4.62 us: 1.01x slower                                          |
| unpickle_list        | 4.82 us                                                | 4.96 us: 1.03x slower                                          |
| unpickle             | 14.1 us                                                | 14.8 us: 1.04x slower                                          |
| pickle_dict          | 27.3 us                                                | 32.1 us: 1.18x slower                                          |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.17 ms: 1.54x faster                                          |
| python_startup_no_site | 5.82 ms                                                | 6.68 ms: 1.15x slower                                          |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.38x faster                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 147 us: 3.48x faster                                           |
| generators               | 76.8 ms                                                | 29.4 ms: 2.61x faster                                          |
| deltablue                | 7.42 ms                                                | 3.32 ms: 2.23x faster                                          |
| asyncio_tcp              | 925 ms                                                 | 506 ms: 1.83x faster                                           |
| chaos                    | 106 ms                                                 | 62.1 ms: 1.71x faster                                          |
| richards_super           | 90.7 ms                                                | 53.4 ms: 1.70x faster                                          |
| logging_silent           | 175 ns                                                 | 104 ns: 1.68x faster                                           |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                         |
| scimark_sor              | 197 ms                                                 | 119 ms: 1.65x faster                                           |
| go                       | 229 ms                                                 | 141 ms: 1.63x faster                                           |
| richards                 | 74.9 ms                                                | 47.5 ms: 1.58x faster                                          |
| raytrace                 | 464 ms                                                 | 295 ms: 1.57x faster                                           |
| hexiom                   | 9.53 ms                                                | 6.07 ms: 1.57x faster                                          |
| python_startup           | 14.2 ms                                                | 9.17 ms: 1.54x faster                                          |
| nbody                    | 142 ms                                                 | 92.2 ms: 1.54x faster                                          |
| crypto_pyaes             | 118 ms                                                 | 77.3 ms: 1.53x faster                                          |
| sqlglot_parse            | 2.06 ms                                                | 1.35 ms: 1.53x faster                                          |
| scimark_monte_carlo      | 108 ms                                                 | 72.0 ms: 1.50x faster                                          |
| pickle_pure_python       | 455 us                                                 | 308 us: 1.48x faster                                           |
| pyflate                  | 673 ms                                                 | 456 ms: 1.48x faster                                           |
| async_tree_io            | 1.77 sec                                               | 1.20 sec: 1.47x faster                                         |
| async_tree_none          | 717 ms                                                 | 487 ms: 1.47x faster                                           |
| sqlglot_transpile        | 2.45 ms                                                | 1.67 ms: 1.47x faster                                          |
| scimark_lu               | 163 ms                                                 | 112 ms: 1.46x faster                                           |
| spectral_norm            | 150 ms                                                 | 104 ms: 1.45x faster                                           |
| async_tree_memoization   | 854 ms                                                 | 594 ms: 1.44x faster                                           |
| unpickle_pure_python     | 300 us                                                 | 215 us: 1.40x faster                                           |
| unpack_sequence          | 64.7 ns                                                | 46.3 ns: 1.40x faster                                          |
| deepcopy_memo            | 52.3 us                                                | 37.5 us: 1.40x faster                                          |
| float                    | 111 ms                                                 | 80.0 ms: 1.38x faster                                          |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.38x faster                                          |
| logging_format           | 8.91 us                                                | 6.53 us: 1.36x faster                                          |
| json_dumps               | 13.5 ms                                                | 9.95 ms: 1.36x faster                                          |
| coroutines               | 31.8 ms                                                | 23.6 ms: 1.35x faster                                          |
| logging_simple           | 8.07 us                                                | 6.03 us: 1.34x faster                                          |
| pprint_pformat           | 1.99 sec                                               | 1.50 sec: 1.33x faster                                         |
| tornado_http             | 127 ms                                                 | 97.0 ms: 1.31x faster                                          |
| comprehensions           | 26.8 us                                                | 20.4 us: 1.31x faster                                          |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 729 ms: 1.30x faster                                           |
| pprint_safe_repr         | 955 ms                                                 | 735 ms: 1.30x faster                                           |
| regex_compile            | 177 ms                                                 | 136 ms: 1.30x faster                                           |
| nqueens                  | 100 ms                                                 | 77.7 ms: 1.29x faster                                          |
| tomli_loads              | 2.92 sec                                               | 2.27 sec: 1.29x faster                                         |
| xml_etree_process        | 74.9 ms                                                | 58.4 ms: 1.28x faster                                          |
| mypy2                    | 428 ms                                                 | 337 ms: 1.27x faster                                           |
| sqlglot_normalize        | 135 ms                                                 | 107 ms: 1.27x faster                                           |
| deepcopy                 | 442 us                                                 | 351 us: 1.26x faster                                           |
| pycparser                | 1.50 sec                                               | 1.19 sec: 1.26x faster                                         |
| fannkuch                 | 486 ms                                                 | 395 ms: 1.23x faster                                           |
| sqlglot_optimize         | 65.3 ms                                                | 53.5 ms: 1.22x faster                                          |
| scimark_fft              | 424 ms                                                 | 349 ms: 1.21x faster                                           |
| deepcopy_reduce          | 3.82 us                                                | 3.20 us: 1.20x faster                                          |
| docutils                 | 3.17 sec                                               | 2.67 sec: 1.19x faster                                         |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.66 ms: 1.17x faster                                          |
| dulwich_log              | 75.9 ms                                                | 65.5 ms: 1.16x faster                                          |
| bench_thread_pool        | 947 us                                                 | 819 us: 1.16x faster                                           |
| json_loads               | 28.8 us                                                | 25.1 us: 1.15x faster                                          |
| json                     | 5.42 ms                                                | 4.78 ms: 1.13x faster                                          |
| xml_etree_generate       | 94.2 ms                                                | 84.3 ms: 1.12x faster                                          |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.11x faster                                          |
| regex_v8                 | 25.0 ms                                                | 22.6 ms: 1.11x faster                                          |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.10x faster                                           |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                           |
| pathlib                  | 20.0 ms                                                | 18.8 ms: 1.07x faster                                          |
| sqlite_synth             | 2.93 us                                                | 2.76 us: 1.06x faster                                          |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                           |
| mdp                      | 2.82 sec                                               | 2.69 sec: 1.05x faster                                         |
| gc_traversal             | 3.84 ms                                                | 3.68 ms: 1.04x faster                                          |
| regex_dna                | 222 ms                                                 | 217 ms: 1.02x faster                                           |
| pidigits                 | 190 ms                                                 | 192 ms: 1.01x slower                                           |
| pickle                   | 10.3 us                                                | 10.4 us: 1.01x slower                                          |
| pickle_list              | 4.56 us                                                | 4.62 us: 1.01x slower                                          |
| unpickle_list            | 4.82 us                                                | 4.96 us: 1.03x slower                                          |
| telco                    | 6.54 ms                                                | 6.75 ms: 1.03x slower                                          |
| unpickle                 | 14.1 us                                                | 14.8 us: 1.04x slower                                          |
| async_generators         | 425 ms                                                 | 448 ms: 1.05x slower                                           |
| regex_effbot             | 3.23 ms                                                | 3.56 ms: 1.10x slower                                          |
| python_startup_no_site   | 5.82 ms                                                | 6.68 ms: 1.15x slower                                          |
| pickle_dict              | 27.3 us                                                | 32.1 us: 1.18x slower                                          |
| dask                     | 423 ms                                                 | 526 ms: 1.25x slower                                           |
| coverage                 | 72.8 ms                                                | 92.9 ms: 1.28x slower                                          |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                   |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x


# Results vs. 3.10.4

- fork: brandtbucher
- ref: un_materialize_alt
- machine: linux-x86_64
- commit hash: 25202d9
- commit date: 2023-07-16
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.66 sec: 1.19x faster                                                    |
| tornado_http   | 127 ms                                                 | 96.5 ms: 1.32x faster                                                     |
| Geometric mean | (ref)                                                  | 1.25x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 93.8 ms: 1.51x faster                                                     |
| float          | 111 ms                                                 | 79.1 ms: 1.40x faster                                                     |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.27x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                                      |
| regex_v8       | 25.0 ms                                                | 22.1 ms: 1.13x faster                                                     |
| regex_dna      | 222 ms                                                 | 214 ms: 1.03x faster                                                      |
| regex_effbot   | 3.23 ms                                                | 3.52 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 296 us: 1.54x faster                                                      |
| unpickle_pure_python | 300 us                                                 | 211 us: 1.42x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.78 ms: 1.38x faster                                                     |
| xml_etree_process    | 74.9 ms                                                | 57.5 ms: 1.30x faster                                                     |
| tomli_loads          | 2.92 sec                                               | 2.32 sec: 1.26x faster                                                    |
| xml_etree_generate   | 94.2 ms                                                | 83.1 ms: 1.13x faster                                                     |
| json_loads           | 28.8 us                                                | 25.5 us: 1.13x faster                                                     |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                                      |
| pickle_list          | 4.56 us                                                | 4.59 us: 1.01x slower                                                     |
| unpickle_list        | 4.82 us                                                | 4.95 us: 1.03x slower                                                     |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                                     |
| unpickle             | 14.1 us                                                | 15.1 us: 1.07x slower                                                     |
| pickle_dict          | 27.3 us                                                | 32.5 us: 1.19x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.18 ms: 1.54x faster                                                     |
| python_startup_no_site | 5.82 ms                                                | 6.67 ms: 1.15x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 141 us: 3.62x faster                                                      |
| generators               | 76.8 ms                                                | 28.5 ms: 2.69x faster                                                     |
| deltablue                | 7.42 ms                                                | 3.25 ms: 2.29x faster                                                     |
| asyncio_tcp              | 925 ms                                                 | 508 ms: 1.82x faster                                                      |
| chaos                    | 106 ms                                                 | 59.5 ms: 1.79x faster                                                     |
| logging_silent           | 175 ns                                                 | 102 ns: 1.72x faster                                                      |
| raytrace                 | 464 ms                                                 | 270 ms: 1.72x faster                                                      |
| crypto_pyaes             | 118 ms                                                 | 69.3 ms: 1.71x faster                                                     |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.78 sec: 1.69x faster                                                    |
| richards_super           | 90.7 ms                                                | 54.0 ms: 1.68x faster                                                     |
| go                       | 229 ms                                                 | 139 ms: 1.65x faster                                                      |
| scimark_sor              | 197 ms                                                 | 120 ms: 1.63x faster                                                      |
| scimark_monte_carlo      | 108 ms                                                 | 67.7 ms: 1.60x faster                                                     |
| sqlglot_parse            | 2.06 ms                                                | 1.29 ms: 1.60x faster                                                     |
| hexiom                   | 9.53 ms                                                | 6.00 ms: 1.59x faster                                                     |
| python_startup           | 14.2 ms                                                | 9.18 ms: 1.54x faster                                                     |
| pickle_pure_python       | 455 us                                                 | 296 us: 1.54x faster                                                      |
| richards                 | 74.9 ms                                                | 49.0 ms: 1.53x faster                                                     |
| sqlglot_transpile        | 2.45 ms                                                | 1.61 ms: 1.52x faster                                                     |
| nbody                    | 142 ms                                                 | 93.8 ms: 1.51x faster                                                     |
| pyflate                  | 673 ms                                                 | 447 ms: 1.50x faster                                                      |
| async_tree_none          | 717 ms                                                 | 480 ms: 1.49x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.49x faster                                                    |
| scimark_lu               | 163 ms                                                 | 111 ms: 1.48x faster                                                      |
| async_tree_memoization   | 854 ms                                                 | 582 ms: 1.47x faster                                                      |
| spectral_norm            | 150 ms                                                 | 103 ms: 1.45x faster                                                      |
| coroutines               | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                     |
| unpickle_pure_python     | 300 us                                                 | 211 us: 1.42x faster                                                      |
| deepcopy_memo            | 52.3 us                                                | 37.2 us: 1.41x faster                                                     |
| float                    | 111 ms                                                 | 79.1 ms: 1.40x faster                                                     |
| logging_simple           | 8.07 us                                                | 5.81 us: 1.39x faster                                                     |
| json_dumps               | 13.5 ms                                                | 9.78 ms: 1.38x faster                                                     |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                     |
| logging_format           | 8.91 us                                                | 6.45 us: 1.38x faster                                                     |
| unpack_sequence          | 64.7 ns                                                | 47.9 ns: 1.35x faster                                                     |
| pprint_pformat           | 1.99 sec                                               | 1.49 sec: 1.34x faster                                                    |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 716 ms: 1.33x faster                                                      |
| tornado_http             | 127 ms                                                 | 96.5 ms: 1.32x faster                                                     |
| comprehensions           | 26.8 us                                                | 20.5 us: 1.31x faster                                                     |
| xml_etree_process        | 74.9 ms                                                | 57.5 ms: 1.30x faster                                                     |
| pprint_safe_repr         | 955 ms                                                 | 734 ms: 1.30x faster                                                      |
| pycparser                | 1.50 sec                                               | 1.16 sec: 1.30x faster                                                    |
| sqlglot_normalize        | 135 ms                                                 | 105 ms: 1.29x faster                                                      |
| regex_compile            | 177 ms                                                 | 137 ms: 1.29x faster                                                      |
| tomli_loads              | 2.92 sec                                               | 2.32 sec: 1.26x faster                                                    |
| nqueens                  | 100 ms                                                 | 79.5 ms: 1.26x faster                                                     |
| deepcopy                 | 442 us                                                 | 353 us: 1.25x faster                                                      |
| fannkuch                 | 486 ms                                                 | 393 ms: 1.24x faster                                                      |
| sqlglot_optimize         | 65.3 ms                                                | 52.8 ms: 1.24x faster                                                     |
| deepcopy_reduce          | 3.82 us                                                | 3.16 us: 1.21x faster                                                     |
| docutils                 | 3.17 sec                                               | 2.66 sec: 1.19x faster                                                    |
| scimark_fft              | 424 ms                                                 | 358 ms: 1.18x faster                                                      |
| bench_thread_pool        | 947 us                                                 | 815 us: 1.16x faster                                                      |
| dulwich_log              | 75.9 ms                                                | 65.7 ms: 1.16x faster                                                     |
| regex_v8                 | 25.0 ms                                                | 22.1 ms: 1.13x faster                                                     |
| xml_etree_generate       | 94.2 ms                                                | 83.1 ms: 1.13x faster                                                     |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.82 ms: 1.13x faster                                                     |
| json_loads               | 28.8 us                                                | 25.5 us: 1.13x faster                                                     |
| create_gc_cycles         | 1.67 ms                                                | 1.49 ms: 1.12x faster                                                     |
| json                     | 5.42 ms                                                | 4.90 ms: 1.10x faster                                                     |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.10x faster                                                      |
| xml_etree_iterparse      | 111 ms                                                 | 102 ms: 1.09x faster                                                      |
| mdp                      | 2.82 sec                                               | 2.59 sec: 1.09x faster                                                    |
| pathlib                  | 20.0 ms                                                | 18.6 ms: 1.07x faster                                                     |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                                      |
| sqlite_synth             | 2.93 us                                                | 2.78 us: 1.06x faster                                                     |
| regex_dna                | 222 ms                                                 | 214 ms: 1.03x faster                                                      |
| pickle_list              | 4.56 us                                                | 4.59 us: 1.01x slower                                                     |
| unpickle_list            | 4.82 us                                                | 4.95 us: 1.03x slower                                                     |
| pickle                   | 10.3 us                                                | 10.6 us: 1.03x slower                                                     |
| pidigits                 | 190 ms                                                 | 198 ms: 1.04x slower                                                      |
| async_generators         | 425 ms                                                 | 445 ms: 1.05x slower                                                      |
| unpickle                 | 14.1 us                                                | 15.1 us: 1.07x slower                                                     |
| regex_effbot             | 3.23 ms                                                | 3.52 ms: 1.09x slower                                                     |
| telco                    | 6.54 ms                                                | 7.18 ms: 1.10x slower                                                     |
| gc_traversal             | 3.84 ms                                                | 4.30 ms: 1.12x slower                                                     |
| python_startup_no_site   | 5.82 ms                                                | 6.67 ms: 1.15x slower                                                     |
| pickle_dict              | 27.3 us                                                | 32.5 us: 1.19x slower                                                     |
| dask                     | 423 ms                                                 | 521 ms: 1.23x slower                                                      |
| coverage                 | 72.8 ms                                                | 93.1 ms: 1.28x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                              |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

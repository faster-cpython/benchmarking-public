
# Results vs. 3.10.4

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: fed9a7f
- commit date: 2023-08-11
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-fed9a7f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.57 sec: 1.23x faster                                                    |
| tornado_http   | 127 ms                                                 | 99.6 ms: 1.28x faster                                                     |
| Geometric mean | (ref)                                                  | 1.26x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-fed9a7f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.7 ms: 1.61x faster                                                     |
| float          | 111 ms                                                 | 87.7 ms: 1.26x faster                                                     |
| pidigits       | 190 ms                                                 | 201 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                  | 1.24x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-fed9a7f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                                      |
| regex_v8       | 25.0 ms                                                | 22.8 ms: 1.10x faster                                                     |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                                      |
| regex_effbot   | 3.23 ms                                                | 3.57 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-fed9a7f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 293 us: 1.55x faster                                                      |
| unpickle_pure_python | 300 us                                                 | 211 us: 1.42x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.68 ms: 1.40x faster                                                     |
| tomli_loads          | 2.92 sec                                               | 2.30 sec: 1.27x faster                                                    |
| xml_etree_process    | 74.9 ms                                                | 60.0 ms: 1.25x faster                                                     |
| json_loads           | 28.8 us                                                | 25.3 us: 1.14x faster                                                     |
| xml_etree_generate   | 94.2 ms                                                | 88.1 ms: 1.07x faster                                                     |
| pickle_list          | 4.56 us                                                | 4.63 us: 1.02x slower                                                     |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                                     |
| unpickle_list        | 4.82 us                                                | 4.99 us: 1.04x slower                                                     |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                                     |
| pickle_dict          | 27.3 us                                                | 31.6 us: 1.16x slower                                                     |
| xml_etree_parse      | 163 ms                                                 | 346 ms: 2.12x slower                                                      |
| xml_etree_iterparse  | 111 ms                                                 | 323 ms: 2.90x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-fed9a7f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.52 ms: 1.49x faster                                                     |
| python_startup_no_site | 5.82 ms                                                | 6.92 ms: 1.19x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.12x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-fed9a7f |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.37x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-fed9a7f |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 146 us: 3.50x faster                                                      |
| generators               | 76.8 ms                                                | 28.2 ms: 2.72x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 706 ms: 2.51x faster                                                      |
| deltablue                | 7.42 ms                                                | 3.21 ms: 2.31x faster                                                     |
| async_tree_none          | 717 ms                                                 | 327 ms: 2.19x faster                                                      |
| async_tree_memoization   | 854 ms                                                 | 446 ms: 1.91x faster                                                      |
| asyncio_tcp              | 925 ms                                                 | 484 ms: 1.91x faster                                                      |
| chaos                    | 106 ms                                                 | 59.4 ms: 1.79x faster                                                     |
| richards_super           | 90.7 ms                                                | 52.6 ms: 1.72x faster                                                     |
| raytrace                 | 464 ms                                                 | 269 ms: 1.72x faster                                                      |
| logging_silent           | 175 ns                                                 | 103 ns: 1.71x faster                                                      |
| crypto_pyaes             | 118 ms                                                 | 70.4 ms: 1.68x faster                                                     |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                    |
| go                       | 229 ms                                                 | 137 ms: 1.67x faster                                                      |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 578 ms: 1.65x faster                                                      |
| scimark_sor              | 197 ms                                                 | 120 ms: 1.64x faster                                                      |
| nbody                    | 142 ms                                                 | 87.7 ms: 1.61x faster                                                     |
| richards                 | 74.9 ms                                                | 46.4 ms: 1.61x faster                                                     |
| hexiom                   | 9.53 ms                                                | 6.03 ms: 1.58x faster                                                     |
| sqlglot_parse            | 2.06 ms                                                | 1.31 ms: 1.57x faster                                                     |
| scimark_monte_carlo      | 108 ms                                                 | 69.1 ms: 1.57x faster                                                     |
| pickle_pure_python       | 455 us                                                 | 293 us: 1.55x faster                                                      |
| sqlglot_transpile        | 2.45 ms                                                | 1.62 ms: 1.51x faster                                                     |
| pyflate                  | 673 ms                                                 | 449 ms: 1.50x faster                                                      |
| python_startup           | 14.2 ms                                                | 9.52 ms: 1.49x faster                                                     |
| scimark_lu               | 163 ms                                                 | 111 ms: 1.47x faster                                                      |
| unpack_sequence          | 64.7 ns                                                | 44.4 ns: 1.46x faster                                                     |
| coroutines               | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                     |
| spectral_norm            | 150 ms                                                 | 105 ms: 1.42x faster                                                      |
| unpickle_pure_python     | 300 us                                                 | 211 us: 1.42x faster                                                      |
| json_dumps               | 13.5 ms                                                | 9.68 ms: 1.40x faster                                                     |
| deepcopy_memo            | 52.3 us                                                | 37.6 us: 1.39x faster                                                     |
| logging_format           | 8.91 us                                                | 6.43 us: 1.38x faster                                                     |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.37x faster                                                     |
| logging_simple           | 8.07 us                                                | 5.89 us: 1.37x faster                                                     |
| pprint_pformat           | 1.99 sec                                               | 1.46 sec: 1.36x faster                                                    |
| pprint_safe_repr         | 955 ms                                                 | 710 ms: 1.34x faster                                                      |
| pycparser                | 1.50 sec                                               | 1.15 sec: 1.31x faster                                                    |
| comprehensions           | 26.8 us                                                | 20.5 us: 1.31x faster                                                     |
| regex_compile            | 177 ms                                                 | 137 ms: 1.29x faster                                                      |
| sqlglot_normalize        | 135 ms                                                 | 105 ms: 1.29x faster                                                      |
| tornado_http             | 127 ms                                                 | 99.6 ms: 1.28x faster                                                     |
| deepcopy                 | 442 us                                                 | 347 us: 1.27x faster                                                      |
| tomli_loads              | 2.92 sec                                               | 2.30 sec: 1.27x faster                                                    |
| nqueens                  | 100 ms                                                 | 79.2 ms: 1.26x faster                                                     |
| float                    | 111 ms                                                 | 87.7 ms: 1.26x faster                                                     |
| fannkuch                 | 486 ms                                                 | 389 ms: 1.25x faster                                                      |
| xml_etree_process        | 74.9 ms                                                | 60.0 ms: 1.25x faster                                                     |
| sqlglot_optimize         | 65.3 ms                                                | 53.0 ms: 1.23x faster                                                     |
| docutils                 | 3.17 sec                                               | 2.57 sec: 1.23x faster                                                    |
| deepcopy_reduce          | 3.82 us                                                | 3.15 us: 1.21x faster                                                     |
| scimark_fft              | 424 ms                                                 | 356 ms: 1.19x faster                                                      |
| create_gc_cycles         | 1.67 ms                                                | 1.44 ms: 1.16x faster                                                     |
| bench_thread_pool        | 947 us                                                 | 822 us: 1.15x faster                                                      |
| dulwich_log              | 75.9 ms                                                | 65.9 ms: 1.15x faster                                                     |
| json_loads               | 28.8 us                                                | 25.3 us: 1.14x faster                                                     |
| json                     | 5.42 ms                                                | 4.76 ms: 1.14x faster                                                     |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.82 ms: 1.13x faster                                                     |
| mdp                      | 2.82 sec                                               | 2.55 sec: 1.11x faster                                                    |
| regex_v8                 | 25.0 ms                                                | 22.8 ms: 1.10x faster                                                     |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.09x faster                                                      |
| mypy2                    | 428 ms                                                 | 397 ms: 1.08x faster                                                      |
| pathlib                  | 20.0 ms                                                | 18.7 ms: 1.07x faster                                                     |
| xml_etree_generate       | 94.2 ms                                                | 88.1 ms: 1.07x faster                                                     |
| regex_dna                | 222 ms                                                 | 208 ms: 1.07x faster                                                      |
| sqlite_synth             | 2.93 us                                                | 2.76 us: 1.06x faster                                                     |
| pickle_list              | 4.56 us                                                | 4.63 us: 1.02x slower                                                     |
| async_generators         | 425 ms                                                 | 432 ms: 1.02x slower                                                      |
| gc_traversal             | 3.84 ms                                                | 3.94 ms: 1.03x slower                                                     |
| pickle                   | 10.3 us                                                | 10.6 us: 1.03x slower                                                     |
| unpickle_list            | 4.82 us                                                | 4.99 us: 1.04x slower                                                     |
| pidigits                 | 190 ms                                                 | 201 ms: 1.06x slower                                                      |
| unpickle                 | 14.1 us                                                | 15.0 us: 1.06x slower                                                     |
| regex_effbot             | 3.23 ms                                                | 3.57 ms: 1.10x slower                                                     |
| pickle_dict              | 27.3 us                                                | 31.6 us: 1.16x slower                                                     |
| telco                    | 6.54 ms                                                | 7.72 ms: 1.18x slower                                                     |
| python_startup_no_site   | 5.82 ms                                                | 6.92 ms: 1.19x slower                                                     |
| dask                     | 423 ms                                                 | 524 ms: 1.24x slower                                                      |
| coverage                 | 72.8 ms                                                | 93.3 ms: 1.28x slower                                                     |
| xml_etree_parse          | 163 ms                                                 | 346 ms: 2.12x slower                                                      |
| xml_etree_iterparse      | 111 ms                                                 | 323 ms: 2.90x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.23x

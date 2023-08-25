
# Results vs. 3.10.4

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: acf9079
- commit date: 2023-08-13
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-acf9079 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.43 sec: 1.30x faster                                                    |
| tornado_http   | 127 ms                                                 | 93.6 ms: 1.36x faster                                                     |
| Geometric mean | (ref)                                                  | 1.33x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-acf9079 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.6 ms: 1.58x faster                                                     |
| float          | 111 ms                                                 | 75.4 ms: 1.47x faster                                                     |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.33x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-acf9079 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.30x faster                                                      |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                     |
| regex_dna      | 222 ms                                                 | 209 ms: 1.06x faster                                                      |
| regex_effbot   | 3.23 ms                                                | 3.59 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-acf9079 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 299 us: 1.52x faster                                                      |
| unpickle_pure_python | 300 us                                                 | 215 us: 1.40x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.84 ms: 1.38x faster                                                     |
| xml_etree_process    | 74.9 ms                                                | 57.2 ms: 1.31x faster                                                     |
| tomli_loads          | 2.92 sec                                               | 2.33 sec: 1.25x faster                                                    |
| xml_etree_generate   | 94.2 ms                                                | 83.3 ms: 1.13x faster                                                     |
| json_loads           | 28.8 us                                                | 25.7 us: 1.12x faster                                                     |
| xml_etree_iterparse  | 111 ms                                                 | 100 ms: 1.11x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                                      |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                                     |
| unpickle_list        | 4.82 us                                                | 5.11 us: 1.06x slower                                                     |
| unpickle             | 14.1 us                                                | 15.2 us: 1.07x slower                                                     |
| pickle_dict          | 27.3 us                                                | 31.6 us: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                              |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-acf9079 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.25 ms: 1.53x faster                                                     |
| python_startup_no_site | 5.82 ms                                                | 6.73 ms: 1.16x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-acf9079 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-acf9079 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 149 us: 3.43x faster                                                      |
| generators               | 76.8 ms                                                | 28.5 ms: 2.69x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 677 ms: 2.62x faster                                                      |
| deltablue                | 7.42 ms                                                | 3.14 ms: 2.36x faster                                                     |
| async_tree_none          | 717 ms                                                 | 311 ms: 2.31x faster                                                      |
| async_tree_memoization   | 854 ms                                                 | 395 ms: 2.16x faster                                                      |
| asyncio_tcp              | 925 ms                                                 | 485 ms: 1.91x faster                                                      |
| chaos                    | 106 ms                                                 | 58.8 ms: 1.81x faster                                                     |
| crypto_pyaes             | 118 ms                                                 | 68.3 ms: 1.73x faster                                                     |
| raytrace                 | 464 ms                                                 | 270 ms: 1.72x faster                                                      |
| richards_super           | 90.7 ms                                                | 52.9 ms: 1.72x faster                                                     |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 562 ms: 1.69x faster                                                      |
| logging_silent           | 175 ns                                                 | 104 ns: 1.69x faster                                                      |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                    |
| go                       | 229 ms                                                 | 139 ms: 1.65x faster                                                      |
| scimark_sor              | 197 ms                                                 | 121 ms: 1.62x faster                                                      |
| scimark_monte_carlo      | 108 ms                                                 | 66.8 ms: 1.62x faster                                                     |
| richards                 | 74.9 ms                                                | 46.8 ms: 1.60x faster                                                     |
| sqlglot_parse            | 2.06 ms                                                | 1.29 ms: 1.60x faster                                                     |
| hexiom                   | 9.53 ms                                                | 5.97 ms: 1.60x faster                                                     |
| nbody                    | 142 ms                                                 | 89.6 ms: 1.58x faster                                                     |
| python_startup           | 14.2 ms                                                | 9.25 ms: 1.53x faster                                                     |
| sqlglot_transpile        | 2.45 ms                                                | 1.61 ms: 1.52x faster                                                     |
| pickle_pure_python       | 455 us                                                 | 299 us: 1.52x faster                                                      |
| pyflate                  | 673 ms                                                 | 444 ms: 1.52x faster                                                      |
| unpack_sequence          | 64.7 ns                                                | 43.2 ns: 1.50x faster                                                     |
| float                    | 111 ms                                                 | 75.4 ms: 1.47x faster                                                     |
| scimark_lu               | 163 ms                                                 | 112 ms: 1.46x faster                                                      |
| coroutines               | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                     |
| spectral_norm            | 150 ms                                                 | 106 ms: 1.41x faster                                                      |
| unpickle_pure_python     | 300 us                                                 | 215 us: 1.40x faster                                                      |
| deepcopy_memo            | 52.3 us                                                | 37.8 us: 1.38x faster                                                     |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                     |
| json_dumps               | 13.5 ms                                                | 9.84 ms: 1.38x faster                                                     |
| logging_format           | 8.91 us                                                | 6.53 us: 1.36x faster                                                     |
| tornado_http             | 127 ms                                                 | 93.6 ms: 1.36x faster                                                     |
| logging_simple           | 8.07 us                                                | 5.95 us: 1.36x faster                                                     |
| pprint_pformat           | 1.99 sec                                               | 1.48 sec: 1.34x faster                                                    |
| comprehensions           | 26.8 us                                                | 20.2 us: 1.33x faster                                                     |
| pycparser                | 1.50 sec                                               | 1.14 sec: 1.32x faster                                                    |
| pprint_safe_repr         | 955 ms                                                 | 725 ms: 1.32x faster                                                      |
| xml_etree_process        | 74.9 ms                                                | 57.2 ms: 1.31x faster                                                     |
| docutils                 | 3.17 sec                                               | 2.43 sec: 1.30x faster                                                    |
| regex_compile            | 177 ms                                                 | 137 ms: 1.30x faster                                                      |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.27x faster                                                      |
| deepcopy                 | 442 us                                                 | 351 us: 1.26x faster                                                      |
| tomli_loads              | 2.92 sec                                               | 2.33 sec: 1.25x faster                                                    |
| nqueens                  | 100 ms                                                 | 80.2 ms: 1.25x faster                                                     |
| mypy2                    | 428 ms                                                 | 347 ms: 1.24x faster                                                      |
| sqlglot_optimize         | 65.3 ms                                                | 52.9 ms: 1.24x faster                                                     |
| fannkuch                 | 486 ms                                                 | 394 ms: 1.23x faster                                                      |
| deepcopy_reduce          | 3.82 us                                                | 3.19 us: 1.20x faster                                                     |
| scimark_fft              | 424 ms                                                 | 356 ms: 1.19x faster                                                      |
| create_gc_cycles         | 1.67 ms                                                | 1.44 ms: 1.16x faster                                                     |
| bench_thread_pool        | 947 us                                                 | 822 us: 1.15x faster                                                      |
| dulwich_log              | 75.9 ms                                                | 66.3 ms: 1.14x faster                                                     |
| xml_etree_generate       | 94.2 ms                                                | 83.3 ms: 1.13x faster                                                     |
| regex_v8                 | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                     |
| json_loads               | 28.8 us                                                | 25.7 us: 1.12x faster                                                     |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.86 ms: 1.12x faster                                                     |
| xml_etree_iterparse      | 111 ms                                                 | 100 ms: 1.11x faster                                                      |
| mdp                      | 2.82 sec                                               | 2.54 sec: 1.11x faster                                                    |
| json                     | 5.42 ms                                                | 4.88 ms: 1.11x faster                                                     |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.09x faster                                                      |
| pathlib                  | 20.0 ms                                                | 18.4 ms: 1.09x faster                                                     |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                                      |
| regex_dna                | 222 ms                                                 | 209 ms: 1.06x faster                                                      |
| gc_traversal             | 3.84 ms                                                | 3.64 ms: 1.05x faster                                                     |
| sqlite_synth             | 2.93 us                                                | 2.82 us: 1.04x faster                                                     |
| pidigits                 | 190 ms                                                 | 189 ms: 1.01x faster                                                      |
| pickle                   | 10.3 us                                                | 10.4 us: 1.01x slower                                                     |
| async_generators         | 425 ms                                                 | 431 ms: 1.01x slower                                                      |
| unpickle_list            | 4.82 us                                                | 5.11 us: 1.06x slower                                                     |
| unpickle                 | 14.1 us                                                | 15.2 us: 1.07x slower                                                     |
| regex_effbot             | 3.23 ms                                                | 3.59 ms: 1.11x slower                                                     |
| python_startup_no_site   | 5.82 ms                                                | 6.73 ms: 1.16x slower                                                     |
| pickle_dict              | 27.3 us                                                | 31.6 us: 1.16x slower                                                     |
| dask                     | 423 ms                                                 | 494 ms: 1.17x slower                                                      |
| telco                    | 6.54 ms                                                | 7.96 ms: 1.22x slower                                                     |
| coverage                 | 72.8 ms                                                | 91.8 ms: 1.26x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.33x faster                                                              |

Benchmark hidden because not significant (2): pickle_list, bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

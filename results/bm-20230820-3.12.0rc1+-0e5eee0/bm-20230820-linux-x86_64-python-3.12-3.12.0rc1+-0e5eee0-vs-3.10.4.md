
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 0e5eee0
- commit date: 2023-08-20
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-linux-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 269 ms: 1.25x faster                                    |
| docutils       | 3.17 sec                                               | 2.73 sec: 1.16x faster                                  |
| tornado_http   | 127 ms                                                 | 99.4 ms: 1.28x faster                                   |
| Geometric mean | (ref)                                                  | 1.23x faster                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-linux-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.0 ms: 1.61x faster                                   |
| float          | 111 ms                                                 | 80.8 ms: 1.37x faster                                   |
| pidigits       | 190 ms                                                 | 200 ms: 1.06x slower                                    |
| Geometric mean | (ref)                                                  | 1.28x faster                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-linux-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 146 ms: 1.21x faster                                    |
| regex_v8       | 25.0 ms                                                | 22.8 ms: 1.10x faster                                   |
| regex_dna      | 222 ms                                                 | 203 ms: 1.09x faster                                    |
| regex_effbot   | 3.23 ms                                                | 3.70 ms: 1.15x slower                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-linux-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 312 us: 1.46x faster                                    |
| json_dumps           | 13.5 ms                                                | 9.66 ms: 1.40x faster                                   |
| unpickle_pure_python | 300 us                                                 | 219 us: 1.37x faster                                    |
| tomli_loads          | 2.92 sec                                               | 2.22 sec: 1.32x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 59.2 ms: 1.26x faster                                   |
| json_loads           | 28.8 us                                                | 25.2 us: 1.14x faster                                   |
| xml_etree_generate   | 94.2 ms                                                | 85.1 ms: 1.11x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                    |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                    |
| pickle_list          | 4.56 us                                                | 4.62 us: 1.01x slower                                   |
| unpickle_list        | 4.82 us                                                | 5.05 us: 1.05x slower                                   |
| unpickle             | 14.1 us                                                | 15.2 us: 1.07x slower                                   |
| pickle_dict          | 27.3 us                                                | 30.2 us: 1.11x slower                                   |
| Geometric mean       | (ref)                                                  | 1.13x faster                                            |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-linux-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.31 ms: 1.52x faster                                   |
| python_startup_no_site | 5.82 ms                                                | 6.77 ms: 1.16x slower                                   |
| Geometric mean         | (ref)                                                  | 1.14x faster                                            |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-linux-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.36x faster                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-linux-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 145 us: 3.52x faster                                    |
| generators               | 76.8 ms                                                | 30.2 ms: 2.54x faster                                   |
| deltablue                | 7.42 ms                                                | 3.56 ms: 2.08x faster                                   |
| asyncio_tcp              | 925 ms                                                 | 516 ms: 1.79x faster                                    |
| richards_super           | 90.7 ms                                                | 50.8 ms: 1.79x faster                                   |
| richards                 | 74.9 ms                                                | 44.1 ms: 1.70x faster                                   |
| go                       | 229 ms                                                 | 136 ms: 1.68x faster                                    |
| logging_silent           | 175 ns                                                 | 104 ns: 1.68x faster                                    |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                  |
| chaos                    | 106 ms                                                 | 64.3 ms: 1.65x faster                                   |
| nbody                    | 142 ms                                                 | 88.0 ms: 1.61x faster                                   |
| scimark_sor              | 197 ms                                                 | 126 ms: 1.57x faster                                    |
| sqlglot_parse            | 2.06 ms                                                | 1.33 ms: 1.54x faster                                   |
| raytrace                 | 464 ms                                                 | 302 ms: 1.53x faster                                    |
| async_tree_io            | 1.77 sec                                               | 1.17 sec: 1.52x faster                                  |
| python_startup           | 14.2 ms                                                | 9.31 ms: 1.52x faster                                   |
| async_tree_none          | 717 ms                                                 | 472 ms: 1.52x faster                                    |
| hexiom                   | 9.53 ms                                                | 6.28 ms: 1.52x faster                                   |
| crypto_pyaes             | 118 ms                                                 | 78.5 ms: 1.51x faster                                   |
| scimark_monte_carlo      | 108 ms                                                 | 71.8 ms: 1.51x faster                                   |
| pyflate                  | 673 ms                                                 | 450 ms: 1.50x faster                                    |
| async_tree_memoization   | 854 ms                                                 | 574 ms: 1.49x faster                                    |
| sqlglot_transpile        | 2.45 ms                                                | 1.66 ms: 1.47x faster                                   |
| scimark_lu               | 163 ms                                                 | 111 ms: 1.47x faster                                    |
| pickle_pure_python       | 455 us                                                 | 312 us: 1.46x faster                                    |
| coroutines               | 31.8 ms                                                | 22.3 ms: 1.43x faster                                   |
| json_dumps               | 13.5 ms                                                | 9.66 ms: 1.40x faster                                   |
| spectral_norm            | 150 ms                                                 | 107 ms: 1.40x faster                                    |
| deepcopy_memo            | 52.3 us                                                | 37.5 us: 1.39x faster                                   |
| unpickle_pure_python     | 300 us                                                 | 219 us: 1.37x faster                                    |
| float                    | 111 ms                                                 | 80.8 ms: 1.37x faster                                   |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.36x faster                                   |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 713 ms: 1.33x faster                                    |
| pprint_pformat           | 1.99 sec                                               | 1.50 sec: 1.32x faster                                  |
| tomli_loads              | 2.92 sec                                               | 2.22 sec: 1.32x faster                                  |
| pycparser                | 1.50 sec                                               | 1.16 sec: 1.30x faster                                  |
| comprehensions           | 26.8 us                                                | 20.7 us: 1.30x faster                                   |
| pprint_safe_repr         | 955 ms                                                 | 738 ms: 1.29x faster                                    |
| logging_simple           | 8.07 us                                                | 6.26 us: 1.29x faster                                   |
| tornado_http             | 127 ms                                                 | 99.4 ms: 1.28x faster                                   |
| logging_format           | 8.91 us                                                | 6.96 us: 1.28x faster                                   |
| xml_etree_process        | 74.9 ms                                                | 59.2 ms: 1.26x faster                                   |
| 2to3                     | 336 ms                                                 | 269 ms: 1.25x faster                                    |
| deepcopy                 | 442 us                                                 | 354 us: 1.25x faster                                    |
| mypy2                    | 428 ms                                                 | 344 ms: 1.24x faster                                    |
| deepcopy_reduce          | 3.82 us                                                | 3.09 us: 1.24x faster                                   |
| fannkuch                 | 486 ms                                                 | 395 ms: 1.23x faster                                    |
| sqlglot_normalize        | 135 ms                                                 | 110 ms: 1.23x faster                                    |
| nqueens                  | 100 ms                                                 | 81.3 ms: 1.23x faster                                   |
| sqlglot_optimize         | 65.3 ms                                                | 54.0 ms: 1.21x faster                                   |
| regex_compile            | 177 ms                                                 | 146 ms: 1.21x faster                                    |
| unpack_sequence          | 64.7 ns                                                | 53.7 ns: 1.21x faster                                   |
| scimark_fft              | 424 ms                                                 | 358 ms: 1.18x faster                                    |
| docutils                 | 3.17 sec                                               | 2.73 sec: 1.16x faster                                  |
| sqlalchemy_imperative    | 21.2 ms                                                | 18.3 ms: 1.16x faster                                   |
| json_loads               | 28.8 us                                                | 25.2 us: 1.14x faster                                   |
| sqlalchemy_declarative   | 165 ms                                                 | 145 ms: 1.14x faster                                    |
| bench_thread_pool        | 947 us                                                 | 832 us: 1.14x faster                                    |
| json                     | 5.42 ms                                                | 4.81 ms: 1.13x faster                                   |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.90 ms: 1.11x faster                                   |
| dulwich_log              | 75.9 ms                                                | 68.3 ms: 1.11x faster                                   |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.11x faster                                   |
| xml_etree_generate       | 94.2 ms                                                | 85.1 ms: 1.11x faster                                   |
| pathlib                  | 20.0 ms                                                | 18.2 ms: 1.10x faster                                   |
| regex_v8                 | 25.0 ms                                                | 22.8 ms: 1.10x faster                                   |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.10x faster                                    |
| regex_dna                | 222 ms                                                 | 203 ms: 1.09x faster                                    |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                    |
| sqlite_synth             | 2.93 us                                                | 2.73 us: 1.08x faster                                   |
| mdp                      | 2.82 sec                                               | 2.66 sec: 1.06x faster                                  |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                    |
| pickle_list              | 4.56 us                                                | 4.62 us: 1.01x slower                                   |
| telco                    | 6.54 ms                                                | 6.84 ms: 1.05x slower                                   |
| unpickle_list            | 4.82 us                                                | 5.05 us: 1.05x slower                                   |
| pidigits                 | 190 ms                                                 | 200 ms: 1.06x slower                                    |
| async_generators         | 425 ms                                                 | 452 ms: 1.06x slower                                    |
| unpickle                 | 14.1 us                                                | 15.2 us: 1.07x slower                                   |
| pickle_dict              | 27.3 us                                                | 30.2 us: 1.11x slower                                   |
| regex_effbot             | 3.23 ms                                                | 3.70 ms: 1.15x slower                                   |
| gc_traversal             | 3.84 ms                                                | 4.46 ms: 1.16x slower                                   |
| python_startup_no_site   | 5.82 ms                                                | 6.77 ms: 1.16x slower                                   |
| dask                     | 423 ms                                                 | 538 ms: 1.27x slower                                    |
| coverage                 | 72.8 ms                                                | 94.9 ms: 1.30x slower                                   |
| Geometric mean           | (ref)                                                  | 1.27x faster                                            |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

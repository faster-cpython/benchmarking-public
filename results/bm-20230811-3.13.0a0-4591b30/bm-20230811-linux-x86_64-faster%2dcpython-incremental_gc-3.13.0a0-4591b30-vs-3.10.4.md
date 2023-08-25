
# Results vs. 3.10.4

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: 4591b30
- commit date: 2023-08-11
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-4591b30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                    |
| tornado_http   | 127 ms                                                 | 103 ms: 1.23x faster                                                      |
| Geometric mean | (ref)                                                  | 1.25x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-4591b30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 90.0 ms: 1.57x faster                                                     |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.17x faster                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-4591b30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.30x faster                                                      |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                     |
| regex_dna      | 222 ms                                                 | 215 ms: 1.03x faster                                                      |
| regex_effbot   | 3.23 ms                                                | 3.59 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-4591b30 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 294 us: 1.55x faster                                                      |
| unpickle_pure_python | 300 us                                                 | 213 us: 1.41x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.75 ms: 1.39x faster                                                     |
| xml_etree_process    | 74.9 ms                                                | 58.3 ms: 1.29x faster                                                     |
| tomli_loads          | 2.92 sec                                               | 2.29 sec: 1.27x faster                                                    |
| json_loads           | 28.8 us                                                | 25.3 us: 1.14x faster                                                     |
| unpickle_list        | 4.82 us                                                | 4.88 us: 1.01x slower                                                     |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                                     |
| unpickle             | 14.1 us                                                | 15.6 us: 1.10x slower                                                     |
| pickle_dict          | 27.3 us                                                | 31.6 us: 1.16x slower                                                     |
| xml_etree_parse      | 163 ms                                                 | 570 ms: 3.50x slower                                                      |
| xml_etree_iterparse  | 111 ms                                                 | 516 ms: 4.63x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.10x slower                                                              |

Benchmark hidden because not significant (2): xml_etree_generate, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-4591b30 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.47 ms: 1.49x faster                                                     |
| python_startup_no_site | 5.82 ms                                                | 6.89 ms: 1.18x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.12x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-4591b30 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.9 ms: 1.36x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-4591b30 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 147 us: 3.48x faster                                                      |
| generators               | 76.8 ms                                                | 28.7 ms: 2.67x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 700 ms: 2.53x faster                                                      |
| deltablue                | 7.42 ms                                                | 3.33 ms: 2.23x faster                                                     |
| async_tree_none          | 717 ms                                                 | 340 ms: 2.11x faster                                                      |
| async_tree_memoization   | 854 ms                                                 | 431 ms: 1.98x faster                                                      |
| asyncio_tcp              | 925 ms                                                 | 480 ms: 1.93x faster                                                      |
| chaos                    | 106 ms                                                 | 58.4 ms: 1.82x faster                                                     |
| crypto_pyaes             | 118 ms                                                 | 68.9 ms: 1.72x faster                                                     |
| logging_silent           | 175 ns                                                 | 103 ns: 1.70x faster                                                      |
| raytrace                 | 464 ms                                                 | 272 ms: 1.70x faster                                                      |
| richards_super           | 90.7 ms                                                | 53.3 ms: 1.70x faster                                                     |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                    |
| go                       | 229 ms                                                 | 139 ms: 1.64x faster                                                      |
| scimark_sor              | 197 ms                                                 | 120 ms: 1.64x faster                                                      |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 586 ms: 1.62x faster                                                      |
| richards                 | 74.9 ms                                                | 46.5 ms: 1.61x faster                                                     |
| scimark_monte_carlo      | 108 ms                                                 | 67.7 ms: 1.60x faster                                                     |
| hexiom                   | 9.53 ms                                                | 5.98 ms: 1.59x faster                                                     |
| unpack_sequence          | 64.7 ns                                                | 40.7 ns: 1.59x faster                                                     |
| sqlglot_parse            | 2.06 ms                                                | 1.30 ms: 1.59x faster                                                     |
| nbody                    | 142 ms                                                 | 90.0 ms: 1.57x faster                                                     |
| pickle_pure_python       | 455 us                                                 | 294 us: 1.55x faster                                                      |
| pyflate                  | 673 ms                                                 | 438 ms: 1.54x faster                                                      |
| python_startup           | 14.2 ms                                                | 9.47 ms: 1.49x faster                                                     |
| sqlglot_transpile        | 2.45 ms                                                | 1.66 ms: 1.47x faster                                                     |
| scimark_lu               | 163 ms                                                 | 113 ms: 1.45x faster                                                      |
| coroutines               | 31.8 ms                                                | 22.0 ms: 1.45x faster                                                     |
| spectral_norm            | 150 ms                                                 | 104 ms: 1.44x faster                                                      |
| unpickle_pure_python     | 300 us                                                 | 213 us: 1.41x faster                                                      |
| json_dumps               | 13.5 ms                                                | 9.75 ms: 1.39x faster                                                     |
| logging_format           | 8.91 us                                                | 6.43 us: 1.39x faster                                                     |
| deepcopy_memo            | 52.3 us                                                | 38.1 us: 1.37x faster                                                     |
| pprint_pformat           | 1.99 sec                                               | 1.46 sec: 1.36x faster                                                    |
| mako                     | 14.8 ms                                                | 10.9 ms: 1.36x faster                                                     |
| logging_simple           | 8.07 us                                                | 5.94 us: 1.36x faster                                                     |
| pycparser                | 1.50 sec                                               | 1.11 sec: 1.35x faster                                                    |
| pprint_safe_repr         | 955 ms                                                 | 710 ms: 1.34x faster                                                      |
| comprehensions           | 26.8 us                                                | 20.4 us: 1.32x faster                                                     |
| regex_compile            | 177 ms                                                 | 137 ms: 1.30x faster                                                      |
| xml_etree_process        | 74.9 ms                                                | 58.3 ms: 1.29x faster                                                     |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.27x faster                                                      |
| tomli_loads              | 2.92 sec                                               | 2.29 sec: 1.27x faster                                                    |
| nqueens                  | 100 ms                                                 | 79.5 ms: 1.26x faster                                                     |
| docutils                 | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                    |
| fannkuch                 | 486 ms                                                 | 388 ms: 1.25x faster                                                      |
| deepcopy                 | 442 us                                                 | 356 us: 1.24x faster                                                      |
| tornado_http             | 127 ms                                                 | 103 ms: 1.23x faster                                                      |
| sqlglot_optimize         | 65.3 ms                                                | 53.8 ms: 1.21x faster                                                     |
| deepcopy_reduce          | 3.82 us                                                | 3.19 us: 1.20x faster                                                     |
| scimark_fft              | 424 ms                                                 | 361 ms: 1.17x faster                                                      |
| create_gc_cycles         | 1.67 ms                                                | 1.43 ms: 1.17x faster                                                     |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.71 ms: 1.16x faster                                                     |
| bench_thread_pool        | 947 us                                                 | 824 us: 1.15x faster                                                      |
| dulwich_log              | 75.9 ms                                                | 66.4 ms: 1.14x faster                                                     |
| json_loads               | 28.8 us                                                | 25.3 us: 1.14x faster                                                     |
| json                     | 5.42 ms                                                | 4.79 ms: 1.13x faster                                                     |
| regex_v8                 | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                     |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.09x faster                                                      |
| mdp                      | 2.82 sec                                               | 2.59 sec: 1.09x faster                                                    |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                                     |
| pathlib                  | 20.0 ms                                                | 18.7 ms: 1.07x faster                                                     |
| gc_traversal             | 3.84 ms                                                | 3.68 ms: 1.05x faster                                                     |
| regex_dna                | 222 ms                                                 | 215 ms: 1.03x faster                                                      |
| pidigits                 | 190 ms                                                 | 189 ms: 1.01x faster                                                      |
| unpickle_list            | 4.82 us                                                | 4.88 us: 1.01x slower                                                     |
| mypy2                    | 428 ms                                                 | 444 ms: 1.04x slower                                                      |
| pickle                   | 10.3 us                                                | 10.7 us: 1.04x slower                                                     |
| async_generators         | 425 ms                                                 | 447 ms: 1.05x slower                                                      |
| unpickle                 | 14.1 us                                                | 15.6 us: 1.10x slower                                                     |
| regex_effbot             | 3.23 ms                                                | 3.59 ms: 1.11x slower                                                     |
| pickle_dict              | 27.3 us                                                | 31.6 us: 1.16x slower                                                     |
| python_startup_no_site   | 5.82 ms                                                | 6.89 ms: 1.18x slower                                                     |
| telco                    | 6.54 ms                                                | 8.04 ms: 1.23x slower                                                     |
| dask                     | 423 ms                                                 | 520 ms: 1.23x slower                                                      |
| coverage                 | 72.8 ms                                                | 93.5 ms: 1.28x slower                                                     |
| xml_etree_parse          | 163 ms                                                 | 570 ms: 3.50x slower                                                      |
| xml_etree_iterparse      | 111 ms                                                 | 516 ms: 4.63x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.27x faster                                                              |

Benchmark hidden because not significant (4): xml_etree_generate, pickle_list, float, bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.20x

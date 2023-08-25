
# Results vs. 3.10.4

- fork: faster-cpython
- ref: gc_stats
- machine: linux-x86_64
- commit hash: 90a79be
- commit date: 2023-07-29
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-90a79be |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.65 sec: 1.19x faster                                              |
| tornado_http   | 127 ms                                                 | 95.6 ms: 1.33x faster                                               |
| Geometric mean | (ref)                                                  | 1.26x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-90a79be |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 94.2 ms: 1.50x faster                                               |
| float          | 111 ms                                                 | 81.4 ms: 1.36x faster                                               |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.27x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-90a79be |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                                |
| regex_v8       | 25.0 ms                                                | 22.7 ms: 1.10x faster                                               |
| regex_dna      | 222 ms                                                 | 208 ms: 1.06x faster                                                |
| regex_effbot   | 3.23 ms                                                | 3.53 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-90a79be |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 295 us: 1.55x faster                                                |
| unpickle_pure_python | 300 us                                                 | 214 us: 1.41x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.67 ms: 1.40x faster                                               |
| xml_etree_process    | 74.9 ms                                                | 58.0 ms: 1.29x faster                                               |
| tomli_loads          | 2.92 sec                                               | 2.30 sec: 1.27x faster                                              |
| xml_etree_generate   | 94.2 ms                                                | 84.1 ms: 1.12x faster                                               |
| json_loads           | 28.8 us                                                | 26.1 us: 1.10x faster                                               |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                                |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                               |
| unpickle_list        | 4.82 us                                                | 4.92 us: 1.02x slower                                               |
| pickle_list          | 4.56 us                                                | 4.71 us: 1.03x slower                                               |
| unpickle             | 14.1 us                                                | 15.2 us: 1.07x slower                                               |
| pickle_dict          | 27.3 us                                                | 31.8 us: 1.17x slower                                               |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-90a79be |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.39 ms: 1.51x faster                                               |
| python_startup_no_site | 5.82 ms                                                | 6.87 ms: 1.18x slower                                               |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-90a79be |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.6 ms: 1.39x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-90a79be |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 146 us: 3.51x faster                                                |
| generators               | 76.8 ms                                                | 29.1 ms: 2.64x faster                                               |
| deltablue                | 7.42 ms                                                | 3.29 ms: 2.26x faster                                               |
| asyncio_tcp              | 925 ms                                                 | 478 ms: 1.94x faster                                                |
| chaos                    | 106 ms                                                 | 60.3 ms: 1.76x faster                                               |
| richards_super           | 90.7 ms                                                | 52.7 ms: 1.72x faster                                               |
| raytrace                 | 464 ms                                                 | 272 ms: 1.71x faster                                                |
| logging_silent           | 175 ns                                                 | 103 ns: 1.69x faster                                                |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                              |
| crypto_pyaes             | 118 ms                                                 | 71.0 ms: 1.67x faster                                               |
| go                       | 229 ms                                                 | 139 ms: 1.65x faster                                                |
| scimark_sor              | 197 ms                                                 | 121 ms: 1.62x faster                                                |
| richards                 | 74.9 ms                                                | 46.4 ms: 1.61x faster                                               |
| scimark_monte_carlo      | 108 ms                                                 | 67.2 ms: 1.61x faster                                               |
| sqlglot_parse            | 2.06 ms                                                | 1.29 ms: 1.59x faster                                               |
| hexiom                   | 9.53 ms                                                | 6.09 ms: 1.56x faster                                               |
| pickle_pure_python       | 455 us                                                 | 295 us: 1.55x faster                                                |
| sqlglot_transpile        | 2.45 ms                                                | 1.61 ms: 1.52x faster                                               |
| pyflate                  | 673 ms                                                 | 444 ms: 1.52x faster                                                |
| python_startup           | 14.2 ms                                                | 9.39 ms: 1.51x faster                                               |
| nbody                    | 142 ms                                                 | 94.2 ms: 1.50x faster                                               |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.49x faster                                              |
| async_tree_none          | 717 ms                                                 | 483 ms: 1.49x faster                                                |
| coroutines               | 31.8 ms                                                | 21.6 ms: 1.47x faster                                               |
| scimark_lu               | 163 ms                                                 | 112 ms: 1.46x faster                                                |
| async_tree_memoization   | 854 ms                                                 | 587 ms: 1.46x faster                                                |
| spectral_norm            | 150 ms                                                 | 107 ms: 1.41x faster                                                |
| unpickle_pure_python     | 300 us                                                 | 214 us: 1.41x faster                                                |
| json_dumps               | 13.5 ms                                                | 9.67 ms: 1.40x faster                                               |
| mako                     | 14.8 ms                                                | 10.6 ms: 1.39x faster                                               |
| deepcopy_memo            | 52.3 us                                                | 37.7 us: 1.39x faster                                               |
| logging_format           | 8.91 us                                                | 6.45 us: 1.38x faster                                               |
| unpack_sequence          | 64.7 ns                                                | 47.3 ns: 1.37x faster                                               |
| logging_simple           | 8.07 us                                                | 5.92 us: 1.36x faster                                               |
| float                    | 111 ms                                                 | 81.4 ms: 1.36x faster                                               |
| pprint_pformat           | 1.99 sec                                               | 1.49 sec: 1.33x faster                                              |
| tornado_http             | 127 ms                                                 | 95.6 ms: 1.33x faster                                               |
| pprint_safe_repr         | 955 ms                                                 | 722 ms: 1.32x faster                                                |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 723 ms: 1.32x faster                                                |
| comprehensions           | 26.8 us                                                | 20.4 us: 1.31x faster                                               |
| regex_compile            | 177 ms                                                 | 136 ms: 1.30x faster                                                |
| xml_etree_process        | 74.9 ms                                                | 58.0 ms: 1.29x faster                                               |
| sqlglot_normalize        | 135 ms                                                 | 105 ms: 1.29x faster                                                |
| pycparser                | 1.50 sec                                               | 1.17 sec: 1.28x faster                                              |
| mypy2                    | 428 ms                                                 | 337 ms: 1.27x faster                                                |
| tomli_loads              | 2.92 sec                                               | 2.30 sec: 1.27x faster                                              |
| deepcopy                 | 442 us                                                 | 350 us: 1.26x faster                                                |
| nqueens                  | 100 ms                                                 | 79.9 ms: 1.25x faster                                               |
| sqlglot_optimize         | 65.3 ms                                                | 53.0 ms: 1.23x faster                                               |
| deepcopy_reduce          | 3.82 us                                                | 3.14 us: 1.22x faster                                               |
| fannkuch                 | 486 ms                                                 | 401 ms: 1.21x faster                                                |
| docutils                 | 3.17 sec                                               | 2.65 sec: 1.19x faster                                              |
| scimark_fft              | 424 ms                                                 | 358 ms: 1.18x faster                                                |
| bench_thread_pool        | 947 us                                                 | 815 us: 1.16x faster                                                |
| dulwich_log              | 75.9 ms                                                | 66.1 ms: 1.15x faster                                               |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.76 ms: 1.15x faster                                               |
| xml_etree_generate       | 94.2 ms                                                | 84.1 ms: 1.12x faster                                               |
| json                     | 5.42 ms                                                | 4.90 ms: 1.11x faster                                               |
| json_loads               | 28.8 us                                                | 26.1 us: 1.10x faster                                               |
| regex_v8                 | 25.0 ms                                                | 22.7 ms: 1.10x faster                                               |
| create_gc_cycles         | 1.67 ms                                                | 1.52 ms: 1.10x faster                                               |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.10x faster                                                |
| pathlib                  | 20.0 ms                                                | 18.4 ms: 1.09x faster                                               |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                               |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                                |
| regex_dna                | 222 ms                                                 | 208 ms: 1.06x faster                                                |
| mdp                      | 2.82 sec                                               | 2.70 sec: 1.04x faster                                              |
| pidigits                 | 190 ms                                                 | 189 ms: 1.01x faster                                                |
| pickle                   | 10.3 us                                                | 10.4 us: 1.01x slower                                               |
| unpickle_list            | 4.82 us                                                | 4.92 us: 1.02x slower                                               |
| pickle_list              | 4.56 us                                                | 4.71 us: 1.03x slower                                               |
| gc_traversal             | 3.84 ms                                                | 3.98 ms: 1.04x slower                                               |
| async_generators         | 425 ms                                                 | 455 ms: 1.07x slower                                                |
| unpickle                 | 14.1 us                                                | 15.2 us: 1.07x slower                                               |
| regex_effbot             | 3.23 ms                                                | 3.53 ms: 1.09x slower                                               |
| pickle_dict              | 27.3 us                                                | 31.8 us: 1.17x slower                                               |
| python_startup_no_site   | 5.82 ms                                                | 6.87 ms: 1.18x slower                                               |
| telco                    | 6.54 ms                                                | 7.88 ms: 1.20x slower                                               |
| dask                     | 423 ms                                                 | 519 ms: 1.23x slower                                                |
| coverage                 | 72.8 ms                                                | 93.4 ms: 1.28x slower                                               |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                        |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.22x

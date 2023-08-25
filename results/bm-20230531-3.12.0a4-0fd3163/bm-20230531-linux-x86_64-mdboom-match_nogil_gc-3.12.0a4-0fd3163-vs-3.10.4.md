
# Results vs. 3.10.4

- fork: mdboom
- ref: match_nogil_gc
- machine: linux-x86_64
- commit hash: 0fd3163
- commit date: 2023-05-31
- overall geometric mean: 1.37x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230531-linux-x86_64-mdboom-match_nogil_gc-3.12.0a4-0fd3163 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 245 ms: 1.37x faster                                            |
| chameleon      | 9.06 ms                                                | 6.37 ms: 1.42x faster                                           |
| docutils       | 3.17 sec                                               | 2.15 sec: 1.48x faster                                          |
| html5lib       | 85.9 ms                                                | 57.8 ms: 1.49x faster                                           |
| Geometric mean | (ref)                                                  | 1.44x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230531-linux-x86_64-mdboom-match_nogil_gc-3.12.0a4-0fd3163 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 111 ms                                                 | 60.7 ms: 1.82x faster                                           |
| nbody          | 142 ms                                                 | 92.3 ms: 1.53x faster                                           |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                            |
| Geometric mean | (ref)                                                  | 1.41x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230531-linux-x86_64-mdboom-match_nogil_gc-3.12.0a4-0fd3163 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 131 ms: 1.35x faster                                            |
| regex_v8       | 25.0 ms                                                | 22.1 ms: 1.13x faster                                           |
| regex_dna      | 222 ms                                                 | 210 ms: 1.05x faster                                            |
| regex_effbot   | 3.23 ms                                                | 3.46 ms: 1.07x slower                                           |
| Geometric mean | (ref)                                                  | 1.11x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230531-linux-x86_64-mdboom-match_nogil_gc-3.12.0a4-0fd3163 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 282 us: 1.61x faster                                            |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.52x faster                                            |
| tomli_loads          | 2.92 sec                                               | 1.98 sec: 1.47x faster                                          |
| xml_etree_process    | 74.9 ms                                                | 51.6 ms: 1.45x faster                                           |
| json_dumps           | 13.5 ms                                                | 9.55 ms: 1.42x faster                                           |
| xml_etree_iterparse  | 111 ms                                                 | 80.9 ms: 1.38x faster                                           |
| xml_etree_parse      | 163 ms                                                 | 122 ms: 1.34x faster                                            |
| xml_etree_generate   | 94.2 ms                                                | 73.4 ms: 1.28x faster                                           |
| json_loads           | 28.8 us                                                | 23.7 us: 1.22x faster                                           |
| pickle_list          | 4.56 us                                                | 4.05 us: 1.13x faster                                           |
| unpickle             | 14.1 us                                                | 13.0 us: 1.09x faster                                           |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                           |
| unpickle_list        | 4.82 us                                                | 4.95 us: 1.03x slower                                           |
| pickle_dict          | 27.3 us                                                | 31.2 us: 1.15x slower                                           |
| Geometric mean       | (ref)                                                  | 1.25x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230531-linux-x86_64-mdboom-match_nogil_gc-3.12.0a4-0fd3163 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.24 ms: 1.72x faster                                           |
| python_startup_no_site | 5.82 ms                                                | 5.93 ms: 1.02x slower                                           |
| Geometric mean         | (ref)                                                  | 1.30x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230531-linux-x86_64-mdboom-match_nogil_gc-3.12.0a4-0fd3163 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.69 ms: 1.52x faster                                           |
| genshi_text     | 30.3 ms                                                | 20.2 ms: 1.50x faster                                           |
| django_template | 45.9 ms                                                | 32.9 ms: 1.40x faster                                           |
| genshi_xml      | 63.3 ms                                                | 45.9 ms: 1.38x faster                                           |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230531-linux-x86_64-mdboom-match_nogil_gc-3.12.0a4-0fd3163 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io            | 1.77 sec                                               | 534 ms: 3.32x faster                                            |
| async_tree_none          | 717 ms                                                 | 260 ms: 2.75x faster                                            |
| async_tree_memoization   | 854 ms                                                 | 315 ms: 2.71x faster                                            |
| deltablue                | 7.42 ms                                                | 3.11 ms: 2.38x faster                                           |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 469 ms: 2.03x faster                                            |
| logging_silent           | 175 ns                                                 | 89.6 ns: 1.95x faster                                           |
| scimark_sor              | 197 ms                                                 | 106 ms: 1.85x faster                                            |
| float                    | 111 ms                                                 | 60.7 ms: 1.82x faster                                           |
| asyncio_tcp              | 925 ms                                                 | 511 ms: 1.81x faster                                            |
| richards                 | 74.9 ms                                                | 42.5 ms: 1.76x faster                                           |
| python_startup           | 14.2 ms                                                | 8.24 ms: 1.72x faster                                           |
| richards_super           | 90.7 ms                                                | 52.9 ms: 1.72x faster                                           |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                          |
| go                       | 229 ms                                                 | 137 ms: 1.67x faster                                            |
| pyflate                  | 673 ms                                                 | 403 ms: 1.67x faster                                            |
| scimark_monte_carlo      | 108 ms                                                 | 65.2 ms: 1.66x faster                                           |
| raytrace                 | 464 ms                                                 | 286 ms: 1.62x faster                                            |
| pickle_pure_python       | 455 us                                                 | 282 us: 1.61x faster                                            |
| crypto_pyaes             | 118 ms                                                 | 73.7 ms: 1.61x faster                                           |
| spectral_norm            | 150 ms                                                 | 94.7 ms: 1.58x faster                                           |
| hexiom                   | 9.53 ms                                                | 6.06 ms: 1.57x faster                                           |
| scimark_lu               | 163 ms                                                 | 105 ms: 1.55x faster                                            |
| deepcopy_memo            | 52.3 us                                                | 33.8 us: 1.55x faster                                           |
| chaos                    | 106 ms                                                 | 68.8 ms: 1.54x faster                                           |
| nbody                    | 142 ms                                                 | 92.3 ms: 1.53x faster                                           |
| mako                     | 14.8 ms                                                | 9.69 ms: 1.52x faster                                           |
| unpickle_pure_python     | 300 us                                                 | 198 us: 1.52x faster                                            |
| genshi_text              | 30.3 ms                                                | 20.2 ms: 1.50x faster                                           |
| sqlglot_parse            | 2.06 ms                                                | 1.38 ms: 1.49x faster                                           |
| html5lib                 | 85.9 ms                                                | 57.8 ms: 1.49x faster                                           |
| unpack_sequence          | 64.7 ns                                                | 43.6 ns: 1.48x faster                                           |
| docutils                 | 3.17 sec                                               | 2.15 sec: 1.48x faster                                          |
| tomli_loads              | 2.92 sec                                               | 1.98 sec: 1.47x faster                                          |
| sqlglot_transpile        | 2.45 ms                                                | 1.67 ms: 1.47x faster                                           |
| xml_etree_process        | 74.9 ms                                                | 51.6 ms: 1.45x faster                                           |
| pprint_pformat           | 1.99 sec                                               | 1.39 sec: 1.42x faster                                          |
| chameleon                | 9.06 ms                                                | 6.37 ms: 1.42x faster                                           |
| pycparser                | 1.50 sec                                               | 1.06 sec: 1.42x faster                                          |
| json_dumps               | 13.5 ms                                                | 9.55 ms: 1.42x faster                                           |
| pprint_safe_repr         | 955 ms                                                 | 676 ms: 1.41x faster                                            |
| django_template          | 45.9 ms                                                | 32.9 ms: 1.40x faster                                           |
| logging_simple           | 8.07 us                                                | 5.80 us: 1.39x faster                                           |
| mypy2                    | 428 ms                                                 | 309 ms: 1.38x faster                                            |
| logging_format           | 8.91 us                                                | 6.44 us: 1.38x faster                                           |
| xml_etree_iterparse      | 111 ms                                                 | 80.9 ms: 1.38x faster                                           |
| genshi_xml               | 63.3 ms                                                | 45.9 ms: 1.38x faster                                           |
| 2to3                     | 336 ms                                                 | 245 ms: 1.37x faster                                            |
| scimark_fft              | 424 ms                                                 | 309 ms: 1.37x faster                                            |
| regex_compile            | 177 ms                                                 | 131 ms: 1.35x faster                                            |
| xml_etree_parse          | 163 ms                                                 | 122 ms: 1.34x faster                                            |
| thrift                   | 1.03 ms                                                | 772 us: 1.34x faster                                            |
| dask                     | 423 ms                                                 | 317 ms: 1.33x faster                                            |
| deepcopy                 | 442 us                                                 | 332 us: 1.33x faster                                            |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.12 ms: 1.32x faster                                           |
| fannkuch                 | 486 ms                                                 | 368 ms: 1.32x faster                                            |
| nqueens                  | 100 ms                                                 | 77.6 ms: 1.29x faster                                           |
| deepcopy_reduce          | 3.82 us                                                | 2.97 us: 1.29x faster                                           |
| xml_etree_generate       | 94.2 ms                                                | 73.4 ms: 1.28x faster                                           |
| sqlglot_optimize         | 65.3 ms                                                | 51.6 ms: 1.27x faster                                           |
| async_generators         | 425 ms                                                 | 338 ms: 1.26x faster                                            |
| sqlglot_normalize        | 135 ms                                                 | 108 ms: 1.25x faster                                            |
| coroutines               | 31.8 ms                                                | 26.1 ms: 1.22x faster                                           |
| json_loads               | 28.8 us                                                | 23.7 us: 1.22x faster                                           |
| sympy_integrate          | 24.3 ms                                                | 20.2 ms: 1.20x faster                                           |
| sympy_expand             | 545 ms                                                 | 455 ms: 1.20x faster                                            |
| dulwich_log              | 75.9 ms                                                | 63.5 ms: 1.20x faster                                           |
| bench_thread_pool        | 947 us                                                 | 792 us: 1.20x faster                                            |
| json                     | 5.42 ms                                                | 4.59 ms: 1.18x faster                                           |
| sympy_str                | 328 ms                                                 | 281 ms: 1.17x faster                                            |
| create_gc_cycles         | 1.67 ms                                                | 1.46 ms: 1.14x faster                                           |
| mdp                      | 2.82 sec                                               | 2.48 sec: 1.14x faster                                          |
| gc_traversal             | 3.84 ms                                                | 3.38 ms: 1.14x faster                                           |
| sympy_sum                | 185 ms                                                 | 163 ms: 1.14x faster                                            |
| regex_v8                 | 25.0 ms                                                | 22.1 ms: 1.13x faster                                           |
| pickle_list              | 4.56 us                                                | 4.05 us: 1.13x faster                                           |
| comprehensions           | 26.8 us                                                | 23.9 us: 1.12x faster                                           |
| pathlib                  | 20.0 ms                                                | 18.2 ms: 1.10x faster                                           |
| typing_runtime_protocols | 510 us                                                 | 463 us: 1.10x faster                                            |
| sqlite_synth             | 2.93 us                                                | 2.67 us: 1.10x faster                                           |
| unpickle                 | 14.1 us                                                | 13.0 us: 1.09x faster                                           |
| djangocms                | 35.9 us                                                | 33.1 us: 1.09x faster                                           |
| regex_dna                | 222 ms                                                 | 210 ms: 1.05x faster                                            |
| meteor_contest           | 115 ms                                                 | 109 ms: 1.05x faster                                            |
| pickle                   | 10.3 us                                                | 10.2 us: 1.01x faster                                           |
| pidigits                 | 190 ms                                                 | 189 ms: 1.00x faster                                            |
| python_startup_no_site   | 5.82 ms                                                | 5.93 ms: 1.02x slower                                           |
| unpickle_list            | 4.82 us                                                | 4.95 us: 1.03x slower                                           |
| generators               | 76.8 ms                                                | 79.1 ms: 1.03x slower                                           |
| regex_effbot             | 3.23 ms                                                | 3.46 ms: 1.07x slower                                           |
| pickle_dict              | 27.3 us                                                | 31.2 us: 1.15x slower                                           |
| coverage                 | 72.8 ms                                                | 99.2 ms: 1.36x slower                                           |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                    |

Benchmark hidden because not significant (2): telco, bench_mp_pool
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

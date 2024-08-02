# Results vs. 3.10.4

- fork: gvanrossum
- ref: backoff_counter_woes
- machine: linux-aarch64
- commit hash: 4c1049b
- commit date: 2024-05-04
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 303 ms: 1.26x faster                                                         |
| chameleon      | 10.8 ms                                                               | 9.33 ms: 1.16x faster                                                        |
| docutils       | 3.53 sec                                                              | 3.11 sec: 1.14x faster                                                       |
| html5lib       | 86.5 ms                                                               | 65.9 ms: 1.31x faster                                                        |
| tornado_http   | 178 ms                                                                | 129 ms: 1.39x faster                                                         |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 489 ms: 1.94x faster                                                         |
| async_tree_io           | 2.28 sec                                                              | 1.22 sec: 1.88x faster                                                       |
| async_tree_memoization  | 1.13 sec                                                              | 644 ms: 1.76x faster                                                         |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 787 ms: 1.62x faster                                                         |
| Geometric mean          | (ref)                                                                 | 1.79x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 111 ms: 1.50x faster                                                         |
| float          | 135 ms                                                                | 91.5 ms: 1.47x faster                                                        |
| pidigits       | 235 ms                                                                | 234 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 129 ms: 1.37x faster                                                         |
| regex_dna      | 257 ms                                                                | 246 ms: 1.05x faster                                                         |
| regex_v8       | 32.2 ms                                                               | 31.1 ms: 1.03x faster                                                        |
| regex_effbot   | 4.25 ms                                                               | 4.85 ms: 1.14x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 355 us: 1.49x faster                                                         |
| unpickle_pure_python | 366 us                                                                | 254 us: 1.44x faster                                                         |
| tomli_loads          | 3.36 sec                                                              | 2.62 sec: 1.28x faster                                                       |
| json_dumps           | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                        |
| xml_etree_process    | 99.5 ms                                                               | 79.8 ms: 1.25x faster                                                        |
| xml_etree_parse      | 212 ms                                                                | 191 ms: 1.11x faster                                                         |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                         |
| unpickle_list        | 6.99 us                                                               | 6.67 us: 1.05x faster                                                        |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                         |
| pickle_list          | 5.24 us                                                               | 5.31 us: 1.01x slower                                                        |
| json_loads           | 30.9 us                                                               | 32.6 us: 1.05x slower                                                        |
| pickle_dict          | 35.1 us                                                               | 37.7 us: 1.07x slower                                                        |
| pickle               | 12.5 us                                                               | 13.5 us: 1.08x slower                                                        |
| unpickle             | 17.5 us                                                               | 19.8 us: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 12.5 ms: 1.12x slower                                                        |
| python_startup_no_site | 6.89 ms                                                               | 8.42 ms: 1.22x slower                                                        |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                        |
| django_template | 53.3 ms                                                               | 41.9 ms: 1.27x faster                                                        |
| genshi_text     | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                                        |
| genshi_xml      | 69.8 ms                                                               | 60.6 ms: 1.15x faster                                                        |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 202 us: 3.27x faster                                                         |
| deltablue                | 8.94 ms                                                               | 3.84 ms: 2.33x faster                                                        |
| bench_mp_pool            | 14.5 ms                                                               | 7.06 ms: 2.06x faster                                                        |
| raytrace                 | 573 ms                                                                | 295 ms: 1.95x faster                                                         |
| async_tree_none          | 950 ms                                                                | 489 ms: 1.94x faster                                                         |
| async_tree_io            | 2.28 sec                                                              | 1.22 sec: 1.88x faster                                                       |
| chaos                    | 121 ms                                                                | 66.2 ms: 1.83x faster                                                        |
| generators               | 68.1 ms                                                               | 38.4 ms: 1.77x faster                                                        |
| async_tree_memoization   | 1.13 sec                                                              | 644 ms: 1.76x faster                                                         |
| sqlglot_parse            | 2.40 ms                                                               | 1.39 ms: 1.72x faster                                                        |
| richards_super           | 107 ms                                                                | 62.2 ms: 1.72x faster                                                        |
| asyncio_tcp              | 944 ms                                                                | 562 ms: 1.68x faster                                                         |
| go                       | 264 ms                                                                | 159 ms: 1.66x faster                                                         |
| logging_silent           | 222 ns                                                                | 135 ns: 1.65x faster                                                         |
| richards                 | 91.7 ms                                                               | 55.7 ms: 1.65x faster                                                        |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.64x faster                                                        |
| comprehensions           | 33.1 us                                                               | 20.3 us: 1.63x faster                                                        |
| scimark_lu               | 227 ms                                                                | 139 ms: 1.63x faster                                                         |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 787 ms: 1.62x faster                                                         |
| crypto_pyaes             | 134 ms                                                                | 84.3 ms: 1.59x faster                                                        |
| scimark_monte_carlo      | 128 ms                                                                | 81.3 ms: 1.57x faster                                                        |
| scimark_sor              | 246 ms                                                                | 159 ms: 1.54x faster                                                         |
| hexiom                   | 10.9 ms                                                               | 7.12 ms: 1.53x faster                                                        |
| nbody                    | 166 ms                                                                | 111 ms: 1.50x faster                                                         |
| pickle_pure_python       | 529 us                                                                | 355 us: 1.49x faster                                                         |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.22 sec: 1.48x faster                                                       |
| float                    | 135 ms                                                                | 91.5 ms: 1.47x faster                                                        |
| unpickle_pure_python     | 366 us                                                                | 254 us: 1.44x faster                                                         |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                        |
| pyflate                  | 795 ms                                                                | 559 ms: 1.42x faster                                                         |
| pylint                   | 485 ms                                                                | 342 ms: 1.42x faster                                                         |
| tornado_http             | 178 ms                                                                | 129 ms: 1.39x faster                                                         |
| pycparser                | 1.69 sec                                                              | 1.22 sec: 1.38x faster                                                       |
| regex_compile            | 177 ms                                                                | 129 ms: 1.37x faster                                                         |
| spectral_norm            | 186 ms                                                                | 138 ms: 1.36x faster                                                         |
| logging_format           | 10.6 us                                                               | 7.93 us: 1.34x faster                                                        |
| logging_simple           | 9.78 us                                                               | 7.31 us: 1.34x faster                                                        |
| thrift                   | 1.26 ms                                                               | 945 us: 1.33x faster                                                         |
| html5lib                 | 86.5 ms                                                               | 65.9 ms: 1.31x faster                                                        |
| tomli_loads              | 3.36 sec                                                              | 2.62 sec: 1.28x faster                                                       |
| sympy_sum                | 184 ms                                                                | 144 ms: 1.28x faster                                                         |
| django_template          | 53.3 ms                                                               | 41.9 ms: 1.27x faster                                                        |
| genshi_text              | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                                        |
| json_dumps               | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                        |
| bench_thread_pool        | 1.59 ms                                                               | 1.26 ms: 1.26x faster                                                        |
| sympy_integrate          | 26.5 ms                                                               | 21.1 ms: 1.26x faster                                                        |
| 2to3                     | 381 ms                                                                | 303 ms: 1.26x faster                                                         |
| xml_etree_process        | 99.5 ms                                                               | 79.8 ms: 1.25x faster                                                        |
| coroutines               | 37.2 ms                                                               | 29.8 ms: 1.25x faster                                                        |
| dulwich_log              | 73.5 ms                                                               | 59.2 ms: 1.24x faster                                                        |
| deepcopy_memo            | 61.7 us                                                               | 50.1 us: 1.23x faster                                                        |
| pprint_pformat           | 2.36 sec                                                              | 1.92 sec: 1.23x faster                                                       |
| pprint_safe_repr         | 1.15 sec                                                              | 939 ms: 1.22x faster                                                         |
| sympy_str                | 329 ms                                                                | 269 ms: 1.22x faster                                                         |
| sqlglot_normalize        | 156 ms                                                                | 128 ms: 1.22x faster                                                         |
| sqlglot_optimize         | 75.4 ms                                                               | 62.2 ms: 1.21x faster                                                        |
| dask                     | 450 ms                                                                | 373 ms: 1.20x faster                                                         |
| sympy_expand             | 543 ms                                                                | 457 ms: 1.19x faster                                                         |
| nqueens                  | 117 ms                                                                | 99.2 ms: 1.18x faster                                                        |
| gunicorn                 | 1.45 ms                                                               | 1.22 ms: 1.18x faster                                                        |
| fannkuch                 | 546 ms                                                                | 464 ms: 1.18x faster                                                         |
| aiohttp                  | 1.39 ms                                                               | 1.18 ms: 1.17x faster                                                        |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.52 ms: 1.17x faster                                                        |
| chameleon                | 10.8 ms                                                               | 9.33 ms: 1.16x faster                                                        |
| genshi_xml               | 69.8 ms                                                               | 60.6 ms: 1.15x faster                                                        |
| deepcopy                 | 511 us                                                                | 449 us: 1.14x faster                                                         |
| docutils                 | 3.53 sec                                                              | 3.11 sec: 1.14x faster                                                       |
| pathlib                  | 26.3 ms                                                               | 23.3 ms: 1.13x faster                                                        |
| scimark_fft              | 500 ms                                                                | 443 ms: 1.13x faster                                                         |
| deepcopy_reduce          | 4.60 us                                                               | 4.08 us: 1.13x faster                                                        |
| mdp                      | 3.70 sec                                                              | 3.31 sec: 1.12x faster                                                       |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.11x faster                                                         |
| xml_etree_parse          | 212 ms                                                                | 191 ms: 1.11x faster                                                         |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                         |
| sqlite_synth             | 4.12 us                                                               | 3.91 us: 1.05x faster                                                        |
| unpickle_list            | 6.99 us                                                               | 6.67 us: 1.05x faster                                                        |
| regex_dna                | 257 ms                                                                | 246 ms: 1.05x faster                                                         |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                         |
| regex_v8                 | 32.2 ms                                                               | 31.1 ms: 1.03x faster                                                        |
| json                     | 5.88 ms                                                               | 5.83 ms: 1.01x faster                                                        |
| pidigits                 | 235 ms                                                                | 234 ms: 1.01x faster                                                         |
| asyncio_websockets       | 657 ms                                                                | 659 ms: 1.00x slower                                                         |
| pickle_list              | 5.24 us                                                               | 5.31 us: 1.01x slower                                                        |
| json_loads               | 30.9 us                                                               | 32.6 us: 1.05x slower                                                        |
| async_generators         | 452 ms                                                                | 484 ms: 1.07x slower                                                         |
| pickle_dict              | 35.1 us                                                               | 37.7 us: 1.07x slower                                                        |
| create_gc_cycles         | 2.26 ms                                                               | 2.45 ms: 1.08x slower                                                        |
| pickle                   | 12.5 us                                                               | 13.5 us: 1.08x slower                                                        |
| python_startup           | 11.2 ms                                                               | 12.5 ms: 1.12x slower                                                        |
| unpickle                 | 17.5 us                                                               | 19.8 us: 1.13x slower                                                        |
| regex_effbot             | 4.25 ms                                                               | 4.85 ms: 1.14x slower                                                        |
| telco                    | 8.49 ms                                                               | 9.78 ms: 1.15x slower                                                        |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.21x slower                                                         |
| python_startup_no_site   | 6.89 ms                                                               | 8.42 ms: 1.22x slower                                                        |
| gc_traversal             | 4.15 ms                                                               | 5.09 ms: 1.23x slower                                                        |
| Geometric mean           | (ref)                                                                 | 1.28x faster                                                                 |

Benchmark hidden because not significant (1): flaskblogging
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240504-3.13.0a6+-4c1049b/bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.13x
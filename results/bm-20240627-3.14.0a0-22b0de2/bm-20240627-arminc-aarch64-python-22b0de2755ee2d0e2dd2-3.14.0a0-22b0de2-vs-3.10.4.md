# Results vs. 3.10.4

- fork: python
- ref: 22b0de2755ee2d0e2dd2
- machine: linux-aarch64
- commit hash: 22b0de2
- commit date: 2024-06-27
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 308 ms: 1.24x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.13 sec: 1.13x faster                                                  |
| html5lib       | 86.5 ms                                                               | 67.3 ms: 1.28x faster                                                   |
| tornado_http   | 178 ms                                                                | 129 ms: 1.38x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.06 sec: 2.15x faster                                                  |
| async_tree_none         | 950 ms                                                                | 444 ms: 2.14x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 579 ms: 1.96x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 729 ms: 1.74x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.99x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 112 ms: 1.48x faster                                                    |
| float          | 135 ms                                                                | 91.6 ms: 1.47x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 129 ms: 1.37x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.93 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 358 us: 1.48x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 252 us: 1.45x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.56 sec: 1.31x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 80.5 ms: 1.24x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.7 ms: 1.22x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 189 ms: 1.12x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                    |
| json_loads           | 30.9 us                                                               | 33.3 us: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.74 ms: 1.27x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.21x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                   |
| django_template | 53.3 ms                                                               | 42.2 ms: 1.26x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 28.8 ms: 1.22x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 61.5 ms: 1.14x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.25x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 199 us: 3.32x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.85 ms: 2.32x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.06 sec: 2.15x faster                                                  |
| async_tree_none          | 950 ms                                                                | 444 ms: 2.14x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.01 ms: 2.07x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 579 ms: 1.96x faster                                                    |
| raytrace                 | 573 ms                                                                | 298 ms: 1.93x faster                                                    |
| generators               | 68.1 ms                                                               | 37.6 ms: 1.81x faster                                                   |
| richards_super           | 107 ms                                                                | 59.7 ms: 1.80x faster                                                   |
| chaos                    | 121 ms                                                                | 68.3 ms: 1.77x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 729 ms: 1.74x faster                                                    |
| richards                 | 91.7 ms                                                               | 54.2 ms: 1.69x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.42 ms: 1.69x faster                                                   |
| scimark_lu               | 227 ms                                                                | 138 ms: 1.65x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 81.5 ms: 1.64x faster                                                   |
| go                       | 264 ms                                                                | 161 ms: 1.64x faster                                                    |
| logging_silent           | 222 ns                                                                | 136 ns: 1.64x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 579 ms: 1.63x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.75 ms: 1.62x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 38.3 us: 1.61x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.6 us: 1.61x faster                                                   |
| scimark_sor              | 246 ms                                                                | 159 ms: 1.54x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 82.9 ms: 1.54x faster                                                   |
| deepcopy                 | 511 us                                                                | 333 us: 1.53x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.13 ms: 1.53x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.21 sec: 1.48x faster                                                  |
| nbody                    | 166 ms                                                                | 112 ms: 1.48x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 358 us: 1.48x faster                                                    |
| float                    | 135 ms                                                                | 91.6 ms: 1.47x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 252 us: 1.45x faster                                                    |
| pyflate                  | 795 ms                                                                | 561 ms: 1.42x faster                                                    |
| pylint                   | 485 ms                                                                | 343 ms: 1.42x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.07 us: 1.38x faster                                                   |
| tornado_http             | 178 ms                                                                | 129 ms: 1.38x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.38x faster                                                  |
| mako                     | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                   |
| regex_compile            | 177 ms                                                                | 129 ms: 1.37x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.77 us: 1.37x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.48 us: 1.32x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.56 sec: 1.31x faster                                                  |
| spectral_norm            | 186 ms                                                                | 142 ms: 1.31x faster                                                    |
| thrift                   | 1.26 ms                                                               | 961 us: 1.31x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 67.3 ms: 1.28x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.24 ms: 1.28x faster                                                   |
| sympy_sum                | 184 ms                                                                | 145 ms: 1.27x faster                                                    |
| django_template          | 53.3 ms                                                               | 42.2 ms: 1.26x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 21.1 ms: 1.26x faster                                                   |
| coroutines               | 37.2 ms                                                               | 29.6 ms: 1.26x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 59.4 ms: 1.24x faster                                                   |
| 2to3                     | 381 ms                                                                | 308 ms: 1.24x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 80.5 ms: 1.24x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 28.8 ms: 1.22x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.7 ms: 1.22x faster                                                   |
| sympy_str                | 329 ms                                                                | 270 ms: 1.22x faster                                                    |
| dask                     | 450 ms                                                                | 371 ms: 1.21x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.7 ms: 1.21x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 129 ms: 1.21x faster                                                    |
| fannkuch                 | 546 ms                                                                | 453 ms: 1.21x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 62.7 ms: 1.20x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 964 ms: 1.19x faster                                                    |
| nqueens                  | 117 ms                                                                | 98.7 ms: 1.19x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.99 sec: 1.18x faster                                                  |
| sympy_expand             | 543 ms                                                                | 464 ms: 1.17x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.59 ms: 1.16x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 61.5 ms: 1.14x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.13 sec: 1.13x faster                                                  |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.12x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 189 ms: 1.12x faster                                                    |
| scimark_fft              | 500 ms                                                                | 451 ms: 1.11x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.34 sec: 1.11x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                    |
| json                     | 5.88 ms                                                               | 5.80 ms: 1.01x faster                                                   |
| json_loads               | 30.9 us                                                               | 33.3 us: 1.08x slower                                                   |
| async_generators         | 452 ms                                                                | 489 ms: 1.08x slower                                                    |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.93 ms: 1.16x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.92 ms: 1.17x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 4.90 ms: 1.18x slower                                                   |
| coverage                 | 83.6 ms                                                               | 100 ms: 1.20x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.74 ms: 1.27x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.33x faster                                                            |

Benchmark hidden because not significant (4): regex_dna, pidigits, asyncio_websockets, create_gc_cycles
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240627-3.14.0a0-22b0de2/bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.13x
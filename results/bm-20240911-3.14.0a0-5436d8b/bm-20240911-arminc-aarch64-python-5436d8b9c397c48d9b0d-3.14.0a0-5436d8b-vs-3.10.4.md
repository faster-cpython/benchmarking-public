# Results vs. 3.10.4

- fork: python
- ref: 5436d8b9c397c48d9b0d
- machine: linux-aarch64
- commit hash: 5436d8b
- commit date: 2024-09-11
- overall geometric mean: 1.32x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 295 ms: 1.29x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.02 sec: 1.17x faster                                                  |
| html5lib       | 86.5 ms                                                               | 65.9 ms: 1.31x faster                                                   |
| tornado_http   | 178 ms                                                                | 127 ms: 1.40x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 425 ms: 2.23x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 560 ms: 2.02x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.17 sec: 1.96x faster                                                  |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 725 ms: 1.75x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.98x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 110 ms: 1.51x faster                                                    |
| float          | 135 ms                                                                | 91.8 ms: 1.47x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 126 ms: 1.40x faster                                                    |
| regex_dna      | 257 ms                                                                | 247 ms: 1.04x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 31.0 ms: 1.04x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 368 us: 1.44x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 254 us: 1.44x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 79.0 ms: 1.26x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 185 ms: 1.14x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.38 us: 1.10x faster                                                   |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 146 ms: 1.06x faster                                                    |
| json_loads           | 30.9 us                                                               | 31.7 us: 1.02x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 37.8 us: 1.08x slower                                                   |
| pickle               | 12.5 us                                                               | 13.7 us: 1.10x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.4 us: 1.11x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                            |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.58 ms: 1.25x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.20x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.3 ms: 1.43x faster                                                   |
| django_template | 53.3 ms                                                               | 41.4 ms: 1.29x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.3 ms: 1.29x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 60.9 ms: 1.15x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 192 us: 3.44x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.89 ms: 2.30x faster                                                   |
| async_tree_none          | 950 ms                                                                | 425 ms: 2.23x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.03 ms: 2.07x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 560 ms: 2.02x faster                                                    |
| generators               | 68.1 ms                                                               | 34.7 ms: 1.96x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.17 sec: 1.96x faster                                                  |
| go                       | 264 ms                                                                | 138 ms: 1.92x faster                                                    |
| raytrace                 | 573 ms                                                                | 302 ms: 1.90x faster                                                    |
| richards_super           | 107 ms                                                                | 59.6 ms: 1.80x faster                                                   |
| chaos                    | 121 ms                                                                | 68.7 ms: 1.76x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 725 ms: 1.75x faster                                                    |
| richards                 | 91.7 ms                                                               | 52.9 ms: 1.73x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 551 ms: 1.71x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.41 ms: 1.71x faster                                                   |
| logging_silent           | 222 ns                                                                | 132 ns: 1.68x faster                                                    |
| scimark_lu               | 227 ms                                                                | 136 ms: 1.67x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.65x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 37.6 us: 1.64x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 81.8 ms: 1.64x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.3 us: 1.64x faster                                                   |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.57x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 82.1 ms: 1.56x faster                                                   |
| deepcopy                 | 511 us                                                                | 331 us: 1.54x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.10 ms: 1.54x faster                                                   |
| nbody                    | 166 ms                                                                | 110 ms: 1.51x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.21 sec: 1.48x faster                                                  |
| float                    | 135 ms                                                                | 91.8 ms: 1.47x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 368 us: 1.44x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 254 us: 1.44x faster                                                    |
| pyflate                  | 795 ms                                                                | 557 ms: 1.43x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.3 ms: 1.43x faster                                                   |
| regex_compile            | 177 ms                                                                | 126 ms: 1.40x faster                                                    |
| tornado_http             | 178 ms                                                                | 127 ms: 1.40x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.21 sec: 1.40x faster                                                  |
| logging_simple           | 9.78 us                                                               | 7.06 us: 1.38x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.69 us: 1.38x faster                                                   |
| thrift                   | 1.26 ms                                                               | 924 us: 1.36x faster                                                    |
| pylint                   | 485 ms                                                                | 360 ms: 1.35x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 65.9 ms: 1.31x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.4 ms: 1.31x faster                                                   |
| spectral_norm            | 186 ms                                                                | 143 ms: 1.31x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.54 us: 1.30x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.23 ms: 1.30x faster                                                   |
| sympy_sum                | 184 ms                                                                | 142 ms: 1.29x faster                                                    |
| 2to3                     | 381 ms                                                                | 295 ms: 1.29x faster                                                    |
| django_template          | 53.3 ms                                                               | 41.4 ms: 1.29x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 20.6 ms: 1.29x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.3 ms: 1.29x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                  |
| dulwich_log              | 73.5 ms                                                               | 57.7 ms: 1.27x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 911 ms: 1.26x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 79.0 ms: 1.26x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 20.9 ms: 1.26x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.88 sec: 1.26x faster                                                  |
| sympy_str                | 329 ms                                                                | 264 ms: 1.25x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 127 ms: 1.23x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 62.5 ms: 1.21x faster                                                   |
| fannkuch                 | 546 ms                                                                | 459 ms: 1.19x faster                                                    |
| sympy_expand             | 543 ms                                                                | 462 ms: 1.18x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.49 ms: 1.18x faster                                                   |
| nqueens                  | 117 ms                                                                | 100 ms: 1.17x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.02 sec: 1.17x faster                                                  |
| genshi_xml               | 69.8 ms                                                               | 60.9 ms: 1.15x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 185 ms: 1.14x faster                                                    |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.12x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.34 sec: 1.11x faster                                                  |
| unpickle_list            | 6.99 us                                                               | 6.38 us: 1.10x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 146 ms: 1.06x faster                                                    |
| scimark_fft              | 500 ms                                                                | 471 ms: 1.06x faster                                                    |
| json                     | 5.88 ms                                                               | 5.56 ms: 1.06x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.93 us: 1.05x faster                                                   |
| regex_dna                | 257 ms                                                                | 247 ms: 1.04x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 31.0 ms: 1.04x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 663 ms: 1.01x slower                                                    |
| json_loads               | 30.9 us                                                               | 31.7 us: 1.02x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 37.8 us: 1.08x slower                                                   |
| async_generators         | 452 ms                                                                | 489 ms: 1.08x slower                                                    |
| pickle                   | 12.5 us                                                               | 13.7 us: 1.10x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.4 us: 1.11x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| coverage                 | 83.6 ms                                                               | 97.7 ms: 1.17x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.2 ms: 1.20x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.12 ms: 1.23x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.58 ms: 1.25x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.32x faster                                                            |

Benchmark hidden because not significant (3): pickle_list, pidigits, create_gc_cycles
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240911-3.14.0a0-5436d8b/bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.13x
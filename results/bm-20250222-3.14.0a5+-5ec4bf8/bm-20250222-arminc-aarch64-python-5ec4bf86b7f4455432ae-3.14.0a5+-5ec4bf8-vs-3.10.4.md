# Results vs. 3.10.4

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-aarch64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.312x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 314 ms: 1.21x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.05 sec: 1.16x faster                                                   |
| html5lib       | 86.5 ms                                                               | 64.6 ms: 1.34x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 929 ms: 2.46x faster                                                     |
| async_tree_none         | 950 ms                                                                | 388 ms: 2.45x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 488 ms: 2.32x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 681 ms: 1.87x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.26x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 87.4 ms: 1.54x faster                                                    |
| nbody          | 166 ms                                                                | 123 ms: 1.35x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 129 ms: 1.37x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 31.6 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                             |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 397 us: 1.33x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 276 us: 1.33x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.56 sec: 1.31x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 82.6 ms: 1.21x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 182 ms: 1.16x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.06x faster                                                     |
| pickle_list          | 5.24 us                                                               | 5.73 us: 1.09x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 39.7 us: 1.13x slower                                                    |
| json_loads           | 30.9 us                                                               | 35.9 us: 1.16x slower                                                    |
| pickle               | 12.5 us                                                               | 15.5 us: 1.24x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (3): xml_etree_generate, unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.05 ms: 1.31x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.4 ms: 1.47x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.39x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                                    |
| mako            | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 64.9 ms: 1.08x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.26x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 209 us: 3.16x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 929 ms: 2.46x faster                                                     |
| async_tree_none          | 950 ms                                                                | 388 ms: 2.45x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 488 ms: 2.32x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.03 ms: 2.22x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 681 ms: 1.87x faster                                                     |
| go                       | 264 ms                                                                | 142 ms: 1.86x faster                                                     |
| richards_super           | 107 ms                                                                | 59.1 ms: 1.81x faster                                                    |
| generators               | 68.1 ms                                                               | 37.6 ms: 1.81x faster                                                    |
| raytrace                 | 573 ms                                                                | 326 ms: 1.76x faster                                                     |
| chaos                    | 121 ms                                                                | 69.7 ms: 1.74x faster                                                    |
| richards                 | 91.7 ms                                                               | 53.3 ms: 1.72x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 558 ms: 1.69x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.44 ms: 1.67x faster                                                    |
| logging_silent           | 222 ns                                                                | 135 ns: 1.65x faster                                                     |
| scimark_lu               | 227 ms                                                                | 141 ms: 1.60x faster                                                     |
| pylint                   | 485 ms                                                                | 304 ms: 1.60x faster                                                     |
| scimark_sor              | 246 ms                                                                | 155 ms: 1.59x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 1.79 ms: 1.59x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 86.7 ms: 1.55x faster                                                    |
| comprehensions           | 33.1 us                                                               | 21.5 us: 1.54x faster                                                    |
| float                    | 135 ms                                                                | 87.4 ms: 1.54x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 40.6 us: 1.52x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 85.9 ms: 1.49x faster                                                    |
| spectral_norm            | 186 ms                                                                | 126 ms: 1.48x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 7.49 ms: 1.46x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.25 sec: 1.46x faster                                                   |
| deepcopy                 | 511 us                                                                | 361 us: 1.41x faster                                                     |
| pyflate                  | 795 ms                                                                | 564 ms: 1.41x faster                                                     |
| regex_compile            | 177 ms                                                                | 129 ms: 1.37x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 145 ms: 1.36x faster                                                     |
| django_template          | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.2 ms: 1.35x faster                                                    |
| nbody                    | 166 ms                                                                | 123 ms: 1.35x faster                                                     |
| mako                     | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 64.6 ms: 1.34x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 397 us: 1.33x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 276 us: 1.33x faster                                                     |
| logging_format           | 10.6 us                                                               | 8.03 us: 1.32x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.56 sec: 1.31x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.47 us: 1.31x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.30 sec: 1.31x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.5 ms: 1.30x faster                                                    |
| thrift                   | 1.26 ms                                                               | 978 us: 1.29x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                    |
| sympy_sum                | 184 ms                                                                | 148 ms: 1.25x faster                                                     |
| sqlglot_normalize        | 156 ms                                                                | 128 ms: 1.22x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 60.3 ms: 1.22x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 21.9 ms: 1.21x faster                                                    |
| 2to3                     | 381 ms                                                                | 314 ms: 1.21x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.32 ms: 1.21x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 82.6 ms: 1.21x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.32 ms: 1.20x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.83 us: 1.20x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 978 ms: 1.17x faster                                                     |
| sympy_str                | 329 ms                                                                | 281 ms: 1.17x faster                                                     |
| scimark_fft              | 500 ms                                                                | 429 ms: 1.17x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 2.03 sec: 1.16x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 182 ms: 1.16x faster                                                     |
| docutils                 | 3.53 sec                                                              | 3.05 sec: 1.16x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 23.0 ms: 1.15x faster                                                    |
| sympy_expand             | 543 ms                                                                | 474 ms: 1.14x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 66.2 ms: 1.14x faster                                                    |
| nqueens                  | 117 ms                                                                | 104 ms: 1.13x faster                                                     |
| fannkuch                 | 546 ms                                                                | 494 ms: 1.11x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 64.9 ms: 1.08x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.44 sec: 1.08x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.06x faster                                                     |
| meteor_contest           | 126 ms                                                                | 120 ms: 1.06x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 31.6 ms: 1.02x faster                                                    |
| json                     | 5.88 ms                                                               | 6.06 ms: 1.03x slower                                                    |
| pickle_list              | 5.24 us                                                               | 5.73 us: 1.09x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 39.7 us: 1.13x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.81 ms: 1.16x slower                                                    |
| json_loads               | 30.9 us                                                               | 35.9 us: 1.16x slower                                                    |
| coverage                 | 83.6 ms                                                               | 98.7 ms: 1.18x slower                                                    |
| pickle                   | 12.5 us                                                               | 15.5 us: 1.24x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 9.05 ms: 1.31x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.4 ms: 1.47x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.72 ms: 1.65x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 7.33 ms: 1.76x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.33 sec: 504.18x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.18x faster                                                             |

Benchmark hidden because not significant (9): xml_etree_generate, regex_effbot, unpickle_list, pidigits, async_generators, sqlite_synth, regex_dna, asyncio_websockets, unpickle
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.312x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.31x
# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_attributes_to_gu
- machine: linux-x86_64
- commit hash: bb3ea59
- commit date: 2024-08-23
- overall geometric mean: 1.44x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                                            |
| docutils       | 3.30 sec                                               | 2.71 sec: 1.21x faster                                                          |
| html5lib       | 88.9 ms                                                | 66.2 ms: 1.34x faster                                                           |
| tornado_http   | 136 ms                                                 | 89.6 ms: 1.52x faster                                                           |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 324 ms: 2.25x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 391 ms: 2.22x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 932 ms: 1.90x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 555 ms: 1.83x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.04x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.5 ms: 1.77x faster                                                           |
| float          | 117 ms                                                 | 78.4 ms: 1.49x faster                                                           |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.40x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                            |
| regex_v8       | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                           |
| regex_dna      | 227 ms                                                 | 223 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 299 us: 1.62x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.10 sec: 1.50x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.36x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 84.9 ms: 1.17x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                                            |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                           |
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                           |
| django_template | 48.2 ms                                                | 33.5 ms: 1.44x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 49.2 ms: 1.34x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.42x faster                                                            |
| generators               | 80.1 ms                                                | 27.8 ms: 2.88x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                                           |
| async_tree_none          | 728 ms                                                 | 324 ms: 2.25x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 391 ms: 2.22x faster                                                            |
| go                       | 240 ms                                                 | 118 ms: 2.04x faster                                                            |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                                           |
| deepcopy_memo            | 58.5 us                                                | 29.8 us: 1.96x faster                                                           |
| raytrace                 | 507 ms                                                 | 261 ms: 1.94x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 477 ms: 1.93x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 932 ms: 1.90x faster                                                            |
| logging_silent           | 190 ns                                                 | 102 ns: 1.87x faster                                                            |
| richards_super           | 94.7 ms                                                | 51.3 ms: 1.85x faster                                                           |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 555 ms: 1.83x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 70.7 ms: 1.81x faster                                                           |
| nbody                    | 154 ms                                                 | 86.5 ms: 1.77x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 67.5 ms: 1.75x faster                                                           |
| richards                 | 79.3 ms                                                | 45.4 ms: 1.75x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                           |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                                            |
| pylint                   | 551 ms                                                 | 320 ms: 1.73x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.13 ms: 1.70x faster                                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.69x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 299 us: 1.62x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                           |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.55x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                            |
| spectral_norm            | 170 ms                                                 | 111 ms: 1.53x faster                                                            |
| tornado_http             | 136 ms                                                 | 89.6 ms: 1.52x faster                                                           |
| pyflate                  | 716 ms                                                 | 471 ms: 1.52x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.52 us: 1.50x faster                                                           |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.10 sec: 1.50x faster                                                          |
| float                    | 117 ms                                                 | 78.4 ms: 1.49x faster                                                           |
| logging_format           | 9.09 us                                                | 6.10 us: 1.49x faster                                                           |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                            |
| genshi_text              | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                           |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                          |
| django_template          | 48.2 ms                                                | 33.5 ms: 1.44x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 726 ms: 1.40x faster                                                            |
| thrift                   | 1.07 ms                                                | 765 us: 1.40x faster                                                            |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                           |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                                            |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.36x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.82 ms: 1.34x faster                                                           |
| html5lib                 | 88.9 ms                                                | 66.2 ms: 1.34x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 49.2 ms: 1.34x faster                                                           |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                            |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                          |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.33x faster                                                            |
| fannkuch                 | 532 ms                                                 | 402 ms: 1.32x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                                           |
| nqueens                  | 106 ms                                                 | 80.4 ms: 1.32x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 53.4 ms: 1.29x faster                                                           |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                                            |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                           |
| scimark_fft              | 466 ms                                                 | 361 ms: 1.29x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 785 us: 1.26x faster                                                            |
| sympy_expand             | 566 ms                                                 | 453 ms: 1.25x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.71 sec: 1.21x faster                                                          |
| xml_etree_generate       | 99.4 ms                                                | 84.9 ms: 1.17x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                                          |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                                            |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                                            |
| json                     | 5.69 ms                                                | 5.30 ms: 1.07x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                           |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                            |
| async_generators         | 444 ms                                                 | 437 ms: 1.02x faster                                                            |
| regex_dna                | 227 ms                                                 | 223 ms: 1.01x faster                                                            |
| gc_traversal             | 3.62 ms                                                | 3.72 ms: 1.03x slower                                                           |
| coverage                 | 79.4 ms                                                | 85.8 ms: 1.08x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.77 ms: 1.09x slower                                                           |
| telco                    | 7.27 ms                                                | 8.27 ms: 1.14x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                                    |

Benchmark hidden because not significant (3): asyncio_websockets, bench_mp_pool, regex_effbot
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240823-3.14.0a0-bb3ea59/bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.12x
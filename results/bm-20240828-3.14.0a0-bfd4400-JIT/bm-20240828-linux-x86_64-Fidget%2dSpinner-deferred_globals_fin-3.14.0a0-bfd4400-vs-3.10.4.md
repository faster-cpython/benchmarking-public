# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-x86_64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 281 ms: 1.24x faster                                                            |
| docutils       | 3.30 sec                                               | 3.00 sec: 1.10x faster                                                          |
| html5lib       | 88.9 ms                                                | 65.9 ms: 1.35x faster                                                           |
| tornado_http   | 136 ms                                                 | 93.0 ms: 1.47x faster                                                           |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 328 ms: 2.22x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 429 ms: 2.03x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 904 ms: 1.96x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 566 ms: 1.80x faster                                                            |
| Geometric mean          | (ref)                                                  | 1.99x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.0 ms: 1.92x faster                                                           |
| float          | 117 ms                                                 | 70.5 ms: 1.66x faster                                                           |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.49x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 141 ms: 1.34x faster                                                            |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                           |
| regex_dna      | 227 ms                                                 | 217 ms: 1.05x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.50 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                          |
| pickle_pure_python   | 484 us                                                 | 303 us: 1.60x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 209 us: 1.58x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 57.7 ms: 1.37x faster                                                           |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 81.9 ms: 1.21x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 98.8 ms: 1.17x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.13x faster                                                            |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.15 ms: 1.20x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.85 ms: 1.66x faster                                                           |
| django_template | 48.2 ms                                                | 35.7 ms: 1.35x faster                                                           |
| genshi_text     | 31.8 ms                                                | 26.0 ms: 1.23x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 59.7 ms: 1.11x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 174 us: 3.12x faster                                                            |
| deltablue                | 7.91 ms                                                | 3.12 ms: 2.54x faster                                                           |
| generators               | 80.1 ms                                                | 32.8 ms: 2.44x faster                                                           |
| async_tree_none          | 728 ms                                                 | 328 ms: 2.22x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 26.5 us: 2.21x faster                                                           |
| richards_super           | 94.7 ms                                                | 44.3 ms: 2.14x faster                                                           |
| richards                 | 79.3 ms                                                | 39.0 ms: 2.03x faster                                                           |
| async_tree_memoization   | 870 ms                                                 | 429 ms: 2.03x faster                                                            |
| chaos                    | 115 ms                                                 | 58.3 ms: 1.98x faster                                                           |
| async_tree_io            | 1.77 sec                                               | 904 ms: 1.96x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 65.5 ms: 1.95x faster                                                           |
| scimark_sor              | 220 ms                                                 | 114 ms: 1.93x faster                                                            |
| raytrace                 | 507 ms                                                 | 263 ms: 1.93x faster                                                            |
| logging_silent           | 190 ns                                                 | 98.7 ns: 1.92x faster                                                           |
| nbody                    | 154 ms                                                 | 80.0 ms: 1.92x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 62.4 ms: 1.89x faster                                                           |
| asyncio_tcp              | 922 ms                                                 | 499 ms: 1.85x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 566 ms: 1.80x faster                                                            |
| deepcopy                 | 479 us                                                 | 268 us: 1.79x faster                                                            |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                           |
| spectral_norm            | 170 ms                                                 | 98.6 ms: 1.72x faster                                                           |
| float                    | 117 ms                                                 | 70.5 ms: 1.66x faster                                                           |
| mako                     | 16.3 ms                                                | 9.85 ms: 1.66x faster                                                           |
| go                       | 240 ms                                                 | 145 ms: 1.65x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                          |
| pickle_pure_python       | 484 us                                                 | 303 us: 1.60x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 209 us: 1.58x faster                                                            |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.58x faster                                                            |
| pyflate                  | 716 ms                                                 | 456 ms: 1.57x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.76 ms: 1.54x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.68 ms: 1.54x faster                                                           |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                           |
| scimark_fft              | 466 ms                                                 | 306 ms: 1.52x faster                                                            |
| logging_format           | 9.09 us                                                | 6.02 us: 1.51x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.77 us: 1.51x faster                                                           |
| logging_simple           | 8.30 us                                                | 5.51 us: 1.51x faster                                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.30 ms: 1.51x faster                                                           |
| pylint                   | 551 ms                                                 | 368 ms: 1.50x faster                                                            |
| tornado_http             | 136 ms                                                 | 93.0 ms: 1.47x faster                                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                          |
| fannkuch                 | 532 ms                                                 | 377 ms: 1.41x faster                                                            |
| pprint_safe_repr         | 1.02 sec                                               | 736 ms: 1.38x faster                                                            |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                          |
| xml_etree_process        | 79.1 ms                                                | 57.7 ms: 1.37x faster                                                           |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.36x faster                                                          |
| django_template          | 48.2 ms                                                | 35.7 ms: 1.35x faster                                                           |
| thrift                   | 1.07 ms                                                | 794 us: 1.35x faster                                                            |
| html5lib                 | 88.9 ms                                                | 65.9 ms: 1.35x faster                                                           |
| regex_compile            | 188 ms                                                 | 141 ms: 1.34x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.27x faster                                                            |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                           |
| 2to3                     | 348 ms                                                 | 281 ms: 1.24x faster                                                            |
| genshi_text              | 31.8 ms                                                | 26.0 ms: 1.23x faster                                                           |
| nqueens                  | 106 ms                                                 | 86.6 ms: 1.22x faster                                                           |
| xml_etree_generate       | 99.4 ms                                                | 81.9 ms: 1.21x faster                                                           |
| bench_thread_pool        | 986 us                                                 | 816 us: 1.21x faster                                                            |
| sqlglot_optimize         | 69.2 ms                                                | 57.9 ms: 1.19x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 98.8 ms: 1.17x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                           |
| sympy_str                | 346 ms                                                 | 305 ms: 1.13x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.13x faster                                                            |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 23.0 ms: 1.12x faster                                                           |
| sympy_sum                | 196 ms                                                 | 176 ms: 1.11x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 59.7 ms: 1.11x faster                                                           |
| sympy_expand             | 566 ms                                                 | 513 ms: 1.10x faster                                                            |
| docutils                 | 3.30 sec                                               | 3.00 sec: 1.10x faster                                                          |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.66 sec: 1.07x faster                                                          |
| json                     | 5.69 ms                                                | 5.37 ms: 1.06x faster                                                           |
| regex_dna                | 227 ms                                                 | 217 ms: 1.05x faster                                                            |
| regex_effbot             | 3.63 ms                                                | 3.50 ms: 1.04x faster                                                           |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.00x faster                                                            |
| gc_traversal             | 3.62 ms                                                | 3.69 ms: 1.02x slower                                                           |
| async_generators         | 444 ms                                                 | 452 ms: 1.02x slower                                                            |
| coverage                 | 79.4 ms                                                | 84.9 ms: 1.07x slower                                                           |
| telco                    | 7.27 ms                                                | 7.77 ms: 1.07x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.08x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.15 ms: 1.20x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                    |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240828-3.14.0a0-bfd4400-JIT/bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.21x
# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-x86_64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.33x faster                                                            |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                          |
| html5lib       | 88.9 ms                                                | 64.8 ms: 1.37x faster                                                           |
| tornado_http   | 136 ms                                                 | 90.2 ms: 1.51x faster                                                           |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 325 ms: 2.24x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 406 ms: 2.14x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 907 ms: 1.95x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 560 ms: 1.82x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 87.3 ms: 1.76x faster                                                           |
| float          | 117 ms                                                 | 77.9 ms: 1.50x faster                                                           |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.39x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                            |
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                           |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 300 us: 1.62x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.55x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 86.4 ms: 1.15x faster                                                           |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 159 ms: 1.06x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                           |
| django_template | 48.2 ms                                                | 34.3 ms: 1.41x faster                                                           |
| genshi_text     | 31.8 ms                                                | 23.0 ms: 1.38x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 51.0 ms: 1.29x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.35x faster                                                            |
| generators               | 80.1 ms                                                | 28.1 ms: 2.85x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.14 ms: 2.52x faster                                                           |
| async_tree_none          | 728 ms                                                 | 325 ms: 2.24x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 406 ms: 2.14x faster                                                            |
| chaos                    | 115 ms                                                 | 58.1 ms: 1.99x faster                                                           |
| raytrace                 | 507 ms                                                 | 256 ms: 1.98x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 29.8 us: 1.96x faster                                                           |
| async_tree_io            | 1.77 sec                                               | 907 ms: 1.95x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 486 ms: 1.90x faster                                                            |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                            |
| logging_silent           | 190 ns                                                 | 104 ns: 1.83x faster                                                            |
| richards_super           | 94.7 ms                                                | 51.9 ms: 1.82x faster                                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 560 ms: 1.82x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 66.6 ms: 1.77x faster                                                           |
| nbody                    | 154 ms                                                 | 87.3 ms: 1.76x faster                                                           |
| richards                 | 79.3 ms                                                | 45.4 ms: 1.75x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                           |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 73.5 ms: 1.74x faster                                                           |
| pylint                   | 551 ms                                                 | 318 ms: 1.74x faster                                                            |
| go                       | 240 ms                                                 | 139 ms: 1.73x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.10 ms: 1.70x faster                                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.62x faster                                                            |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.55x faster                                                            |
| pyflate                  | 716 ms                                                 | 464 ms: 1.54x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.45 us: 1.52x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                          |
| tornado_http             | 136 ms                                                 | 90.2 ms: 1.51x faster                                                           |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                                           |
| float                    | 117 ms                                                 | 77.9 ms: 1.50x faster                                                           |
| logging_format           | 9.09 us                                                | 6.07 us: 1.50x faster                                                           |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.50x faster                                                            |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                            |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                          |
| django_template          | 48.2 ms                                                | 34.3 ms: 1.41x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                                          |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.38x faster                                                          |
| genshi_text              | 31.8 ms                                                | 23.0 ms: 1.38x faster                                                           |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                           |
| html5lib                 | 88.9 ms                                                | 64.8 ms: 1.37x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 746 ms: 1.36x faster                                                            |
| thrift                   | 1.07 ms                                                | 787 us: 1.36x faster                                                            |
| nqueens                  | 106 ms                                                 | 78.8 ms: 1.34x faster                                                           |
| fannkuch                 | 532 ms                                                 | 396 ms: 1.34x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                                            |
| 2to3                     | 348 ms                                                 | 261 ms: 1.33x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.96 ms: 1.30x faster                                                           |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                            |
| sqlglot_optimize         | 69.2 ms                                                | 53.2 ms: 1.30x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 51.0 ms: 1.29x faster                                                           |
| scimark_fft              | 466 ms                                                 | 361 ms: 1.29x faster                                                            |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                           |
| sympy_str                | 346 ms                                                 | 271 ms: 1.27x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 786 us: 1.25x faster                                                            |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                          |
| xml_etree_generate       | 99.4 ms                                                | 86.4 ms: 1.15x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                           |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                            |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                            |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.67 sec: 1.07x faster                                                          |
| xml_etree_parse          | 168 ms                                                 | 159 ms: 1.06x faster                                                            |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                            |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                            |
| async_generators         | 444 ms                                                 | 434 ms: 1.02x faster                                                            |
| coverage                 | 79.4 ms                                                | 84.0 ms: 1.06x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 3.85 ms: 1.06x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                           |
| telco                    | 7.27 ms                                                | 8.14 ms: 1.12x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                    |

Benchmark hidden because not significant (3): regex_effbot, asyncio_websockets, bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240828-3.14.0a0-bfd4400/bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.12x
# Results vs. 3.10.4

- fork: faster-cpython
- ref: more_robust_immortal
- machine: linux-x86_64
- commit hash: 9f86e46
- commit date: 2024-10-10
- overall geometric mean: 1.422x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                            |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                          |
| html5lib       | 88.9 ms                                                | 61.7 ms: 1.44x faster                                                           |
| tornado_http   | 136 ms                                                 | 90.4 ms: 1.51x faster                                                           |
| Geometric mean | (ref)                                                  | 1.39x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 325 ms: 2.24x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 396 ms: 2.20x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 937 ms: 1.89x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 559 ms: 1.82x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 92.7 ms: 1.66x faster                                                           |
| float          | 117 ms                                                 | 78.8 ms: 1.49x faster                                                           |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                            |
| regex_v8       | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                           |
| regex_dna      | 227 ms                                                 | 222 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 309 us: 1.57x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                          |
| unpickle_pure_python | 331 us                                                 | 220 us: 1.50x faster                                                            |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                           |
| json_loads           | 31.2 us                                                | 26.3 us: 1.19x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 87.0 ms: 1.14x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 155 ms: 1.08x faster                                                            |
| pickle_list          | 5.08 us                                                | 5.11 us: 1.01x slower                                                           |
| unpickle             | 14.4 us                                                | 15.1 us: 1.05x slower                                                           |
| pickle               | 10.7 us                                                | 11.4 us: 1.07x slower                                                           |
| pickle_dict          | 29.6 us                                                | 34.2 us: 1.15x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 34.2 ms: 1.41x faster                                                           |
| mako            | 16.3 ms                                                | 11.6 ms: 1.41x faster                                                           |
| genshi_text     | 31.8 ms                                                | 22.8 ms: 1.40x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 49.1 ms: 1.35x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.42x faster                                                            |
| generators               | 80.1 ms                                                | 26.9 ms: 2.97x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.32 ms: 2.39x faster                                                           |
| async_tree_none          | 728 ms                                                 | 325 ms: 2.24x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 396 ms: 2.20x faster                                                            |
| go                       | 240 ms                                                 | 121 ms: 1.98x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 477 ms: 1.93x faster                                                            |
| chaos                    | 115 ms                                                 | 60.2 ms: 1.92x faster                                                           |
| async_tree_io            | 1.77 sec                                               | 937 ms: 1.89x faster                                                            |
| raytrace                 | 507 ms                                                 | 269 ms: 1.88x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 31.3 us: 1.87x faster                                                           |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 559 ms: 1.82x faster                                                            |
| richards_super           | 94.7 ms                                                | 52.9 ms: 1.79x faster                                                           |
| logging_silent           | 190 ns                                                 | 108 ns: 1.76x faster                                                            |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.75x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 73.3 ms: 1.74x faster                                                           |
| pylint                   | 551 ms                                                 | 318 ms: 1.74x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 68.5 ms: 1.73x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                                           |
| richards                 | 79.3 ms                                                | 46.8 ms: 1.69x faster                                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.66x faster                                                           |
| nbody                    | 154 ms                                                 | 92.7 ms: 1.66x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.29 ms: 1.65x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                           |
| pyflate                  | 716 ms                                                 | 457 ms: 1.57x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 309 us: 1.57x faster                                                            |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                          |
| tornado_http             | 136 ms                                                 | 90.4 ms: 1.51x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 220 us: 1.50x faster                                                            |
| float                    | 117 ms                                                 | 78.8 ms: 1.49x faster                                                           |
| logging_simple           | 8.30 us                                                | 5.60 us: 1.48x faster                                                           |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.47x faster                                                           |
| logging_format           | 9.09 us                                                | 6.18 us: 1.47x faster                                                           |
| spectral_norm            | 170 ms                                                 | 116 ms: 1.47x faster                                                            |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.78 sec: 1.44x faster                                                          |
| html5lib                 | 88.9 ms                                                | 61.7 ms: 1.44x faster                                                           |
| django_template          | 48.2 ms                                                | 34.2 ms: 1.41x faster                                                           |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.41x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.41x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 725 ms: 1.40x faster                                                            |
| genshi_text              | 31.8 ms                                                | 22.8 ms: 1.40x faster                                                           |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                           |
| thrift                   | 1.07 ms                                                | 780 us: 1.37x faster                                                            |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.80 ms: 1.35x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                          |
| genshi_xml               | 66.0 ms                                                | 49.1 ms: 1.35x faster                                                           |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                                            |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                           |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                                            |
| dulwich_log              | 84.3 ms                                                | 64.3 ms: 1.31x faster                                                           |
| nqueens                  | 106 ms                                                 | 80.7 ms: 1.31x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 53.6 ms: 1.29x faster                                                           |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                            |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                           |
| unpack_sequence          | 60.0 ns                                                | 47.0 ns: 1.28x faster                                                           |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                          |
| scimark_fft              | 466 ms                                                 | 373 ms: 1.25x faster                                                            |
| sympy_expand             | 566 ms                                                 | 458 ms: 1.23x faster                                                            |
| json_loads               | 31.2 us                                                | 26.3 us: 1.19x faster                                                           |
| bench_thread_pool        | 986 us                                                 | 849 us: 1.16x faster                                                            |
| json                     | 5.69 ms                                                | 4.93 ms: 1.16x faster                                                           |
| xml_etree_generate       | 99.4 ms                                                | 87.0 ms: 1.14x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.51 sec: 1.14x faster                                                          |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 155 ms: 1.08x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                                           |
| regex_dna                | 227 ms                                                 | 222 ms: 1.02x faster                                                            |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                            |
| async_generators         | 444 ms                                                 | 437 ms: 1.02x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                            |
| pickle_list              | 5.08 us                                                | 5.11 us: 1.01x slower                                                           |
| unpickle                 | 14.4 us                                                | 15.1 us: 1.05x slower                                                           |
| coverage                 | 79.4 ms                                                | 84.1 ms: 1.06x slower                                                           |
| pickle                   | 10.7 us                                                | 11.4 us: 1.07x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 3.99 ms: 1.10x slower                                                           |
| telco                    | 7.27 ms                                                | 8.01 ms: 1.10x slower                                                           |
| pickle_dict              | 29.6 us                                                | 34.2 us: 1.15x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                           |
| bench_mp_pool            | 24.0 ms                                                | 56.3 ms: 2.35x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                                    |

Benchmark hidden because not significant (2): regex_effbot, unpickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241010-3.14.0a0-9f86e46/bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.422x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.12x
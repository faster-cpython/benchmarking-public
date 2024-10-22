# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: partial_evaluator
- machine: linux-x86_64
- commit hash: a6bc1a0
- commit date: 2024-09-04
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 276 ms: 1.26x faster                                                         |
| docutils       | 3.30 sec                                               | 2.95 sec: 1.12x faster                                                       |
| html5lib       | 88.9 ms                                                | 62.4 ms: 1.42x faster                                                        |
| tornado_http   | 136 ms                                                 | 95.0 ms: 1.43x faster                                                        |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 331 ms: 2.20x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 414 ms: 2.10x faster                                                         |
| async_tree_io           | 1.77 sec                                               | 946 ms: 1.87x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 568 ms: 1.79x faster                                                         |
| Geometric mean          | (ref)                                                  | 1.98x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.0 ms: 1.92x faster                                                        |
| float          | 117 ms                                                 | 70.9 ms: 1.65x faster                                                        |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.48x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 141 ms: 1.33x faster                                                         |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.12x faster                                                        |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.63x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 300 us: 1.61x faster                                                         |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 54.5 ms: 1.45x faster                                                        |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 77.4 ms: 1.28x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 98.8 ms: 1.17x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                         |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.21 ms: 1.22x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.72 ms: 1.68x faster                                                        |
| django_template | 48.2 ms                                                | 35.9 ms: 1.34x faster                                                        |
| genshi_text     | 31.8 ms                                                | 24.6 ms: 1.30x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 56.6 ms: 1.17x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.18 ms: 2.49x faster                                                        |
| generators               | 80.1 ms                                                | 32.9 ms: 2.43x faster                                                        |
| async_tree_none          | 728 ms                                                 | 331 ms: 2.20x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 27.0 us: 2.16x faster                                                        |
| richards_super           | 94.7 ms                                                | 44.8 ms: 2.12x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 414 ms: 2.10x faster                                                         |
| richards                 | 79.3 ms                                                | 39.2 ms: 2.02x faster                                                        |
| chaos                    | 115 ms                                                 | 59.1 ms: 1.95x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 65.7 ms: 1.95x faster                                                        |
| nbody                    | 154 ms                                                 | 80.0 ms: 1.92x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 63.2 ms: 1.87x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 946 ms: 1.87x faster                                                         |
| asyncio_tcp              | 922 ms                                                 | 494 ms: 1.86x faster                                                         |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                                         |
| raytrace                 | 507 ms                                                 | 272 ms: 1.86x faster                                                         |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                         |
| go                       | 240 ms                                                 | 130 ms: 1.85x faster                                                         |
| deepcopy                 | 479 us                                                 | 261 us: 1.83x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 568 ms: 1.79x faster                                                         |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.75x faster                                                        |
| mako                     | 16.3 ms                                                | 9.72 ms: 1.68x faster                                                        |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.66x faster                                                         |
| float                    | 117 ms                                                 | 70.9 ms: 1.65x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.63x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.61x faster                                                         |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.60x faster                                                         |
| pyflate                  | 716 ms                                                 | 456 ms: 1.57x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                                         |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.68 ms: 1.53x faster                                                        |
| scimark_fft              | 466 ms                                                 | 309 ms: 1.51x faster                                                         |
| hexiom                   | 10.4 ms                                                | 6.92 ms: 1.50x faster                                                        |
| pylint                   | 551 ms                                                 | 372 ms: 1.48x faster                                                         |
| logging_format           | 9.09 us                                                | 6.14 us: 1.48x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.37 ms: 1.48x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.61 us: 1.48x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 54.5 ms: 1.45x faster                                                        |
| tornado_http             | 136 ms                                                 | 95.0 ms: 1.43x faster                                                        |
| fannkuch                 | 532 ms                                                 | 371 ms: 1.43x faster                                                         |
| html5lib                 | 88.9 ms                                                | 62.4 ms: 1.42x faster                                                        |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 729 ms: 1.40x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                       |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                        |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                        |
| thrift                   | 1.07 ms                                                | 782 us: 1.37x faster                                                         |
| django_template          | 48.2 ms                                                | 35.9 ms: 1.34x faster                                                        |
| regex_compile            | 188 ms                                                 | 141 ms: 1.33x faster                                                         |
| pathlib                  | 20.5 ms                                                | 15.7 ms: 1.30x faster                                                        |
| genshi_text              | 31.8 ms                                                | 24.6 ms: 1.30x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.22 sec: 1.29x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 77.4 ms: 1.28x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                                         |
| 2to3                     | 348 ms                                                 | 276 ms: 1.26x faster                                                         |
| nqueens                  | 106 ms                                                 | 85.3 ms: 1.24x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 68.4 ms: 1.23x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 57.8 ms: 1.20x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 831 us: 1.19x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 98.8 ms: 1.17x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 56.6 ms: 1.17x faster                                                        |
| sympy_str                | 346 ms                                                 | 299 ms: 1.16x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                         |
| sympy_sum                | 196 ms                                                 | 172 ms: 1.14x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 22.7 ms: 1.13x faster                                                        |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.12x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                       |
| docutils                 | 3.30 sec                                               | 2.95 sec: 1.12x faster                                                       |
| sympy_expand             | 566 ms                                                 | 507 ms: 1.12x faster                                                         |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                        |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                         |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                                        |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                         |
| async_generators         | 444 ms                                                 | 459 ms: 1.03x slower                                                         |
| gc_traversal             | 3.62 ms                                                | 3.77 ms: 1.04x slower                                                        |
| coverage                 | 79.4 ms                                                | 86.4 ms: 1.09x slower                                                        |
| telco                    | 7.27 ms                                                | 7.91 ms: 1.09x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.21 ms: 1.22x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                 |

Benchmark hidden because not significant (2): regex_effbot, bench_mp_pool
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240904-3.14.0a0-a6bc1a0-JIT/bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.22x
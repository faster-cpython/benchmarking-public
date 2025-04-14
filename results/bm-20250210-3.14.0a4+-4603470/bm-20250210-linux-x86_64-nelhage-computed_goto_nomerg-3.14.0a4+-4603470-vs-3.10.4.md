# Results vs. 3.10.4

- fork: nelhage
- ref: computed_goto_nomerg
- machine: linux-x86_64
- commit hash: 4603470
- commit date: 2025-02-10
- overall geometric mean: 1.463x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 252 ms: 1.39x faster                                                    |
| docutils       | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                  |
| html5lib       | 88.9 ms                                                | 61.2 ms: 1.45x faster                                                   |
| Geometric mean | (ref)                                                  | 1.37x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 621 ms: 2.85x faster                                                    |
| async_tree_none         | 728 ms                                                 | 266 ms: 2.74x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 325 ms: 2.68x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 488 ms: 2.08x faster                                                    |
| Geometric mean          | (ref)                                                  | 2.57x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 68.4 ms: 1.71x faster                                                   |
| nbody          | 154 ms                                                 | 91.7 ms: 1.67x faster                                                   |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.43x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.21 ms: 1.13x faster                                                   |
| regex_v8       | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                   |
| regex_dna      | 227 ms                                                 | 211 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                  | 1.19x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 317 us: 1.53x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 58.4 ms: 1.36x faster                                                   |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 96.5 ms: 1.20x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 83.4 ms: 1.19x faster                                                   |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.6 ms: 1.53x faster                                                   |
| genshi_text     | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                   |
| mako            | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 48.1 ms: 1.37x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.47x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 158 us: 3.43x faster                                                    |
| generators               | 80.1 ms                                                | 27.8 ms: 2.88x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 621 ms: 2.85x faster                                                    |
| async_tree_none          | 728 ms                                                 | 266 ms: 2.74x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 325 ms: 2.68x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.18 ms: 2.49x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 488 ms: 2.08x faster                                                    |
| go                       | 240 ms                                                 | 116 ms: 2.08x faster                                                    |
| pylint                   | 551 ms                                                 | 272 ms: 2.03x faster                                                    |
| chaos                    | 115 ms                                                 | 57.5 ms: 2.01x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 30.4 us: 1.92x faster                                                   |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                    |
| richards_super           | 94.7 ms                                                | 50.2 ms: 1.89x faster                                                   |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                                    |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                    |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 70.4 ms: 1.82x faster                                                   |
| spectral_norm            | 170 ms                                                 | 94.1 ms: 1.81x faster                                                   |
| richards                 | 79.3 ms                                                | 44.3 ms: 1.79x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 66.2 ms: 1.78x faster                                                   |
| comprehensions           | 28.8 us                                                | 16.3 us: 1.76x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.23 ms: 1.76x faster                                                   |
| float                    | 117 ms                                                 | 68.4 ms: 1.71x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.10 ms: 1.70x faster                                                   |
| nbody                    | 154 ms                                                 | 91.7 ms: 1.67x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.54 ms: 1.67x faster                                                   |
| pyflate                  | 716 ms                                                 | 435 ms: 1.65x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.39 us: 1.54x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 317 us: 1.53x faster                                                    |
| django_template          | 48.2 ms                                                | 31.6 ms: 1.53x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                                   |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                    |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                                   |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                    |
| genshi_text              | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                   |
| logging_format           | 9.09 us                                                | 6.07 us: 1.50x faster                                                   |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                   |
| html5lib                 | 88.9 ms                                                | 61.2 ms: 1.45x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 707 ms: 1.44x faster                                                    |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.3 ms: 1.43x faster                                                   |
| thrift                   | 1.07 ms                                                | 753 us: 1.42x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 103 ms: 1.39x faster                                                    |
| 2to3                     | 348 ms                                                 | 252 ms: 1.39x faster                                                    |
| scimark_fft              | 466 ms                                                 | 339 ms: 1.38x faster                                                    |
| genshi_xml               | 66.0 ms                                                | 48.1 ms: 1.37x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 58.4 ms: 1.36x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 127 ms: 1.35x faster                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 51.5 ms: 1.34x faster                                                   |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.34x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.85 ms: 1.33x faster                                                   |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.31x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 64.5 ms: 1.31x faster                                                   |
| nqueens                  | 106 ms                                                 | 81.0 ms: 1.31x faster                                                   |
| sympy_str                | 346 ms                                                 | 267 ms: 1.30x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                  |
| sympy_expand             | 566 ms                                                 | 450 ms: 1.26x faster                                                    |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.25x faster                                                   |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 96.5 ms: 1.20x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 83.4 ms: 1.19x faster                                                   |
| async_generators         | 444 ms                                                 | 381 ms: 1.16x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.46 sec: 1.16x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 860 us: 1.15x faster                                                    |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                   |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.13x faster                                                    |
| regex_effbot             | 3.63 ms                                                | 3.21 ms: 1.13x faster                                                   |
| json                     | 5.69 ms                                                | 5.15 ms: 1.11x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                   |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                                   |
| regex_dna                | 227 ms                                                 | 211 ms: 1.07x faster                                                    |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                    |
| telco                    | 7.27 ms                                                | 7.80 ms: 1.07x slower                                                   |
| coverage                 | 79.4 ms                                                | 89.5 ms: 1.13x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 4.73 ms: 1.30x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.53x slower                                                   |
| bench_mp_pool            | 24.0 ms                                                | 80.9 ms: 3.37x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                            |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250210-3.14.0a4+-4603470/bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.463x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.26x
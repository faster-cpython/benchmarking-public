# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: optimizer_constant_p
- machine: linux-x86_64
- commit hash: 3330a62
- commit date: 2024-06-15
- overall geometric mean: 1.36x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 281 ms: 1.24x faster                                                            |
| docutils       | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                          |
| html5lib       | 88.9 ms                                                | 68.1 ms: 1.30x faster                                                           |
| tornado_http   | 136 ms                                                 | 96.2 ms: 1.42x faster                                                           |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 374 ms: 1.95x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 949 ms: 1.86x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 492 ms: 1.77x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 620 ms: 1.64x faster                                                            |
| Geometric mean          | (ref)                                                  | 1.80x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.4 ms: 1.91x faster                                                           |
| float          | 117 ms                                                 | 71.9 ms: 1.63x faster                                                           |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.47x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 137 ms: 1.38x faster                                                            |
| regex_v8       | 27.8 ms                                                | 23.7 ms: 1.17x faster                                                           |
| regex_dna      | 227 ms                                                 | 226 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 295 us: 1.64x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                          |
| unpickle_pure_python | 331 us                                                 | 221 us: 1.49x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 58.2 ms: 1.36x faster                                                           |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.36x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 82.5 ms: 1.21x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 152 ms: 1.11x faster                                                            |
| json_loads           | 31.2 us                                                | 28.9 us: 1.08x faster                                                           |
| pickle_list          | 5.08 us                                                | 5.19 us: 1.02x slower                                                           |
| unpickle             | 14.4 us                                                | 15.1 us: 1.05x slower                                                           |
| pickle               | 10.7 us                                                | 12.2 us: 1.14x slower                                                           |
| pickle_dict          | 29.6 us                                                | 35.4 us: 1.20x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.2 ms: 1.30x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.65 ms: 1.29x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.0 ms: 1.62x faster                                                           |
| django_template | 48.2 ms                                                | 37.0 ms: 1.30x faster                                                           |
| genshi_text     | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 58.8 ms: 1.12x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                                            |
| generators               | 80.1 ms                                                | 30.2 ms: 2.65x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.61 ms: 2.19x faster                                                           |
| deepcopy_memo            | 58.5 us                                                | 28.9 us: 2.03x faster                                                           |
| async_tree_none          | 728 ms                                                 | 374 ms: 1.95x faster                                                            |
| richards_super           | 94.7 ms                                                | 48.8 ms: 1.94x faster                                                           |
| chaos                    | 115 ms                                                 | 59.8 ms: 1.93x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 61.7 ms: 1.92x faster                                                           |
| nbody                    | 154 ms                                                 | 80.4 ms: 1.91x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 68.2 ms: 1.87x faster                                                           |
| async_tree_io            | 1.77 sec                                               | 949 ms: 1.86x faster                                                            |
| richards                 | 79.3 ms                                                | 42.9 ms: 1.85x faster                                                           |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                                            |
| logging_silent           | 190 ns                                                 | 107 ns: 1.78x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 520 ms: 1.77x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 492 ms: 1.77x faster                                                            |
| deepcopy                 | 479 us                                                 | 272 us: 1.76x faster                                                            |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.65x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 295 us: 1.64x faster                                                            |
| scimark_sor              | 220 ms                                                 | 134 ms: 1.64x faster                                                            |
| pyflate                  | 716 ms                                                 | 437 ms: 1.64x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 620 ms: 1.64x faster                                                            |
| go                       | 240 ms                                                 | 147 ms: 1.63x faster                                                            |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                                            |
| float                    | 117 ms                                                 | 71.9 ms: 1.63x faster                                                           |
| mako                     | 16.3 ms                                                | 10.0 ms: 1.62x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                          |
| pylint                   | 551 ms                                                 | 349 ms: 1.58x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.63 ms: 1.57x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.56x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 221 us: 1.49x faster                                                            |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.49x faster                                                           |
| scimark_fft              | 466 ms                                                 | 315 ms: 1.48x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.63 us: 1.47x faster                                                           |
| fannkuch                 | 532 ms                                                 | 361 ms: 1.47x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.44 ms: 1.46x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                          |
| logging_format           | 9.09 us                                                | 6.30 us: 1.44x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 711 ms: 1.43x faster                                                            |
| tornado_http             | 136 ms                                                 | 96.2 ms: 1.42x faster                                                           |
| scimark_lu               | 176 ms                                                 | 126 ms: 1.40x faster                                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                                          |
| regex_compile            | 188 ms                                                 | 137 ms: 1.38x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 58.2 ms: 1.36x faster                                                           |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.36x faster                                                           |
| thrift                   | 1.07 ms                                                | 815 us: 1.31x faster                                                            |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                                          |
| html5lib                 | 88.9 ms                                                | 68.1 ms: 1.30x faster                                                           |
| django_template          | 48.2 ms                                                | 37.0 ms: 1.30x faster                                                           |
| python_startup           | 14.6 ms                                                | 11.2 ms: 1.30x faster                                                           |
| genshi_text              | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                            |
| 2to3                     | 348 ms                                                 | 281 ms: 1.24x faster                                                            |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 68.7 ms: 1.23x faster                                                           |
| nqueens                  | 106 ms                                                 | 86.7 ms: 1.22x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 56.9 ms: 1.22x faster                                                           |
| xml_etree_generate       | 99.4 ms                                                | 82.5 ms: 1.21x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 23.7 ms: 1.17x faster                                                           |
| dask                     | 441 ms                                                 | 380 ms: 1.16x faster                                                            |
| sympy_sum                | 196 ms                                                 | 170 ms: 1.16x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 22.4 ms: 1.15x faster                                                           |
| sympy_str                | 346 ms                                                 | 300 ms: 1.15x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 873 us: 1.13x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                          |
| genshi_xml               | 66.0 ms                                                | 58.8 ms: 1.12x faster                                                           |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                            |
| sympy_expand             | 566 ms                                                 | 509 ms: 1.11x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 152 ms: 1.11x faster                                                            |
| mdp                      | 2.85 sec                                               | 2.58 sec: 1.10x faster                                                          |
| json_loads               | 31.2 us                                                | 28.9 us: 1.08x faster                                                           |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                                           |
| json                     | 5.69 ms                                                | 5.46 ms: 1.04x faster                                                           |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                                            |
| regex_dna                | 227 ms                                                 | 226 ms: 1.00x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 565 ms: 1.01x slower                                                            |
| pickle_list              | 5.08 us                                                | 5.19 us: 1.02x slower                                                           |
| unpickle                 | 14.4 us                                                | 15.1 us: 1.05x slower                                                           |
| async_generators         | 444 ms                                                 | 469 ms: 1.06x slower                                                            |
| gc_traversal             | 3.62 ms                                                | 3.90 ms: 1.08x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.80 ms: 1.11x slower                                                           |
| telco                    | 7.27 ms                                                | 8.09 ms: 1.11x slower                                                           |
| pickle                   | 10.7 us                                                | 12.2 us: 1.14x slower                                                           |
| pickle_dict              | 29.6 us                                                | 35.4 us: 1.20x slower                                                           |
| coverage                 | 79.4 ms                                                | 95.0 ms: 1.20x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.65 ms: 1.29x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                                    |

Benchmark hidden because not significant (3): regex_effbot, bench_mp_pool, unpickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240615-3.14.0a0-3330a62-JIT/bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.21x
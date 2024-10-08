# Results vs. 3.10.4

- fork: savannahostrowski
- ref: jit_invalidate_500k
- machine: linux-x86_64
- commit hash: 61a6174
- commit date: 2024-09-25
- overall geometric mean: 1.37x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 276 ms: 1.26x faster                                                            |
| docutils       | 3.30 sec                                               | 2.93 sec: 1.12x faster                                                          |
| html5lib       | 88.9 ms                                                | 62.0 ms: 1.43x faster                                                           |
| tornado_http   | 136 ms                                                 | 94.6 ms: 1.44x faster                                                           |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 320 ms: 2.28x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 398 ms: 2.18x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 887 ms: 1.99x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 564 ms: 1.80x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.06x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.4 ms: 1.89x faster                                                           |
| float          | 117 ms                                                 | 69.8 ms: 1.68x faster                                                           |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.48x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 142 ms: 1.32x faster                                                            |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                           |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.70 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.63x faster                                                          |
| pickle_pure_python   | 484 us                                                 | 303 us: 1.60x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                            |
| json_dumps           | 14.2 ms                                                | 9.81 ms: 1.44x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 54.8 ms: 1.44x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 77.3 ms: 1.29x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                            |
| json_loads           | 31.2 us                                                | 27.2 us: 1.15x faster                                                           |
| pickle_list          | 5.08 us                                                | 5.11 us: 1.01x slower                                                           |
| unpickle_list        | 5.20 us                                                | 5.27 us: 1.01x slower                                                           |
| unpickle             | 14.4 us                                                | 14.8 us: 1.03x slower                                                           |
| pickle               | 10.7 us                                                | 11.7 us: 1.09x slower                                                           |
| pickle_dict          | 29.6 us                                                | 35.0 us: 1.18x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.74 ms: 1.68x faster                                                           |
| django_template | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                           |
| genshi_text     | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 58.3 ms: 1.13x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                                            |
| deltablue                | 7.91 ms                                                | 3.20 ms: 2.47x faster                                                           |
| generators               | 80.1 ms                                                | 34.9 ms: 2.30x faster                                                           |
| async_tree_none          | 728 ms                                                 | 320 ms: 2.28x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 398 ms: 2.18x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 27.4 us: 2.13x faster                                                           |
| richards_super           | 94.7 ms                                                | 46.9 ms: 2.02x faster                                                           |
| async_tree_io            | 1.77 sec                                               | 887 ms: 1.99x faster                                                            |
| chaos                    | 115 ms                                                 | 59.1 ms: 1.95x faster                                                           |
| richards                 | 79.3 ms                                                | 41.1 ms: 1.93x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 67.5 ms: 1.89x faster                                                           |
| nbody                    | 154 ms                                                 | 81.4 ms: 1.89x faster                                                           |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 63.2 ms: 1.87x faster                                                           |
| asyncio_tcp              | 922 ms                                                 | 497 ms: 1.86x faster                                                            |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                            |
| raytrace                 | 507 ms                                                 | 276 ms: 1.83x faster                                                            |
| go                       | 240 ms                                                 | 133 ms: 1.81x faster                                                            |
| deepcopy                 | 479 us                                                 | 266 us: 1.80x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 564 ms: 1.80x faster                                                            |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                                           |
| float                    | 117 ms                                                 | 69.8 ms: 1.68x faster                                                           |
| mako                     | 16.3 ms                                                | 9.74 ms: 1.68x faster                                                           |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.64x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.63x faster                                                          |
| pyflate                  | 716 ms                                                 | 439 ms: 1.63x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.62x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 303 us: 1.60x faster                                                            |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.59x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                           |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.69 ms: 1.53x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.97 ms: 1.49x faster                                                           |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                                            |
| logging_format           | 9.09 us                                                | 6.15 us: 1.48x faster                                                           |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.40 ms: 1.47x faster                                                           |
| pylint                   | 551 ms                                                 | 381 ms: 1.45x faster                                                            |
| json_dumps               | 14.2 ms                                                | 9.81 ms: 1.44x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 54.8 ms: 1.44x faster                                                           |
| tornado_http             | 136 ms                                                 | 94.6 ms: 1.44x faster                                                           |
| html5lib                 | 88.9 ms                                                | 62.0 ms: 1.43x faster                                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                          |
| fannkuch                 | 532 ms                                                 | 377 ms: 1.41x faster                                                            |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 744 ms: 1.37x faster                                                            |
| thrift                   | 1.07 ms                                                | 788 us: 1.36x faster                                                            |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                                          |
| django_template          | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                          |
| regex_compile            | 188 ms                                                 | 142 ms: 1.32x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 77.3 ms: 1.29x faster                                                           |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                           |
| genshi_text              | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.28x faster                                                            |
| 2to3                     | 348 ms                                                 | 276 ms: 1.26x faster                                                            |
| dulwich_log              | 84.3 ms                                                | 68.6 ms: 1.23x faster                                                           |
| nqueens                  | 106 ms                                                 | 88.5 ms: 1.20x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 58.4 ms: 1.19x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                                           |
| bench_thread_pool        | 986 us                                                 | 844 us: 1.17x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                            |
| sympy_str                | 346 ms                                                 | 300 ms: 1.15x faster                                                            |
| json_loads               | 31.2 us                                                | 27.2 us: 1.15x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 58.3 ms: 1.13x faster                                                           |
| sympy_sum                | 196 ms                                                 | 174 ms: 1.13x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 22.9 ms: 1.13x faster                                                           |
| docutils                 | 3.30 sec                                               | 2.93 sec: 1.12x faster                                                          |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                          |
| sympy_expand             | 566 ms                                                 | 506 ms: 1.12x faster                                                            |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                            |
| json                     | 5.69 ms                                                | 5.17 ms: 1.10x faster                                                           |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                                           |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                            |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                            |
| pickle_list              | 5.08 us                                                | 5.11 us: 1.01x slower                                                           |
| unpickle_list            | 5.20 us                                                | 5.27 us: 1.01x slower                                                           |
| regex_effbot             | 3.63 ms                                                | 3.70 ms: 1.02x slower                                                           |
| unpickle                 | 14.4 us                                                | 14.8 us: 1.03x slower                                                           |
| async_generators         | 444 ms                                                 | 460 ms: 1.04x slower                                                            |
| gc_traversal             | 3.62 ms                                                | 3.77 ms: 1.04x slower                                                           |
| coverage                 | 79.4 ms                                                | 85.4 ms: 1.07x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                           |
| pickle                   | 10.7 us                                                | 11.7 us: 1.09x slower                                                           |
| telco                    | 7.27 ms                                                | 7.96 ms: 1.10x slower                                                           |
| pickle_dict              | 29.6 us                                                | 35.0 us: 1.18x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                           |
| unpack_sequence          | 60.0 ns                                                | 112 ns: 1.86x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                                    |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240925-3.14.0a0-61a6174-JIT/bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.19x
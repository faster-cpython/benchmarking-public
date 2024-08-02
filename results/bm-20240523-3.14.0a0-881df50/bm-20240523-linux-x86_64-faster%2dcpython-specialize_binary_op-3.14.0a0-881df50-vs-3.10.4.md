# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_binary_op
- machine: linux-x86_64
- commit hash: 881df50
- commit date: 2024-05-23
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 271 ms: 1.29x faster                                                            |
| chameleon      | 9.68 ms                                                | 7.03 ms: 1.38x faster                                                           |
| docutils       | 3.30 sec                                               | 2.78 sec: 1.18x faster                                                          |
| html5lib       | 88.9 ms                                                | 67.2 ms: 1.32x faster                                                           |
| tornado_http   | 136 ms                                                 | 94.1 ms: 1.45x faster                                                           |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 383 ms: 1.90x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 933 ms: 1.89x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 464 ms: 1.88x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 613 ms: 1.66x faster                                                            |
| Geometric mean          | (ref)                                                  | 1.83x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 97.1 ms: 1.58x faster                                                           |
| float          | 117 ms                                                 | 78.5 ms: 1.49x faster                                                           |
| pidigits       | 191 ms                                                 | 191 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.33x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 133 ms: 1.42x faster                                                            |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                           |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.85 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 309 us: 1.57x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.18 sec: 1.44x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 60.0 ms: 1.32x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 85.8 ms: 1.16x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                                            |
| json_loads           | 31.2 us                                                | 29.1 us: 1.07x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 161 ms: 1.04x faster                                                            |
| pickle_list          | 5.08 us                                                | 5.19 us: 1.02x slower                                                           |
| unpickle_list        | 5.20 us                                                | 5.35 us: 1.03x slower                                                           |
| unpickle             | 14.4 us                                                | 15.2 us: 1.06x slower                                                           |
| pickle               | 10.7 us                                                | 12.0 us: 1.13x slower                                                           |
| pickle_dict          | 29.6 us                                                | 35.9 us: 1.21x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.1 ms: 1.46x faster                                                           |
| django_template | 48.2 ms                                                | 34.7 ms: 1.39x faster                                                           |
| genshi_text     | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 50.9 ms: 1.30x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.35x faster                                                            |
| generators               | 80.1 ms                                                | 29.7 ms: 2.70x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.23 ms: 2.45x faster                                                           |
| async_tree_none          | 728 ms                                                 | 383 ms: 1.90x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 933 ms: 1.89x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 464 ms: 1.88x faster                                                            |
| chaos                    | 115 ms                                                 | 61.7 ms: 1.87x faster                                                           |
| raytrace                 | 507 ms                                                 | 277 ms: 1.83x faster                                                            |
| logging_silent           | 190 ns                                                 | 104 ns: 1.83x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 509 ms: 1.81x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 72.4 ms: 1.76x faster                                                           |
| richards_super           | 94.7 ms                                                | 54.1 ms: 1.75x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                           |
| pylint                   | 551 ms                                                 | 318 ms: 1.73x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 69.6 ms: 1.70x faster                                                           |
| go                       | 240 ms                                                 | 142 ms: 1.69x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 613 ms: 1.66x faster                                                            |
| richards                 | 79.3 ms                                                | 47.9 ms: 1.65x faster                                                           |
| scimark_sor              | 220 ms                                                 | 133 ms: 1.65x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.32 ms: 1.64x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                           |
| nbody                    | 154 ms                                                 | 97.1 ms: 1.58x faster                                                           |
| spectral_norm            | 170 ms                                                 | 108 ms: 1.58x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 309 us: 1.57x faster                                                            |
| pyflate                  | 716 ms                                                 | 472 ms: 1.52x faster                                                            |
| float                    | 117 ms                                                 | 78.5 ms: 1.49x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                            |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                            |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.46x faster                                                           |
| deepcopy_memo            | 58.5 us                                                | 40.0 us: 1.46x faster                                                           |
| tornado_http             | 136 ms                                                 | 94.1 ms: 1.45x faster                                                           |
| coroutines               | 35.1 ms                                                | 24.3 ms: 1.44x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.18 sec: 1.44x faster                                                          |
| logging_simple           | 8.30 us                                                | 5.82 us: 1.43x faster                                                           |
| logging_format           | 9.09 us                                                | 6.39 us: 1.42x faster                                                           |
| regex_compile            | 188 ms                                                 | 133 ms: 1.42x faster                                                            |
| python_startup           | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                                          |
| django_template          | 48.2 ms                                                | 34.7 ms: 1.39x faster                                                           |
| chameleon                | 9.68 ms                                                | 7.03 ms: 1.38x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.38x faster                                                          |
| genshi_text              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 748 ms: 1.36x faster                                                            |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                           |
| html5lib                 | 88.9 ms                                                | 67.2 ms: 1.32x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 60.0 ms: 1.32x faster                                                           |
| thrift                   | 1.07 ms                                                | 814 us: 1.32x faster                                                            |
| deepcopy                 | 479 us                                                 | 365 us: 1.31x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                            |
| nqueens                  | 106 ms                                                 | 81.3 ms: 1.30x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 50.9 ms: 1.30x faster                                                           |
| fannkuch                 | 532 ms                                                 | 410 ms: 1.30x faster                                                            |
| 2to3                     | 348 ms                                                 | 271 ms: 1.29x faster                                                            |
| dulwich_log              | 84.3 ms                                                | 65.6 ms: 1.29x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 3.27 us: 1.28x faster                                                           |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.27x faster                                                            |
| sqlglot_optimize         | 69.2 ms                                                | 54.6 ms: 1.27x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 20.4 ms: 1.27x faster                                                           |
| sympy_str                | 346 ms                                                 | 279 ms: 1.24x faster                                                            |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.23x faster                                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.31 ms: 1.22x faster                                                           |
| sympy_expand             | 566 ms                                                 | 468 ms: 1.21x faster                                                            |
| scimark_fft              | 466 ms                                                 | 390 ms: 1.19x faster                                                            |
| dask                     | 441 ms                                                 | 370 ms: 1.19x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 831 us: 1.19x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.78 sec: 1.18x faster                                                          |
| xml_etree_generate       | 99.4 ms                                                | 85.8 ms: 1.16x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                           |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.09x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                                            |
| mdp                      | 2.85 sec                                               | 2.64 sec: 1.08x faster                                                          |
| json_loads               | 31.2 us                                                | 29.1 us: 1.07x faster                                                           |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 161 ms: 1.04x faster                                                            |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.96 us: 1.02x faster                                                           |
| bench_mp_pool            | 24.0 ms                                                | 23.8 ms: 1.01x faster                                                           |
| pidigits                 | 191 ms                                                 | 191 ms: 1.00x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 569 ms: 1.02x slower                                                            |
| pickle_list              | 5.08 us                                                | 5.19 us: 1.02x slower                                                           |
| unpickle_list            | 5.20 us                                                | 5.35 us: 1.03x slower                                                           |
| flaskblogging            | 8.58 ms                                                | 8.90 ms: 1.04x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 3.78 ms: 1.04x slower                                                           |
| unpickle                 | 14.4 us                                                | 15.2 us: 1.06x slower                                                           |
| regex_effbot             | 3.63 ms                                                | 3.85 ms: 1.06x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                           |
| pickle                   | 10.7 us                                                | 12.0 us: 1.13x slower                                                           |
| coverage                 | 79.4 ms                                                | 92.4 ms: 1.16x slower                                                           |
| telco                    | 7.27 ms                                                | 8.57 ms: 1.18x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                           |
| pickle_dict              | 29.6 us                                                | 35.9 us: 1.21x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                                    |

Benchmark hidden because not significant (1): async_generators
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240523-3.14.0a0-881df50/bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.11x
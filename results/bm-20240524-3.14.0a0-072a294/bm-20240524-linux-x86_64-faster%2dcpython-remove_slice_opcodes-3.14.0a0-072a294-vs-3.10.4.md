# Results vs. 3.10.4

- fork: faster-cpython
- ref: remove_slice_opcodes
- machine: linux-x86_64
- commit hash: 072a294
- commit date: 2024-05-24
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 271 ms: 1.28x faster                                                            |
| chameleon      | 9.68 ms                                                | 7.05 ms: 1.37x faster                                                           |
| docutils       | 3.30 sec                                               | 2.78 sec: 1.19x faster                                                          |
| html5lib       | 88.9 ms                                                | 67.8 ms: 1.31x faster                                                           |
| tornado_http   | 136 ms                                                 | 94.2 ms: 1.45x faster                                                           |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 387 ms: 1.88x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 976 ms: 1.81x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 485 ms: 1.79x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 623 ms: 1.63x faster                                                            |
| Geometric mean          | (ref)                                                  | 1.78x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.0 ms: 1.78x faster                                                           |
| float          | 117 ms                                                 | 79.0 ms: 1.48x faster                                                           |
| pidigits       | 191 ms                                                 | 190 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.38x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 133 ms: 1.41x faster                                                            |
| regex_v8       | 27.8 ms                                                | 25.9 ms: 1.07x faster                                                           |
| regex_dna      | 227 ms                                                 | 230 ms: 1.02x slower                                                            |
| regex_effbot   | 3.63 ms                                                | 3.78 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 304 us: 1.59x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.16 sec: 1.46x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.7 ms: 1.32x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 60.3 ms: 1.31x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 86.8 ms: 1.15x faster                                                           |
| json_loads           | 31.2 us                                                | 29.0 us: 1.08x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 107 ms: 1.08x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 161 ms: 1.04x faster                                                            |
| unpickle             | 14.4 us                                                | 15.2 us: 1.05x slower                                                           |
| unpickle_list        | 5.20 us                                                | 5.60 us: 1.08x slower                                                           |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                                           |
| pickle_dict          | 29.6 us                                                | 34.9 us: 1.18x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                                    |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.14 ms: 1.20x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                           |
| django_template | 48.2 ms                                                | 35.2 ms: 1.37x faster                                                           |
| genshi_text     | 31.8 ms                                                | 23.6 ms: 1.35x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 52.1 ms: 1.27x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.30x faster                                                            |
| generators               | 80.1 ms                                                | 29.5 ms: 2.72x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.32 ms: 2.38x faster                                                           |
| chaos                    | 115 ms                                                 | 60.0 ms: 1.93x faster                                                           |
| raytrace                 | 507 ms                                                 | 269 ms: 1.88x faster                                                            |
| async_tree_none          | 728 ms                                                 | 387 ms: 1.88x faster                                                            |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 508 ms: 1.81x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 976 ms: 1.81x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 485 ms: 1.79x faster                                                            |
| nbody                    | 154 ms                                                 | 86.0 ms: 1.78x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 67.2 ms: 1.76x faster                                                           |
| richards_super           | 94.7 ms                                                | 54.3 ms: 1.74x faster                                                           |
| pylint                   | 551 ms                                                 | 317 ms: 1.74x faster                                                            |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 75.0 ms: 1.70x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.12 ms: 1.70x faster                                                           |
| richards                 | 79.3 ms                                                | 47.5 ms: 1.67x faster                                                           |
| go                       | 240 ms                                                 | 144 ms: 1.66x faster                                                            |
| scimark_sor              | 220 ms                                                 | 133 ms: 1.65x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 623 ms: 1.63x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.59x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.57x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                            |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                            |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.49x faster                                                           |
| float                    | 117 ms                                                 | 79.0 ms: 1.48x faster                                                           |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.47x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 39.8 us: 1.47x faster                                                           |
| pyflate                  | 716 ms                                                 | 491 ms: 1.46x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 2.16 sec: 1.46x faster                                                          |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                           |
| tornado_http             | 136 ms                                                 | 94.2 ms: 1.45x faster                                                           |
| regex_compile            | 188 ms                                                 | 133 ms: 1.41x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.90 us: 1.41x faster                                                           |
| logging_format           | 9.09 us                                                | 6.49 us: 1.40x faster                                                           |
| python_startup           | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                                          |
| chameleon                | 9.68 ms                                                | 7.05 ms: 1.37x faster                                                           |
| django_template          | 48.2 ms                                                | 35.2 ms: 1.37x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.36x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 753 ms: 1.35x faster                                                            |
| genshi_text              | 31.8 ms                                                | 23.6 ms: 1.35x faster                                                           |
| thrift                   | 1.07 ms                                                | 807 us: 1.33x faster                                                            |
| json_dumps               | 14.2 ms                                                | 10.7 ms: 1.32x faster                                                           |
| html5lib                 | 88.9 ms                                                | 67.8 ms: 1.31x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 60.3 ms: 1.31x faster                                                           |
| deepcopy                 | 479 us                                                 | 366 us: 1.31x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                                            |
| dulwich_log              | 84.3 ms                                                | 65.4 ms: 1.29x faster                                                           |
| 2to3                     | 348 ms                                                 | 271 ms: 1.28x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.05 ms: 1.28x faster                                                           |
| fannkuch                 | 532 ms                                                 | 416 ms: 1.28x faster                                                            |
| nqueens                  | 106 ms                                                 | 82.9 ms: 1.28x faster                                                           |
| scimark_fft              | 466 ms                                                 | 365 ms: 1.27x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 3.27 us: 1.27x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 20.4 ms: 1.27x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 52.1 ms: 1.27x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.25 sec: 1.26x faster                                                          |
| sympy_sum                | 196 ms                                                 | 156 ms: 1.26x faster                                                            |
| sqlglot_optimize         | 69.2 ms                                                | 54.9 ms: 1.26x faster                                                           |
| sympy_str                | 346 ms                                                 | 281 ms: 1.23x faster                                                            |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.22x faster                                                           |
| sympy_expand             | 566 ms                                                 | 472 ms: 1.20x faster                                                            |
| dask                     | 441 ms                                                 | 369 ms: 1.20x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.78 sec: 1.19x faster                                                          |
| bench_thread_pool        | 986 us                                                 | 835 us: 1.18x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 86.8 ms: 1.15x faster                                                           |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                            |
| json_loads               | 31.2 us                                                | 29.0 us: 1.08x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 107 ms: 1.08x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 25.9 ms: 1.07x faster                                                           |
| json                     | 5.69 ms                                                | 5.37 ms: 1.06x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 161 ms: 1.04x faster                                                            |
| mdp                      | 2.85 sec                                               | 2.78 sec: 1.02x faster                                                          |
| sqlite_synth             | 3.02 us                                                | 2.99 us: 1.01x faster                                                           |
| pidigits                 | 191 ms                                                 | 190 ms: 1.00x faster                                                            |
| async_generators         | 444 ms                                                 | 447 ms: 1.01x slower                                                            |
| asyncio_websockets       | 559 ms                                                 | 566 ms: 1.01x slower                                                            |
| regex_dna                | 227 ms                                                 | 230 ms: 1.02x slower                                                            |
| flaskblogging            | 8.58 ms                                                | 8.90 ms: 1.04x slower                                                           |
| regex_effbot             | 3.63 ms                                                | 3.78 ms: 1.04x slower                                                           |
| unpickle                 | 14.4 us                                                | 15.2 us: 1.05x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 3.87 ms: 1.07x slower                                                           |
| unpickle_list            | 5.20 us                                                | 5.60 us: 1.08x slower                                                           |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.87 ms: 1.15x slower                                                           |
| coverage                 | 79.4 ms                                                | 91.8 ms: 1.16x slower                                                           |
| telco                    | 7.27 ms                                                | 8.40 ms: 1.16x slower                                                           |
| pickle_dict              | 29.6 us                                                | 34.9 us: 1.18x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.14 ms: 1.20x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.33x faster                                                                    |

Benchmark hidden because not significant (2): bench_mp_pool, pickle_list
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240524-3.14.0a0-072a294/bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.11x
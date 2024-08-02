# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_binary_op
- machine: linux-x86_64
- commit hash: 5386b2d
- commit date: 2024-05-29
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 279 ms: 1.25x faster                                                            |
| docutils       | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                          |
| html5lib       | 88.9 ms                                                | 66.9 ms: 1.33x faster                                                           |
| tornado_http   | 136 ms                                                 | 96.6 ms: 1.41x faster                                                           |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 384 ms: 1.89x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 464 ms: 1.87x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 958 ms: 1.85x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 615 ms: 1.65x faster                                                            |
| Geometric mean          | (ref)                                                  | 1.81x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.8 ms: 1.90x faster                                                           |
| float          | 117 ms                                                 | 71.7 ms: 1.63x faster                                                           |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.46x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 137 ms: 1.38x faster                                                            |
| regex_v8       | 27.8 ms                                                | 24.1 ms: 1.15x faster                                                           |
| regex_dna      | 227 ms                                                 | 229 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 300 us: 1.62x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                          |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                            |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 58.2 ms: 1.36x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 82.0 ms: 1.21x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 100 ms: 1.15x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 150 ms: 1.12x faster                                                            |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                                           |
| unpickle             | 14.4 us                                                | 14.7 us: 1.03x slower                                                           |
| pickle_list          | 5.08 us                                                | 5.26 us: 1.04x slower                                                           |
| unpickle_list        | 5.20 us                                                | 5.48 us: 1.05x slower                                                           |
| pickle               | 10.7 us                                                | 12.1 us: 1.13x slower                                                           |
| pickle_dict          | 29.6 us                                                | 36.0 us: 1.22x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.1 ms: 1.32x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.59 ms: 1.28x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.61x faster                                                           |
| django_template | 48.2 ms                                                | 36.1 ms: 1.33x faster                                                           |
| genshi_text     | 31.8 ms                                                | 25.4 ms: 1.25x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 58.2 ms: 1.13x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.19x faster                                                            |
| generators               | 80.1 ms                                                | 30.3 ms: 2.65x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.80 ms: 2.08x faster                                                           |
| richards_super           | 94.7 ms                                                | 47.9 ms: 1.98x faster                                                           |
| chaos                    | 115 ms                                                 | 58.9 ms: 1.96x faster                                                           |
| nbody                    | 154 ms                                                 | 80.8 ms: 1.90x faster                                                           |
| richards                 | 79.3 ms                                                | 41.7 ms: 1.90x faster                                                           |
| async_tree_none          | 728 ms                                                 | 384 ms: 1.89x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 62.5 ms: 1.89x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 67.6 ms: 1.89x faster                                                           |
| async_tree_memoization   | 870 ms                                                 | 464 ms: 1.87x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 958 ms: 1.85x faster                                                            |
| raytrace                 | 507 ms                                                 | 284 ms: 1.78x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 518 ms: 1.78x faster                                                            |
| logging_silent           | 190 ns                                                 | 108 ns: 1.76x faster                                                            |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 615 ms: 1.65x faster                                                            |
| float                    | 117 ms                                                 | 71.7 ms: 1.63x faster                                                           |
| go                       | 240 ms                                                 | 148 ms: 1.62x faster                                                            |
| scimark_sor              | 220 ms                                                 | 136 ms: 1.62x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.62x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.62x faster                                                            |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.61x faster                                                           |
| pyflate                  | 716 ms                                                 | 448 ms: 1.60x faster                                                            |
| pylint                   | 551 ms                                                 | 352 ms: 1.57x faster                                                            |
| coroutines               | 35.1 ms                                                | 22.5 ms: 1.56x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.67 ms: 1.56x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.67 ms: 1.54x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                          |
| fannkuch                 | 532 ms                                                 | 356 ms: 1.49x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                                           |
| logging_format           | 9.09 us                                                | 6.20 us: 1.47x faster                                                           |
| deepcopy_memo            | 58.5 us                                                | 39.9 us: 1.47x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                          |
| spectral_norm            | 170 ms                                                 | 118 ms: 1.44x faster                                                            |
| pprint_safe_repr         | 1.02 sec                                               | 705 ms: 1.44x faster                                                            |
| tornado_http             | 136 ms                                                 | 96.6 ms: 1.41x faster                                                           |
| scimark_fft              | 466 ms                                                 | 335 ms: 1.39x faster                                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                                          |
| scimark_lu               | 176 ms                                                 | 128 ms: 1.38x faster                                                            |
| regex_compile            | 188 ms                                                 | 137 ms: 1.38x faster                                                            |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 58.2 ms: 1.36x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.82 ms: 1.34x faster                                                           |
| django_template          | 48.2 ms                                                | 36.1 ms: 1.33x faster                                                           |
| html5lib                 | 88.9 ms                                                | 66.9 ms: 1.33x faster                                                           |
| python_startup           | 14.6 ms                                                | 11.1 ms: 1.32x faster                                                           |
| thrift                   | 1.07 ms                                                | 817 us: 1.31x faster                                                            |
| deepcopy                 | 479 us                                                 | 374 us: 1.28x faster                                                            |
| genshi_text              | 31.8 ms                                                | 25.4 ms: 1.25x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                            |
| 2to3                     | 348 ms                                                 | 279 ms: 1.25x faster                                                            |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.24x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 3.38 us: 1.24x faster                                                           |
| nqueens                  | 106 ms                                                 | 86.7 ms: 1.22x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 69.3 ms: 1.22x faster                                                           |
| xml_etree_generate       | 99.4 ms                                                | 82.0 ms: 1.21x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 57.1 ms: 1.21x faster                                                           |
| dask                     | 441 ms                                                 | 378 ms: 1.17x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 24.1 ms: 1.15x faster                                                           |
| sympy_str                | 346 ms                                                 | 301 ms: 1.15x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 100 ms: 1.15x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 22.5 ms: 1.15x faster                                                           |
| sympy_sum                | 196 ms                                                 | 173 ms: 1.14x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 58.2 ms: 1.13x faster                                                           |
| bench_thread_pool        | 986 us                                                 | 870 us: 1.13x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                          |
| xml_etree_parse          | 168 ms                                                 | 150 ms: 1.12x faster                                                            |
| sympy_expand             | 566 ms                                                 | 509 ms: 1.11x faster                                                            |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                            |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                                           |
| json                     | 5.69 ms                                                | 5.27 ms: 1.08x faster                                                           |
| sqlite_synth             | 3.02 us                                                | 2.90 us: 1.04x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.74 sec: 1.04x faster                                                          |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                            |
| regex_dna                | 227 ms                                                 | 229 ms: 1.01x slower                                                            |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.01x slower                                                            |
| unpickle                 | 14.4 us                                                | 14.7 us: 1.03x slower                                                           |
| pickle_list              | 5.08 us                                                | 5.26 us: 1.04x slower                                                           |
| async_generators         | 444 ms                                                 | 468 ms: 1.05x slower                                                            |
| unpickle_list            | 5.20 us                                                | 5.48 us: 1.05x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.80 ms: 1.11x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 4.04 ms: 1.12x slower                                                           |
| telco                    | 7.27 ms                                                | 8.16 ms: 1.12x slower                                                           |
| pickle                   | 10.7 us                                                | 12.1 us: 1.13x slower                                                           |
| coverage                 | 79.4 ms                                                | 93.8 ms: 1.18x slower                                                           |
| pickle_dict              | 29.6 us                                                | 36.0 us: 1.22x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.59 ms: 1.28x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                                    |

Benchmark hidden because not significant (2): bench_mp_pool, regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240529-3.14.0a0-5386b2d-JIT/bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.21x
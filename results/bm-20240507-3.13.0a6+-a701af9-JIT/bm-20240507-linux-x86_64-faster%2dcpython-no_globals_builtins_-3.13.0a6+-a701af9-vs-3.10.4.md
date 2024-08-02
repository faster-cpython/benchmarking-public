# Results vs. 3.10.4

- fork: faster-cpython
- ref: no_globals_builtins_
- machine: linux-x86_64
- commit hash: a701af9
- commit date: 2024-05-07
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 281 ms: 1.24x faster                                                             |
| chameleon      | 9.68 ms                                                | 7.11 ms: 1.36x faster                                                            |
| docutils       | 3.30 sec                                               | 3.00 sec: 1.10x faster                                                           |
| html5lib       | 88.9 ms                                                | 68.7 ms: 1.29x faster                                                            |
| tornado_http   | 136 ms                                                 | 97.5 ms: 1.40x faster                                                            |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 372 ms: 1.96x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 946 ms: 1.87x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 486 ms: 1.79x faster                                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 633 ms: 1.60x faster                                                             |
| Geometric mean          | (ref)                                                  | 1.80x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.2 ms: 1.89x faster                                                            |
| float          | 117 ms                                                 | 71.7 ms: 1.63x faster                                                            |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                  | 1.47x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 140 ms: 1.34x faster                                                             |
| regex_v8       | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                            |
| regex_dna      | 227 ms                                                 | 228 ms: 1.00x slower                                                             |
| regex_effbot   | 3.63 ms                                                | 3.73 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 301 us: 1.61x faster                                                             |
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                           |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                             |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 58.9 ms: 1.34x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 83.7 ms: 1.19x faster                                                            |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                             |
| xml_etree_parse      | 168 ms                                                 | 154 ms: 1.09x faster                                                             |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                                            |
| pickle_list          | 5.08 us                                                | 5.05 us: 1.01x faster                                                            |
| unpickle_list        | 5.20 us                                                | 5.30 us: 1.02x slower                                                            |
| unpickle             | 14.4 us                                                | 15.7 us: 1.09x slower                                                            |
| pickle_dict          | 29.6 us                                                | 33.1 us: 1.12x slower                                                            |
| pickle               | 10.7 us                                                | 12.0 us: 1.13x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.2 ms: 1.31x faster                                                            |
| python_startup_no_site | 5.93 ms                                                | 7.65 ms: 1.29x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.60 ms: 1.70x faster                                                            |
| django_template | 48.2 ms                                                | 36.9 ms: 1.31x faster                                                            |
| genshi_text     | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 59.0 ms: 1.12x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 174 us: 3.12x faster                                                             |
| generators               | 80.1 ms                                                | 30.3 ms: 2.64x faster                                                            |
| deltablue                | 7.91 ms                                                | 3.76 ms: 2.10x faster                                                            |
| async_tree_none          | 728 ms                                                 | 372 ms: 1.96x faster                                                             |
| chaos                    | 115 ms                                                 | 59.3 ms: 1.95x faster                                                            |
| richards_super           | 94.7 ms                                                | 49.5 ms: 1.92x faster                                                            |
| nbody                    | 154 ms                                                 | 81.2 ms: 1.89x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 68.2 ms: 1.87x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 946 ms: 1.87x faster                                                             |
| scimark_monte_carlo      | 118 ms                                                 | 64.2 ms: 1.84x faster                                                            |
| richards                 | 79.3 ms                                                | 43.1 ms: 1.84x faster                                                            |
| raytrace                 | 507 ms                                                 | 279 ms: 1.82x faster                                                             |
| logging_silent           | 190 ns                                                 | 106 ns: 1.80x faster                                                             |
| async_tree_memoization   | 870 ms                                                 | 486 ms: 1.79x faster                                                             |
| asyncio_tcp              | 922 ms                                                 | 519 ms: 1.77x faster                                                             |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                            |
| mako                     | 16.3 ms                                                | 9.60 ms: 1.70x faster                                                            |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.69x faster                                                             |
| scimark_sor              | 220 ms                                                 | 130 ms: 1.69x faster                                                             |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                            |
| float                    | 117 ms                                                 | 71.7 ms: 1.63x faster                                                            |
| go                       | 240 ms                                                 | 148 ms: 1.62x faster                                                             |
| pickle_pure_python       | 484 us                                                 | 301 us: 1.61x faster                                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 633 ms: 1.60x faster                                                             |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.58 ms: 1.58x faster                                                            |
| pyflate                  | 716 ms                                                 | 453 ms: 1.58x faster                                                             |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.57x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 37.2 us: 1.57x faster                                                            |
| pylint                   | 551 ms                                                 | 357 ms: 1.54x faster                                                             |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                             |
| scimark_fft              | 466 ms                                                 | 316 ms: 1.47x faster                                                             |
| fannkuch                 | 532 ms                                                 | 369 ms: 1.44x faster                                                             |
| logging_simple           | 8.30 us                                                | 5.81 us: 1.43x faster                                                            |
| logging_format           | 9.09 us                                                | 6.40 us: 1.42x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.57 ms: 1.42x faster                                                            |
| scimark_lu               | 176 ms                                                 | 124 ms: 1.41x faster                                                             |
| pprint_safe_repr         | 1.02 sec                                               | 727 ms: 1.40x faster                                                             |
| tornado_http             | 136 ms                                                 | 97.5 ms: 1.40x faster                                                            |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.39x faster                                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.39x faster                                                           |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                            |
| chameleon                | 9.68 ms                                                | 7.11 ms: 1.36x faster                                                            |
| regex_compile            | 188 ms                                                 | 140 ms: 1.34x faster                                                             |
| xml_etree_process        | 79.1 ms                                                | 58.9 ms: 1.34x faster                                                            |
| thrift                   | 1.07 ms                                                | 809 us: 1.32x faster                                                             |
| python_startup           | 14.6 ms                                                | 11.2 ms: 1.31x faster                                                            |
| django_template          | 48.2 ms                                                | 36.9 ms: 1.31x faster                                                            |
| pycparser                | 1.58 sec                                               | 1.21 sec: 1.30x faster                                                           |
| html5lib                 | 88.9 ms                                                | 68.7 ms: 1.29x faster                                                            |
| deepcopy                 | 479 us                                                 | 370 us: 1.29x faster                                                             |
| deepcopy_reduce          | 4.17 us                                                | 3.23 us: 1.29x faster                                                            |
| genshi_text              | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 115 ms: 1.24x faster                                                             |
| 2to3                     | 348 ms                                                 | 281 ms: 1.24x faster                                                             |
| nqueens                  | 106 ms                                                 | 86.7 ms: 1.22x faster                                                            |
| sqlglot_optimize         | 69.2 ms                                                | 56.9 ms: 1.22x faster                                                            |
| dulwich_log              | 84.3 ms                                                | 70.1 ms: 1.20x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 83.7 ms: 1.19x faster                                                            |
| djangocms                | 38.4 us                                                | 32.5 us: 1.18x faster                                                            |
| dask                     | 441 ms                                                 | 380 ms: 1.16x faster                                                             |
| pathlib                  | 20.5 ms                                                | 17.6 ms: 1.16x faster                                                            |
| sympy_str                | 346 ms                                                 | 300 ms: 1.15x faster                                                             |
| aiohttp                  | 1.44 ms                                                | 1.25 ms: 1.15x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                             |
| sympy_sum                | 196 ms                                                 | 173 ms: 1.14x faster                                                             |
| sympy_integrate          | 25.8 ms                                                | 22.7 ms: 1.14x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 869 us: 1.13x faster                                                             |
| gunicorn                 | 1.53 ms                                                | 1.35 ms: 1.13x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 59.0 ms: 1.12x faster                                                            |
| sympy_expand             | 566 ms                                                 | 511 ms: 1.11x faster                                                             |
| docutils                 | 3.30 sec                                               | 3.00 sec: 1.10x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 154 ms: 1.09x faster                                                             |
| mypy2                    | 894 ms                                                 | 820 ms: 1.09x faster                                                             |
| mdp                      | 2.85 sec                                               | 2.61 sec: 1.09x faster                                                           |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                                            |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.08x faster                                                             |
| regex_v8                 | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                            |
| json                     | 5.69 ms                                                | 5.29 ms: 1.08x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.06x faster                                                            |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                             |
| pickle_list              | 5.08 us                                                | 5.05 us: 1.01x faster                                                            |
| regex_dna                | 227 ms                                                 | 228 ms: 1.00x slower                                                             |
| asyncio_websockets       | 559 ms                                                 | 570 ms: 1.02x slower                                                             |
| unpickle_list            | 5.20 us                                                | 5.30 us: 1.02x slower                                                            |
| regex_effbot             | 3.63 ms                                                | 3.73 ms: 1.03x slower                                                            |
| async_generators         | 444 ms                                                 | 465 ms: 1.05x slower                                                             |
| gc_traversal             | 3.62 ms                                                | 3.84 ms: 1.06x slower                                                            |
| flaskblogging            | 8.58 ms                                                | 9.31 ms: 1.09x slower                                                            |
| coverage                 | 79.4 ms                                                | 86.3 ms: 1.09x slower                                                            |
| unpickle                 | 14.4 us                                                | 15.7 us: 1.09x slower                                                            |
| pickle_dict              | 29.6 us                                                | 33.1 us: 1.12x slower                                                            |
| create_gc_cycles         | 1.62 ms                                                | 1.82 ms: 1.13x slower                                                            |
| pickle                   | 10.7 us                                                | 12.0 us: 1.13x slower                                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.65 ms: 1.29x slower                                                            |
| telco                    | 7.27 ms                                                | 172 ms: 23.62x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.28x faster                                                                     |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240507-3.13.0a6+-a701af9-JIT/bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.21x
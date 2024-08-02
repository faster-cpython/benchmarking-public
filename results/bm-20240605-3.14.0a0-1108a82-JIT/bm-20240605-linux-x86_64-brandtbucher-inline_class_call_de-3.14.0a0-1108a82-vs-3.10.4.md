# Results vs. 3.10.4

- fork: brandtbucher
- ref: inline_class_call_de
- machine: linux-x86_64
- commit hash: 1108a82
- commit date: 2024-06-05
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 280 ms: 1.25x faster                                                        |
| docutils       | 3.30 sec                                               | 2.95 sec: 1.12x faster                                                      |
| html5lib       | 88.9 ms                                                | 69.3 ms: 1.28x faster                                                       |
| tornado_http   | 136 ms                                                 | 97.2 ms: 1.40x faster                                                       |
| Geometric mean | (ref)                                                  | 1.26x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 380 ms: 1.92x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 480 ms: 1.81x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 980 ms: 1.80x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 638 ms: 1.59x faster                                                        |
| Geometric mean          | (ref)                                                  | 1.78x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.4 ms: 1.89x faster                                                       |
| float          | 117 ms                                                 | 72.7 ms: 1.61x faster                                                       |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.46x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 137 ms: 1.37x faster                                                        |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                       |
| regex_dna      | 227 ms                                                 | 231 ms: 1.02x slower                                                        |
| regex_effbot   | 3.63 ms                                                | 3.86 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 300 us: 1.62x faster                                                        |
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                        |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 58.5 ms: 1.35x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 82.7 ms: 1.20x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.14x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 150 ms: 1.12x faster                                                        |
| json_loads           | 31.2 us                                                | 29.4 us: 1.06x faster                                                       |
| unpickle_list        | 5.20 us                                                | 5.40 us: 1.04x slower                                                       |
| pickle_list          | 5.08 us                                                | 5.34 us: 1.05x slower                                                       |
| unpickle             | 14.4 us                                                | 15.2 us: 1.06x slower                                                       |
| pickle               | 10.7 us                                                | 12.2 us: 1.14x slower                                                       |
| pickle_dict          | 29.6 us                                                | 35.1 us: 1.19x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.2 ms: 1.30x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.63 ms: 1.29x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                       |
| django_template | 48.2 ms                                                | 36.6 ms: 1.31x faster                                                       |
| genshi_text     | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 58.9 ms: 1.12x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 174 us: 3.12x faster                                                        |
| generators               | 80.1 ms                                                | 30.6 ms: 2.61x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.75 ms: 2.11x faster                                                       |
| richards_super           | 94.7 ms                                                | 48.5 ms: 1.95x faster                                                       |
| async_tree_none          | 728 ms                                                 | 380 ms: 1.92x faster                                                        |
| chaos                    | 115 ms                                                 | 60.3 ms: 1.91x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 67.4 ms: 1.90x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 62.6 ms: 1.89x faster                                                       |
| nbody                    | 154 ms                                                 | 81.4 ms: 1.89x faster                                                       |
| richards                 | 79.3 ms                                                | 42.2 ms: 1.88x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 480 ms: 1.81x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 980 ms: 1.80x faster                                                        |
| raytrace                 | 507 ms                                                 | 283 ms: 1.79x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 519 ms: 1.78x faster                                                        |
| logging_silent           | 190 ns                                                 | 107 ns: 1.77x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                       |
| scimark_sor              | 220 ms                                                 | 133 ms: 1.66x faster                                                        |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.64x faster                                                        |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.62x faster                                                        |
| go                       | 240 ms                                                 | 149 ms: 1.61x faster                                                        |
| float                    | 117 ms                                                 | 72.7 ms: 1.61x faster                                                       |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 638 ms: 1.59x faster                                                        |
| pylint                   | 551 ms                                                 | 352 ms: 1.57x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.65 ms: 1.56x faster                                                       |
| pyflate                  | 716 ms                                                 | 460 ms: 1.56x faster                                                        |
| hexiom                   | 10.4 ms                                                | 6.70 ms: 1.55x faster                                                       |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.54x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 38.1 us: 1.53x faster                                                       |
| fannkuch                 | 532 ms                                                 | 355 ms: 1.50x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.33 ms: 1.50x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                        |
| scimark_fft              | 466 ms                                                 | 314 ms: 1.49x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 701 ms: 1.45x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.74 us: 1.45x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                      |
| logging_format           | 9.09 us                                                | 6.44 us: 1.41x faster                                                       |
| tornado_http             | 136 ms                                                 | 97.2 ms: 1.40x faster                                                       |
| scimark_lu               | 176 ms                                                 | 127 ms: 1.39x faster                                                        |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                                      |
| regex_compile            | 188 ms                                                 | 137 ms: 1.37x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 58.5 ms: 1.35x faster                                                       |
| thrift                   | 1.07 ms                                                | 813 us: 1.32x faster                                                        |
| django_template          | 48.2 ms                                                | 36.6 ms: 1.31x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.21 sec: 1.31x faster                                                      |
| python_startup           | 14.6 ms                                                | 11.2 ms: 1.30x faster                                                       |
| html5lib                 | 88.9 ms                                                | 69.3 ms: 1.28x faster                                                       |
| genshi_text              | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                       |
| deepcopy                 | 479 us                                                 | 379 us: 1.26x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 3.32 us: 1.25x faster                                                       |
| 2to3                     | 348 ms                                                 | 280 ms: 1.25x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 68.5 ms: 1.23x faster                                                       |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.23x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 57.0 ms: 1.21x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 82.7 ms: 1.20x faster                                                       |
| nqueens                  | 106 ms                                                 | 88.1 ms: 1.20x faster                                                       |
| dask                     | 441 ms                                                 | 379 ms: 1.16x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 22.5 ms: 1.15x faster                                                       |
| sympy_sum                | 196 ms                                                 | 172 ms: 1.15x faster                                                        |
| sympy_str                | 346 ms                                                 | 302 ms: 1.15x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.14x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 875 us: 1.13x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 58.9 ms: 1.12x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 150 ms: 1.12x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.95 sec: 1.12x faster                                                      |
| sympy_expand             | 566 ms                                                 | 510 ms: 1.11x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                       |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.58 sec: 1.10x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.07x faster                                                       |
| json                     | 5.69 ms                                                | 5.34 ms: 1.07x faster                                                       |
| json_loads               | 31.2 us                                                | 29.4 us: 1.06x faster                                                       |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                        |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.02x slower                                                        |
| regex_dna                | 227 ms                                                 | 231 ms: 1.02x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 3.76 ms: 1.04x slower                                                       |
| unpickle_list            | 5.20 us                                                | 5.40 us: 1.04x slower                                                       |
| async_generators         | 444 ms                                                 | 466 ms: 1.05x slower                                                        |
| pickle_list              | 5.08 us                                                | 5.34 us: 1.05x slower                                                       |
| unpickle                 | 14.4 us                                                | 15.2 us: 1.06x slower                                                       |
| regex_effbot             | 3.63 ms                                                | 3.86 ms: 1.06x slower                                                       |
| telco                    | 7.27 ms                                                | 8.05 ms: 1.11x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.80 ms: 1.11x slower                                                       |
| pickle                   | 10.7 us                                                | 12.2 us: 1.14x slower                                                       |
| coverage                 | 79.4 ms                                                | 93.4 ms: 1.18x slower                                                       |
| pickle_dict              | 29.6 us                                                | 35.1 us: 1.19x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.63 ms: 1.29x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240605-3.14.0a0-1108a82-JIT/bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.21x
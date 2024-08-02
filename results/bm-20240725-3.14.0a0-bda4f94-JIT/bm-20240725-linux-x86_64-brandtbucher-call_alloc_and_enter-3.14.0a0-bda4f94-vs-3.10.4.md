# Results vs. 3.10.4

- fork: brandtbucher
- ref: call_alloc_and_enter
- machine: linux-x86_64
- commit hash: bda4f94
- commit date: 2024-07-25
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 271 ms: 1.29x faster                                                        |
| docutils       | 3.30 sec                                               | 2.89 sec: 1.14x faster                                                      |
| html5lib       | 88.9 ms                                                | 65.8 ms: 1.35x faster                                                       |
| tornado_http   | 136 ms                                                 | 92.3 ms: 1.48x faster                                                       |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 327 ms: 2.23x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 399 ms: 2.18x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 898 ms: 1.97x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 562 ms: 1.81x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.04x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.9 ms: 1.92x faster                                                       |
| float          | 117 ms                                                 | 70.6 ms: 1.66x faster                                                       |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.49x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 132 ms: 1.42x faster                                                        |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                       |
| regex_dna      | 227 ms                                                 | 231 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 297 us: 1.63x faster                                                        |
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 55.9 ms: 1.41x faster                                                       |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 79.7 ms: 1.25x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 98.5 ms: 1.17x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.13x faster                                                        |
| json_loads           | 31.2 us                                                | 27.6 us: 1.13x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.15 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.85 ms: 1.66x faster                                                       |
| django_template | 48.2 ms                                                | 35.5 ms: 1.36x faster                                                       |
| genshi_text     | 31.8 ms                                                | 24.8 ms: 1.29x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 59.0 ms: 1.12x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.24x faster                                                        |
| generators               | 80.1 ms                                                | 28.6 ms: 2.80x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.51 ms: 2.26x faster                                                       |
| async_tree_none          | 728 ms                                                 | 327 ms: 2.23x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 399 ms: 2.18x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 28.6 us: 2.04x faster                                                       |
| richards_super           | 94.7 ms                                                | 46.9 ms: 2.02x faster                                                       |
| chaos                    | 115 ms                                                 | 58.4 ms: 1.98x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 898 ms: 1.97x faster                                                        |
| richards                 | 79.3 ms                                                | 40.5 ms: 1.96x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 60.7 ms: 1.95x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 66.3 ms: 1.93x faster                                                       |
| nbody                    | 154 ms                                                 | 79.9 ms: 1.92x faster                                                       |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 486 ms: 1.90x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 562 ms: 1.81x faster                                                        |
| deepcopy                 | 479 us                                                 | 269 us: 1.78x faster                                                        |
| logging_silent           | 190 ns                                                 | 107 ns: 1.77x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                       |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.71x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                       |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.70x faster                                                        |
| go                       | 240 ms                                                 | 144 ms: 1.66x faster                                                        |
| float                    | 117 ms                                                 | 70.6 ms: 1.66x faster                                                       |
| mako                     | 16.3 ms                                                | 9.85 ms: 1.66x faster                                                       |
| pyflate                  | 716 ms                                                 | 433 ms: 1.65x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 297 us: 1.63x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                       |
| hexiom                   | 10.4 ms                                                | 6.53 ms: 1.59x faster                                                       |
| pylint                   | 551 ms                                                 | 347 ms: 1.59x faster                                                        |
| coroutines               | 35.1 ms                                                | 22.4 ms: 1.56x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.29 ms: 1.51x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.77 us: 1.50x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.53 us: 1.50x faster                                                       |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                                        |
| logging_format           | 9.09 us                                                | 6.09 us: 1.49x faster                                                       |
| tornado_http             | 136 ms                                                 | 92.3 ms: 1.48x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.43x faster                                                      |
| regex_compile            | 188 ms                                                 | 132 ms: 1.42x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 716 ms: 1.42x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 55.9 ms: 1.41x faster                                                       |
| fannkuch                 | 532 ms                                                 | 377 ms: 1.41x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                                      |
| scimark_lu               | 176 ms                                                 | 127 ms: 1.38x faster                                                        |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                       |
| thrift                   | 1.07 ms                                                | 782 us: 1.37x faster                                                        |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                       |
| django_template          | 48.2 ms                                                | 35.5 ms: 1.36x faster                                                       |
| html5lib                 | 88.9 ms                                                | 65.8 ms: 1.35x faster                                                       |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                       |
| 2to3                     | 348 ms                                                 | 271 ms: 1.29x faster                                                        |
| genshi_text              | 31.8 ms                                                | 24.8 ms: 1.29x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 79.7 ms: 1.25x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 55.9 ms: 1.24x faster                                                       |
| nqueens                  | 106 ms                                                 | 86.0 ms: 1.23x faster                                                       |
| dask                     | 441 ms                                                 | 366 ms: 1.21x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 824 us: 1.20x faster                                                        |
| sympy_str                | 346 ms                                                 | 294 ms: 1.18x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 98.5 ms: 1.17x faster                                                       |
| sympy_sum                | 196 ms                                                 | 169 ms: 1.16x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 22.2 ms: 1.16x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                       |
| docutils                 | 3.30 sec                                               | 2.89 sec: 1.14x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.13x faster                                                        |
| sympy_expand             | 566 ms                                                 | 499 ms: 1.13x faster                                                        |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                        |
| json_loads               | 31.2 us                                                | 27.6 us: 1.13x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 59.0 ms: 1.12x faster                                                       |
| json                     | 5.69 ms                                                | 5.14 ms: 1.11x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.71 sec: 1.05x faster                                                      |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                        |
| gc_traversal             | 3.62 ms                                                | 3.56 ms: 1.02x faster                                                       |
| regex_dna                | 227 ms                                                 | 231 ms: 1.02x slower                                                        |
| async_generators         | 444 ms                                                 | 455 ms: 1.03x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                                       |
| telco                    | 7.27 ms                                                | 7.83 ms: 1.08x slower                                                       |
| coverage                 | 79.4 ms                                                | 91.6 ms: 1.15x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.15 ms: 1.21x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                |

Benchmark hidden because not significant (3): asyncio_websockets, bench_mp_pool, regex_effbot
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240725-3.14.0a0-bda4f94-JIT/bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.19x
# Results vs. 3.10.4

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 091375e
- commit date: 2024-07-03
- overall geometric mean: 1.40x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 279 ms: 1.25x faster                                             |
| docutils       | 3.30 sec                                               | 3.01 sec: 1.09x faster                                           |
| html5lib       | 88.9 ms                                                | 68.3 ms: 1.30x faster                                            |
| tornado_http   | 136 ms                                                 | 97.7 ms: 1.40x faster                                            |
| Geometric mean | (ref)                                                  | 1.25x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.23x faster                                             |
| async_tree_memoization  | 870 ms                                                 | 412 ms: 2.11x faster                                             |
| async_tree_io           | 1.77 sec                                               | 870 ms: 2.03x faster                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 571 ms: 1.78x faster                                             |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.9 ms: 1.92x faster                                            |
| float          | 117 ms                                                 | 70.2 ms: 1.67x faster                                            |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.49x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 138 ms: 1.37x faster                                             |
| regex_v8       | 27.8 ms                                                | 24.3 ms: 1.14x faster                                            |
| regex_dna      | 227 ms                                                 | 230 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                  | 1.12x faster                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 200 us: 1.65x faster                                             |
| pickle_pure_python   | 484 us                                                 | 297 us: 1.63x faster                                             |
| tomli_loads          | 3.14 sec                                               | 2.03 sec: 1.55x faster                                           |
| xml_etree_process    | 79.1 ms                                                | 57.5 ms: 1.38x faster                                            |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                            |
| xml_etree_generate   | 99.4 ms                                                | 80.9 ms: 1.23x faster                                            |
| xml_etree_iterparse  | 115 ms                                                 | 99.3 ms: 1.16x faster                                            |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                             |
| json_loads           | 31.2 us                                                | 27.3 us: 1.14x faster                                            |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                            |
| python_startup_no_site | 5.93 ms                                                | 7.13 ms: 1.20x slower                                            |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.86 ms: 1.66x faster                                            |
| genshi_text     | 31.8 ms                                                | 24.1 ms: 1.32x faster                                            |
| django_template | 48.2 ms                                                | 36.6 ms: 1.32x faster                                            |
| genshi_xml      | 66.0 ms                                                | 62.6 ms: 1.06x faster                                            |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.17x faster                                             |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.23x faster                                             |
| async_tree_memoization   | 870 ms                                                 | 412 ms: 2.11x faster                                             |
| deepcopy_memo            | 58.5 us                                                | 28.4 us: 2.06x faster                                            |
| scimark_monte_carlo      | 118 ms                                                 | 57.4 ms: 2.06x faster                                            |
| async_tree_io            | 1.77 sec                                               | 870 ms: 2.03x faster                                             |
| chaos                    | 115 ms                                                 | 59.8 ms: 1.93x faster                                            |
| deltablue                | 7.91 ms                                                | 4.10 ms: 1.93x faster                                            |
| logging_silent           | 190 ns                                                 | 98.4 ns: 1.93x faster                                            |
| nbody                    | 154 ms                                                 | 79.9 ms: 1.92x faster                                            |
| crypto_pyaes             | 128 ms                                                 | 66.9 ms: 1.91x faster                                            |
| richards_super           | 94.7 ms                                                | 49.7 ms: 1.91x faster                                            |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                             |
| asyncio_tcp              | 922 ms                                                 | 508 ms: 1.82x faster                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 571 ms: 1.78x faster                                             |
| richards                 | 79.3 ms                                                | 44.6 ms: 1.78x faster                                            |
| deepcopy                 | 479 us                                                 | 274 us: 1.75x faster                                             |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.69x faster                                            |
| go                       | 240 ms                                                 | 143 ms: 1.68x faster                                             |
| pyflate                  | 716 ms                                                 | 427 ms: 1.68x faster                                             |
| float                    | 117 ms                                                 | 70.2 ms: 1.67x faster                                            |
| scimark_sor              | 220 ms                                                 | 132 ms: 1.67x faster                                             |
| mako                     | 16.3 ms                                                | 9.86 ms: 1.66x faster                                            |
| generators               | 80.1 ms                                                | 48.4 ms: 1.66x faster                                            |
| unpickle_pure_python     | 331 us                                                 | 200 us: 1.65x faster                                             |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                             |
| pickle_pure_python       | 484 us                                                 | 297 us: 1.63x faster                                             |
| hexiom                   | 10.4 ms                                                | 6.59 ms: 1.58x faster                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.57x faster                                            |
| tomli_loads              | 3.14 sec                                               | 2.03 sec: 1.55x faster                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                            |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.52x faster                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.30 ms: 1.50x faster                                            |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                             |
| logging_simple           | 8.30 us                                                | 5.59 us: 1.49x faster                                            |
| fannkuch                 | 532 ms                                                 | 362 ms: 1.47x faster                                             |
| logging_format           | 9.09 us                                                | 6.27 us: 1.45x faster                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                           |
| scimark_lu               | 176 ms                                                 | 124 ms: 1.42x faster                                             |
| tornado_http             | 136 ms                                                 | 97.7 ms: 1.40x faster                                            |
| pylint                   | 551 ms                                                 | 397 ms: 1.39x faster                                             |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                            |
| pprint_safe_repr         | 1.02 sec                                               | 739 ms: 1.38x faster                                             |
| xml_etree_process        | 79.1 ms                                                | 57.5 ms: 1.38x faster                                            |
| regex_compile            | 188 ms                                                 | 138 ms: 1.37x faster                                             |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                            |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                           |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                           |
| thrift                   | 1.07 ms                                                | 802 us: 1.34x faster                                             |
| genshi_text              | 31.8 ms                                                | 24.1 ms: 1.32x faster                                            |
| django_template          | 48.2 ms                                                | 36.6 ms: 1.32x faster                                            |
| html5lib                 | 88.9 ms                                                | 68.3 ms: 1.30x faster                                            |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                            |
| 2to3                     | 348 ms                                                 | 279 ms: 1.25x faster                                             |
| nqueens                  | 106 ms                                                 | 85.4 ms: 1.24x faster                                            |
| xml_etree_generate       | 99.4 ms                                                | 80.9 ms: 1.23x faster                                            |
| sqlglot_normalize        | 143 ms                                                 | 119 ms: 1.20x faster                                             |
| sqlglot_optimize         | 69.2 ms                                                | 57.6 ms: 1.20x faster                                            |
| dask                     | 441 ms                                                 | 369 ms: 1.19x faster                                             |
| bench_thread_pool        | 986 us                                                 | 837 us: 1.18x faster                                             |
| dulwich_log              | 84.3 ms                                                | 71.8 ms: 1.17x faster                                            |
| xml_etree_iterparse      | 115 ms                                                 | 99.3 ms: 1.16x faster                                            |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                             |
| json_loads               | 31.2 us                                                | 27.3 us: 1.14x faster                                            |
| regex_v8                 | 27.8 ms                                                | 24.3 ms: 1.14x faster                                            |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                             |
| sympy_str                | 346 ms                                                 | 309 ms: 1.12x faster                                             |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                           |
| sympy_integrate          | 25.8 ms                                                | 23.2 ms: 1.11x faster                                            |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                            |
| sympy_sum                | 196 ms                                                 | 178 ms: 1.10x faster                                             |
| docutils                 | 3.30 sec                                               | 3.01 sec: 1.09x faster                                           |
| sympy_expand             | 566 ms                                                 | 517 ms: 1.09x faster                                             |
| genshi_xml               | 66.0 ms                                                | 62.6 ms: 1.06x faster                                            |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                             |
| regex_dna                | 227 ms                                                 | 230 ms: 1.02x slower                                             |
| async_generators         | 444 ms                                                 | 460 ms: 1.04x slower                                             |
| gc_traversal             | 3.62 ms                                                | 3.85 ms: 1.06x slower                                            |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                            |
| telco                    | 7.27 ms                                                | 7.97 ms: 1.10x slower                                            |
| coverage                 | 79.4 ms                                                | 92.4 ms: 1.16x slower                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.13 ms: 1.20x slower                                            |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                     |

Benchmark hidden because not significant (3): regex_effbot, bench_mp_pool, asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240703-3.14.0a0-091375e-JIT/bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.19x
# Results vs. 3.10.4

- fork: python
- ref: a852c7bdd48979218a0c
- machine: linux-aarch64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.288x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 310 ms: 1.23x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.12 sec: 1.13x faster                                                  |
| html5lib       | 86.5 ms                                                               | 63.6 ms: 1.36x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 883 ms: 2.59x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 466 ms: 2.43x faster                                                    |
| async_tree_none         | 950 ms                                                                | 392 ms: 2.42x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 652 ms: 1.95x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.33x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 82.5 ms: 1.63x faster                                                   |
| nbody          | 166 ms                                                                | 129 ms: 1.29x faster                                                    |
| pidigits       | 235 ms                                                                | 237 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 121 ms: 1.46x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 26.4 ms: 1.22x faster                                                   |
| regex_dna      | 257 ms                                                                | 216 ms: 1.19x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.77 ms: 1.13x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 251 us: 1.46x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.32 sec: 1.45x faster                                                  |
| pickle_pure_python   | 529 us                                                                | 392 us: 1.35x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 78.4 ms: 1.27x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.8 ms: 1.21x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 177 ms: 1.19x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 144 ms: 1.09x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.53 us: 1.07x faster                                                   |
| unpickle             | 17.5 us                                                               | 18.6 us: 1.06x slower                                                   |
| json_loads           | 30.9 us                                                               | 33.1 us: 1.07x slower                                                   |
| pickle_list          | 5.24 us                                                               | 5.71 us: 1.09x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 38.4 us: 1.09x slower                                                   |
| pickle               | 12.5 us                                                               | 15.6 us: 1.25x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.69 ms: 1.26x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.9 ms: 1.47x faster                                                   |
| django_template | 53.3 ms                                                               | 39.2 ms: 1.36x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.6 ms: 1.28x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 64.1 ms: 1.09x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.29x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 205 us: 3.22x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 883 ms: 2.59x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 466 ms: 2.43x faster                                                    |
| async_tree_none          | 950 ms                                                                | 392 ms: 2.42x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.83 ms: 2.34x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.62 sec: 2.28x faster                                                  |
| richards_super           | 107 ms                                                                | 50.8 ms: 2.11x faster                                                   |
| richards                 | 91.7 ms                                                               | 44.3 ms: 2.07x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 652 ms: 1.95x faster                                                    |
| generators               | 68.1 ms                                                               | 37.1 ms: 1.84x faster                                                   |
| raytrace                 | 573 ms                                                                | 329 ms: 1.74x faster                                                    |
| chaos                    | 121 ms                                                                | 69.7 ms: 1.74x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 546 ms: 1.73x faster                                                    |
| logging_silent           | 222 ns                                                                | 129 ns: 1.72x faster                                                    |
| go                       | 264 ms                                                                | 154 ms: 1.72x faster                                                    |
| scimark_sor              | 246 ms                                                                | 145 ms: 1.70x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.0 us: 1.67x faster                                                   |
| float                    | 135 ms                                                                | 82.5 ms: 1.63x faster                                                   |
| spectral_norm            | 186 ms                                                                | 116 ms: 1.61x faster                                                    |
| deepcopy                 | 511 us                                                                | 321 us: 1.59x faster                                                    |
| comprehensions           | 33.1 us                                                               | 21.5 us: 1.54x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 84.3 ms: 1.52x faster                                                   |
| scimark_lu               | 227 ms                                                                | 150 ms: 1.51x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.20 sec: 1.49x faster                                                  |
| pylint                   | 485 ms                                                                | 328 ms: 1.48x faster                                                    |
| mako                     | 18.9 ms                                                               | 12.9 ms: 1.47x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.44 ms: 1.47x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 91.5 ms: 1.47x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 251 us: 1.46x faster                                                    |
| regex_compile            | 177 ms                                                                | 121 ms: 1.46x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.32 sec: 1.45x faster                                                  |
| pyflate                  | 795 ms                                                                | 553 ms: 1.44x faster                                                    |
| logging_simple           | 9.78 us                                                               | 6.95 us: 1.41x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.58 us: 1.40x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 53.7 ms: 1.37x faster                                                   |
| django_template          | 53.3 ms                                                               | 39.2 ms: 1.36x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 63.6 ms: 1.36x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 392 us: 1.35x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.52 us: 1.31x faster                                                   |
| thrift                   | 1.26 ms                                                               | 973 us: 1.29x faster                                                    |
| nbody                    | 166 ms                                                                | 129 ms: 1.29x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.8 ms: 1.28x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.6 ms: 1.28x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.33 sec: 1.27x faster                                                  |
| xml_etree_process        | 99.5 ms                                                               | 78.4 ms: 1.27x faster                                                   |
| sympy_sum                | 184 ms                                                                | 150 ms: 1.23x faster                                                    |
| 2to3                     | 381 ms                                                                | 310 ms: 1.23x faster                                                    |
| scimark_fft              | 500 ms                                                                | 408 ms: 1.23x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 26.4 ms: 1.22x faster                                                   |
| coroutines               | 37.2 ms                                                               | 30.6 ms: 1.22x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.8 ms: 1.21x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 177 ms: 1.19x faster                                                    |
| regex_dna                | 257 ms                                                                | 216 ms: 1.19x faster                                                    |
| sympy_str                | 329 ms                                                                | 276 ms: 1.19x faster                                                    |
| fannkuch                 | 546 ms                                                                | 461 ms: 1.18x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.38 ms: 1.16x faster                                                   |
| nqueens                  | 117 ms                                                                | 102 ms: 1.15x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 23.1 ms: 1.14x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.12 sec: 1.13x faster                                                  |
| regex_effbot             | 4.25 ms                                                               | 3.77 ms: 1.13x faster                                                   |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.11x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.10x faster                                                    |
| sympy_expand             | 543 ms                                                                | 494 ms: 1.10x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.77 us: 1.09x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 64.1 ms: 1.09x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 144 ms: 1.09x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.53 us: 1.07x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.16 ms: 1.07x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.29 sec: 1.03x faster                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 1.13 sec: 1.02x faster                                                  |
| json                     | 5.88 ms                                                               | 5.77 ms: 1.02x faster                                                   |
| pidigits                 | 235 ms                                                                | 237 ms: 1.01x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 668 ms: 1.02x slower                                                    |
| async_generators         | 452 ms                                                                | 478 ms: 1.06x slower                                                    |
| unpickle                 | 17.5 us                                                               | 18.6 us: 1.06x slower                                                   |
| json_loads               | 30.9 us                                                               | 33.1 us: 1.07x slower                                                   |
| pickle_list              | 5.24 us                                                               | 5.71 us: 1.09x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 38.4 us: 1.09x slower                                                   |
| coverage                 | 83.6 ms                                                               | 103 ms: 1.23x slower                                                    |
| pickle                   | 12.5 us                                                               | 15.6 us: 1.25x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.69 ms: 1.26x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.80 ms: 1.64x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.96 ms: 1.75x slower                                                   |
| telco                    | 8.49 ms                                                               | 164 ms: 19.38x slower                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 1.27 sec: 87.26x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.20x faster                                                            |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.288x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.41x
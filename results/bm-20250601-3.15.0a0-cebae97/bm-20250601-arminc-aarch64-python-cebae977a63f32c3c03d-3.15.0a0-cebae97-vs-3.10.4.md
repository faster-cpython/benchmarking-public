# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-aarch64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.035x slower
- HPT reliability: 98.32%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 356 ms: 1.07x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.45 sec: 1.02x faster                                                  |
| html5lib       | 86.5 ms                                                               | 67.3 ms: 1.29x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 987 ms: 2.32x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 525 ms: 2.16x faster                                                    |
| async_tree_none         | 950 ms                                                                | 441 ms: 2.15x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 808 ms: 1.57x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.03x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 96.5 ms: 1.40x faster                                                   |
| nbody          | 166 ms                                                                | 144 ms: 1.15x faster                                                    |
| pidigits       | 235 ms                                                                | 277 ms: 1.18x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 226 ms: 1.14x faster                                                    |
| regex_compile  | 177 ms                                                                | 158 ms: 1.11x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.1 ms: 1.07x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.08 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.93 sec: 1.15x faster                                                  |
| pickle_pure_python   | 529 us                                                                | 474 us: 1.12x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 328 us: 1.11x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 17.2 ms: 1.03x slower                                                   |
| xml_etree_iterparse  | 156 ms                                                                | 167 ms: 1.07x slower                                                    |
| xml_etree_parse      | 212 ms                                                                | 229 ms: 1.08x slower                                                    |
| xml_etree_process    | 99.5 ms                                                               | 108 ms: 1.08x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 42.6 us: 1.21x slower                                                   |
| json_loads           | 30.9 us                                                               | 38.0 us: 1.23x slower                                                   |
| unpickle             | 17.5 us                                                               | 22.6 us: 1.29x slower                                                   |
| xml_etree_generate   | 123 ms                                                                | 161 ms: 1.31x slower                                                    |
| pickle_list          | 5.24 us                                                               | 7.06 us: 1.35x slower                                                   |
| pickle               | 12.5 us                                                               | 19.7 us: 1.58x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.12x slower                                                            |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.71 ms: 1.41x slower                                                   |
| python_startup         | 11.2 ms                                                               | 17.2 ms: 1.53x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.47x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 17.9 ms: 1.06x faster                                                   |
| django_template | 53.3 ms                                                               | 52.5 ms: 1.02x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 74.7 ms: 1.07x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 260 us: 2.54x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 987 ms: 2.32x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 525 ms: 2.16x faster                                                    |
| async_tree_none          | 950 ms                                                                | 441 ms: 2.15x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.54 ms: 1.97x faster                                                   |
| go                       | 264 ms                                                                | 141 ms: 1.88x faster                                                    |
| mdp                      | 3.70 sec                                                              | 2.01 sec: 1.84x faster                                                  |
| generators               | 68.1 ms                                                               | 39.6 ms: 1.72x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 556 ms: 1.70x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 808 ms: 1.57x faster                                                    |
| richards_super           | 107 ms                                                                | 71.2 ms: 1.51x faster                                                   |
| raytrace                 | 573 ms                                                                | 390 ms: 1.47x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.25 sec: 1.46x faster                                                  |
| richards                 | 91.7 ms                                                               | 62.9 ms: 1.46x faster                                                   |
| chaos                    | 121 ms                                                                | 83.8 ms: 1.45x faster                                                   |
| comprehensions           | 33.1 us                                                               | 23.1 us: 1.43x faster                                                   |
| scimark_sor              | 246 ms                                                                | 173 ms: 1.42x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 43.7 us: 1.41x faster                                                   |
| float                    | 135 ms                                                                | 96.5 ms: 1.40x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 94.8 ms: 1.35x faster                                                   |
| pyflate                  | 795 ms                                                                | 590 ms: 1.35x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 8.37 ms: 1.30x faster                                                   |
| pylint                   | 485 ms                                                                | 374 ms: 1.30x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 67.3 ms: 1.29x faster                                                   |
| deepcopy                 | 511 us                                                                | 401 us: 1.27x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 105 ms: 1.27x faster                                                    |
| spectral_norm            | 186 ms                                                                | 151 ms: 1.24x faster                                                    |
| scimark_lu               | 227 ms                                                                | 184 ms: 1.23x faster                                                    |
| nbody                    | 166 ms                                                                | 144 ms: 1.15x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.93 sec: 1.15x faster                                                  |
| regex_dna                | 257 ms                                                                | 226 ms: 1.14x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.49 sec: 1.13x faster                                                  |
| coroutines               | 37.2 ms                                                               | 33.1 ms: 1.12x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 65.6 ms: 1.12x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 474 us: 1.12x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 328 us: 1.11x faster                                                    |
| regex_compile            | 177 ms                                                                | 158 ms: 1.11x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 23.9 ms: 1.11x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.48 ms: 1.08x faster                                                   |
| 2to3                     | 381 ms                                                                | 356 ms: 1.07x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.1 ms: 1.07x faster                                                   |
| mako                     | 18.9 ms                                                               | 17.9 ms: 1.06x faster                                                   |
| logging_simple           | 9.78 us                                                               | 9.31 us: 1.05x faster                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.08 ms: 1.04x faster                                                   |
| sympy_sum                | 184 ms                                                                | 178 ms: 1.04x faster                                                    |
| logging_format           | 10.6 us                                                               | 10.3 us: 1.03x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.45 sec: 1.02x faster                                                  |
| django_template          | 53.3 ms                                                               | 52.5 ms: 1.02x faster                                                   |
| meteor_contest           | 126 ms                                                                | 127 ms: 1.01x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 670 ms: 1.02x slower                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.78 ms: 1.02x slower                                                   |
| pathlib                  | 26.3 ms                                                               | 26.9 ms: 1.02x slower                                                   |
| json_dumps               | 16.7 ms                                                               | 17.2 ms: 1.03x slower                                                   |
| sympy_str                | 329 ms                                                                | 339 ms: 1.03x slower                                                    |
| nqueens                  | 117 ms                                                                | 125 ms: 1.07x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 74.7 ms: 1.07x slower                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 167 ms: 1.07x slower                                                    |
| xml_etree_parse          | 212 ms                                                                | 229 ms: 1.08x slower                                                    |
| xml_etree_process        | 99.5 ms                                                               | 108 ms: 1.08x slower                                                    |
| fannkuch                 | 546 ms                                                                | 596 ms: 1.09x slower                                                    |
| sympy_expand             | 543 ms                                                                | 599 ms: 1.10x slower                                                    |
| async_generators         | 452 ms                                                                | 521 ms: 1.15x slower                                                    |
| sqlite_synth             | 4.12 us                                                               | 4.81 us: 1.17x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.76 sec: 1.17x slower                                                  |
| pidigits                 | 235 ms                                                                | 277 ms: 1.18x slower                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.35 sec: 1.18x slower                                                  |
| json                     | 5.88 ms                                                               | 6.95 ms: 1.18x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 42.6 us: 1.21x slower                                                   |
| json_loads               | 30.9 us                                                               | 38.0 us: 1.23x slower                                                   |
| unpickle                 | 17.5 us                                                               | 22.6 us: 1.29x slower                                                   |
| xml_etree_generate       | 123 ms                                                                | 161 ms: 1.31x slower                                                    |
| pickle_list              | 5.24 us                                                               | 7.06 us: 1.35x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 9.71 ms: 1.41x slower                                                   |
| python_startup           | 11.2 ms                                                               | 17.2 ms: 1.53x slower                                                   |
| telco                    | 8.49 ms                                                               | 13.2 ms: 1.56x slower                                                   |
| pickle                   | 12.5 us                                                               | 19.7 us: 1.58x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.97 ms: 1.76x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 7.69 ms: 1.85x slower                                                   |
| logging_silent           | 222 ns                                                                | 914 ns: 4.12x slower                                                    |
| coverage                 | 83.6 ms                                                               | 739 ms: 8.84x slower                                                    |
| thrift                   | 1.26 ms                                                               | 199 ms: 158.09x slower                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 5.59 sec: 384.43x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.08x slower                                                            |

Benchmark hidden because not significant (4): genshi_text, unpickle_list, scimark_fft, deepcopy_reduce
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.035x slower

# HPT report

- Reliability score: 98.32% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.39x
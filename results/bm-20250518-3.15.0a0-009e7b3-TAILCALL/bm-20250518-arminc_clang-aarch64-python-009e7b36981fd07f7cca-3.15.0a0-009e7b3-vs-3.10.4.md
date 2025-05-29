# Results vs. 3.10.4

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: linux-aarch64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.226x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 301 ms: 1.26x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                  |
| html5lib       | 86.5 ms                                                               | 60.6 ms: 1.43x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 866 ms: 2.64x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 454 ms: 2.50x faster                                                    |
| async_tree_none         | 950 ms                                                                | 384 ms: 2.47x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 721 ms: 1.77x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 87.0 ms: 1.55x faster                                                   |
| nbody          | 166 ms                                                                | 128 ms: 1.29x faster                                                    |
| pidigits       | 235 ms                                                                | 292 ms: 1.24x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.17x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 120 ms: 1.47x faster                                                    |
| regex_dna      | 257 ms                                                                | 246 ms: 1.04x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.50 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 254 us: 1.44x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.41 sec: 1.40x faster                                                  |
| pickle_pure_python   | 529 us                                                                | 400 us: 1.32x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 75.9 ms: 1.31x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                                   |
| unpickle_list        | 6.99 us                                                               | 5.79 us: 1.21x faster                                                   |
| xml_etree_generate   | 123 ms                                                                | 108 ms: 1.14x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.06x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 204 ms: 1.04x faster                                                    |
| unpickle             | 17.5 us                                                               | 17.1 us: 1.02x faster                                                   |
| pickle_list          | 5.24 us                                                               | 5.38 us: 1.03x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 37.1 us: 1.06x slower                                                   |
| json_loads           | 30.9 us                                                               | 34.2 us: 1.10x slower                                                   |
| pickle               | 12.5 us                                                               | 15.1 us: 1.21x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.12x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.83 ms: 1.28x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.3 ms: 1.37x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 38.9 ms: 1.37x faster                                                   |
| mako            | 18.9 ms                                                               | 14.3 ms: 1.33x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 59.9 ms: 1.17x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 195 us: 3.39x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 866 ms: 2.64x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 454 ms: 2.50x faster                                                    |
| async_tree_none          | 950 ms                                                                | 384 ms: 2.47x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.92 ms: 2.28x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.64 sec: 2.25x faster                                                  |
| go                       | 264 ms                                                                | 130 ms: 2.03x faster                                                    |
| generators               | 68.1 ms                                                               | 35.5 ms: 1.92x faster                                                   |
| richards_super           | 107 ms                                                                | 56.4 ms: 1.90x faster                                                   |
| chaos                    | 121 ms                                                                | 65.5 ms: 1.85x faster                                                   |
| richards                 | 91.7 ms                                                               | 49.8 ms: 1.84x faster                                                   |
| raytrace                 | 573 ms                                                                | 320 ms: 1.79x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 721 ms: 1.77x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 35.7 us: 1.73x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 546 ms: 1.73x faster                                                    |
| scimark_sor              | 246 ms                                                                | 143 ms: 1.72x faster                                                    |
| scimark_lu               | 227 ms                                                                | 134 ms: 1.69x faster                                                    |
| comprehensions           | 33.1 us                                                               | 20.3 us: 1.63x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 78.8 ms: 1.62x faster                                                   |
| deepcopy                 | 511 us                                                                | 321 us: 1.59x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 85.4 ms: 1.57x faster                                                   |
| float                    | 135 ms                                                                | 87.0 ms: 1.55x faster                                                   |
| pyflate                  | 795 ms                                                                | 519 ms: 1.53x faster                                                    |
| spectral_norm            | 186 ms                                                                | 122 ms: 1.52x faster                                                    |
| pylint                   | 485 ms                                                                | 321 ms: 1.51x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.27 ms: 1.50x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.20 sec: 1.49x faster                                                  |
| regex_compile            | 177 ms                                                                | 120 ms: 1.47x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 254 us: 1.44x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 60.6 ms: 1.43x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 52.3 ms: 1.40x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.41 sec: 1.40x faster                                                  |
| django_template          | 53.3 ms                                                               | 38.9 ms: 1.37x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.25 sec: 1.36x faster                                                  |
| deepcopy_reduce          | 4.60 us                                                               | 3.42 us: 1.34x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 20.0 ms: 1.33x faster                                                   |
| mako                     | 18.9 ms                                                               | 14.3 ms: 1.33x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 400 us: 1.32x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 75.9 ms: 1.31x faster                                                   |
| sympy_sum                | 184 ms                                                                | 141 ms: 1.30x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.6 ms: 1.30x faster                                                   |
| nbody                    | 166 ms                                                                | 128 ms: 1.29x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.58 us: 1.29x faster                                                   |
| logging_format           | 10.6 us                                                               | 8.22 us: 1.29x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                   |
| 2to3                     | 381 ms                                                                | 301 ms: 1.26x faster                                                    |
| scimark_fft              | 500 ms                                                                | 400 ms: 1.25x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.90 sec: 1.24x faster                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 927 ms: 1.24x faster                                                    |
| sympy_str                | 329 ms                                                                | 268 ms: 1.22x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 5.79 us: 1.21x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.9 ms: 1.20x faster                                                   |
| sympy_expand             | 543 ms                                                                | 457 ms: 1.19x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                  |
| genshi_xml               | 69.8 ms                                                               | 59.9 ms: 1.17x faster                                                   |
| nqueens                  | 117 ms                                                                | 102 ms: 1.15x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 108 ms: 1.14x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.67 ms: 1.14x faster                                                   |
| fannkuch                 | 546 ms                                                                | 482 ms: 1.13x faster                                                    |
| meteor_contest           | 126 ms                                                                | 118 ms: 1.07x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.86 us: 1.07x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.06x faster                                                    |
| async_generators         | 452 ms                                                                | 429 ms: 1.06x faster                                                    |
| regex_dna                | 257 ms                                                                | 246 ms: 1.04x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 204 ms: 1.04x faster                                                    |
| unpickle                 | 17.5 us                                                               | 17.1 us: 1.02x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 667 ms: 1.02x slower                                                    |
| pickle_list              | 5.24 us                                                               | 5.38 us: 1.03x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 37.1 us: 1.06x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.50 ms: 1.06x slower                                                   |
| json_loads               | 30.9 us                                                               | 34.2 us: 1.10x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.44 ms: 1.11x slower                                                   |
| pickle                   | 12.5 us                                                               | 15.1 us: 1.21x slower                                                   |
| pidigits                 | 235 ms                                                                | 292 ms: 1.24x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.83 ms: 1.28x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.3 ms: 1.37x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.70 ms: 1.61x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.81 ms: 1.69x slower                                                   |
| logging_silent           | 222 ns                                                                | 647 ns: 2.91x slower                                                    |
| coverage                 | 83.6 ms                                                               | 535 ms: 6.40x slower                                                    |
| thrift                   | 1.26 ms                                                               | 193 ms: 153.21x slower                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 3.27 sec: 224.83x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.12x faster                                                            |

Benchmark hidden because not significant (2): json, regex_v8
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.226x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.40x
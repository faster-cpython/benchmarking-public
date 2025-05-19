# Results vs. 3.10.4

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: linux-aarch64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.229x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 299 ms: 1.28x faster                                                    |
| docutils       | 3.53 sec                                                              | 2.94 sec: 1.20x faster                                                  |
| html5lib       | 86.5 ms                                                               | 63.0 ms: 1.37x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 868 ms: 2.63x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 461 ms: 2.46x faster                                                    |
| async_tree_none         | 950 ms                                                                | 392 ms: 2.42x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 649 ms: 1.96x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.35x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 86.4 ms: 1.56x faster                                                   |
| nbody          | 166 ms                                                                | 122 ms: 1.36x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 122 ms: 1.45x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 28.2 ms: 1.14x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 3.82 ms: 1.11x faster                                                   |
| regex_dna      | 257 ms                                                                | 231 ms: 1.11x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.20x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 262 us: 1.40x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 382 us: 1.39x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.44 sec: 1.37x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 79.3 ms: 1.26x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 178 ms: 1.19x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 141 ms: 1.11x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.45 us: 1.08x faster                                                   |
| xml_etree_generate   | 123 ms                                                                | 114 ms: 1.07x faster                                                    |
| unpickle             | 17.5 us                                                               | 18.2 us: 1.04x slower                                                   |
| pickle_list          | 5.24 us                                                               | 5.58 us: 1.07x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 39.4 us: 1.12x slower                                                   |
| json_loads           | 30.9 us                                                               | 36.0 us: 1.16x slower                                                   |
| pickle               | 12.5 us                                                               | 15.2 us: 1.22x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.62 ms: 1.25x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                                   |
| django_template | 53.3 ms                                                               | 39.5 ms: 1.35x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 26.7 ms: 1.32x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 60.3 ms: 1.16x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.29x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 203 us: 3.25x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 868 ms: 2.63x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 461 ms: 2.46x faster                                                    |
| async_tree_none          | 950 ms                                                                | 392 ms: 2.42x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.74 ms: 2.39x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.65 sec: 2.24x faster                                                  |
| go                       | 264 ms                                                                | 131 ms: 2.02x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 649 ms: 1.96x faster                                                    |
| richards_super           | 107 ms                                                                | 57.5 ms: 1.86x faster                                                   |
| richards                 | 91.7 ms                                                               | 50.5 ms: 1.82x faster                                                   |
| generators               | 68.1 ms                                                               | 37.5 ms: 1.82x faster                                                   |
| raytrace                 | 573 ms                                                                | 322 ms: 1.78x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 539 ms: 1.75x faster                                                    |
| chaos                    | 121 ms                                                                | 70.3 ms: 1.72x faster                                                   |
| scimark_sor              | 246 ms                                                                | 146 ms: 1.69x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 38.0 us: 1.62x faster                                                   |
| pylint                   | 485 ms                                                                | 307 ms: 1.58x faster                                                    |
| comprehensions           | 33.1 us                                                               | 21.2 us: 1.57x faster                                                   |
| float                    | 135 ms                                                                | 86.4 ms: 1.56x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 86.2 ms: 1.56x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 82.9 ms: 1.54x faster                                                   |
| scimark_lu               | 227 ms                                                                | 148 ms: 1.54x faster                                                    |
| deepcopy                 | 511 us                                                                | 333 us: 1.53x faster                                                    |
| pyflate                  | 795 ms                                                                | 525 ms: 1.51x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.25 ms: 1.50x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.20 sec: 1.49x faster                                                  |
| regex_compile            | 177 ms                                                                | 122 ms: 1.45x faster                                                    |
| spectral_norm            | 186 ms                                                                | 130 ms: 1.43x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 262 us: 1.40x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 382 us: 1.39x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.44 sec: 1.37x faster                                                  |
| html5lib                 | 86.5 ms                                                               | 63.0 ms: 1.37x faster                                                   |
| nbody                    | 166 ms                                                                | 122 ms: 1.36x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                                   |
| django_template          | 53.3 ms                                                               | 39.5 ms: 1.35x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 54.7 ms: 1.34x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.26 sec: 1.34x faster                                                  |
| genshi_text              | 35.2 ms                                                               | 26.7 ms: 1.32x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 20.2 ms: 1.31x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.57 us: 1.29x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.58 us: 1.28x faster                                                   |
| logging_format           | 10.6 us                                                               | 8.27 us: 1.28x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.85 sec: 1.28x faster                                                  |
| 2to3                     | 381 ms                                                                | 299 ms: 1.28x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 905 ms: 1.27x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.5 ms: 1.26x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 79.3 ms: 1.26x faster                                                   |
| sympy_sum                | 184 ms                                                                | 147 ms: 1.25x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                                   |
| sympy_str                | 329 ms                                                                | 270 ms: 1.22x faster                                                    |
| docutils                 | 3.53 sec                                                              | 2.94 sec: 1.20x faster                                                  |
| xml_etree_parse          | 212 ms                                                                | 178 ms: 1.19x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                   |
| fannkuch                 | 546 ms                                                                | 466 ms: 1.17x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 60.3 ms: 1.16x faster                                                   |
| sympy_expand             | 543 ms                                                                | 469 ms: 1.16x faster                                                    |
| nqueens                  | 117 ms                                                                | 102 ms: 1.15x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.8 ms: 1.15x faster                                                   |
| scimark_fft              | 500 ms                                                                | 439 ms: 1.14x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 28.2 ms: 1.14x faster                                                   |
| regex_effbot             | 4.25 ms                                                               | 3.82 ms: 1.11x faster                                                   |
| regex_dna                | 257 ms                                                                | 231 ms: 1.11x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 141 ms: 1.11x faster                                                    |
| meteor_contest           | 126 ms                                                                | 114 ms: 1.11x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.99 ms: 1.09x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.45 us: 1.08x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 114 ms: 1.07x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.94 us: 1.05x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 669 ms: 1.02x slower                                                    |
| unpickle                 | 17.5 us                                                               | 18.2 us: 1.04x slower                                                   |
| json                     | 5.88 ms                                                               | 6.11 ms: 1.04x slower                                                   |
| pickle_list              | 5.24 us                                                               | 5.58 us: 1.07x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 39.4 us: 1.12x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.57 ms: 1.13x slower                                                   |
| json_loads               | 30.9 us                                                               | 36.0 us: 1.16x slower                                                   |
| pickle                   | 12.5 us                                                               | 15.2 us: 1.22x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.62 ms: 1.25x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.82 ms: 1.64x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.76 ms: 1.66x slower                                                   |
| logging_silent           | 222 ns                                                                | 604 ns: 2.72x slower                                                    |
| coverage                 | 83.6 ms                                                               | 548 ms: 6.56x slower                                                    |
| thrift                   | 1.26 ms                                                               | 197 ms: 156.14x slower                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 4.22 sec: 290.52x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.11x faster                                                            |

Benchmark hidden because not significant (2): async_generators, pidigits
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.229x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.34x
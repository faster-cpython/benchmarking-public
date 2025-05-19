# Results vs. 3.10.4

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: linux-aarch64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.195x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 314 ms: 1.21x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                  |
| html5lib       | 86.5 ms                                                               | 61.0 ms: 1.42x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 908 ms: 2.52x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 489 ms: 2.32x faster                                                    |
| async_tree_none         | 950 ms                                                                | 411 ms: 2.31x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 675 ms: 1.89x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.24x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 84.8 ms: 1.59x faster                                                   |
| nbody          | 166 ms                                                                | 118 ms: 1.41x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 126 ms: 1.41x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 28.3 ms: 1.14x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 3.84 ms: 1.11x faster                                                   |
| regex_dna      | 257 ms                                                                | 238 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.18x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.35 sec: 1.43x faster                                                  |
| unpickle_pure_python | 366 us                                                                | 258 us: 1.42x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 396 us: 1.33x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 77.8 ms: 1.28x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 182 ms: 1.17x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.67 us: 1.05x faster                                                   |
| pickle_list          | 5.24 us                                                               | 5.58 us: 1.06x slower                                                   |
| unpickle             | 17.5 us                                                               | 18.8 us: 1.07x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 39.0 us: 1.11x slower                                                   |
| json_loads           | 30.9 us                                                               | 35.3 us: 1.14x slower                                                   |
| pickle               | 12.5 us                                                               | 15.6 us: 1.25x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.75 ms: 1.27x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.3 ms: 1.36x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.5 ms: 1.41x faster                                                   |
| django_template | 53.3 ms                                                               | 39.5 ms: 1.35x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 63.0 ms: 1.11x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 209 us: 3.16x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 908 ms: 2.52x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.85 ms: 2.32x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 489 ms: 2.32x faster                                                    |
| async_tree_none          | 950 ms                                                                | 411 ms: 2.31x faster                                                    |
| mdp                      | 3.70 sec                                                              | 1.68 sec: 2.20x faster                                                  |
| richards_super           | 107 ms                                                                | 51.9 ms: 2.07x faster                                                   |
| richards                 | 91.7 ms                                                               | 47.2 ms: 1.94x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 675 ms: 1.89x faster                                                    |
| generators               | 68.1 ms                                                               | 36.8 ms: 1.85x faster                                                   |
| raytrace                 | 573 ms                                                                | 334 ms: 1.72x faster                                                    |
| chaos                    | 121 ms                                                                | 70.7 ms: 1.71x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 555 ms: 1.70x faster                                                    |
| scimark_sor              | 246 ms                                                                | 147 ms: 1.68x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.5 us: 1.65x faster                                                   |
| float                    | 135 ms                                                                | 84.8 ms: 1.59x faster                                                   |
| go                       | 264 ms                                                                | 168 ms: 1.57x faster                                                    |
| scimark_lu               | 227 ms                                                                | 147 ms: 1.55x faster                                                    |
| deepcopy                 | 511 us                                                                | 333 us: 1.54x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 87.3 ms: 1.46x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.25 sec: 1.46x faster                                                  |
| pyflate                  | 795 ms                                                                | 548 ms: 1.45x faster                                                    |
| pylint                   | 485 ms                                                                | 335 ms: 1.45x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.35 sec: 1.43x faster                                                  |
| crypto_pyaes             | 134 ms                                                                | 94.4 ms: 1.42x faster                                                   |
| spectral_norm            | 186 ms                                                                | 131 ms: 1.42x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 258 us: 1.42x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 61.0 ms: 1.42x faster                                                   |
| nbody                    | 166 ms                                                                | 118 ms: 1.41x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.5 ms: 1.41x faster                                                   |
| regex_compile            | 177 ms                                                                | 126 ms: 1.41x faster                                                    |
| comprehensions           | 33.1 us                                                               | 23.6 us: 1.40x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.90 ms: 1.38x faster                                                   |
| django_template          | 53.3 ms                                                               | 39.5 ms: 1.35x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 396 us: 1.33x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.52 us: 1.31x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.63 us: 1.28x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 77.8 ms: 1.28x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                                   |
| logging_format           | 10.6 us                                                               | 8.36 us: 1.27x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 21.1 ms: 1.26x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                                   |
| coroutines               | 37.2 ms                                                               | 29.9 ms: 1.24x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 59.2 ms: 1.24x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.39 sec: 1.22x faster                                                  |
| sympy_str                | 329 ms                                                                | 269 ms: 1.22x faster                                                    |
| sympy_sum                | 184 ms                                                                | 151 ms: 1.22x faster                                                    |
| 2to3                     | 381 ms                                                                | 314 ms: 1.21x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 182 ms: 1.17x faster                                                    |
| scimark_fft              | 500 ms                                                                | 430 ms: 1.16x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                  |
| bench_thread_pool        | 1.59 ms                                                               | 1.40 ms: 1.14x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 28.3 ms: 1.14x faster                                                   |
| sympy_expand             | 543 ms                                                                | 479 ms: 1.13x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 23.3 ms: 1.13x faster                                                   |
| nqueens                  | 117 ms                                                                | 105 ms: 1.12x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.85 ms: 1.11x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 63.0 ms: 1.11x faster                                                   |
| fannkuch                 | 546 ms                                                                | 492 ms: 1.11x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 3.84 ms: 1.11x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.77 us: 1.09x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                                    |
| regex_dna                | 257 ms                                                                | 238 ms: 1.08x faster                                                    |
| meteor_contest           | 126 ms                                                                | 120 ms: 1.05x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.67 us: 1.05x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.14 sec: 1.01x faster                                                  |
| asyncio_websockets       | 657 ms                                                                | 670 ms: 1.02x slower                                                    |
| json                     | 5.88 ms                                                               | 6.00 ms: 1.02x slower                                                   |
| pickle_list              | 5.24 us                                                               | 5.58 us: 1.06x slower                                                   |
| unpickle                 | 17.5 us                                                               | 18.8 us: 1.07x slower                                                   |
| async_generators         | 452 ms                                                                | 485 ms: 1.07x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 39.0 us: 1.11x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.60 ms: 1.13x slower                                                   |
| json_loads               | 30.9 us                                                               | 35.3 us: 1.14x slower                                                   |
| pickle                   | 12.5 us                                                               | 15.6 us: 1.25x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.75 ms: 1.27x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.3 ms: 1.36x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.85 ms: 1.65x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.76 ms: 1.66x slower                                                   |
| logging_silent           | 222 ns                                                                | 626 ns: 2.82x slower                                                    |
| coverage                 | 83.6 ms                                                               | 548 ms: 6.55x slower                                                    |
| thrift                   | 1.26 ms                                                               | 194 ms: 153.73x slower                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 3.94 sec: 271.31x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.08x faster                                                            |

Benchmark hidden because not significant (2): pprint_pformat, pidigits
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250518-3.15.0a0-009e7b3-JIT/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.195x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.37x
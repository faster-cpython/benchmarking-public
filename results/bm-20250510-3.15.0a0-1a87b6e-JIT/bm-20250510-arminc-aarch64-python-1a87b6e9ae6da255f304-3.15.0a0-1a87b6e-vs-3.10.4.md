# Results vs. 3.10.4

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-aarch64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.194x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 313 ms: 1.22x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                  |
| html5lib       | 86.5 ms                                                               | 61.0 ms: 1.42x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 915 ms: 2.50x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 483 ms: 2.34x faster                                                    |
| async_tree_none         | 950 ms                                                                | 412 ms: 2.31x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 677 ms: 1.88x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.24x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 84.4 ms: 1.60x faster                                                   |
| nbody          | 166 ms                                                                | 119 ms: 1.39x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 122 ms: 1.44x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 28.9 ms: 1.11x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 3.83 ms: 1.11x faster                                                   |
| regex_dna      | 257 ms                                                                | 232 ms: 1.11x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.18x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.37 sec: 1.42x faster                                                  |
| unpickle_pure_python | 366 us                                                                | 262 us: 1.39x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 394 us: 1.34x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 78.8 ms: 1.26x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 14.3 ms: 1.17x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 185 ms: 1.14x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.11x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.43 us: 1.09x faster                                                   |
| xml_etree_iterparse  | 156 ms                                                                | 144 ms: 1.08x faster                                                    |
| unpickle             | 17.5 us                                                               | 18.5 us: 1.06x slower                                                   |
| pickle_list          | 5.24 us                                                               | 5.65 us: 1.08x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 38.8 us: 1.10x slower                                                   |
| json_loads           | 30.9 us                                                               | 35.3 us: 1.14x slower                                                   |
| pickle               | 12.5 us                                                               | 15.5 us: 1.24x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.65 ms: 1.26x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                   |
| django_template | 53.3 ms                                                               | 40.2 ms: 1.33x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.1 ms: 1.30x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 62.8 ms: 1.11x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 214 us: 3.09x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 915 ms: 2.50x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 483 ms: 2.34x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.85 ms: 2.32x faster                                                   |
| async_tree_none          | 950 ms                                                                | 412 ms: 2.31x faster                                                    |
| mdp                      | 3.70 sec                                                              | 1.68 sec: 2.20x faster                                                  |
| richards_super           | 107 ms                                                                | 51.9 ms: 2.07x faster                                                   |
| richards                 | 91.7 ms                                                               | 46.9 ms: 1.95x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 677 ms: 1.88x faster                                                    |
| generators               | 68.1 ms                                                               | 37.3 ms: 1.83x faster                                                   |
| raytrace                 | 573 ms                                                                | 330 ms: 1.74x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 544 ms: 1.74x faster                                                    |
| chaos                    | 121 ms                                                                | 70.6 ms: 1.72x faster                                                   |
| scimark_sor              | 246 ms                                                                | 146 ms: 1.68x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.5 us: 1.64x faster                                                   |
| float                    | 135 ms                                                                | 84.4 ms: 1.60x faster                                                   |
| go                       | 264 ms                                                                | 167 ms: 1.58x faster                                                    |
| scimark_lu               | 227 ms                                                                | 148 ms: 1.54x faster                                                    |
| pylint                   | 485 ms                                                                | 320 ms: 1.52x faster                                                    |
| deepcopy                 | 511 us                                                                | 338 us: 1.51x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 84.7 ms: 1.51x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.22 sec: 1.48x faster                                                  |
| regex_compile            | 177 ms                                                                | 122 ms: 1.44x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 93.7 ms: 1.43x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.37 sec: 1.42x faster                                                  |
| html5lib                 | 86.5 ms                                                               | 61.0 ms: 1.42x faster                                                   |
| comprehensions           | 33.1 us                                                               | 23.6 us: 1.41x faster                                                   |
| pyflate                  | 795 ms                                                                | 567 ms: 1.40x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.82 ms: 1.40x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 262 us: 1.39x faster                                                    |
| spectral_norm            | 186 ms                                                                | 134 ms: 1.39x faster                                                    |
| nbody                    | 166 ms                                                                | 119 ms: 1.39x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 394 us: 1.34x faster                                                    |
| django_template          | 53.3 ms                                                               | 40.2 ms: 1.33x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.1 ms: 1.30x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.56 us: 1.29x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 57.7 ms: 1.27x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.74 us: 1.26x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 78.8 ms: 1.26x faster                                                   |
| logging_format           | 10.6 us                                                               | 8.41 us: 1.26x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 21.1 ms: 1.26x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.36 sec: 1.25x faster                                                  |
| sympy_sum                | 184 ms                                                                | 148 ms: 1.24x faster                                                    |
| coroutines               | 37.2 ms                                                               | 30.1 ms: 1.24x faster                                                   |
| 2to3                     | 381 ms                                                                | 313 ms: 1.22x faster                                                    |
| sympy_str                | 329 ms                                                                | 275 ms: 1.19x faster                                                    |
| scimark_fft              | 500 ms                                                                | 426 ms: 1.17x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.3 ms: 1.17x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.37 ms: 1.16x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 23.0 ms: 1.14x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 185 ms: 1.14x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                  |
| sympy_expand             | 543 ms                                                                | 483 ms: 1.12x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 62.8 ms: 1.11x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 28.9 ms: 1.11x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.11x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 3.83 ms: 1.11x faster                                                   |
| regex_dna                | 257 ms                                                                | 232 ms: 1.11x faster                                                    |
| fannkuch                 | 546 ms                                                                | 499 ms: 1.09x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.43 us: 1.09x faster                                                   |
| nqueens                  | 117 ms                                                                | 108 ms: 1.09x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.03 ms: 1.08x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 144 ms: 1.08x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.87 us: 1.06x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 670 ms: 1.02x slower                                                    |
| async_generators         | 452 ms                                                                | 473 ms: 1.05x slower                                                    |
| json                     | 5.88 ms                                                               | 6.22 ms: 1.06x slower                                                   |
| unpickle                 | 17.5 us                                                               | 18.5 us: 1.06x slower                                                   |
| pickle_list              | 5.24 us                                                               | 5.65 us: 1.08x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.18 ms: 1.08x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 38.8 us: 1.10x slower                                                   |
| json_loads               | 30.9 us                                                               | 35.3 us: 1.14x slower                                                   |
| pickle                   | 12.5 us                                                               | 15.5 us: 1.24x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.65 ms: 1.26x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.75 ms: 1.63x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.71 ms: 1.64x slower                                                   |
| logging_silent           | 222 ns                                                                | 629 ns: 2.83x slower                                                    |
| coverage                 | 83.6 ms                                                               | 545 ms: 6.52x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 1.40 sec: 96.06x slower                                                 |
| thrift                   | 1.26 ms                                                               | 194 ms: 153.61x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.10x faster                                                            |

Benchmark hidden because not significant (4): meteor_contest, pprint_safe_repr, pprint_pformat, pidigits
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.194x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.37x
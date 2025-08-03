# Results vs. 3.10.4

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: linux-aarch64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.288x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 310 ms: 1.23x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.13 sec: 1.13x faster                                                  |
| html5lib       | 86.5 ms                                                               | 64.5 ms: 1.34x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 902 ms: 2.53x faster                                                    |
| async_tree_none         | 950 ms                                                                | 391 ms: 2.43x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 472 ms: 2.40x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 663 ms: 1.92x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 82.9 ms: 1.62x faster                                                   |
| nbody          | 166 ms                                                                | 127 ms: 1.31x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 126 ms: 1.40x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 26.0 ms: 1.24x faster                                                   |
| regex_dna      | 257 ms                                                                | 218 ms: 1.18x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.79 ms: 1.12x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.31 sec: 1.46x faster                                                  |
| unpickle_pure_python | 366 us                                                                | 252 us: 1.45x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 399 us: 1.33x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 77.3 ms: 1.29x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.23x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 178 ms: 1.19x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 109 ms: 1.13x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.48 us: 1.08x faster                                                   |
| xml_etree_iterparse  | 156 ms                                                                | 145 ms: 1.08x faster                                                    |
| unpickle             | 17.5 us                                                               | 18.3 us: 1.05x slower                                                   |
| json_loads           | 30.9 us                                                               | 33.3 us: 1.08x slower                                                   |
| pickle_list          | 5.24 us                                                               | 5.68 us: 1.09x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 38.2 us: 1.09x slower                                                   |
| pickle               | 12.5 us                                                               | 15.3 us: 1.22x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.62 ms: 1.25x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.9 ms: 1.47x faster                                                   |
| django_template | 53.3 ms                                                               | 40.4 ms: 1.32x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 26.8 ms: 1.31x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 64.1 ms: 1.09x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.29x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 207 us: 3.20x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 902 ms: 2.53x faster                                                    |
| async_tree_none          | 950 ms                                                                | 391 ms: 2.43x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 472 ms: 2.40x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.88 ms: 2.30x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.69 sec: 2.18x faster                                                  |
| richards_super           | 107 ms                                                                | 50.8 ms: 2.11x faster                                                   |
| richards                 | 91.7 ms                                                               | 44.4 ms: 2.06x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 663 ms: 1.92x faster                                                    |
| generators               | 68.1 ms                                                               | 36.3 ms: 1.87x faster                                                   |
| chaos                    | 121 ms                                                                | 69.6 ms: 1.74x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 543 ms: 1.74x faster                                                    |
| go                       | 264 ms                                                                | 154 ms: 1.72x faster                                                    |
| scimark_sor              | 246 ms                                                                | 143 ms: 1.72x faster                                                    |
| raytrace                 | 573 ms                                                                | 336 ms: 1.71x faster                                                    |
| logging_silent           | 222 ns                                                                | 131 ns: 1.69x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.1 us: 1.66x faster                                                   |
| float                    | 135 ms                                                                | 82.9 ms: 1.62x faster                                                   |
| spectral_norm            | 186 ms                                                                | 117 ms: 1.59x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 80.7 ms: 1.58x faster                                                   |
| deepcopy                 | 511 us                                                                | 331 us: 1.54x faster                                                    |
| scimark_lu               | 227 ms                                                                | 149 ms: 1.52x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 89.0 ms: 1.51x faster                                                   |
| pyflate                  | 795 ms                                                                | 533 ms: 1.49x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.21 sec: 1.49x faster                                                  |
| pylint                   | 485 ms                                                                | 328 ms: 1.48x faster                                                    |
| mako                     | 18.9 ms                                                               | 12.9 ms: 1.47x faster                                                   |
| comprehensions           | 33.1 us                                                               | 22.6 us: 1.47x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.31 sec: 1.46x faster                                                  |
| unpickle_pure_python     | 366 us                                                                | 252 us: 1.45x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.58 ms: 1.44x faster                                                   |
| logging_simple           | 9.78 us                                                               | 6.90 us: 1.42x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.56 us: 1.40x faster                                                   |
| regex_compile            | 177 ms                                                                | 126 ms: 1.40x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 52.9 ms: 1.39x faster                                                   |
| thrift                   | 1.26 ms                                                               | 935 us: 1.35x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 64.5 ms: 1.34x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 399 us: 1.33x faster                                                    |
| django_template          | 53.3 ms                                                               | 40.4 ms: 1.32x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 26.8 ms: 1.31x faster                                                   |
| nbody                    | 166 ms                                                                | 127 ms: 1.31x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.54 us: 1.30x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 77.3 ms: 1.29x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 20.8 ms: 1.28x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.33 sec: 1.27x faster                                                  |
| sympy_sum                | 184 ms                                                                | 146 ms: 1.26x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.5 ms: 1.26x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 26.0 ms: 1.24x faster                                                   |
| scimark_fft              | 500 ms                                                                | 405 ms: 1.24x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.23x faster                                                   |
| 2to3                     | 381 ms                                                                | 310 ms: 1.23x faster                                                    |
| sympy_str                | 329 ms                                                                | 272 ms: 1.21x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 178 ms: 1.19x faster                                                    |
| regex_dna                | 257 ms                                                                | 218 ms: 1.18x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.4 ms: 1.18x faster                                                   |
| fannkuch                 | 546 ms                                                                | 469 ms: 1.16x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.38 ms: 1.16x faster                                                   |
| nqueens                  | 117 ms                                                                | 102 ms: 1.15x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.64 us: 1.13x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 109 ms: 1.13x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.13 sec: 1.13x faster                                                  |
| regex_effbot             | 4.25 ms                                                               | 3.79 ms: 1.12x faster                                                   |
| sympy_expand             | 543 ms                                                                | 487 ms: 1.11x faster                                                    |
| meteor_contest           | 126 ms                                                                | 114 ms: 1.10x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.94 ms: 1.10x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 64.1 ms: 1.09x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.48 us: 1.08x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 145 ms: 1.08x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.32 sec: 1.01x faster                                                  |
| json                     | 5.88 ms                                                               | 5.84 ms: 1.01x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 667 ms: 1.02x slower                                                    |
| unpickle                 | 17.5 us                                                               | 18.3 us: 1.05x slower                                                   |
| async_generators         | 452 ms                                                                | 485 ms: 1.07x slower                                                    |
| json_loads               | 30.9 us                                                               | 33.3 us: 1.08x slower                                                   |
| pickle_list              | 5.24 us                                                               | 5.68 us: 1.09x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 38.2 us: 1.09x slower                                                   |
| pickle                   | 12.5 us                                                               | 15.3 us: 1.22x slower                                                   |
| coverage                 | 83.6 ms                                                               | 103 ms: 1.23x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.62 ms: 1.25x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.79 ms: 1.68x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 7.00 ms: 1.68x slower                                                   |
| telco                    | 8.49 ms                                                               | 167 ms: 19.69x slower                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 3.60 sec: 247.98x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.18x faster                                                            |

Benchmark hidden because not significant (2): pprint_safe_repr, pidigits
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.288x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.41x
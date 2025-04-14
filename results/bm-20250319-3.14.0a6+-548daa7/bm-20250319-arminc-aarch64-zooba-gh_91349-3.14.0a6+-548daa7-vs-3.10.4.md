# Results vs. 3.10.4

- fork: zooba
- ref: gh_91349
- machine: linux-aarch64
- commit hash: 548daa7
- commit date: 2025-03-19
- overall geometric mean: 1.319x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 301 ms: 1.27x faster                                        |
| docutils       | 3.53 sec                                                              | 3.07 sec: 1.15x faster                                      |
| html5lib       | 86.5 ms                                                               | 64.5 ms: 1.34x faster                                       |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 884 ms: 2.58x faster                                        |
| async_tree_none         | 950 ms                                                                | 383 ms: 2.48x faster                                        |
| async_tree_memoization  | 1.13 sec                                                              | 468 ms: 2.42x faster                                        |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 658 ms: 1.93x faster                                        |
| Geometric mean          | (ref)                                                                 | 2.34x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 135 ms                                                                | 87.0 ms: 1.55x faster                                       |
| nbody          | 166 ms                                                                | 125 ms: 1.33x faster                                        |
| pidigits       | 235 ms                                                                | 237 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 127 ms: 1.39x faster                                        |
| regex_v8       | 32.2 ms                                                               | 28.9 ms: 1.11x faster                                       |
| regex_effbot   | 4.25 ms                                                               | 4.01 ms: 1.06x faster                                       |
| regex_dna      | 257 ms                                                                | 247 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 386 us: 1.37x faster                                        |
| tomli_loads          | 3.36 sec                                                              | 2.45 sec: 1.37x faster                                      |
| unpickle_pure_python | 366 us                                                                | 270 us: 1.36x faster                                        |
| xml_etree_process    | 99.5 ms                                                               | 79.4 ms: 1.25x faster                                       |
| xml_etree_parse      | 212 ms                                                                | 176 ms: 1.20x faster                                        |
| json_dumps           | 16.7 ms                                                               | 14.1 ms: 1.18x faster                                       |
| xml_etree_iterparse  | 156 ms                                                                | 141 ms: 1.11x faster                                        |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.08x faster                                        |
| json_loads           | 30.9 us                                                               | 35.2 us: 1.14x slower                                       |
| Geometric mean       | (ref)                                                                 | 1.19x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                       |
| python_startup_no_site | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                       |
| Geometric mean         | (ref)                                                                 | 1.46x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                       |
| django_template | 53.3 ms                                                               | 40.9 ms: 1.30x faster                                       |
| genshi_text     | 35.2 ms                                                               | 27.0 ms: 1.30x faster                                       |
| genshi_xml      | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                       |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 197 us: 3.35x faster                                        |
| async_tree_io            | 2.28 sec                                                              | 884 ms: 2.58x faster                                        |
| async_tree_none          | 950 ms                                                                | 383 ms: 2.48x faster                                        |
| async_tree_memoization   | 1.13 sec                                                              | 468 ms: 2.42x faster                                        |
| deltablue                | 8.94 ms                                                               | 4.04 ms: 2.21x faster                                       |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 658 ms: 1.93x faster                                        |
| go                       | 264 ms                                                                | 140 ms: 1.89x faster                                        |
| generators               | 68.1 ms                                                               | 36.3 ms: 1.88x faster                                       |
| richards_super           | 107 ms                                                                | 59.6 ms: 1.80x faster                                       |
| raytrace                 | 573 ms                                                                | 321 ms: 1.79x faster                                        |
| richards                 | 91.7 ms                                                               | 52.0 ms: 1.76x faster                                       |
| chaos                    | 121 ms                                                                | 71.0 ms: 1.70x faster                                       |
| logging_silent           | 222 ns                                                                | 133 ns: 1.67x faster                                        |
| scimark_sor              | 246 ms                                                                | 151 ms: 1.63x faster                                        |
| deepcopy_memo            | 61.7 us                                                               | 39.1 us: 1.58x faster                                       |
| pylint                   | 485 ms                                                                | 311 ms: 1.56x faster                                        |
| comprehensions           | 33.1 us                                                               | 21.3 us: 1.56x faster                                       |
| float                    | 135 ms                                                                | 87.0 ms: 1.55x faster                                       |
| crypto_pyaes             | 134 ms                                                                | 89.1 ms: 1.50x faster                                       |
| deepcopy                 | 511 us                                                                | 341 us: 1.50x faster                                        |
| scimark_monte_carlo      | 128 ms                                                                | 85.5 ms: 1.50x faster                                       |
| spectral_norm            | 186 ms                                                                | 125 ms: 1.49x faster                                        |
| scimark_lu               | 227 ms                                                                | 157 ms: 1.44x faster                                        |
| hexiom                   | 10.9 ms                                                               | 7.57 ms: 1.44x faster                                       |
| dulwich_log              | 73.5 ms                                                               | 51.2 ms: 1.44x faster                                       |
| pyflate                  | 795 ms                                                                | 561 ms: 1.42x faster                                        |
| regex_compile            | 177 ms                                                                | 127 ms: 1.39x faster                                        |
| logging_simple           | 9.78 us                                                               | 7.10 us: 1.38x faster                                       |
| pickle_pure_python       | 529 us                                                                | 386 us: 1.37x faster                                        |
| tomli_loads              | 3.36 sec                                                              | 2.45 sec: 1.37x faster                                      |
| unpickle_pure_python     | 366 us                                                                | 270 us: 1.36x faster                                        |
| logging_format           | 10.6 us                                                               | 7.84 us: 1.35x faster                                       |
| sqlalchemy_declarative   | 197 ms                                                                | 146 ms: 1.35x faster                                        |
| thrift                   | 1.26 ms                                                               | 936 us: 1.35x faster                                        |
| html5lib                 | 86.5 ms                                                               | 64.5 ms: 1.34x faster                                       |
| mako                     | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                       |
| pycparser                | 1.69 sec                                                              | 1.27 sec: 1.33x faster                                      |
| nbody                    | 166 ms                                                                | 125 ms: 1.33x faster                                        |
| django_template          | 53.3 ms                                                               | 40.9 ms: 1.30x faster                                       |
| genshi_text              | 35.2 ms                                                               | 27.0 ms: 1.30x faster                                       |
| deepcopy_reduce          | 4.60 us                                                               | 3.59 us: 1.28x faster                                       |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.2 ms: 1.27x faster                                       |
| 2to3                     | 381 ms                                                                | 301 ms: 1.27x faster                                        |
| sympy_sum                | 184 ms                                                                | 146 ms: 1.26x faster                                        |
| coroutines               | 37.2 ms                                                               | 29.6 ms: 1.26x faster                                       |
| xml_etree_process        | 99.5 ms                                                               | 79.4 ms: 1.25x faster                                       |
| sympy_integrate          | 26.5 ms                                                               | 21.5 ms: 1.23x faster                                       |
| pprint_pformat           | 2.36 sec                                                              | 1.92 sec: 1.23x faster                                      |
| pprint_safe_repr         | 1.15 sec                                                              | 940 ms: 1.22x faster                                        |
| xml_etree_parse          | 212 ms                                                                | 176 ms: 1.20x faster                                        |
| pathlib                  | 26.3 ms                                                               | 22.1 ms: 1.19x faster                                       |
| sympy_str                | 329 ms                                                                | 277 ms: 1.19x faster                                        |
| scimark_fft              | 500 ms                                                                | 424 ms: 1.18x faster                                        |
| json_dumps               | 16.7 ms                                                               | 14.1 ms: 1.18x faster                                       |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.17x faster                                       |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.54 ms: 1.17x faster                                       |
| genshi_xml               | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                       |
| docutils                 | 3.53 sec                                                              | 3.07 sec: 1.15x faster                                      |
| sympy_expand             | 543 ms                                                                | 473 ms: 1.15x faster                                        |
| nqueens                  | 117 ms                                                                | 103 ms: 1.14x faster                                        |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                        |
| regex_v8                 | 32.2 ms                                                               | 28.9 ms: 1.11x faster                                       |
| xml_etree_iterparse      | 156 ms                                                                | 141 ms: 1.11x faster                                        |
| mdp                      | 3.70 sec                                                              | 3.34 sec: 1.11x faster                                      |
| fannkuch                 | 546 ms                                                                | 500 ms: 1.09x faster                                        |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.08x faster                                        |
| sqlite_synth             | 4.12 us                                                               | 3.82 us: 1.08x faster                                       |
| regex_effbot             | 4.25 ms                                                               | 4.01 ms: 1.06x faster                                       |
| regex_dna                | 257 ms                                                                | 247 ms: 1.04x faster                                        |
| pidigits                 | 235 ms                                                                | 237 ms: 1.01x slower                                        |
| asyncio_websockets       | 657 ms                                                                | 672 ms: 1.02x slower                                        |
| json_loads               | 30.9 us                                                               | 35.2 us: 1.14x slower                                       |
| telco                    | 8.49 ms                                                               | 9.93 ms: 1.17x slower                                       |
| coverage                 | 83.6 ms                                                               | 99.7 ms: 1.19x slower                                       |
| python_startup           | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                       |
| python_startup_no_site   | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                       |
| gc_traversal             | 4.15 ms                                                               | 6.59 ms: 1.59x slower                                       |
| create_gc_cycles         | 2.26 ms                                                               | 3.60 ms: 1.59x slower                                       |
| bench_mp_pool            | 14.5 ms                                                               | 3.19 sec: 219.43x slower                                    |
| Geometric mean           | (ref)                                                                 | 1.22x faster                                                |

Benchmark hidden because not significant (2): async_generators, json
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250319-3.14.0a6+-548daa7/bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.319x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.31x
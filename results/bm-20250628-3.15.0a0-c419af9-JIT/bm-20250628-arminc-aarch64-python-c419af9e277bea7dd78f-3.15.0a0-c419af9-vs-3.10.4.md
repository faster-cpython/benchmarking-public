# Results vs. 3.10.4

- fork: python
- ref: c419af9e277bea7dd78f
- machine: linux-aarch64
- commit hash: c419af9
- commit date: 2025-06-28
- overall geometric mean: 1.335x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 310 ms: 1.23x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.13 sec: 1.13x faster                                                  |
| html5lib       | 86.5 ms                                                               | 62.5 ms: 1.38x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 918 ms: 2.49x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 471 ms: 2.40x faster                                                    |
| async_tree_none         | 950 ms                                                                | 404 ms: 2.35x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 666 ms: 1.91x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.28x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 83.1 ms: 1.62x faster                                                   |
| nbody          | 166 ms                                                                | 129 ms: 1.28x faster                                                    |
| pidigits       | 235 ms                                                                | 236 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 124 ms: 1.43x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 26.5 ms: 1.22x faster                                                   |
| regex_dna      | 257 ms                                                                | 217 ms: 1.19x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.84 ms: 1.10x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.31 sec: 1.45x faster                                                  |
| unpickle_pure_python | 366 us                                                                | 253 us: 1.44x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 396 us: 1.33x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 78.3 ms: 1.27x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 178 ms: 1.19x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 109 ms: 1.13x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.9 us: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.22x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.67 ms: 1.26x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.1 ms: 1.44x faster                                                   |
| django_template | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 28.3 ms: 1.24x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 62.5 ms: 1.12x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 203 us: 3.25x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 918 ms: 2.49x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 471 ms: 2.40x faster                                                    |
| async_tree_none          | 950 ms                                                                | 404 ms: 2.35x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.85 ms: 2.32x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.66 sec: 2.23x faster                                                  |
| richards_super           | 107 ms                                                                | 51.3 ms: 2.09x faster                                                   |
| richards                 | 91.7 ms                                                               | 44.3 ms: 2.07x faster                                                   |
| generators               | 68.1 ms                                                               | 35.2 ms: 1.93x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 666 ms: 1.91x faster                                                    |
| chaos                    | 121 ms                                                                | 68.9 ms: 1.76x faster                                                   |
| scimark_sor              | 246 ms                                                                | 141 ms: 1.75x faster                                                    |
| raytrace                 | 573 ms                                                                | 333 ms: 1.72x faster                                                    |
| logging_silent           | 222 ns                                                                | 129 ns: 1.72x faster                                                    |
| go                       | 264 ms                                                                | 156 ms: 1.69x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.8 us: 1.63x faster                                                   |
| float                    | 135 ms                                                                | 83.1 ms: 1.62x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 80.3 ms: 1.59x faster                                                   |
| spectral_norm            | 186 ms                                                                | 119 ms: 1.56x faster                                                    |
| deepcopy                 | 511 us                                                                | 329 us: 1.55x faster                                                    |
| scimark_lu               | 227 ms                                                                | 149 ms: 1.52x faster                                                    |
| pylint                   | 485 ms                                                                | 320 ms: 1.52x faster                                                    |
| pyflate                  | 795 ms                                                                | 531 ms: 1.50x faster                                                    |
| comprehensions           | 33.1 us                                                               | 22.4 us: 1.48x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.43 ms: 1.47x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.31 sec: 1.45x faster                                                  |
| unpickle_pure_python     | 366 us                                                                | 253 us: 1.44x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.1 ms: 1.44x faster                                                   |
| regex_compile            | 177 ms                                                                | 124 ms: 1.43x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 95.3 ms: 1.41x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.02 us: 1.39x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 62.5 ms: 1.38x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.76 us: 1.37x faster                                                   |
| django_template          | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 396 us: 1.33x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 55.4 ms: 1.33x faster                                                   |
| thrift                   | 1.26 ms                                                               | 978 us: 1.29x faster                                                    |
| nbody                    | 166 ms                                                                | 129 ms: 1.28x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 78.3 ms: 1.27x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.62 us: 1.27x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 21.0 ms: 1.26x faster                                                   |
| coroutines               | 37.2 ms                                                               | 29.8 ms: 1.25x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 28.3 ms: 1.24x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.37 sec: 1.23x faster                                                  |
| 2to3                     | 381 ms                                                                | 310 ms: 1.23x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 26.5 ms: 1.22x faster                                                   |
| scimark_fft              | 500 ms                                                                | 413 ms: 1.21x faster                                                    |
| sympy_sum                | 184 ms                                                                | 153 ms: 1.20x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 178 ms: 1.19x faster                                                    |
| regex_dna                | 257 ms                                                                | 217 ms: 1.19x faster                                                    |
| sympy_str                | 329 ms                                                                | 279 ms: 1.18x faster                                                    |
| fannkuch                 | 546 ms                                                                | 477 ms: 1.14x faster                                                    |
| sympy_expand             | 543 ms                                                                | 478 ms: 1.14x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 23.2 ms: 1.14x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 109 ms: 1.13x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.13 sec: 1.13x faster                                                  |
| sqlite_synth             | 4.12 us                                                               | 3.66 us: 1.12x faster                                                   |
| nqueens                  | 117 ms                                                                | 105 ms: 1.12x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 62.5 ms: 1.12x faster                                                   |
| regex_effbot             | 4.25 ms                                                               | 3.84 ms: 1.10x faster                                                   |
| meteor_contest           | 126 ms                                                                | 115 ms: 1.09x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.08 ms: 1.08x faster                                                   |
| json                     | 5.88 ms                                                               | 5.77 ms: 1.02x faster                                                   |
| pidigits                 | 235 ms                                                                | 236 ms: 1.01x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 665 ms: 1.01x slower                                                    |
| async_generators         | 452 ms                                                                | 473 ms: 1.05x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.9 us: 1.06x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.38 ms: 1.10x slower                                                   |
| coverage                 | 83.6 ms                                                               | 103 ms: 1.24x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.67 ms: 1.26x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.75 ms: 1.66x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.93 ms: 1.67x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.33x faster                                                            |

Benchmark hidden because not significant (2): pprint_safe_repr, pprint_pformat
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250628-3.15.0a0-c419af9-JIT/bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.335x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.39x
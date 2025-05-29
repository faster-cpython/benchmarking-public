# Results vs. 3.10.4

- fork: mdboom
- ref: tail_call_no_preserv
- machine: linux-x86_64
- commit hash: 09f3d0f
- commit date: 2025-01-16
- overall geometric mean: 1.350x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 282 ms: 1.24x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.89 sec: 1.18x faster                                                       |
| html5lib       | 94.6 ms                                                      | 67.0 ms: 1.41x faster                                                        |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 629 ms: 2.54x faster                                                         |
| async_tree_none         | 692 ms                                                       | 283 ms: 2.45x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 347 ms: 2.36x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 543 ms: 1.72x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.24x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 71.9 ms: 1.55x faster                                                        |
| nbody          | 134 ms                                                       | 89.2 ms: 1.50x faster                                                        |
| pidigits       | 271 ms                                                       | 286 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 138 ms: 1.38x faster                                                         |
| regex_dna      | 261 ms                                                       | 223 ms: 1.17x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.00 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 216 us: 1.44x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.06 sec: 1.42x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 325 us: 1.40x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 57.6 ms: 1.32x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.7 ms: 1.24x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.20x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 80.9 ms: 1.14x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                                         |
| Geometric mean       | (ref)                                                        | 1.24x faster                                                                 |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.06 ms: 1.24x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 37.2 ms: 1.35x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 23.5 ms: 1.34x faster                                                        |
| mako            | 14.7 ms                                                      | 11.3 ms: 1.30x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 53.7 ms: 1.18x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 172 us: 3.11x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 629 ms: 2.54x faster                                                         |
| async_tree_none          | 692 ms                                                       | 283 ms: 2.45x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 347 ms: 2.36x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.33 ms: 2.25x faster                                                        |
| go                       | 262 ms                                                       | 128 ms: 2.04x faster                                                         |
| generators               | 57.3 ms                                                      | 30.6 ms: 1.87x faster                                                        |
| scimark_lu               | 167 ms                                                       | 89.2 ms: 1.87x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 57.5 ms: 1.87x faster                                                        |
| logging_silent           | 167 ns                                                       | 89.9 ns: 1.86x faster                                                        |
| raytrace                 | 489 ms                                                       | 267 ms: 1.83x faster                                                         |
| richards_super           | 90.6 ms                                                      | 49.9 ms: 1.82x faster                                                        |
| pylint                   | 566 ms                                                       | 319 ms: 1.77x faster                                                         |
| chaos                    | 109 ms                                                       | 61.4 ms: 1.77x faster                                                        |
| richards                 | 75.1 ms                                                      | 43.3 ms: 1.74x faster                                                        |
| scimark_sor              | 180 ms                                                       | 104 ms: 1.73x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 28.9 us: 1.72x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 543 ms: 1.72x faster                                                         |
| pyflate                  | 733 ms                                                       | 431 ms: 1.70x faster                                                         |
| deepcopy                 | 468 us                                                       | 279 us: 1.68x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.35 ms: 1.66x faster                                                        |
| float                    | 111 ms                                                       | 71.9 ms: 1.55x faster                                                        |
| spectral_norm            | 139 ms                                                       | 90.0 ms: 1.55x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.74 ms: 1.54x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.12 ms: 1.54x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.53x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 78.1 ms: 1.53x faster                                                        |
| nbody                    | 134 ms                                                       | 89.2 ms: 1.50x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.10 us: 1.45x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 216 us: 1.44x faster                                                         |
| thrift                   | 1.18 ms                                                      | 827 us: 1.42x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 2.82 us: 1.42x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.06 sec: 1.42x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.83 us: 1.41x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 67.0 ms: 1.41x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 325 us: 1.40x faster                                                         |
| regex_compile            | 190 ms                                                       | 138 ms: 1.38x faster                                                         |
| coroutines               | 30.3 ms                                                      | 22.3 ms: 1.36x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.8 ms: 1.35x faster                                                        |
| django_template          | 50.2 ms                                                      | 37.2 ms: 1.35x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 23.5 ms: 1.34x faster                                                        |
| scimark_fft              | 361 ms                                                       | 272 ms: 1.33x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                       |
| fannkuch                 | 483 ms                                                       | 366 ms: 1.32x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 57.6 ms: 1.32x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 145 ms: 1.31x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.30x faster                                                       |
| mako                     | 14.7 ms                                                      | 11.3 ms: 1.30x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 817 ms: 1.28x faster                                                         |
| sympy_sum                | 193 ms                                                       | 150 ms: 1.28x faster                                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.7 ms: 1.28x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.7 ms: 1.24x faster                                                        |
| 2to3                     | 350 ms                                                       | 282 ms: 1.24x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 65.4 ms: 1.24x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.10 ms: 1.24x faster                                                        |
| sympy_str                | 360 ms                                                       | 292 ms: 1.23x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 930 us: 1.23x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 23.0 ms: 1.22x faster                                                        |
| nqueens                  | 115 ms                                                       | 94.1 ms: 1.22x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.2 us: 1.20x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 120 ms: 1.20x faster                                                         |
| sympy_expand             | 600 ms                                                       | 500 ms: 1.20x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.89 sec: 1.18x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 53.7 ms: 1.18x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 59.6 ms: 1.18x faster                                                        |
| regex_dna                | 261 ms                                                       | 223 ms: 1.17x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 80.9 ms: 1.14x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.65 sec: 1.13x faster                                                       |
| json                     | 5.86 ms                                                      | 5.22 ms: 1.12x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.84 us: 1.05x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 105 ms: 1.05x faster                                                         |
| meteor_contest           | 138 ms                                                       | 133 ms: 1.04x faster                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.00 ms: 1.03x faster                                                        |
| async_generators         | 421 ms                                                       | 429 ms: 1.02x slower                                                         |
| pidigits                 | 271 ms                                                       | 286 ms: 1.06x slower                                                         |
| telco                    | 7.23 ms                                                      | 8.03 ms: 1.11x slower                                                        |
| coverage                 | 63.3 ms                                                      | 75.9 ms: 1.20x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.06 ms: 1.24x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 5.34 ms: 1.56x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.89 ms: 1.64x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.36 sec: 213.75x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.27x faster                                                                 |

Benchmark hidden because not significant (3): regex_v8, asyncio_websockets, xml_etree_parse
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250116-3.14.0a4+-09f3d0f-CLANG/bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.350x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.33x
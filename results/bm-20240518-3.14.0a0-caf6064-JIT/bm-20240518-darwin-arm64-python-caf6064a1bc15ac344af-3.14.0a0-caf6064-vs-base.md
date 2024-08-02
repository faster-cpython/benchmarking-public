# Results vs. base

- fork: python
- ref: caf6064a1bc15ac344af
- machine: darwin-arm64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 182 ms                                                                                                          | 192 ms: 1.06x slower                                                                                                |
| chameleon      | 4.29 ms                                                                                                         | 4.45 ms: 1.04x slower                                                                                               |
| docutils       | 1.44 sec                                                                                                        | 1.52 sec: 1.06x slower                                                                                              |
| Geometric mean | (ref)                                                                                                           | 1.03x slower                                                                                                        |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|---------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| async_tree_eager_tg | 41.4 ms                                                                                                         | 41.7 ms: 1.01x slower                                                                                               |
| async_tree_eager    | 61.0 ms                                                                                                         | 63.1 ms: 1.03x slower                                                                                               |
| Geometric mean      | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmark hidden because not significant (14): async_tree_eager_cpu_io_mixed_tg, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_eager_io_tg, async_tree_eager_io, async_tree_eager_memoization_tg, async_tree_memoization, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_none, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| float          | 48.2 ms                                                                                                         | 47.5 ms: 1.02x faster                                                                                               |
| pidigits       | 281 ms                                                                                                          | 282 ms: 1.00x slower                                                                                                |
| nbody          | 60.3 ms                                                                                                         | 63.5 ms: 1.05x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                                                                         | 17.4 ms: 1.00x slower                                                                                               |
| regex_dna      | 149 ms                                                                                                          | 149 ms: 1.00x slower                                                                                                |
| regex_effbot   | 2.56 ms                                                                                                         | 2.58 ms: 1.01x slower                                                                                               |
| regex_compile  | 68.2 ms                                                                                                         | 72.5 ms: 1.06x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.02x slower                                                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.46 sec                                                                                                        | 1.25 sec: 1.17x faster                                                                                              |
| unpickle_pure_python | 140 us                                                                                                          | 131 us: 1.07x faster                                                                                                |
| xml_etree_process    | 36.9 ms                                                                                                         | 35.3 ms: 1.05x faster                                                                                               |
| pickle_pure_python   | 178 us                                                                                                          | 172 us: 1.04x faster                                                                                                |
| json_dumps           | 6.29 ms                                                                                                         | 6.10 ms: 1.03x faster                                                                                               |
| xml_etree_generate   | 52.2 ms                                                                                                         | 50.8 ms: 1.03x faster                                                                                               |
| pickle_list          | 3.00 us                                                                                                         | 2.92 us: 1.03x faster                                                                                               |
| xml_etree_parse      | 104 ms                                                                                                          | 102 ms: 1.02x faster                                                                                                |
| xml_etree_iterparse  | 71.6 ms                                                                                                         | 71.1 ms: 1.01x faster                                                                                               |
| unpickle_list        | 2.90 us                                                                                                         | 2.89 us: 1.00x faster                                                                                               |
| pickle_dict          | 18.3 us                                                                                                         | 18.2 us: 1.00x faster                                                                                               |
| pickle               | 7.45 us                                                                                                         | 7.48 us: 1.00x slower                                                                                               |
| json_loads           | 16.9 us                                                                                                         | 17.1 us: 1.01x slower                                                                                               |
| Geometric mean       | (ref)                                                                                                           | 1.03x faster                                                                                                        |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 14.0 ms                                                                                                         | 15.3 ms: 1.09x slower                                                                                               |
| python_startup_no_site | 11.5 ms                                                                                                         | 12.8 ms: 1.12x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.10x slower                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.91 ms                                                                                                         | 6.38 ms: 1.08x faster                                                                                               |
| django_template | 19.4 ms                                                                                                         | 21.0 ms: 1.08x slower                                                                                               |
| genshi_text     | 13.7 ms                                                                                                         | 17.0 ms: 1.24x slower                                                                                               |
| genshi_xml      | 29.7 ms                                                                                                         | 40.4 ms: 1.36x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.14x slower                                                                                                        |

All benchmarks:
===============

| Benchmark                | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|--------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| tomli_loads              | 1.46 sec                                                                                                        | 1.25 sec: 1.17x faster                                                                                              |
| mako                     | 6.91 ms                                                                                                         | 6.38 ms: 1.08x faster                                                                                               |
| unpickle_pure_python     | 140 us                                                                                                          | 131 us: 1.07x faster                                                                                                |
| fannkuch                 | 249 ms                                                                                                          | 235 ms: 1.06x faster                                                                                                |
| deepcopy_memo            | 22.6 us                                                                                                         | 21.5 us: 1.05x faster                                                                                               |
| xml_etree_process        | 36.9 ms                                                                                                         | 35.3 ms: 1.05x faster                                                                                               |
| pickle_pure_python       | 178 us                                                                                                          | 172 us: 1.04x faster                                                                                                |
| json_dumps               | 6.29 ms                                                                                                         | 6.10 ms: 1.03x faster                                                                                               |
| xml_etree_generate       | 52.2 ms                                                                                                         | 50.8 ms: 1.03x faster                                                                                               |
| pickle_list              | 3.00 us                                                                                                         | 2.92 us: 1.03x faster                                                                                               |
| xml_etree_parse          | 104 ms                                                                                                          | 102 ms: 1.02x faster                                                                                                |
| pyflate                  | 320 ms                                                                                                          | 314 ms: 1.02x faster                                                                                                |
| float                    | 48.2 ms                                                                                                         | 47.5 ms: 1.02x faster                                                                                               |
| logging_format           | 3.35 us                                                                                                         | 3.31 us: 1.01x faster                                                                                               |
| logging_simple           | 3.07 us                                                                                                         | 3.03 us: 1.01x faster                                                                                               |
| xml_etree_iterparse      | 71.6 ms                                                                                                         | 71.1 ms: 1.01x faster                                                                                               |
| unpickle_list            | 2.90 us                                                                                                         | 2.89 us: 1.00x faster                                                                                               |
| pickle_dict              | 18.3 us                                                                                                         | 18.2 us: 1.00x faster                                                                                               |
| pidigits                 | 281 ms                                                                                                          | 282 ms: 1.00x slower                                                                                                |
| regex_v8                 | 17.3 ms                                                                                                         | 17.4 ms: 1.00x slower                                                                                               |
| asyncio_websockets       | 408 ms                                                                                                          | 409 ms: 1.00x slower                                                                                                |
| coroutines               | 15.9 ms                                                                                                         | 15.9 ms: 1.00x slower                                                                                               |
| regex_dna                | 149 ms                                                                                                          | 149 ms: 1.00x slower                                                                                                |
| pickle                   | 7.45 us                                                                                                         | 7.48 us: 1.00x slower                                                                                               |
| async_tree_eager_tg      | 41.4 ms                                                                                                         | 41.7 ms: 1.01x slower                                                                                               |
| regex_effbot             | 2.56 ms                                                                                                         | 2.58 ms: 1.01x slower                                                                                               |
| json_loads               | 16.9 us                                                                                                         | 17.1 us: 1.01x slower                                                                                               |
| telco                    | 4.61 ms                                                                                                         | 4.65 ms: 1.01x slower                                                                                               |
| pprint_safe_repr         | 462 ms                                                                                                          | 466 ms: 1.01x slower                                                                                                |
| typing_runtime_protocols | 91.7 us                                                                                                         | 92.5 us: 1.01x slower                                                                                               |
| asyncio_tcp_ssl          | 1.28 sec                                                                                                        | 1.29 sec: 1.01x slower                                                                                              |
| pathlib                  | 22.5 ms                                                                                                         | 22.7 ms: 1.01x slower                                                                                               |
| create_gc_cycles         | 910 us                                                                                                          | 920 us: 1.01x slower                                                                                                |
| deepcopy_reduce          | 1.79 us                                                                                                         | 1.81 us: 1.01x slower                                                                                               |
| pprint_pformat           | 943 ms                                                                                                          | 955 ms: 1.01x slower                                                                                                |
| thrift                   | 428 us                                                                                                          | 434 us: 1.01x slower                                                                                                |
| dask                     | 220 ms                                                                                                          | 223 ms: 1.01x slower                                                                                                |
| generators               | 22.9 ms                                                                                                         | 23.2 ms: 1.01x slower                                                                                               |
| sqlite_synth             | 1.54 us                                                                                                         | 1.57 us: 1.02x slower                                                                                               |
| deepcopy                 | 200 us                                                                                                          | 204 us: 1.02x slower                                                                                                |
| scimark_fft              | 180 ms                                                                                                          | 184 ms: 1.02x slower                                                                                                |
| go                       | 100 ms                                                                                                          | 103 ms: 1.03x slower                                                                                                |
| sympy_sum                | 69.9 ms                                                                                                         | 72.3 ms: 1.03x slower                                                                                               |
| async_tree_eager         | 61.0 ms                                                                                                         | 63.1 ms: 1.03x slower                                                                                               |
| logging_silent           | 60.0 ns                                                                                                         | 62.1 ns: 1.03x slower                                                                                               |
| richards                 | 31.1 ms                                                                                                         | 32.2 ms: 1.04x slower                                                                                               |
| flaskblogging            | 3.40 ms                                                                                                         | 3.53 ms: 1.04x slower                                                                                               |
| chameleon                | 4.29 ms                                                                                                         | 4.45 ms: 1.04x slower                                                                                               |
| meteor_contest           | 69.8 ms                                                                                                         | 72.5 ms: 1.04x slower                                                                                               |
| bench_thread_pool        | 463 us                                                                                                          | 482 us: 1.04x slower                                                                                                |
| sympy_expand             | 227 ms                                                                                                          | 237 ms: 1.05x slower                                                                                                |
| sympy_str                | 132 ms                                                                                                          | 138 ms: 1.05x slower                                                                                                |
| crypto_pyaes             | 49.6 ms                                                                                                         | 51.9 ms: 1.05x slower                                                                                               |
| scimark_sparse_mat_mult  | 2.77 ms                                                                                                         | 2.90 ms: 1.05x slower                                                                                               |
| scimark_monte_carlo      | 42.2 ms                                                                                                         | 44.3 ms: 1.05x slower                                                                                               |
| nbody                    | 60.3 ms                                                                                                         | 63.5 ms: 1.05x slower                                                                                               |
| async_generators         | 279 ms                                                                                                          | 294 ms: 1.05x slower                                                                                                |
| sympy_integrate          | 10.3 ms                                                                                                         | 10.9 ms: 1.05x slower                                                                                               |
| richards_super           | 34.3 ms                                                                                                         | 36.2 ms: 1.06x slower                                                                                               |
| docutils                 | 1.44 sec                                                                                                        | 1.52 sec: 1.06x slower                                                                                              |
| 2to3                     | 182 ms                                                                                                          | 192 ms: 1.06x slower                                                                                                |
| gc_traversal             | 2.46 ms                                                                                                         | 2.61 ms: 1.06x slower                                                                                               |
| scimark_sor              | 94.0 ms                                                                                                         | 99.9 ms: 1.06x slower                                                                                               |
| sqlglot_optimize         | 31.0 ms                                                                                                         | 33.0 ms: 1.06x slower                                                                                               |
| pycparser                | 632 ms                                                                                                          | 671 ms: 1.06x slower                                                                                                |
| regex_compile            | 68.2 ms                                                                                                         | 72.5 ms: 1.06x slower                                                                                               |
| bench_mp_pool            | 45.7 ms                                                                                                         | 49.0 ms: 1.07x slower                                                                                               |
| django_template          | 19.4 ms                                                                                                         | 21.0 ms: 1.08x slower                                                                                               |
| mdp                      | 1.49 sec                                                                                                        | 1.62 sec: 1.09x slower                                                                                              |
| hexiom                   | 4.08 ms                                                                                                         | 4.43 ms: 1.09x slower                                                                                               |
| python_startup           | 14.0 ms                                                                                                         | 15.3 ms: 1.09x slower                                                                                               |
| nqueens                  | 52.6 ms                                                                                                         | 57.4 ms: 1.09x slower                                                                                               |
| raytrace                 | 147 ms                                                                                                          | 161 ms: 1.10x slower                                                                                                |
| python_startup_no_site   | 11.5 ms                                                                                                         | 12.8 ms: 1.12x slower                                                                                               |
| sqlglot_transpile        | 892 us                                                                                                          | 1.01 ms: 1.13x slower                                                                                               |
| sqlglot_parse            | 733 us                                                                                                          | 833 us: 1.14x slower                                                                                                |
| chaos                    | 34.3 ms                                                                                                         | 39.2 ms: 1.14x slower                                                                                               |
| comprehensions           | 10.7 us                                                                                                         | 12.3 us: 1.15x slower                                                                                               |
| deltablue                | 2.14 ms                                                                                                         | 2.48 ms: 1.16x slower                                                                                               |
| scimark_lu               | 66.8 ms                                                                                                         | 78.6 ms: 1.18x slower                                                                                               |
| genshi_text              | 13.7 ms                                                                                                         | 17.0 ms: 1.24x slower                                                                                               |
| genshi_xml               | 29.7 ms                                                                                                         | 40.4 ms: 1.36x slower                                                                                               |
| Geometric mean           | (ref)                                                                                                           | 1.03x slower                                                                                                        |

Benchmark hidden because not significant (22): json, coverage, asyncio_tcp, html5lib, async_tree_eager_cpu_io_mixed_tg, spectral_norm, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_eager_io_tg, unpickle, async_tree_eager_io, async_tree_eager_memoization_tg, async_tree_memoization, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_none, async_tree_eager_memoization, tornado_http, pylint
Ignored benchmarks (1) of results/bm-20240518-3.14.0a0-caf6064/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.32x
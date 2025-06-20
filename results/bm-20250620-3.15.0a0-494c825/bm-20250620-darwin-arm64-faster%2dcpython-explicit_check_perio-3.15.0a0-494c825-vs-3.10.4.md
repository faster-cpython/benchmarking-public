# Results vs. 3.10.4

- fork: faster-cpython
- ref: explicit_check_perio
- machine: darwin-arm64
- commit hash: 494c825
- commit date: 2025-06-20
- overall geometric mean: 1.240x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 188 ms: 1.07x faster                                                            |
| docutils       | 1.74 sec                                               | 1.52 sec: 1.14x faster                                                          |
| html5lib       | 43.5 ms                                                | 34.4 ms: 1.27x faster                                                           |
| sphinx         | 729 ms                                                 | 619 ms: 1.18x faster                                                            |
| Geometric mean | (ref)                                                  | 1.16x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.4 ms: 5.34x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.20x faster                                                            |
| async_tree_eager_io           | 1.01 sec                                               | 396 ms: 2.56x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 418 ms: 2.43x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 216 ms: 2.23x faster                                                            |
| async_tree_none               | 391 ms                                                 | 183 ms: 2.14x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 368 ms: 1.82x faster                                                            |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 434 ms: 1.54x faster                                                            |
| coroutines                    | 20.5 ms                                                | 18.9 ms: 1.09x faster                                                           |
| async_generators              | 233 ms                                                 | 275 ms: 1.18x slower                                                            |
| Geometric mean                | (ref)                                                  | 1.92x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 57.9 ms: 1.25x faster                                                           |
| nbody          | 92.5 ms                                                | 85.2 ms: 1.09x faster                                                           |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 143 ms: 1.22x faster                                                            |
| regex_v8       | 19.1 ms                                                | 16.2 ms: 1.18x faster                                                           |
| regex_compile  | 95.6 ms                                                | 82.3 ms: 1.16x faster                                                           |
| regex_effbot   | 2.34 ms                                                | 2.34 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 8.31 ms                                                | 6.87 ms: 1.21x faster                                                           |
| tomli_loads          | 1.72 sec                                               | 1.47 sec: 1.17x faster                                                          |
| pickle_pure_python   | 285 us                                                 | 244 us: 1.17x faster                                                            |
| unpickle_pure_python | 198 us                                                 | 180 us: 1.10x faster                                                            |
| xml_etree_parse      | 109 ms                                                 | 105 ms: 1.05x faster                                                            |
| xml_etree_process    | 44.6 ms                                                | 43.9 ms: 1.02x faster                                                           |
| xml_etree_generate   | 53.9 ms                                                | 59.1 ms: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                    |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.9 ms: 1.04x faster                                                           |
| python_startup_no_site | 12.8 ms                                                | 14.2 ms: 1.11x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 9.21 ms: 1.06x faster                                                           |
| genshi_xml      | 35.1 ms                                                | 36.4 ms: 1.03x slower                                                           |
| django_template | 24.4 ms                                                | 25.3 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.4 ms: 5.34x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.20x faster                                                            |
| typing_runtime_protocols      | 326 us                                                 | 111 us: 2.93x faster                                                            |
| subparsers                    | 39.8 ms                                                | 14.9 ms: 2.67x faster                                                           |
| async_tree_eager_io           | 1.01 sec                                               | 396 ms: 2.56x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 418 ms: 2.43x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 216 ms: 2.23x faster                                                            |
| async_tree_none               | 391 ms                                                 | 183 ms: 2.14x faster                                                            |
| mdp                           | 1.65 sec                                               | 829 ms: 1.99x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 368 ms: 1.82x faster                                                            |
| deltablue                     | 4.99 ms                                                | 2.87 ms: 1.74x faster                                                           |
| go                            | 163 ms                                                 | 100 ms: 1.63x faster                                                            |
| deepcopy                      | 276 us                                                 | 178 us: 1.55x faster                                                            |
| scimark_sor                   | 140 ms                                                 | 90.5 ms: 1.55x faster                                                           |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 434 ms: 1.54x faster                                                            |
| deepcopy_memo                 | 34.7 us                                                | 22.6 us: 1.54x faster                                                           |
| raytrace                      | 327 ms                                                 | 213 ms: 1.53x faster                                                            |
| richards_super                | 61.0 ms                                                | 42.5 ms: 1.43x faster                                                           |
| chaos                         | 67.7 ms                                                | 47.3 ms: 1.43x faster                                                           |
| richards                      | 52.3 ms                                                | 37.8 ms: 1.38x faster                                                           |
| k_core                        | 2.01 sec                                               | 1.47 sec: 1.37x faster                                                          |
| scimark_monte_carlo           | 72.4 ms                                                | 53.1 ms: 1.36x faster                                                           |
| pylint                        | 231 ms                                                 | 170 ms: 1.36x faster                                                            |
| dulwich_log                   | 35.6 ms                                                | 26.6 ms: 1.34x faster                                                           |
| pyflate                       | 448 ms                                                 | 335 ms: 1.33x faster                                                            |
| comprehensions                | 17.3 us                                                | 13.3 us: 1.31x faster                                                           |
| spectral_norm                 | 95.3 ms                                                | 74.0 ms: 1.29x faster                                                           |
| html5lib                      | 43.5 ms                                                | 34.4 ms: 1.27x faster                                                           |
| float                         | 72.4 ms                                                | 57.9 ms: 1.25x faster                                                           |
| regex_dna                     | 175 ms                                                 | 143 ms: 1.22x faster                                                            |
| json_dumps                    | 8.31 ms                                                | 6.87 ms: 1.21x faster                                                           |
| hexiom                        | 6.25 ms                                                | 5.17 ms: 1.21x faster                                                           |
| deepcopy_reduce               | 2.32 us                                                | 1.93 us: 1.20x faster                                                           |
| crypto_pyaes                  | 73.3 ms                                                | 61.1 ms: 1.20x faster                                                           |
| pycparser                     | 887 ms                                                 | 742 ms: 1.20x faster                                                            |
| scimark_lu                    | 103 ms                                                 | 85.8 ms: 1.20x faster                                                           |
| thrift                        | 562 us                                                 | 471 us: 1.19x faster                                                            |
| regex_v8                      | 19.1 ms                                                | 16.2 ms: 1.18x faster                                                           |
| sphinx                        | 729 ms                                                 | 619 ms: 1.18x faster                                                            |
| tomli_loads                   | 1.72 sec                                               | 1.47 sec: 1.17x faster                                                          |
| pickle_pure_python            | 285 us                                                 | 244 us: 1.17x faster                                                            |
| regex_compile                 | 95.6 ms                                                | 82.3 ms: 1.16x faster                                                           |
| sympy_integrate               | 13.2 ms                                                | 11.4 ms: 1.15x faster                                                           |
| pathlib                       | 25.7 ms                                                | 22.6 ms: 1.14x faster                                                           |
| docutils                      | 1.74 sec                                               | 1.52 sec: 1.14x faster                                                          |
| logging_format                | 5.03 us                                                | 4.43 us: 1.13x faster                                                           |
| sympy_sum                     | 92.7 ms                                                | 82.2 ms: 1.13x faster                                                           |
| scimark_fft                   | 225 ms                                                 | 202 ms: 1.11x faster                                                            |
| logging_simple                | 4.59 us                                                | 4.14 us: 1.11x faster                                                           |
| unpickle_pure_python          | 198 us                                                 | 180 us: 1.10x faster                                                            |
| nbody                         | 92.5 ms                                                | 85.2 ms: 1.09x faster                                                           |
| coroutines                    | 20.5 ms                                                | 18.9 ms: 1.09x faster                                                           |
| 2to3                          | 201 ms                                                 | 188 ms: 1.07x faster                                                            |
| mako                          | 9.81 ms                                                | 9.21 ms: 1.06x faster                                                           |
| sympy_str                     | 166 ms                                                 | 156 ms: 1.06x faster                                                            |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.22 ms: 1.06x faster                                                           |
| xml_etree_parse               | 109 ms                                                 | 105 ms: 1.05x faster                                                            |
| connected_components          | 318 ms                                                 | 304 ms: 1.05x faster                                                            |
| bpe_tokeniser                 | 3.44 sec                                               | 3.29 sec: 1.05x faster                                                          |
| json                          | 3.10 ms                                                | 2.97 ms: 1.04x faster                                                           |
| meteor_contest                | 77.8 ms                                                | 74.6 ms: 1.04x faster                                                           |
| python_startup                | 19.6 ms                                                | 18.9 ms: 1.04x faster                                                           |
| pprint_pformat                | 1.33 sec                                               | 1.28 sec: 1.03x faster                                                          |
| pprint_safe_repr              | 648 ms                                                 | 632 ms: 1.02x faster                                                            |
| dask                          | 789 ms                                                 | 772 ms: 1.02x faster                                                            |
| xml_etree_process             | 44.6 ms                                                | 43.9 ms: 1.02x faster                                                           |
| sympy_expand                  | 269 ms                                                 | 265 ms: 1.01x faster                                                            |
| generators                    | 31.7 ms                                                | 31.5 ms: 1.01x faster                                                           |
| fannkuch                      | 303 ms                                                 | 303 ms: 1.00x slower                                                            |
| shortest_path                 | 328 ms                                                 | 329 ms: 1.00x slower                                                            |
| regex_effbot                  | 2.34 ms                                                | 2.34 ms: 1.00x slower                                                           |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                            |
| many_optionals                | 486 us                                                 | 501 us: 1.03x slower                                                            |
| genshi_xml                    | 35.1 ms                                                | 36.4 ms: 1.03x slower                                                           |
| django_template               | 24.4 ms                                                | 25.3 ms: 1.04x slower                                                           |
| nqueens                       | 63.8 ms                                                | 69.9 ms: 1.09x slower                                                           |
| xml_etree_generate            | 53.9 ms                                                | 59.1 ms: 1.10x slower                                                           |
| sqlite_synth                  | 1.48 us                                                | 1.62 us: 1.10x slower                                                           |
| python_startup_no_site        | 12.8 ms                                                | 14.2 ms: 1.11x slower                                                           |
| create_gc_cycles              | 1.16 ms                                                | 1.35 ms: 1.16x slower                                                           |
| async_generators              | 233 ms                                                 | 275 ms: 1.18x slower                                                            |
| gc_traversal                  | 2.71 ms                                                | 3.19 ms: 1.18x slower                                                           |
| coverage                      | 41.2 ms                                                | 49.7 ms: 1.21x slower                                                           |
| telco                         | 3.49 ms                                                | 4.75 ms: 1.36x slower                                                           |
| logging_silent                | 117 ns                                                 | 346 ns: 2.96x slower                                                            |
| Geometric mean                | (ref)                                                  | 1.22x faster                                                                    |

Benchmark hidden because not significant (4): xml_etree_iterparse, asyncio_websockets, json_loads, genshi_text
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250620-3.15.0a0-494c825/bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.240x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.17x
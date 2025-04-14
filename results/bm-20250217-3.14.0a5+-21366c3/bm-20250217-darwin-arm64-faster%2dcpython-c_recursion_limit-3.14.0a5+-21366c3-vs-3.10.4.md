# Results vs. 3.10.4

- fork: faster-cpython
- ref: c_recursion_limit
- machine: darwin-arm64
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.255x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 205 ms: 1.02x slower                                                          |
| docutils       | 1.74 sec                                               | 1.51 sec: 1.15x faster                                                        |
| html5lib       | 43.5 ms                                                | 32.9 ms: 1.32x faster                                                         |
| sphinx         | 729 ms                                                 | 608 ms: 1.20x faster                                                          |
| Geometric mean | (ref)                                                  | 1.16x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 74.2 ms: 5.28x faster                                                         |
| async_tree_eager_memoization  | 483 ms                                                 | 152 ms: 3.18x faster                                                          |
| async_tree_eager_io           | 1.01 sec                                               | 409 ms: 2.48x faster                                                          |
| async_tree_io                 | 1.02 sec                                               | 424 ms: 2.40x faster                                                          |
| async_tree_memoization        | 481 ms                                                 | 221 ms: 2.18x faster                                                          |
| async_tree_none               | 391 ms                                                 | 184 ms: 2.13x faster                                                          |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 370 ms: 1.81x faster                                                          |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 437 ms: 1.53x faster                                                          |
| coroutines                    | 20.5 ms                                                | 18.6 ms: 1.10x faster                                                         |
| async_generators              | 233 ms                                                 | 269 ms: 1.15x slower                                                          |
| Geometric mean                | (ref)                                                  | 1.91x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 54.2 ms: 1.34x faster                                                         |
| nbody          | 92.5 ms                                                | 91.9 ms: 1.01x faster                                                         |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                          |
| regex_compile  | 95.6 ms                                                | 77.5 ms: 1.23x faster                                                         |
| regex_v8       | 19.1 ms                                                | 16.9 ms: 1.13x faster                                                         |
| regex_effbot   | 2.34 ms                                                | 2.30 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.15x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 232 us: 1.23x faster                                                          |
| tomli_loads          | 1.72 sec                                               | 1.44 sec: 1.19x faster                                                        |
| unpickle_pure_python | 198 us                                                 | 170 us: 1.16x faster                                                          |
| json_dumps           | 8.31 ms                                                | 7.53 ms: 1.10x faster                                                         |
| xml_etree_parse      | 109 ms                                                 | 102 ms: 1.08x faster                                                          |
| xml_etree_process    | 44.6 ms                                                | 43.0 ms: 1.04x faster                                                         |
| json_loads           | 16.6 us                                                | 17.8 us: 1.08x slower                                                         |
| xml_etree_generate   | 53.9 ms                                                | 58.4 ms: 1.08x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                  |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.1 ms: 1.08x faster                                                         |
| python_startup_no_site | 12.8 ms                                                | 13.4 ms: 1.05x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.18 ms: 1.20x faster                                                         |
| genshi_text     | 17.7 ms                                                | 16.3 ms: 1.09x faster                                                         |
| genshi_xml      | 35.1 ms                                                | 33.8 ms: 1.04x faster                                                         |
| django_template | 24.4 ms                                                | 24.1 ms: 1.01x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                  |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 74.2 ms: 5.28x faster                                                         |
| typing_runtime_protocols      | 326 us                                                 | 101 us: 3.22x faster                                                          |
| async_tree_eager_memoization  | 483 ms                                                 | 152 ms: 3.18x faster                                                          |
| subparsers                    | 39.8 ms                                                | 12.9 ms: 3.10x faster                                                         |
| async_tree_eager_io           | 1.01 sec                                               | 409 ms: 2.48x faster                                                          |
| async_tree_io                 | 1.02 sec                                               | 424 ms: 2.40x faster                                                          |
| async_tree_memoization        | 481 ms                                                 | 221 ms: 2.18x faster                                                          |
| async_tree_none               | 391 ms                                                 | 184 ms: 2.13x faster                                                          |
| deltablue                     | 4.99 ms                                                | 2.76 ms: 1.81x faster                                                         |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 370 ms: 1.81x faster                                                          |
| go                            | 163 ms                                                 | 94.6 ms: 1.73x faster                                                         |
| deepcopy_memo                 | 34.7 us                                                | 20.9 us: 1.66x faster                                                         |
| deepcopy                      | 276 us                                                 | 167 us: 1.66x faster                                                          |
| logging_silent                | 117 ns                                                 | 73.4 ns: 1.60x faster                                                         |
| raytrace                      | 327 ms                                                 | 212 ms: 1.54x faster                                                          |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 437 ms: 1.53x faster                                                          |
| chaos                         | 67.7 ms                                                | 44.5 ms: 1.52x faster                                                         |
| sqlglot_parse                 | 1.35 ms                                                | 888 us: 1.52x faster                                                          |
| scimark_sor                   | 140 ms                                                 | 92.7 ms: 1.51x faster                                                         |
| sqlglot_transpile             | 1.56 ms                                                | 1.08 ms: 1.45x faster                                                         |
| scimark_monte_carlo           | 72.4 ms                                                | 50.1 ms: 1.45x faster                                                         |
| richards_super                | 61.0 ms                                                | 42.7 ms: 1.43x faster                                                         |
| pylint                        | 231 ms                                                 | 170 ms: 1.36x faster                                                          |
| float                         | 72.4 ms                                                | 54.2 ms: 1.34x faster                                                         |
| comprehensions                | 17.3 us                                                | 13.0 us: 1.33x faster                                                         |
| html5lib                      | 43.5 ms                                                | 32.9 ms: 1.32x faster                                                         |
| deepcopy_reduce               | 2.32 us                                                | 1.76 us: 1.32x faster                                                         |
| richards                      | 52.3 ms                                                | 39.8 ms: 1.31x faster                                                         |
| k_core                        | 2.01 sec                                               | 1.54 sec: 1.30x faster                                                        |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.10 ms: 1.28x faster                                                         |
| pyflate                       | 448 ms                                                 | 351 ms: 1.28x faster                                                          |
| pycparser                     | 887 ms                                                 | 703 ms: 1.26x faster                                                          |
| crypto_pyaes                  | 73.3 ms                                                | 58.6 ms: 1.25x faster                                                         |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                          |
| logging_format                | 5.03 us                                                | 4.07 us: 1.24x faster                                                         |
| regex_compile                 | 95.6 ms                                                | 77.5 ms: 1.23x faster                                                         |
| scimark_lu                    | 103 ms                                                 | 83.4 ms: 1.23x faster                                                         |
| pickle_pure_python            | 285 us                                                 | 232 us: 1.23x faster                                                          |
| logging_simple                | 4.59 us                                                | 3.75 us: 1.22x faster                                                         |
| spectral_norm                 | 95.3 ms                                                | 77.9 ms: 1.22x faster                                                         |
| sqlalchemy_declarative        | 75.7 ms                                                | 62.5 ms: 1.21x faster                                                         |
| thrift                        | 562 us                                                 | 465 us: 1.21x faster                                                          |
| pprint_pformat                | 1.33 sec                                               | 1.10 sec: 1.21x faster                                                        |
| sphinx                        | 729 ms                                                 | 608 ms: 1.20x faster                                                          |
| mako                          | 9.81 ms                                                | 8.18 ms: 1.20x faster                                                         |
| tomli_loads                   | 1.72 sec                                               | 1.44 sec: 1.19x faster                                                        |
| pprint_safe_repr              | 648 ms                                                 | 542 ms: 1.19x faster                                                          |
| hexiom                        | 6.25 ms                                                | 5.26 ms: 1.19x faster                                                         |
| dulwich_log                   | 35.6 ms                                                | 30.0 ms: 1.19x faster                                                         |
| unpickle_pure_python          | 198 us                                                 | 170 us: 1.16x faster                                                          |
| sympy_sum                     | 92.7 ms                                                | 80.1 ms: 1.16x faster                                                         |
| docutils                      | 1.74 sec                                               | 1.51 sec: 1.15x faster                                                        |
| scimark_fft                   | 225 ms                                                 | 198 ms: 1.14x faster                                                          |
| regex_v8                      | 19.1 ms                                                | 16.9 ms: 1.13x faster                                                         |
| pathlib                       | 25.7 ms                                                | 23.2 ms: 1.11x faster                                                         |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.08 ms: 1.11x faster                                                         |
| coroutines                    | 20.5 ms                                                | 18.6 ms: 1.10x faster                                                         |
| json_dumps                    | 8.31 ms                                                | 7.53 ms: 1.10x faster                                                         |
| genshi_text                   | 17.7 ms                                                | 16.3 ms: 1.09x faster                                                         |
| generators                    | 31.7 ms                                                | 29.1 ms: 1.09x faster                                                         |
| python_startup                | 19.6 ms                                                | 18.1 ms: 1.08x faster                                                         |
| sympy_str                     | 166 ms                                                 | 154 ms: 1.08x faster                                                          |
| xml_etree_parse               | 109 ms                                                 | 102 ms: 1.08x faster                                                          |
| sympy_integrate               | 13.2 ms                                                | 12.3 ms: 1.07x faster                                                         |
| bpe_tokeniser                 | 3.44 sec                                               | 3.20 sec: 1.07x faster                                                        |
| mdp                           | 1.65 sec                                               | 1.56 sec: 1.06x faster                                                        |
| sympy_expand                  | 269 ms                                                 | 255 ms: 1.06x faster                                                          |
| sqlglot_optimize              | 37.2 ms                                                | 35.6 ms: 1.05x faster                                                         |
| bench_thread_pool             | 545 us                                                 | 522 us: 1.04x faster                                                          |
| genshi_xml                    | 35.1 ms                                                | 33.8 ms: 1.04x faster                                                         |
| xml_etree_process             | 44.6 ms                                                | 43.0 ms: 1.04x faster                                                         |
| many_optionals                | 486 us                                                 | 468 us: 1.04x faster                                                          |
| json                          | 3.10 ms                                                | 3.00 ms: 1.03x faster                                                         |
| fannkuch                      | 303 ms                                                 | 294 ms: 1.03x faster                                                          |
| regex_effbot                  | 2.34 ms                                                | 2.30 ms: 1.01x faster                                                         |
| django_template               | 24.4 ms                                                | 24.1 ms: 1.01x faster                                                         |
| nbody                         | 92.5 ms                                                | 91.9 ms: 1.01x faster                                                         |
| connected_components          | 318 ms                                                 | 316 ms: 1.01x faster                                                          |
| meteor_contest                | 77.8 ms                                                | 78.0 ms: 1.00x slower                                                         |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                          |
| 2to3                          | 201 ms                                                 | 205 ms: 1.02x slower                                                          |
| sqlglot_normalize             | 192 ms                                                 | 196 ms: 1.02x slower                                                          |
| nqueens                       | 63.8 ms                                                | 65.7 ms: 1.03x slower                                                         |
| sqlite_synth                  | 1.48 us                                                | 1.54 us: 1.04x slower                                                         |
| shortest_path                 | 328 ms                                                 | 343 ms: 1.04x slower                                                          |
| python_startup_no_site        | 12.8 ms                                                | 13.4 ms: 1.05x slower                                                         |
| bench_mp_pool                 | 56.0 ms                                                | 59.7 ms: 1.07x slower                                                         |
| json_loads                    | 16.6 us                                                | 17.8 us: 1.08x slower                                                         |
| xml_etree_generate            | 53.9 ms                                                | 58.4 ms: 1.08x slower                                                         |
| create_gc_cycles              | 1.16 ms                                                | 1.29 ms: 1.11x slower                                                         |
| gc_traversal                  | 2.71 ms                                                | 3.11 ms: 1.15x slower                                                         |
| async_generators              | 233 ms                                                 | 269 ms: 1.15x slower                                                          |
| coverage                      | 41.2 ms                                                | 47.6 ms: 1.16x slower                                                         |
| telco                         | 3.49 ms                                                | 4.78 ms: 1.37x slower                                                         |
| Geometric mean                | (ref)                                                  | 1.25x faster                                                                  |

Benchmark hidden because not significant (2): asyncio_websockets, xml_etree_iterparse
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, tornado_http
Ignored benchmarks (8) of results/bm-20250217-3.14.0a5+-21366c3/bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.255x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.14x
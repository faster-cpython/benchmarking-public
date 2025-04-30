# Results vs. 3.10.4

- fork: faster-cpython
- ref: virtual_iterators
- machine: darwin-arm64
- commit hash: cad1946
- commit date: 2025-04-30
- overall geometric mean: 1.227x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 219 ms: 1.09x slower                                                          |
| docutils       | 1.74 sec                                               | 1.53 sec: 1.13x faster                                                        |
| html5lib       | 43.5 ms                                                | 34.8 ms: 1.25x faster                                                         |
| sphinx         | 729 ms                                                 | 619 ms: 1.18x faster                                                          |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|-------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 76.7 ms: 5.11x faster                                                         |
| async_tree_eager_memoization  | 483 ms                                                 | 154 ms: 3.14x faster                                                          |
| async_tree_eager_io           | 1.01 sec                                               | 410 ms: 2.47x faster                                                          |
| async_tree_io                 | 1.02 sec                                               | 425 ms: 2.40x faster                                                          |
| async_tree_memoization        | 481 ms                                                 | 226 ms: 2.13x faster                                                          |
| async_tree_none               | 391 ms                                                 | 188 ms: 2.08x faster                                                          |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 375 ms: 1.79x faster                                                          |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 441 ms: 1.52x faster                                                          |
| coroutines                    | 20.5 ms                                                | 19.7 ms: 1.04x faster                                                         |
| asyncio_websockets            | 242 ms                                                 | 244 ms: 1.01x slower                                                          |
| async_generators              | 233 ms                                                 | 277 ms: 1.19x slower                                                          |
| Geometric mean                | (ref)                                                  | 1.87x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 57.7 ms: 1.25x faster                                                         |
| nbody          | 92.5 ms                                                | 89.1 ms: 1.04x faster                                                         |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 140 ms: 1.25x faster                                                          |
| regex_v8       | 19.1 ms                                                | 15.8 ms: 1.21x faster                                                         |
| regex_compile  | 95.6 ms                                                | 85.4 ms: 1.12x faster                                                         |
| regex_effbot   | 2.34 ms                                                | 2.24 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                  | 1.15x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.72 sec                                               | 1.50 sec: 1.15x faster                                                        |
| pickle_pure_python   | 285 us                                                 | 251 us: 1.14x faster                                                          |
| unpickle_pure_python | 198 us                                                 | 183 us: 1.08x faster                                                          |
| xml_etree_parse      | 109 ms                                                 | 106 ms: 1.04x faster                                                          |
| json_dumps           | 8.31 ms                                                | 8.16 ms: 1.02x faster                                                         |
| xml_etree_process    | 44.6 ms                                                | 45.0 ms: 1.01x slower                                                         |
| xml_etree_iterparse  | 74.5 ms                                                | 75.7 ms: 1.02x slower                                                         |
| json_loads           | 16.6 us                                                | 18.8 us: 1.13x slower                                                         |
| xml_etree_generate   | 53.9 ms                                                | 61.4 ms: 1.14x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.8 ms: 1.01x slower                                                         |
| python_startup_no_site | 12.8 ms                                                | 14.7 ms: 1.15x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 9.07 ms: 1.08x faster                                                         |
| genshi_text     | 17.7 ms                                                | 18.2 ms: 1.03x slower                                                         |
| genshi_xml      | 35.1 ms                                                | 36.7 ms: 1.04x slower                                                         |
| django_template | 24.4 ms                                                | 25.6 ms: 1.05x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                  |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|-------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 76.7 ms: 5.11x faster                                                         |
| async_tree_eager_memoization  | 483 ms                                                 | 154 ms: 3.14x faster                                                          |
| typing_runtime_protocols      | 326 us                                                 | 107 us: 3.05x faster                                                          |
| subparsers                    | 39.8 ms                                                | 13.6 ms: 2.94x faster                                                         |
| async_tree_eager_io           | 1.01 sec                                               | 410 ms: 2.47x faster                                                          |
| async_tree_io                 | 1.02 sec                                               | 425 ms: 2.40x faster                                                          |
| async_tree_memoization        | 481 ms                                                 | 226 ms: 2.13x faster                                                          |
| async_tree_none               | 391 ms                                                 | 188 ms: 2.08x faster                                                          |
| mdp                           | 1.65 sec                                               | 855 ms: 1.93x faster                                                          |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 375 ms: 1.79x faster                                                          |
| deltablue                     | 4.99 ms                                                | 2.86 ms: 1.74x faster                                                         |
| raytrace                      | 327 ms                                                 | 203 ms: 1.61x faster                                                          |
| go                            | 163 ms                                                 | 102 ms: 1.60x faster                                                          |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 441 ms: 1.52x faster                                                          |
| deepcopy                      | 276 us                                                 | 184 us: 1.50x faster                                                          |
| scimark_sor                   | 140 ms                                                 | 93.8 ms: 1.49x faster                                                         |
| logging_silent                | 117 ns                                                 | 78.5 ns: 1.49x faster                                                         |
| deepcopy_memo                 | 34.7 us                                                | 23.6 us: 1.47x faster                                                         |
| chaos                         | 67.7 ms                                                | 46.8 ms: 1.45x faster                                                         |
| richards_super                | 61.0 ms                                                | 44.1 ms: 1.38x faster                                                         |
| scimark_monte_carlo           | 72.4 ms                                                | 53.6 ms: 1.35x faster                                                         |
| richards                      | 52.3 ms                                                | 39.4 ms: 1.33x faster                                                         |
| dulwich_log                   | 35.6 ms                                                | 27.2 ms: 1.31x faster                                                         |
| k_core                        | 2.01 sec                                               | 1.55 sec: 1.30x faster                                                        |
| pyflate                       | 448 ms                                                 | 346 ms: 1.29x faster                                                          |
| comprehensions                | 17.3 us                                                | 13.7 us: 1.26x faster                                                         |
| float                         | 72.4 ms                                                | 57.7 ms: 1.25x faster                                                         |
| html5lib                      | 43.5 ms                                                | 34.8 ms: 1.25x faster                                                         |
| regex_dna                     | 175 ms                                                 | 140 ms: 1.25x faster                                                          |
| spectral_norm                 | 95.3 ms                                                | 77.4 ms: 1.23x faster                                                         |
| scimark_lu                    | 103 ms                                                 | 83.3 ms: 1.23x faster                                                         |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.37 ms: 1.23x faster                                                         |
| regex_v8                      | 19.1 ms                                                | 15.8 ms: 1.21x faster                                                         |
| logging_format                | 5.03 us                                                | 4.23 us: 1.19x faster                                                         |
| crypto_pyaes                  | 73.3 ms                                                | 62.1 ms: 1.18x faster                                                         |
| deepcopy_reduce               | 2.32 us                                                | 1.97 us: 1.18x faster                                                         |
| sphinx                        | 729 ms                                                 | 619 ms: 1.18x faster                                                          |
| pycparser                     | 887 ms                                                 | 754 ms: 1.18x faster                                                          |
| hexiom                        | 6.25 ms                                                | 5.33 ms: 1.17x faster                                                         |
| logging_simple                | 4.59 us                                                | 3.94 us: 1.17x faster                                                         |
| sqlalchemy_declarative        | 75.7 ms                                                | 65.1 ms: 1.16x faster                                                         |
| pprint_pformat                | 1.33 sec                                               | 1.15 sec: 1.16x faster                                                        |
| tomli_loads                   | 1.72 sec                                               | 1.50 sec: 1.15x faster                                                        |
| pprint_safe_repr              | 648 ms                                                 | 568 ms: 1.14x faster                                                          |
| pickle_pure_python            | 285 us                                                 | 251 us: 1.14x faster                                                          |
| docutils                      | 1.74 sec                                               | 1.53 sec: 1.13x faster                                                        |
| regex_compile                 | 95.6 ms                                                | 85.4 ms: 1.12x faster                                                         |
| unpickle_pure_python          | 198 us                                                 | 183 us: 1.08x faster                                                          |
| mako                          | 9.81 ms                                                | 9.07 ms: 1.08x faster                                                         |
| scimark_fft                   | 225 ms                                                 | 209 ms: 1.08x faster                                                          |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.24 ms: 1.05x faster                                                         |
| coroutines                    | 20.5 ms                                                | 19.7 ms: 1.04x faster                                                         |
| regex_effbot                  | 2.34 ms                                                | 2.24 ms: 1.04x faster                                                         |
| nbody                         | 92.5 ms                                                | 89.1 ms: 1.04x faster                                                         |
| xml_etree_parse               | 109 ms                                                 | 106 ms: 1.04x faster                                                          |
| pathlib                       | 25.7 ms                                                | 25.2 ms: 1.02x faster                                                         |
| generators                    | 31.7 ms                                                | 31.0 ms: 1.02x faster                                                         |
| json_dumps                    | 8.31 ms                                                | 8.16 ms: 1.02x faster                                                         |
| bpe_tokeniser                 | 3.44 sec                                               | 3.38 sec: 1.02x faster                                                        |
| bench_thread_pool             | 545 us                                                 | 542 us: 1.01x faster                                                          |
| meteor_contest                | 77.8 ms                                                | 77.5 ms: 1.00x faster                                                         |
| connected_components          | 318 ms                                                 | 317 ms: 1.00x faster                                                          |
| many_optionals                | 486 us                                                 | 489 us: 1.01x slower                                                          |
| asyncio_websockets            | 242 ms                                                 | 244 ms: 1.01x slower                                                          |
| xml_etree_process             | 44.6 ms                                                | 45.0 ms: 1.01x slower                                                         |
| python_startup                | 19.6 ms                                                | 19.8 ms: 1.01x slower                                                         |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                          |
| xml_etree_iterparse           | 74.5 ms                                                | 75.7 ms: 1.02x slower                                                         |
| genshi_text                   | 17.7 ms                                                | 18.2 ms: 1.03x slower                                                         |
| shortest_path                 | 328 ms                                                 | 341 ms: 1.04x slower                                                          |
| json                          | 3.10 ms                                                | 3.24 ms: 1.04x slower                                                         |
| fannkuch                      | 303 ms                                                 | 316 ms: 1.04x slower                                                          |
| genshi_xml                    | 35.1 ms                                                | 36.7 ms: 1.04x slower                                                         |
| django_template               | 24.4 ms                                                | 25.6 ms: 1.05x slower                                                         |
| 2to3                          | 201 ms                                                 | 219 ms: 1.09x slower                                                          |
| sqlite_synth                  | 1.48 us                                                | 1.61 us: 1.09x slower                                                         |
| create_gc_cycles              | 1.16 ms                                                | 1.30 ms: 1.11x slower                                                         |
| json_loads                    | 16.6 us                                                | 18.8 us: 1.13x slower                                                         |
| xml_etree_generate            | 53.9 ms                                                | 61.4 ms: 1.14x slower                                                         |
| python_startup_no_site        | 12.8 ms                                                | 14.7 ms: 1.15x slower                                                         |
| gc_traversal                  | 2.71 ms                                                | 3.12 ms: 1.15x slower                                                         |
| nqueens                       | 63.8 ms                                                | 74.0 ms: 1.16x slower                                                         |
| async_generators              | 233 ms                                                 | 277 ms: 1.19x slower                                                          |
| bench_mp_pool                 | 56.0 ms                                                | 67.7 ms: 1.21x slower                                                         |
| coverage                      | 41.2 ms                                                | 50.3 ms: 1.22x slower                                                         |
| telco                         | 3.49 ms                                                | 4.96 ms: 1.42x slower                                                         |
| Geometric mean                | (ref)                                                  | 1.22x faster                                                                  |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250430-3.14.0a7+-cad1946/bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.227x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.15x
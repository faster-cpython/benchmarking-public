# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_stackrefs_single
- machine: darwin-arm64
- commit hash: 916faf4
- commit date: 2025-03-07
- overall geometric mean: 1.253x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 179 ms: 1.13x faster                                                             |
| docutils       | 1.74 sec                                               | 1.51 sec: 1.15x faster                                                           |
| html5lib       | 43.5 ms                                                | 32.6 ms: 1.34x faster                                                            |
| sphinx         | 729 ms                                                 | 614 ms: 1.19x faster                                                             |
| Geometric mean | (ref)                                                  | 1.20x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|-------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 70.3 ms: 5.58x faster                                                            |
| async_tree_eager_memoization  | 483 ms                                                 | 152 ms: 3.17x faster                                                             |
| async_tree_eager_io           | 1.01 sec                                               | 395 ms: 2.57x faster                                                             |
| async_tree_io                 | 1.02 sec                                               | 416 ms: 2.45x faster                                                             |
| async_tree_memoization        | 481 ms                                                 | 218 ms: 2.21x faster                                                             |
| async_tree_none               | 391 ms                                                 | 178 ms: 2.19x faster                                                             |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 366 ms: 1.83x faster                                                             |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 430 ms: 1.55x faster                                                             |
| coroutines                    | 20.5 ms                                                | 18.0 ms: 1.14x faster                                                            |
| async_generators              | 233 ms                                                 | 264 ms: 1.13x slower                                                             |
| Geometric mean                | (ref)                                                  | 1.95x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 56.4 ms: 1.28x faster                                                            |
| nbody          | 92.5 ms                                                | 90.5 ms: 1.02x faster                                                            |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                             |
| regex_compile  | 95.6 ms                                                | 78.5 ms: 1.22x faster                                                            |
| regex_v8       | 19.1 ms                                                | 17.0 ms: 1.13x faster                                                            |
| regex_effbot   | 2.34 ms                                                | 2.29 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.15x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.72 sec                                               | 1.35 sec: 1.28x faster                                                           |
| pickle_pure_python   | 285 us                                                 | 237 us: 1.20x faster                                                             |
| unpickle_pure_python | 198 us                                                 | 173 us: 1.15x faster                                                             |
| json_dumps           | 8.31 ms                                                | 7.54 ms: 1.10x faster                                                            |
| xml_etree_process    | 44.6 ms                                                | 42.0 ms: 1.06x faster                                                            |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.06x faster                                                             |
| xml_etree_iterparse  | 74.5 ms                                                | 73.9 ms: 1.01x faster                                                            |
| xml_etree_generate   | 53.9 ms                                                | 58.1 ms: 1.08x slower                                                            |
| json_loads           | 16.6 us                                                | 17.9 us: 1.08x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.4 ms: 1.01x faster                                                            |
| python_startup_no_site | 12.8 ms                                                | 14.4 ms: 1.13x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.64 ms: 1.14x faster                                                            |
| genshi_text     | 17.7 ms                                                | 16.3 ms: 1.09x faster                                                            |
| genshi_xml      | 35.1 ms                                                | 33.5 ms: 1.05x faster                                                            |
| django_template | 24.4 ms                                                | 23.4 ms: 1.04x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                     |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|-------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 70.3 ms: 5.58x faster                                                            |
| typing_runtime_protocols      | 326 us                                                 | 103 us: 3.18x faster                                                             |
| async_tree_eager_memoization  | 483 ms                                                 | 152 ms: 3.17x faster                                                             |
| subparsers                    | 39.8 ms                                                | 12.8 ms: 3.12x faster                                                            |
| async_tree_eager_io           | 1.01 sec                                               | 395 ms: 2.57x faster                                                             |
| async_tree_io                 | 1.02 sec                                               | 416 ms: 2.45x faster                                                             |
| async_tree_memoization        | 481 ms                                                 | 218 ms: 2.21x faster                                                             |
| async_tree_none               | 391 ms                                                 | 178 ms: 2.19x faster                                                             |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 366 ms: 1.83x faster                                                             |
| deltablue                     | 4.99 ms                                                | 2.83 ms: 1.76x faster                                                            |
| raytrace                      | 327 ms                                                 | 199 ms: 1.64x faster                                                             |
| go                            | 163 ms                                                 | 101 ms: 1.62x faster                                                             |
| deepcopy                      | 276 us                                                 | 172 us: 1.60x faster                                                             |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 430 ms: 1.55x faster                                                             |
| deepcopy_memo                 | 34.7 us                                                | 22.7 us: 1.53x faster                                                            |
| scimark_sor                   | 140 ms                                                 | 92.3 ms: 1.52x faster                                                            |
| logging_silent                | 117 ns                                                 | 78.4 ns: 1.49x faster                                                            |
| chaos                         | 67.7 ms                                                | 45.6 ms: 1.49x faster                                                            |
| sqlglot_parse                 | 1.35 ms                                                | 912 us: 1.48x faster                                                             |
| scimark_monte_carlo           | 72.4 ms                                                | 49.9 ms: 1.45x faster                                                            |
| richards_super                | 61.0 ms                                                | 42.6 ms: 1.43x faster                                                            |
| sqlglot_transpile             | 1.56 ms                                                | 1.10 ms: 1.42x faster                                                            |
| richards                      | 52.3 ms                                                | 36.9 ms: 1.42x faster                                                            |
| html5lib                      | 43.5 ms                                                | 32.6 ms: 1.34x faster                                                            |
| pyflate                       | 448 ms                                                 | 340 ms: 1.32x faster                                                             |
| spectral_norm                 | 95.3 ms                                                | 72.8 ms: 1.31x faster                                                            |
| deepcopy_reduce               | 2.32 us                                                | 1.78 us: 1.31x faster                                                            |
| pylint                        | 231 ms                                                 | 176 ms: 1.31x faster                                                             |
| comprehensions                | 17.3 us                                                | 13.3 us: 1.30x faster                                                            |
| float                         | 72.4 ms                                                | 56.4 ms: 1.28x faster                                                            |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.06 ms: 1.28x faster                                                            |
| k_core                        | 2.01 sec                                               | 1.57 sec: 1.28x faster                                                           |
| scimark_lu                    | 103 ms                                                 | 80.0 ms: 1.28x faster                                                            |
| tomli_loads                   | 1.72 sec                                               | 1.35 sec: 1.28x faster                                                           |
| logging_format                | 5.03 us                                                | 4.04 us: 1.25x faster                                                            |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                             |
| logging_simple                | 4.59 us                                                | 3.71 us: 1.24x faster                                                            |
| pprint_pformat                | 1.33 sec                                               | 1.08 sec: 1.23x faster                                                           |
| pycparser                     | 887 ms                                                 | 728 ms: 1.22x faster                                                             |
| regex_compile                 | 95.6 ms                                                | 78.5 ms: 1.22x faster                                                            |
| pprint_safe_repr              | 648 ms                                                 | 535 ms: 1.21x faster                                                             |
| dulwich_log                   | 35.6 ms                                                | 29.5 ms: 1.21x faster                                                            |
| thrift                        | 562 us                                                 | 469 us: 1.20x faster                                                             |
| pickle_pure_python            | 285 us                                                 | 237 us: 1.20x faster                                                             |
| crypto_pyaes                  | 73.3 ms                                                | 61.5 ms: 1.19x faster                                                            |
| sqlalchemy_declarative        | 75.7 ms                                                | 63.7 ms: 1.19x faster                                                            |
| sphinx                        | 729 ms                                                 | 614 ms: 1.19x faster                                                             |
| hexiom                        | 6.25 ms                                                | 5.29 ms: 1.18x faster                                                            |
| sympy_sum                     | 92.7 ms                                                | 79.4 ms: 1.17x faster                                                            |
| docutils                      | 1.74 sec                                               | 1.51 sec: 1.15x faster                                                           |
| unpickle_pure_python          | 198 us                                                 | 173 us: 1.15x faster                                                             |
| generators                    | 31.7 ms                                                | 27.8 ms: 1.14x faster                                                            |
| coroutines                    | 20.5 ms                                                | 18.0 ms: 1.14x faster                                                            |
| mako                          | 9.81 ms                                                | 8.64 ms: 1.14x faster                                                            |
| regex_v8                      | 19.1 ms                                                | 17.0 ms: 1.13x faster                                                            |
| 2to3                          | 201 ms                                                 | 179 ms: 1.13x faster                                                             |
| scimark_fft                   | 225 ms                                                 | 201 ms: 1.12x faster                                                             |
| json_dumps                    | 8.31 ms                                                | 7.54 ms: 1.10x faster                                                            |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.11 ms: 1.10x faster                                                            |
| genshi_text                   | 17.7 ms                                                | 16.3 ms: 1.09x faster                                                            |
| sympy_str                     | 166 ms                                                 | 153 ms: 1.08x faster                                                             |
| pathlib                       | 25.7 ms                                                | 23.9 ms: 1.08x faster                                                            |
| sympy_integrate               | 13.2 ms                                                | 12.3 ms: 1.07x faster                                                            |
| xml_etree_process             | 44.6 ms                                                | 42.0 ms: 1.06x faster                                                            |
| bpe_tokeniser                 | 3.44 sec                                               | 3.24 sec: 1.06x faster                                                           |
| mdp                           | 1.65 sec                                               | 1.56 sec: 1.06x faster                                                           |
| xml_etree_parse               | 109 ms                                                 | 104 ms: 1.06x faster                                                             |
| sympy_expand                  | 269 ms                                                 | 255 ms: 1.05x faster                                                             |
| bench_thread_pool             | 545 us                                                 | 519 us: 1.05x faster                                                             |
| genshi_xml                    | 35.1 ms                                                | 33.5 ms: 1.05x faster                                                            |
| sqlglot_optimize              | 37.2 ms                                                | 35.5 ms: 1.05x faster                                                            |
| django_template               | 24.4 ms                                                | 23.4 ms: 1.04x faster                                                            |
| many_optionals                | 486 us                                                 | 472 us: 1.03x faster                                                             |
| dask                          | 789 ms                                                 | 769 ms: 1.03x faster                                                             |
| nbody                         | 92.5 ms                                                | 90.5 ms: 1.02x faster                                                            |
| json                          | 3.10 ms                                                | 3.04 ms: 1.02x faster                                                            |
| regex_effbot                  | 2.34 ms                                                | 2.29 ms: 1.02x faster                                                            |
| python_startup                | 19.6 ms                                                | 19.4 ms: 1.01x faster                                                            |
| connected_components          | 318 ms                                                 | 315 ms: 1.01x faster                                                             |
| xml_etree_iterparse           | 74.5 ms                                                | 73.9 ms: 1.01x faster                                                            |
| fannkuch                      | 303 ms                                                 | 304 ms: 1.01x slower                                                             |
| meteor_contest                | 77.8 ms                                                | 78.3 ms: 1.01x slower                                                            |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                             |
| sqlglot_normalize             | 192 ms                                                 | 197 ms: 1.02x slower                                                             |
| sqlite_synth                  | 1.48 us                                                | 1.54 us: 1.04x slower                                                            |
| shortest_path                 | 328 ms                                                 | 342 ms: 1.04x slower                                                             |
| nqueens                       | 63.8 ms                                                | 66.8 ms: 1.05x slower                                                            |
| xml_etree_generate            | 53.9 ms                                                | 58.1 ms: 1.08x slower                                                            |
| json_loads                    | 16.6 us                                                | 17.9 us: 1.08x slower                                                            |
| create_gc_cycles              | 1.16 ms                                                | 1.27 ms: 1.09x slower                                                            |
| bench_mp_pool                 | 56.0 ms                                                | 61.3 ms: 1.10x slower                                                            |
| python_startup_no_site        | 12.8 ms                                                | 14.4 ms: 1.13x slower                                                            |
| async_generators              | 233 ms                                                 | 264 ms: 1.13x slower                                                             |
| coverage                      | 41.2 ms                                                | 47.0 ms: 1.14x slower                                                            |
| gc_traversal                  | 2.71 ms                                                | 3.10 ms: 1.14x slower                                                            |
| telco                         | 3.49 ms                                                | 4.75 ms: 1.36x slower                                                            |
| Geometric mean                | (ref)                                                  | 1.25x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (8) of results/bm-20250307-3.14.0a5+-916faf4/bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.253x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.13x
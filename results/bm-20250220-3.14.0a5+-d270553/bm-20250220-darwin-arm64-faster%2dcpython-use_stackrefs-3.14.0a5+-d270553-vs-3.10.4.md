# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_stackrefs
- machine: darwin-arm64
- commit hash: d270553
- commit date: 2025-02-20
- overall geometric mean: 1.278x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 200 ms: 1.00x faster                                                      |
| docutils       | 1.74 sec                                               | 1.49 sec: 1.16x faster                                                    |
| html5lib       | 43.5 ms                                                | 32.2 ms: 1.35x faster                                                     |
| sphinx         | 729 ms                                                 | 605 ms: 1.20x faster                                                      |
| Geometric mean | (ref)                                                  | 1.17x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 69.2 ms: 5.67x faster                                                     |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.21x faster                                                      |
| async_tree_eager_io           | 1.01 sec                                               | 389 ms: 2.61x faster                                                      |
| async_tree_io                 | 1.02 sec                                               | 408 ms: 2.50x faster                                                      |
| async_tree_memoization        | 481 ms                                                 | 211 ms: 2.28x faster                                                      |
| async_tree_none               | 391 ms                                                 | 177 ms: 2.21x faster                                                      |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 367 ms: 1.82x faster                                                      |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 429 ms: 1.56x faster                                                      |
| coroutines                    | 20.5 ms                                                | 17.9 ms: 1.15x faster                                                     |
| async_generators              | 233 ms                                                 | 270 ms: 1.16x slower                                                      |
| Geometric mean                | (ref)                                                  | 1.96x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 53.2 ms: 1.36x faster                                                     |
| nbody          | 92.5 ms                                                | 80.7 ms: 1.15x faster                                                     |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.16x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 74.4 ms: 1.28x faster                                                     |
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                      |
| regex_v8       | 19.1 ms                                                | 16.9 ms: 1.13x faster                                                     |
| regex_effbot   | 2.34 ms                                                | 2.30 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.16x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 225 us: 1.27x faster                                                      |
| tomli_loads          | 1.72 sec                                               | 1.39 sec: 1.23x faster                                                    |
| unpickle_pure_python | 198 us                                                 | 167 us: 1.19x faster                                                      |
| json_dumps           | 8.31 ms                                                | 7.49 ms: 1.11x faster                                                     |
| xml_etree_parse      | 109 ms                                                 | 102 ms: 1.07x faster                                                      |
| xml_etree_process    | 44.6 ms                                                | 41.8 ms: 1.07x faster                                                     |
| xml_etree_iterparse  | 74.5 ms                                                | 73.7 ms: 1.01x faster                                                     |
| xml_etree_generate   | 53.9 ms                                                | 57.4 ms: 1.07x slower                                                     |
| json_loads           | 16.6 us                                                | 17.8 us: 1.07x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.1 ms: 1.15x faster                                                     |
| python_startup_no_site | 12.8 ms                                                | 12.3 ms: 1.04x faster                                                     |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.97 ms: 1.23x faster                                                     |
| genshi_text     | 17.7 ms                                                | 15.5 ms: 1.14x faster                                                     |
| genshi_xml      | 35.1 ms                                                | 32.2 ms: 1.09x faster                                                     |
| django_template | 24.4 ms                                                | 23.0 ms: 1.06x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                              |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 69.2 ms: 5.67x faster                                                     |
| typing_runtime_protocols      | 326 us                                                 | 101 us: 3.24x faster                                                      |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.21x faster                                                      |
| subparsers                    | 39.8 ms                                                | 12.8 ms: 3.12x faster                                                     |
| async_tree_eager_io           | 1.01 sec                                               | 389 ms: 2.61x faster                                                      |
| async_tree_io                 | 1.02 sec                                               | 408 ms: 2.50x faster                                                      |
| async_tree_memoization        | 481 ms                                                 | 211 ms: 2.28x faster                                                      |
| async_tree_none               | 391 ms                                                 | 177 ms: 2.21x faster                                                      |
| deltablue                     | 4.99 ms                                                | 2.67 ms: 1.87x faster                                                     |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 367 ms: 1.82x faster                                                      |
| go                            | 163 ms                                                 | 92.9 ms: 1.76x faster                                                     |
| raytrace                      | 327 ms                                                 | 194 ms: 1.69x faster                                                      |
| deepcopy_memo                 | 34.7 us                                                | 20.6 us: 1.69x faster                                                     |
| deepcopy                      | 276 us                                                 | 165 us: 1.67x faster                                                      |
| logging_silent                | 117 ns                                                 | 70.6 ns: 1.66x faster                                                     |
| scimark_sor                   | 140 ms                                                 | 89.0 ms: 1.57x faster                                                     |
| sqlglot_parse                 | 1.35 ms                                                | 864 us: 1.56x faster                                                      |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 429 ms: 1.56x faster                                                      |
| scimark_monte_carlo           | 72.4 ms                                                | 47.2 ms: 1.53x faster                                                     |
| chaos                         | 67.7 ms                                                | 44.2 ms: 1.53x faster                                                     |
| sqlglot_transpile             | 1.56 ms                                                | 1.04 ms: 1.50x faster                                                     |
| richards_super                | 61.0 ms                                                | 42.5 ms: 1.43x faster                                                     |
| richards                      | 52.3 ms                                                | 37.7 ms: 1.39x faster                                                     |
| float                         | 72.4 ms                                                | 53.2 ms: 1.36x faster                                                     |
| pylint                        | 231 ms                                                 | 170 ms: 1.36x faster                                                      |
| html5lib                      | 43.5 ms                                                | 32.2 ms: 1.35x faster                                                     |
| deepcopy_reduce               | 2.32 us                                                | 1.72 us: 1.35x faster                                                     |
| comprehensions                | 17.3 us                                                | 13.0 us: 1.33x faster                                                     |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.94 ms: 1.31x faster                                                     |
| pprint_pformat                | 1.33 sec                                               | 1.02 sec: 1.30x faster                                                    |
| logging_format                | 5.03 us                                                | 3.91 us: 1.29x faster                                                     |
| regex_compile                 | 95.6 ms                                                | 74.4 ms: 1.28x faster                                                     |
| logging_simple                | 4.59 us                                                | 3.59 us: 1.28x faster                                                     |
| pprint_safe_repr              | 648 ms                                                 | 506 ms: 1.28x faster                                                      |
| generators                    | 31.7 ms                                                | 25.0 ms: 1.27x faster                                                     |
| pickle_pure_python            | 285 us                                                 | 225 us: 1.27x faster                                                      |
| pycparser                     | 887 ms                                                 | 701 ms: 1.27x faster                                                      |
| k_core                        | 2.01 sec                                               | 1.59 sec: 1.27x faster                                                    |
| scimark_lu                    | 103 ms                                                 | 81.1 ms: 1.27x faster                                                     |
| pyflate                       | 448 ms                                                 | 354 ms: 1.26x faster                                                      |
| hexiom                        | 6.25 ms                                                | 4.97 ms: 1.26x faster                                                     |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                      |
| tomli_loads                   | 1.72 sec                                               | 1.39 sec: 1.23x faster                                                    |
| mako                          | 9.81 ms                                                | 7.97 ms: 1.23x faster                                                     |
| dulwich_log                   | 35.6 ms                                                | 29.0 ms: 1.23x faster                                                     |
| thrift                        | 562 us                                                 | 459 us: 1.23x faster                                                      |
| sqlalchemy_declarative        | 75.7 ms                                                | 61.8 ms: 1.23x faster                                                     |
| sphinx                        | 729 ms                                                 | 605 ms: 1.20x faster                                                      |
| crypto_pyaes                  | 73.3 ms                                                | 61.7 ms: 1.19x faster                                                     |
| spectral_norm                 | 95.3 ms                                                | 80.2 ms: 1.19x faster                                                     |
| unpickle_pure_python          | 198 us                                                 | 167 us: 1.19x faster                                                      |
| sympy_sum                     | 92.7 ms                                                | 78.1 ms: 1.19x faster                                                     |
| docutils                      | 1.74 sec                                               | 1.49 sec: 1.16x faster                                                    |
| scimark_fft                   | 225 ms                                                 | 195 ms: 1.16x faster                                                      |
| python_startup                | 19.6 ms                                                | 17.1 ms: 1.15x faster                                                     |
| coroutines                    | 20.5 ms                                                | 17.9 ms: 1.15x faster                                                     |
| nbody                         | 92.5 ms                                                | 80.7 ms: 1.15x faster                                                     |
| genshi_text                   | 17.7 ms                                                | 15.5 ms: 1.14x faster                                                     |
| regex_v8                      | 19.1 ms                                                | 16.9 ms: 1.13x faster                                                     |
| json_dumps                    | 8.31 ms                                                | 7.49 ms: 1.11x faster                                                     |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.09 ms: 1.11x faster                                                     |
| sympy_str                     | 166 ms                                                 | 150 ms: 1.11x faster                                                      |
| pathlib                       | 25.7 ms                                                | 23.5 ms: 1.09x faster                                                     |
| genshi_xml                    | 35.1 ms                                                | 32.2 ms: 1.09x faster                                                     |
| sympy_integrate               | 13.2 ms                                                | 12.1 ms: 1.09x faster                                                     |
| mdp                           | 1.65 sec                                               | 1.52 sec: 1.09x faster                                                    |
| sympy_expand                  | 269 ms                                                 | 250 ms: 1.08x faster                                                      |
| bench_thread_pool             | 545 us                                                 | 507 us: 1.07x faster                                                      |
| xml_etree_parse               | 109 ms                                                 | 102 ms: 1.07x faster                                                      |
| sqlglot_optimize              | 37.2 ms                                                | 34.8 ms: 1.07x faster                                                     |
| xml_etree_process             | 44.6 ms                                                | 41.8 ms: 1.07x faster                                                     |
| django_template               | 24.4 ms                                                | 23.0 ms: 1.06x faster                                                     |
| python_startup_no_site        | 12.8 ms                                                | 12.3 ms: 1.04x faster                                                     |
| many_optionals                | 486 us                                                 | 468 us: 1.04x faster                                                      |
| bpe_tokeniser                 | 3.44 sec                                               | 3.32 sec: 1.04x faster                                                    |
| dask                          | 789 ms                                                 | 772 ms: 1.02x faster                                                      |
| regex_effbot                  | 2.34 ms                                                | 2.30 ms: 1.02x faster                                                     |
| sqlglot_normalize             | 192 ms                                                 | 190 ms: 1.01x faster                                                      |
| xml_etree_iterparse           | 74.5 ms                                                | 73.7 ms: 1.01x faster                                                     |
| json                          | 3.10 ms                                                | 3.08 ms: 1.01x faster                                                     |
| 2to3                          | 201 ms                                                 | 200 ms: 1.00x faster                                                      |
| meteor_contest                | 77.8 ms                                                | 77.5 ms: 1.00x faster                                                     |
| connected_components          | 318 ms                                                 | 317 ms: 1.00x faster                                                      |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                      |
| fannkuch                      | 303 ms                                                 | 306 ms: 1.01x slower                                                      |
| sqlite_synth                  | 1.48 us                                                | 1.55 us: 1.05x slower                                                     |
| shortest_path                 | 328 ms                                                 | 346 ms: 1.05x slower                                                      |
| xml_etree_generate            | 53.9 ms                                                | 57.4 ms: 1.07x slower                                                     |
| bench_mp_pool                 | 56.0 ms                                                | 59.9 ms: 1.07x slower                                                     |
| json_loads                    | 16.6 us                                                | 17.8 us: 1.07x slower                                                     |
| nqueens                       | 63.8 ms                                                | 70.1 ms: 1.10x slower                                                     |
| create_gc_cycles              | 1.16 ms                                                | 1.29 ms: 1.11x slower                                                     |
| coverage                      | 41.2 ms                                                | 47.3 ms: 1.15x slower                                                     |
| gc_traversal                  | 2.71 ms                                                | 3.11 ms: 1.15x slower                                                     |
| async_generators              | 233 ms                                                 | 270 ms: 1.16x slower                                                      |
| telco                         | 3.49 ms                                                | 4.72 ms: 1.35x slower                                                     |
| Geometric mean                | (ref)                                                  | 1.28x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (8) of results/bm-20250220-3.14.0a5+-d270553/bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.278x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.13x
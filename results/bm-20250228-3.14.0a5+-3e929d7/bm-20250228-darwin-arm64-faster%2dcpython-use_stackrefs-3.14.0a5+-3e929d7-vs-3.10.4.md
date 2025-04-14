# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_stackrefs
- machine: darwin-arm64
- commit hash: 3e929d7
- commit date: 2025-02-28
- overall geometric mean: 1.287x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 173 ms: 1.17x faster                                                      |
| docutils       | 1.74 sec                                               | 1.50 sec: 1.16x faster                                                    |
| html5lib       | 43.5 ms                                                | 32.3 ms: 1.35x faster                                                     |
| sphinx         | 729 ms                                                 | 599 ms: 1.22x faster                                                      |
| Geometric mean | (ref)                                                  | 1.22x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 67.3 ms: 5.82x faster                                                     |
| async_tree_eager_memoization  | 483 ms                                                 | 149 ms: 3.25x faster                                                      |
| async_tree_eager_io           | 1.01 sec                                               | 384 ms: 2.64x faster                                                      |
| async_tree_io                 | 1.02 sec                                               | 400 ms: 2.54x faster                                                      |
| async_tree_memoization        | 481 ms                                                 | 209 ms: 2.30x faster                                                      |
| async_tree_none               | 391 ms                                                 | 172 ms: 2.27x faster                                                      |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 363 ms: 1.84x faster                                                      |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 426 ms: 1.57x faster                                                      |
| coroutines                    | 20.5 ms                                                | 17.6 ms: 1.17x faster                                                     |
| async_generators              | 233 ms                                                 | 262 ms: 1.12x slower                                                      |
| Geometric mean                | (ref)                                                  | 2.00x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 53.0 ms: 1.37x faster                                                     |
| nbody          | 92.5 ms                                                | 79.9 ms: 1.16x faster                                                     |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.16x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 75.5 ms: 1.27x faster                                                     |
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                      |
| regex_v8       | 19.1 ms                                                | 16.9 ms: 1.13x faster                                                     |
| regex_effbot   | 2.34 ms                                                | 2.29 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.16x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 223 us: 1.27x faster                                                      |
| tomli_loads          | 1.72 sec                                               | 1.43 sec: 1.21x faster                                                    |
| unpickle_pure_python | 198 us                                                 | 168 us: 1.18x faster                                                      |
| json_dumps           | 8.31 ms                                                | 7.45 ms: 1.11x faster                                                     |
| xml_etree_process    | 44.6 ms                                                | 40.9 ms: 1.09x faster                                                     |
| xml_etree_parse      | 109 ms                                                 | 102 ms: 1.07x faster                                                      |
| xml_etree_iterparse  | 74.5 ms                                                | 73.4 ms: 1.01x faster                                                     |
| xml_etree_generate   | 53.9 ms                                                | 56.6 ms: 1.05x slower                                                     |
| json_loads           | 16.6 us                                                | 17.6 us: 1.06x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 16.6 ms: 1.19x faster                                                     |
| python_startup_no_site | 12.8 ms                                                | 11.8 ms: 1.08x faster                                                     |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.81 ms: 1.26x faster                                                     |
| genshi_text     | 17.7 ms                                                | 15.4 ms: 1.15x faster                                                     |
| genshi_xml      | 35.1 ms                                                | 32.0 ms: 1.10x faster                                                     |
| django_template | 24.4 ms                                                | 22.7 ms: 1.07x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                              |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 67.3 ms: 5.82x faster                                                     |
| async_tree_eager_memoization  | 483 ms                                                 | 149 ms: 3.25x faster                                                      |
| typing_runtime_protocols      | 326 us                                                 | 101 us: 3.23x faster                                                      |
| subparsers                    | 39.8 ms                                                | 12.7 ms: 3.14x faster                                                     |
| async_tree_eager_io           | 1.01 sec                                               | 384 ms: 2.64x faster                                                      |
| async_tree_io                 | 1.02 sec                                               | 400 ms: 2.54x faster                                                      |
| async_tree_memoization        | 481 ms                                                 | 209 ms: 2.30x faster                                                      |
| async_tree_none               | 391 ms                                                 | 172 ms: 2.27x faster                                                      |
| deltablue                     | 4.99 ms                                                | 2.66 ms: 1.87x faster                                                     |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 363 ms: 1.84x faster                                                      |
| go                            | 163 ms                                                 | 93.0 ms: 1.76x faster                                                     |
| deepcopy_memo                 | 34.7 us                                                | 20.3 us: 1.71x faster                                                     |
| raytrace                      | 327 ms                                                 | 193 ms: 1.69x faster                                                      |
| deepcopy                      | 276 us                                                 | 164 us: 1.68x faster                                                      |
| logging_silent                | 117 ns                                                 | 71.4 ns: 1.64x faster                                                     |
| sqlglot_parse                 | 1.35 ms                                                | 856 us: 1.58x faster                                                      |
| scimark_sor                   | 140 ms                                                 | 89.1 ms: 1.57x faster                                                     |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 426 ms: 1.57x faster                                                      |
| chaos                         | 67.7 ms                                                | 44.1 ms: 1.53x faster                                                     |
| scimark_monte_carlo           | 72.4 ms                                                | 47.5 ms: 1.52x faster                                                     |
| sqlglot_transpile             | 1.56 ms                                                | 1.04 ms: 1.50x faster                                                     |
| richards_super                | 61.0 ms                                                | 41.8 ms: 1.46x faster                                                     |
| richards                      | 52.3 ms                                                | 37.5 ms: 1.40x faster                                                     |
| pylint                        | 231 ms                                                 | 168 ms: 1.37x faster                                                      |
| float                         | 72.4 ms                                                | 53.0 ms: 1.37x faster                                                     |
| deepcopy_reduce               | 2.32 us                                                | 1.71 us: 1.36x faster                                                     |
| html5lib                      | 43.5 ms                                                | 32.3 ms: 1.35x faster                                                     |
| comprehensions                | 17.3 us                                                | 12.9 us: 1.34x faster                                                     |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.88 ms: 1.32x faster                                                     |
| pprint_pformat                | 1.33 sec                                               | 1.03 sec: 1.29x faster                                                    |
| logging_format                | 5.03 us                                                | 3.92 us: 1.28x faster                                                     |
| pickle_pure_python            | 285 us                                                 | 223 us: 1.27x faster                                                      |
| pprint_safe_repr              | 648 ms                                                 | 509 ms: 1.27x faster                                                      |
| pyflate                       | 448 ms                                                 | 352 ms: 1.27x faster                                                      |
| generators                    | 31.7 ms                                                | 24.9 ms: 1.27x faster                                                     |
| k_core                        | 2.01 sec                                               | 1.58 sec: 1.27x faster                                                    |
| logging_simple                | 4.59 us                                                | 3.62 us: 1.27x faster                                                     |
| pycparser                     | 887 ms                                                 | 700 ms: 1.27x faster                                                      |
| regex_compile                 | 95.6 ms                                                | 75.5 ms: 1.27x faster                                                     |
| hexiom                        | 6.25 ms                                                | 4.96 ms: 1.26x faster                                                     |
| mako                          | 9.81 ms                                                | 7.81 ms: 1.26x faster                                                     |
| scimark_lu                    | 103 ms                                                 | 81.8 ms: 1.25x faster                                                     |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                      |
| thrift                        | 562 us                                                 | 454 us: 1.24x faster                                                      |
| sqlalchemy_declarative        | 75.7 ms                                                | 61.5 ms: 1.23x faster                                                     |
| dulwich_log                   | 35.6 ms                                                | 29.0 ms: 1.23x faster                                                     |
| sphinx                        | 729 ms                                                 | 599 ms: 1.22x faster                                                      |
| tomli_loads                   | 1.72 sec                                               | 1.43 sec: 1.21x faster                                                    |
| spectral_norm                 | 95.3 ms                                                | 79.5 ms: 1.20x faster                                                     |
| sympy_sum                     | 92.7 ms                                                | 77.5 ms: 1.20x faster                                                     |
| crypto_pyaes                  | 73.3 ms                                                | 61.5 ms: 1.19x faster                                                     |
| python_startup                | 19.6 ms                                                | 16.6 ms: 1.19x faster                                                     |
| unpickle_pure_python          | 198 us                                                 | 168 us: 1.18x faster                                                      |
| coroutines                    | 20.5 ms                                                | 17.6 ms: 1.17x faster                                                     |
| 2to3                          | 201 ms                                                 | 173 ms: 1.17x faster                                                      |
| docutils                      | 1.74 sec                                               | 1.50 sec: 1.16x faster                                                    |
| nbody                         | 92.5 ms                                                | 79.9 ms: 1.16x faster                                                     |
| genshi_text                   | 17.7 ms                                                | 15.4 ms: 1.15x faster                                                     |
| regex_v8                      | 19.1 ms                                                | 16.9 ms: 1.13x faster                                                     |
| scimark_fft                   | 225 ms                                                 | 200 ms: 1.12x faster                                                      |
| sympy_str                     | 166 ms                                                 | 149 ms: 1.11x faster                                                      |
| json_dumps                    | 8.31 ms                                                | 7.45 ms: 1.11x faster                                                     |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.07 ms: 1.11x faster                                                     |
| genshi_xml                    | 35.1 ms                                                | 32.0 ms: 1.10x faster                                                     |
| pathlib                       | 25.7 ms                                                | 23.5 ms: 1.09x faster                                                     |
| xml_etree_process             | 44.6 ms                                                | 40.9 ms: 1.09x faster                                                     |
| sympy_integrate               | 13.2 ms                                                | 12.1 ms: 1.09x faster                                                     |
| python_startup_no_site        | 12.8 ms                                                | 11.8 ms: 1.08x faster                                                     |
| sympy_expand                  | 269 ms                                                 | 249 ms: 1.08x faster                                                      |
| mdp                           | 1.65 sec                                               | 1.53 sec: 1.08x faster                                                    |
| sqlglot_optimize              | 37.2 ms                                                | 34.6 ms: 1.07x faster                                                     |
| django_template               | 24.4 ms                                                | 22.7 ms: 1.07x faster                                                     |
| xml_etree_parse               | 109 ms                                                 | 102 ms: 1.07x faster                                                      |
| many_optionals                | 486 us                                                 | 462 us: 1.05x faster                                                      |
| bpe_tokeniser                 | 3.44 sec                                               | 3.32 sec: 1.03x faster                                                    |
| bench_thread_pool             | 545 us                                                 | 528 us: 1.03x faster                                                      |
| json                          | 3.10 ms                                                | 3.00 ms: 1.03x faster                                                     |
| dask                          | 789 ms                                                 | 769 ms: 1.03x faster                                                      |
| regex_effbot                  | 2.34 ms                                                | 2.29 ms: 1.02x faster                                                     |
| sqlglot_normalize             | 192 ms                                                 | 189 ms: 1.02x faster                                                      |
| xml_etree_iterparse           | 74.5 ms                                                | 73.4 ms: 1.01x faster                                                     |
| meteor_contest                | 77.8 ms                                                | 77.5 ms: 1.00x faster                                                     |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                      |
| fannkuch                      | 303 ms                                                 | 309 ms: 1.02x slower                                                      |
| connected_components          | 318 ms                                                 | 328 ms: 1.03x slower                                                      |
| sqlite_synth                  | 1.48 us                                                | 1.54 us: 1.04x slower                                                     |
| xml_etree_generate            | 53.9 ms                                                | 56.6 ms: 1.05x slower                                                     |
| json_loads                    | 16.6 us                                                | 17.6 us: 1.06x slower                                                     |
| bench_mp_pool                 | 56.0 ms                                                | 59.7 ms: 1.07x slower                                                     |
| shortest_path                 | 328 ms                                                 | 351 ms: 1.07x slower                                                      |
| nqueens                       | 63.8 ms                                                | 69.2 ms: 1.08x slower                                                     |
| create_gc_cycles              | 1.16 ms                                                | 1.27 ms: 1.09x slower                                                     |
| async_generators              | 233 ms                                                 | 262 ms: 1.12x slower                                                      |
| coverage                      | 41.2 ms                                                | 47.1 ms: 1.14x slower                                                     |
| gc_traversal                  | 2.71 ms                                                | 3.10 ms: 1.15x slower                                                     |
| telco                         | 3.49 ms                                                | 4.66 ms: 1.34x slower                                                     |
| Geometric mean                | (ref)                                                  | 1.28x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (8) of results/bm-20250228-3.14.0a5+-3e929d7/bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.287x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.14x
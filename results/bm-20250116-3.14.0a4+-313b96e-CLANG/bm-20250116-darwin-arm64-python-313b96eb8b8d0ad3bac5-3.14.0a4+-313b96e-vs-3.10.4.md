# Results vs. 3.10.4

- fork: python
- ref: 313b96eb8b8d0ad3bac5
- machine: darwin-arm64
- commit hash: 313b96e
- commit date: 2025-01-16
- overall geometric mean: 1.310x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 169 ms: 1.19x faster                                                   |
| docutils       | 1.74 sec                                               | 1.44 sec: 1.21x faster                                                 |
| html5lib       | 43.5 ms                                                | 32.9 ms: 1.32x faster                                                  |
| sphinx         | 729 ms                                                 | 577 ms: 1.26x faster                                                   |
| Geometric mean | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 69.6 ms: 5.63x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 147 ms: 3.29x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 373 ms: 2.72x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 379 ms: 2.69x faster                                                   |
| async_tree_none               | 391 ms                                                 | 170 ms: 2.30x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 209 ms: 2.30x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 363 ms: 1.85x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 422 ms: 1.58x faster                                                   |
| coroutines                    | 20.5 ms                                                | 16.9 ms: 1.21x faster                                                  |
| asyncio_websockets            | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_generators              | 233 ms                                                 | 266 ms: 1.14x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.02x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 51.5 ms: 1.41x faster                                                  |
| nbody          | 92.5 ms                                                | 83.0 ms: 1.12x faster                                                  |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 138 ms: 1.26x faster                                                   |
| regex_compile  | 95.6 ms                                                | 77.5 ms: 1.23x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.05 ms: 1.14x faster                                                  |
| regex_v8       | 19.1 ms                                                | 17.0 ms: 1.12x faster                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 220 us: 1.29x faster                                                   |
| unpickle_pure_python | 198 us                                                 | 160 us: 1.24x faster                                                   |
| json_dumps           | 8.31 ms                                                | 7.41 ms: 1.12x faster                                                  |
| xml_etree_process    | 44.6 ms                                                | 41.1 ms: 1.08x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.59 sec: 1.08x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 103 ms: 1.07x faster                                                   |
| xml_etree_iterparse  | 74.5 ms                                                | 72.5 ms: 1.03x faster                                                  |
| json_loads           | 16.6 us                                                | 16.4 us: 1.01x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 55.5 ms: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 16.7 ms: 1.18x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 12.2 ms: 1.05x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.07 ms: 1.22x faster                                                  |
| genshi_text     | 17.7 ms                                                | 15.8 ms: 1.12x faster                                                  |
| django_template | 24.4 ms                                                | 22.7 ms: 1.08x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 33.2 ms: 1.06x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 69.6 ms: 5.63x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 147 ms: 3.29x faster                                                   |
| typing_runtime_protocols      | 326 us                                                 | 104 us: 3.15x faster                                                   |
| subparsers                    | 39.8 ms                                                | 12.7 ms: 3.13x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 373 ms: 2.72x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 379 ms: 2.69x faster                                                   |
| async_tree_none               | 391 ms                                                 | 170 ms: 2.30x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 209 ms: 2.30x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.39 ms: 2.09x faster                                                  |
| raytrace                      | 327 ms                                                 | 175 ms: 1.87x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 363 ms: 1.85x faster                                                   |
| go                            | 163 ms                                                 | 92.6 ms: 1.77x faster                                                  |
| richards_super                | 61.0 ms                                                | 36.9 ms: 1.65x faster                                                  |
| logging_silent                | 117 ns                                                 | 71.3 ns: 1.64x faster                                                  |
| sqlglot_parse                 | 1.35 ms                                                | 837 us: 1.61x faster                                                   |
| deepcopy_memo                 | 34.7 us                                                | 21.7 us: 1.60x faster                                                  |
| chaos                         | 67.7 ms                                                | 42.4 ms: 1.60x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 422 ms: 1.58x faster                                                   |
| richards                      | 52.3 ms                                                | 33.4 ms: 1.57x faster                                                  |
| deepcopy                      | 276 us                                                 | 177 us: 1.56x faster                                                   |
| scimark_sor                   | 140 ms                                                 | 90.3 ms: 1.55x faster                                                  |
| sqlglot_transpile             | 1.56 ms                                                | 1.01 ms: 1.54x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 47.7 ms: 1.52x faster                                                  |
| pylint                        | 231 ms                                                 | 162 ms: 1.42x faster                                                   |
| spectral_norm                 | 95.3 ms                                                | 67.7 ms: 1.41x faster                                                  |
| float                         | 72.4 ms                                                | 51.5 ms: 1.41x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 52.8 ms: 1.39x faster                                                  |
| pyflate                       | 448 ms                                                 | 324 ms: 1.38x faster                                                   |
| scimark_lu                    | 103 ms                                                 | 74.9 ms: 1.37x faster                                                  |
| logging_format                | 5.03 us                                                | 3.71 us: 1.36x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.48 sec: 1.35x faster                                                 |
| logging_simple                | 4.59 us                                                | 3.43 us: 1.34x faster                                                  |
| html5lib                      | 43.5 ms                                                | 32.9 ms: 1.32x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.76 us: 1.32x faster                                                  |
| comprehensions                | 17.3 us                                                | 13.1 us: 1.32x faster                                                  |
| hexiom                        | 6.25 ms                                                | 4.76 ms: 1.31x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 220 us: 1.29x faster                                                   |
| pycparser                     | 887 ms                                                 | 692 ms: 1.28x faster                                                   |
| regex_dna                     | 175 ms                                                 | 138 ms: 1.26x faster                                                   |
| sphinx                        | 729 ms                                                 | 577 ms: 1.26x faster                                                   |
| dulwich_log                   | 35.6 ms                                                | 28.4 ms: 1.25x faster                                                  |
| generators                    | 31.7 ms                                                | 25.4 ms: 1.25x faster                                                  |
| thrift                        | 562 us                                                 | 450 us: 1.25x faster                                                   |
| sqlalchemy_declarative        | 75.7 ms                                                | 61.2 ms: 1.24x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 160 us: 1.24x faster                                                   |
| regex_compile                 | 95.6 ms                                                | 77.5 ms: 1.23x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.45 ms: 1.22x faster                                                  |
| mako                          | 9.81 ms                                                | 8.07 ms: 1.22x faster                                                  |
| coroutines                    | 20.5 ms                                                | 16.9 ms: 1.21x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.44 sec: 1.21x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.11 sec: 1.20x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 77.3 ms: 1.20x faster                                                  |
| 2to3                          | 201 ms                                                 | 169 ms: 1.19x faster                                                   |
| sympy_integrate               | 13.2 ms                                                | 11.1 ms: 1.19x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 547 ms: 1.19x faster                                                   |
| python_startup                | 19.6 ms                                                | 16.7 ms: 1.18x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 192 ms: 1.17x faster                                                   |
| regex_effbot                  | 2.34 ms                                                | 2.05 ms: 1.14x faster                                                  |
| sympy_str                     | 166 ms                                                 | 147 ms: 1.13x faster                                                   |
| pathlib                       | 25.7 ms                                                | 22.8 ms: 1.13x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 17.0 ms: 1.12x faster                                                  |
| genshi_text                   | 17.7 ms                                                | 15.8 ms: 1.12x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 7.41 ms: 1.12x faster                                                  |
| nbody                         | 92.5 ms                                                | 83.0 ms: 1.12x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.08 ms: 1.11x faster                                                  |
| bench_thread_pool             | 545 us                                                 | 498 us: 1.10x faster                                                   |
| sympy_expand                  | 269 ms                                                 | 246 ms: 1.09x faster                                                   |
| json                          | 3.10 ms                                                | 2.85 ms: 1.09x faster                                                  |
| mdp                           | 1.65 sec                                               | 1.52 sec: 1.09x faster                                                 |
| xml_etree_process             | 44.6 ms                                                | 41.1 ms: 1.08x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.59 sec: 1.08x faster                                                 |
| sqlglot_optimize              | 37.2 ms                                                | 34.4 ms: 1.08x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.20 sec: 1.08x faster                                                 |
| django_template               | 24.4 ms                                                | 22.7 ms: 1.08x faster                                                  |
| connected_components          | 318 ms                                                 | 297 ms: 1.07x faster                                                   |
| xml_etree_parse               | 109 ms                                                 | 103 ms: 1.07x faster                                                   |
| genshi_xml                    | 35.1 ms                                                | 33.2 ms: 1.06x faster                                                  |
| nqueens                       | 63.8 ms                                                | 60.6 ms: 1.05x faster                                                  |
| python_startup_no_site        | 12.8 ms                                                | 12.2 ms: 1.05x faster                                                  |
| many_optionals                | 486 us                                                 | 467 us: 1.04x faster                                                   |
| xml_etree_iterparse           | 74.5 ms                                                | 72.5 ms: 1.03x faster                                                  |
| dask                          | 789 ms                                                 | 771 ms: 1.02x faster                                                   |
| sqlglot_normalize             | 192 ms                                                 | 188 ms: 1.02x faster                                                   |
| meteor_contest                | 77.8 ms                                                | 76.7 ms: 1.01x faster                                                  |
| shortest_path                 | 328 ms                                                 | 324 ms: 1.01x faster                                                   |
| json_loads                    | 16.6 us                                                | 16.4 us: 1.01x faster                                                  |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| asyncio_websockets            | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| xml_etree_generate            | 53.9 ms                                                | 55.5 ms: 1.03x slower                                                  |
| fannkuch                      | 303 ms                                                 | 315 ms: 1.04x slower                                                   |
| sqlite_synth                  | 1.48 us                                                | 1.56 us: 1.05x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 59.2 ms: 1.06x slower                                                  |
| coverage                      | 41.2 ms                                                | 44.7 ms: 1.09x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.27 ms: 1.09x slower                                                  |
| async_generators              | 233 ms                                                 | 266 ms: 1.14x slower                                                   |
| gc_traversal                  | 2.71 ms                                                | 3.11 ms: 1.15x slower                                                  |
| telco                         | 3.49 ms                                                | 4.69 ms: 1.35x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.31x faster                                                           |
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (8) of results/bm-20250116-3.14.0a4+-313b96e-CLANG/bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.310x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.13x
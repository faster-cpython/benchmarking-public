# Results vs. 3.10.4

- fork: python
- ref: b3c18bfd828ba90b9c71
- machine: darwin-arm64
- commit hash: b3c18bf
- commit date: 2025-03-03
- overall geometric mean: 1.253x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 179 ms: 1.13x faster                                                   |
| docutils       | 1.74 sec                                               | 1.50 sec: 1.16x faster                                                 |
| html5lib       | 43.5 ms                                                | 33.2 ms: 1.31x faster                                                  |
| sphinx         | 729 ms                                                 | 609 ms: 1.20x faster                                                   |
| Geometric mean | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 69.0 ms: 5.68x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.19x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 395 ms: 2.57x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 414 ms: 2.46x faster                                                   |
| async_tree_none               | 391 ms                                                 | 178 ms: 2.20x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 222 ms: 2.17x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 366 ms: 1.83x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 435 ms: 1.53x faster                                                   |
| coroutines                    | 20.5 ms                                                | 18.6 ms: 1.10x faster                                                  |
| async_generators              | 233 ms                                                 | 268 ms: 1.15x slower                                                   |
| Geometric mean                | (ref)                                                  | 1.94x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 54.4 ms: 1.33x faster                                                  |
| nbody          | 92.5 ms                                                | 92.1 ms: 1.00x faster                                                  |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 78.1 ms: 1.22x faster                                                  |
| regex_dna      | 175 ms                                                 | 146 ms: 1.19x faster                                                   |
| regex_v8       | 19.1 ms                                                | 16.9 ms: 1.13x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.32 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 230 us: 1.24x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.44 sec: 1.19x faster                                                 |
| unpickle_pure_python | 198 us                                                 | 169 us: 1.17x faster                                                   |
| json_dumps           | 8.31 ms                                                | 7.49 ms: 1.11x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.06x faster                                                   |
| xml_etree_process    | 44.6 ms                                                | 42.8 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 75.1 ms: 1.01x slower                                                  |
| json_loads           | 16.6 us                                                | 17.7 us: 1.07x slower                                                  |
| xml_etree_generate   | 53.9 ms                                                | 58.2 ms: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 12.8 ms                                                | 14.5 ms: 1.14x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.32 ms: 1.18x faster                                                  |
| genshi_text     | 17.7 ms                                                | 16.3 ms: 1.08x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 33.9 ms: 1.04x faster                                                  |
| django_template | 24.4 ms                                                | 24.2 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 69.0 ms: 5.68x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 100 us: 3.25x faster                                                   |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.19x faster                                                   |
| subparsers                    | 39.8 ms                                                | 12.8 ms: 3.10x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 395 ms: 2.57x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 414 ms: 2.46x faster                                                   |
| async_tree_none               | 391 ms                                                 | 178 ms: 2.20x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 222 ms: 2.17x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 366 ms: 1.83x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.75 ms: 1.81x faster                                                  |
| go                            | 163 ms                                                 | 94.8 ms: 1.72x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 21.0 us: 1.65x faster                                                  |
| deepcopy                      | 276 us                                                 | 168 us: 1.64x faster                                                   |
| logging_silent                | 117 ns                                                 | 73.1 ns: 1.60x faster                                                  |
| raytrace                      | 327 ms                                                 | 212 ms: 1.54x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 435 ms: 1.53x faster                                                   |
| chaos                         | 67.7 ms                                                | 44.1 ms: 1.53x faster                                                  |
| sqlglot_parse                 | 1.35 ms                                                | 891 us: 1.52x faster                                                   |
| scimark_sor                   | 140 ms                                                 | 92.8 ms: 1.51x faster                                                  |
| sqlglot_transpile             | 1.56 ms                                                | 1.07 ms: 1.45x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 49.9 ms: 1.45x faster                                                  |
| richards_super                | 61.0 ms                                                | 42.9 ms: 1.42x faster                                                  |
| pylint                        | 231 ms                                                 | 171 ms: 1.35x faster                                                   |
| float                         | 72.4 ms                                                | 54.4 ms: 1.33x faster                                                  |
| comprehensions                | 17.3 us                                                | 13.1 us: 1.32x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.76 us: 1.32x faster                                                  |
| html5lib                      | 43.5 ms                                                | 33.2 ms: 1.31x faster                                                  |
| richards                      | 52.3 ms                                                | 40.0 ms: 1.31x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.54 sec: 1.31x faster                                                 |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.09 ms: 1.28x faster                                                  |
| pyflate                       | 448 ms                                                 | 351 ms: 1.28x faster                                                   |
| pycparser                     | 887 ms                                                 | 705 ms: 1.26x faster                                                   |
| crypto_pyaes                  | 73.3 ms                                                | 59.0 ms: 1.24x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 230 us: 1.24x faster                                                   |
| logging_format                | 5.03 us                                                | 4.08 us: 1.23x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 78.1 ms: 1.22x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 78.1 ms: 1.22x faster                                                  |
| logging_simple                | 4.59 us                                                | 3.77 us: 1.22x faster                                                  |
| thrift                        | 562 us                                                 | 463 us: 1.21x faster                                                   |
| scimark_lu                    | 103 ms                                                 | 84.7 ms: 1.21x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 62.6 ms: 1.21x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 1.10 sec: 1.21x faster                                                 |
| sphinx                        | 729 ms                                                 | 609 ms: 1.20x faster                                                   |
| regex_dna                     | 175 ms                                                 | 146 ms: 1.19x faster                                                   |
| tomli_loads                   | 1.72 sec                                               | 1.44 sec: 1.19x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 29.9 ms: 1.19x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 545 ms: 1.19x faster                                                   |
| hexiom                        | 6.25 ms                                                | 5.28 ms: 1.18x faster                                                  |
| mako                          | 9.81 ms                                                | 8.32 ms: 1.18x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 169 us: 1.17x faster                                                   |
| sympy_sum                     | 92.7 ms                                                | 79.9 ms: 1.16x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.50 sec: 1.16x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 16.9 ms: 1.13x faster                                                  |
| 2to3                          | 201 ms                                                 | 179 ms: 1.13x faster                                                   |
| scimark_fft                   | 225 ms                                                 | 201 ms: 1.12x faster                                                   |
| json_dumps                    | 8.31 ms                                                | 7.49 ms: 1.11x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.08 ms: 1.11x faster                                                  |
| coroutines                    | 20.5 ms                                                | 18.6 ms: 1.10x faster                                                  |
| generators                    | 31.7 ms                                                | 28.9 ms: 1.10x faster                                                  |
| sympy_str                     | 166 ms                                                 | 153 ms: 1.09x faster                                                   |
| genshi_text                   | 17.7 ms                                                | 16.3 ms: 1.08x faster                                                  |
| pathlib                       | 25.7 ms                                                | 23.8 ms: 1.08x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 12.3 ms: 1.07x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.24 sec: 1.06x faster                                                 |
| xml_etree_parse               | 109 ms                                                 | 104 ms: 1.06x faster                                                   |
| mdp                           | 1.65 sec                                               | 1.57 sec: 1.05x faster                                                 |
| sympy_expand                  | 269 ms                                                 | 256 ms: 1.05x faster                                                   |
| many_optionals                | 486 us                                                 | 465 us: 1.04x faster                                                   |
| xml_etree_process             | 44.6 ms                                                | 42.8 ms: 1.04x faster                                                  |
| sqlglot_optimize              | 37.2 ms                                                | 35.7 ms: 1.04x faster                                                  |
| bench_thread_pool             | 545 us                                                 | 524 us: 1.04x faster                                                   |
| genshi_xml                    | 35.1 ms                                                | 33.9 ms: 1.04x faster                                                  |
| fannkuch                      | 303 ms                                                 | 292 ms: 1.04x faster                                                   |
| dask                          | 789 ms                                                 | 770 ms: 1.03x faster                                                   |
| json                          | 3.10 ms                                                | 3.06 ms: 1.02x faster                                                  |
| connected_components          | 318 ms                                                 | 314 ms: 1.01x faster                                                   |
| django_template               | 24.4 ms                                                | 24.2 ms: 1.01x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.32 ms: 1.01x faster                                                  |
| nbody                         | 92.5 ms                                                | 92.1 ms: 1.00x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 75.1 ms: 1.01x slower                                                  |
| meteor_contest                | 77.8 ms                                                | 78.7 ms: 1.01x slower                                                  |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                   |
| sqlglot_normalize             | 192 ms                                                 | 196 ms: 1.02x slower                                                   |
| nqueens                       | 63.8 ms                                                | 65.2 ms: 1.02x slower                                                  |
| shortest_path                 | 328 ms                                                 | 339 ms: 1.03x slower                                                   |
| sqlite_synth                  | 1.48 us                                                | 1.55 us: 1.05x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.7 us: 1.07x slower                                                  |
| xml_etree_generate            | 53.9 ms                                                | 58.2 ms: 1.08x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.26 ms: 1.08x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 61.5 ms: 1.10x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 14.5 ms: 1.14x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.08 ms: 1.14x slower                                                  |
| async_generators              | 233 ms                                                 | 268 ms: 1.15x slower                                                   |
| coverage                      | 41.2 ms                                                | 47.8 ms: 1.16x slower                                                  |
| telco                         | 3.49 ms                                                | 4.79 ms: 1.37x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.25x faster                                                           |

Benchmark hidden because not significant (2): python_startup, asyncio_websockets
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (8) of results/bm-20250303-3.14.0a5+-b3c18bf/bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.253x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.14x
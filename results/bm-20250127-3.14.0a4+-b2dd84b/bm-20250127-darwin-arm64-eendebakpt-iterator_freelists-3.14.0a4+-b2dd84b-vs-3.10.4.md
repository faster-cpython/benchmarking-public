# Results vs. 3.10.4

- fork: eendebakpt
- ref: iterator_freelists
- machine: darwin-arm64
- commit hash: b2dd84b
- commit date: 2025-01-27
- overall geometric mean: 1.402x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 187 ms: 1.08x faster                                                     |
| docutils       | 1.74 sec                                               | 1.40 sec: 1.24x faster                                                   |
| html5lib       | 43.5 ms                                                | 28.9 ms: 1.51x faster                                                    |
| sphinx         | 729 ms                                                 | 559 ms: 1.30x faster                                                     |
| Geometric mean | (ref)                                                  | 1.27x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 62.1 ms: 6.31x faster                                                    |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.46x faster                                                     |
| async_tree_io                 | 1.02 sec                                               | 360 ms: 2.83x faster                                                     |
| async_tree_eager_io           | 1.01 sec                                               | 360 ms: 2.81x faster                                                     |
| async_tree_none               | 391 ms                                                 | 159 ms: 2.47x faster                                                     |
| async_tree_memoization        | 481 ms                                                 | 198 ms: 2.43x faster                                                     |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 358 ms: 1.87x faster                                                     |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 419 ms: 1.60x faster                                                     |
| coroutines                    | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                    |
| async_generators              | 233 ms                                                 | 247 ms: 1.06x slower                                                     |
| Geometric mean                | (ref)                                                  | 2.11x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 46.0 ms: 1.58x faster                                                    |
| nbody          | 92.5 ms                                                | 68.1 ms: 1.36x faster                                                    |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.28x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 66.2 ms: 1.44x faster                                                    |
| regex_dna      | 175 ms                                                 | 140 ms: 1.25x faster                                                     |
| regex_v8       | 19.1 ms                                                | 16.6 ms: 1.15x faster                                                    |
| regex_effbot   | 2.34 ms                                                | 2.24 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                  | 1.21x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 195 us: 1.46x faster                                                     |
| unpickle_pure_python | 198 us                                                 | 138 us: 1.44x faster                                                     |
| tomli_loads          | 1.72 sec                                               | 1.19 sec: 1.44x faster                                                   |
| xml_etree_process    | 44.6 ms                                                | 38.0 ms: 1.17x faster                                                    |
| json_dumps           | 8.31 ms                                                | 7.40 ms: 1.12x faster                                                    |
| xml_etree_parse      | 109 ms                                                 | 101 ms: 1.08x faster                                                     |
| xml_etree_iterparse  | 74.5 ms                                                | 71.0 ms: 1.05x faster                                                    |
| xml_etree_generate   | 53.9 ms                                                | 52.3 ms: 1.03x faster                                                    |
| json_loads           | 16.6 us                                                | 17.7 us: 1.07x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 12.8 ms                                                | 14.8 ms: 1.16x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.97 ms: 1.41x faster                                                    |
| genshi_text     | 17.7 ms                                                | 13.1 ms: 1.35x faster                                                    |
| genshi_xml      | 35.1 ms                                                | 28.0 ms: 1.26x faster                                                    |
| django_template | 24.4 ms                                                | 20.3 ms: 1.20x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.30x faster                                                             |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 62.1 ms: 6.31x faster                                                    |
| typing_runtime_protocols      | 326 us                                                 | 92.0 us: 3.54x faster                                                    |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.46x faster                                                     |
| subparsers                    | 39.8 ms                                                | 11.8 ms: 3.37x faster                                                    |
| async_tree_io                 | 1.02 sec                                               | 360 ms: 2.83x faster                                                     |
| async_tree_eager_io           | 1.01 sec                                               | 360 ms: 2.81x faster                                                     |
| async_tree_none               | 391 ms                                                 | 159 ms: 2.47x faster                                                     |
| async_tree_memoization        | 481 ms                                                 | 198 ms: 2.43x faster                                                     |
| deltablue                     | 4.99 ms                                                | 2.29 ms: 2.18x faster                                                    |
| go                            | 163 ms                                                 | 77.0 ms: 2.12x faster                                                    |
| deepcopy_memo                 | 34.7 us                                                | 17.9 us: 1.94x faster                                                    |
| raytrace                      | 327 ms                                                 | 168 ms: 1.94x faster                                                     |
| deepcopy                      | 276 us                                                 | 147 us: 1.88x faster                                                     |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 358 ms: 1.87x faster                                                     |
| chaos                         | 67.7 ms                                                | 37.1 ms: 1.82x faster                                                    |
| scimark_sor                   | 140 ms                                                 | 77.0 ms: 1.82x faster                                                    |
| sqlglot_parse                 | 1.35 ms                                                | 760 us: 1.78x faster                                                     |
| logging_silent                | 117 ns                                                 | 66.6 ns: 1.76x faster                                                    |
| richards_super                | 61.0 ms                                                | 34.9 ms: 1.75x faster                                                    |
| scimark_monte_carlo           | 72.4 ms                                                | 42.2 ms: 1.72x faster                                                    |
| sqlglot_transpile             | 1.56 ms                                                | 920 us: 1.69x faster                                                     |
| richards                      | 52.3 ms                                                | 31.3 ms: 1.67x faster                                                    |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 419 ms: 1.60x faster                                                     |
| spectral_norm                 | 95.3 ms                                                | 60.4 ms: 1.58x faster                                                    |
| float                         | 72.4 ms                                                | 46.0 ms: 1.58x faster                                                    |
| pyflate                       | 448 ms                                                 | 287 ms: 1.56x faster                                                     |
| html5lib                      | 43.5 ms                                                | 28.9 ms: 1.51x faster                                                    |
| deepcopy_reduce               | 2.32 us                                                | 1.54 us: 1.51x faster                                                    |
| hexiom                        | 6.25 ms                                                | 4.18 ms: 1.50x faster                                                    |
| pylint                        | 231 ms                                                 | 157 ms: 1.47x faster                                                     |
| comprehensions                | 17.3 us                                                | 11.8 us: 1.47x faster                                                    |
| logging_simple                | 4.59 us                                                | 3.15 us: 1.46x faster                                                    |
| pickle_pure_python            | 285 us                                                 | 195 us: 1.46x faster                                                     |
| logging_format                | 5.03 us                                                | 3.47 us: 1.45x faster                                                    |
| regex_compile                 | 95.6 ms                                                | 66.2 ms: 1.44x faster                                                    |
| unpickle_pure_python          | 198 us                                                 | 138 us: 1.44x faster                                                     |
| tomli_loads                   | 1.72 sec                                               | 1.19 sec: 1.44x faster                                                   |
| pprint_pformat                | 1.33 sec                                               | 924 ms: 1.44x faster                                                     |
| scimark_lu                    | 103 ms                                                 | 71.8 ms: 1.43x faster                                                    |
| pprint_safe_repr              | 648 ms                                                 | 455 ms: 1.43x faster                                                     |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.39 ms: 1.42x faster                                                    |
| generators                    | 31.7 ms                                                | 22.4 ms: 1.42x faster                                                    |
| mako                          | 9.81 ms                                                | 6.97 ms: 1.41x faster                                                    |
| pycparser                     | 887 ms                                                 | 634 ms: 1.40x faster                                                     |
| crypto_pyaes                  | 73.3 ms                                                | 52.6 ms: 1.39x faster                                                    |
| nbody                         | 92.5 ms                                                | 68.1 ms: 1.36x faster                                                    |
| genshi_text                   | 17.7 ms                                                | 13.1 ms: 1.35x faster                                                    |
| k_core                        | 2.01 sec                                               | 1.50 sec: 1.34x faster                                                   |
| dulwich_log                   | 35.6 ms                                                | 26.8 ms: 1.33x faster                                                    |
| thrift                        | 562 us                                                 | 427 us: 1.32x faster                                                     |
| sqlalchemy_declarative        | 75.7 ms                                                | 57.6 ms: 1.31x faster                                                    |
| scimark_fft                   | 225 ms                                                 | 172 ms: 1.31x faster                                                     |
| sphinx                        | 729 ms                                                 | 559 ms: 1.30x faster                                                     |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.64 ms: 1.30x faster                                                    |
| coroutines                    | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                    |
| sympy_sum                     | 92.7 ms                                                | 72.6 ms: 1.28x faster                                                    |
| genshi_xml                    | 35.1 ms                                                | 28.0 ms: 1.26x faster                                                    |
| fannkuch                      | 303 ms                                                 | 242 ms: 1.25x faster                                                     |
| regex_dna                     | 175 ms                                                 | 140 ms: 1.25x faster                                                     |
| docutils                      | 1.74 sec                                               | 1.40 sec: 1.24x faster                                                   |
| sympy_str                     | 166 ms                                                 | 136 ms: 1.22x faster                                                     |
| bpe_tokeniser                 | 3.44 sec                                               | 2.85 sec: 1.21x faster                                                   |
| django_template               | 24.4 ms                                                | 20.3 ms: 1.20x faster                                                    |
| sympy_integrate               | 13.2 ms                                                | 11.0 ms: 1.20x faster                                                    |
| xml_etree_process             | 44.6 ms                                                | 38.0 ms: 1.17x faster                                                    |
| sympy_expand                  | 269 ms                                                 | 229 ms: 1.17x faster                                                     |
| bench_thread_pool             | 545 us                                                 | 468 us: 1.17x faster                                                     |
| sqlglot_optimize              | 37.2 ms                                                | 31.9 ms: 1.16x faster                                                    |
| regex_v8                      | 19.1 ms                                                | 16.6 ms: 1.15x faster                                                    |
| pathlib                       | 25.7 ms                                                | 22.7 ms: 1.14x faster                                                    |
| nqueens                       | 63.8 ms                                                | 56.5 ms: 1.13x faster                                                    |
| many_optionals                | 486 us                                                 | 431 us: 1.13x faster                                                     |
| json_dumps                    | 8.31 ms                                                | 7.40 ms: 1.12x faster                                                    |
| mdp                           | 1.65 sec                                               | 1.48 sec: 1.11x faster                                                   |
| meteor_contest                | 77.8 ms                                                | 70.1 ms: 1.11x faster                                                    |
| sqlglot_normalize             | 192 ms                                                 | 176 ms: 1.09x faster                                                     |
| xml_etree_parse               | 109 ms                                                 | 101 ms: 1.08x faster                                                     |
| 2to3                          | 201 ms                                                 | 187 ms: 1.08x faster                                                     |
| connected_components          | 318 ms                                                 | 296 ms: 1.08x faster                                                     |
| xml_etree_iterparse           | 74.5 ms                                                | 71.0 ms: 1.05x faster                                                    |
| regex_effbot                  | 2.34 ms                                                | 2.24 ms: 1.04x faster                                                    |
| xml_etree_generate            | 53.9 ms                                                | 52.3 ms: 1.03x faster                                                    |
| json                          | 3.10 ms                                                | 3.01 ms: 1.03x faster                                                    |
| dask                          | 789 ms                                                 | 770 ms: 1.02x faster                                                     |
| shortest_path                 | 328 ms                                                 | 323 ms: 1.02x faster                                                     |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                     |
| sqlite_synth                  | 1.48 us                                                | 1.52 us: 1.03x slower                                                    |
| async_generators              | 233 ms                                                 | 247 ms: 1.06x slower                                                     |
| json_loads                    | 16.6 us                                                | 17.7 us: 1.07x slower                                                    |
| bench_mp_pool                 | 56.0 ms                                                | 60.5 ms: 1.08x slower                                                    |
| create_gc_cycles              | 1.16 ms                                                | 1.28 ms: 1.10x slower                                                    |
| coverage                      | 41.2 ms                                                | 45.7 ms: 1.11x slower                                                    |
| gc_traversal                  | 2.71 ms                                                | 3.12 ms: 1.15x slower                                                    |
| python_startup_no_site        | 12.8 ms                                                | 14.8 ms: 1.16x slower                                                    |
| telco                         | 3.49 ms                                                | 4.56 ms: 1.31x slower                                                    |
| Geometric mean                | (ref)                                                  | 1.40x faster                                                             |

Benchmark hidden because not significant (2): python_startup, asyncio_websockets
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (8) of results/bm-20250127-3.14.0a4+-b2dd84b/bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.402x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.14x
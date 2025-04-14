# Results vs. 3.10.4

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: darwin-arm64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.257x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 177 ms: 1.14x faster                                                   |
| docutils       | 1.74 sec                                               | 1.49 sec: 1.16x faster                                                 |
| html5lib       | 43.5 ms                                                | 34.0 ms: 1.28x faster                                                  |
| sphinx         | 729 ms                                                 | 606 ms: 1.20x faster                                                   |
| Geometric mean | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 69.8 ms: 5.62x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 152 ms: 3.18x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 398 ms: 2.55x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 417 ms: 2.44x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 217 ms: 2.21x faster                                                   |
| async_tree_none               | 391 ms                                                 | 179 ms: 2.19x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 367 ms: 1.82x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 437 ms: 1.53x faster                                                   |
| coroutines                    | 20.5 ms                                                | 18.6 ms: 1.11x faster                                                  |
| async_generators              | 233 ms                                                 | 266 ms: 1.14x slower                                                   |
| Geometric mean                | (ref)                                                  | 1.94x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 54.3 ms: 1.33x faster                                                  |
| nbody          | 92.5 ms                                                | 92.1 ms: 1.00x faster                                                  |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 140 ms: 1.25x faster                                                   |
| regex_compile  | 95.6 ms                                                | 77.8 ms: 1.23x faster                                                  |
| regex_v8       | 19.1 ms                                                | 16.8 ms: 1.14x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.27 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 230 us: 1.24x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.45 sec: 1.19x faster                                                 |
| unpickle_pure_python | 198 us                                                 | 169 us: 1.17x faster                                                   |
| json_dumps           | 8.31 ms                                                | 7.57 ms: 1.10x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.06x faster                                                   |
| xml_etree_process    | 44.6 ms                                                | 42.7 ms: 1.05x faster                                                  |
| json_loads           | 16.6 us                                                | 17.8 us: 1.08x slower                                                  |
| xml_etree_generate   | 53.9 ms                                                | 58.2 ms: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.2 ms: 1.08x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 13.3 ms: 1.04x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.12 ms: 1.21x faster                                                  |
| genshi_text     | 17.7 ms                                                | 16.4 ms: 1.08x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 34.0 ms: 1.03x faster                                                  |
| django_template | 24.4 ms                                                | 24.2 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 69.8 ms: 5.62x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 152 ms: 3.18x faster                                                   |
| typing_runtime_protocols      | 326 us                                                 | 104 us: 3.14x faster                                                   |
| subparsers                    | 39.8 ms                                                | 13.0 ms: 3.07x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 398 ms: 2.55x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 417 ms: 2.44x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 217 ms: 2.21x faster                                                   |
| async_tree_none               | 391 ms                                                 | 179 ms: 2.19x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 367 ms: 1.82x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.80 ms: 1.78x faster                                                  |
| go                            | 163 ms                                                 | 94.8 ms: 1.72x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 21.0 us: 1.65x faster                                                  |
| deepcopy                      | 276 us                                                 | 168 us: 1.64x faster                                                   |
| logging_silent                | 117 ns                                                 | 73.0 ns: 1.60x faster                                                  |
| raytrace                      | 327 ms                                                 | 212 ms: 1.54x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 437 ms: 1.53x faster                                                   |
| chaos                         | 67.7 ms                                                | 44.3 ms: 1.53x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 92.4 ms: 1.51x faster                                                  |
| sqlglot_parse                 | 1.35 ms                                                | 896 us: 1.51x faster                                                   |
| scimark_monte_carlo           | 72.4 ms                                                | 50.0 ms: 1.45x faster                                                  |
| richards_super                | 61.0 ms                                                | 42.8 ms: 1.43x faster                                                  |
| sqlglot_transpile             | 1.56 ms                                                | 1.11 ms: 1.41x faster                                                  |
| richards                      | 52.3 ms                                                | 38.6 ms: 1.35x faster                                                  |
| pylint                        | 231 ms                                                 | 171 ms: 1.35x faster                                                   |
| float                         | 72.4 ms                                                | 54.3 ms: 1.33x faster                                                  |
| comprehensions                | 17.3 us                                                | 13.0 us: 1.33x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.76 us: 1.32x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.55 sec: 1.30x faster                                                 |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.02 ms: 1.29x faster                                                  |
| html5lib                      | 43.5 ms                                                | 34.0 ms: 1.28x faster                                                  |
| pyflate                       | 448 ms                                                 | 351 ms: 1.28x faster                                                   |
| pycparser                     | 887 ms                                                 | 704 ms: 1.26x faster                                                   |
| logging_format                | 5.03 us                                                | 4.01 us: 1.25x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 58.5 ms: 1.25x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 1.06 sec: 1.25x faster                                                 |
| regex_dna                     | 175 ms                                                 | 140 ms: 1.25x faster                                                   |
| logging_simple                | 4.59 us                                                | 3.71 us: 1.24x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 230 us: 1.24x faster                                                   |
| scimark_lu                    | 103 ms                                                 | 83.3 ms: 1.23x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 527 ms: 1.23x faster                                                   |
| regex_compile                 | 95.6 ms                                                | 77.8 ms: 1.23x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 77.8 ms: 1.23x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 62.0 ms: 1.22x faster                                                  |
| thrift                        | 562 us                                                 | 461 us: 1.22x faster                                                   |
| dulwich_log                   | 35.6 ms                                                | 29.4 ms: 1.21x faster                                                  |
| mako                          | 9.81 ms                                                | 8.12 ms: 1.21x faster                                                  |
| sphinx                        | 729 ms                                                 | 606 ms: 1.20x faster                                                   |
| hexiom                        | 6.25 ms                                                | 5.26 ms: 1.19x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.45 sec: 1.19x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 169 us: 1.17x faster                                                   |
| sympy_sum                     | 92.7 ms                                                | 79.4 ms: 1.17x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.49 sec: 1.16x faster                                                 |
| scimark_fft                   | 225 ms                                                 | 197 ms: 1.14x faster                                                   |
| regex_v8                      | 19.1 ms                                                | 16.8 ms: 1.14x faster                                                  |
| 2to3                          | 201 ms                                                 | 177 ms: 1.14x faster                                                   |
| coroutines                    | 20.5 ms                                                | 18.6 ms: 1.11x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.09 ms: 1.10x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 7.57 ms: 1.10x faster                                                  |
| generators                    | 31.7 ms                                                | 29.0 ms: 1.09x faster                                                  |
| sympy_str                     | 166 ms                                                 | 153 ms: 1.08x faster                                                   |
| genshi_text                   | 17.7 ms                                                | 16.4 ms: 1.08x faster                                                  |
| python_startup                | 19.6 ms                                                | 18.2 ms: 1.08x faster                                                  |
| pathlib                       | 25.7 ms                                                | 23.9 ms: 1.08x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 12.3 ms: 1.07x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.23 sec: 1.06x faster                                                 |
| mdp                           | 1.65 sec                                               | 1.56 sec: 1.06x faster                                                 |
| xml_etree_parse               | 109 ms                                                 | 104 ms: 1.06x faster                                                   |
| xml_etree_process             | 44.6 ms                                                | 42.7 ms: 1.05x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 258 ms: 1.04x faster                                                   |
| many_optionals                | 486 us                                                 | 467 us: 1.04x faster                                                   |
| bench_thread_pool             | 545 us                                                 | 525 us: 1.04x faster                                                   |
| sqlglot_optimize              | 37.2 ms                                                | 36.0 ms: 1.03x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 34.0 ms: 1.03x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.27 ms: 1.03x faster                                                  |
| dask                          | 789 ms                                                 | 769 ms: 1.03x faster                                                   |
| json                          | 3.10 ms                                                | 3.04 ms: 1.02x faster                                                  |
| fannkuch                      | 303 ms                                                 | 298 ms: 1.02x faster                                                   |
| django_template               | 24.4 ms                                                | 24.2 ms: 1.01x faster                                                  |
| nbody                         | 92.5 ms                                                | 92.1 ms: 1.00x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 77.6 ms: 1.00x faster                                                  |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                   |
| nqueens                       | 63.8 ms                                                | 65.0 ms: 1.02x slower                                                  |
| sqlglot_normalize             | 192 ms                                                 | 199 ms: 1.03x slower                                                   |
| sqlite_synth                  | 1.48 us                                                | 1.54 us: 1.04x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 13.3 ms: 1.04x slower                                                  |
| shortest_path                 | 328 ms                                                 | 348 ms: 1.06x slower                                                   |
| json_loads                    | 16.6 us                                                | 17.8 us: 1.08x slower                                                  |
| xml_etree_generate            | 53.9 ms                                                | 58.2 ms: 1.08x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 60.8 ms: 1.09x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.27 ms: 1.09x slower                                                  |
| async_generators              | 233 ms                                                 | 266 ms: 1.14x slower                                                   |
| gc_traversal                  | 2.71 ms                                                | 3.10 ms: 1.14x slower                                                  |
| coverage                      | 41.2 ms                                                | 47.9 ms: 1.16x slower                                                  |
| telco                         | 3.49 ms                                                | 4.74 ms: 1.36x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.25x faster                                                           |

Benchmark hidden because not significant (3): connected_components, asyncio_websockets, xml_etree_iterparse
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (16) of results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.257x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.13x
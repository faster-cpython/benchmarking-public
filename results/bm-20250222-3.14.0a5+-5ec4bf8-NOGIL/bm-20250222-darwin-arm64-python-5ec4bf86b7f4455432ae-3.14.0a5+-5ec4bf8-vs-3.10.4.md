# Results vs. 3.10.4

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: darwin-arm64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.205x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 195 ms: 1.03x faster                                                   |
| docutils       | 1.74 sec                                               | 1.45 sec: 1.20x faster                                                 |
| html5lib       | 43.5 ms                                                | 34.6 ms: 1.26x faster                                                  |
| sphinx         | 729 ms                                                 | 622 ms: 1.17x faster                                                   |
| Geometric mean | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 85.3 ms: 4.60x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 157 ms: 3.08x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 338 ms: 3.00x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 352 ms: 2.89x faster                                                   |
| async_tree_none               | 391 ms                                                 | 170 ms: 2.30x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 210 ms: 2.29x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 374 ms: 1.79x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 418 ms: 1.60x faster                                                   |
| coroutines                    | 20.5 ms                                                | 18.7 ms: 1.10x faster                                                  |
| asyncio_websockets            | 242 ms                                                 | 238 ms: 1.02x faster                                                   |
| async_generators              | 233 ms                                                 | 274 ms: 1.17x slower                                                   |
| Geometric mean                | (ref)                                                  | 1.97x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 55.0 ms: 1.32x faster                                                  |
| nbody          | 92.5 ms                                                | 101 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 137 ms: 1.28x faster                                                   |
| regex_v8       | 19.1 ms                                                | 15.7 ms: 1.22x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.11 ms: 1.11x faster                                                  |
| regex_compile  | 95.6 ms                                                | 86.8 ms: 1.10x faster                                                  |
| Geometric mean | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 250 us: 1.14x faster                                                   |
| xml_etree_parse      | 109 ms                                                 | 96.8 ms: 1.13x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 66.3 ms: 1.12x faster                                                  |
| unpickle_pure_python | 198 us                                                 | 182 us: 1.09x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.61 sec: 1.07x faster                                                 |
| json_dumps           | 8.31 ms                                                | 7.97 ms: 1.04x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 59.7 ms: 1.11x slower                                                  |
| json_loads           | 16.6 us                                                | 18.6 us: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.7 ms: 1.00x slower                                                  |
| python_startup_no_site | 12.8 ms                                                | 15.1 ms: 1.18x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 18.2 ms: 1.03x slower                                                  |
| genshi_xml      | 35.1 ms                                                | 37.0 ms: 1.05x slower                                                  |
| django_template | 24.4 ms                                                | 26.2 ms: 1.07x slower                                                  |
| mako            | 9.81 ms                                                | 10.9 ms: 1.11x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.07x slower                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 85.3 ms: 4.60x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 157 ms: 3.08x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 338 ms: 3.00x faster                                                   |
| subparsers                    | 39.8 ms                                                | 13.5 ms: 2.94x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 352 ms: 2.89x faster                                                   |
| typing_runtime_protocols      | 326 us                                                 | 117 us: 2.78x faster                                                   |
| async_tree_none               | 391 ms                                                 | 170 ms: 2.30x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 210 ms: 2.29x faster                                                   |
| gc_traversal                  | 2.71 ms                                                | 1.39 ms: 1.95x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 374 ms: 1.79x faster                                                   |
| deltablue                     | 4.99 ms                                                | 3.03 ms: 1.65x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 418 ms: 1.60x faster                                                   |
| create_gc_cycles              | 1.16 ms                                                | 736 us: 1.58x faster                                                   |
| go                            | 163 ms                                                 | 106 ms: 1.54x faster                                                   |
| deepcopy                      | 276 us                                                 | 183 us: 1.51x faster                                                   |
| deepcopy_memo                 | 34.7 us                                                | 24.6 us: 1.41x faster                                                  |
| raytrace                      | 327 ms                                                 | 237 ms: 1.38x faster                                                   |
| chaos                         | 67.7 ms                                                | 49.3 ms: 1.37x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 104 ms: 1.35x faster                                                   |
| logging_silent                | 117 ns                                                 | 87.3 ns: 1.34x faster                                                  |
| sqlglot_parse                 | 1.35 ms                                                | 1.02 ms: 1.33x faster                                                  |
| float                         | 72.4 ms                                                | 55.0 ms: 1.32x faster                                                  |
| sqlglot_transpile             | 1.56 ms                                                | 1.20 ms: 1.30x faster                                                  |
| pylint                        | 231 ms                                                 | 177 ms: 1.30x faster                                                   |
| pycparser                     | 887 ms                                                 | 687 ms: 1.29x faster                                                   |
| richards_super                | 61.0 ms                                                | 47.7 ms: 1.28x faster                                                  |
| regex_dna                     | 175 ms                                                 | 137 ms: 1.28x faster                                                   |
| html5lib                      | 43.5 ms                                                | 34.6 ms: 1.26x faster                                                  |
| richards                      | 52.3 ms                                                | 42.3 ms: 1.24x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 58.9 ms: 1.23x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 15.7 ms: 1.22x faster                                                  |
| pyflate                       | 448 ms                                                 | 370 ms: 1.21x faster                                                   |
| deepcopy_reduce               | 2.32 us                                                | 1.93 us: 1.21x faster                                                  |
| comprehensions                | 17.3 us                                                | 14.4 us: 1.21x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.45 sec: 1.20x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.69 sec: 1.19x faster                                                 |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.74 ms: 1.17x faster                                                  |
| sphinx                        | 729 ms                                                 | 622 ms: 1.17x faster                                                   |
| dulwich_log                   | 35.6 ms                                                | 31.1 ms: 1.14x faster                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.30 us: 1.14x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 250 us: 1.14x faster                                                   |
| logging_simple                | 4.59 us                                                | 4.05 us: 1.14x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 96.8 ms: 1.13x faster                                                  |
| logging_format                | 5.03 us                                                | 4.45 us: 1.13x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 66.3 ms: 1.12x faster                                                  |
| thrift                        | 562 us                                                 | 504 us: 1.12x faster                                                   |
| regex_effbot                  | 2.34 ms                                                | 2.11 ms: 1.11x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 86.8 ms: 1.10x faster                                                  |
| coroutines                    | 20.5 ms                                                | 18.7 ms: 1.10x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 69.3 ms: 1.09x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 67.2 ms: 1.09x faster                                                  |
| pathlib                       | 25.7 ms                                                | 23.6 ms: 1.09x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 1.22 sec: 1.09x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 85.2 ms: 1.09x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 182 us: 1.09x faster                                                   |
| hexiom                        | 6.25 ms                                                | 5.78 ms: 1.08x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 601 ms: 1.08x faster                                                   |
| tomli_loads                   | 1.72 sec                                               | 1.61 sec: 1.07x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 97.2 ms: 1.06x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 90.7 ms: 1.05x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 7.97 ms: 1.04x faster                                                  |
| generators                    | 31.7 ms                                                | 30.5 ms: 1.04x faster                                                  |
| 2to3                          | 201 ms                                                 | 195 ms: 1.03x faster                                                   |
| bpe_tokeniser                 | 3.44 sec                                               | 3.34 sec: 1.03x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 238 ms: 1.02x faster                                                   |
| many_optionals                | 486 us                                                 | 480 us: 1.01x faster                                                   |
| mdp                           | 1.65 sec                                               | 1.64 sec: 1.00x faster                                                 |
| python_startup                | 19.6 ms                                                | 19.7 ms: 1.00x slower                                                  |
| sympy_integrate               | 13.2 ms                                                | 13.2 ms: 1.00x slower                                                  |
| json                          | 3.10 ms                                                | 3.12 ms: 1.01x slower                                                  |
| sympy_str                     | 166 ms                                                 | 167 ms: 1.01x slower                                                   |
| genshi_text                   | 17.7 ms                                                | 18.2 ms: 1.03x slower                                                  |
| scimark_fft                   | 225 ms                                                 | 233 ms: 1.03x slower                                                   |
| sympy_expand                  | 269 ms                                                 | 280 ms: 1.04x slower                                                   |
| genshi_xml                    | 35.1 ms                                                | 37.0 ms: 1.05x slower                                                  |
| sqlglot_normalize             | 192 ms                                                 | 203 ms: 1.06x slower                                                   |
| fannkuch                      | 303 ms                                                 | 323 ms: 1.07x slower                                                   |
| django_template               | 24.4 ms                                                | 26.2 ms: 1.07x slower                                                  |
| nqueens                       | 63.8 ms                                                | 69.0 ms: 1.08x slower                                                  |
| nbody                         | 92.5 ms                                                | 101 ms: 1.09x slower                                                   |
| connected_components          | 318 ms                                                 | 348 ms: 1.09x slower                                                   |
| meteor_contest                | 77.8 ms                                                | 85.3 ms: 1.10x slower                                                  |
| xml_etree_generate            | 53.9 ms                                                | 59.7 ms: 1.11x slower                                                  |
| mako                          | 9.81 ms                                                | 10.9 ms: 1.11x slower                                                  |
| shortest_path                 | 328 ms                                                 | 366 ms: 1.12x slower                                                   |
| json_loads                    | 16.6 us                                                | 18.6 us: 1.12x slower                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.93 ms: 1.15x slower                                                  |
| async_generators              | 233 ms                                                 | 274 ms: 1.17x slower                                                   |
| bench_mp_pool                 | 56.0 ms                                                | 65.9 ms: 1.18x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 15.1 ms: 1.18x slower                                                  |
| coverage                      | 41.2 ms                                                | 54.0 ms: 1.31x slower                                                  |
| telco                         | 3.49 ms                                                | 5.16 ms: 1.48x slower                                                  |
| bench_thread_pool             | 545 us                                                 | 815 us: 1.49x slower                                                   |
| Geometric mean                | (ref)                                                  | 1.19x faster                                                           |

Benchmark hidden because not significant (3): xml_etree_process, pidigits, sqlglot_optimize
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, tornado_http
Ignored benchmarks (16) of results/bm-20250222-3.14.0a5+-5ec4bf8-NOGIL/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.205x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.29x
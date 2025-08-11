# Results vs. 3.10.4

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: darwin-arm64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.284x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 181 ms: 1.11x faster                                                  |
| docutils       | 1.74 sec                                               | 1.40 sec: 1.24x faster                                                |
| html5lib       | 43.5 ms                                                | 32.8 ms: 1.33x faster                                                 |
| sphinx         | 729 ms                                                 | 581 ms: 1.26x faster                                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 74.0 ms: 5.30x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 137 ms: 3.52x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 305 ms: 3.33x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 319 ms: 3.19x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 184 ms: 2.61x faster                                                  |
| async_tree_none               | 391 ms                                                 | 153 ms: 2.56x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.88x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 397 ms: 1.69x faster                                                  |
| coroutines                    | 20.5 ms                                                | 16.7 ms: 1.23x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| async_generators              | 233 ms                                                 | 282 ms: 1.21x slower                                                  |
| Geometric mean                | (ref)                                                  | 2.14x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 47.7 ms: 1.52x faster                                                 |
| nbody          | 92.5 ms                                                | 87.7 ms: 1.06x faster                                                 |
| pidigits       | 280 ms                                                 | 277 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.17x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 19.1 ms                                                | 14.7 ms: 1.30x faster                                                 |
| regex_dna      | 175 ms                                                 | 137 ms: 1.28x faster                                                  |
| regex_compile  | 95.6 ms                                                | 78.3 ms: 1.22x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.23 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 8.31 ms                                                | 6.04 ms: 1.38x faster                                                 |
| pickle_pure_python   | 285 us                                                 | 226 us: 1.26x faster                                                  |
| unpickle_pure_python | 198 us                                                 | 164 us: 1.21x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 63.2 ms: 1.18x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 95.6 ms: 1.14x faster                                                 |
| tomli_loads          | 1.72 sec                                               | 1.54 sec: 1.11x faster                                                |
| xml_etree_process    | 44.6 ms                                                | 41.5 ms: 1.08x faster                                                 |
| xml_etree_generate   | 53.9 ms                                                | 57.1 ms: 1.06x slower                                                 |
| json_loads           | 16.6 us                                                | 18.0 us: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 12.8 ms                                                | 14.7 ms: 1.15x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 24.4 ms                                                | 23.9 ms: 1.02x faster                                                 |
| genshi_text     | 17.7 ms                                                | 17.6 ms: 1.01x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 36.5 ms: 1.04x slower                                                 |
| mako            | 9.81 ms                                                | 10.6 ms: 1.08x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 74.0 ms: 5.30x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 137 ms: 3.52x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 305 ms: 3.33x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 319 ms: 3.19x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 113 us: 2.89x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 184 ms: 2.61x faster                                                  |
| async_tree_none               | 391 ms                                                 | 153 ms: 2.56x faster                                                  |
| gc_traversal                  | 2.71 ms                                                | 1.30 ms: 2.08x faster                                                 |
| deltablue                     | 4.99 ms                                                | 2.52 ms: 1.98x faster                                                 |
| mdp                           | 1.65 sec                                               | 848 ms: 1.95x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.88x faster                                                  |
| go                            | 163 ms                                                 | 91.4 ms: 1.79x faster                                                 |
| raytrace                      | 327 ms                                                 | 191 ms: 1.71x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 397 ms: 1.69x faster                                                  |
| chaos                         | 67.7 ms                                                | 42.3 ms: 1.60x faster                                                 |
| logging_silent                | 117 ns                                                 | 75.5 ns: 1.55x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 91.5 ms: 1.53x faster                                                 |
| float                         | 72.4 ms                                                | 47.7 ms: 1.52x faster                                                 |
| create_gc_cycles              | 1.16 ms                                                | 775 us: 1.50x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 23.2 us: 1.49x faster                                                 |
| deepcopy                      | 276 us                                                 | 186 us: 1.48x faster                                                  |
| richards_super                | 61.0 ms                                                | 41.1 ms: 1.48x faster                                                 |
| subparsers                    | 39.8 ms                                                | 27.0 ms: 1.47x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 49.8 ms: 1.45x faster                                                 |
| pyflate                       | 448 ms                                                 | 311 ms: 1.44x faster                                                  |
| richards                      | 52.3 ms                                                | 36.4 ms: 1.44x faster                                                 |
| pylint                        | 231 ms                                                 | 167 ms: 1.38x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 6.04 ms: 1.38x faster                                                 |
| comprehensions                | 17.3 us                                                | 12.6 us: 1.37x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 26.0 ms: 1.37x faster                                                 |
| pycparser                     | 887 ms                                                 | 653 ms: 1.36x faster                                                  |
| html5lib                      | 43.5 ms                                                | 32.8 ms: 1.33x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 73.2 ms: 1.30x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 14.7 ms: 1.30x faster                                                 |
| regex_dna                     | 175 ms                                                 | 137 ms: 1.28x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 226 us: 1.26x faster                                                  |
| generators                    | 31.7 ms                                                | 25.2 ms: 1.26x faster                                                 |
| sphinx                        | 729 ms                                                 | 581 ms: 1.26x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 58.4 ms: 1.26x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.61 sec: 1.25x faster                                                |
| hexiom                        | 6.25 ms                                                | 5.01 ms: 1.25x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.40 sec: 1.24x faster                                                |
| coroutines                    | 20.5 ms                                                | 16.7 ms: 1.23x faster                                                 |
| logging_simple                | 4.59 us                                                | 3.76 us: 1.22x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 78.3 ms: 1.22x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 164 us: 1.21x faster                                                  |
| logging_format                | 5.03 us                                                | 4.15 us: 1.21x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 84.8 ms: 1.21x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.93 us: 1.20x faster                                                 |
| xml_etree_iterparse           | 74.5 ms                                                | 63.2 ms: 1.18x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.14 sec: 1.17x faster                                                |
| pprint_safe_repr              | 648 ms                                                 | 558 ms: 1.16x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 95.6 ms: 1.14x faster                                                 |
| thrift                        | 562 us                                                 | 493 us: 1.14x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 11.6 ms: 1.14x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 83.0 ms: 1.12x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.54 sec: 1.11x faster                                                |
| 2to3                          | 201 ms                                                 | 181 ms: 1.11x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.12 sec: 1.10x faster                                                |
| scimark_fft                   | 225 ms                                                 | 205 ms: 1.10x faster                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.37 us: 1.08x faster                                                 |
| xml_etree_process             | 44.6 ms                                                | 41.5 ms: 1.08x faster                                                 |
| pathlib                       | 25.7 ms                                                | 24.2 ms: 1.07x faster                                                 |
| nbody                         | 92.5 ms                                                | 87.7 ms: 1.06x faster                                                 |
| sympy_str                     | 166 ms                                                 | 159 ms: 1.05x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.23 ms: 1.04x faster                                                 |
| fannkuch                      | 303 ms                                                 | 294 ms: 1.03x faster                                                  |
| json                          | 3.10 ms                                                | 3.04 ms: 1.02x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| django_template               | 24.4 ms                                                | 23.9 ms: 1.02x faster                                                 |
| pidigits                      | 280 ms                                                 | 277 ms: 1.01x faster                                                  |
| genshi_text                   | 17.7 ms                                                | 17.6 ms: 1.01x faster                                                 |
| dask                          | 789 ms                                                 | 804 ms: 1.02x slower                                                  |
| connected_components          | 318 ms                                                 | 328 ms: 1.03x slower                                                  |
| nqueens                       | 63.8 ms                                                | 65.9 ms: 1.03x slower                                                 |
| genshi_xml                    | 35.1 ms                                                | 36.5 ms: 1.04x slower                                                 |
| xml_etree_generate            | 53.9 ms                                                | 57.1 ms: 1.06x slower                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.64 ms: 1.07x slower                                                 |
| meteor_contest                | 77.8 ms                                                | 83.5 ms: 1.07x slower                                                 |
| shortest_path                 | 328 ms                                                 | 353 ms: 1.08x slower                                                  |
| mako                          | 9.81 ms                                                | 10.6 ms: 1.08x slower                                                 |
| json_loads                    | 16.6 us                                                | 18.0 us: 1.09x slower                                                 |
| python_startup_no_site        | 12.8 ms                                                | 14.7 ms: 1.15x slower                                                 |
| async_generators              | 233 ms                                                 | 282 ms: 1.21x slower                                                  |
| many_optionals                | 486 us                                                 | 599 us: 1.23x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 76.0 ms: 1.36x slower                                                 |
| bench_thread_pool             | 545 us                                                 | 753 us: 1.38x slower                                                  |
| telco                         | 3.49 ms                                                | 5.04 ms: 1.45x slower                                                 |
| coverage                      | 41.2 ms                                                | 62.6 ms: 1.52x slower                                                 |
| Geometric mean                | (ref)                                                  | 1.28x faster                                                          |

Benchmark hidden because not significant (2): python_startup, sympy_expand
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250809-3.15.0a0-046a4e3-NOGIL/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.284x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 1.35x
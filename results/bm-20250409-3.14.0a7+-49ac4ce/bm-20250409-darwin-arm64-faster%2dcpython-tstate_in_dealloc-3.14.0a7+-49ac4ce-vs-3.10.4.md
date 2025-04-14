# Results vs. 3.10.4

- fork: faster-cpython
- ref: tstate_in_dealloc
- machine: darwin-arm64
- commit hash: 49ac4ce
- commit date: 2025-04-09
- overall geometric mean: 1.387x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 161 ms: 1.25x faster                                                          |
| docutils       | 1.74 sec                                               | 1.43 sec: 1.21x faster                                                        |
| html5lib       | 43.5 ms                                                | 29.7 ms: 1.46x faster                                                         |
| sphinx         | 729 ms                                                 | 579 ms: 1.26x faster                                                          |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|-------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 62.8 ms: 6.24x faster                                                         |
| async_tree_eager_memoization  | 483 ms                                                 | 138 ms: 3.51x faster                                                          |
| async_tree_eager_io           | 1.01 sec                                               | 359 ms: 2.83x faster                                                          |
| async_tree_io                 | 1.02 sec                                               | 375 ms: 2.71x faster                                                          |
| async_tree_memoization        | 481 ms                                                 | 191 ms: 2.52x faster                                                          |
| async_tree_none               | 391 ms                                                 | 161 ms: 2.43x faster                                                          |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 359 ms: 1.86x faster                                                          |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 412 ms: 1.62x faster                                                          |
| coroutines                    | 20.5 ms                                                | 16.6 ms: 1.24x faster                                                         |
| async_generators              | 233 ms                                                 | 266 ms: 1.14x slower                                                          |
| Geometric mean                | (ref)                                                  | 2.09x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 47.0 ms: 1.54x faster                                                         |
| nbody          | 92.5 ms                                                | 71.7 ms: 1.29x faster                                                         |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                  | 1.25x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 67.6 ms: 1.41x faster                                                         |
| regex_dna      | 175 ms                                                 | 140 ms: 1.24x faster                                                          |
| regex_v8       | 19.1 ms                                                | 15.5 ms: 1.23x faster                                                         |
| regex_effbot   | 2.34 ms                                                | 2.24 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                  | 1.23x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.72 sec                                               | 1.21 sec: 1.42x faster                                                        |
| pickle_pure_python   | 285 us                                                 | 205 us: 1.39x faster                                                          |
| unpickle_pure_python | 198 us                                                 | 149 us: 1.33x faster                                                          |
| xml_etree_process    | 44.6 ms                                                | 38.6 ms: 1.16x faster                                                         |
| json_dumps           | 8.31 ms                                                | 7.48 ms: 1.11x faster                                                         |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.05x faster                                                          |
| xml_etree_iterparse  | 74.5 ms                                                | 71.8 ms: 1.04x faster                                                         |
| xml_etree_generate   | 53.9 ms                                                | 54.8 ms: 1.02x slower                                                         |
| json_loads           | 16.6 us                                                | 18.1 us: 1.09x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.2 ms: 1.14x faster                                                         |
| python_startup_no_site | 12.8 ms                                                | 13.0 ms: 1.01x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.62 ms: 1.29x faster                                                         |
| genshi_text     | 17.7 ms                                                | 13.8 ms: 1.28x faster                                                         |
| genshi_xml      | 35.1 ms                                                | 28.8 ms: 1.22x faster                                                         |
| django_template | 24.4 ms                                                | 21.0 ms: 1.16x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.24x faster                                                                  |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|-------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 62.8 ms: 6.24x faster                                                         |
| async_tree_eager_memoization  | 483 ms                                                 | 138 ms: 3.51x faster                                                          |
| typing_runtime_protocols      | 326 us                                                 | 93.9 us: 3.47x faster                                                         |
| subparsers                    | 39.8 ms                                                | 12.3 ms: 3.23x faster                                                         |
| async_tree_eager_io           | 1.01 sec                                               | 359 ms: 2.83x faster                                                          |
| async_tree_io                 | 1.02 sec                                               | 375 ms: 2.71x faster                                                          |
| async_tree_memoization        | 481 ms                                                 | 191 ms: 2.52x faster                                                          |
| async_tree_none               | 391 ms                                                 | 161 ms: 2.43x faster                                                          |
| mdp                           | 1.65 sec                                               | 765 ms: 2.16x faster                                                          |
| deltablue                     | 4.99 ms                                                | 2.35 ms: 2.12x faster                                                         |
| go                            | 163 ms                                                 | 79.9 ms: 2.05x faster                                                         |
| deepcopy_memo                 | 34.7 us                                                | 18.2 us: 1.90x faster                                                         |
| raytrace                      | 327 ms                                                 | 172 ms: 1.90x faster                                                          |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 359 ms: 1.86x faster                                                          |
| deepcopy                      | 276 us                                                 | 153 us: 1.81x faster                                                          |
| chaos                         | 67.7 ms                                                | 38.0 ms: 1.78x faster                                                         |
| scimark_sor                   | 140 ms                                                 | 79.5 ms: 1.76x faster                                                         |
| logging_silent                | 117 ns                                                 | 67.1 ns: 1.75x faster                                                         |
| scimark_monte_carlo           | 72.4 ms                                                | 42.2 ms: 1.72x faster                                                         |
| richards_super                | 61.0 ms                                                | 36.5 ms: 1.67x faster                                                         |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 412 ms: 1.62x faster                                                          |
| richards                      | 52.3 ms                                                | 32.5 ms: 1.61x faster                                                         |
| float                         | 72.4 ms                                                | 47.0 ms: 1.54x faster                                                         |
| pyflate                       | 448 ms                                                 | 291 ms: 1.54x faster                                                          |
| comprehensions                | 17.3 us                                                | 11.5 us: 1.51x faster                                                         |
| html5lib                      | 43.5 ms                                                | 29.7 ms: 1.46x faster                                                         |
| dulwich_log                   | 35.6 ms                                                | 24.5 ms: 1.45x faster                                                         |
| hexiom                        | 6.25 ms                                                | 4.34 ms: 1.44x faster                                                         |
| deepcopy_reduce               | 2.32 us                                                | 1.62 us: 1.43x faster                                                         |
| logging_simple                | 4.59 us                                                | 3.22 us: 1.43x faster                                                         |
| logging_format                | 5.03 us                                                | 3.54 us: 1.42x faster                                                         |
| pylint                        | 231 ms                                                 | 162 ms: 1.42x faster                                                          |
| tomli_loads                   | 1.72 sec                                               | 1.21 sec: 1.42x faster                                                        |
| regex_compile                 | 95.6 ms                                                | 67.6 ms: 1.41x faster                                                         |
| pickle_pure_python            | 285 us                                                 | 205 us: 1.39x faster                                                          |
| spectral_norm                 | 95.3 ms                                                | 68.9 ms: 1.38x faster                                                         |
| scimark_lu                    | 103 ms                                                 | 74.2 ms: 1.38x faster                                                         |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.57 ms: 1.38x faster                                                         |
| generators                    | 31.7 ms                                                | 23.4 ms: 1.35x faster                                                         |
| pycparser                     | 887 ms                                                 | 656 ms: 1.35x faster                                                          |
| pprint_pformat                | 1.33 sec                                               | 986 ms: 1.35x faster                                                          |
| pprint_safe_repr              | 648 ms                                                 | 487 ms: 1.33x faster                                                          |
| unpickle_pure_python          | 198 us                                                 | 149 us: 1.33x faster                                                          |
| crypto_pyaes                  | 73.3 ms                                                | 55.6 ms: 1.32x faster                                                         |
| k_core                        | 2.01 sec                                               | 1.53 sec: 1.31x faster                                                        |
| nbody                         | 92.5 ms                                                | 71.7 ms: 1.29x faster                                                         |
| mako                          | 9.81 ms                                                | 7.62 ms: 1.29x faster                                                         |
| genshi_text                   | 17.7 ms                                                | 13.8 ms: 1.28x faster                                                         |
| sqlalchemy_declarative        | 75.7 ms                                                | 59.9 ms: 1.26x faster                                                         |
| sphinx                        | 729 ms                                                 | 579 ms: 1.26x faster                                                          |
| 2to3                          | 201 ms                                                 | 161 ms: 1.25x faster                                                          |
| regex_dna                     | 175 ms                                                 | 140 ms: 1.24x faster                                                          |
| coroutines                    | 20.5 ms                                                | 16.6 ms: 1.24x faster                                                         |
| scimark_fft                   | 225 ms                                                 | 183 ms: 1.23x faster                                                          |
| sympy_sum                     | 92.7 ms                                                | 75.1 ms: 1.23x faster                                                         |
| regex_v8                      | 19.1 ms                                                | 15.5 ms: 1.23x faster                                                         |
| genshi_xml                    | 35.1 ms                                                | 28.8 ms: 1.22x faster                                                         |
| sympy_integrate               | 13.2 ms                                                | 10.8 ms: 1.22x faster                                                         |
| docutils                      | 1.74 sec                                               | 1.43 sec: 1.21x faster                                                        |
| sympy_str                     | 166 ms                                                 | 142 ms: 1.17x faster                                                          |
| django_template               | 24.4 ms                                                | 21.0 ms: 1.16x faster                                                         |
| xml_etree_process             | 44.6 ms                                                | 38.6 ms: 1.16x faster                                                         |
| fannkuch                      | 303 ms                                                 | 262 ms: 1.15x faster                                                          |
| python_startup                | 19.6 ms                                                | 17.2 ms: 1.14x faster                                                         |
| bpe_tokeniser                 | 3.44 sec                                               | 3.04 sec: 1.13x faster                                                        |
| sympy_expand                  | 269 ms                                                 | 241 ms: 1.12x faster                                                          |
| json_dumps                    | 8.31 ms                                                | 7.48 ms: 1.11x faster                                                         |
| bench_thread_pool             | 545 us                                                 | 495 us: 1.10x faster                                                          |
| many_optionals                | 486 us                                                 | 446 us: 1.09x faster                                                          |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.14 ms: 1.09x faster                                                         |
| meteor_contest                | 77.8 ms                                                | 72.1 ms: 1.08x faster                                                         |
| nqueens                       | 63.8 ms                                                | 59.3 ms: 1.08x faster                                                         |
| pathlib                       | 25.7 ms                                                | 24.0 ms: 1.07x faster                                                         |
| xml_etree_parse               | 109 ms                                                 | 104 ms: 1.05x faster                                                          |
| connected_components          | 318 ms                                                 | 303 ms: 1.05x faster                                                          |
| regex_effbot                  | 2.34 ms                                                | 2.24 ms: 1.04x faster                                                         |
| xml_etree_iterparse           | 74.5 ms                                                | 71.8 ms: 1.04x faster                                                         |
| json                          | 3.10 ms                                                | 3.09 ms: 1.01x faster                                                         |
| shortest_path                 | 328 ms                                                 | 331 ms: 1.01x slower                                                          |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                          |
| python_startup_no_site        | 12.8 ms                                                | 13.0 ms: 1.01x slower                                                         |
| xml_etree_generate            | 53.9 ms                                                | 54.8 ms: 1.02x slower                                                         |
| sqlite_synth                  | 1.48 us                                                | 1.55 us: 1.04x slower                                                         |
| bench_mp_pool                 | 56.0 ms                                                | 59.3 ms: 1.06x slower                                                         |
| json_loads                    | 16.6 us                                                | 18.1 us: 1.09x slower                                                         |
| create_gc_cycles              | 1.16 ms                                                | 1.28 ms: 1.10x slower                                                         |
| async_generators              | 233 ms                                                 | 266 ms: 1.14x slower                                                          |
| coverage                      | 41.2 ms                                                | 47.0 ms: 1.14x slower                                                         |
| gc_traversal                  | 2.71 ms                                                | 3.10 ms: 1.15x slower                                                         |
| telco                         | 3.49 ms                                                | 4.70 ms: 1.35x slower                                                         |
| Geometric mean                | (ref)                                                  | 1.38x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250409-3.14.0a7+-49ac4ce/bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.387x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.14x
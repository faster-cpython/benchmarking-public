# Results vs. base

- fork: faster-cpython
- ref: tstate_in_dealloc
- machine: darwin-arm64
- commit hash: 49ac4ce
- commit date: 2025-04-09
- overall geometric mean: 1.039x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 167 ms                                                                 | 161 ms: 1.04x faster                                                          |
| docutils       | 1.45 sec                                                               | 1.43 sec: 1.01x faster                                                        |
| html5lib       | 31.6 ms                                                                | 29.7 ms: 1.06x faster                                                         |
| sphinx         | 589 ms                                                                 | 579 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                       | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|---------------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none                 | 169 ms                                                                 | 161 ms: 1.05x faster                                                          |
| coroutines                      | 17.3 ms                                                                | 16.6 ms: 1.04x faster                                                         |
| async_tree_io                   | 392 ms                                                                 | 375 ms: 1.04x faster                                                          |
| async_tree_memoization          | 199 ms                                                                 | 191 ms: 1.04x faster                                                          |
| async_tree_eager                | 65.4 ms                                                                | 62.8 ms: 1.04x faster                                                         |
| async_tree_io_tg                | 375 ms                                                                 | 361 ms: 1.04x faster                                                          |
| async_tree_none_tg              | 160 ms                                                                 | 154 ms: 1.04x faster                                                          |
| async_tree_eager_io             | 371 ms                                                                 | 359 ms: 1.03x faster                                                          |
| async_tree_memoization_tg       | 196 ms                                                                 | 190 ms: 1.03x faster                                                          |
| async_tree_eager_io_tg          | 384 ms                                                                 | 373 ms: 1.03x faster                                                          |
| async_tree_eager_tg             | 135 ms                                                                 | 131 ms: 1.03x faster                                                          |
| async_tree_eager_memoization    | 141 ms                                                                 | 138 ms: 1.02x faster                                                          |
| async_tree_eager_memoization_tg | 173 ms                                                                 | 170 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed         | 417 ms                                                                 | 412 ms: 1.01x faster                                                          |
| asyncio_websockets              | 242 ms                                                                 | 242 ms: 1.00x faster                                                          |
| async_tree_eager_cpu_io_mixed   | 358 ms                                                                 | 359 ms: 1.01x slower                                                          |
| async_generators                | 264 ms                                                                 | 266 ms: 1.01x slower                                                          |
| Geometric mean                  | (ref)                                                                  | 1.02x faster                                                                  |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 75.7 ms                                                                | 71.7 ms: 1.06x faster                                                         |
| float          | 49.3 ms                                                                | 47.0 ms: 1.05x faster                                                         |
| pidigits       | 283 ms                                                                 | 284 ms: 1.00x slower                                                          |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 72.4 ms                                                                | 67.6 ms: 1.07x faster                                                         |
| regex_v8       | 15.6 ms                                                                | 15.5 ms: 1.00x faster                                                         |
| regex_effbot   | 2.25 ms                                                                | 2.24 ms: 1.00x faster                                                         |
| regex_dna      | 141 ms                                                                 | 140 ms: 1.00x faster                                                          |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.34 sec                                                               | 1.21 sec: 1.10x faster                                                        |
| unpickle_pure_python | 162 us                                                                 | 149 us: 1.09x faster                                                          |
| pickle_pure_python   | 220 us                                                                 | 205 us: 1.07x faster                                                          |
| xml_etree_process    | 40.0 ms                                                                | 38.6 ms: 1.03x faster                                                         |
| xml_etree_generate   | 56.5 ms                                                                | 54.8 ms: 1.03x faster                                                         |
| xml_etree_iterparse  | 73.9 ms                                                                | 71.8 ms: 1.03x faster                                                         |
| json_dumps           | 7.51 ms                                                                | 7.48 ms: 1.00x faster                                                         |
| json_loads           | 17.8 us                                                                | 18.1 us: 1.02x slower                                                         |
| Geometric mean       | (ref)                                                                  | 1.04x faster                                                                  |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 13.9 ms                                                                | 13.0 ms: 1.07x faster                                                         |
| python_startup         | 18.1 ms                                                                | 17.2 ms: 1.05x faster                                                         |
| Geometric mean         | (ref)                                                                  | 1.06x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 15.0 ms                                                                | 13.8 ms: 1.09x faster                                                         |
| genshi_xml      | 30.8 ms                                                                | 28.8 ms: 1.07x faster                                                         |
| django_template | 22.2 ms                                                                | 21.0 ms: 1.06x faster                                                         |
| mako            | 7.85 ms                                                                | 7.62 ms: 1.03x faster                                                         |
| Geometric mean  | (ref)                                                                  | 1.06x faster                                                                  |

All benchmarks:
===============

| Benchmark                       | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|---------------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| scimark_sor                     | 88.8 ms                                                                | 79.5 ms: 1.12x faster                                                         |
| richards                        | 36.3 ms                                                                | 32.5 ms: 1.11x faster                                                         |
| go                              | 88.8 ms                                                                | 79.9 ms: 1.11x faster                                                         |
| hexiom                          | 4.81 ms                                                                | 4.34 ms: 1.11x faster                                                         |
| tomli_loads                     | 1.34 sec                                                               | 1.21 sec: 1.10x faster                                                        |
| richards_super                  | 40.1 ms                                                                | 36.5 ms: 1.10x faster                                                         |
| scimark_lu                      | 81.4 ms                                                                | 74.2 ms: 1.10x faster                                                         |
| scimark_monte_carlo             | 46.3 ms                                                                | 42.2 ms: 1.10x faster                                                         |
| comprehensions                  | 12.6 us                                                                | 11.5 us: 1.10x faster                                                         |
| pyflate                         | 318 ms                                                                 | 291 ms: 1.10x faster                                                          |
| fannkuch                        | 286 ms                                                                 | 262 ms: 1.09x faster                                                          |
| genshi_text                     | 15.0 ms                                                                | 13.8 ms: 1.09x faster                                                         |
| deltablue                       | 2.56 ms                                                                | 2.35 ms: 1.09x faster                                                         |
| unpickle_pure_python            | 162 us                                                                 | 149 us: 1.09x faster                                                          |
| deepcopy_memo                   | 19.6 us                                                                | 18.2 us: 1.07x faster                                                         |
| pickle_pure_python              | 220 us                                                                 | 205 us: 1.07x faster                                                          |
| python_startup_no_site          | 13.9 ms                                                                | 13.0 ms: 1.07x faster                                                         |
| regex_compile                   | 72.4 ms                                                                | 67.6 ms: 1.07x faster                                                         |
| logging_simple                  | 3.45 us                                                                | 3.22 us: 1.07x faster                                                         |
| genshi_xml                      | 30.8 ms                                                                | 28.8 ms: 1.07x faster                                                         |
| html5lib                        | 31.6 ms                                                                | 29.7 ms: 1.06x faster                                                         |
| sqlglot_v2_transpile            | 1.00 ms                                                                | 946 us: 1.06x faster                                                          |
| sqlglot_v2_parse                | 834 us                                                                 | 787 us: 1.06x faster                                                          |
| logging_format                  | 3.75 us                                                                | 3.54 us: 1.06x faster                                                         |
| connected_components            | 322 ms                                                                 | 303 ms: 1.06x faster                                                          |
| chaos                           | 40.1 ms                                                                | 38.0 ms: 1.06x faster                                                         |
| scimark_fft                     | 193 ms                                                                 | 183 ms: 1.06x faster                                                          |
| django_template                 | 22.2 ms                                                                | 21.0 ms: 1.06x faster                                                         |
| nbody                           | 75.7 ms                                                                | 71.7 ms: 1.06x faster                                                         |
| python_startup                  | 18.1 ms                                                                | 17.2 ms: 1.05x faster                                                         |
| nqueens                         | 62.4 ms                                                                | 59.3 ms: 1.05x faster                                                         |
| pprint_safe_repr                | 511 ms                                                                 | 487 ms: 1.05x faster                                                          |
| async_tree_none                 | 169 ms                                                                 | 161 ms: 1.05x faster                                                          |
| float                           | 49.3 ms                                                                | 47.0 ms: 1.05x faster                                                         |
| pprint_pformat                  | 1.04 sec                                                               | 986 ms: 1.05x faster                                                          |
| logging_silent                  | 70.2 ns                                                                | 67.1 ns: 1.05x faster                                                         |
| typing_runtime_protocols        | 98.3 us                                                                | 93.9 us: 1.05x faster                                                         |
| coroutines                      | 17.3 ms                                                                | 16.6 ms: 1.04x faster                                                         |
| async_tree_io                   | 392 ms                                                                 | 375 ms: 1.04x faster                                                          |
| async_tree_memoization          | 199 ms                                                                 | 191 ms: 1.04x faster                                                          |
| pycparser                       | 683 ms                                                                 | 656 ms: 1.04x faster                                                          |
| 2to3                            | 167 ms                                                                 | 161 ms: 1.04x faster                                                          |
| async_tree_eager                | 65.4 ms                                                                | 62.8 ms: 1.04x faster                                                         |
| raytrace                        | 179 ms                                                                 | 172 ms: 1.04x faster                                                          |
| async_tree_io_tg                | 375 ms                                                                 | 361 ms: 1.04x faster                                                          |
| async_tree_none_tg              | 160 ms                                                                 | 154 ms: 1.04x faster                                                          |
| generators                      | 24.3 ms                                                                | 23.4 ms: 1.04x faster                                                         |
| deepcopy                        | 158 us                                                                 | 153 us: 1.04x faster                                                          |
| meteor_contest                  | 74.7 ms                                                                | 72.1 ms: 1.04x faster                                                         |
| sympy_integrate                 | 11.2 ms                                                                | 10.8 ms: 1.03x faster                                                         |
| xml_etree_process               | 40.0 ms                                                                | 38.6 ms: 1.03x faster                                                         |
| async_tree_eager_io             | 371 ms                                                                 | 359 ms: 1.03x faster                                                          |
| sqlalchemy_imperative           | 6.79 ms                                                                | 6.57 ms: 1.03x faster                                                         |
| async_tree_memoization_tg       | 196 ms                                                                 | 190 ms: 1.03x faster                                                          |
| deepcopy_reduce                 | 1.67 us                                                                | 1.62 us: 1.03x faster                                                         |
| shortest_path                   | 341 ms                                                                 | 331 ms: 1.03x faster                                                          |
| async_tree_eager_io_tg          | 384 ms                                                                 | 373 ms: 1.03x faster                                                          |
| xml_etree_generate              | 56.5 ms                                                                | 54.8 ms: 1.03x faster                                                         |
| sympy_str                       | 146 ms                                                                 | 142 ms: 1.03x faster                                                          |
| mako                            | 7.85 ms                                                                | 7.62 ms: 1.03x faster                                                         |
| sqlglot_v2_normalize            | 68.9 ms                                                                | 66.9 ms: 1.03x faster                                                         |
| bpe_tokeniser                   | 3.13 sec                                                               | 3.04 sec: 1.03x faster                                                        |
| subparsers                      | 12.7 ms                                                                | 12.3 ms: 1.03x faster                                                         |
| xml_etree_iterparse             | 73.9 ms                                                                | 71.8 ms: 1.03x faster                                                         |
| sqlglot_v2_optimize             | 33.5 ms                                                                | 32.6 ms: 1.03x faster                                                         |
| mdp                             | 785 ms                                                                 | 765 ms: 1.03x faster                                                          |
| spectral_norm                   | 70.7 ms                                                                | 68.9 ms: 1.03x faster                                                         |
| async_tree_eager_tg             | 135 ms                                                                 | 131 ms: 1.03x faster                                                          |
| async_tree_eager_memoization    | 141 ms                                                                 | 138 ms: 1.02x faster                                                          |
| dulwich_log                     | 25.0 ms                                                                | 24.5 ms: 1.02x faster                                                         |
| crypto_pyaes                    | 56.8 ms                                                                | 55.6 ms: 1.02x faster                                                         |
| many_optionals                  | 455 us                                                                 | 446 us: 1.02x faster                                                          |
| sympy_sum                       | 76.6 ms                                                                | 75.1 ms: 1.02x faster                                                         |
| sqlalchemy_declarative          | 61.0 ms                                                                | 59.9 ms: 1.02x faster                                                         |
| async_tree_eager_memoization_tg | 173 ms                                                                 | 170 ms: 1.02x faster                                                          |
| sympy_expand                    | 245 ms                                                                 | 241 ms: 1.02x faster                                                          |
| sphinx                          | 589 ms                                                                 | 579 ms: 1.02x faster                                                          |
| scimark_sparse_mat_mult         | 3.19 ms                                                                | 3.14 ms: 1.02x faster                                                         |
| create_gc_cycles                | 1.30 ms                                                                | 1.28 ms: 1.01x faster                                                         |
| bench_mp_pool                   | 60.1 ms                                                                | 59.3 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed         | 417 ms                                                                 | 412 ms: 1.01x faster                                                          |
| docutils                        | 1.45 sec                                                               | 1.43 sec: 1.01x faster                                                        |
| bench_thread_pool               | 501 us                                                                 | 495 us: 1.01x faster                                                          |
| gc_traversal                    | 3.13 ms                                                                | 3.10 ms: 1.01x faster                                                         |
| json_dumps                      | 7.51 ms                                                                | 7.48 ms: 1.00x faster                                                         |
| regex_v8                        | 15.6 ms                                                                | 15.5 ms: 1.00x faster                                                         |
| regex_effbot                    | 2.25 ms                                                                | 2.24 ms: 1.00x faster                                                         |
| asyncio_websockets              | 242 ms                                                                 | 242 ms: 1.00x faster                                                          |
| regex_dna                       | 141 ms                                                                 | 140 ms: 1.00x faster                                                          |
| pidigits                        | 283 ms                                                                 | 284 ms: 1.00x slower                                                          |
| sqlite_synth                    | 1.54 us                                                                | 1.55 us: 1.00x slower                                                         |
| async_tree_eager_cpu_io_mixed   | 358 ms                                                                 | 359 ms: 1.01x slower                                                          |
| coverage                        | 46.8 ms                                                                | 47.0 ms: 1.01x slower                                                         |
| async_generators                | 264 ms                                                                 | 266 ms: 1.01x slower                                                          |
| pathlib                         | 23.8 ms                                                                | 24.0 ms: 1.01x slower                                                         |
| telco                           | 4.66 ms                                                                | 4.70 ms: 1.01x slower                                                         |
| json                            | 3.04 ms                                                                | 3.09 ms: 1.02x slower                                                         |
| json_loads                      | 17.8 us                                                                | 18.1 us: 1.02x slower                                                         |
| Geometric mean                  | (ref)                                                                  | 1.04x faster                                                                  |

Benchmark hidden because not significant (5): pylint, k_core, xml_etree_parse, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.99x
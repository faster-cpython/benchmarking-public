# Results vs. base

- fork: faster-cpython
- ref: use_stackrefs
- machine: darwin-arm64
- commit hash: d270553
- commit date: 2025-02-20
- overall geometric mean: 1.017x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250219-darwin-arm64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                                 | 200 ms: 1.12x slower                                                      |
| html5lib       | 33.9 ms                                                                | 32.2 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250219-darwin-arm64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization           | 220 ms                                                                 | 211 ms: 1.04x faster                                                      |
| coroutines                       | 18.6 ms                                                                | 17.9 ms: 1.04x faster                                                     |
| async_tree_io_tg                 | 402 ms                                                                 | 388 ms: 1.04x faster                                                      |
| async_tree_none_tg               | 172 ms                                                                 | 166 ms: 1.03x faster                                                      |
| async_tree_eager_io              | 401 ms                                                                 | 389 ms: 1.03x faster                                                      |
| async_tree_io                    | 420 ms                                                                 | 408 ms: 1.03x faster                                                      |
| async_tree_eager                 | 71.2 ms                                                                | 69.2 ms: 1.03x faster                                                     |
| async_tree_none                  | 182 ms                                                                 | 177 ms: 1.03x faster                                                      |
| async_tree_eager_io_tg           | 411 ms                                                                 | 400 ms: 1.03x faster                                                      |
| async_tree_memoization_tg        | 213 ms                                                                 | 208 ms: 1.02x faster                                                      |
| async_tree_eager_memoization     | 154 ms                                                                 | 151 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed_tg       | 435 ms                                                                 | 426 ms: 1.02x faster                                                      |
| async_tree_eager_memoization_tg  | 193 ms                                                                 | 189 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed          | 434 ms                                                                 | 429 ms: 1.01x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 369 ms                                                                 | 367 ms: 1.00x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 404 ms                                                                 | 407 ms: 1.01x slower                                                      |
| async_generators                 | 266 ms                                                                 | 270 ms: 1.01x slower                                                      |
| Geometric mean                   | (ref)                                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (2): async_tree_eager_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250219-darwin-arm64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 92.0 ms                                                                | 80.7 ms: 1.14x faster                                                     |
| float          | 54.4 ms                                                                | 53.2 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.05x faster                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250219-darwin-arm64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 77.5 ms                                                                | 74.4 ms: 1.04x faster                                                     |
| regex_v8       | 16.8 ms                                                                | 16.9 ms: 1.01x slower                                                     |
| regex_dna      | 140 ms                                                                 | 141 ms: 1.01x slower                                                      |
| regex_effbot   | 2.27 ms                                                                | 2.30 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250219-darwin-arm64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.44 sec                                                               | 1.39 sec: 1.03x faster                                                    |
| pickle_pure_python   | 231 us                                                                 | 225 us: 1.03x faster                                                      |
| xml_etree_process    | 42.9 ms                                                                | 41.8 ms: 1.03x faster                                                     |
| xml_etree_generate   | 58.3 ms                                                                | 57.4 ms: 1.02x faster                                                     |
| xml_etree_iterparse  | 74.7 ms                                                                | 73.7 ms: 1.01x faster                                                     |
| json_dumps           | 7.58 ms                                                                | 7.49 ms: 1.01x faster                                                     |
| unpickle_pure_python | 169 us                                                                 | 167 us: 1.01x faster                                                      |
| xml_etree_parse      | 99.4 ms                                                                | 102 ms: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250219-darwin-arm64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 12.6 ms                                                                | 12.3 ms: 1.02x faster                                                     |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250219-darwin-arm64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 34.0 ms                                                                | 32.2 ms: 1.06x faster                                                     |
| genshi_text     | 16.4 ms                                                                | 15.5 ms: 1.05x faster                                                     |
| django_template | 24.2 ms                                                                | 23.0 ms: 1.05x faster                                                     |
| mako            | 7.93 ms                                                                | 7.97 ms: 1.00x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.04x faster                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20250219-darwin-arm64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| generators                       | 29.0 ms                                                                | 25.0 ms: 1.16x faster                                                     |
| nbody                            | 92.0 ms                                                                | 80.7 ms: 1.14x faster                                                     |
| raytrace                         | 212 ms                                                                 | 194 ms: 1.10x faster                                                      |
| scimark_sor                      | 95.1 ms                                                                | 89.0 ms: 1.07x faster                                                     |
| sqlglot_transpile                | 1.10 ms                                                                | 1.04 ms: 1.06x faster                                                     |
| hexiom                           | 5.26 ms                                                                | 4.97 ms: 1.06x faster                                                     |
| scimark_monte_carlo              | 49.9 ms                                                                | 47.2 ms: 1.06x faster                                                     |
| genshi_xml                       | 34.0 ms                                                                | 32.2 ms: 1.06x faster                                                     |
| genshi_text                      | 16.4 ms                                                                | 15.5 ms: 1.05x faster                                                     |
| html5lib                         | 33.9 ms                                                                | 32.2 ms: 1.05x faster                                                     |
| django_template                  | 24.2 ms                                                                | 23.0 ms: 1.05x faster                                                     |
| sqlglot_normalize                | 199 ms                                                                 | 190 ms: 1.05x faster                                                      |
| deltablue                        | 2.79 ms                                                                | 2.67 ms: 1.04x faster                                                     |
| regex_compile                    | 77.5 ms                                                                | 74.4 ms: 1.04x faster                                                     |
| async_tree_memoization           | 220 ms                                                                 | 211 ms: 1.04x faster                                                      |
| pprint_safe_repr                 | 526 ms                                                                 | 506 ms: 1.04x faster                                                      |
| pprint_pformat                   | 1.06 sec                                                               | 1.02 sec: 1.04x faster                                                    |
| coroutines                       | 18.6 ms                                                                | 17.9 ms: 1.04x faster                                                     |
| logging_silent                   | 73.2 ns                                                                | 70.6 ns: 1.04x faster                                                     |
| sqlglot_parse                    | 895 us                                                                 | 864 us: 1.04x faster                                                      |
| async_tree_io_tg                 | 402 ms                                                                 | 388 ms: 1.04x faster                                                      |
| sympy_expand                     | 258 ms                                                                 | 250 ms: 1.04x faster                                                      |
| async_tree_none_tg               | 172 ms                                                                 | 166 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult          | 3.19 ms                                                                | 3.09 ms: 1.03x faster                                                     |
| async_tree_eager_io              | 401 ms                                                                 | 389 ms: 1.03x faster                                                      |
| sqlglot_optimize                 | 35.9 ms                                                                | 34.8 ms: 1.03x faster                                                     |
| tomli_loads                      | 1.44 sec                                                               | 1.39 sec: 1.03x faster                                                    |
| logging_simple                   | 3.70 us                                                                | 3.59 us: 1.03x faster                                                     |
| async_tree_io                    | 420 ms                                                                 | 408 ms: 1.03x faster                                                      |
| pickle_pure_python               | 231 us                                                                 | 225 us: 1.03x faster                                                      |
| typing_runtime_protocols         | 104 us                                                                 | 101 us: 1.03x faster                                                      |
| async_tree_eager                 | 71.2 ms                                                                | 69.2 ms: 1.03x faster                                                     |
| bench_thread_pool                | 522 us                                                                 | 507 us: 1.03x faster                                                      |
| mdp                              | 1.56 sec                                                               | 1.52 sec: 1.03x faster                                                    |
| async_tree_none                  | 182 ms                                                                 | 177 ms: 1.03x faster                                                      |
| xml_etree_process                | 42.9 ms                                                                | 41.8 ms: 1.03x faster                                                     |
| deepcopy_reduce                  | 1.76 us                                                                | 1.72 us: 1.03x faster                                                     |
| async_tree_eager_io_tg           | 411 ms                                                                 | 400 ms: 1.03x faster                                                      |
| scimark_lu                       | 83.2 ms                                                                | 81.1 ms: 1.03x faster                                                     |
| logging_format                   | 4.01 us                                                                | 3.91 us: 1.03x faster                                                     |
| sympy_str                        | 154 ms                                                                 | 150 ms: 1.03x faster                                                      |
| subparsers                       | 13.1 ms                                                                | 12.8 ms: 1.02x faster                                                     |
| python_startup_no_site           | 12.6 ms                                                                | 12.3 ms: 1.02x faster                                                     |
| async_tree_memoization_tg        | 213 ms                                                                 | 208 ms: 1.02x faster                                                      |
| float                            | 54.4 ms                                                                | 53.2 ms: 1.02x faster                                                     |
| async_tree_eager_memoization     | 154 ms                                                                 | 151 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed_tg       | 435 ms                                                                 | 426 ms: 1.02x faster                                                      |
| deepcopy_memo                    | 21.0 us                                                                | 20.6 us: 1.02x faster                                                     |
| async_tree_eager_memoization_tg  | 193 ms                                                                 | 189 ms: 1.02x faster                                                      |
| richards                         | 38.5 ms                                                                | 37.7 ms: 1.02x faster                                                     |
| dulwich_log                      | 29.5 ms                                                                | 29.0 ms: 1.02x faster                                                     |
| go                               | 94.8 ms                                                                | 92.9 ms: 1.02x faster                                                     |
| deepcopy                         | 169 us                                                                 | 165 us: 1.02x faster                                                      |
| coverage                         | 48.0 ms                                                                | 47.3 ms: 1.02x faster                                                     |
| scimark_fft                      | 198 ms                                                                 | 195 ms: 1.02x faster                                                      |
| xml_etree_generate               | 58.3 ms                                                                | 57.4 ms: 1.02x faster                                                     |
| sqlalchemy_imperative            | 7.05 ms                                                                | 6.94 ms: 1.02x faster                                                     |
| sympy_integrate                  | 12.3 ms                                                                | 12.1 ms: 1.01x faster                                                     |
| sympy_sum                        | 79.2 ms                                                                | 78.1 ms: 1.01x faster                                                     |
| xml_etree_iterparse              | 74.7 ms                                                                | 73.7 ms: 1.01x faster                                                     |
| shortest_path                    | 351 ms                                                                 | 346 ms: 1.01x faster                                                      |
| pathlib                          | 23.8 ms                                                                | 23.5 ms: 1.01x faster                                                     |
| pycparser                        | 710 ms                                                                 | 701 ms: 1.01x faster                                                      |
| json_dumps                       | 7.58 ms                                                                | 7.49 ms: 1.01x faster                                                     |
| async_tree_cpu_io_mixed          | 434 ms                                                                 | 429 ms: 1.01x faster                                                      |
| sqlite_synth                     | 1.57 us                                                                | 1.55 us: 1.01x faster                                                     |
| unpickle_pure_python             | 169 us                                                                 | 167 us: 1.01x faster                                                      |
| thrift                           | 463 us                                                                 | 459 us: 1.01x faster                                                      |
| meteor_contest                   | 78.1 ms                                                                | 77.5 ms: 1.01x faster                                                     |
| telco                            | 4.75 ms                                                                | 4.72 ms: 1.01x faster                                                     |
| richards_super                   | 42.8 ms                                                                | 42.5 ms: 1.01x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 369 ms                                                                 | 367 ms: 1.00x faster                                                      |
| sqlalchemy_declarative           | 62.0 ms                                                                | 61.8 ms: 1.00x faster                                                     |
| chaos                            | 44.4 ms                                                                | 44.2 ms: 1.00x faster                                                     |
| comprehensions                   | 13.0 us                                                                | 13.0 us: 1.00x slower                                                     |
| mako                             | 7.93 ms                                                                | 7.97 ms: 1.00x slower                                                     |
| pyflate                          | 352 ms                                                                 | 354 ms: 1.01x slower                                                      |
| regex_v8                         | 16.8 ms                                                                | 16.9 ms: 1.01x slower                                                     |
| async_tree_eager_cpu_io_mixed_tg | 404 ms                                                                 | 407 ms: 1.01x slower                                                      |
| regex_dna                        | 140 ms                                                                 | 141 ms: 1.01x slower                                                      |
| regex_effbot                     | 2.27 ms                                                                | 2.30 ms: 1.01x slower                                                     |
| async_generators                 | 266 ms                                                                 | 270 ms: 1.01x slower                                                      |
| json                             | 3.02 ms                                                                | 3.08 ms: 1.02x slower                                                     |
| spectral_norm                    | 78.2 ms                                                                | 80.2 ms: 1.03x slower                                                     |
| xml_etree_parse                  | 99.4 ms                                                                | 102 ms: 1.03x slower                                                      |
| fannkuch                         | 297 ms                                                                 | 306 ms: 1.03x slower                                                      |
| k_core                           | 1.54 sec                                                               | 1.59 sec: 1.03x slower                                                    |
| bpe_tokeniser                    | 3.22 sec                                                               | 3.32 sec: 1.03x slower                                                    |
| crypto_pyaes                     | 59.0 ms                                                                | 61.7 ms: 1.05x slower                                                     |
| nqueens                          | 65.3 ms                                                                | 70.1 ms: 1.07x slower                                                     |
| 2to3                             | 179 ms                                                                 | 200 ms: 1.12x slower                                                      |
| Geometric mean                   | (ref)                                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (14): async_tree_eager_tg, connected_components, many_optionals, pylint, gc_traversal, docutils, python_startup, pidigits, sphinx, dask, asyncio_websockets, create_gc_cycles, json_loads, bench_mp_pool

- Geometric mean (including insignificant results): 1.017x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x
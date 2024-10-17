# Results vs. base

- fork: savannahostrowski
- ref: remove_ghccc
- machine: darwin-arm64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.00x faster
- HPT reliability: 78.79%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 183 ms                                                                 | 182 ms: 1.01x faster                                                      |
| html5lib       | 33.9 ms                                                                | 33.8 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (3): docutils, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg                 | 610 ms                                                                 | 613 ms: 1.00x slower                                                      |
| async_tree_eager_cpu_io_mixed_tg | 336 ms                                                                 | 337 ms: 1.01x slower                                                      |
| async_tree_eager_tg              | 42.9 ms                                                                | 43.3 ms: 1.01x slower                                                     |
| async_tree_none                  | 197 ms                                                                 | 200 ms: 1.01x slower                                                      |
| async_generators                 | 291 ms                                                                 | 295 ms: 1.01x slower                                                      |
| async_tree_eager                 | 62.8 ms                                                                | 63.8 ms: 1.02x slower                                                     |
| Geometric mean                   | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (15): asyncio_websockets, async_tree_eager_io_tg, asyncio_tcp, asyncio_tcp_ssl, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, async_tree_memoization_tg, async_tree_eager_io, coroutines, async_tree_eager_memoization_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 65.3 ms                                                                | 63.2 ms: 1.03x faster                                                     |
| float          | 48.3 ms                                                                | 47.7 ms: 1.01x faster                                                     |
| pidigits       | 284 ms                                                                 | 283 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 75.0 ms                                                                | 74.0 ms: 1.01x faster                                                     |
| regex_effbot   | 2.60 ms                                                                | 2.62 ms: 1.01x slower                                                     |
| regex_dna      | 148 ms                                                                 | 149 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|---------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads         | 1.24 sec                                                               | 1.23 sec: 1.01x faster                                                    |
| xml_etree_generate  | 50.3 ms                                                                | 49.8 ms: 1.01x faster                                                     |
| xml_etree_process   | 34.5 ms                                                                | 34.3 ms: 1.01x faster                                                     |
| unpickle            | 9.08 us                                                                | 9.04 us: 1.00x faster                                                     |
| pickle_pure_python  | 178 us                                                                 | 179 us: 1.00x slower                                                      |
| xml_etree_parse     | 106 ms                                                                 | 107 ms: 1.01x slower                                                      |
| pickle_dict         | 18.1 us                                                                | 18.3 us: 1.01x slower                                                     |
| pickle              | 7.30 us                                                                | 7.37 us: 1.01x slower                                                     |
| xml_etree_iterparse | 72.5 ms                                                                | 73.2 ms: 1.01x slower                                                     |
| pickle_list         | 2.94 us                                                                | 2.97 us: 1.01x slower                                                     |
| json_dumps          | 7.12 ms                                                                | 7.23 ms: 1.02x slower                                                     |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (3): unpickle_list, unpickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                                | 19.0 ms: 1.01x slower                                                     |
| python_startup_no_site | 14.6 ms                                                                | 14.7 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 42.7 ms                                                                | 38.4 ms: 1.11x faster                                                     |
| mako            | 6.47 ms                                                                | 6.30 ms: 1.03x faster                                                     |
| genshi_text     | 16.6 ms                                                                | 16.3 ms: 1.02x faster                                                     |
| django_template | 22.6 ms                                                                | 22.5 ms: 1.01x faster                                                     |
| Geometric mean  | (ref)                                                                  | 1.04x faster                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpack_sequence                  | 76.0 ns                                                                | 62.2 ns: 1.22x faster                                                     |
| genshi_xml                       | 42.7 ms                                                                | 38.4 ms: 1.11x faster                                                     |
| pprint_safe_repr                 | 497 ms                                                                 | 470 ms: 1.06x faster                                                      |
| scimark_sor                      | 86.2 ms                                                                | 82.4 ms: 1.05x faster                                                     |
| pprint_pformat                   | 998 ms                                                                 | 961 ms: 1.04x faster                                                      |
| nbody                            | 65.3 ms                                                                | 63.2 ms: 1.03x faster                                                     |
| sqlglot_parse                    | 875 us                                                                 | 849 us: 1.03x faster                                                      |
| scimark_fft                      | 190 ms                                                                 | 185 ms: 1.03x faster                                                      |
| meteor_contest                   | 75.2 ms                                                                | 73.1 ms: 1.03x faster                                                     |
| mako                             | 6.47 ms                                                                | 6.30 ms: 1.03x faster                                                     |
| pyflate                          | 326 ms                                                                 | 318 ms: 1.03x faster                                                      |
| bpe_tokeniser                    | 3.04 sec                                                               | 2.98 sec: 1.02x faster                                                    |
| genshi_text                      | 16.6 ms                                                                | 16.3 ms: 1.02x faster                                                     |
| spectral_norm                    | 69.3 ms                                                                | 68.1 ms: 1.02x faster                                                     |
| sqlglot_transpile                | 1.06 ms                                                                | 1.04 ms: 1.02x faster                                                     |
| scimark_monte_carlo              | 45.6 ms                                                                | 45.0 ms: 1.01x faster                                                     |
| crypto_pyaes                     | 53.9 ms                                                                | 53.1 ms: 1.01x faster                                                     |
| regex_compile                    | 75.0 ms                                                                | 74.0 ms: 1.01x faster                                                     |
| logging_simple                   | 3.13 us                                                                | 3.09 us: 1.01x faster                                                     |
| go                               | 98.0 ms                                                                | 96.8 ms: 1.01x faster                                                     |
| float                            | 48.3 ms                                                                | 47.7 ms: 1.01x faster                                                     |
| tomli_loads                      | 1.24 sec                                                               | 1.23 sec: 1.01x faster                                                    |
| xml_etree_generate               | 50.3 ms                                                                | 49.8 ms: 1.01x faster                                                     |
| logging_format                   | 3.40 us                                                                | 3.37 us: 1.01x faster                                                     |
| scimark_sparse_mat_mult          | 3.14 ms                                                                | 3.11 ms: 1.01x faster                                                     |
| pycparser                        | 678 ms                                                                 | 673 ms: 1.01x faster                                                      |
| dulwich_log                      | 28.7 ms                                                                | 28.5 ms: 1.01x faster                                                     |
| 2to3                             | 183 ms                                                                 | 182 ms: 1.01x faster                                                      |
| sympy_sum                        | 79.7 ms                                                                | 79.2 ms: 1.01x faster                                                     |
| django_template                  | 22.6 ms                                                                | 22.5 ms: 1.01x faster                                                     |
| xml_etree_process                | 34.5 ms                                                                | 34.3 ms: 1.01x faster                                                     |
| comprehensions                   | 13.0 us                                                                | 13.0 us: 1.00x faster                                                     |
| deltablue                        | 2.43 ms                                                                | 2.42 ms: 1.00x faster                                                     |
| gc_traversal                     | 2.96 ms                                                                | 2.95 ms: 1.00x faster                                                     |
| unpickle                         | 9.08 us                                                                | 9.04 us: 1.00x faster                                                     |
| html5lib                         | 33.9 ms                                                                | 33.8 ms: 1.00x faster                                                     |
| sympy_integrate                  | 12.5 ms                                                                | 12.5 ms: 1.00x faster                                                     |
| pidigits                         | 284 ms                                                                 | 283 ms: 1.00x faster                                                      |
| sqlglot_optimize                 | 36.8 ms                                                                | 36.9 ms: 1.00x slower                                                     |
| fannkuch                         | 264 ms                                                                 | 265 ms: 1.00x slower                                                      |
| telco                            | 4.54 ms                                                                | 4.55 ms: 1.00x slower                                                     |
| coverage                         | 43.9 ms                                                                | 44.1 ms: 1.00x slower                                                     |
| bench_thread_pool                | 472 us                                                                 | 474 us: 1.00x slower                                                      |
| pickle_pure_python               | 178 us                                                                 | 179 us: 1.00x slower                                                      |
| async_tree_io_tg                 | 610 ms                                                                 | 613 ms: 1.00x slower                                                      |
| async_tree_eager_cpu_io_mixed_tg | 336 ms                                                                 | 337 ms: 1.01x slower                                                      |
| hexiom                           | 4.92 ms                                                                | 4.95 ms: 1.01x slower                                                     |
| create_gc_cycles                 | 1.31 ms                                                                | 1.32 ms: 1.01x slower                                                     |
| regex_effbot                     | 2.60 ms                                                                | 2.62 ms: 1.01x slower                                                     |
| python_startup                   | 18.9 ms                                                                | 19.0 ms: 1.01x slower                                                     |
| xml_etree_parse                  | 106 ms                                                                 | 107 ms: 1.01x slower                                                      |
| python_startup_no_site           | 14.6 ms                                                                | 14.7 ms: 1.01x slower                                                     |
| pickle_dict                      | 18.1 us                                                                | 18.3 us: 1.01x slower                                                     |
| raytrace                         | 167 ms                                                                 | 169 ms: 1.01x slower                                                      |
| pickle                           | 7.30 us                                                                | 7.37 us: 1.01x slower                                                     |
| pathlib                          | 22.3 ms                                                                | 22.5 ms: 1.01x slower                                                     |
| xml_etree_iterparse              | 72.5 ms                                                                | 73.2 ms: 1.01x slower                                                     |
| pickle_list                      | 2.94 us                                                                | 2.97 us: 1.01x slower                                                     |
| async_tree_eager_tg              | 42.9 ms                                                                | 43.3 ms: 1.01x slower                                                     |
| logging_silent                   | 69.9 ns                                                                | 70.7 ns: 1.01x slower                                                     |
| chaos                            | 41.4 ms                                                                | 41.8 ms: 1.01x slower                                                     |
| regex_dna                        | 148 ms                                                                 | 149 ms: 1.01x slower                                                      |
| async_tree_none                  | 197 ms                                                                 | 200 ms: 1.01x slower                                                      |
| async_generators                 | 291 ms                                                                 | 295 ms: 1.01x slower                                                      |
| sympy_expand                     | 245 ms                                                                 | 249 ms: 1.02x slower                                                      |
| json_dumps                       | 7.12 ms                                                                | 7.23 ms: 1.02x slower                                                     |
| async_tree_eager                 | 62.8 ms                                                                | 63.8 ms: 1.02x slower                                                     |
| deepcopy_reduce                  | 1.50 us                                                                | 1.53 us: 1.02x slower                                                     |
| mdp                              | 1.54 sec                                                               | 1.56 sec: 1.02x slower                                                    |
| thrift                           | 418 us                                                                 | 426 us: 1.02x slower                                                      |
| sqlglot_normalize                | 182 ms                                                                 | 186 ms: 1.02x slower                                                      |
| deepcopy                         | 152 us                                                                 | 155 us: 1.02x slower                                                      |
| scimark_lu                       | 64.4 ms                                                                | 65.7 ms: 1.02x slower                                                     |
| nqueens                          | 58.4 ms                                                                | 59.9 ms: 1.03x slower                                                     |
| richards_super                   | 37.1 ms                                                                | 38.3 ms: 1.03x slower                                                     |
| richards                         | 33.4 ms                                                                | 34.5 ms: 1.03x slower                                                     |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (30): pylint, unpickle_list, docutils, unpickle_pure_python, generators, asyncio_websockets, bench_mp_pool, sympy_str, deepcopy_memo, json, regex_v8, json_loads, async_tree_eager_io_tg, sqlite_synth, sphinx, asyncio_tcp, asyncio_tcp_ssl, typing_runtime_protocols, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, async_tree_memoization_tg, async_tree_eager_io, coroutines, async_tree_eager_memoization_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_eager_memoization, tornado_http

# HPT report

- Reliability score: 78.79% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x
# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: darwin-arm64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.00x faster
- HPT reliability: 98.77%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.50x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 163 ms: 1.01x slower                                                            |
| docutils       | 1.44 sec                                                   | 1.48 sec: 1.03x slower                                                          |
| html5lib       | 31.2 ms                                                    | 31.6 ms: 1.02x slower                                                           |
| tornado_http   | 66.7 ms                                                    | 78.8 ms: 1.18x slower                                                           |
| Geometric mean | (ref)                                                      | 1.06x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 640 ms: 1.20x faster                                                            |
| async_tree_eager_io_tg           | 768 ms                                                     | 676 ms: 1.14x faster                                                            |
| async_tree_io_tg                 | 565 ms                                                     | 507 ms: 1.11x faster                                                            |
| async_tree_none_tg               | 198 ms                                                     | 184 ms: 1.08x faster                                                            |
| async_tree_memoization           | 260 ms                                                     | 242 ms: 1.07x faster                                                            |
| async_tree_none                  | 209 ms                                                     | 196 ms: 1.07x faster                                                            |
| async_tree_memoization_tg        | 240 ms                                                     | 229 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 453 ms: 1.03x faster                                                            |
| async_tree_io                    | 563 ms                                                     | 547 ms: 1.03x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 362 ms: 1.01x slower                                                            |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 337 ms: 1.02x slower                                                            |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.2 ms: 1.02x slower                                                           |
| async_tree_eager                 | 60.3 ms                                                    | 62.8 ms: 1.04x slower                                                           |
| Geometric mean                   | (ref)                                                      | 1.04x faster                                                                    |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 48.4 ms: 1.00x faster                                                           |
| nbody          | 59.6 ms                                                    | 59.4 ms: 1.00x faster                                                           |
| pidigits       | 282 ms                                                     | 282 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                      | 1.00x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                           |
| regex_effbot   | 2.58 ms                                                    | 2.50 ms: 1.03x faster                                                           |
| regex_dna      | 149 ms                                                     | 146 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_generate   | 52.7 ms                                                    | 53.4 ms: 1.01x slower                                                           |
| unpickle_pure_python | 141 us                                                     | 144 us: 1.02x slower                                                            |
| tomli_loads          | 1.47 sec                                                   | 1.50 sec: 1.02x slower                                                          |
| json_loads           | 16.8 us                                                    | 17.3 us: 1.03x slower                                                           |
| xml_etree_parse      | 106 ms                                                     | 109 ms: 1.03x slower                                                            |
| pickle_pure_python   | 179 us                                                     | 184 us: 1.03x slower                                                            |
| xml_etree_process    | 37.1 ms                                                    | 38.3 ms: 1.03x slower                                                           |
| xml_etree_iterparse  | 71.5 ms                                                    | 74.3 ms: 1.04x slower                                                           |
| json_dumps           | 6.23 ms                                                    | 6.52 ms: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                      | 1.03x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 16.4 ms: 1.08x slower                                                           |
| python_startup_no_site | 12.3 ms                                                    | 13.4 ms: 1.09x slower                                                           |
| Geometric mean         | (ref)                                                      | 1.09x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 13.9 ms                                                    | 14.2 ms: 1.02x slower                                                           |
| django_template | 19.4 ms                                                    | 19.8 ms: 1.02x slower                                                           |
| mako            | 6.99 ms                                                    | 7.16 ms: 1.03x slower                                                           |
| genshi_xml      | 29.9 ms                                                    | 30.7 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 146 us: 1.40x faster                                                            |
| deepcopy_memo                    | 22.6 us                                                    | 17.1 us: 1.32x faster                                                           |
| async_tree_eager_io              | 766 ms                                                     | 640 ms: 1.20x faster                                                            |
| deepcopy_reduce                  | 1.82 us                                                    | 1.52 us: 1.20x faster                                                           |
| async_tree_eager_io_tg           | 768 ms                                                     | 676 ms: 1.14x faster                                                            |
| async_tree_io_tg                 | 565 ms                                                     | 507 ms: 1.11x faster                                                            |
| generators                       | 22.9 ms                                                    | 20.6 ms: 1.11x faster                                                           |
| async_tree_none_tg               | 198 ms                                                     | 184 ms: 1.08x faster                                                            |
| async_tree_memoization           | 260 ms                                                     | 242 ms: 1.07x faster                                                            |
| mdp                              | 1.53 sec                                                   | 1.44 sec: 1.07x faster                                                          |
| async_tree_none                  | 209 ms                                                     | 196 ms: 1.07x faster                                                            |
| async_tree_memoization_tg        | 240 ms                                                     | 229 ms: 1.04x faster                                                            |
| regex_v8                         | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                           |
| go                               | 101 ms                                                     | 97.2 ms: 1.03x faster                                                           |
| regex_effbot                     | 2.58 ms                                                    | 2.50 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 453 ms: 1.03x faster                                                            |
| async_tree_io                    | 563 ms                                                     | 547 ms: 1.03x faster                                                            |
| dulwich_log                      | 27.6 ms                                                    | 26.9 ms: 1.02x faster                                                           |
| regex_dna                        | 149 ms                                                     | 146 ms: 1.02x faster                                                            |
| richards_super                   | 35.2 ms                                                    | 34.6 ms: 1.02x faster                                                           |
| thrift                           | 435 us                                                     | 430 us: 1.01x faster                                                            |
| scimark_sor                      | 94.9 ms                                                    | 93.7 ms: 1.01x faster                                                           |
| richards                         | 31.8 ms                                                    | 31.4 ms: 1.01x faster                                                           |
| create_gc_cycles                 | 897 us                                                     | 886 us: 1.01x faster                                                            |
| deltablue                        | 2.14 ms                                                    | 2.12 ms: 1.01x faster                                                           |
| async_generators                 | 281 ms                                                     | 279 ms: 1.01x faster                                                            |
| float                            | 48.6 ms                                                    | 48.4 ms: 1.00x faster                                                           |
| nbody                            | 59.6 ms                                                    | 59.4 ms: 1.00x faster                                                           |
| coverage                         | 45.0 ms                                                    | 44.9 ms: 1.00x faster                                                           |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                            |
| pidigits                         | 282 ms                                                     | 282 ms: 1.00x faster                                                            |
| spectral_norm                    | 66.4 ms                                                    | 66.5 ms: 1.00x slower                                                           |
| pyflate                          | 321 ms                                                     | 322 ms: 1.00x slower                                                            |
| bench_thread_pool                | 447 us                                                     | 449 us: 1.00x slower                                                            |
| logging_silent                   | 60.1 ns                                                    | 60.4 ns: 1.00x slower                                                           |
| logging_simple                   | 3.04 us                                                    | 3.06 us: 1.00x slower                                                           |
| scimark_lu                       | 66.9 ms                                                    | 67.5 ms: 1.01x slower                                                           |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.80 ms: 1.01x slower                                                           |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 362 ms: 1.01x slower                                                            |
| pycparser                        | 632 ms                                                     | 639 ms: 1.01x slower                                                            |
| sympy_integrate                  | 10.3 ms                                                    | 10.5 ms: 1.01x slower                                                           |
| xml_etree_generate               | 52.7 ms                                                    | 53.4 ms: 1.01x slower                                                           |
| raytrace                         | 147 ms                                                     | 149 ms: 1.01x slower                                                            |
| coroutines                       | 15.8 ms                                                    | 16.1 ms: 1.01x slower                                                           |
| 2to3                             | 161 ms                                                     | 163 ms: 1.01x slower                                                            |
| telco                            | 4.60 ms                                                    | 4.67 ms: 1.01x slower                                                           |
| html5lib                         | 31.2 ms                                                    | 31.6 ms: 1.02x slower                                                           |
| sqlglot_parse                    | 732 us                                                     | 744 us: 1.02x slower                                                            |
| nqueens                          | 52.2 ms                                                    | 53.1 ms: 1.02x slower                                                           |
| logging_format                   | 3.31 us                                                    | 3.37 us: 1.02x slower                                                           |
| sqlglot_transpile                | 891 us                                                     | 907 us: 1.02x slower                                                            |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.11 sec: 1.02x slower                                                          |
| unpickle_pure_python             | 141 us                                                     | 144 us: 1.02x slower                                                            |
| genshi_text                      | 13.9 ms                                                    | 14.2 ms: 1.02x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 337 ms: 1.02x slower                                                            |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.2 ms: 1.02x slower                                                           |
| django_template                  | 19.4 ms                                                    | 19.8 ms: 1.02x slower                                                           |
| meteor_contest                   | 70.3 ms                                                    | 71.8 ms: 1.02x slower                                                           |
| tomli_loads                      | 1.47 sec                                                   | 1.50 sec: 1.02x slower                                                          |
| pprint_safe_repr                 | 465 ms                                                     | 475 ms: 1.02x slower                                                            |
| sympy_sum                        | 69.2 ms                                                    | 70.8 ms: 1.02x slower                                                           |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.5 ms: 1.02x slower                                                           |
| pprint_pformat                   | 947 ms                                                     | 969 ms: 1.02x slower                                                            |
| sympy_expand                     | 226 ms                                                     | 231 ms: 1.02x slower                                                            |
| mako                             | 6.99 ms                                                    | 7.16 ms: 1.03x slower                                                           |
| genshi_xml                       | 29.9 ms                                                    | 30.7 ms: 1.03x slower                                                           |
| sympy_str                        | 131 ms                                                     | 135 ms: 1.03x slower                                                            |
| json                             | 2.93 ms                                                    | 3.01 ms: 1.03x slower                                                           |
| json_loads                       | 16.8 us                                                    | 17.3 us: 1.03x slower                                                           |
| xml_etree_parse                  | 106 ms                                                     | 109 ms: 1.03x slower                                                            |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.8 ms: 1.03x slower                                                           |
| scimark_fft                      | 181 ms                                                     | 186 ms: 1.03x slower                                                            |
| bench_mp_pool                    | 47.2 ms                                                    | 48.6 ms: 1.03x slower                                                           |
| docutils                         | 1.44 sec                                                   | 1.48 sec: 1.03x slower                                                          |
| pickle_pure_python               | 179 us                                                     | 184 us: 1.03x slower                                                            |
| crypto_pyaes                     | 49.5 ms                                                    | 51.1 ms: 1.03x slower                                                           |
| xml_etree_process                | 37.1 ms                                                    | 38.3 ms: 1.03x slower                                                           |
| sqlglot_normalize                | 166 ms                                                     | 172 ms: 1.04x slower                                                            |
| xml_etree_iterparse              | 71.5 ms                                                    | 74.3 ms: 1.04x slower                                                           |
| async_tree_eager                 | 60.3 ms                                                    | 62.8 ms: 1.04x slower                                                           |
| json_dumps                       | 6.23 ms                                                    | 6.52 ms: 1.05x slower                                                           |
| fannkuch                         | 248 ms                                                     | 262 ms: 1.06x slower                                                            |
| chaos                            | 34.0 ms                                                    | 36.2 ms: 1.06x slower                                                           |
| python_startup                   | 15.2 ms                                                    | 16.4 ms: 1.08x slower                                                           |
| python_startup_no_site           | 12.3 ms                                                    | 13.4 ms: 1.09x slower                                                           |
| comprehensions                   | 10.2 us                                                    | 11.0 us: 1.09x slower                                                           |
| typing_runtime_protocols         | 87.6 us                                                    | 95.6 us: 1.09x slower                                                           |
| tornado_http                     | 66.7 ms                                                    | 78.8 ms: 1.18x slower                                                           |
| Geometric mean                   | (ref)                                                      | 1.00x faster                                                                    |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed_tg, pathlib, hexiom, regex_compile, gc_traversal, async_tree_eager_memoization_tg, async_tree_eager_memoization, asyncio_tcp_ssl, asyncio_tcp, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 98.77% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.50x
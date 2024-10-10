# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: more_robust_immortal
- machine: darwin-arm64
- commit hash: 94f8fd0
- commit date: 2024-10-10
- overall geometric mean: 1.01x faster
- HPT reliability: 97.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.65x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 160 ms: 1.01x faster                                                            |
| docutils       | 1.44 sec                                                   | 1.40 sec: 1.03x faster                                                          |
| html5lib       | 31.2 ms                                                    | 32.0 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                      | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 675 ms: 1.14x faster                                                            |
| async_tree_none                  | 209 ms                                                     | 192 ms: 1.09x faster                                                            |
| async_tree_eager_io_tg           | 768 ms                                                     | 712 ms: 1.08x faster                                                            |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 459 ms: 1.02x faster                                                            |
| async_tree_eager                 | 60.3 ms                                                    | 59.7 ms: 1.01x faster                                                           |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.7 ms: 1.01x slower                                                           |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                            |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                            |
| async_tree_io                    | 563 ms                                                     | 593 ms: 1.05x slower                                                            |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                                    |

Benchmark hidden because not significant (7): async_tree_memoization, async_tree_io_tg, async_tree_none_tg, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 283 ms: 1.00x slower                                                            |
| float          | 48.6 ms                                                    | 48.9 ms: 1.01x slower                                                           |
| nbody          | 59.6 ms                                                    | 65.4 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                      | 1.03x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 16.7 ms: 1.03x faster                                                           |
| regex_dna      | 149 ms                                                     | 148 ms: 1.01x faster                                                            |
| regex_compile  | 68.5 ms                                                    | 67.8 ms: 1.01x faster                                                           |
| regex_effbot   | 2.58 ms                                                    | 2.63 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle               | 7.48 us                                                    | 7.33 us: 1.02x faster                                                           |
| xml_etree_generate   | 52.7 ms                                                    | 52.1 ms: 1.01x faster                                                           |
| pickle_dict          | 18.3 us                                                    | 18.1 us: 1.01x faster                                                           |
| json_loads           | 16.8 us                                                    | 16.7 us: 1.01x faster                                                           |
| unpickle_pure_python | 141 us                                                     | 142 us: 1.01x slower                                                            |
| xml_etree_process    | 37.1 ms                                                    | 37.4 ms: 1.01x slower                                                           |
| tomli_loads          | 1.47 sec                                                   | 1.49 sec: 1.02x slower                                                          |
| xml_etree_parse      | 106 ms                                                     | 108 ms: 1.02x slower                                                            |
| unpickle_list        | 2.88 us                                                    | 2.96 us: 1.03x slower                                                           |
| xml_etree_iterparse  | 71.5 ms                                                    | 73.4 ms: 1.03x slower                                                           |
| pickle_pure_python   | 179 us                                                     | 184 us: 1.03x slower                                                            |
| Geometric mean       | (ref)                                                      | 1.01x slower                                                                    |

Benchmark hidden because not significant (3): unpickle, json_dumps, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 17.0 ms: 1.12x slower                                                           |
| python_startup_no_site | 12.3 ms                                                    | 14.2 ms: 1.15x slower                                                           |
| Geometric mean         | (ref)                                                      | 1.14x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 13.9 ms                                                    | 13.7 ms: 1.01x faster                                                           |
| genshi_xml      | 29.9 ms                                                    | 29.8 ms: 1.01x faster                                                           |
| django_template | 19.4 ms                                                    | 19.9 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_websockets               | 409 ms                                                     | 241 ms: 1.69x faster                                                            |
| deepcopy                         | 204 us                                                     | 147 us: 1.39x faster                                                            |
| deepcopy_memo                    | 22.6 us                                                    | 17.1 us: 1.32x faster                                                           |
| go                               | 101 ms                                                     | 81.6 ms: 1.23x faster                                                           |
| deepcopy_reduce                  | 1.82 us                                                    | 1.52 us: 1.20x faster                                                           |
| async_tree_eager_io              | 766 ms                                                     | 675 ms: 1.14x faster                                                            |
| generators                       | 22.9 ms                                                    | 20.3 ms: 1.13x faster                                                           |
| async_tree_none                  | 209 ms                                                     | 192 ms: 1.09x faster                                                            |
| async_tree_eager_io_tg           | 768 ms                                                     | 712 ms: 1.08x faster                                                            |
| pathlib                          | 23.3 ms                                                    | 21.9 ms: 1.06x faster                                                           |
| mdp                              | 1.53 sec                                                   | 1.46 sec: 1.05x faster                                                          |
| thrift                           | 435 us                                                     | 416 us: 1.05x faster                                                            |
| regex_v8                         | 17.3 ms                                                    | 16.7 ms: 1.03x faster                                                           |
| docutils                         | 1.44 sec                                                   | 1.40 sec: 1.03x faster                                                          |
| coverage                         | 45.0 ms                                                    | 43.9 ms: 1.02x faster                                                           |
| richards_super                   | 35.2 ms                                                    | 34.4 ms: 1.02x faster                                                           |
| json                             | 2.93 ms                                                    | 2.87 ms: 1.02x faster                                                           |
| sqlite_synth                     | 1.55 us                                                    | 1.52 us: 1.02x faster                                                           |
| richards                         | 31.8 ms                                                    | 31.2 ms: 1.02x faster                                                           |
| pickle                           | 7.48 us                                                    | 7.33 us: 1.02x faster                                                           |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 459 ms: 1.02x faster                                                            |
| async_generators                 | 281 ms                                                     | 276 ms: 1.02x faster                                                            |
| pprint_safe_repr                 | 465 ms                                                     | 457 ms: 1.02x faster                                                            |
| genshi_text                      | 13.9 ms                                                    | 13.7 ms: 1.01x faster                                                           |
| xml_etree_generate               | 52.7 ms                                                    | 52.1 ms: 1.01x faster                                                           |
| pickle_dict                      | 18.3 us                                                    | 18.1 us: 1.01x faster                                                           |
| regex_dna                        | 149 ms                                                     | 148 ms: 1.01x faster                                                            |
| regex_compile                    | 68.5 ms                                                    | 67.8 ms: 1.01x faster                                                           |
| async_tree_eager                 | 60.3 ms                                                    | 59.7 ms: 1.01x faster                                                           |
| 2to3                             | 161 ms                                                     | 160 ms: 1.01x faster                                                            |
| json_loads                       | 16.8 us                                                    | 16.7 us: 1.01x faster                                                           |
| pprint_pformat                   | 947 ms                                                     | 940 ms: 1.01x faster                                                            |
| dulwich_log                      | 27.6 ms                                                    | 27.4 ms: 1.01x faster                                                           |
| genshi_xml                       | 29.9 ms                                                    | 29.8 ms: 1.01x faster                                                           |
| scimark_sor                      | 94.9 ms                                                    | 95.1 ms: 1.00x slower                                                           |
| sqlglot_normalize                | 166 ms                                                     | 166 ms: 1.00x slower                                                            |
| meteor_contest                   | 70.3 ms                                                    | 70.5 ms: 1.00x slower                                                           |
| logging_simple                   | 3.04 us                                                    | 3.05 us: 1.00x slower                                                           |
| pidigits                         | 282 ms                                                     | 283 ms: 1.00x slower                                                            |
| float                            | 48.6 ms                                                    | 48.9 ms: 1.01x slower                                                           |
| sqlglot_transpile                | 891 us                                                     | 896 us: 1.01x slower                                                            |
| logging_silent                   | 60.1 ns                                                    | 60.5 ns: 1.01x slower                                                           |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.07 sec: 1.01x slower                                                          |
| sqlglot_parse                    | 732 us                                                     | 737 us: 1.01x slower                                                            |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.7 ms: 1.01x slower                                                           |
| sympy_sum                        | 69.2 ms                                                    | 69.7 ms: 1.01x slower                                                           |
| telco                            | 4.60 ms                                                    | 4.64 ms: 1.01x slower                                                           |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                            |
| unpickle_pure_python             | 141 us                                                     | 142 us: 1.01x slower                                                            |
| logging_format                   | 3.31 us                                                    | 3.34 us: 1.01x slower                                                           |
| pycparser                        | 632 ms                                                     | 639 ms: 1.01x slower                                                            |
| xml_etree_process                | 37.1 ms                                                    | 37.4 ms: 1.01x slower                                                           |
| pyflate                          | 321 ms                                                     | 326 ms: 1.02x slower                                                            |
| gc_traversal                     | 2.45 ms                                                    | 2.49 ms: 1.02x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                            |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.82 ms: 1.02x slower                                                           |
| sympy_str                        | 131 ms                                                     | 134 ms: 1.02x slower                                                            |
| bench_thread_pool                | 447 us                                                     | 455 us: 1.02x slower                                                            |
| regex_effbot                     | 2.58 ms                                                    | 2.63 ms: 1.02x slower                                                           |
| tomli_loads                      | 1.47 sec                                                   | 1.49 sec: 1.02x slower                                                          |
| hexiom                           | 4.06 ms                                                    | 4.14 ms: 1.02x slower                                                           |
| django_template                  | 19.4 ms                                                    | 19.9 ms: 1.02x slower                                                           |
| xml_etree_parse                  | 106 ms                                                     | 108 ms: 1.02x slower                                                            |
| create_gc_cycles                 | 897 us                                                     | 918 us: 1.02x slower                                                            |
| unpickle_list                    | 2.88 us                                                    | 2.96 us: 1.03x slower                                                           |
| xml_etree_iterparse              | 71.5 ms                                                    | 73.4 ms: 1.03x slower                                                           |
| html5lib                         | 31.2 ms                                                    | 32.0 ms: 1.03x slower                                                           |
| pickle_pure_python               | 179 us                                                     | 184 us: 1.03x slower                                                            |
| crypto_pyaes                     | 49.5 ms                                                    | 51.2 ms: 1.03x slower                                                           |
| deltablue                        | 2.14 ms                                                    | 2.23 ms: 1.04x slower                                                           |
| raytrace                         | 147 ms                                                     | 153 ms: 1.04x slower                                                            |
| nqueens                          | 52.2 ms                                                    | 54.4 ms: 1.04x slower                                                           |
| bench_mp_pool                    | 47.2 ms                                                    | 49.3 ms: 1.04x slower                                                           |
| scimark_monte_carlo              | 42.5 ms                                                    | 44.4 ms: 1.05x slower                                                           |
| coroutines                       | 15.8 ms                                                    | 16.6 ms: 1.05x slower                                                           |
| async_tree_io                    | 563 ms                                                     | 593 ms: 1.05x slower                                                            |
| sympy_integrate                  | 10.3 ms                                                    | 10.9 ms: 1.06x slower                                                           |
| scimark_fft                      | 181 ms                                                     | 191 ms: 1.06x slower                                                            |
| fannkuch                         | 248 ms                                                     | 262 ms: 1.06x slower                                                            |
| spectral_norm                    | 66.4 ms                                                    | 70.2 ms: 1.06x slower                                                           |
| typing_runtime_protocols         | 87.6 us                                                    | 93.1 us: 1.06x slower                                                           |
| chaos                            | 34.0 ms                                                    | 36.3 ms: 1.07x slower                                                           |
| asyncio_tcp                      | 402 ms                                                     | 430 ms: 1.07x slower                                                            |
| comprehensions                   | 10.2 us                                                    | 11.0 us: 1.08x slower                                                           |
| nbody                            | 59.6 ms                                                    | 65.4 ms: 1.10x slower                                                           |
| python_startup                   | 15.2 ms                                                    | 17.0 ms: 1.12x slower                                                           |
| python_startup_no_site           | 12.3 ms                                                    | 14.2 ms: 1.15x slower                                                           |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                                    |

Benchmark hidden because not significant (17): async_tree_memoization, unpickle, async_tree_io_tg, async_tree_none_tg, json_dumps, mako, asyncio_tcp_ssl, scimark_lu, sympy_expand, pickle_list, sqlglot_optimize, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_eager_memoization, pylint, tornado_http
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241010-3.14.0a0-94f8fd0/bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0.json: unpack_sequence

# HPT report

- Reliability score: 97.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.65x
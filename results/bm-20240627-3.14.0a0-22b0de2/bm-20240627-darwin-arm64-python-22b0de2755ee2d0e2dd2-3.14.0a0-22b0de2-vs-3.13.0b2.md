# Results vs. 3.13.0b2

- fork: python
- ref: 22b0de2755ee2d0e2dd2
- machine: darwin-arm64
- commit hash: 22b0de2
- commit date: 2024-06-27
- overall geometric mean: 1.01x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 188 ms: 1.17x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.49 sec: 1.03x slower                                                |
| html5lib       | 31.2 ms                                                    | 31.8 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                      | 1.06x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg               | 198 ms                                                     | 175 ms: 1.13x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 233 ms: 1.11x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 511 ms: 1.11x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 699 ms: 1.10x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 707 ms: 1.08x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 194 ms: 1.08x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 539 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 452 ms: 1.03x faster                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 62.5 ms: 1.04x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.04x faster                                                          |

Benchmark hidden because not significant (5): async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, async_tree_eager_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 59.6 ms                                                    | 60.0 ms: 1.01x slower                                                 |
| float          | 48.6 ms                                                    | 50.6 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.54 ms: 1.02x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 17.3 ms: 1.00x slower                                                 |
| regex_dna      | 149 ms                                                     | 150 ms: 1.00x slower                                                  |
| regex_compile  | 68.5 ms                                                    | 69.4 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.49 sec: 1.02x slower                                                |
| xml_etree_iterparse  | 71.5 ms                                                    | 73.0 ms: 1.02x slower                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 54.0 ms: 1.03x slower                                                 |
| xml_etree_process    | 37.1 ms                                                    | 38.2 ms: 1.03x slower                                                 |
| pickle_pure_python   | 179 us                                                     | 185 us: 1.03x slower                                                  |
| json_dumps           | 6.23 ms                                                    | 6.46 ms: 1.04x slower                                                 |
| unpickle_pure_python | 141 us                                                     | 146 us: 1.04x slower                                                  |
| json_loads           | 16.8 us                                                    | 17.6 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.03x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 15.6 ms: 1.27x slower                                                 |
| python_startup         | 15.2 ms                                                    | 21.5 ms: 1.42x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.34x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 29.9 ms                                                    | 29.8 ms: 1.00x faster                                                 |
| mako            | 6.99 ms                                                    | 7.12 ms: 1.02x slower                                                 |
| django_template | 19.4 ms                                                    | 20.0 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 147 us: 1.39x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 17.1 us: 1.32x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.52 us: 1.20x faster                                                 |
| async_tree_none_tg               | 198 ms                                                     | 175 ms: 1.13x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 233 ms: 1.11x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 511 ms: 1.11x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 699 ms: 1.10x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 707 ms: 1.08x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 194 ms: 1.08x faster                                                  |
| mdp                              | 1.53 sec                                                   | 1.44 sec: 1.07x faster                                                |
| async_tree_io                    | 563 ms                                                     | 539 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 452 ms: 1.03x faster                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.54 ms: 1.02x faster                                                 |
| create_gc_cycles                 | 897 us                                                     | 887 us: 1.01x faster                                                  |
| generators                       | 22.9 ms                                                    | 22.7 ms: 1.01x faster                                                 |
| richards_super                   | 35.2 ms                                                    | 35.0 ms: 1.00x faster                                                 |
| genshi_xml                       | 29.9 ms                                                    | 29.8 ms: 1.00x faster                                                 |
| go                               | 101 ms                                                     | 100 ms: 1.00x faster                                                  |
| regex_v8                         | 17.3 ms                                                    | 17.3 ms: 1.00x slower                                                 |
| asyncio_websockets               | 409 ms                                                     | 410 ms: 1.00x slower                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                 |
| regex_dna                        | 149 ms                                                     | 150 ms: 1.00x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                                  |
| async_generators                 | 281 ms                                                     | 282 ms: 1.00x slower                                                  |
| pyflate                          | 321 ms                                                     | 323 ms: 1.01x slower                                                  |
| raytrace                         | 147 ms                                                     | 148 ms: 1.01x slower                                                  |
| nbody                            | 59.6 ms                                                    | 60.0 ms: 1.01x slower                                                 |
| scimark_sor                      | 94.9 ms                                                    | 95.8 ms: 1.01x slower                                                 |
| telco                            | 4.60 ms                                                    | 4.65 ms: 1.01x slower                                                 |
| coverage                         | 45.0 ms                                                    | 45.5 ms: 1.01x slower                                                 |
| regex_compile                    | 68.5 ms                                                    | 69.4 ms: 1.01x slower                                                 |
| logging_simple                   | 3.04 us                                                    | 3.08 us: 1.01x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 61.0 ns: 1.01x slower                                                 |
| pycparser                        | 632 ms                                                     | 643 ms: 1.02x slower                                                  |
| hexiom                           | 4.06 ms                                                    | 4.13 ms: 1.02x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 455 us: 1.02x slower                                                  |
| tomli_loads                      | 1.47 sec                                                   | 1.49 sec: 1.02x slower                                                |
| mako                             | 6.99 ms                                                    | 7.12 ms: 1.02x slower                                                 |
| xml_etree_iterparse              | 71.5 ms                                                    | 73.0 ms: 1.02x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 50.5 ms: 1.02x slower                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 10.6 ms: 1.02x slower                                                 |
| html5lib                         | 31.2 ms                                                    | 31.8 ms: 1.02x slower                                                 |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.13 sec: 1.02x slower                                                |
| logging_format                   | 3.31 us                                                    | 3.39 us: 1.03x slower                                                 |
| xml_etree_generate               | 52.7 ms                                                    | 54.0 ms: 1.03x slower                                                 |
| json                             | 2.93 ms                                                    | 3.01 ms: 1.03x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 72.2 ms: 1.03x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 16.3 ms: 1.03x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.8 ms: 1.03x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 68.4 ms: 1.03x slower                                                 |
| django_template                  | 19.4 ms                                                    | 20.0 ms: 1.03x slower                                                 |
| xml_etree_process                | 37.1 ms                                                    | 38.2 ms: 1.03x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 233 ms: 1.03x slower                                                  |
| sympy_str                        | 131 ms                                                     | 136 ms: 1.03x slower                                                  |
| sqlglot_normalize                | 166 ms                                                     | 171 ms: 1.03x slower                                                  |
| docutils                         | 1.44 sec                                                   | 1.49 sec: 1.03x slower                                                |
| nqueens                          | 52.2 ms                                                    | 54.0 ms: 1.03x slower                                                 |
| pickle_pure_python               | 179 us                                                     | 185 us: 1.03x slower                                                  |
| sympy_sum                        | 69.2 ms                                                    | 71.7 ms: 1.04x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 44.0 ms: 1.04x slower                                                 |
| pprint_pformat                   | 947 ms                                                     | 981 ms: 1.04x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 62.5 ms: 1.04x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.46 ms: 1.04x slower                                                 |
| chaos                            | 34.0 ms                                                    | 35.3 ms: 1.04x slower                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 483 ms: 1.04x slower                                                  |
| float                            | 48.6 ms                                                    | 50.6 ms: 1.04x slower                                                 |
| unpickle_pure_python             | 141 us                                                     | 146 us: 1.04x slower                                                  |
| sqlglot_transpile                | 891 us                                                     | 929 us: 1.04x slower                                                  |
| sqlglot_parse                    | 732 us                                                     | 763 us: 1.04x slower                                                  |
| json_loads                       | 16.8 us                                                    | 17.6 us: 1.04x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.90 ms: 1.04x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 190 ms: 1.05x slower                                                  |
| typing_runtime_protocols         | 87.6 us                                                    | 92.7 us: 1.06x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 10.8 us: 1.06x slower                                                 |
| fannkuch                         | 248 ms                                                     | 268 ms: 1.08x slower                                                  |
| scimark_lu                       | 66.9 ms                                                    | 72.4 ms: 1.08x slower                                                 |
| asyncio_tcp                      | 402 ms                                                     | 441 ms: 1.10x slower                                                  |
| 2to3                             | 161 ms                                                     | 188 ms: 1.17x slower                                                  |
| bench_mp_pool                    | 47.2 ms                                                    | 57.2 ms: 1.21x slower                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 15.6 ms: 1.27x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 21.5 ms: 1.42x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (16): async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, deltablue, richards, thrift, pidigits, async_tree_eager_tg, asyncio_tcp_ssl, genshi_text, pathlib, dask, xml_etree_parse, tornado_http, async_tree_memoization_tg, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x
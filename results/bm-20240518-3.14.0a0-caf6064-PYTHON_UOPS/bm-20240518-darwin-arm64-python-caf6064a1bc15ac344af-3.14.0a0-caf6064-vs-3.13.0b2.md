# Results vs. 3.13.0b2

- fork: python
- ref: caf6064a1bc15ac344af
- machine: darwin-arm64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.13x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 0.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 182 ms: 1.13x slower                                                  |
| chameleon      | 4.27 ms                                                    | 4.94 ms: 1.16x slower                                                 |
| docutils       | 1.44 sec                                                   | 1.66 sec: 1.16x slower                                                |
| html5lib       | 31.2 ms                                                    | 32.9 ms: 1.06x slower                                                 |
| tornado_http   | 66.7 ms                                                    | 70.6 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                      | 1.11x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 335 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 367 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 480 ms: 1.03x slower                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 129 ms: 1.03x slower                                                  |
| async_tree_none_tg               | 198 ms                                                     | 206 ms: 1.04x slower                                                  |
| async_tree_memoization           | 260 ms                                                     | 272 ms: 1.05x slower                                                  |
| async_tree_none                  | 209 ms                                                     | 221 ms: 1.05x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 44.4 ms: 1.07x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 259 ms: 1.08x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 68.7 ms: 1.14x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.04x slower                                                          |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_eager_io_tg, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_eager_io, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 282 ms: 1.00x slower                                                  |
| float          | 48.6 ms                                                    | 60.5 ms: 1.25x slower                                                 |
| nbody          | 59.6 ms                                                    | 77.3 ms: 1.30x slower                                                 |
| Geometric mean | (ref)                                                      | 1.17x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.59 ms: 1.00x slower                                                 |
| regex_v8       | 17.3 ms                                                    | 17.6 ms: 1.02x slower                                                 |
| regex_compile  | 68.5 ms                                                    | 95.7 ms: 1.40x slower                                                 |
| Geometric mean | (ref)                                                      | 1.09x slower                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_dict          | 18.3 us                                                    | 18.2 us: 1.01x faster                                                 |
| pickle_list          | 2.96 us                                                    | 2.97 us: 1.00x slower                                                 |
| unpickle             | 9.12 us                                                    | 9.39 us: 1.03x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 6.53 ms: 1.05x slower                                                 |
| xml_etree_iterparse  | 71.5 ms                                                    | 76.5 ms: 1.07x slower                                                 |
| xml_etree_process    | 37.1 ms                                                    | 41.1 ms: 1.11x slower                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 58.7 ms: 1.11x slower                                                 |
| tomli_loads          | 1.47 sec                                                   | 1.64 sec: 1.12x slower                                                |
| unpickle_pure_python | 141 us                                                     | 176 us: 1.25x slower                                                  |
| pickle_pure_python   | 179 us                                                     | 228 us: 1.28x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.07x slower                                                          |

Benchmark hidden because not significant (4): pickle, unpickle_list, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 14.2 ms: 1.07x faster                                                 |
| python_startup_no_site | 12.3 ms                                                    | 11.7 ms: 1.05x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.06x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 29.9 ms                                                    | 36.0 ms: 1.20x slower                                                 |
| django_template | 19.4 ms                                                    | 23.8 ms: 1.23x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 17.3 ms: 1.25x slower                                                 |
| mako            | 6.99 ms                                                    | 9.09 ms: 1.30x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.24x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup                   | 15.2 ms                                                    | 14.2 ms: 1.07x faster                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 11.7 ms: 1.05x faster                                                 |
| pathlib                          | 23.3 ms                                                    | 22.5 ms: 1.04x faster                                                 |
| pickle_dict                      | 18.3 us                                                    | 18.2 us: 1.01x faster                                                 |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.59 ms: 1.00x slower                                                 |
| pidigits                         | 282 ms                                                     | 282 ms: 1.00x slower                                                  |
| pickle_list                      | 2.96 us                                                    | 2.97 us: 1.00x slower                                                 |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.01x slower                                                 |
| thrift                           | 435 us                                                     | 439 us: 1.01x slower                                                  |
| coroutines                       | 15.8 ms                                                    | 16.1 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 335 ms: 1.01x slower                                                  |
| coverage                         | 45.0 ms                                                    | 45.7 ms: 1.02x slower                                                 |
| regex_v8                         | 17.3 ms                                                    | 17.6 ms: 1.02x slower                                                 |
| create_gc_cycles                 | 897 us                                                     | 914 us: 1.02x slower                                                  |
| json                             | 2.93 ms                                                    | 3.00 ms: 1.02x slower                                                 |
| dask                             | 221 ms                                                     | 227 ms: 1.02x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 367 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 480 ms: 1.03x slower                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 129 ms: 1.03x slower                                                  |
| generators                       | 22.9 ms                                                    | 23.6 ms: 1.03x slower                                                 |
| unpickle                         | 9.12 us                                                    | 9.39 us: 1.03x slower                                                 |
| sqlite_synth                     | 1.55 us                                                    | 1.61 us: 1.04x slower                                                 |
| logging_format                   | 3.31 us                                                    | 3.45 us: 1.04x slower                                                 |
| async_tree_none_tg               | 198 ms                                                     | 206 ms: 1.04x slower                                                  |
| logging_simple                   | 3.04 us                                                    | 3.18 us: 1.05x slower                                                 |
| async_tree_memoization           | 260 ms                                                     | 272 ms: 1.05x slower                                                  |
| json_dumps                       | 6.23 ms                                                    | 6.53 ms: 1.05x slower                                                 |
| async_generators                 | 281 ms                                                     | 296 ms: 1.05x slower                                                  |
| async_tree_none                  | 209 ms                                                     | 221 ms: 1.05x slower                                                  |
| html5lib                         | 31.2 ms                                                    | 32.9 ms: 1.06x slower                                                 |
| tornado_http                     | 66.7 ms                                                    | 70.6 ms: 1.06x slower                                                 |
| xml_etree_iterparse              | 71.5 ms                                                    | 76.5 ms: 1.07x slower                                                 |
| mdp                              | 1.53 sec                                                   | 1.64 sec: 1.07x slower                                                |
| async_tree_eager_tg              | 41.4 ms                                                    | 44.4 ms: 1.07x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 259 ms: 1.08x slower                                                  |
| xml_etree_process                | 37.1 ms                                                    | 41.1 ms: 1.11x slower                                                 |
| telco                            | 4.60 ms                                                    | 5.12 ms: 1.11x slower                                                 |
| xml_etree_generate               | 52.7 ms                                                    | 58.7 ms: 1.11x slower                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.64 sec: 1.12x slower                                                |
| 2to3                             | 161 ms                                                     | 182 ms: 1.13x slower                                                  |
| scimark_sor                      | 94.9 ms                                                    | 108 ms: 1.14x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 68.7 ms: 1.14x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 80.1 ms: 1.14x slower                                                 |
| pycparser                        | 632 ms                                                     | 723 ms: 1.14x slower                                                  |
| pylint                           | 170 ms                                                     | 195 ms: 1.15x slower                                                  |
| docutils                         | 1.44 sec                                                   | 1.66 sec: 1.16x slower                                                |
| chameleon                        | 4.27 ms                                                    | 4.94 ms: 1.16x slower                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 2.11 us: 1.16x slower                                                 |
| go                               | 101 ms                                                     | 117 ms: 1.17x slower                                                  |
| richards_super                   | 35.2 ms                                                    | 41.2 ms: 1.17x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 525 us: 1.18x slower                                                  |
| sympy_expand                     | 226 ms                                                     | 266 ms: 1.18x slower                                                  |
| richards                         | 31.8 ms                                                    | 37.6 ms: 1.18x slower                                                 |
| raytrace                         | 147 ms                                                     | 175 ms: 1.19x slower                                                  |
| genshi_xml                       | 29.9 ms                                                    | 36.0 ms: 1.20x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 37.2 ms: 1.20x slower                                                 |
| deepcopy                         | 204 us                                                     | 248 us: 1.22x slower                                                  |
| sympy_integrate                  | 10.3 ms                                                    | 12.6 ms: 1.22x slower                                                 |
| django_template                  | 19.4 ms                                                    | 23.8 ms: 1.23x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 108 us: 1.23x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 61.2 ms: 1.24x slower                                                 |
| sympy_sum                        | 69.2 ms                                                    | 85.9 ms: 1.24x slower                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 578 ms: 1.25x slower                                                  |
| pprint_pformat                   | 947 ms                                                     | 1.18 sec: 1.25x slower                                                |
| float                            | 48.6 ms                                                    | 60.5 ms: 1.25x slower                                                 |
| pyflate                          | 321 ms                                                     | 399 ms: 1.25x slower                                                  |
| sympy_str                        | 131 ms                                                     | 164 ms: 1.25x slower                                                  |
| genshi_text                      | 13.9 ms                                                    | 17.3 ms: 1.25x slower                                                 |
| unpickle_pure_python             | 141 us                                                     | 176 us: 1.25x slower                                                  |
| pickle_pure_python               | 179 us                                                     | 228 us: 1.28x slower                                                  |
| fannkuch                         | 248 ms                                                     | 318 ms: 1.28x slower                                                  |
| scimark_fft                      | 181 ms                                                     | 232 ms: 1.28x slower                                                  |
| sqlglot_transpile                | 891 us                                                     | 1.15 ms: 1.30x slower                                                 |
| nbody                            | 59.6 ms                                                    | 77.3 ms: 1.30x slower                                                 |
| mako                             | 6.99 ms                                                    | 9.09 ms: 1.30x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 957 us: 1.31x slower                                                  |
| nqueens                          | 52.2 ms                                                    | 69.1 ms: 1.32x slower                                                 |
| deltablue                        | 2.14 ms                                                    | 2.94 ms: 1.37x slower                                                 |
| chaos                            | 34.0 ms                                                    | 47.0 ms: 1.38x slower                                                 |
| regex_compile                    | 68.5 ms                                                    | 95.7 ms: 1.40x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 94.2 ms: 1.42x slower                                                 |
| deepcopy_memo                    | 22.6 us                                                    | 32.4 us: 1.43x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 61.1 ms: 1.44x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 4.01 ms: 1.45x slower                                                 |
| scimark_lu                       | 66.9 ms                                                    | 98.1 ms: 1.47x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 6.00 ms: 1.48x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 95.4 ns: 1.59x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 17.3 us: 1.71x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.13x slower                                                          |

Benchmark hidden because not significant (15): flaskblogging, pickle, bench_mp_pool, async_tree_io_tg, regex_dna, unpickle_list, xml_etree_parse, json_loads, asyncio_tcp_ssl, async_tree_eager_io_tg, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_eager_io, asyncio_tcp, async_tree_eager_memoization
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, dulwich_log, gunicorn, mypy2, sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 0.41x
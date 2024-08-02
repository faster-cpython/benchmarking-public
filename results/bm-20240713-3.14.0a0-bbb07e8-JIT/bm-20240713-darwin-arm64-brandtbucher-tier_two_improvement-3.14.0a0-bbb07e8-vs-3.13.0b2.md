# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: tier_two_improvement
- machine: darwin-arm64
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.02x slower
- HPT reliability: 99.74%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 171 ms: 1.06x slower                                                        |
| docutils       | 1.44 sec                                                   | 1.51 sec: 1.05x slower                                                      |
| html5lib       | 31.2 ms                                                    | 30.9 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                      | 1.03x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg               | 198 ms                                                     | 177 ms: 1.12x faster                                                        |
| async_tree_memoization           | 260 ms                                                     | 232 ms: 1.12x faster                                                        |
| async_tree_eager_io_tg           | 768 ms                                                     | 699 ms: 1.10x faster                                                        |
| async_tree_io_tg                 | 565 ms                                                     | 515 ms: 1.10x faster                                                        |
| async_tree_none                  | 209 ms                                                     | 195 ms: 1.08x faster                                                        |
| async_tree_io                    | 563 ms                                                     | 535 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 456 ms: 1.02x faster                                                        |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.1 ms: 1.01x faster                                                       |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                        |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 335 ms: 1.01x slower                                                        |
| async_tree_eager                 | 60.3 ms                                                    | 63.5 ms: 1.05x slower                                                       |
| Geometric mean                   | (ref)                                                      | 1.03x faster                                                                |

Benchmark hidden because not significant (5): async_tree_eager_io, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 47.6 ms: 1.02x faster                                                       |
| pidigits       | 282 ms                                                     | 283 ms: 1.00x slower                                                        |
| nbody          | 59.6 ms                                                    | 64.1 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                      | 1.02x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.57 ms: 1.00x faster                                                       |
| regex_compile  | 68.5 ms                                                    | 73.8 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                      | 1.02x slower                                                                |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.23 sec: 1.19x faster                                                      |
| unpickle_pure_python | 141 us                                                     | 133 us: 1.06x faster                                                        |
| xml_etree_process    | 37.1 ms                                                    | 36.4 ms: 1.02x faster                                                       |
| pickle_pure_python   | 179 us                                                     | 175 us: 1.02x faster                                                        |
| xml_etree_iterparse  | 71.5 ms                                                    | 70.5 ms: 1.01x faster                                                       |
| xml_etree_generate   | 52.7 ms                                                    | 52.4 ms: 1.01x faster                                                       |
| xml_etree_parse      | 106 ms                                                     | 107 ms: 1.01x slower                                                        |
| json_dumps           | 6.23 ms                                                    | 6.41 ms: 1.03x slower                                                       |
| json_loads           | 16.8 us                                                    | 17.4 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 15.4 ms: 1.02x slower                                                       |
| python_startup_no_site | 12.3 ms                                                    | 12.8 ms: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                      | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.47 ms: 1.08x faster                                                       |
| django_template | 19.4 ms                                                    | 21.6 ms: 1.11x slower                                                       |
| genshi_text     | 13.9 ms                                                    | 16.3 ms: 1.17x slower                                                       |
| genshi_xml      | 29.9 ms                                                    | 39.8 ms: 1.33x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.13x slower                                                                |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo                    | 22.6 us                                                    | 16.8 us: 1.35x faster                                                       |
| deepcopy                         | 204 us                                                     | 153 us: 1.33x faster                                                        |
| tomli_loads                      | 1.47 sec                                                   | 1.23 sec: 1.19x faster                                                      |
| deepcopy_reduce                  | 1.82 us                                                    | 1.55 us: 1.17x faster                                                       |
| async_tree_none_tg               | 198 ms                                                     | 177 ms: 1.12x faster                                                        |
| async_tree_memoization           | 260 ms                                                     | 232 ms: 1.12x faster                                                        |
| async_tree_eager_io_tg           | 768 ms                                                     | 699 ms: 1.10x faster                                                        |
| async_tree_io_tg                 | 565 ms                                                     | 515 ms: 1.10x faster                                                        |
| mako                             | 6.99 ms                                                    | 6.47 ms: 1.08x faster                                                       |
| async_tree_none                  | 209 ms                                                     | 195 ms: 1.08x faster                                                        |
| unpickle_pure_python             | 141 us                                                     | 133 us: 1.06x faster                                                        |
| async_tree_io                    | 563 ms                                                     | 535 ms: 1.05x faster                                                        |
| richards                         | 31.8 ms                                                    | 30.9 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 456 ms: 1.02x faster                                                        |
| generators                       | 22.9 ms                                                    | 22.4 ms: 1.02x faster                                                       |
| pyflate                          | 321 ms                                                     | 314 ms: 1.02x faster                                                        |
| float                            | 48.6 ms                                                    | 47.6 ms: 1.02x faster                                                       |
| richards_super                   | 35.2 ms                                                    | 34.5 ms: 1.02x faster                                                       |
| xml_etree_process                | 37.1 ms                                                    | 36.4 ms: 1.02x faster                                                       |
| pickle_pure_python               | 179 us                                                     | 175 us: 1.02x faster                                                        |
| xml_etree_iterparse              | 71.5 ms                                                    | 70.5 ms: 1.01x faster                                                       |
| fannkuch                         | 248 ms                                                     | 246 ms: 1.01x faster                                                        |
| telco                            | 4.60 ms                                                    | 4.55 ms: 1.01x faster                                                       |
| html5lib                         | 31.2 ms                                                    | 30.9 ms: 1.01x faster                                                       |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.1 ms: 1.01x faster                                                       |
| xml_etree_generate               | 52.7 ms                                                    | 52.4 ms: 1.01x faster                                                       |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.04 sec: 1.01x faster                                                      |
| regex_effbot                     | 2.58 ms                                                    | 2.57 ms: 1.00x faster                                                       |
| coroutines                       | 15.8 ms                                                    | 15.8 ms: 1.00x faster                                                       |
| asyncio_websockets               | 409 ms                                                     | 410 ms: 1.00x slower                                                        |
| pidigits                         | 282 ms                                                     | 283 ms: 1.00x slower                                                        |
| go                               | 101 ms                                                     | 101 ms: 1.01x slower                                                        |
| gc_traversal                     | 2.45 ms                                                    | 2.47 ms: 1.01x slower                                                       |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                        |
| logging_simple                   | 3.04 us                                                    | 3.07 us: 1.01x slower                                                       |
| create_gc_cycles                 | 897 us                                                     | 905 us: 1.01x slower                                                        |
| coverage                         | 45.0 ms                                                    | 45.5 ms: 1.01x slower                                                       |
| pathlib                          | 23.3 ms                                                    | 23.6 ms: 1.01x slower                                                       |
| xml_etree_parse                  | 106 ms                                                     | 107 ms: 1.01x slower                                                        |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 335 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.31 sec: 1.02x slower                                                      |
| mdp                              | 1.53 sec                                                   | 1.56 sec: 1.02x slower                                                      |
| meteor_contest                   | 70.3 ms                                                    | 71.6 ms: 1.02x slower                                                       |
| python_startup                   | 15.2 ms                                                    | 15.4 ms: 1.02x slower                                                       |
| logging_format                   | 3.31 us                                                    | 3.37 us: 1.02x slower                                                       |
| dask                             | 221 ms                                                     | 226 ms: 1.02x slower                                                        |
| json_dumps                       | 6.23 ms                                                    | 6.41 ms: 1.03x slower                                                       |
| json_loads                       | 16.8 us                                                    | 17.4 us: 1.03x slower                                                       |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.9 ms: 1.03x slower                                                       |
| spectral_norm                    | 66.4 ms                                                    | 68.6 ms: 1.03x slower                                                       |
| logging_silent                   | 60.1 ns                                                    | 62.2 ns: 1.03x slower                                                       |
| python_startup_no_site           | 12.3 ms                                                    | 12.8 ms: 1.04x slower                                                       |
| pprint_safe_repr                 | 465 ms                                                     | 482 ms: 1.04x slower                                                        |
| pprint_pformat                   | 947 ms                                                     | 986 ms: 1.04x slower                                                        |
| async_generators                 | 281 ms                                                     | 294 ms: 1.05x slower                                                        |
| crypto_pyaes                     | 49.5 ms                                                    | 51.9 ms: 1.05x slower                                                       |
| docutils                         | 1.44 sec                                                   | 1.51 sec: 1.05x slower                                                      |
| async_tree_eager                 | 60.3 ms                                                    | 63.5 ms: 1.05x slower                                                       |
| sympy_sum                        | 69.2 ms                                                    | 73.1 ms: 1.06x slower                                                       |
| bench_thread_pool                | 447 us                                                     | 473 us: 1.06x slower                                                        |
| 2to3                             | 161 ms                                                     | 171 ms: 1.06x slower                                                        |
| scimark_fft                      | 181 ms                                                     | 192 ms: 1.07x slower                                                        |
| scimark_sor                      | 94.9 ms                                                    | 101 ms: 1.07x slower                                                        |
| sympy_str                        | 131 ms                                                     | 141 ms: 1.07x slower                                                        |
| sympy_integrate                  | 10.3 ms                                                    | 11.1 ms: 1.07x slower                                                       |
| bench_mp_pool                    | 47.2 ms                                                    | 50.6 ms: 1.07x slower                                                       |
| nbody                            | 59.6 ms                                                    | 64.1 ms: 1.08x slower                                                       |
| sympy_expand                     | 226 ms                                                     | 243 ms: 1.08x slower                                                        |
| pycparser                        | 632 ms                                                     | 682 ms: 1.08x slower                                                        |
| regex_compile                    | 68.5 ms                                                    | 73.8 ms: 1.08x slower                                                       |
| sqlglot_normalize                | 166 ms                                                     | 179 ms: 1.08x slower                                                        |
| sqlglot_optimize                 | 30.9 ms                                                    | 33.4 ms: 1.08x slower                                                       |
| hexiom                           | 4.06 ms                                                    | 4.39 ms: 1.08x slower                                                       |
| deltablue                        | 2.14 ms                                                    | 2.32 ms: 1.09x slower                                                       |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 3.03 ms: 1.09x slower                                                       |
| nqueens                          | 52.2 ms                                                    | 58.0 ms: 1.11x slower                                                       |
| django_template                  | 19.4 ms                                                    | 21.6 ms: 1.11x slower                                                       |
| typing_runtime_protocols         | 87.6 us                                                    | 97.4 us: 1.11x slower                                                       |
| raytrace                         | 147 ms                                                     | 165 ms: 1.12x slower                                                        |
| sqlglot_transpile                | 891 us                                                     | 1.01 ms: 1.13x slower                                                       |
| sqlglot_parse                    | 732 us                                                     | 836 us: 1.14x slower                                                        |
| chaos                            | 34.0 ms                                                    | 39.6 ms: 1.16x slower                                                       |
| genshi_text                      | 13.9 ms                                                    | 16.3 ms: 1.17x slower                                                       |
| comprehensions                   | 10.2 us                                                    | 12.4 us: 1.22x slower                                                       |
| scimark_lu                       | 66.9 ms                                                    | 82.8 ms: 1.24x slower                                                       |
| genshi_xml                       | 29.9 ms                                                    | 39.8 ms: 1.33x slower                                                       |
| Geometric mean                   | (ref)                                                      | 1.02x slower                                                                |

Benchmark hidden because not significant (12): async_tree_eager_io, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, thrift, regex_v8, regex_dna, json, async_tree_memoization_tg, tornado_http, asyncio_tcp, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.74% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x
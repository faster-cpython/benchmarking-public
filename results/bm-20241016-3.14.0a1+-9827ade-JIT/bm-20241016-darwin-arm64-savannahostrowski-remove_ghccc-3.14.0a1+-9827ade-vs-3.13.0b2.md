# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: remove_ghccc
- machine: darwin-arm64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.04x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 182 ms: 1.13x slower                                                      |
| docutils       | 1.44 sec                                                   | 1.57 sec: 1.09x slower                                                    |
| html5lib       | 31.2 ms                                                    | 33.8 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                      | 1.12x slower                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 672 ms: 1.14x faster                                                      |
| async_tree_eager_io_tg           | 768 ms                                                     | 714 ms: 1.08x faster                                                      |
| async_tree_memoization           | 260 ms                                                     | 246 ms: 1.06x faster                                                      |
| async_tree_none                  | 209 ms                                                     | 200 ms: 1.05x faster                                                      |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 458 ms: 1.02x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 365 ms: 1.02x slower                                                      |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 337 ms: 1.02x slower                                                      |
| async_tree_io                    | 563 ms                                                     | 584 ms: 1.04x slower                                                      |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 471 ms: 1.04x slower                                                      |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 131 ms: 1.05x slower                                                      |
| async_tree_eager_tg              | 41.4 ms                                                    | 43.3 ms: 1.05x slower                                                     |
| async_tree_eager                 | 60.3 ms                                                    | 63.8 ms: 1.06x slower                                                     |
| async_tree_none_tg               | 198 ms                                                     | 213 ms: 1.08x slower                                                      |
| async_tree_io_tg                 | 565 ms                                                     | 613 ms: 1.08x slower                                                      |
| Geometric mean                   | (ref)                                                      | 1.01x slower                                                              |

Benchmark hidden because not significant (2): async_tree_memoization_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 47.7 ms: 1.02x faster                                                     |
| pidigits       | 282 ms                                                     | 283 ms: 1.00x slower                                                      |
| nbody          | 59.6 ms                                                    | 63.2 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                      | 1.01x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 16.9 ms: 1.02x faster                                                     |
| regex_effbot   | 2.58 ms                                                    | 2.62 ms: 1.02x slower                                                     |
| regex_compile  | 68.5 ms                                                    | 74.0 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                      | 1.02x slower                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.23 sec: 1.19x faster                                                    |
| xml_etree_process    | 37.1 ms                                                    | 34.3 ms: 1.08x faster                                                     |
| unpickle_pure_python | 141 us                                                     | 132 us: 1.07x faster                                                      |
| xml_etree_generate   | 52.7 ms                                                    | 49.8 ms: 1.06x faster                                                     |
| json_loads           | 16.8 us                                                    | 16.5 us: 1.02x faster                                                     |
| pickle               | 7.48 us                                                    | 7.37 us: 1.01x faster                                                     |
| unpickle             | 9.12 us                                                    | 9.04 us: 1.01x faster                                                     |
| xml_etree_parse      | 106 ms                                                     | 107 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 71.5 ms                                                    | 73.2 ms: 1.02x slower                                                     |
| unpickle_list        | 2.88 us                                                    | 2.97 us: 1.03x slower                                                     |
| json_dumps           | 6.23 ms                                                    | 7.23 ms: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                              |

Benchmark hidden because not significant (3): pickle_dict, pickle_pure_python, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 14.7 ms: 1.19x slower                                                     |
| python_startup         | 15.2 ms                                                    | 19.0 ms: 1.25x slower                                                     |
| Geometric mean         | (ref)                                                      | 1.22x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.30 ms: 1.11x faster                                                     |
| django_template | 19.4 ms                                                    | 22.5 ms: 1.16x slower                                                     |
| genshi_text     | 13.9 ms                                                    | 16.3 ms: 1.17x slower                                                     |
| genshi_xml      | 29.9 ms                                                    | 38.4 ms: 1.28x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.12x slower                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| asyncio_websockets               | 409 ms                                                     | 242 ms: 1.69x faster                                                      |
| deepcopy_memo                    | 22.6 us                                                    | 16.8 us: 1.35x faster                                                     |
| deepcopy                         | 204 us                                                     | 155 us: 1.31x faster                                                      |
| tomli_loads                      | 1.47 sec                                                   | 1.23 sec: 1.19x faster                                                    |
| deepcopy_reduce                  | 1.82 us                                                    | 1.53 us: 1.19x faster                                                     |
| scimark_sor                      | 94.9 ms                                                    | 82.4 ms: 1.15x faster                                                     |
| async_tree_eager_io              | 766 ms                                                     | 672 ms: 1.14x faster                                                      |
| mako                             | 6.99 ms                                                    | 6.30 ms: 1.11x faster                                                     |
| xml_etree_process                | 37.1 ms                                                    | 34.3 ms: 1.08x faster                                                     |
| async_tree_eager_io_tg           | 768 ms                                                     | 714 ms: 1.08x faster                                                      |
| unpickle_pure_python             | 141 us                                                     | 132 us: 1.07x faster                                                      |
| xml_etree_generate               | 52.7 ms                                                    | 49.8 ms: 1.06x faster                                                     |
| async_tree_memoization           | 260 ms                                                     | 246 ms: 1.06x faster                                                      |
| async_tree_none                  | 209 ms                                                     | 200 ms: 1.05x faster                                                      |
| go                               | 101 ms                                                     | 96.8 ms: 1.04x faster                                                     |
| pathlib                          | 23.3 ms                                                    | 22.5 ms: 1.04x faster                                                     |
| bpe_tokeniser                    | 3.05 sec                                                   | 2.98 sec: 1.03x faster                                                    |
| regex_v8                         | 17.3 ms                                                    | 16.9 ms: 1.02x faster                                                     |
| thrift                           | 435 us                                                     | 426 us: 1.02x faster                                                      |
| coverage                         | 45.0 ms                                                    | 44.1 ms: 1.02x faster                                                     |
| json                             | 2.93 ms                                                    | 2.87 ms: 1.02x faster                                                     |
| json_loads                       | 16.8 us                                                    | 16.5 us: 1.02x faster                                                     |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 458 ms: 1.02x faster                                                      |
| float                            | 48.6 ms                                                    | 47.7 ms: 1.02x faster                                                     |
| scimark_lu                       | 66.9 ms                                                    | 65.7 ms: 1.02x faster                                                     |
| pickle                           | 7.48 us                                                    | 7.37 us: 1.01x faster                                                     |
| telco                            | 4.60 ms                                                    | 4.55 ms: 1.01x faster                                                     |
| unpickle                         | 9.12 us                                                    | 9.04 us: 1.01x faster                                                     |
| pyflate                          | 321 ms                                                     | 318 ms: 1.01x faster                                                      |
| sqlite_synth                     | 1.55 us                                                    | 1.54 us: 1.01x faster                                                     |
| pidigits                         | 282 ms                                                     | 283 ms: 1.00x slower                                                      |
| pprint_safe_repr                 | 465 ms                                                     | 470 ms: 1.01x slower                                                      |
| pprint_pformat                   | 947 ms                                                     | 961 ms: 1.02x slower                                                      |
| regex_effbot                     | 2.58 ms                                                    | 2.62 ms: 1.02x slower                                                     |
| logging_simple                   | 3.04 us                                                    | 3.09 us: 1.02x slower                                                     |
| xml_etree_parse                  | 106 ms                                                     | 107 ms: 1.02x slower                                                      |
| logging_format                   | 3.31 us                                                    | 3.37 us: 1.02x slower                                                     |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 365 ms: 1.02x slower                                                      |
| mdp                              | 1.53 sec                                                   | 1.56 sec: 1.02x slower                                                    |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 337 ms: 1.02x slower                                                      |
| xml_etree_iterparse              | 71.5 ms                                                    | 73.2 ms: 1.02x slower                                                     |
| scimark_fft                      | 181 ms                                                     | 185 ms: 1.03x slower                                                      |
| spectral_norm                    | 66.4 ms                                                    | 68.1 ms: 1.03x slower                                                     |
| unpickle_list                    | 2.88 us                                                    | 2.97 us: 1.03x slower                                                     |
| dulwich_log                      | 27.6 ms                                                    | 28.5 ms: 1.03x slower                                                     |
| async_tree_io                    | 563 ms                                                     | 584 ms: 1.04x slower                                                      |
| meteor_contest                   | 70.3 ms                                                    | 73.1 ms: 1.04x slower                                                     |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 471 ms: 1.04x slower                                                      |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 131 ms: 1.05x slower                                                      |
| async_tree_eager_tg              | 41.4 ms                                                    | 43.3 ms: 1.05x slower                                                     |
| async_generators                 | 281 ms                                                     | 295 ms: 1.05x slower                                                      |
| coroutines                       | 15.8 ms                                                    | 16.7 ms: 1.06x slower                                                     |
| async_tree_eager                 | 60.3 ms                                                    | 63.8 ms: 1.06x slower                                                     |
| scimark_monte_carlo              | 42.5 ms                                                    | 45.0 ms: 1.06x slower                                                     |
| nbody                            | 59.6 ms                                                    | 63.2 ms: 1.06x slower                                                     |
| bench_thread_pool                | 447 us                                                     | 474 us: 1.06x slower                                                      |
| pycparser                        | 632 ms                                                     | 673 ms: 1.06x slower                                                      |
| fannkuch                         | 248 ms                                                     | 265 ms: 1.07x slower                                                      |
| crypto_pyaes                     | 49.5 ms                                                    | 53.1 ms: 1.07x slower                                                     |
| regex_compile                    | 68.5 ms                                                    | 74.0 ms: 1.08x slower                                                     |
| async_tree_none_tg               | 198 ms                                                     | 213 ms: 1.08x slower                                                      |
| html5lib                         | 31.2 ms                                                    | 33.8 ms: 1.08x slower                                                     |
| async_tree_io_tg                 | 565 ms                                                     | 613 ms: 1.08x slower                                                      |
| richards                         | 31.8 ms                                                    | 34.5 ms: 1.08x slower                                                     |
| richards_super                   | 35.2 ms                                                    | 38.3 ms: 1.09x slower                                                     |
| typing_runtime_protocols         | 87.6 us                                                    | 95.3 us: 1.09x slower                                                     |
| docutils                         | 1.44 sec                                                   | 1.57 sec: 1.09x slower                                                    |
| generators                       | 22.9 ms                                                    | 25.2 ms: 1.10x slower                                                     |
| sympy_expand                     | 226 ms                                                     | 249 ms: 1.10x slower                                                      |
| asyncio_tcp                      | 402 ms                                                     | 443 ms: 1.10x slower                                                      |
| sqlglot_normalize                | 166 ms                                                     | 186 ms: 1.12x slower                                                      |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 3.11 ms: 1.12x slower                                                     |
| deltablue                        | 2.14 ms                                                    | 2.42 ms: 1.13x slower                                                     |
| 2to3                             | 161 ms                                                     | 182 ms: 1.13x slower                                                      |
| sympy_sum                        | 69.2 ms                                                    | 79.2 ms: 1.14x slower                                                     |
| sympy_str                        | 131 ms                                                     | 151 ms: 1.15x slower                                                      |
| raytrace                         | 147 ms                                                     | 169 ms: 1.15x slower                                                      |
| nqueens                          | 52.2 ms                                                    | 59.9 ms: 1.15x slower                                                     |
| django_template                  | 19.4 ms                                                    | 22.5 ms: 1.16x slower                                                     |
| sqlglot_parse                    | 732 us                                                     | 849 us: 1.16x slower                                                      |
| json_dumps                       | 6.23 ms                                                    | 7.23 ms: 1.16x slower                                                     |
| sqlglot_transpile                | 891 us                                                     | 1.04 ms: 1.17x slower                                                     |
| genshi_text                      | 13.9 ms                                                    | 16.3 ms: 1.17x slower                                                     |
| logging_silent                   | 60.1 ns                                                    | 70.7 ns: 1.18x slower                                                     |
| python_startup_no_site           | 12.3 ms                                                    | 14.7 ms: 1.19x slower                                                     |
| sqlglot_optimize                 | 30.9 ms                                                    | 36.9 ms: 1.19x slower                                                     |
| sympy_integrate                  | 10.3 ms                                                    | 12.5 ms: 1.20x slower                                                     |
| gc_traversal                     | 2.45 ms                                                    | 2.95 ms: 1.20x slower                                                     |
| hexiom                           | 4.06 ms                                                    | 4.95 ms: 1.22x slower                                                     |
| chaos                            | 34.0 ms                                                    | 41.8 ms: 1.23x slower                                                     |
| pylint                           | 170 ms                                                     | 210 ms: 1.23x slower                                                      |
| python_startup                   | 15.2 ms                                                    | 19.0 ms: 1.25x slower                                                     |
| comprehensions                   | 10.2 us                                                    | 13.0 us: 1.28x slower                                                     |
| genshi_xml                       | 29.9 ms                                                    | 38.4 ms: 1.28x slower                                                     |
| bench_mp_pool                    | 47.2 ms                                                    | 61.7 ms: 1.31x slower                                                     |
| create_gc_cycles                 | 897 us                                                     | 1.32 ms: 1.48x slower                                                     |
| Geometric mean                   | (ref)                                                      | 1.04x slower                                                              |

Benchmark hidden because not significant (8): async_tree_memoization_tg, regex_dna, pickle_dict, pickle_pure_python, pickle_list, asyncio_tcp_ssl, async_tree_eager_memoization, tornado_http
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241016-3.14.0a1+-9827ade-JIT/bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.19x
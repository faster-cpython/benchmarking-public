# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_likely
- machine: darwin-arm64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.05x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 183 ms: 1.14x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.58 sec: 1.10x slower                                                |
| html5lib       | 31.2 ms                                                    | 33.9 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                      | 1.13x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 669 ms: 1.15x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 714 ms: 1.07x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 244 ms: 1.06x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 198 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 458 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 363 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 337 ms: 1.02x slower                                                  |
| async_tree_io                    | 563 ms                                                     | 581 ms: 1.03x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.8 ms: 1.03x slower                                                 |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 130 ms: 1.04x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 470 ms: 1.04x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 63.4 ms: 1.05x slower                                                 |
| async_tree_none_tg               | 198 ms                                                     | 213 ms: 1.08x slower                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 611 ms: 1.08x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (2): async_tree_memoization_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 48.2 ms: 1.01x faster                                                 |
| pidigits       | 282 ms                                                     | 283 ms: 1.00x slower                                                  |
| nbody          | 59.6 ms                                                    | 65.3 ms: 1.10x slower                                                 |
| Geometric mean | (ref)                                                      | 1.03x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 17.0 ms: 1.01x faster                                                 |
| regex_dna      | 149 ms                                                     | 149 ms: 1.00x faster                                                  |
| regex_effbot   | 2.58 ms                                                    | 2.65 ms: 1.03x slower                                                 |
| regex_compile  | 68.5 ms                                                    | 75.4 ms: 1.10x slower                                                 |
| Geometric mean | (ref)                                                      | 1.03x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.25 sec: 1.17x faster                                                |
| unpickle_pure_python | 141 us                                                     | 132 us: 1.07x faster                                                  |
| xml_etree_process    | 37.1 ms                                                    | 34.9 ms: 1.06x faster                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 50.6 ms: 1.04x faster                                                 |
| pickle_list          | 2.96 us                                                    | 2.87 us: 1.03x faster                                                 |
| pickle               | 7.48 us                                                    | 7.34 us: 1.02x faster                                                 |
| json_loads           | 16.8 us                                                    | 16.5 us: 1.02x faster                                                 |
| unpickle             | 9.12 us                                                    | 9.06 us: 1.01x faster                                                 |
| pickle_dict          | 18.3 us                                                    | 18.2 us: 1.01x faster                                                 |
| xml_etree_parse      | 106 ms                                                     | 107 ms: 1.01x slower                                                  |
| xml_etree_iterparse  | 71.5 ms                                                    | 73.0 ms: 1.02x slower                                                 |
| unpickle_list        | 2.88 us                                                    | 2.97 us: 1.03x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 7.13 ms: 1.15x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 14.7 ms: 1.19x slower                                                 |
| python_startup         | 15.2 ms                                                    | 18.9 ms: 1.25x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.22x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.46 ms: 1.08x faster                                                 |
| genshi_text     | 13.9 ms                                                    | 16.1 ms: 1.16x slower                                                 |
| django_template | 19.4 ms                                                    | 22.7 ms: 1.17x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 42.1 ms: 1.41x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.15x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_websockets               | 409 ms                                                     | 241 ms: 1.69x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 17.0 us: 1.33x faster                                                 |
| deepcopy                         | 204 us                                                     | 155 us: 1.32x faster                                                  |
| deepcopy_reduce                  | 1.82 us                                                    | 1.55 us: 1.17x faster                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.25 sec: 1.17x faster                                                |
| async_tree_eager_io              | 766 ms                                                     | 669 ms: 1.15x faster                                                  |
| scimark_sor                      | 94.9 ms                                                    | 85.9 ms: 1.10x faster                                                 |
| mako                             | 6.99 ms                                                    | 6.46 ms: 1.08x faster                                                 |
| async_tree_eager_io_tg           | 768 ms                                                     | 714 ms: 1.07x faster                                                  |
| unpickle_pure_python             | 141 us                                                     | 132 us: 1.07x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 244 ms: 1.06x faster                                                  |
| xml_etree_process                | 37.1 ms                                                    | 34.9 ms: 1.06x faster                                                 |
| async_tree_none                  | 209 ms                                                     | 198 ms: 1.06x faster                                                  |
| pathlib                          | 23.3 ms                                                    | 22.2 ms: 1.05x faster                                                 |
| xml_etree_generate               | 52.7 ms                                                    | 50.6 ms: 1.04x faster                                                 |
| scimark_lu                       | 66.9 ms                                                    | 64.6 ms: 1.04x faster                                                 |
| json                             | 2.93 ms                                                    | 2.84 ms: 1.03x faster                                                 |
| pickle_list                      | 2.96 us                                                    | 2.87 us: 1.03x faster                                                 |
| thrift                           | 435 us                                                     | 424 us: 1.03x faster                                                  |
| go                               | 101 ms                                                     | 97.9 ms: 1.03x faster                                                 |
| coverage                         | 45.0 ms                                                    | 43.8 ms: 1.03x faster                                                 |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 458 ms: 1.02x faster                                                  |
| pickle                           | 7.48 us                                                    | 7.34 us: 1.02x faster                                                 |
| json_loads                       | 16.8 us                                                    | 16.5 us: 1.02x faster                                                 |
| regex_v8                         | 17.3 ms                                                    | 17.0 ms: 1.01x faster                                                 |
| sqlite_synth                     | 1.55 us                                                    | 1.54 us: 1.01x faster                                                 |
| float                            | 48.6 ms                                                    | 48.2 ms: 1.01x faster                                                 |
| unpickle                         | 9.12 us                                                    | 9.06 us: 1.01x faster                                                 |
| telco                            | 4.60 ms                                                    | 4.57 ms: 1.01x faster                                                 |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.03 sec: 1.01x faster                                                |
| pickle_dict                      | 18.3 us                                                    | 18.2 us: 1.01x faster                                                 |
| regex_dna                        | 149 ms                                                     | 149 ms: 1.00x faster                                                  |
| pidigits                         | 282 ms                                                     | 283 ms: 1.00x slower                                                  |
| xml_etree_parse                  | 106 ms                                                     | 107 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 363 ms: 1.01x slower                                                  |
| pyflate                          | 321 ms                                                     | 326 ms: 1.02x slower                                                  |
| mdp                              | 1.53 sec                                                   | 1.56 sec: 1.02x slower                                                |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 337 ms: 1.02x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 73.0 ms: 1.02x slower                                                 |
| regex_effbot                     | 2.58 ms                                                    | 2.65 ms: 1.03x slower                                                 |
| logging_simple                   | 3.04 us                                                    | 3.12 us: 1.03x slower                                                 |
| logging_format                   | 3.31 us                                                    | 3.40 us: 1.03x slower                                                 |
| unpickle_list                    | 2.88 us                                                    | 2.97 us: 1.03x slower                                                 |
| async_tree_io                    | 563 ms                                                     | 581 ms: 1.03x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.8 ms: 1.03x slower                                                 |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 130 ms: 1.04x slower                                                  |
| async_generators                 | 281 ms                                                     | 292 ms: 1.04x slower                                                  |
| dulwich_log                      | 27.6 ms                                                    | 28.7 ms: 1.04x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 16.5 ms: 1.04x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 470 ms: 1.04x slower                                                  |
| spectral_norm                    | 66.4 ms                                                    | 69.4 ms: 1.05x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 63.4 ms: 1.05x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 190 ms: 1.05x slower                                                  |
| pprint_safe_repr                 | 465 ms                                                     | 490 ms: 1.05x slower                                                  |
| bench_thread_pool                | 447 us                                                     | 473 us: 1.06x slower                                                  |
| meteor_contest                   | 70.3 ms                                                    | 74.4 ms: 1.06x slower                                                 |
| pprint_pformat                   | 947 ms                                                     | 1.00 sec: 1.06x slower                                                |
| fannkuch                         | 248 ms                                                     | 266 ms: 1.07x slower                                                  |
| scimark_monte_carlo              | 42.5 ms                                                    | 45.6 ms: 1.07x slower                                                 |
| async_tree_none_tg               | 198 ms                                                     | 213 ms: 1.08x slower                                                  |
| pycparser                        | 632 ms                                                     | 683 ms: 1.08x slower                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 611 ms: 1.08x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 53.7 ms: 1.09x slower                                                 |
| html5lib                         | 31.2 ms                                                    | 33.9 ms: 1.09x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 247 ms: 1.09x slower                                                  |
| nbody                            | 59.6 ms                                                    | 65.3 ms: 1.10x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.58 sec: 1.10x slower                                                |
| regex_compile                    | 68.5 ms                                                    | 75.4 ms: 1.10x slower                                                 |
| generators                       | 22.9 ms                                                    | 25.4 ms: 1.11x slower                                                 |
| sqlglot_normalize                | 166 ms                                                     | 184 ms: 1.11x slower                                                  |
| richards_super                   | 35.2 ms                                                    | 39.3 ms: 1.12x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 97.8 us: 1.12x slower                                                 |
| richards                         | 31.8 ms                                                    | 35.6 ms: 1.12x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 58.6 ms: 1.12x slower                                                 |
| asyncio_tcp                      | 402 ms                                                     | 452 ms: 1.12x slower                                                  |
| deltablue                        | 2.14 ms                                                    | 2.41 ms: 1.13x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 3.16 ms: 1.14x slower                                                 |
| 2to3                             | 161 ms                                                     | 183 ms: 1.14x slower                                                  |
| sympy_sum                        | 69.2 ms                                                    | 79.2 ms: 1.14x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 7.13 ms: 1.15x slower                                                 |
| sympy_str                        | 131 ms                                                     | 151 ms: 1.15x slower                                                  |
| genshi_text                      | 13.9 ms                                                    | 16.1 ms: 1.16x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 70.3 ns: 1.17x slower                                                 |
| django_template                  | 19.4 ms                                                    | 22.7 ms: 1.17x slower                                                 |
| raytrace                         | 147 ms                                                     | 174 ms: 1.19x slower                                                  |
| sqlglot_parse                    | 732 us                                                     | 871 us: 1.19x slower                                                  |
| sqlglot_transpile                | 891 us                                                     | 1.06 ms: 1.19x slower                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 14.7 ms: 1.19x slower                                                 |
| gc_traversal                     | 2.45 ms                                                    | 2.95 ms: 1.20x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 37.2 ms: 1.20x slower                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 12.6 ms: 1.21x slower                                                 |
| chaos                            | 34.0 ms                                                    | 41.3 ms: 1.22x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 4.94 ms: 1.22x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 18.9 ms: 1.25x slower                                                 |
| pylint                           | 170 ms                                                     | 213 ms: 1.25x slower                                                  |
| comprehensions                   | 10.2 us                                                    | 13.1 us: 1.29x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 62.0 ms: 1.31x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 42.1 ms: 1.41x slower                                                 |
| create_gc_cycles                 | 897 us                                                     | 1.32 ms: 1.47x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.05x slower                                                          |

Benchmark hidden because not significant (5): async_tree_memoization_tg, pickle_pure_python, async_tree_eager_memoization, asyncio_tcp_ssl, tornado_http
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.20x
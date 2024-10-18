# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_unlikely
- machine: darwin-arm64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 183 ms: 1.14x slower                                                    |
| docutils       | 1.44 sec                                                   | 1.58 sec: 1.10x slower                                                  |
| html5lib       | 31.2 ms                                                    | 34.0 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                      | 1.13x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 671 ms: 1.14x faster                                                    |
| async_tree_eager_io_tg           | 768 ms                                                     | 715 ms: 1.07x faster                                                    |
| async_tree_memoization           | 260 ms                                                     | 245 ms: 1.06x faster                                                    |
| async_tree_none                  | 209 ms                                                     | 199 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 458 ms: 1.02x faster                                                    |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 363 ms: 1.01x slower                                                    |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 337 ms: 1.02x slower                                                    |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.4 ms: 1.02x slower                                                   |
| async_tree_io                    | 563 ms                                                     | 582 ms: 1.03x slower                                                    |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 131 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 471 ms: 1.04x slower                                                    |
| async_tree_eager                 | 60.3 ms                                                    | 63.4 ms: 1.05x slower                                                   |
| async_tree_none_tg               | 198 ms                                                     | 214 ms: 1.08x slower                                                    |
| async_tree_io_tg                 | 565 ms                                                     | 613 ms: 1.09x slower                                                    |
| Geometric mean                   | (ref)                                                      | 1.00x slower                                                            |

Benchmark hidden because not significant (2): async_tree_memoization_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 48.4 ms: 1.01x faster                                                   |
| pidigits       | 282 ms                                                     | 284 ms: 1.01x slower                                                    |
| nbody          | 59.6 ms                                                    | 65.5 ms: 1.10x slower                                                   |
| Geometric mean | (ref)                                                      | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 16.9 ms: 1.02x faster                                                   |
| regex_dna      | 149 ms                                                     | 148 ms: 1.01x faster                                                    |
| regex_effbot   | 2.58 ms                                                    | 2.63 ms: 1.02x slower                                                   |
| regex_compile  | 68.5 ms                                                    | 75.8 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                      | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.26 sec: 1.16x faster                                                  |
| unpickle_pure_python | 141 us                                                     | 132 us: 1.07x faster                                                    |
| xml_etree_process    | 37.1 ms                                                    | 35.0 ms: 1.06x faster                                                   |
| xml_etree_generate   | 52.7 ms                                                    | 50.8 ms: 1.04x faster                                                   |
| pickle_list          | 2.96 us                                                    | 2.86 us: 1.03x faster                                                   |
| pickle               | 7.48 us                                                    | 7.32 us: 1.02x faster                                                   |
| json_loads           | 16.8 us                                                    | 16.6 us: 1.02x faster                                                   |
| pickle_dict          | 18.3 us                                                    | 18.2 us: 1.00x faster                                                   |
| pickle_pure_python   | 179 us                                                     | 180 us: 1.01x slower                                                    |
| xml_etree_parse      | 106 ms                                                     | 107 ms: 1.02x slower                                                    |
| xml_etree_iterparse  | 71.5 ms                                                    | 72.9 ms: 1.02x slower                                                   |
| unpickle_list        | 2.88 us                                                    | 2.96 us: 1.03x slower                                                   |
| json_dumps           | 6.23 ms                                                    | 7.14 ms: 1.15x slower                                                   |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                            |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 14.8 ms: 1.20x slower                                                   |
| python_startup         | 15.2 ms                                                    | 19.2 ms: 1.26x slower                                                   |
| Geometric mean         | (ref)                                                      | 1.23x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.48 ms: 1.08x faster                                                   |
| django_template | 19.4 ms                                                    | 22.8 ms: 1.17x slower                                                   |
| genshi_text     | 13.9 ms                                                    | 17.0 ms: 1.22x slower                                                   |
| genshi_xml      | 29.9 ms                                                    | 42.9 ms: 1.43x slower                                                   |
| Geometric mean  | (ref)                                                      | 1.17x slower                                                            |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets               | 409 ms                                                     | 241 ms: 1.69x faster                                                    |
| deepcopy_memo                    | 22.6 us                                                    | 16.9 us: 1.34x faster                                                   |
| deepcopy                         | 204 us                                                     | 156 us: 1.31x faster                                                    |
| deepcopy_reduce                  | 1.82 us                                                    | 1.56 us: 1.17x faster                                                   |
| tomli_loads                      | 1.47 sec                                                   | 1.26 sec: 1.16x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 671 ms: 1.14x faster                                                    |
| scimark_sor                      | 94.9 ms                                                    | 86.1 ms: 1.10x faster                                                   |
| mako                             | 6.99 ms                                                    | 6.48 ms: 1.08x faster                                                   |
| async_tree_eager_io_tg           | 768 ms                                                     | 715 ms: 1.07x faster                                                    |
| unpickle_pure_python             | 141 us                                                     | 132 us: 1.07x faster                                                    |
| async_tree_memoization           | 260 ms                                                     | 245 ms: 1.06x faster                                                    |
| xml_etree_process                | 37.1 ms                                                    | 35.0 ms: 1.06x faster                                                   |
| async_tree_none                  | 209 ms                                                     | 199 ms: 1.05x faster                                                    |
| pathlib                          | 23.3 ms                                                    | 22.4 ms: 1.04x faster                                                   |
| xml_etree_generate               | 52.7 ms                                                    | 50.8 ms: 1.04x faster                                                   |
| scimark_lu                       | 66.9 ms                                                    | 64.6 ms: 1.04x faster                                                   |
| coverage                         | 45.0 ms                                                    | 43.5 ms: 1.03x faster                                                   |
| pickle_list                      | 2.96 us                                                    | 2.86 us: 1.03x faster                                                   |
| go                               | 101 ms                                                     | 98.2 ms: 1.02x faster                                                   |
| thrift                           | 435 us                                                     | 426 us: 1.02x faster                                                    |
| pickle                           | 7.48 us                                                    | 7.32 us: 1.02x faster                                                   |
| regex_v8                         | 17.3 ms                                                    | 16.9 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 458 ms: 1.02x faster                                                    |
| json                             | 2.93 ms                                                    | 2.88 ms: 1.02x faster                                                   |
| json_loads                       | 16.8 us                                                    | 16.6 us: 1.02x faster                                                   |
| regex_dna                        | 149 ms                                                     | 148 ms: 1.01x faster                                                    |
| sqlite_synth                     | 1.55 us                                                    | 1.54 us: 1.01x faster                                                   |
| float                            | 48.6 ms                                                    | 48.4 ms: 1.01x faster                                                   |
| pickle_dict                      | 18.3 us                                                    | 18.2 us: 1.00x faster                                                   |
| pidigits                         | 282 ms                                                     | 284 ms: 1.01x slower                                                    |
| pickle_pure_python               | 179 us                                                     | 180 us: 1.01x slower                                                    |
| mdp                              | 1.53 sec                                                   | 1.55 sec: 1.01x slower                                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.09 sec: 1.01x slower                                                  |
| telco                            | 4.60 ms                                                    | 4.67 ms: 1.01x slower                                                   |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 363 ms: 1.01x slower                                                    |
| xml_etree_parse                  | 106 ms                                                     | 107 ms: 1.02x slower                                                    |
| regex_effbot                     | 2.58 ms                                                    | 2.63 ms: 1.02x slower                                                   |
| logging_simple                   | 3.04 us                                                    | 3.10 us: 1.02x slower                                                   |
| pyflate                          | 321 ms                                                     | 327 ms: 1.02x slower                                                    |
| xml_etree_iterparse              | 71.5 ms                                                    | 72.9 ms: 1.02x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 337 ms: 1.02x slower                                                    |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.4 ms: 1.02x slower                                                   |
| logging_format                   | 3.31 us                                                    | 3.40 us: 1.03x slower                                                   |
| unpickle_list                    | 2.88 us                                                    | 2.96 us: 1.03x slower                                                   |
| async_tree_io                    | 563 ms                                                     | 582 ms: 1.03x slower                                                    |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 131 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 471 ms: 1.04x slower                                                    |
| dulwich_log                      | 27.6 ms                                                    | 28.8 ms: 1.05x slower                                                   |
| coroutines                       | 15.8 ms                                                    | 16.6 ms: 1.05x slower                                                   |
| async_generators                 | 281 ms                                                     | 295 ms: 1.05x slower                                                    |
| async_tree_eager                 | 60.3 ms                                                    | 63.4 ms: 1.05x slower                                                   |
| spectral_norm                    | 66.4 ms                                                    | 69.8 ms: 1.05x slower                                                   |
| scimark_fft                      | 181 ms                                                     | 191 ms: 1.06x slower                                                    |
| meteor_contest                   | 70.3 ms                                                    | 74.6 ms: 1.06x slower                                                   |
| bench_thread_pool                | 447 us                                                     | 475 us: 1.06x slower                                                    |
| pprint_safe_repr                 | 465 ms                                                     | 496 ms: 1.07x slower                                                    |
| fannkuch                         | 248 ms                                                     | 266 ms: 1.07x slower                                                    |
| pprint_pformat                   | 947 ms                                                     | 1.02 sec: 1.07x slower                                                  |
| pycparser                        | 632 ms                                                     | 683 ms: 1.08x slower                                                    |
| async_tree_none_tg               | 198 ms                                                     | 214 ms: 1.08x slower                                                    |
| scimark_monte_carlo              | 42.5 ms                                                    | 45.9 ms: 1.08x slower                                                   |
| async_tree_io_tg                 | 565 ms                                                     | 613 ms: 1.09x slower                                                    |
| html5lib                         | 31.2 ms                                                    | 34.0 ms: 1.09x slower                                                   |
| sympy_expand                     | 226 ms                                                     | 247 ms: 1.09x slower                                                    |
| crypto_pyaes                     | 49.5 ms                                                    | 54.1 ms: 1.09x slower                                                   |
| docutils                         | 1.44 sec                                                   | 1.58 sec: 1.10x slower                                                  |
| nbody                            | 59.6 ms                                                    | 65.5 ms: 1.10x slower                                                   |
| richards_super                   | 35.2 ms                                                    | 38.7 ms: 1.10x slower                                                   |
| generators                       | 22.9 ms                                                    | 25.2 ms: 1.10x slower                                                   |
| richards                         | 31.8 ms                                                    | 35.2 ms: 1.10x slower                                                   |
| regex_compile                    | 68.5 ms                                                    | 75.8 ms: 1.11x slower                                                   |
| nqueens                          | 52.2 ms                                                    | 58.2 ms: 1.11x slower                                                   |
| typing_runtime_protocols         | 87.6 us                                                    | 97.9 us: 1.12x slower                                                   |
| deltablue                        | 2.14 ms                                                    | 2.41 ms: 1.13x slower                                                   |
| sqlglot_normalize                | 166 ms                                                     | 186 ms: 1.13x slower                                                    |
| asyncio_tcp                      | 402 ms                                                     | 456 ms: 1.13x slower                                                    |
| 2to3                             | 161 ms                                                     | 183 ms: 1.14x slower                                                    |
| json_dumps                       | 6.23 ms                                                    | 7.14 ms: 1.15x slower                                                   |
| sympy_sum                        | 69.2 ms                                                    | 79.3 ms: 1.15x slower                                                   |
| sympy_str                        | 131 ms                                                     | 151 ms: 1.15x slower                                                    |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 3.19 ms: 1.15x slower                                                   |
| logging_silent                   | 60.1 ns                                                    | 69.9 ns: 1.16x slower                                                   |
| django_template                  | 19.4 ms                                                    | 22.8 ms: 1.17x slower                                                   |
| raytrace                         | 147 ms                                                     | 173 ms: 1.18x slower                                                    |
| sqlglot_parse                    | 732 us                                                     | 873 us: 1.19x slower                                                    |
| sqlglot_transpile                | 891 us                                                     | 1.07 ms: 1.20x slower                                                   |
| gc_traversal                     | 2.45 ms                                                    | 2.95 ms: 1.20x slower                                                   |
| python_startup_no_site           | 12.3 ms                                                    | 14.8 ms: 1.20x slower                                                   |
| sqlglot_optimize                 | 30.9 ms                                                    | 37.5 ms: 1.21x slower                                                   |
| sympy_integrate                  | 10.3 ms                                                    | 12.6 ms: 1.22x slower                                                   |
| genshi_text                      | 13.9 ms                                                    | 17.0 ms: 1.22x slower                                                   |
| hexiom                           | 4.06 ms                                                    | 4.95 ms: 1.22x slower                                                   |
| chaos                            | 34.0 ms                                                    | 41.8 ms: 1.23x slower                                                   |
| python_startup                   | 15.2 ms                                                    | 19.2 ms: 1.26x slower                                                   |
| comprehensions                   | 10.2 us                                                    | 12.9 us: 1.27x slower                                                   |
| bench_mp_pool                    | 47.2 ms                                                    | 61.8 ms: 1.31x slower                                                   |
| genshi_xml                       | 29.9 ms                                                    | 42.9 ms: 1.43x slower                                                   |
| create_gc_cycles                 | 897 us                                                     | 1.31 ms: 1.46x slower                                                   |
| pylint                           | 170 ms                                                     | 252 ms: 1.48x slower                                                    |
| Geometric mean                   | (ref)                                                      | 1.05x slower                                                            |

Benchmark hidden because not significant (5): async_tree_memoization_tg, unpickle, async_tree_eager_memoization, asyncio_tcp_ssl, tornado_http
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.19x
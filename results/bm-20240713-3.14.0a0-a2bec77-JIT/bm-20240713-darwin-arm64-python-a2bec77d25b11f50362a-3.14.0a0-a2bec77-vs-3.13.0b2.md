# Results vs. 3.13.0b2

- fork: python
- ref: a2bec77d25b11f50362a
- machine: darwin-arm64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.02x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 172 ms: 1.07x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.52 sec: 1.06x slower                                                |
| html5lib       | 31.2 ms                                                    | 32.7 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                      | 1.05x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg               | 198 ms                                                     | 175 ms: 1.13x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 233 ms: 1.11x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 509 ms: 1.11x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 698 ms: 1.10x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 193 ms: 1.08x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 527 ms: 1.07x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 736 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 453 ms: 1.03x faster                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.6 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 333 ms: 1.01x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 63.6 ms: 1.06x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.04x faster                                                          |

Benchmark hidden because not significant (5): async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 47.8 ms: 1.02x faster                                                 |
| pidigits       | 282 ms                                                     | 282 ms: 1.00x slower                                                  |
| nbody          | 59.6 ms                                                    | 64.2 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 17.3 ms: 1.00x slower                                                 |
| regex_effbot   | 2.58 ms                                                    | 2.59 ms: 1.00x slower                                                 |
| regex_dna      | 149 ms                                                     | 153 ms: 1.02x slower                                                  |
| regex_compile  | 68.5 ms                                                    | 73.7 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                      | 1.03x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.26 sec: 1.16x faster                                                |
| unpickle_pure_python | 141 us                                                     | 133 us: 1.06x faster                                                  |
| xml_etree_process    | 37.1 ms                                                    | 36.4 ms: 1.02x faster                                                 |
| pickle_pure_python   | 179 us                                                     | 175 us: 1.02x faster                                                  |
| json_dumps           | 6.23 ms                                                    | 6.27 ms: 1.01x slower                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 53.5 ms: 1.01x slower                                                 |
| json_loads           | 16.8 us                                                    | 17.3 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 15.4 ms: 1.02x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 12.8 ms: 1.04x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.03x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.51 ms: 1.07x faster                                                 |
| django_template | 19.4 ms                                                    | 21.4 ms: 1.10x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 16.3 ms: 1.17x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 40.0 ms: 1.34x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.13x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 22.6 us                                                    | 16.8 us: 1.34x faster                                                 |
| deepcopy                         | 204 us                                                     | 153 us: 1.33x faster                                                  |
| deepcopy_reduce                  | 1.82 us                                                    | 1.56 us: 1.17x faster                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.26 sec: 1.16x faster                                                |
| async_tree_none_tg               | 198 ms                                                     | 175 ms: 1.13x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 233 ms: 1.11x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 509 ms: 1.11x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 698 ms: 1.10x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 193 ms: 1.08x faster                                                  |
| mako                             | 6.99 ms                                                    | 6.51 ms: 1.07x faster                                                 |
| async_tree_io                    | 563 ms                                                     | 527 ms: 1.07x faster                                                  |
| mdp                              | 1.53 sec                                                   | 1.45 sec: 1.06x faster                                                |
| unpickle_pure_python             | 141 us                                                     | 133 us: 1.06x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 736 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 453 ms: 1.03x faster                                                  |
| xml_etree_process                | 37.1 ms                                                    | 36.4 ms: 1.02x faster                                                 |
| pickle_pure_python               | 179 us                                                     | 175 us: 1.02x faster                                                  |
| float                            | 48.6 ms                                                    | 47.8 ms: 1.02x faster                                                 |
| pyflate                          | 321 ms                                                     | 317 ms: 1.01x faster                                                  |
| richards                         | 31.8 ms                                                    | 31.5 ms: 1.01x faster                                                 |
| telco                            | 4.60 ms                                                    | 4.56 ms: 1.01x faster                                                 |
| thrift                           | 435 us                                                     | 432 us: 1.01x faster                                                  |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.28 sec: 1.01x faster                                                |
| fannkuch                         | 248 ms                                                     | 247 ms: 1.01x faster                                                  |
| pidigits                         | 282 ms                                                     | 282 ms: 1.00x slower                                                  |
| regex_v8                         | 17.3 ms                                                    | 17.3 ms: 1.00x slower                                                 |
| regex_effbot                     | 2.58 ms                                                    | 2.59 ms: 1.00x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.6 ms: 1.01x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.27 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 333 ms: 1.01x slower                                                  |
| go                               | 101 ms                                                     | 101 ms: 1.01x slower                                                  |
| logging_simple                   | 3.04 us                                                    | 3.07 us: 1.01x slower                                                 |
| create_gc_cycles                 | 897 us                                                     | 905 us: 1.01x slower                                                  |
| generators                       | 22.9 ms                                                    | 23.2 ms: 1.01x slower                                                 |
| xml_etree_generate               | 52.7 ms                                                    | 53.5 ms: 1.01x slower                                                 |
| coverage                         | 45.0 ms                                                    | 45.7 ms: 1.01x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 15.4 ms: 1.02x slower                                                 |
| dask                             | 221 ms                                                     | 225 ms: 1.02x slower                                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.11 sec: 1.02x slower                                                |
| coroutines                       | 15.8 ms                                                    | 16.2 ms: 1.02x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 61.5 ns: 1.02x slower                                                 |
| pathlib                          | 23.3 ms                                                    | 23.8 ms: 1.02x slower                                                 |
| regex_dna                        | 149 ms                                                     | 153 ms: 1.02x slower                                                  |
| logging_format                   | 3.31 us                                                    | 3.39 us: 1.02x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 71.9 ms: 1.02x slower                                                 |
| json_loads                       | 16.8 us                                                    | 17.3 us: 1.03x slower                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 480 ms: 1.03x slower                                                  |
| spectral_norm                    | 66.4 ms                                                    | 68.8 ms: 1.04x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 44.1 ms: 1.04x slower                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 12.8 ms: 1.04x slower                                                 |
| pprint_pformat                   | 947 ms                                                     | 988 ms: 1.04x slower                                                  |
| async_generators                 | 281 ms                                                     | 293 ms: 1.04x slower                                                  |
| html5lib                         | 31.2 ms                                                    | 32.7 ms: 1.05x slower                                                 |
| sympy_sum                        | 69.2 ms                                                    | 72.9 ms: 1.05x slower                                                 |
| sympy_str                        | 131 ms                                                     | 139 ms: 1.05x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 52.2 ms: 1.06x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 63.6 ms: 1.06x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 191 ms: 1.06x slower                                                  |
| docutils                         | 1.44 sec                                                   | 1.52 sec: 1.06x slower                                                |
| bench_mp_pool                    | 47.2 ms                                                    | 50.2 ms: 1.06x slower                                                 |
| gc_traversal                     | 2.45 ms                                                    | 2.61 ms: 1.06x slower                                                 |
| sqlglot_normalize                | 166 ms                                                     | 176 ms: 1.07x slower                                                  |
| sympy_integrate                  | 10.3 ms                                                    | 11.0 ms: 1.07x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 476 us: 1.07x slower                                                  |
| 2to3                             | 161 ms                                                     | 172 ms: 1.07x slower                                                  |
| sympy_expand                     | 226 ms                                                     | 241 ms: 1.07x slower                                                  |
| pycparser                        | 632 ms                                                     | 676 ms: 1.07x slower                                                  |
| sqlglot_optimize                 | 30.9 ms                                                    | 33.2 ms: 1.07x slower                                                 |
| scimark_sor                      | 94.9 ms                                                    | 102 ms: 1.08x slower                                                  |
| regex_compile                    | 68.5 ms                                                    | 73.7 ms: 1.08x slower                                                 |
| nbody                            | 59.6 ms                                                    | 64.2 ms: 1.08x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 94.6 us: 1.08x slower                                                 |
| deltablue                        | 2.14 ms                                                    | 2.33 ms: 1.09x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 4.42 ms: 1.09x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 3.03 ms: 1.09x slower                                                 |
| django_template                  | 19.4 ms                                                    | 21.4 ms: 1.10x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 57.8 ms: 1.11x slower                                                 |
| raytrace                         | 147 ms                                                     | 165 ms: 1.12x slower                                                  |
| sqlglot_transpile                | 891 us                                                     | 1.00 ms: 1.13x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 834 us: 1.14x slower                                                  |
| chaos                            | 34.0 ms                                                    | 39.3 ms: 1.16x slower                                                 |
| genshi_text                      | 13.9 ms                                                    | 16.3 ms: 1.17x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 12.3 us: 1.21x slower                                                 |
| scimark_lu                       | 66.9 ms                                                    | 82.8 ms: 1.24x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 40.0 ms: 1.34x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (13): async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, xml_etree_iterparse, json, asyncio_websockets, richards_super, async_tree_eager_cpu_io_mixed, xml_etree_parse, tornado_http, async_tree_memoization_tg, asyncio_tcp, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x
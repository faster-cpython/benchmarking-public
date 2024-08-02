# Results vs. 3.13.0b2

- fork: python
- ref: a2bec77d25b11f50362a
- machine: darwin-arm64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.00x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 1.44 sec                                                   | 1.46 sec: 1.01x slower                                                |
| html5lib       | 31.2 ms                                                    | 31.6 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg               | 198 ms                                                     | 176 ms: 1.12x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 232 ms: 1.12x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 509 ms: 1.11x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 698 ms: 1.10x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 194 ms: 1.08x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 711 ms: 1.08x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 534 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 454 ms: 1.03x faster                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.01x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 64.4 ms: 1.07x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.04x faster                                                          |

Benchmark hidden because not significant (5): async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, async_tree_eager_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 59.6 ms                                                    | 60.6 ms: 1.02x slower                                                 |
| float          | 48.6 ms                                                    | 50.1 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_compile, regex_effbot, regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 71.5 ms                                                    | 72.2 ms: 1.01x slower                                                 |
| unpickle_pure_python | 141 us                                                     | 143 us: 1.01x slower                                                  |
| tomli_loads          | 1.47 sec                                                   | 1.49 sec: 1.02x slower                                                |
| pickle_pure_python   | 179 us                                                     | 181 us: 1.02x slower                                                  |
| xml_etree_generate   | 52.7 ms                                                    | 53.8 ms: 1.02x slower                                                 |
| xml_etree_process    | 37.1 ms                                                    | 37.9 ms: 1.02x slower                                                 |
| json_loads           | 16.8 us                                                    | 17.2 us: 1.02x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 6.40 ms: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 15.6 ms: 1.03x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 12.7 ms: 1.03x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.03x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 13.9 ms                                                    | 14.1 ms: 1.01x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 30.3 ms: 1.01x slower                                                 |
| mako            | 6.99 ms                                                    | 7.14 ms: 1.02x slower                                                 |
| django_template | 19.4 ms                                                    | 19.9 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 145 us: 1.41x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 17.0 us: 1.33x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.50 us: 1.22x faster                                                 |
| async_tree_none_tg               | 198 ms                                                     | 176 ms: 1.12x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 232 ms: 1.12x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 509 ms: 1.11x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 698 ms: 1.10x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 194 ms: 1.08x faster                                                  |
| mdp                              | 1.53 sec                                                   | 1.42 sec: 1.08x faster                                                |
| async_tree_eager_io              | 766 ms                                                     | 711 ms: 1.08x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 534 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 454 ms: 1.03x faster                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                                  |
| deltablue                        | 2.14 ms                                                    | 2.11 ms: 1.02x faster                                                 |
| logging_silent                   | 60.1 ns                                                    | 59.4 ns: 1.01x faster                                                 |
| richards_super                   | 35.2 ms                                                    | 34.8 ms: 1.01x faster                                                 |
| richards                         | 31.8 ms                                                    | 31.6 ms: 1.01x faster                                                 |
| generators                       | 22.9 ms                                                    | 22.8 ms: 1.01x faster                                                 |
| go                               | 101 ms                                                     | 100 ms: 1.01x faster                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                 |
| create_gc_cycles                 | 897 us                                                     | 900 us: 1.00x slower                                                  |
| hexiom                           | 4.06 ms                                                    | 4.08 ms: 1.00x slower                                                 |
| pyflate                          | 321 ms                                                     | 322 ms: 1.00x slower                                                  |
| telco                            | 4.60 ms                                                    | 4.62 ms: 1.00x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.01x slower                                                  |
| coverage                         | 45.0 ms                                                    | 45.3 ms: 1.01x slower                                                 |
| pathlib                          | 23.3 ms                                                    | 23.5 ms: 1.01x slower                                                 |
| async_generators                 | 281 ms                                                     | 283 ms: 1.01x slower                                                  |
| thrift                           | 435 us                                                     | 438 us: 1.01x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 72.2 ms: 1.01x slower                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 10.5 ms: 1.01x slower                                                 |
| pycparser                        | 632 ms                                                     | 639 ms: 1.01x slower                                                  |
| genshi_text                      | 13.9 ms                                                    | 14.1 ms: 1.01x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.46 sec: 1.01x slower                                                |
| html5lib                         | 31.2 ms                                                    | 31.6 ms: 1.01x slower                                                 |
| json                             | 2.93 ms                                                    | 2.97 ms: 1.01x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 71.2 ms: 1.01x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 30.3 ms: 1.01x slower                                                 |
| unpickle_pure_python             | 141 us                                                     | 143 us: 1.01x slower                                                  |
| scimark_sor                      | 94.9 ms                                                    | 96.3 ms: 1.02x slower                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.49 sec: 1.02x slower                                                |
| pickle_pure_python               | 179 us                                                     | 181 us: 1.02x slower                                                  |
| nbody                            | 59.6 ms                                                    | 60.6 ms: 1.02x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 906 us: 1.02x slower                                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.11 sec: 1.02x slower                                                |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.5 ms: 1.02x slower                                                 |
| sqlglot_normalize                | 166 ms                                                     | 169 ms: 1.02x slower                                                  |
| bench_thread_pool                | 447 us                                                     | 455 us: 1.02x slower                                                  |
| sqlglot_parse                    | 732 us                                                     | 746 us: 1.02x slower                                                  |
| sympy_sum                        | 69.2 ms                                                    | 70.6 ms: 1.02x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 50.5 ms: 1.02x slower                                                 |
| logging_simple                   | 3.04 us                                                    | 3.10 us: 1.02x slower                                                 |
| xml_etree_generate               | 52.7 ms                                                    | 53.8 ms: 1.02x slower                                                 |
| xml_etree_process                | 37.1 ms                                                    | 37.9 ms: 1.02x slower                                                 |
| mako                             | 6.99 ms                                                    | 7.14 ms: 1.02x slower                                                 |
| json_loads                       | 16.8 us                                                    | 17.2 us: 1.02x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 68.0 ms: 1.02x slower                                                 |
| logging_format                   | 3.31 us                                                    | 3.39 us: 1.02x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 231 ms: 1.02x slower                                                  |
| bench_mp_pool                    | 47.2 ms                                                    | 48.4 ms: 1.02x slower                                                 |
| raytrace                         | 147 ms                                                     | 151 ms: 1.03x slower                                                  |
| sympy_str                        | 131 ms                                                     | 135 ms: 1.03x slower                                                  |
| django_template                  | 19.4 ms                                                    | 19.9 ms: 1.03x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.40 ms: 1.03x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 15.6 ms: 1.03x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.7 ms: 1.03x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 16.3 ms: 1.03x slower                                                 |
| float                            | 48.6 ms                                                    | 50.1 ms: 1.03x slower                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 12.7 ms: 1.03x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 54.2 ms: 1.04x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 189 ms: 1.05x slower                                                  |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.91 ms: 1.05x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 91.9 us: 1.05x slower                                                 |
| fannkuch                         | 248 ms                                                     | 261 ms: 1.05x slower                                                  |
| comprehensions                   | 10.2 us                                                    | 10.7 us: 1.05x slower                                                 |
| scimark_lu                       | 66.9 ms                                                    | 70.8 ms: 1.06x slower                                                 |
| chaos                            | 34.0 ms                                                    | 36.1 ms: 1.06x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 64.4 ms: 1.07x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (20): async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, dask, async_tree_eager_cpu_io_mixed, regex_compile, pprint_safe_repr, regex_effbot, asyncio_websockets, pidigits, regex_v8, regex_dna, pprint_pformat, async_tree_eager_tg, 2to3, tornado_http, async_tree_memoization_tg, xml_etree_parse, pylint, asyncio_tcp
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x
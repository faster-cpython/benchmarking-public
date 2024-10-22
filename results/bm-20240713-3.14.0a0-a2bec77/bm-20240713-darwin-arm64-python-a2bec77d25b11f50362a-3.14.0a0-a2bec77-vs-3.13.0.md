# Results vs. 3.13.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: darwin-arm64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 6.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 161 ms: 1.10x faster                                                  |
| docutils       | 1.44 sec                                               | 1.46 sec: 1.01x slower                                                |
| html5lib       | 36.6 ms                                                | 31.6 ms: 1.16x faster                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 241 ms: 1.20x faster                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 41.4 ms: 1.17x faster                                                 |
| async_tree_memoization           | 270 ms                                                 | 232 ms: 1.17x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 149 ms: 1.14x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 176 ms: 1.13x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 123 ms: 1.13x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 412 ms: 1.11x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 194 ms: 1.09x faster                                                  |
| async_tree_eager                 | 70.5 ms                                                | 64.4 ms: 1.09x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 357 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 332 ms: 1.05x faster                                                  |
| async_generators                 | 294 ms                                                 | 283 ms: 1.04x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                |
| async_tree_io                    | 507 ms                                                 | 534 ms: 1.05x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 711 ms: 1.39x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 698 ms: 1.47x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 409 ms: 1.70x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 60.6 ms: 1.22x faster                                                 |
| float          | 56.2 ms                                                | 50.1 ms: 1.12x faster                                                 |
| pidigits       | 284 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 68.5 ms: 1.15x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.59 ms: 1.02x faster                                                 |
| regex_dna      | 148 ms                                                 | 149 ms: 1.01x slower                                                  |
| regex_v8       | 16.9 ms                                                | 17.3 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 181 us: 1.17x faster                                                  |
| unpickle_pure_python | 163 us                                                 | 143 us: 1.14x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 37.9 ms: 1.08x faster                                                 |
| xml_etree_generate   | 56.6 ms                                                | 53.8 ms: 1.05x faster                                                 |
| tomli_loads          | 1.56 sec                                               | 1.49 sec: 1.05x faster                                                |
| xml_etree_iterparse  | 74.2 ms                                                | 72.2 ms: 1.03x faster                                                 |
| json_dumps           | 6.56 ms                                                | 6.40 ms: 1.02x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 107 ms: 1.02x faster                                                  |
| json_loads           | 16.9 us                                                | 17.2 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 15.6 ms: 1.09x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 12.7 ms: 1.07x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.1 ms: 1.20x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 30.3 ms: 1.13x faster                                                 |
| django_template | 22.2 ms                                                | 19.9 ms: 1.11x faster                                                 |
| mako            | 7.68 ms                                                | 7.14 ms: 1.08x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 232 us                                                 | 145 us: 1.60x faster                                                  |
| deepcopy_memo                    | 27.2 us                                                | 17.0 us: 1.60x faster                                                 |
| generators                       | 31.5 ms                                                | 22.8 ms: 1.38x faster                                                 |
| deepcopy_reduce                  | 2.06 us                                                | 1.50 us: 1.38x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.11 ms: 1.27x faster                                                 |
| nbody                            | 73.9 ms                                                | 60.6 ms: 1.22x faster                                                 |
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                                 |
| raytrace                         | 182 ms                                                 | 151 ms: 1.20x faster                                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 241 ms: 1.20x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 14.1 ms: 1.20x faster                                                 |
| hexiom                           | 4.85 ms                                                | 4.08 ms: 1.19x faster                                                 |
| logging_silent                   | 69.9 ns                                                | 59.4 ns: 1.18x faster                                                 |
| pickle_pure_python               | 213 us                                                 | 181 us: 1.17x faster                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 41.4 ms: 1.17x faster                                                 |
| async_tree_memoization           | 270 ms                                                 | 232 ms: 1.17x faster                                                  |
| html5lib                         | 36.6 ms                                                | 31.6 ms: 1.16x faster                                                 |
| nqueens                          | 62.9 ms                                                | 54.2 ms: 1.16x faster                                                 |
| dask                             | 255 ms                                                 | 221 ms: 1.16x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 43.7 ms: 1.15x faster                                                 |
| logging_simple                   | 3.57 us                                                | 3.10 us: 1.15x faster                                                 |
| go                               | 115 ms                                                 | 100 ms: 1.15x faster                                                  |
| sqlglot_parse                    | 856 us                                                 | 746 us: 1.15x faster                                                  |
| regex_compile                    | 78.5 ms                                                | 68.5 ms: 1.15x faster                                                 |
| unpickle_pure_python             | 163 us                                                 | 143 us: 1.14x faster                                                  |
| chaos                            | 41.3 ms                                                | 36.1 ms: 1.14x faster                                                 |
| pprint_safe_repr                 | 531 ms                                                 | 465 ms: 1.14x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 948 ms: 1.14x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.39 us: 1.14x faster                                                 |
| spectral_norm                    | 77.3 ms                                                | 68.0 ms: 1.14x faster                                                 |
| comprehensions                   | 12.2 us                                                | 10.7 us: 1.14x faster                                                 |
| async_tree_eager_memoization     | 169 ms                                                 | 149 ms: 1.14x faster                                                  |
| genshi_xml                       | 34.4 ms                                                | 30.3 ms: 1.13x faster                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 906 us: 1.13x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 176 ms: 1.13x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 123 ms: 1.13x faster                                                  |
| richards_super                   | 39.1 ms                                                | 34.8 ms: 1.12x faster                                                 |
| float                            | 56.2 ms                                                | 50.1 ms: 1.12x faster                                                 |
| richards                         | 35.4 ms                                                | 31.6 ms: 1.12x faster                                                 |
| sqlglot_normalize                | 189 ms                                                 | 169 ms: 1.12x faster                                                  |
| django_template                  | 22.2 ms                                                | 19.9 ms: 1.11x faster                                                 |
| bench_thread_pool                | 506 us                                                 | 455 us: 1.11x faster                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 31.5 ms: 1.11x faster                                                 |
| asyncio_tcp                      | 457 ms                                                 | 412 ms: 1.11x faster                                                  |
| pycparser                        | 706 ms                                                 | 639 ms: 1.10x faster                                                  |
| 2to3                             | 178 ms                                                 | 161 ms: 1.10x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 91.9 us: 1.10x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 96.3 ms: 1.10x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 194 ms: 1.09x faster                                                  |
| async_tree_eager                 | 70.5 ms                                                | 64.4 ms: 1.09x faster                                                 |
| python_startup                   | 17.0 ms                                                | 15.6 ms: 1.09x faster                                                 |
| pyflate                          | 351 ms                                                 | 322 ms: 1.09x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.5 ms: 1.08x faster                                                 |
| scimark_lu                       | 76.5 ms                                                | 70.8 ms: 1.08x faster                                                 |
| fannkuch                         | 282 ms                                                 | 261 ms: 1.08x faster                                                  |
| xml_etree_process                | 40.9 ms                                                | 37.9 ms: 1.08x faster                                                 |
| sympy_str                        | 145 ms                                                 | 135 ms: 1.08x faster                                                  |
| mako                             | 7.68 ms                                                | 7.14 ms: 1.08x faster                                                 |
| python_startup_no_site           | 13.7 ms                                                | 12.7 ms: 1.07x faster                                                 |
| sympy_sum                        | 75.6 ms                                                | 70.6 ms: 1.07x faster                                                 |
| crypto_pyaes                     | 54.0 ms                                                | 50.5 ms: 1.07x faster                                                 |
| sympy_expand                     | 246 ms                                                 | 231 ms: 1.07x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 189 ms: 1.06x faster                                                  |
| thrift                           | 466 us                                                 | 438 us: 1.06x faster                                                  |
| mdp                              | 1.50 sec                                               | 1.42 sec: 1.06x faster                                                |
| bench_mp_pool                    | 50.9 ms                                                | 48.4 ms: 1.05x faster                                                 |
| xml_etree_generate               | 56.6 ms                                                | 53.8 ms: 1.05x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 357 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 332 ms: 1.05x faster                                                  |
| tomli_loads                      | 1.56 sec                                               | 1.49 sec: 1.05x faster                                                |
| bpe_tokeniser                    | 3.24 sec                                               | 3.11 sec: 1.04x faster                                                |
| async_generators                 | 294 ms                                                 | 283 ms: 1.04x faster                                                  |
| telco                            | 4.80 ms                                                | 4.62 ms: 1.04x faster                                                 |
| meteor_contest                   | 73.8 ms                                                | 71.2 ms: 1.04x faster                                                 |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.91 ms: 1.03x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 72.2 ms: 1.03x faster                                                 |
| json_dumps                       | 6.56 ms                                                | 6.40 ms: 1.02x faster                                                 |
| xml_etree_parse                  | 109 ms                                                 | 107 ms: 1.02x faster                                                  |
| coverage                         | 46.1 ms                                                | 45.3 ms: 1.02x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.59 ms: 1.02x faster                                                 |
| gc_traversal                     | 2.48 ms                                                | 2.46 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 282 ms: 1.00x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.46 sec: 1.01x slower                                                |
| json                             | 2.94 ms                                                | 2.97 ms: 1.01x slower                                                 |
| regex_dna                        | 148 ms                                                 | 149 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                |
| regex_v8                         | 16.9 ms                                                | 17.3 ms: 1.02x slower                                                 |
| json_loads                       | 16.9 us                                                | 17.2 us: 1.02x slower                                                 |
| pathlib                          | 22.8 ms                                                | 23.5 ms: 1.03x slower                                                 |
| async_tree_io                    | 507 ms                                                 | 534 ms: 1.05x slower                                                  |
| create_gc_cycles                 | 803 us                                                 | 900 us: 1.12x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 711 ms: 1.39x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 698 ms: 1.47x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 409 ms: 1.70x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (5): tornado_http, pylint, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io_tg
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 6.12x
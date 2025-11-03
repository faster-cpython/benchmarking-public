# Results vs. 3.13.0

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: windows-amd64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.059x faster
- HPT reliability: 91.81%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                      |
| html5lib       | 38.2 ms                                                     | 37.2 ms: 1.03x faster                                                       |
| sphinx         | 617 ms                                                      | 629 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 149 ms: 2.01x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 191 ms: 1.47x faster                                                        |
| async_tree_io              | 513 ms                                                      | 371 ms: 1.38x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 198 ms: 1.34x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 374 ms: 1.33x faster                                                        |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.30x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 159 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 321 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 338 ms: 1.13x faster                                                        |
| async_generators           | 223 ms                                                      | 233 ms: 1.05x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.26x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.3 ms: 1.15x faster                                                       |
| pidigits       | 146 ms                                                      | 144 ms: 1.02x faster                                                        |
| nbody          | 66.3 ms                                                     | 65.2 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.5 ms: 1.65x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.57 ms: 1.08x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 81.7 ms: 1.01x slower                                                       |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 6.19 ms                                                     | 5.54 ms: 1.12x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.2 us: 1.06x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 88.5 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 59.4 ms: 1.02x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 134 us: 1.03x slower                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 55.4 ms: 1.04x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 38.9 ms: 1.07x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 215 us: 1.16x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.73 ms: 1.03x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 15.8 ms: 1.04x slower                                                       |
| django_template | 20.3 ms                                                     | 23.9 ms: 1.18x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 506 us: 16.72x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 28.8 ms: 2.61x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 149 ms: 2.01x faster                                                        |
| mdp                        | 1.43 sec                                                    | 826 ms: 1.73x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 14.5 ms: 1.65x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 191 ms: 1.47x faster                                                        |
| async_tree_io              | 513 ms                                                      | 371 ms: 1.38x faster                                                        |
| deepcopy                   | 223 us                                                      | 165 us: 1.36x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 198 ms: 1.34x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 17.2 us: 1.34x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 374 ms: 1.33x faster                                                        |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.30x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 159 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 321 ms: 1.18x faster                                                        |
| float                      | 50.8 ms                                                     | 44.3 ms: 1.15x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.77 us: 1.14x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.26 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 338 ms: 1.13x faster                                                        |
| json                       | 3.30 ms                                                     | 2.92 ms: 1.13x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.54 ms: 1.12x faster                                                       |
| go                         | 84.7 ms                                                     | 77.3 ms: 1.10x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.40 ms: 1.09x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.57 ms: 1.08x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.59 sec: 1.07x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.06x faster                                                       |
| scimark_fft                | 175 ms                                                      | 167 ms: 1.05x faster                                                        |
| xml_etree_parse            | 92.2 ms                                                     | 88.5 ms: 1.04x faster                                                       |
| html5lib                   | 38.2 ms                                                     | 37.2 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 59.4 ms: 1.02x faster                                                       |
| pidigits                   | 146 ms                                                      | 144 ms: 1.02x faster                                                        |
| nbody                      | 66.3 ms                                                     | 65.2 ms: 1.02x faster                                                       |
| typing_runtime_protocols   | 103 us                                                      | 102 us: 1.01x faster                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.0 ms: 1.01x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 488 ms: 1.01x slower                                                        |
| regex_compile              | 80.7 ms                                                     | 81.7 ms: 1.01x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.01x slower                                                       |
| sympy_expand               | 286 ms                                                      | 290 ms: 1.01x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 73.1 ms: 1.02x slower                                                       |
| pyflate                    | 283 ms                                                      | 288 ms: 1.02x slower                                                        |
| spectral_norm              | 63.4 ms                                                     | 64.5 ms: 1.02x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                      |
| sphinx                     | 617 ms                                                      | 629 ms: 1.02x slower                                                        |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                        |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                                        |
| pprint_pformat             | 977 ms                                                      | 997 ms: 1.02x slower                                                        |
| shortest_path              | 355 ms                                                      | 364 ms: 1.02x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 56.0 ns: 1.03x slower                                                       |
| mako                       | 6.56 ms                                                     | 6.73 ms: 1.03x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 87.4 ms: 1.03x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 41.3 ms: 1.03x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 134 us: 1.03x slower                                                        |
| xml_etree_generate         | 53.5 ms                                                     | 55.4 ms: 1.04x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.8 ms: 1.04x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.98 sec: 1.04x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.8 ms: 1.04x slower                                                       |
| connected_components       | 320 ms                                                      | 334 ms: 1.04x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.05 us: 1.05x slower                                                       |
| async_generators           | 223 ms                                                      | 233 ms: 1.05x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 47.8 ms: 1.05x slower                                                       |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| python_startup             | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 59.9 ms: 1.06x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.54 us: 1.06x slower                                                       |
| richards_super             | 29.8 ms                                                     | 31.6 ms: 1.06x slower                                                       |
| richards                   | 26.3 ms                                                     | 28.0 ms: 1.06x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 38.9 ms: 1.07x slower                                                       |
| chaos                      | 37.9 ms                                                     | 40.4 ms: 1.07x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.10 ms: 1.07x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.31 ms: 1.07x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 869 us: 1.07x slower                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 90.9 ms: 1.08x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.2 us: 1.08x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.18 ms: 1.09x slower                                                       |
| fannkuch                   | 252 ms                                                      | 274 ms: 1.09x slower                                                        |
| coverage                   | 45.3 ms                                                     | 49.9 ms: 1.10x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 63.6 ms: 1.13x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 215 us: 1.16x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                       |
| raytrace                   | 153 ms                                                      | 179 ms: 1.17x slower                                                        |
| django_template            | 20.3 ms                                                     | 23.9 ms: 1.18x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.23 ms: 1.18x slower                                                       |
| many_optionals             | 361 us                                                      | 561 us: 1.55x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 31.5 ms: 2.90x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (5): pylint, sqlite_synth, pycparser, scimark_sor, genshi_xml
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.059x faster

# HPT report

- Reliability score: 91.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
# Results vs. 3.13.0

- fork: python
- ref: 3f2cfd0462e13368092a
- machine: windows-amd64
- commit hash: 3f2cfd0
- commit date: 2025-01-25
- overall geometric mean: 1.012x faster
- HPT reliability: 61.63%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 231 ms: 1.07x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.76 sec: 1.15x slower                                                      |
| html5lib       | 38.2 ms                                                     | 40.4 ms: 1.06x slower                                                       |
| sphinx         | 617 ms                                                      | 686 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                       | 1.10x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 218 ms: 1.29x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 412 ms: 1.20x faster                                                        |
| async_tree_io              | 513 ms                                                      | 426 ms: 1.20x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 226 ms: 1.17x faster                                                        |
| async_tree_none            | 219 ms                                                      | 190 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 177 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 345 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 348 ms: 1.10x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 312 ms: 1.04x slower                                                        |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 40.4 ms: 1.26x faster                                                       |
| nbody          | 66.3 ms                                                     | 55.9 ms: 1.18x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 15.1 ms: 1.58x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.48 ms: 1.14x faster                                                       |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 84.6 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 112 us: 1.16x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.21 sec: 1.13x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 50.2 ms: 1.07x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 88.5 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 60.0 ms: 1.01x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 36.8 ms: 1.01x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.27 ms: 1.01x slower                                                       |
| json_loads           | 15.1 us                                                     | 16.0 us: 1.06x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 213 us: 1.15x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 24.1 ms: 1.01x faster                                                       |
| python_startup_no_site | 16.9 ms                                                     | 17.8 ms: 1.06x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.09 ms: 1.29x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 19.5 ms: 1.28x slower                                                       |
| django_template | 20.3 ms                                                     | 27.4 ms: 1.35x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 47.3 ms: 1.40x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.17x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 544 us: 15.58x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 15.1 ms: 1.58x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 17.1 us: 1.35x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.09 ms: 1.29x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 218 ms: 1.29x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 49.2 ms: 1.29x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.04 ms: 1.28x faster                                                       |
| float                      | 50.8 ms                                                     | 40.4 ms: 1.26x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 63.2 ms: 1.21x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 412 ms: 1.20x faster                                                        |
| async_tree_io              | 513 ms                                                      | 426 ms: 1.20x faster                                                        |
| scimark_fft                | 175 ms                                                      | 146 ms: 1.20x faster                                                        |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                                        |
| nbody                      | 66.3 ms                                                     | 55.9 ms: 1.18x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 226 ms: 1.17x faster                                                        |
| unpickle_pure_python       | 130 us                                                      | 112 us: 1.16x faster                                                        |
| async_tree_none            | 219 ms                                                      | 190 ms: 1.15x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.48 ms: 1.14x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 177 ms: 1.13x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.21 sec: 1.13x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.34 ms: 1.12x faster                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 41.1 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 345 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 348 ms: 1.10x faster                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.64 sec: 1.09x faster                                                      |
| json                       | 3.30 ms                                                     | 3.04 ms: 1.09x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.89 us: 1.07x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 50.2 ms: 1.07x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 38.3 ms: 1.06x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.62 sec: 1.05x faster                                                      |
| fannkuch                   | 252 ms                                                      | 241 ms: 1.04x faster                                                        |
| xml_etree_parse            | 92.2 ms                                                     | 88.5 ms: 1.04x faster                                                       |
| connected_components       | 320 ms                                                      | 311 ms: 1.03x faster                                                        |
| shortest_path              | 355 ms                                                      | 347 ms: 1.02x faster                                                        |
| pyflate                    | 283 ms                                                      | 277 ms: 1.02x faster                                                        |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                        |
| python_startup             | 24.4 ms                                                     | 24.1 ms: 1.01x faster                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 60.0 ms: 1.01x faster                                                       |
| pprint_pformat             | 977 ms                                                      | 970 ms: 1.01x faster                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.58 us: 1.01x faster                                                       |
| scimark_lu                 | 56.7 ms                                                     | 56.9 ms: 1.00x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 36.8 ms: 1.01x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.27 ms: 1.01x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 312 ms: 1.04x slower                                                        |
| bench_thread_pool          | 810 us                                                      | 842 us: 1.04x slower                                                        |
| pathlib                    | 75.3 ms                                                     | 78.5 ms: 1.04x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 84.6 ms: 1.05x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 88.4 ms: 1.05x slower                                                       |
| coverage                   | 45.3 ms                                                     | 47.7 ms: 1.05x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 17.8 ms: 1.06x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 40.4 ms: 1.06x slower                                                       |
| pycparser                  | 695 ms                                                      | 736 ms: 1.06x slower                                                        |
| json_loads                 | 15.1 us                                                     | 16.0 us: 1.06x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 76.8 ms: 1.07x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.53 sec: 1.07x slower                                                      |
| 2to3                       | 215 ms                                                      | 231 ms: 1.07x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 43.1 ms: 1.08x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 112 us: 1.08x slower                                                        |
| sympy_expand               | 286 ms                                                      | 311 ms: 1.09x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 59.4 ns: 1.09x slower                                                       |
| sympy_str                  | 167 ms                                                      | 182 ms: 1.09x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 93.1 ms: 1.09x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.6 ms: 1.10x slower                                                       |
| chaos                      | 37.9 ms                                                     | 42.0 ms: 1.11x slower                                                       |
| sphinx                     | 617 ms                                                      | 686 ms: 1.11x slower                                                        |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                        |
| logging_format             | 6.18 us                                                     | 6.92 us: 1.12x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.48 us: 1.12x slower                                                       |
| go                         | 84.7 ms                                                     | 95.4 ms: 1.13x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 63.7 ms: 1.14x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 869 us: 1.14x slower                                                        |
| comprehensions             | 10.4 us                                                     | 11.9 us: 1.15x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 213 us: 1.15x slower                                                        |
| docutils                   | 1.53 sec                                                    | 1.76 sec: 1.15x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.11 ms: 1.17x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 38.5 ms: 1.18x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 208 ms: 1.21x slower                                                        |
| many_optionals             | 361 us                                                      | 456 us: 1.26x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.42 ms: 1.28x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 19.5 ms: 1.28x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 5.05 ms: 1.32x slower                                                       |
| generators                 | 19.0 ms                                                     | 25.0 ms: 1.32x slower                                                       |
| django_template            | 20.3 ms                                                     | 27.4 ms: 1.35x slower                                                       |
| richards_super             | 29.8 ms                                                     | 40.6 ms: 1.36x slower                                                       |
| richards                   | 26.3 ms                                                     | 35.9 ms: 1.37x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 47.3 ms: 1.40x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 15.9 ms: 1.47x slower                                                       |
| raytrace                   | 153 ms                                                      | 228 ms: 1.49x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (5): create_gc_cycles, pidigits, pprint_safe_repr, gc_traversal, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250125-3.14.0a4+-3f2cfd0-JIT/bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.012x faster

# HPT report

- Reliability score: 61.63% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
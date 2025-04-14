# Results vs. 3.13.0

- fork: python
- ref: b3c18bfd828ba90b9c71
- machine: windows-amd64
- commit hash: b3c18bf
- commit date: 2025-03-03
- overall geometric mean: 1.011x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 230 ms: 1.07x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.73 sec: 1.13x slower                                                      |
| html5lib       | 38.2 ms                                                     | 40.9 ms: 1.07x slower                                                       |
| sphinx         | 617 ms                                                      | 650 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                        |
| async_tree_io              | 513 ms                                                      | 418 ms: 1.23x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 411 ms: 1.21x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 219 ms: 1.21x faster                                                        |
| async_tree_none            | 219 ms                                                      | 187 ms: 1.17x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 178 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 343 ms: 1.11x faster                                                        |
| async_generators           | 223 ms                                                      | 224 ms: 1.01x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 325 ms: 1.08x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 47.4 ms: 1.07x faster                                                       |
| pidigits       | 146 ms                                                      | 154 ms: 1.05x slower                                                        |
| nbody          | 66.3 ms                                                     | 73.5 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.9 ms: 1.60x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.50 ms: 1.13x faster                                                       |
| regex_dna      | 115 ms                                                      | 118 ms: 1.03x slower                                                        |
| regex_compile  | 80.7 ms                                                     | 87.3 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.8 us: 1.02x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 91.0 ms: 1.01x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.8 ms: 1.07x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 58.6 ms: 1.10x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.90 ms: 1.11x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 41.3 ms: 1.13x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 154 us: 1.18x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 234 us: 1.26x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.0 ms: 1.18x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 36.0 ms: 1.06x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 16.5 ms: 1.09x slower                                                       |
| mako            | 6.56 ms                                                     | 7.17 ms: 1.09x slower                                                       |
| django_template | 20.3 ms                                                     | 25.6 ms: 1.26x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.12x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 512 us: 16.54x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 32.0 ms: 2.35x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.9 ms: 1.60x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                        |
| async_tree_io              | 513 ms                                                      | 418 ms: 1.23x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 411 ms: 1.21x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 219 ms: 1.21x faster                                                        |
| deepcopy                   | 223 us                                                      | 191 us: 1.17x faster                                                        |
| async_tree_none            | 219 ms                                                      | 187 ms: 1.17x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.50 ms: 1.13x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 178 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 343 ms: 1.11x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 21.0 us: 1.10x faster                                                       |
| float                      | 50.8 ms                                                     | 47.4 ms: 1.07x faster                                                       |
| json                       | 3.30 ms                                                     | 3.10 ms: 1.07x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 60.0 ms: 1.06x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.8 us: 1.02x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.99 us: 1.02x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 91.0 ms: 1.01x faster                                                       |
| async_generators           | 223 ms                                                      | 224 ms: 1.01x slower                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.60 us: 1.01x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.24 ms: 1.01x slower                                                       |
| telco                      | 4.85 ms                                                     | 4.90 ms: 1.01x slower                                                       |
| shortest_path              | 355 ms                                                      | 361 ms: 1.02x slower                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.67 ms: 1.02x slower                                                       |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.03x slower                                                        |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                       |
| k_core                     | 1.70 sec                                                    | 1.75 sec: 1.03x slower                                                      |
| connected_components       | 320 ms                                                      | 331 ms: 1.04x slower                                                        |
| coverage                   | 45.3 ms                                                     | 47.0 ms: 1.04x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 87.5 ms: 1.04x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.99 sec: 1.04x slower                                                      |
| sympy_expand               | 286 ms                                                      | 297 ms: 1.04x slower                                                        |
| pidigits                   | 146 ms                                                      | 154 ms: 1.05x slower                                                        |
| go                         | 84.7 ms                                                     | 88.9 ms: 1.05x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 89.5 ms: 1.05x slower                                                       |
| sphinx                     | 617 ms                                                      | 650 ms: 1.05x slower                                                        |
| sympy_str                  | 167 ms                                                      | 176 ms: 1.06x slower                                                        |
| gc_traversal               | 1.96 ms                                                     | 2.07 ms: 1.06x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 109 us: 1.06x slower                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 36.0 ms: 1.06x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 863 us: 1.07x slower                                                        |
| 2to3                       | 215 ms                                                      | 230 ms: 1.07x slower                                                        |
| python_startup             | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 40.9 ms: 1.07x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.8 ms: 1.07x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 77.6 ms: 1.08x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 87.3 ms: 1.08x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 43.4 ms: 1.08x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 325 ms: 1.08x slower                                                        |
| pycparser                  | 695 ms                                                      | 755 ms: 1.09x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 16.5 ms: 1.09x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 35.4 ms: 1.09x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.09x slower                                                       |
| mako                       | 6.56 ms                                                     | 7.17 ms: 1.09x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 58.6 ms: 1.10x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.57 sec: 1.10x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.4 us: 1.10x slower                                                       |
| chaos                      | 37.9 ms                                                     | 41.7 ms: 1.10x slower                                                       |
| scimark_fft                | 175 ms                                                      | 193 ms: 1.11x slower                                                        |
| nbody                      | 66.3 ms                                                     | 73.5 ms: 1.11x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 50.6 ms: 1.11x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.90 ms: 1.11x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 62.8 ms: 1.12x slower                                                       |
| pyflate                    | 283 ms                                                      | 317 ms: 1.12x slower                                                        |
| docutils                   | 1.53 sec                                                    | 1.73 sec: 1.13x slower                                                      |
| fannkuch                   | 252 ms                                                      | 285 ms: 1.13x slower                                                        |
| xml_etree_process          | 36.5 ms                                                     | 41.3 ms: 1.13x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.54 us: 1.13x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 196 ms: 1.14x slower                                                        |
| hexiom                     | 3.84 ms                                                     | 4.40 ms: 1.14x slower                                                       |
| logging_format             | 6.18 us                                                     | 7.09 us: 1.15x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.10 ms: 1.15x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 63.0 ns: 1.15x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.13 sec: 1.16x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 561 ms: 1.16x slower                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 47.2 ms: 1.16x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 887 us: 1.16x slower                                                        |
| scimark_sor                | 76.2 ms                                                     | 89.9 ms: 1.18x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.0 ms: 1.18x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 67.2 ms: 1.18x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 154 us: 1.18x slower                                                        |
| richards                   | 26.3 ms                                                     | 31.3 ms: 1.19x slower                                                       |
| richards_super             | 29.8 ms                                                     | 35.5 ms: 1.19x slower                                                       |
| many_optionals             | 361 us                                                      | 435 us: 1.20x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.31 ms: 1.22x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 234 us: 1.26x slower                                                        |
| django_template            | 20.3 ms                                                     | 25.6 ms: 1.26x slower                                                       |
| raytrace                   | 153 ms                                                      | 195 ms: 1.27x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.4 ms: 1.51x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.011x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown
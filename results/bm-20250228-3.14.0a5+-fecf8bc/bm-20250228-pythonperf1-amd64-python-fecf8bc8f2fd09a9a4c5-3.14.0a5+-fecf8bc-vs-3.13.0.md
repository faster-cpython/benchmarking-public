# Results vs. 3.13.0

- fork: python
- ref: fecf8bc8f2fd09a9a4c5
- machine: windows-amd64
- commit hash: fecf8bc
- commit date: 2025-02-28
- overall geometric mean: 1.005x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 227 ms: 1.05x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                      |
| html5lib       | 38.2 ms                                                     | 40.2 ms: 1.05x slower                                                       |
| sphinx         | 617 ms                                                      | 646 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 398 ms: 1.25x faster                                                        |
| async_tree_io              | 513 ms                                                      | 417 ms: 1.23x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 217 ms: 1.22x faster                                                        |
| async_tree_none            | 219 ms                                                      | 185 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 174 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 339 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 340 ms: 1.12x faster                                                        |
| async_generators           | 223 ms                                                      | 221 ms: 1.01x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 314 ms: 1.05x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.2 ms: 1.10x faster                                                       |
| pidigits       | 146 ms                                                      | 150 ms: 1.03x slower                                                        |
| nbody          | 66.3 ms                                                     | 72.7 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.9 ms: 1.60x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.48 ms: 1.15x faster                                                       |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                                        |
| regex_compile  | 80.7 ms                                                     | 86.9 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.6 us: 1.04x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 89.1 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.0 ms: 1.03x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.42 sec: 1.03x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 57.2 ms: 1.07x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.76 ms: 1.09x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 40.3 ms: 1.11x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 150 us: 1.16x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 227 us: 1.22x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.0 ms: 1.03x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.68 ms: 1.02x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 37.3 ms: 1.10x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 17.1 ms: 1.12x slower                                                       |
| django_template | 20.3 ms                                                     | 25.2 ms: 1.24x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.12x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 512 us: 16.54x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 31.8 ms: 2.37x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.9 ms: 1.60x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 398 ms: 1.25x faster                                                        |
| async_tree_io              | 513 ms                                                      | 417 ms: 1.23x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 217 ms: 1.22x faster                                                        |
| deepcopy                   | 223 us                                                      | 184 us: 1.22x faster                                                        |
| async_tree_none            | 219 ms                                                      | 185 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 174 ms: 1.15x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.48 ms: 1.15x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 20.3 us: 1.14x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 339 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 340 ms: 1.12x faster                                                        |
| float                      | 50.8 ms                                                     | 46.2 ms: 1.10x faster                                                       |
| json                       | 3.30 ms                                                     | 3.13 ms: 1.06x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.92 us: 1.06x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.6 us: 1.04x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 61.3 ms: 1.03x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 89.1 ms: 1.03x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.77 ms: 1.02x faster                                                       |
| shortest_path              | 355 ms                                                      | 352 ms: 1.01x faster                                                        |
| async_generators           | 223 ms                                                      | 221 ms: 1.01x faster                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.59 us: 1.00x slower                                                       |
| connected_components       | 320 ms                                                      | 322 ms: 1.01x slower                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.90 sec: 1.01x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.65 ms: 1.02x slower                                                       |
| mako                       | 6.56 ms                                                     | 6.68 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.0 ms: 1.03x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.0 ms: 1.03x slower                                                       |
| pidigits                   | 146 ms                                                      | 150 ms: 1.03x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 106 us: 1.03x slower                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 86.5 ms: 1.03x slower                                                       |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.03x slower                                                        |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.42 sec: 1.03x slower                                                      |
| go                         | 84.7 ms                                                     | 87.6 ms: 1.03x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.04 ms: 1.04x slower                                                       |
| sympy_str                  | 167 ms                                                      | 174 ms: 1.04x slower                                                        |
| sympy_expand               | 286 ms                                                      | 298 ms: 1.04x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 88.9 ms: 1.04x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 314 ms: 1.05x slower                                                        |
| sphinx                     | 617 ms                                                      | 646 ms: 1.05x slower                                                        |
| coverage                   | 45.3 ms                                                     | 47.5 ms: 1.05x slower                                                       |
| 2to3                       | 215 ms                                                      | 227 ms: 1.05x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 42.3 ms: 1.05x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 40.2 ms: 1.05x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 856 us: 1.06x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 57.2 ms: 1.07x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 86.9 ms: 1.08x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 35.1 ms: 1.08x slower                                                       |
| pycparser                  | 695 ms                                                      | 752 ms: 1.08x slower                                                        |
| docutils                   | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 77.9 ms: 1.08x slower                                                       |
| scimark_fft                | 175 ms                                                      | 190 ms: 1.09x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 59.6 ns: 1.09x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.76 ms: 1.09x slower                                                       |
| chaos                      | 37.9 ms                                                     | 41.5 ms: 1.09x slower                                                       |
| fannkuch                   | 252 ms                                                      | 276 ms: 1.10x slower                                                        |
| comprehensions             | 10.4 us                                                     | 11.4 us: 1.10x slower                                                       |
| nbody                      | 66.3 ms                                                     | 72.7 ms: 1.10x slower                                                       |
| pyflate                    | 283 ms                                                      | 311 ms: 1.10x slower                                                        |
| genshi_xml                 | 33.9 ms                                                     | 37.3 ms: 1.10x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 50.2 ms: 1.10x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.58 sec: 1.10x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 40.3 ms: 1.11x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.85 us: 1.11x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.40 us: 1.11x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 45.2 ms: 1.11x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 191 ms: 1.11x slower                                                        |
| nqueens                    | 56.1 ms                                                     | 62.6 ms: 1.12x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 17.1 ms: 1.12x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 85.4 ms: 1.12x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 63.6 ms: 1.12x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.36 ms: 1.13x slower                                                       |
| richards                   | 26.3 ms                                                     | 29.8 ms: 1.14x slower                                                       |
| richards_super             | 29.8 ms                                                     | 34.0 ms: 1.14x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.12 sec: 1.14x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 555 ms: 1.15x slower                                                        |
| sqlglot_transpile          | 953 us                                                      | 1.09 ms: 1.15x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 150 us: 1.16x slower                                                        |
| sqlglot_parse              | 764 us                                                      | 883 us: 1.16x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.22 ms: 1.17x slower                                                       |
| many_optionals             | 361 us                                                      | 435 us: 1.20x slower                                                        |
| pickle_pure_python         | 186 us                                                      | 227 us: 1.22x slower                                                        |
| django_template            | 20.3 ms                                                     | 25.2 ms: 1.24x slower                                                       |
| raytrace                   | 153 ms                                                      | 193 ms: 1.26x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.2 ms: 1.50x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (3): pylint, create_gc_cycles, k_core
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown
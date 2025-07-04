# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_for_compa
- machine: windows-amd64
- commit hash: e27d994
- commit date: 2025-06-18
- overall geometric mean: 1.051x faster
- HPT reliability: 99.24%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                                 |
| docutils       | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                               |
| sphinx         | 617 ms                                                      | 636 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                         |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.86x faster                                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 208 ms: 1.27x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 392 ms: 1.27x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.19x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 340 ms: 1.12x faster                                                                 |
| async_generators           | 223 ms                                                      | 233 ms: 1.05x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.14x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.5 ms: 1.14x faster                                                                |
| nbody          | 66.3 ms                                                     | 64.7 ms: 1.02x faster                                                                |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.1 ms: 1.69x faster                                                                |
| regex_effbot   | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                                |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                         |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.2 us: 1.07x faster                                                                |
| xml_etree_parse      | 92.2 ms                                                     | 89.2 ms: 1.03x faster                                                                |
| unpickle_pure_python | 130 us                                                      | 134 us: 1.03x slower                                                                 |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                               |
| xml_etree_generate   | 53.5 ms                                                     | 56.6 ms: 1.06x slower                                                                |
| xml_etree_iterparse  | 60.5 ms                                                     | 65.1 ms: 1.08x slower                                                                |
| xml_etree_process    | 36.5 ms                                                     | 39.6 ms: 1.08x slower                                                                |
| pickle_pure_python   | 186 us                                                      | 213 us: 1.15x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                                         |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                                |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.3 ms: 1.01x slower                                                                |
| django_template | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                                         |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 492 us: 17.21x faster                                                                |
| pathlib                    | 75.3 ms                                                     | 31.7 ms: 2.38x faster                                                                |
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.86x faster                                                                 |
| mdp                        | 1.43 sec                                                    | 813 ms: 1.76x faster                                                                 |
| regex_v8                   | 23.8 ms                                                     | 14.1 ms: 1.69x faster                                                                |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                                 |
| deepcopy                   | 223 us                                                      | 168 us: 1.33x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                                 |
| deepcopy_memo              | 23.1 us                                                     | 18.1 us: 1.28x faster                                                                |
| async_tree_memoization     | 265 ms                                                      | 208 ms: 1.27x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 392 ms: 1.27x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.19x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                                 |
| float                      | 50.8 ms                                                     | 44.5 ms: 1.14x faster                                                                |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 340 ms: 1.12x faster                                                                 |
| deepcopy_reduce            | 2.02 us                                                     | 1.82 us: 1.11x faster                                                                |
| regex_effbot               | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                                |
| go                         | 84.7 ms                                                     | 77.4 ms: 1.09x faster                                                                |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.07x faster                                                                |
| json                       | 3.30 ms                                                     | 3.10 ms: 1.06x faster                                                                |
| telco                      | 4.85 ms                                                     | 4.63 ms: 1.05x faster                                                                |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.49 ms: 1.05x faster                                                                |
| xml_etree_parse            | 92.2 ms                                                     | 89.2 ms: 1.03x faster                                                                |
| nbody                      | 66.3 ms                                                     | 64.7 ms: 1.02x faster                                                                |
| sqlite_synth               | 1.59 us                                                     | 1.58 us: 1.00x faster                                                                |
| genshi_text                | 15.2 ms                                                     | 15.3 ms: 1.01x slower                                                                |
| meteor_contest             | 72.0 ms                                                     | 72.5 ms: 1.01x slower                                                                |
| spectral_norm              | 63.4 ms                                                     | 64.3 ms: 1.01x slower                                                                |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.02x slower                                                                |
| dulwich_log                | 40.1 ms                                                     | 40.9 ms: 1.02x slower                                                                |
| sympy_expand               | 286 ms                                                      | 292 ms: 1.02x slower                                                                 |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                                                 |
| generators                 | 19.0 ms                                                     | 19.5 ms: 1.03x slower                                                                |
| shortest_path              | 355 ms                                                      | 365 ms: 1.03x slower                                                                 |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                                 |
| sympy_sum                  | 85.2 ms                                                     | 87.5 ms: 1.03x slower                                                                |
| scimark_sor                | 76.2 ms                                                     | 78.4 ms: 1.03x slower                                                                |
| sphinx                     | 617 ms                                                      | 636 ms: 1.03x slower                                                                 |
| unpickle_pure_python       | 130 us                                                      | 134 us: 1.03x slower                                                                 |
| crypto_pyaes               | 45.6 ms                                                     | 47.3 ms: 1.04x slower                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                               |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                                 |
| pyflate                    | 283 ms                                                      | 295 ms: 1.04x slower                                                                 |
| bpe_tokeniser              | 2.87 sec                                                    | 2.99 sec: 1.04x slower                                                               |
| async_generators           | 223 ms                                                      | 233 ms: 1.05x slower                                                                 |
| connected_components       | 320 ms                                                      | 335 ms: 1.05x slower                                                                 |
| comprehensions             | 10.4 us                                                     | 10.9 us: 1.05x slower                                                                |
| scimark_monte_carlo        | 40.7 ms                                                     | 42.8 ms: 1.05x slower                                                                |
| scimark_lu                 | 56.7 ms                                                     | 59.6 ms: 1.05x slower                                                                |
| richards                   | 26.3 ms                                                     | 27.7 ms: 1.06x slower                                                                |
| python_startup             | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                                |
| xml_etree_generate         | 53.5 ms                                                     | 56.6 ms: 1.06x slower                                                                |
| richards_super             | 29.8 ms                                                     | 31.6 ms: 1.06x slower                                                                |
| docutils                   | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                               |
| fannkuch                   | 252 ms                                                      | 269 ms: 1.07x slower                                                                 |
| scimark_fft                | 175 ms                                                      | 188 ms: 1.08x slower                                                                 |
| xml_etree_iterparse        | 60.5 ms                                                     | 65.1 ms: 1.08x slower                                                                |
| gc_traversal               | 1.96 ms                                                     | 2.12 ms: 1.08x slower                                                                |
| create_gc_cycles           | 1.22 ms                                                     | 1.32 ms: 1.08x slower                                                                |
| xml_etree_process          | 36.5 ms                                                     | 39.6 ms: 1.08x slower                                                                |
| hexiom                     | 3.84 ms                                                     | 4.19 ms: 1.09x slower                                                                |
| chaos                      | 37.9 ms                                                     | 41.6 ms: 1.10x slower                                                                |
| nqueens                    | 56.1 ms                                                     | 61.7 ms: 1.10x slower                                                                |
| pprint_safe_repr           | 485 ms                                                      | 541 ms: 1.12x slower                                                                 |
| coverage                   | 45.3 ms                                                     | 51.5 ms: 1.14x slower                                                                |
| pprint_pformat             | 977 ms                                                      | 1.11 sec: 1.14x slower                                                               |
| logging_simple             | 5.77 us                                                     | 6.56 us: 1.14x slower                                                                |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.14x slower                                                                |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                                |
| logging_format             | 6.18 us                                                     | 7.06 us: 1.14x slower                                                                |
| pickle_pure_python         | 186 us                                                      | 213 us: 1.15x slower                                                                 |
| deltablue                  | 1.89 ms                                                     | 2.23 ms: 1.18x slower                                                                |
| django_template            | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                                |
| raytrace                   | 153 ms                                                      | 182 ms: 1.18x slower                                                                 |
| many_optionals             | 361 us                                                      | 434 us: 1.20x slower                                                                 |
| subparsers                 | 10.9 ms                                                     | 17.0 ms: 1.56x slower                                                                |
| logging_silent             | 54.6 ns                                                     | 329 ns: 6.03x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                         |

Benchmark hidden because not significant (10): pylint, typing_runtime_protocols, pidigits, regex_compile, k_core, mako, html5lib, json_dumps, genshi_xml, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250618-3.15.0a0-e27d994/bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.051x faster

# HPT report

- Reliability score: 99.24% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
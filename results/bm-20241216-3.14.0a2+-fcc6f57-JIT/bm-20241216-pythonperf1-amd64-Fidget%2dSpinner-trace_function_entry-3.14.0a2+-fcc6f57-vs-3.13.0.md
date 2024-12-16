# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: windows-amd64
- commit hash: fcc6f57
- commit date: 2024-12-16
- overall geometric mean: 1.034x faster
- HPT reliability: 57.74%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 218 ms: 1.01x slower                                                                  |
| docutils       | 1.53 sec                                                    | 1.75 sec: 1.15x slower                                                                |
| sphinx         | 617 ms                                                      | 652 ms: 1.06x slower                                                                  |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                                  |
| async_tree_io              | 513 ms                                                      | 404 ms: 1.27x faster                                                                  |
| async_tree_io_tg           | 497 ms                                                      | 398 ms: 1.25x faster                                                                  |
| async_tree_none            | 219 ms                                                      | 179 ms: 1.23x faster                                                                  |
| async_tree_memoization     | 265 ms                                                      | 219 ms: 1.21x faster                                                                  |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 350 ms: 1.09x faster                                                                  |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 355 ms: 1.07x faster                                                                  |
| asyncio_websockets         | 300 ms                                                      | 305 ms: 1.02x slower                                                                  |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                                  |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.13x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 54.2 ms: 1.22x faster                                                                 |
| float          | 50.8 ms                                                     | 49.2 ms: 1.03x faster                                                                 |
| pidigits       | 146 ms                                                      | 147 ms: 1.00x slower                                                                  |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 16.9 ms: 1.41x faster                                                                 |
| regex_effbot   | 1.69 ms                                                     | 1.52 ms: 1.11x faster                                                                 |
| regex_dna      | 115 ms                                                      | 118 ms: 1.02x slower                                                                  |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 107 us: 1.21x faster                                                                  |
| tomli_loads          | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                                |
| xml_etree_generate   | 53.5 ms                                                     | 50.2 ms: 1.06x faster                                                                 |
| xml_etree_parse      | 92.2 ms                                                     | 86.8 ms: 1.06x faster                                                                 |
| json_loads           | 15.1 us                                                     | 14.2 us: 1.06x faster                                                                 |
| xml_etree_process    | 36.5 ms                                                     | 35.5 ms: 1.03x faster                                                                 |
| xml_etree_iterparse  | 60.5 ms                                                     | 61.2 ms: 1.01x slower                                                                 |
| pickle_pure_python   | 186 us                                                      | 192 us: 1.03x slower                                                                  |
| json_dumps           | 6.19 ms                                                     | 6.39 ms: 1.03x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 23.4 ms: 1.04x faster                                                                 |
| python_startup_no_site | 16.9 ms                                                     | 17.7 ms: 1.04x slower                                                                 |
| Geometric mean         | (ref)                                                       | 1.00x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.18 ms: 1.27x faster                                                                 |
| genshi_text     | 15.2 ms                                                     | 16.2 ms: 1.07x slower                                                                 |
| genshi_xml      | 33.9 ms                                                     | 37.9 ms: 1.12x slower                                                                 |
| django_template | 20.3 ms                                                     | 25.9 ms: 1.27x slower                                                                 |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 530 us: 15.96x faster                                                                 |
| regex_v8                   | 23.8 ms                                                     | 16.9 ms: 1.41x faster                                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                                  |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.03 ms: 1.28x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 404 ms: 1.27x faster                                                                  |
| mako                       | 6.56 ms                                                     | 5.18 ms: 1.27x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 398 ms: 1.25x faster                                                                  |
| scimark_fft                | 175 ms                                                      | 141 ms: 1.24x faster                                                                  |
| async_tree_none            | 219 ms                                                      | 179 ms: 1.23x faster                                                                  |
| nbody                      | 66.3 ms                                                     | 54.2 ms: 1.22x faster                                                                 |
| unpickle_pure_python       | 130 us                                                      | 107 us: 1.21x faster                                                                  |
| async_tree_memoization     | 265 ms                                                      | 219 ms: 1.21x faster                                                                  |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                                                  |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                                  |
| tomli_loads                | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                                |
| scimark_monte_carlo        | 40.7 ms                                                     | 35.8 ms: 1.14x faster                                                                 |
| json                       | 3.30 ms                                                     | 2.93 ms: 1.13x faster                                                                 |
| regex_effbot               | 1.69 ms                                                     | 1.52 ms: 1.11x faster                                                                 |
| crypto_pyaes               | 45.6 ms                                                     | 41.0 ms: 1.11x faster                                                                 |
| telco                      | 4.85 ms                                                     | 4.37 ms: 1.11x faster                                                                 |
| deepcopy_memo              | 23.1 us                                                     | 20.8 us: 1.11x faster                                                                 |
| bpe_tokeniser              | 2.87 sec                                                    | 2.62 sec: 1.10x faster                                                                |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 350 ms: 1.09x faster                                                                  |
| k_core                     | 1.70 sec                                                    | 1.57 sec: 1.08x faster                                                                |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 355 ms: 1.07x faster                                                                  |
| xml_etree_generate         | 53.5 ms                                                     | 50.2 ms: 1.06x faster                                                                 |
| xml_etree_parse            | 92.2 ms                                                     | 86.8 ms: 1.06x faster                                                                 |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.06x faster                                                                 |
| fannkuch                   | 252 ms                                                      | 239 ms: 1.05x faster                                                                  |
| deepcopy_reduce            | 2.02 us                                                     | 1.92 us: 1.05x faster                                                                 |
| python_startup             | 24.4 ms                                                     | 23.4 ms: 1.04x faster                                                                 |
| connected_components       | 320 ms                                                      | 308 ms: 1.04x faster                                                                  |
| float                      | 50.8 ms                                                     | 49.2 ms: 1.03x faster                                                                 |
| pyflate                    | 283 ms                                                      | 275 ms: 1.03x faster                                                                  |
| xml_etree_process          | 36.5 ms                                                     | 35.5 ms: 1.03x faster                                                                 |
| shortest_path              | 355 ms                                                      | 346 ms: 1.03x faster                                                                  |
| bench_mp_pool              | 84.2 ms                                                     | 82.4 ms: 1.02x faster                                                                 |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.02x faster                                                                 |
| create_gc_cycles           | 1.22 ms                                                     | 1.21 ms: 1.01x faster                                                                 |
| dulwich_log                | 40.1 ms                                                     | 39.8 ms: 1.01x faster                                                                 |
| pprint_pformat             | 977 ms                                                      | 971 ms: 1.01x faster                                                                  |
| pidigits                   | 146 ms                                                      | 147 ms: 1.00x slower                                                                  |
| 2to3                       | 215 ms                                                      | 218 ms: 1.01x slower                                                                  |
| xml_etree_iterparse        | 60.5 ms                                                     | 61.2 ms: 1.01x slower                                                                 |
| asyncio_websockets         | 300 ms                                                      | 305 ms: 1.02x slower                                                                  |
| go                         | 84.7 ms                                                     | 86.1 ms: 1.02x slower                                                                 |
| meteor_contest             | 72.0 ms                                                     | 73.4 ms: 1.02x slower                                                                 |
| pprint_safe_repr           | 485 ms                                                      | 495 ms: 1.02x slower                                                                  |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.02x slower                                                                  |
| pickle_pure_python         | 186 us                                                      | 192 us: 1.03x slower                                                                  |
| json_dumps                 | 6.19 ms                                                     | 6.39 ms: 1.03x slower                                                                 |
| sympy_str                  | 167 ms                                                      | 173 ms: 1.04x slower                                                                  |
| python_startup_no_site     | 16.9 ms                                                     | 17.7 ms: 1.04x slower                                                                 |
| sympy_sum                  | 85.2 ms                                                     | 89.0 ms: 1.04x slower                                                                 |
| sympy_expand               | 286 ms                                                      | 300 ms: 1.05x slower                                                                  |
| mdp                        | 1.43 sec                                                    | 1.50 sec: 1.05x slower                                                                |
| sphinx                     | 617 ms                                                      | 652 ms: 1.06x slower                                                                  |
| genshi_text                | 15.2 ms                                                     | 16.2 ms: 1.07x slower                                                                 |
| logging_simple             | 5.77 us                                                     | 6.18 us: 1.07x slower                                                                 |
| coverage                   | 45.3 ms                                                     | 48.7 ms: 1.07x slower                                                                 |
| logging_format             | 6.18 us                                                     | 6.65 us: 1.08x slower                                                                 |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.09x slower                                                                 |
| scimark_lu                 | 56.7 ms                                                     | 61.9 ms: 1.09x slower                                                                 |
| typing_runtime_protocols   | 103 us                                                      | 113 us: 1.10x slower                                                                  |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                                  |
| nqueens                    | 56.1 ms                                                     | 61.9 ms: 1.10x slower                                                                 |
| chaos                      | 37.9 ms                                                     | 41.9 ms: 1.11x slower                                                                 |
| genshi_xml                 | 33.9 ms                                                     | 37.9 ms: 1.12x slower                                                                 |
| sqlglot_parse              | 764 us                                                      | 856 us: 1.12x slower                                                                  |
| scimark_sor                | 76.2 ms                                                     | 86.1 ms: 1.13x slower                                                                 |
| comprehensions             | 10.4 us                                                     | 11.7 us: 1.13x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.13x slower                                                                 |
| sqlglot_optimize           | 32.5 ms                                                     | 37.1 ms: 1.14x slower                                                                 |
| docutils                   | 1.53 sec                                                    | 1.75 sec: 1.15x slower                                                                |
| sqlglot_normalize          | 172 ms                                                      | 197 ms: 1.15x slower                                                                  |
| sqlglot_transpile          | 953 us                                                      | 1.11 ms: 1.16x slower                                                                 |
| logging_silent             | 54.6 ns                                                     | 63.6 ns: 1.17x slower                                                                 |
| hexiom                     | 3.84 ms                                                     | 4.49 ms: 1.17x slower                                                                 |
| richards                   | 26.3 ms                                                     | 31.0 ms: 1.18x slower                                                                 |
| richards_super             | 29.8 ms                                                     | 35.4 ms: 1.19x slower                                                                 |
| generators                 | 19.0 ms                                                     | 23.0 ms: 1.21x slower                                                                 |
| deltablue                  | 1.89 ms                                                     | 2.30 ms: 1.21x slower                                                                 |
| raytrace                   | 153 ms                                                      | 187 ms: 1.22x slower                                                                  |
| many_optionals             | 361 us                                                      | 460 us: 1.27x slower                                                                  |
| django_template            | 20.3 ms                                                     | 25.9 ms: 1.27x slower                                                                 |
| subparsers                 | 10.9 ms                                                     | 15.9 ms: 1.46x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                          |

Benchmark hidden because not significant (8): pylint, bench_thread_pool, regex_compile, spectral_norm, pathlib, gc_traversal, html5lib, pycparser
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241216-3.14.0a2+-fcc6f57-JIT/bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57.json: mypy2

- Geometric mean (including insignificant results): 1.034x faster

# HPT report

- Reliability score: 57.74% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
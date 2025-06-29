# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_os
- machine: windows-amd64
- commit hash: 33054dd
- commit date: 2025-06-28
- overall geometric mean: 1.078x faster
- HPT reliability: 77.64%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 219 ms: 1.02x slower                                               |
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                             |
| sphinx         | 617 ms                                                      | 645 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                       | 1.04x slower                                                       |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                               |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                               |
| async_tree_io              | 513 ms                                                      | 399 ms: 1.29x faster                                               |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                               |
| async_tree_memoization     | 265 ms                                                      | 210 ms: 1.26x faster                                               |
| async_tree_io_tg           | 497 ms                                                      | 394 ms: 1.26x faster                                               |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 334 ms: 1.14x faster                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 346 ms: 1.11x faster                                               |
| async_generators           | 223 ms                                                      | 250 ms: 1.12x slower                                               |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.14x slower                                              |
| Geometric mean             | (ref)                                                       | 1.20x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.0 ms: 1.13x faster                                              |
| nbody          | 66.3 ms                                                     | 59.7 ms: 1.11x faster                                              |
| Geometric mean | (ref)                                                       | 1.08x faster                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                              |
| regex_effbot   | 1.69 ms                                                     | 1.56 ms: 1.08x faster                                              |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                       | 1.15x faster                                                       |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 108 us: 1.21x faster                                               |
| tomli_loads          | 1.37 sec                                                    | 1.14 sec: 1.20x faster                                             |
| json_loads           | 15.1 us                                                     | 14.6 us: 1.04x faster                                              |
| xml_etree_parse      | 92.2 ms                                                     | 89.0 ms: 1.04x faster                                              |
| xml_etree_process    | 36.5 ms                                                     | 35.8 ms: 1.02x faster                                              |
| json_dumps           | 6.19 ms                                                     | 6.29 ms: 1.02x slower                                              |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.4 ms: 1.06x slower                                              |
| pickle_pure_python   | 186 us                                                      | 205 us: 1.10x slower                                               |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                       |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.0 ms: 1.07x slower                                              |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                              |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.31 ms: 1.24x faster                                              |
| genshi_text     | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                              |
| django_template | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                              |
| Geometric mean  | (ref)                                                       | 1.00x slower                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 507 us: 16.69x faster                                              |
| pathlib                    | 75.3 ms                                                     | 31.7 ms: 2.37x faster                                              |
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                               |
| mdp                        | 1.43 sec                                                    | 803 ms: 1.78x faster                                               |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                              |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                               |
| deepcopy                   | 223 us                                                      | 171 us: 1.31x faster                                               |
| async_tree_io              | 513 ms                                                      | 399 ms: 1.29x faster                                               |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                               |
| async_tree_memoization     | 265 ms                                                      | 210 ms: 1.26x faster                                               |
| async_tree_io_tg           | 497 ms                                                      | 394 ms: 1.26x faster                                               |
| deepcopy_memo              | 23.1 us                                                     | 18.5 us: 1.25x faster                                              |
| mako                       | 6.56 ms                                                     | 5.31 ms: 1.24x faster                                              |
| unpickle_pure_python       | 130 us                                                      | 108 us: 1.21x faster                                               |
| tomli_loads                | 1.37 sec                                                    | 1.14 sec: 1.20x faster                                             |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                               |
| fannkuch                   | 252 ms                                                      | 216 ms: 1.17x faster                                               |
| scimark_fft                | 175 ms                                                      | 151 ms: 1.16x faster                                               |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.29 ms: 1.14x faster                                              |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 334 ms: 1.14x faster                                               |
| float                      | 50.8 ms                                                     | 45.0 ms: 1.13x faster                                              |
| telco                      | 4.85 ms                                                     | 4.29 ms: 1.13x faster                                              |
| bpe_tokeniser              | 2.87 sec                                                    | 2.58 sec: 1.11x faster                                             |
| pyflate                    | 283 ms                                                      | 255 ms: 1.11x faster                                               |
| nbody                      | 66.3 ms                                                     | 59.7 ms: 1.11x faster                                              |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 346 ms: 1.11x faster                                               |
| deepcopy_reduce            | 2.02 us                                                     | 1.85 us: 1.09x faster                                              |
| go                         | 84.7 ms                                                     | 77.9 ms: 1.09x faster                                              |
| regex_effbot               | 1.69 ms                                                     | 1.56 ms: 1.08x faster                                              |
| pprint_pformat             | 977 ms                                                      | 918 ms: 1.06x faster                                               |
| pprint_safe_repr           | 485 ms                                                      | 460 ms: 1.05x faster                                               |
| json                       | 3.30 ms                                                     | 3.17 ms: 1.04x faster                                              |
| json_loads                 | 15.1 us                                                     | 14.6 us: 1.04x faster                                              |
| xml_etree_parse            | 92.2 ms                                                     | 89.0 ms: 1.04x faster                                              |
| k_core                     | 1.70 sec                                                    | 1.64 sec: 1.03x faster                                             |
| meteor_contest             | 72.0 ms                                                     | 70.4 ms: 1.02x faster                                              |
| xml_etree_process          | 36.5 ms                                                     | 35.8 ms: 1.02x faster                                              |
| shortest_path              | 355 ms                                                      | 357 ms: 1.01x slower                                               |
| crypto_pyaes               | 45.6 ms                                                     | 46.0 ms: 1.01x slower                                              |
| logging_silent             | 54.6 ns                                                     | 55.3 ns: 1.01x slower                                              |
| spectral_norm              | 63.4 ms                                                     | 64.3 ms: 1.01x slower                                              |
| json_dumps                 | 6.19 ms                                                     | 6.29 ms: 1.02x slower                                              |
| typing_runtime_protocols   | 103 us                                                      | 105 us: 1.02x slower                                               |
| dulwich_log                | 40.1 ms                                                     | 40.9 ms: 1.02x slower                                              |
| comprehensions             | 10.4 us                                                     | 10.6 us: 1.02x slower                                              |
| genshi_text                | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                              |
| 2to3                       | 215 ms                                                      | 219 ms: 1.02x slower                                               |
| sympy_str                  | 167 ms                                                      | 171 ms: 1.02x slower                                               |
| connected_components       | 320 ms                                                      | 328 ms: 1.03x slower                                               |
| scimark_sor                | 76.2 ms                                                     | 78.9 ms: 1.04x slower                                              |
| sympy_integrate            | 12.3 ms                                                     | 12.8 ms: 1.04x slower                                              |
| sympy_expand               | 286 ms                                                      | 296 ms: 1.04x slower                                               |
| richards                   | 26.3 ms                                                     | 27.2 ms: 1.04x slower                                              |
| sympy_sum                  | 85.2 ms                                                     | 88.3 ms: 1.04x slower                                              |
| richards_super             | 29.8 ms                                                     | 30.9 ms: 1.04x slower                                              |
| generators                 | 19.0 ms                                                     | 19.7 ms: 1.04x slower                                              |
| scimark_monte_carlo        | 40.7 ms                                                     | 42.6 ms: 1.04x slower                                              |
| sphinx                     | 617 ms                                                      | 645 ms: 1.05x slower                                               |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                               |
| scimark_lu                 | 56.7 ms                                                     | 60.2 ms: 1.06x slower                                              |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.4 ms: 1.06x slower                                              |
| python_startup             | 24.4 ms                                                     | 26.0 ms: 1.07x slower                                              |
| logging_simple             | 5.77 us                                                     | 6.19 us: 1.07x slower                                              |
| logging_format             | 6.18 us                                                     | 6.63 us: 1.07x slower                                              |
| hexiom                     | 3.84 ms                                                     | 4.13 ms: 1.07x slower                                              |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                             |
| nqueens                    | 56.1 ms                                                     | 60.8 ms: 1.08x slower                                              |
| create_gc_cycles           | 1.22 ms                                                     | 1.33 ms: 1.09x slower                                              |
| chaos                      | 37.9 ms                                                     | 41.2 ms: 1.09x slower                                              |
| gc_traversal               | 1.96 ms                                                     | 2.14 ms: 1.09x slower                                              |
| pickle_pure_python         | 186 us                                                      | 205 us: 1.10x slower                                               |
| coverage                   | 45.3 ms                                                     | 50.3 ms: 1.11x slower                                              |
| async_generators           | 223 ms                                                      | 250 ms: 1.12x slower                                               |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                              |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.14x slower                                              |
| raytrace                   | 153 ms                                                      | 179 ms: 1.17x slower                                               |
| deltablue                  | 1.89 ms                                                     | 2.22 ms: 1.17x slower                                              |
| django_template            | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                              |
| many_optionals             | 361 us                                                      | 450 us: 1.24x slower                                               |
| subparsers                 | 10.9 ms                                                     | 17.0 ms: 1.57x slower                                              |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                       |

Benchmark hidden because not significant (8): pylint, sqlite_synth, regex_compile, pidigits, pycparser, html5lib, xml_etree_generate, genshi_xml
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250628-3.15.0a0-33054dd-JIT/bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.078x faster

# HPT report

- Reliability score: 77.64% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
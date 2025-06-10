# Results vs. 3.13.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.008x slower
- HPT reliability: 54.54%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                       |
| docutils       | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                     |
| sphinx         | 617 ms                                                      | 647 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.33x faster                                       |
| async_tree_io              | 513 ms                                                      | 395 ms: 1.30x faster                                       |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                       |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                       |
| async_tree_io_tg           | 497 ms                                                      | 393 ms: 1.26x faster                                       |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 332 ms: 1.14x faster                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                       |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                       |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                      |
| Geometric mean             | (ref)                                                       | 1.21x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.4 ms: 1.17x faster                                      |
| nbody          | 66.3 ms                                                     | 60.6 ms: 1.09x faster                                      |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.8 ms: 1.73x faster                                      |
| regex_effbot   | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                      |
| regex_compile  | 80.7 ms                                                     | 78.0 ms: 1.03x faster                                      |
| regex_dna      | 115 ms                                                      | 116 ms: 1.00x slower                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.14 sec: 1.21x faster                                     |
| unpickle_pure_python | 130 us                                                      | 112 us: 1.16x faster                                       |
| xml_etree_parse      | 92.2 ms                                                     | 88.0 ms: 1.05x faster                                      |
| json_loads           | 15.1 us                                                     | 14.5 us: 1.04x faster                                      |
| xml_etree_process    | 36.5 ms                                                     | 36.7 ms: 1.01x slower                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.0 ms: 1.06x slower                                      |
| pickle_pure_python   | 186 us                                                      | 206 us: 1.11x slower                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                               |

Benchmark hidden because not significant (2): xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.5 ms: 1.16x slower                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.50 ms: 1.19x faster                                      |
| genshi_text     | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                      |
| django_template | 20.3 ms                                                     | 23.8 ms: 1.17x slower                                      |
| Geometric mean  | (ref)                                                       | 1.00x slower                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.2 ms: 2.34x faster                                      |
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                       |
| mdp                        | 1.43 sec                                                    | 812 ms: 1.76x faster                                       |
| regex_v8                   | 23.8 ms                                                     | 13.8 ms: 1.73x faster                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.33x faster                                       |
| deepcopy                   | 223 us                                                      | 170 us: 1.32x faster                                       |
| async_tree_io              | 513 ms                                                      | 395 ms: 1.30x faster                                       |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                       |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                       |
| async_tree_io_tg           | 497 ms                                                      | 393 ms: 1.26x faster                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.5 us: 1.25x faster                                      |
| tomli_loads                | 1.37 sec                                                    | 1.14 sec: 1.21x faster                                     |
| mako                       | 6.56 ms                                                     | 5.50 ms: 1.19x faster                                      |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                       |
| float                      | 50.8 ms                                                     | 43.4 ms: 1.17x faster                                      |
| unpickle_pure_python       | 130 us                                                      | 112 us: 1.16x faster                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 332 ms: 1.14x faster                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.30 ms: 1.13x faster                                      |
| go                         | 84.7 ms                                                     | 75.6 ms: 1.12x faster                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.82 us: 1.11x faster                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                       |
| scimark_fft                | 175 ms                                                      | 158 ms: 1.11x faster                                       |
| pyflate                    | 283 ms                                                      | 256 ms: 1.10x faster                                       |
| regex_effbot               | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                      |
| nbody                      | 66.3 ms                                                     | 60.6 ms: 1.09x faster                                      |
| telco                      | 4.85 ms                                                     | 4.44 ms: 1.09x faster                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.66 sec: 1.08x faster                                     |
| json                       | 3.30 ms                                                     | 3.11 ms: 1.06x faster                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.0 ms: 1.05x faster                                      |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.04x faster                                      |
| k_core                     | 1.70 sec                                                    | 1.63 sec: 1.04x faster                                     |
| fannkuch                   | 252 ms                                                      | 242 ms: 1.04x faster                                       |
| regex_compile              | 80.7 ms                                                     | 78.0 ms: 1.03x faster                                      |
| spectral_norm              | 63.4 ms                                                     | 62.0 ms: 1.02x faster                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.9 ms: 1.02x faster                                      |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.02x faster                                      |
| shortest_path              | 355 ms                                                      | 352 ms: 1.01x faster                                       |
| regex_dna                  | 115 ms                                                      | 116 ms: 1.00x slower                                       |
| xml_etree_process          | 36.5 ms                                                     | 36.7 ms: 1.01x slower                                      |
| genshi_text                | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                      |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                       |
| typing_runtime_protocols   | 103 us                                                      | 105 us: 1.01x slower                                       |
| connected_components       | 320 ms                                                      | 325 ms: 1.02x slower                                       |
| richards                   | 26.3 ms                                                     | 26.7 ms: 1.02x slower                                      |
| crypto_pyaes               | 45.6 ms                                                     | 46.5 ms: 1.02x slower                                      |
| meteor_contest             | 72.0 ms                                                     | 73.6 ms: 1.02x slower                                      |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                       |
| sympy_str                  | 167 ms                                                      | 171 ms: 1.02x slower                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.7 ms: 1.03x slower                                      |
| richards_super             | 29.8 ms                                                     | 30.5 ms: 1.03x slower                                      |
| sympy_sum                  | 85.2 ms                                                     | 87.9 ms: 1.03x slower                                      |
| sympy_expand               | 286 ms                                                      | 296 ms: 1.03x slower                                       |
| chaos                      | 37.9 ms                                                     | 39.3 ms: 1.04x slower                                      |
| dulwich_log                | 40.1 ms                                                     | 41.8 ms: 1.04x slower                                      |
| scimark_lu                 | 56.7 ms                                                     | 59.2 ms: 1.04x slower                                      |
| generators                 | 19.0 ms                                                     | 19.9 ms: 1.05x slower                                      |
| sphinx                     | 617 ms                                                      | 647 ms: 1.05x slower                                       |
| comprehensions             | 10.4 us                                                     | 10.9 us: 1.06x slower                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.0 ms: 1.06x slower                                      |
| hexiom                     | 3.84 ms                                                     | 4.10 ms: 1.07x slower                                      |
| nqueens                    | 56.1 ms                                                     | 60.1 ms: 1.07x slower                                      |
| pprint_safe_repr           | 485 ms                                                      | 519 ms: 1.07x slower                                       |
| python_startup             | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.32 ms: 1.08x slower                                      |
| pprint_pformat             | 977 ms                                                      | 1.06 sec: 1.08x slower                                     |
| gc_traversal               | 1.96 ms                                                     | 2.13 ms: 1.08x slower                                      |
| docutils                   | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                     |
| logging_simple             | 5.77 us                                                     | 6.34 us: 1.10x slower                                      |
| logging_format             | 6.18 us                                                     | 6.81 us: 1.10x slower                                      |
| pickle_pure_python         | 186 us                                                      | 206 us: 1.11x slower                                       |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                       |
| raytrace                   | 153 ms                                                      | 177 ms: 1.16x slower                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.5 ms: 1.16x slower                                      |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                      |
| deltablue                  | 1.89 ms                                                     | 2.21 ms: 1.17x slower                                      |
| django_template            | 20.3 ms                                                     | 23.8 ms: 1.17x slower                                      |
| many_optionals             | 361 us                                                      | 447 us: 1.24x slower                                       |
| subparsers                 | 10.9 ms                                                     | 16.9 ms: 1.56x slower                                      |
| logging_silent             | 54.6 ns                                                     | 314 ns: 5.76x slower                                       |
| coverage                   | 45.3 ms                                                     | 298 ms: 6.57x slower                                       |
| thrift                     | 8.47 ms                                                     | 95.2 ms: 11.24x slower                                     |
| Geometric mean             | (ref)                                                       | 1.03x slower                                               |

Benchmark hidden because not significant (7): pylint, xml_etree_generate, json_dumps, scimark_sor, html5lib, pycparser, genshi_xml
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.008x slower

# HPT report

- Reliability score: 54.54% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
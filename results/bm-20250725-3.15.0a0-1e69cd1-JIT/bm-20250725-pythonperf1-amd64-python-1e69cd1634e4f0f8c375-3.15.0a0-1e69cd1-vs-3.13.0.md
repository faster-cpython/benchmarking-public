# Results vs. 3.13.0

- fork: python
- ref: 1e69cd1634e4f0f8c375
- machine: windows-amd64
- commit hash: 1e69cd1
- commit date: 2025-07-25
- overall geometric mean: 1.069x faster
- HPT reliability: 80.25%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                     |
| html5lib       | 38.2 ms                                                     | 39.0 ms: 1.02x slower                                                      |
| sphinx         | 617 ms                                                      | 642 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 166 ms: 1.80x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 203 ms: 1.31x faster                                                       |
| async_tree_io              | 513 ms                                                      | 398 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 386 ms: 1.29x faster                                                       |
| async_tree_none            | 219 ms                                                      | 177 ms: 1.24x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 337 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 351 ms: 1.09x faster                                                       |
| async_generators           | 223 ms                                                      | 253 ms: 1.14x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.17x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 56.7 ms: 1.17x faster                                                      |
| float          | 50.8 ms                                                     | 44.4 ms: 1.14x faster                                                      |
| pidigits       | 146 ms                                                      | 150 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.9 ms: 1.60x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.64 ms: 1.03x faster                                                      |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 105 us: 1.24x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.11 sec: 1.24x faster                                                     |
| xml_etree_generate   | 53.5 ms                                                     | 49.8 ms: 1.07x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.2 us: 1.06x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 35.2 ms: 1.04x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 89.2 ms: 1.03x faster                                                      |
| json_dumps           | 6.19 ms                                                     | 6.31 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 65.0 ms: 1.07x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 207 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.7 ms: 1.09x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.9 ms: 1.18x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.40 ms: 1.22x faster                                                      |
| genshi_xml      | 33.9 ms                                                     | 35.2 ms: 1.04x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 16.1 ms: 1.06x slower                                                      |
| django_template | 20.3 ms                                                     | 23.9 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 491 us: 17.25x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 33.5 ms: 2.25x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 166 ms: 1.80x faster                                                       |
| mdp                        | 1.43 sec                                                    | 808 ms: 1.77x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.9 ms: 1.60x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                       |
| deepcopy                   | 223 us                                                      | 170 us: 1.32x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 203 ms: 1.31x faster                                                       |
| async_tree_io              | 513 ms                                                      | 398 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 386 ms: 1.29x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.0 us: 1.28x faster                                                      |
| async_tree_none            | 219 ms                                                      | 177 ms: 1.24x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 105 us: 1.24x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.11 sec: 1.24x faster                                                     |
| mako                       | 6.56 ms                                                     | 5.40 ms: 1.22x faster                                                      |
| fannkuch                   | 252 ms                                                      | 207 ms: 1.21x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                       |
| nbody                      | 66.3 ms                                                     | 56.7 ms: 1.17x faster                                                      |
| float                      | 50.8 ms                                                     | 44.4 ms: 1.14x faster                                                      |
| pyflate                    | 283 ms                                                      | 249 ms: 1.14x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.54 sec: 1.13x faster                                                     |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 337 ms: 1.13x faster                                                       |
| scimark_fft                | 175 ms                                                      | 155 ms: 1.12x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.32 ms: 1.12x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.34 ms: 1.11x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.84 us: 1.10x faster                                                      |
| go                         | 84.7 ms                                                     | 77.0 ms: 1.10x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 351 ms: 1.09x faster                                                       |
| json                       | 3.30 ms                                                     | 3.04 ms: 1.08x faster                                                      |
| pprint_pformat             | 977 ms                                                      | 906 ms: 1.08x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 49.8 ms: 1.07x faster                                                      |
| pprint_safe_repr           | 485 ms                                                      | 452 ms: 1.07x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.06x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.63 sec: 1.04x faster                                                     |
| xml_etree_process          | 36.5 ms                                                     | 35.2 ms: 1.04x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 89.2 ms: 1.03x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.64 ms: 1.03x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.3 ms: 1.01x faster                                                      |
| shortest_path              | 355 ms                                                      | 359 ms: 1.01x slower                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.61 us: 1.01x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 46.2 ms: 1.01x slower                                                      |
| connected_components       | 320 ms                                                      | 326 ms: 1.02x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.31 ms: 1.02x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 73.4 ms: 1.02x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 39.0 ms: 1.02x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 77.9 ms: 1.02x slower                                                      |
| comprehensions             | 10.4 us                                                     | 10.6 us: 1.02x slower                                                      |
| pidigits                   | 146 ms                                                      | 150 ms: 1.02x slower                                                       |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 58.2 ms: 1.03x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 41.2 ms: 1.03x slower                                                      |
| sympy_str                  | 167 ms                                                      | 172 ms: 1.03x slower                                                       |
| logging_simple             | 5.77 us                                                     | 5.97 us: 1.03x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 35.2 ms: 1.04x slower                                                      |
| sphinx                     | 617 ms                                                      | 642 ms: 1.04x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 88.7 ms: 1.04x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.0 ms: 1.05x slower                                                      |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.05 ms: 1.05x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.52 us: 1.06x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 67.0 ms: 1.06x slower                                                      |
| generators                 | 19.0 ms                                                     | 20.1 ms: 1.06x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 16.1 ms: 1.06x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.8 ms: 1.06x slower                                                      |
| richards_super             | 29.8 ms                                                     | 31.6 ms: 1.06x slower                                                      |
| sympy_expand               | 286 ms                                                      | 304 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 65.0 ms: 1.07x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                     |
| nqueens                    | 56.1 ms                                                     | 60.6 ms: 1.08x slower                                                      |
| chaos                      | 37.9 ms                                                     | 41.3 ms: 1.09x slower                                                      |
| python_startup             | 24.4 ms                                                     | 26.7 ms: 1.09x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 207 us: 1.11x slower                                                       |
| coverage                   | 45.3 ms                                                     | 50.5 ms: 1.11x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.37 ms: 1.12x slower                                                      |
| async_generators           | 223 ms                                                      | 253 ms: 1.14x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.24 ms: 1.14x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.19 ms: 1.16x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.17x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.9 ms: 1.18x slower                                                      |
| django_template            | 20.3 ms                                                     | 23.9 ms: 1.18x slower                                                      |
| raytrace                   | 153 ms                                                      | 183 ms: 1.20x slower                                                       |
| many_optionals             | 361 us                                                      | 604 us: 1.67x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 31.5 ms: 2.90x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (5): pylint, regex_compile, typing_runtime_protocols, logging_silent, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.069x faster

# HPT report

- Reliability score: 80.25% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
# Results vs. 3.13.0

- fork: python
- ref: 0f866cbfefd797b4dae2
- machine: windows-amd64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.072x faster
- HPT reliability: 53.86%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.68 sec: 1.09x slower                                                     |
| sphinx         | 617 ms                                                      | 651 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                       |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.30x faster                                                       |
| async_tree_io              | 513 ms                                                      | 396 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 391 ms: 1.27x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 345 ms: 1.11x faster                                                       |
| async_generators           | 223 ms                                                      | 242 ms: 1.09x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.12x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.8 ms: 1.16x faster                                                      |
| nbody          | 66.3 ms                                                     | 57.7 ms: 1.15x faster                                                      |
| pidigits       | 146 ms                                                      | 149 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.63 ms: 1.04x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.8 ms: 1.02x faster                                                      |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.16 sec: 1.18x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 114 us: 1.14x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 87.5 ms: 1.05x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.6 us: 1.03x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 52.2 ms: 1.02x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 36.7 ms: 1.01x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 6.32 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.6 ms: 1.07x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 206 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.42 ms: 1.21x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| django_template | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 491 us: 17.26x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 31.7 ms: 2.37x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.88x faster                                                       |
| mdp                        | 1.43 sec                                                    | 802 ms: 1.78x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                      |
| deepcopy                   | 223 us                                                      | 167 us: 1.34x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 17.8 us: 1.30x faster                                                      |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.30x faster                                                       |
| async_tree_io              | 513 ms                                                      | 396 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 391 ms: 1.27x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.42 ms: 1.21x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.16 sec: 1.18x faster                                                     |
| float                      | 50.8 ms                                                     | 43.8 ms: 1.16x faster                                                      |
| nbody                      | 66.3 ms                                                     | 57.7 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 114 us: 1.14x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.30 ms: 1.13x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.81 us: 1.12x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.36 ms: 1.11x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 345 ms: 1.11x faster                                                       |
| scimark_fft                | 175 ms                                                      | 160 ms: 1.10x faster                                                       |
| go                         | 84.7 ms                                                     | 78.0 ms: 1.09x faster                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.65 sec: 1.08x faster                                                     |
| pyflate                    | 283 ms                                                      | 264 ms: 1.07x faster                                                       |
| json                       | 3.30 ms                                                     | 3.11 ms: 1.06x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 87.5 ms: 1.05x faster                                                      |
| fannkuch                   | 252 ms                                                      | 241 ms: 1.05x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.63 ms: 1.04x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.6 us: 1.03x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 61.5 ms: 1.03x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.65 sec: 1.03x faster                                                     |
| regex_compile              | 80.7 ms                                                     | 78.8 ms: 1.02x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 52.2 ms: 1.02x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.01x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 36.7 ms: 1.01x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 104 us: 1.01x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 77.1 ms: 1.01x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 73.3 ms: 1.02x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| pidigits                   | 146 ms                                                      | 149 ms: 1.02x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.32 ms: 1.02x slower                                                      |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.6 ms: 1.02x slower                                                      |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 87.3 ms: 1.03x slower                                                      |
| connected_components       | 320 ms                                                      | 328 ms: 1.03x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 46.9 ms: 1.03x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 41.3 ms: 1.03x slower                                                      |
| sympy_expand               | 286 ms                                                      | 295 ms: 1.03x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 42.4 ms: 1.04x slower                                                      |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| chaos                      | 37.9 ms                                                     | 39.5 ms: 1.04x slower                                                      |
| shortest_path              | 355 ms                                                      | 372 ms: 1.05x slower                                                       |
| comprehensions             | 10.4 us                                                     | 10.9 us: 1.05x slower                                                      |
| generators                 | 19.0 ms                                                     | 20.0 ms: 1.05x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 59.2 ms: 1.05x slower                                                      |
| sphinx                     | 617 ms                                                      | 651 ms: 1.05x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                      |
| richards_super             | 29.8 ms                                                     | 31.6 ms: 1.06x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 60.5 ms: 1.07x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.6 ms: 1.07x slower                                                      |
| richards                   | 26.3 ms                                                     | 28.1 ms: 1.07x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 520 ms: 1.07x slower                                                       |
| async_generators           | 223 ms                                                      | 242 ms: 1.09x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.73 us: 1.09x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.14 ms: 1.09x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.07 sec: 1.09x slower                                                     |
| docutils                   | 1.53 sec                                                    | 1.68 sec: 1.09x slower                                                     |
| logging_simple             | 5.77 us                                                     | 6.32 us: 1.09x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.21 ms: 1.10x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.34 ms: 1.10x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 206 us: 1.11x slower                                                       |
| coverage                   | 45.3 ms                                                     | 50.5 ms: 1.11x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.12x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                                      |
| raytrace                   | 153 ms                                                      | 181 ms: 1.18x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.26 ms: 1.20x slower                                                      |
| many_optionals             | 361 us                                                      | 446 us: 1.23x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 17.1 ms: 1.57x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 322 ns: 5.89x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (4): pylint, pycparser, html5lib, genshi_xml
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.072x faster

# HPT report

- Reliability score: 53.86% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
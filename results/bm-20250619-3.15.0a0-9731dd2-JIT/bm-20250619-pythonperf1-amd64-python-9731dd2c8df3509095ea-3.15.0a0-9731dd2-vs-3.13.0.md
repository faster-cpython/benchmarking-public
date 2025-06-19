# Results vs. 3.13.0

- fork: python
- ref: 9731dd2c8df3509095ea
- machine: windows-amd64
- commit hash: 9731dd2
- commit date: 2025-06-19
- overall geometric mean: 1.075x faster
- HPT reliability: 57.77%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.69 sec: 1.10x slower                                                     |
| sphinx         | 617 ms                                                      | 645 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                       |
| async_tree_io              | 513 ms                                                      | 395 ms: 1.30x faster                                                       |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 390 ms: 1.28x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 167 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 327 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 338 ms: 1.13x faster                                                       |
| async_generators           | 223 ms                                                      | 242 ms: 1.09x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 52.4 ms: 1.26x faster                                                      |
| float          | 50.8 ms                                                     | 43.8 ms: 1.16x faster                                                      |
| pidigits       | 146 ms                                                      | 150 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.60 ms: 1.06x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.2 ms: 1.03x faster                                                      |
| regex_dna      | 115 ms                                                      | 118 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.16 sec: 1.18x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 112 us: 1.16x faster                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 51.1 ms: 1.05x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.5 us: 1.04x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 88.8 ms: 1.04x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 36.2 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.8 ms: 1.05x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 207 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.2 ms: 1.07x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.67 ms: 1.16x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.1 ms: 1.01x faster                                                      |
| django_template | 20.3 ms                                                     | 24.1 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 489 us: 17.30x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 33.1 ms: 2.28x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                       |
| mdp                        | 1.43 sec                                                    | 812 ms: 1.76x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                       |
| deepcopy                   | 223 us                                                      | 169 us: 1.32x faster                                                       |
| async_tree_io              | 513 ms                                                      | 395 ms: 1.30x faster                                                       |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.29x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.0 us: 1.28x faster                                                      |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 390 ms: 1.28x faster                                                       |
| nbody                      | 66.3 ms                                                     | 52.4 ms: 1.26x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 167 ms: 1.20x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.16 sec: 1.18x faster                                                     |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 327 ms: 1.16x faster                                                       |
| float                      | 50.8 ms                                                     | 43.8 ms: 1.16x faster                                                      |
| mako                       | 6.56 ms                                                     | 5.67 ms: 1.16x faster                                                      |
| unpickle_pure_python       | 130 us                                                      | 112 us: 1.16x faster                                                       |
| scimark_fft                | 175 ms                                                      | 153 ms: 1.14x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.29 ms: 1.14x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 338 ms: 1.13x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.80 us: 1.12x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.36 ms: 1.11x faster                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.61 sec: 1.10x faster                                                     |
| go                         | 84.7 ms                                                     | 77.0 ms: 1.10x faster                                                      |
| pyflate                    | 283 ms                                                      | 258 ms: 1.10x faster                                                       |
| json                       | 3.30 ms                                                     | 3.10 ms: 1.06x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.60 ms: 1.06x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 51.1 ms: 1.05x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.04x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.8 ms: 1.04x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.64 sec: 1.03x faster                                                     |
| fannkuch                   | 252 ms                                                      | 243 ms: 1.03x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 78.2 ms: 1.03x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.54 us: 1.03x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.8 ms: 1.03x faster                                                      |
| genshi_text                | 15.2 ms                                                     | 15.1 ms: 1.01x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 36.2 ms: 1.01x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 75.9 ms: 1.00x faster                                                      |
| shortest_path              | 355 ms                                                      | 361 ms: 1.02x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 105 us: 1.02x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 73.5 ms: 1.02x slower                                                      |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.02x slower                                                       |
| pidigits                   | 146 ms                                                      | 150 ms: 1.02x slower                                                       |
| connected_components       | 320 ms                                                      | 329 ms: 1.03x slower                                                       |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.7 ms: 1.03x slower                                                      |
| sympy_str                  | 167 ms                                                      | 172 ms: 1.03x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 87.8 ms: 1.03x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 41.4 ms: 1.03x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.8 ms: 1.03x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 47.2 ms: 1.04x slower                                                      |
| sympy_expand               | 286 ms                                                      | 296 ms: 1.04x slower                                                       |
| richards                   | 26.3 ms                                                     | 27.3 ms: 1.04x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.8 ms: 1.04x slower                                                      |
| sphinx                     | 617 ms                                                      | 645 ms: 1.05x slower                                                       |
| spectral_norm              | 63.4 ms                                                     | 66.5 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.8 ms: 1.05x slower                                                      |
| comprehensions             | 10.4 us                                                     | 10.9 us: 1.06x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 516 ms: 1.06x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 59.9 ms: 1.07x slower                                                      |
| chaos                      | 37.9 ms                                                     | 40.5 ms: 1.07x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 60.6 ms: 1.07x slower                                                      |
| python_startup             | 24.4 ms                                                     | 26.2 ms: 1.07x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.06 sec: 1.08x slower                                                     |
| create_gc_cycles           | 1.22 ms                                                     | 1.32 ms: 1.08x slower                                                      |
| async_generators           | 223 ms                                                      | 242 ms: 1.09x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.21 ms: 1.09x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.69 sec: 1.10x slower                                                     |
| logging_simple             | 5.77 us                                                     | 6.38 us: 1.11x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 207 us: 1.11x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.95 us: 1.13x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.22 ms: 1.13x slower                                                      |
| coverage                   | 45.3 ms                                                     | 51.8 ms: 1.14x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.18 ms: 1.15x slower                                                      |
| raytrace                   | 153 ms                                                      | 177 ms: 1.16x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.1 ms: 1.19x slower                                                      |
| many_optionals             | 361 us                                                      | 447 us: 1.24x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 17.2 ms: 1.58x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 319 ns: 5.84x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (5): pylint, json_dumps, html5lib, pycparser, genshi_xml
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250619-3.15.0a0-9731dd2-JIT/bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.075x faster

# HPT report

- Reliability score: 57.77% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
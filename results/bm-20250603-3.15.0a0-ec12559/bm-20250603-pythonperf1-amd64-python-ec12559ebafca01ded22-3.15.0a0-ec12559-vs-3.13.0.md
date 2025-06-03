# Results vs. 3.13.0

- fork: python
- ref: ec12559ebafca01ded22
- machine: windows-amd64
- commit hash: ec12559
- commit date: 2025-06-03
- overall geometric mean: 1.026x slower
- HPT reliability: 94.89%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 222 ms: 1.03x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                     |
| html5lib       | 38.2 ms                                                     | 38.9 ms: 1.02x slower                                                      |
| sphinx         | 617 ms                                                      | 645 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                       |
| async_tree_io              | 513 ms                                                      | 395 ms: 1.30x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 205 ms: 1.29x faster                                                       |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 399 ms: 1.25x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.12x faster                                                       |
| async_generators           | 223 ms                                                      | 235 ms: 1.05x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.17x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.7 ms: 1.14x faster                                                      |
| nbody          | 66.3 ms                                                     | 62.6 ms: 1.06x faster                                                      |
| pidigits       | 146 ms                                                      | 149 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.3 ms: 1.67x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.58 ms: 1.07x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 79.4 ms: 1.02x faster                                                      |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 88.3 ms: 1.04x faster                                                      |
| json_dumps           | 6.19 ms                                                     | 6.29 ms: 1.02x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 133 us: 1.02x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 55.8 ms: 1.04x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.6 ms: 1.05x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 39.1 ms: 1.07x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 211 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.5 ms: 1.16x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.45 ms: 1.02x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                      |
| genshi_xml      | 33.9 ms                                                     | 35.2 ms: 1.04x slower                                                      |
| django_template | 20.3 ms                                                     | 25.1 ms: 1.24x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 31.8 ms: 2.37x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.88x faster                                                       |
| mdp                        | 1.43 sec                                                    | 810 ms: 1.77x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.3 ms: 1.67x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                       |
| async_tree_io              | 513 ms                                                      | 395 ms: 1.30x faster                                                       |
| deepcopy                   | 223 us                                                      | 173 us: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 205 ms: 1.29x faster                                                       |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.2 us: 1.27x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 399 ms: 1.25x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| float                      | 50.8 ms                                                     | 44.7 ms: 1.14x faster                                                      |
| go                         | 84.7 ms                                                     | 75.3 ms: 1.12x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.12x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.86 us: 1.09x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 58.5 ms: 1.08x faster                                                      |
| json                       | 3.30 ms                                                     | 3.06 ms: 1.08x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.58 ms: 1.07x faster                                                      |
| nbody                      | 66.3 ms                                                     | 62.6 ms: 1.06x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.59 ms: 1.06x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.49 ms: 1.05x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.3 ms: 1.04x faster                                                      |
| mako                       | 6.56 ms                                                     | 6.45 ms: 1.02x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 79.4 ms: 1.02x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.2 ms: 1.01x faster                                                      |
| meteor_contest             | 72.0 ms                                                     | 71.4 ms: 1.01x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.58 us: 1.00x faster                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.4 ms: 1.00x slower                                                      |
| sympy_expand               | 286 ms                                                      | 288 ms: 1.01x slower                                                       |
| sympy_str                  | 167 ms                                                      | 168 ms: 1.01x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 77.0 ms: 1.01x slower                                                      |
| comprehensions             | 10.4 us                                                     | 10.5 us: 1.01x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.91 sec: 1.01x slower                                                     |
| json_dumps                 | 6.19 ms                                                     | 6.29 ms: 1.02x slower                                                      |
| pidigits                   | 146 ms                                                      | 149 ms: 1.02x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 40.8 ms: 1.02x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 38.9 ms: 1.02x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 105 us: 1.02x slower                                                       |
| scimark_fft                | 175 ms                                                      | 178 ms: 1.02x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 133 us: 1.02x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 46.7 ms: 1.03x slower                                                      |
| shortest_path              | 355 ms                                                      | 364 ms: 1.03x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 87.5 ms: 1.03x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                      |
| 2to3                       | 215 ms                                                      | 222 ms: 1.03x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 58.6 ms: 1.03x slower                                                      |
| pycparser                  | 695 ms                                                      | 719 ms: 1.03x slower                                                       |
| richards_super             | 29.8 ms                                                     | 30.8 ms: 1.04x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.2 ms: 1.04x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.7 ms: 1.04x slower                                                      |
| connected_components       | 320 ms                                                      | 332 ms: 1.04x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 35.2 ms: 1.04x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 55.8 ms: 1.04x slower                                                      |
| sphinx                     | 617 ms                                                      | 645 ms: 1.05x slower                                                       |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| chaos                      | 37.9 ms                                                     | 39.8 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.6 ms: 1.05x slower                                                      |
| async_generators           | 223 ms                                                      | 235 ms: 1.05x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.06 ms: 1.06x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                     |
| xml_etree_process          | 36.5 ms                                                     | 39.1 ms: 1.07x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.32 ms: 1.08x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 60.8 ms: 1.08x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.29 us: 1.09x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.14 ms: 1.09x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.76 us: 1.09x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 546 ms: 1.13x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 211 us: 1.13x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.11 sec: 1.14x slower                                                     |
| python_startup_no_site     | 16.9 ms                                                     | 19.5 ms: 1.16x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.20 ms: 1.16x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.17x slower                                                      |
| raytrace                   | 153 ms                                                      | 182 ms: 1.18x slower                                                       |
| many_optionals             | 361 us                                                      | 441 us: 1.22x slower                                                       |
| django_template            | 20.3 ms                                                     | 25.1 ms: 1.24x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 17.2 ms: 1.59x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 315 ns: 5.77x slower                                                       |
| coverage                   | 45.3 ms                                                     | 294 ms: 6.48x slower                                                       |
| thrift                     | 8.47 ms                                                     | 94.7 ms: 11.18x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (5): pylint, pyflate, tomli_loads, k_core, fannkuch
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250603-3.15.0a0-ec12559/bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.026x slower

# HPT report

- Reliability score: 94.89% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
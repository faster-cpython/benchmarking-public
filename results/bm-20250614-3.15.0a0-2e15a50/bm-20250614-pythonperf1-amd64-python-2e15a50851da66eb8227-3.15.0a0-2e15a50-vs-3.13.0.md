# Results vs. 3.13.0

- fork: python
- ref: 2e15a50851da66eb8227
- machine: windows-amd64
- commit hash: 2e15a50
- commit date: 2025-06-14
- overall geometric mean: 1.063x faster
- HPT reliability: 90.58%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                     |
| sphinx         | 617 ms                                                      | 633 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.89x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                       |
| async_tree_io              | 513 ms                                                      | 396 ms: 1.30x faster                                                       |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.30x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 389 ms: 1.28x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                       |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.4 ms: 1.17x faster                                                      |
| nbody          | 66.3 ms                                                     | 61.6 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.2 ms: 1.81x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.51 ms: 1.12x faster                                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.2 us: 1.06x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 88.2 ms: 1.05x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 132 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.1 ms: 1.06x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 56.7 ms: 1.06x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 39.1 ms: 1.07x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 208 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (2): tomli_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.68 ms: 1.02x slower                                                      |
| django_template | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 491 us: 17.25x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 32.0 ms: 2.36x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.89x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.2 ms: 1.81x faster                                                      |
| mdp                        | 1.43 sec                                                    | 804 ms: 1.78x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                       |
| deepcopy                   | 223 us                                                      | 171 us: 1.30x faster                                                       |
| async_tree_io              | 513 ms                                                      | 396 ms: 1.30x faster                                                       |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.30x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.28x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.0 us: 1.28x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 389 ms: 1.28x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                                       |
| float                      | 50.8 ms                                                     | 43.4 ms: 1.17x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| go                         | 84.7 ms                                                     | 74.7 ms: 1.13x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.51 ms: 1.12x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.83 us: 1.10x faster                                                      |
| json                       | 3.30 ms                                                     | 3.01 ms: 1.10x faster                                                      |
| nbody                      | 66.3 ms                                                     | 61.6 ms: 1.07x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.06x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.61 ms: 1.05x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.2 ms: 1.05x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.51 ms: 1.04x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 61.8 ms: 1.03x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.9 ms: 1.02x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 74.8 ms: 1.02x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.58 us: 1.01x faster                                                      |
| fannkuch                   | 252 ms                                                      | 253 ms: 1.00x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 72.5 ms: 1.01x slower                                                      |
| sympy_str                  | 167 ms                                                      | 168 ms: 1.01x slower                                                       |
| sympy_expand               | 286 ms                                                      | 289 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 132 us: 1.01x slower                                                       |
| mako                       | 6.56 ms                                                     | 6.68 ms: 1.02x slower                                                      |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.4 ms: 1.02x slower                                                      |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 58.1 ms: 1.02x slower                                                      |
| richards                   | 26.3 ms                                                     | 26.9 ms: 1.03x slower                                                      |
| sphinx                     | 617 ms                                                      | 633 ms: 1.03x slower                                                       |
| comprehensions             | 10.4 us                                                     | 10.6 us: 1.03x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.6 ms: 1.03x slower                                                      |
| pyflate                    | 283 ms                                                      | 291 ms: 1.03x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 3.95 ms: 1.03x slower                                                      |
| shortest_path              | 355 ms                                                      | 365 ms: 1.03x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 87.8 ms: 1.03x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.96 sec: 1.03x slower                                                     |
| crypto_pyaes               | 45.6 ms                                                     | 47.1 ms: 1.03x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 41.5 ms: 1.04x slower                                                      |
| scimark_fft                | 175 ms                                                      | 183 ms: 1.05x slower                                                       |
| connected_components       | 320 ms                                                      | 335 ms: 1.05x slower                                                       |
| chaos                      | 37.9 ms                                                     | 39.9 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.1 ms: 1.06x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 56.7 ms: 1.06x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                     |
| xml_etree_process          | 36.5 ms                                                     | 39.1 ms: 1.07x slower                                                      |
| python_startup             | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 61.3 ms: 1.09x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.34 ms: 1.09x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.15 ms: 1.10x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.85 us: 1.11x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.41 us: 1.11x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.09 sec: 1.12x slower                                                     |
| pickle_pure_python         | 186 us                                                      | 208 us: 1.12x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 544 ms: 1.12x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.14 ms: 1.13x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                      |
| coverage                   | 45.3 ms                                                     | 52.5 ms: 1.16x slower                                                      |
| django_template            | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                      |
| raytrace                   | 153 ms                                                      | 183 ms: 1.20x slower                                                       |
| many_optionals             | 361 us                                                      | 438 us: 1.21x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.9 ms: 1.56x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 320 ns: 5.86x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (13): pylint, typing_runtime_protocols, genshi_text, regex_compile, tomli_loads, sympy_integrate, regex_dna, pidigits, json_dumps, pycparser, genshi_xml, k_core, html5lib
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250614-3.15.0a0-2e15a50/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 90.58% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
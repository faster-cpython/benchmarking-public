# Results vs. 3.13.0

- fork: python
- ref: 605022aeb69ae19cae1c
- machine: windows-amd64
- commit hash: 605022a
- commit date: 2025-05-19
- overall geometric mean: 1.014x slower
- HPT reliability: 73.03%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                     |
| sphinx         | 617 ms                                                      | 642 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.36x faster                                                       |
| async_tree_io              | 513 ms                                                      | 395 ms: 1.30x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 205 ms: 1.29x faster                                                       |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 389 ms: 1.28x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 334 ms: 1.15x faster                                                       |
| async_generators           | 223 ms                                                      | 229 ms: 1.03x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 42.5 ms: 1.20x faster                                                      |
| nbody          | 66.3 ms                                                     | 61.6 ms: 1.08x faster                                                      |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.5 ms: 1.64x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 79.9 ms: 1.01x faster                                                      |
| regex_dna      | 115 ms                                                      | 118 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 88.2 ms: 1.04x faster                                                      |
| json_loads           | 15.1 us                                                     | 15.0 us: 1.01x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 136 us: 1.05x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.5 ms: 1.05x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 56.2 ms: 1.05x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 39.1 ms: 1.07x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 208 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (2): tomli_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.0 ms: 1.02x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 18.8 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.47 ms: 1.01x faster                                                      |
| django_template | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 29.6 ms: 2.55x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.85x faster                                                       |
| mdp                        | 1.43 sec                                                    | 779 ms: 1.84x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.5 ms: 1.64x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.36x faster                                                       |
| async_tree_io              | 513 ms                                                      | 395 ms: 1.30x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 205 ms: 1.29x faster                                                       |
| deepcopy                   | 223 us                                                      | 173 us: 1.29x faster                                                       |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 389 ms: 1.28x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 19.2 us: 1.20x faster                                                      |
| float                      | 50.8 ms                                                     | 42.5 ms: 1.20x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 334 ms: 1.15x faster                                                       |
| json                       | 3.30 ms                                                     | 2.95 ms: 1.12x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 57.5 ms: 1.10x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.85 us: 1.10x faster                                                      |
| go                         | 84.7 ms                                                     | 78.1 ms: 1.08x faster                                                      |
| nbody                      | 66.3 ms                                                     | 61.6 ms: 1.08x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.46 ms: 1.06x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.61 ms: 1.05x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.2 ms: 1.04x faster                                                      |
| fannkuch                   | 252 ms                                                      | 246 ms: 1.02x faster                                                       |
| mako                       | 6.56 ms                                                     | 6.47 ms: 1.01x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.57 us: 1.01x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 79.9 ms: 1.01x faster                                                      |
| json_loads                 | 15.1 us                                                     | 15.0 us: 1.01x faster                                                      |
| pyflate                    | 283 ms                                                      | 280 ms: 1.01x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.4 ms: 1.01x faster                                                      |
| scimark_fft                | 175 ms                                                      | 174 ms: 1.00x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 76.0 ms: 1.00x faster                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.89 sec: 1.00x slower                                                     |
| sympy_integrate            | 12.3 ms                                                     | 12.4 ms: 1.01x slower                                                      |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 489 ms: 1.01x slower                                                       |
| sympy_expand               | 286 ms                                                      | 289 ms: 1.01x slower                                                       |
| sympy_str                  | 167 ms                                                      | 169 ms: 1.01x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 73.0 ms: 1.01x slower                                                      |
| connected_components       | 320 ms                                                      | 325 ms: 1.02x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 994 ms: 1.02x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 57.8 ms: 1.02x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 40.9 ms: 1.02x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.0 ms: 1.02x slower                                                      |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.03x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 46.9 ms: 1.03x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.0 ms: 1.03x slower                                                      |
| async_generators           | 223 ms                                                      | 229 ms: 1.03x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 87.7 ms: 1.03x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.8 ms: 1.03x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 840 us: 1.04x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 3.99 ms: 1.04x slower                                                      |
| sphinx                     | 617 ms                                                      | 642 ms: 1.04x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.8 ms: 1.04x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 108 us: 1.05x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 136 us: 1.05x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.28 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.5 ms: 1.05x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 56.2 ms: 1.05x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                     |
| gc_traversal               | 1.96 ms                                                     | 2.08 ms: 1.06x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 39.1 ms: 1.07x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 60.6 ms: 1.08x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 92.0 ms: 1.09x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.4 us: 1.10x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 18.8 ms: 1.11x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.44 us: 1.12x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.91 us: 1.12x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 208 us: 1.12x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.12 ms: 1.12x slower                                                      |
| raytrace                   | 153 ms                                                      | 178 ms: 1.16x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                      |
| many_optionals             | 361 us                                                      | 441 us: 1.22x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 17.1 ms: 1.58x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 316 ns: 5.78x slower                                                       |
| coverage                   | 45.3 ms                                                     | 295 ms: 6.51x slower                                                       |
| thrift                     | 8.47 ms                                                     | 92.4 ms: 10.92x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (10): pylint, k_core, tomli_loads, json_dumps, shortest_path, genshi_text, chaos, html5lib, pycparser, genshi_xml
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250519-3.15.0a0-605022a/bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.014x slower

# HPT report

- Reliability score: 73.03% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
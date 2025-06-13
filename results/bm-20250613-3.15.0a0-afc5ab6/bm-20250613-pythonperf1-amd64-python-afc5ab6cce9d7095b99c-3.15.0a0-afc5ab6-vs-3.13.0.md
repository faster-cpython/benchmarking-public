# Results vs. 3.13.0

- fork: python
- ref: afc5ab6cce9d7095b99c
- machine: windows-amd64
- commit hash: afc5ab6
- commit date: 2025-06-13
- overall geometric mean: 1.026x slower
- HPT reliability: 99.63%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                     |
| sphinx         | 617 ms                                                      | 637 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.92x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.32x faster                                                       |
| async_tree_io              | 513 ms                                                      | 403 ms: 1.27x faster                                                       |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.27x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 392 ms: 1.27x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 210 ms: 1.26x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.11x faster                                                       |
| async_generators           | 223 ms                                                      | 234 ms: 1.05x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.11x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.5 ms: 1.14x faster                                                      |
| pidigits       | 146 ms                                                      | 149 ms: 1.02x slower                                                       |
| nbody          | 66.3 ms                                                     | 67.5 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.5 ms: 1.77x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.47 ms: 1.15x faster                                                      |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.3 us: 1.06x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 88.3 ms: 1.04x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                     |
| json_dumps           | 6.19 ms                                                     | 6.27 ms: 1.01x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 136 us: 1.05x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 56.4 ms: 1.05x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.6 ms: 1.07x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 39.3 ms: 1.08x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 216 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.2 ms: 1.07x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.64 ms: 1.01x slower                                                      |
| django_template | 20.3 ms                                                     | 23.9 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 31.3 ms: 2.41x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.92x faster                                                       |
| mdp                        | 1.43 sec                                                    | 805 ms: 1.78x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.5 ms: 1.77x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.32x faster                                                       |
| deepcopy                   | 223 us                                                      | 174 us: 1.28x faster                                                       |
| async_tree_io              | 513 ms                                                      | 403 ms: 1.27x faster                                                       |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.27x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 392 ms: 1.27x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 210 ms: 1.26x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.4 us: 1.25x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.47 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                       |
| float                      | 50.8 ms                                                     | 44.5 ms: 1.14x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.11x faster                                                       |
| go                         | 84.7 ms                                                     | 76.8 ms: 1.10x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.84 us: 1.10x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 58.1 ms: 1.09x faster                                                      |
| json                       | 3.30 ms                                                     | 3.08 ms: 1.07x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.06x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.3 ms: 1.04x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.67 ms: 1.04x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.56 ms: 1.02x faster                                                      |
| fannkuch                   | 252 ms                                                      | 253 ms: 1.01x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.4 ms: 1.01x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 72.7 ms: 1.01x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 104 us: 1.01x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                     |
| scimark_sor                | 76.2 ms                                                     | 77.1 ms: 1.01x slower                                                      |
| sympy_str                  | 167 ms                                                      | 169 ms: 1.01x slower                                                       |
| mako                       | 6.56 ms                                                     | 6.64 ms: 1.01x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.27 ms: 1.01x slower                                                      |
| shortest_path              | 355 ms                                                      | 360 ms: 1.01x slower                                                       |
| pidigits                   | 146 ms                                                      | 149 ms: 1.02x slower                                                       |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                       |
| nbody                      | 66.3 ms                                                     | 67.5 ms: 1.02x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 40.9 ms: 1.02x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.4 ms: 1.02x slower                                                      |
| pyflate                    | 283 ms                                                      | 290 ms: 1.02x slower                                                       |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                       |
| comprehensions             | 10.4 us                                                     | 10.7 us: 1.03x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 87.7 ms: 1.03x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.96 sec: 1.03x slower                                                     |
| sphinx                     | 617 ms                                                      | 637 ms: 1.03x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 42.1 ms: 1.03x slower                                                      |
| scimark_fft                | 175 ms                                                      | 182 ms: 1.04x slower                                                       |
| chaos                      | 37.9 ms                                                     | 39.5 ms: 1.04x slower                                                      |
| connected_components       | 320 ms                                                      | 334 ms: 1.04x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 47.6 ms: 1.04x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 136 us: 1.05x slower                                                       |
| async_generators           | 223 ms                                                      | 234 ms: 1.05x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 59.6 ms: 1.05x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 56.4 ms: 1.05x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 59.5 ms: 1.06x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.9 ms: 1.06x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.08 ms: 1.06x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                     |
| richards_super             | 29.8 ms                                                     | 31.7 ms: 1.06x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.6 ms: 1.07x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.60 us: 1.07x slower                                                      |
| python_startup             | 24.4 ms                                                     | 26.2 ms: 1.07x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.20 us: 1.07x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 39.3 ms: 1.08x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.32 ms: 1.08x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.16 ms: 1.10x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.11x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 553 ms: 1.14x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.13 sec: 1.16x slower                                                     |
| pickle_pure_python         | 186 us                                                      | 216 us: 1.16x slower                                                       |
| raytrace                   | 153 ms                                                      | 180 ms: 1.17x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.22 ms: 1.18x slower                                                      |
| django_template            | 20.3 ms                                                     | 23.9 ms: 1.18x slower                                                      |
| many_optionals             | 361 us                                                      | 440 us: 1.22x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 17.2 ms: 1.58x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 322 ns: 5.90x slower                                                       |
| coverage                   | 45.3 ms                                                     | 296 ms: 6.53x slower                                                       |
| thrift                     | 8.47 ms                                                     | 98.1 ms: 11.59x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (9): pylint, sqlite_synth, regex_compile, sympy_expand, genshi_text, genshi_xml, k_core, html5lib, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250613-3.15.0a0-afc5ab6/bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.026x slower

# HPT report

- Reliability score: 99.63% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
# Results vs. 3.13.0

- fork: python
- ref: b150b6aca7b17efe1bb1
- machine: windows-amd64
- commit hash: b150b6a
- commit date: 2025-06-09
- overall geometric mean: 1.017x slower
- HPT reliability: 88.05%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                     |
| sphinx         | 617 ms                                                      | 636 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 164 ms: 1.83x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                       |
| async_tree_io              | 513 ms                                                      | 395 ms: 1.30x faster                                                       |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 389 ms: 1.28x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.19x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                       |
| async_generators           | 223 ms                                                      | 229 ms: 1.03x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.5 ms: 1.17x faster                                                      |
| nbody          | 66.3 ms                                                     | 62.7 ms: 1.06x faster                                                      |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.53 ms: 1.11x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.8 ms: 1.02x faster                                                      |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.3 us: 1.06x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 87.9 ms: 1.05x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.35 sec: 1.01x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 132 us: 1.02x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.29 ms: 1.02x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 56.1 ms: 1.05x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.8 ms: 1.05x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 39.1 ms: 1.07x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 214 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.6 ms: 1.05x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.1 ms: 1.01x faster                                                      |
| django_template | 20.3 ms                                                     | 24.3 ms: 1.20x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 31.8 ms: 2.36x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 164 ms: 1.83x faster                                                       |
| mdp                        | 1.43 sec                                                    | 808 ms: 1.77x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                       |
| deepcopy                   | 223 us                                                      | 172 us: 1.30x faster                                                       |
| async_tree_io              | 513 ms                                                      | 395 ms: 1.30x faster                                                       |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 17.9 us: 1.29x faster                                                      |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 389 ms: 1.28x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.19x faster                                                       |
| float                      | 50.8 ms                                                     | 43.5 ms: 1.17x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                       |
| go                         | 84.7 ms                                                     | 75.0 ms: 1.13x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.53 ms: 1.11x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.84 us: 1.10x faster                                                      |
| json                       | 3.30 ms                                                     | 3.02 ms: 1.09x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 59.0 ms: 1.08x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.06x faster                                                      |
| nbody                      | 66.3 ms                                                     | 62.7 ms: 1.06x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.59 ms: 1.06x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 87.9 ms: 1.05x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.52 ms: 1.03x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 78.8 ms: 1.02x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 74.7 ms: 1.02x faster                                                      |
| typing_runtime_protocols   | 103 us                                                      | 102 us: 1.02x faster                                                       |
| scimark_fft                | 175 ms                                                      | 172 ms: 1.01x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.35 sec: 1.01x faster                                                     |
| genshi_text                | 15.2 ms                                                     | 15.1 ms: 1.01x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.5 ms: 1.01x faster                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.4 ms: 1.01x slower                                                      |
| sympy_str                  | 167 ms                                                      | 168 ms: 1.01x slower                                                       |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                       |
| sympy_expand               | 286 ms                                                      | 289 ms: 1.01x slower                                                       |
| pyflate                    | 283 ms                                                      | 286 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 132 us: 1.02x slower                                                       |
| fannkuch                   | 252 ms                                                      | 256 ms: 1.02x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.29 ms: 1.02x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.92 sec: 1.02x slower                                                     |
| dulwich_log                | 40.1 ms                                                     | 40.9 ms: 1.02x slower                                                      |
| shortest_path              | 355 ms                                                      | 363 ms: 1.02x slower                                                       |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| connected_components       | 320 ms                                                      | 327 ms: 1.02x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 87.4 ms: 1.03x slower                                                      |
| async_generators           | 223 ms                                                      | 229 ms: 1.03x slower                                                       |
| sphinx                     | 617 ms                                                      | 636 ms: 1.03x slower                                                       |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| richards                   | 26.3 ms                                                     | 27.0 ms: 1.03x slower                                                      |
| comprehensions             | 10.4 us                                                     | 10.7 us: 1.03x slower                                                      |
| chaos                      | 37.9 ms                                                     | 39.1 ms: 1.03x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.7 ms: 1.03x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.04x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 47.4 ms: 1.04x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 59.0 ms: 1.04x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.01 ms: 1.04x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 58.9 ms: 1.05x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 56.1 ms: 1.05x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.6 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.8 ms: 1.05x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                     |
| xml_etree_process          | 36.5 ms                                                     | 39.1 ms: 1.07x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.68 us: 1.08x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.33 ms: 1.08x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.28 us: 1.09x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 531 ms: 1.10x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.18 ms: 1.11x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.09 sec: 1.12x slower                                                     |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.18 ms: 1.15x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 214 us: 1.15x slower                                                       |
| raytrace                   | 153 ms                                                      | 179 ms: 1.16x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.3 ms: 1.20x slower                                                      |
| many_optionals             | 361 us                                                      | 435 us: 1.20x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 17.0 ms: 1.57x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 325 ns: 5.95x slower                                                       |
| coverage                   | 45.3 ms                                                     | 296 ms: 6.54x slower                                                       |
| thrift                     | 8.47 ms                                                     | 93.2 ms: 11.01x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (8): pylint, html5lib, meteor_contest, k_core, sqlite_synth, mako, genshi_xml, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250609-3.15.0a0-b150b6a/bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.017x slower

# HPT report

- Reliability score: 88.05% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
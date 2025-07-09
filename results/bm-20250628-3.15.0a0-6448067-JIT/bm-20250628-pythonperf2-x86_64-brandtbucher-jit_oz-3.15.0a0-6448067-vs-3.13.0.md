# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_oz
- machine: linux-x86_64
- commit hash: 6448067
- commit date: 2025-06-28
- overall geometric mean: 1.063x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 286 ms: 1.02x faster                                                |
| docutils       | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                              |
| html5lib       | 73.5 ms                                                      | 68.2 ms: 1.08x faster                                               |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                              |
| Geometric mean | (ref)                                                        | 1.02x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 330 ms: 1.41x faster                                                |
| async_tree_memoization     | 453 ms                                                       | 332 ms: 1.36x faster                                                |
| async_tree_io              | 843 ms                                                       | 627 ms: 1.34x faster                                                |
| async_tree_io_tg           | 831 ms                                                       | 627 ms: 1.33x faster                                                |
| async_tree_none            | 376 ms                                                       | 284 ms: 1.32x faster                                                |
| async_tree_none_tg         | 346 ms                                                       | 272 ms: 1.27x faster                                                |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 503 ms: 1.20x faster                                                |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 506 ms: 1.15x faster                                                |
| async_generators           | 457 ms                                                       | 448 ms: 1.02x faster                                                |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                               |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 66.0 ms: 1.23x faster                                               |
| pidigits       | 252 ms                                                       | 258 ms: 1.02x slower                                                |
| nbody          | 89.3 ms                                                      | 102 ms: 1.14x slower                                                |
| Geometric mean | (ref)                                                        | 1.02x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.0 ms: 1.13x faster                                               |
| regex_dna      | 247 ms                                                       | 220 ms: 1.12x faster                                                |
| regex_effbot   | 3.67 ms                                                      | 3.49 ms: 1.05x faster                                               |
| regex_compile  | 143 ms                                                       | 137 ms: 1.04x faster                                                |
| Geometric mean | (ref)                                                        | 1.09x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.11 sec: 1.16x faster                                              |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.10x faster                                                |
| xml_etree_iterparse  | 103 ms                                                       | 95.9 ms: 1.07x faster                                               |
| xml_etree_process    | 61.2 ms                                                      | 58.0 ms: 1.05x faster                                               |
| xml_etree_generate   | 86.5 ms                                                      | 82.9 ms: 1.04x faster                                               |
| unpickle_pure_python | 217 us                                                       | 215 us: 1.01x faster                                                |
| json_loads           | 24.7 us                                                      | 25.1 us: 1.02x slower                                               |
| pickle_pure_python   | 323 us                                                       | 340 us: 1.05x slower                                                |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                        |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                               |
| python_startup_no_site | 8.96 ms                                                      | 8.85 ms: 1.01x faster                                               |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text    | 26.2 ms                                                      | 23.0 ms: 1.14x faster                                               |
| genshi_xml     | 57.1 ms                                                      | 55.4 ms: 1.03x faster                                               |
| mako           | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                               |
| Geometric mean | (ref)                                                        | 1.03x faster                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.31 sec: 1.94x faster                                              |
| richards                   | 52.9 ms                                                      | 35.8 ms: 1.48x faster                                               |
| richards_super             | 59.6 ms                                                      | 41.8 ms: 1.43x faster                                               |
| async_tree_memoization_tg  | 466 ms                                                       | 330 ms: 1.41x faster                                                |
| deepcopy                   | 392 us                                                       | 281 us: 1.40x faster                                                |
| deepcopy_memo              | 38.6 us                                                      | 28.3 us: 1.37x faster                                               |
| async_tree_memoization     | 453 ms                                                       | 332 ms: 1.36x faster                                                |
| async_tree_io              | 843 ms                                                       | 627 ms: 1.34x faster                                                |
| async_tree_io_tg           | 831 ms                                                       | 627 ms: 1.33x faster                                                |
| async_tree_none            | 376 ms                                                       | 284 ms: 1.32x faster                                                |
| async_tree_none_tg         | 346 ms                                                       | 272 ms: 1.27x faster                                                |
| go                         | 162 ms                                                       | 131 ms: 1.24x faster                                                |
| float                      | 81.3 ms                                                      | 66.0 ms: 1.23x faster                                               |
| scimark_sor                | 123 ms                                                       | 103 ms: 1.20x faster                                                |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 503 ms: 1.20x faster                                                |
| deepcopy_reduce            | 3.54 us                                                      | 2.99 us: 1.18x faster                                               |
| pyflate                    | 503 ms                                                       | 425 ms: 1.18x faster                                                |
| tomli_loads                | 2.46 sec                                                     | 2.11 sec: 1.16x faster                                              |
| dulwich_log                | 68.2 ms                                                      | 58.7 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 506 ms: 1.15x faster                                                |
| generators                 | 33.6 ms                                                      | 29.5 ms: 1.14x faster                                               |
| genshi_text                | 26.2 ms                                                      | 23.0 ms: 1.14x faster                                               |
| deltablue                  | 3.42 ms                                                      | 3.01 ms: 1.14x faster                                               |
| regex_v8                   | 26.1 ms                                                      | 23.0 ms: 1.13x faster                                               |
| regex_dna                  | 247 ms                                                       | 220 ms: 1.12x faster                                                |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.10x faster                                                |
| telco                      | 8.79 ms                                                      | 8.14 ms: 1.08x faster                                               |
| html5lib                   | 73.5 ms                                                      | 68.2 ms: 1.08x faster                                               |
| pylint                     | 347 ms                                                       | 322 ms: 1.08x faster                                                |
| thrift                     | 901 us                                                       | 840 us: 1.07x faster                                                |
| xml_etree_iterparse        | 103 ms                                                       | 95.9 ms: 1.07x faster                                               |
| json                       | 5.69 ms                                                      | 5.31 ms: 1.07x faster                                               |
| logging_simple             | 6.39 us                                                      | 6.05 us: 1.06x faster                                               |
| k_core                     | 2.17 sec                                                     | 2.06 sec: 1.05x faster                                              |
| xml_etree_process          | 61.2 ms                                                      | 58.0 ms: 1.05x faster                                               |
| regex_effbot               | 3.67 ms                                                      | 3.49 ms: 1.05x faster                                               |
| pprint_pformat             | 1.72 sec                                                     | 1.64 sec: 1.05x faster                                              |
| logging_format             | 6.94 us                                                      | 6.62 us: 1.05x faster                                               |
| sympy_integrate            | 23.6 ms                                                      | 22.5 ms: 1.05x faster                                               |
| xml_etree_generate         | 86.5 ms                                                      | 82.9 ms: 1.04x faster                                               |
| pprint_safe_repr           | 843 ms                                                       | 808 ms: 1.04x faster                                                |
| regex_compile              | 143 ms                                                       | 137 ms: 1.04x faster                                                |
| connected_components       | 432 ms                                                       | 415 ms: 1.04x faster                                                |
| python_startup             | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                               |
| logging_silent             | 97.9 ns                                                      | 94.4 ns: 1.04x faster                                               |
| sqlite_synth               | 2.91 us                                                      | 2.81 us: 1.04x faster                                               |
| scimark_lu                 | 98.7 ms                                                      | 95.7 ms: 1.03x faster                                               |
| genshi_xml                 | 57.1 ms                                                      | 55.4 ms: 1.03x faster                                               |
| pathlib                    | 17.5 ms                                                      | 17.0 ms: 1.03x faster                                               |
| scimark_monte_carlo        | 66.1 ms                                                      | 64.3 ms: 1.03x faster                                               |
| meteor_contest             | 130 ms                                                       | 126 ms: 1.03x faster                                                |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                              |
| shortest_path              | 460 ms                                                       | 449 ms: 1.03x faster                                                |
| 2to3                       | 293 ms                                                       | 286 ms: 1.02x faster                                                |
| sympy_str                  | 298 ms                                                       | 292 ms: 1.02x faster                                                |
| async_generators           | 457 ms                                                       | 448 ms: 1.02x faster                                                |
| sympy_expand               | 509 ms                                                       | 500 ms: 1.02x faster                                                |
| sympy_sum                  | 155 ms                                                       | 152 ms: 1.02x faster                                                |
| coverage                   | 80.0 ms                                                      | 78.9 ms: 1.01x faster                                               |
| bpe_tokeniser              | 5.09 sec                                                     | 5.02 sec: 1.01x faster                                              |
| python_startup_no_site     | 8.96 ms                                                      | 8.85 ms: 1.01x faster                                               |
| chaos                      | 60.2 ms                                                      | 59.6 ms: 1.01x faster                                               |
| unpickle_pure_python       | 217 us                                                       | 215 us: 1.01x faster                                                |
| hexiom                     | 6.55 ms                                                      | 6.52 ms: 1.01x faster                                               |
| pycparser                  | 1.24 sec                                                     | 1.26 sec: 1.01x slower                                              |
| json_loads                 | 24.7 us                                                      | 25.1 us: 1.02x slower                                               |
| typing_runtime_protocols   | 169 us                                                       | 172 us: 1.02x slower                                                |
| pidigits                   | 252 ms                                                       | 258 ms: 1.02x slower                                                |
| docutils                   | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                              |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                               |
| scimark_fft                | 328 ms                                                       | 343 ms: 1.05x slower                                                |
| pickle_pure_python         | 323 us                                                       | 340 us: 1.05x slower                                                |
| create_gc_cycles           | 2.68 ms                                                      | 2.83 ms: 1.06x slower                                               |
| spectral_norm              | 97.0 ms                                                      | 102 ms: 1.06x slower                                                |
| raytrace                   | 273 ms                                                       | 288 ms: 1.06x slower                                                |
| mako                       | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                               |
| nqueens                    | 90.7 ms                                                      | 96.6 ms: 1.07x slower                                               |
| comprehensions             | 17.0 us                                                      | 18.4 us: 1.08x slower                                               |
| many_optionals             | 930 us                                                       | 1.05 ms: 1.13x slower                                               |
| crypto_pyaes               | 73.3 ms                                                      | 83.3 ms: 1.14x slower                                               |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.44 ms: 1.14x slower                                               |
| nbody                      | 89.3 ms                                                      | 102 ms: 1.14x slower                                                |
| fannkuch                   | 363 ms                                                       | 437 ms: 1.20x slower                                                |
| gc_traversal               | 4.74 ms                                                      | 6.47 ms: 1.36x slower                                               |
| subparsers                 | 17.5 ms                                                      | 24.9 ms: 1.43x slower                                               |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                        |

Benchmark hidden because not significant (4): asyncio_websockets, django_template, djangocms, json_dumps
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250628-3.15.0a0-6448067-JIT/bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.11x
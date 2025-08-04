# Results vs. 3.13.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3ec3d05
- commit date: 2025-08-03
- overall geometric mean: 1.040x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 286 ms: 1.03x faster                                        |
| docutils       | 2.83 sec                                                     | 2.94 sec: 1.04x slower                                      |
| html5lib       | 73.5 ms                                                      | 67.7 ms: 1.09x faster                                       |
| sphinx         | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                      |
| Geometric mean | (ref)                                                        | 1.02x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                        |
| async_tree_memoization     | 453 ms                                                       | 326 ms: 1.39x faster                                        |
| async_tree_io              | 843 ms                                                       | 628 ms: 1.34x faster                                        |
| async_tree_none            | 376 ms                                                       | 281 ms: 1.34x faster                                        |
| async_tree_io_tg           | 831 ms                                                       | 637 ms: 1.31x faster                                        |
| async_tree_none_tg         | 346 ms                                                       | 270 ms: 1.28x faster                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 503 ms: 1.20x faster                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 506 ms: 1.15x faster                                        |
| async_generators           | 457 ms                                                       | 440 ms: 1.04x faster                                        |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                        |
| coroutines                 | 21.6 ms                                                      | 22.4 ms: 1.04x slower                                       |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 81.3 ms                                                      | 64.6 ms: 1.26x faster                                       |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                        |
| nbody          | 89.3 ms                                                      | 99.1 ms: 1.11x slower                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.3 ms: 1.12x faster                                       |
| regex_dna      | 247 ms                                                       | 227 ms: 1.09x faster                                        |
| regex_compile  | 143 ms                                                       | 135 ms: 1.06x faster                                        |
| regex_effbot   | 3.67 ms                                                      | 3.64 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.92 sec: 1.28x faster                                      |
| unpickle_pure_python | 217 us                                                       | 194 us: 1.12x faster                                        |
| xml_etree_process    | 61.2 ms                                                      | 55.5 ms: 1.10x faster                                       |
| xml_etree_generate   | 86.5 ms                                                      | 80.5 ms: 1.08x faster                                       |
| xml_etree_parse      | 150 ms                                                       | 141 ms: 1.07x faster                                        |
| xml_etree_iterparse  | 103 ms                                                       | 97.8 ms: 1.05x faster                                       |
| pickle_pure_python   | 323 us                                                       | 332 us: 1.03x slower                                        |
| json_loads           | 24.7 us                                                      | 26.5 us: 1.08x slower                                       |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.4 ms: 1.03x faster                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.84 ms: 1.01x faster                                       |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 22.9 ms: 1.14x faster                                       |
| mako            | 10.4 ms                                                      | 9.78 ms: 1.06x faster                                       |
| genshi_xml      | 57.1 ms                                                      | 55.1 ms: 1.04x faster                                       |
| django_template | 36.4 ms                                                      | 35.5 ms: 1.02x faster                                       |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.28 sec: 1.98x faster                                      |
| richards                   | 52.9 ms                                                      | 35.4 ms: 1.50x faster                                       |
| richards_super             | 59.6 ms                                                      | 41.4 ms: 1.44x faster                                       |
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                        |
| deepcopy                   | 392 us                                                       | 280 us: 1.40x faster                                        |
| async_tree_memoization     | 453 ms                                                       | 326 ms: 1.39x faster                                        |
| deepcopy_memo              | 38.6 us                                                      | 28.1 us: 1.37x faster                                       |
| async_tree_io              | 843 ms                                                       | 628 ms: 1.34x faster                                        |
| async_tree_none            | 376 ms                                                       | 281 ms: 1.34x faster                                        |
| async_tree_io_tg           | 831 ms                                                       | 637 ms: 1.31x faster                                        |
| tomli_loads                | 2.46 sec                                                     | 1.92 sec: 1.28x faster                                      |
| async_tree_none_tg         | 346 ms                                                       | 270 ms: 1.28x faster                                        |
| go                         | 162 ms                                                       | 129 ms: 1.26x faster                                        |
| float                      | 81.3 ms                                                      | 64.6 ms: 1.26x faster                                       |
| pyflate                    | 503 ms                                                       | 408 ms: 1.23x faster                                        |
| scimark_sor                | 123 ms                                                       | 101 ms: 1.22x faster                                        |
| spectral_norm              | 97.0 ms                                                      | 79.7 ms: 1.22x faster                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 503 ms: 1.20x faster                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.98 us: 1.19x faster                                       |
| deltablue                  | 3.42 ms                                                      | 2.91 ms: 1.17x faster                                       |
| dulwich_log                | 68.2 ms                                                      | 58.8 ms: 1.16x faster                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 506 ms: 1.15x faster                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.50 sec: 1.15x faster                                      |
| genshi_text                | 26.2 ms                                                      | 22.9 ms: 1.14x faster                                       |
| generators                 | 33.6 ms                                                      | 29.5 ms: 1.14x faster                                       |
| pprint_safe_repr           | 843 ms                                                       | 741 ms: 1.14x faster                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.51 sec: 1.13x faster                                      |
| regex_v8                   | 26.1 ms                                                      | 23.3 ms: 1.12x faster                                       |
| unpickle_pure_python       | 217 us                                                       | 194 us: 1.12x faster                                        |
| scimark_fft                | 328 ms                                                       | 297 ms: 1.10x faster                                        |
| xml_etree_process          | 61.2 ms                                                      | 55.5 ms: 1.10x faster                                       |
| regex_dna                  | 247 ms                                                       | 227 ms: 1.09x faster                                        |
| html5lib                   | 73.5 ms                                                      | 67.7 ms: 1.09x faster                                       |
| k_core                     | 2.17 sec                                                     | 2.01 sec: 1.08x faster                                      |
| xml_etree_generate         | 86.5 ms                                                      | 80.5 ms: 1.08x faster                                       |
| thrift                     | 901 us                                                       | 838 us: 1.07x faster                                        |
| meteor_contest             | 130 ms                                                       | 121 ms: 1.07x faster                                        |
| pylint                     | 347 ms                                                       | 324 ms: 1.07x faster                                        |
| xml_etree_parse            | 150 ms                                                       | 141 ms: 1.07x faster                                        |
| connected_components       | 432 ms                                                       | 407 ms: 1.06x faster                                        |
| mako                       | 10.4 ms                                                      | 9.78 ms: 1.06x faster                                       |
| regex_compile              | 143 ms                                                       | 135 ms: 1.06x faster                                        |
| hexiom                     | 6.55 ms                                                      | 6.21 ms: 1.06x faster                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 62.8 ms: 1.05x faster                                       |
| xml_etree_iterparse        | 103 ms                                                       | 97.8 ms: 1.05x faster                                       |
| pathlib                    | 17.5 ms                                                      | 16.7 ms: 1.05x faster                                       |
| sympy_integrate            | 23.6 ms                                                      | 22.5 ms: 1.05x faster                                       |
| logging_simple             | 6.39 us                                                      | 6.10 us: 1.05x faster                                       |
| logging_silent             | 97.9 ns                                                      | 93.7 ns: 1.04x faster                                       |
| shortest_path              | 460 ms                                                       | 442 ms: 1.04x faster                                        |
| json                       | 5.69 ms                                                      | 5.48 ms: 1.04x faster                                       |
| logging_format             | 6.94 us                                                      | 6.69 us: 1.04x faster                                       |
| async_generators           | 457 ms                                                       | 440 ms: 1.04x faster                                        |
| genshi_xml                 | 57.1 ms                                                      | 55.1 ms: 1.04x faster                                       |
| sqlite_synth               | 2.91 us                                                      | 2.81 us: 1.04x faster                                       |
| scimark_lu                 | 98.7 ms                                                      | 95.4 ms: 1.03x faster                                       |
| python_startup             | 15.9 ms                                                      | 15.4 ms: 1.03x faster                                       |
| sympy_str                  | 298 ms                                                       | 291 ms: 1.03x faster                                        |
| 2to3                       | 293 ms                                                       | 286 ms: 1.03x faster                                        |
| django_template            | 36.4 ms                                                      | 35.5 ms: 1.02x faster                                       |
| sympy_expand               | 509 ms                                                       | 498 ms: 1.02x faster                                        |
| sphinx                     | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                      |
| chaos                      | 60.2 ms                                                      | 59.0 ms: 1.02x faster                                       |
| sympy_sum                  | 155 ms                                                       | 152 ms: 1.02x faster                                        |
| python_startup_no_site     | 8.96 ms                                                      | 8.84 ms: 1.01x faster                                       |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                        |
| regex_effbot               | 3.67 ms                                                      | 3.64 ms: 1.01x faster                                       |
| typing_runtime_protocols   | 169 us                                                       | 171 us: 1.01x slower                                        |
| coverage                   | 80.0 ms                                                      | 80.7 ms: 1.01x slower                                       |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                        |
| comprehensions             | 17.0 us                                                      | 17.3 us: 1.02x slower                                       |
| pickle_pure_python         | 323 us                                                       | 332 us: 1.03x slower                                        |
| fannkuch                   | 363 ms                                                       | 376 ms: 1.03x slower                                        |
| coroutines                 | 21.6 ms                                                      | 22.4 ms: 1.04x slower                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.96 ms: 1.04x slower                                       |
| docutils                   | 2.83 sec                                                     | 2.94 sec: 1.04x slower                                      |
| raytrace                   | 273 ms                                                       | 288 ms: 1.06x slower                                        |
| crypto_pyaes               | 73.3 ms                                                      | 77.6 ms: 1.06x slower                                       |
| json_loads                 | 24.7 us                                                      | 26.5 us: 1.08x slower                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.90 ms: 1.08x slower                                       |
| nbody                      | 89.3 ms                                                      | 99.1 ms: 1.11x slower                                       |
| many_optionals             | 930 us                                                       | 1.23 ms: 1.33x slower                                       |
| gc_traversal               | 4.74 ms                                                      | 6.51 ms: 1.37x slower                                       |
| subparsers                 | 17.5 ms                                                      | 43.1 ms: 2.47x slower                                       |
| telco                      | 8.79 ms                                                      | 158 ms: 18.03x slower                                       |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                |

Benchmark hidden because not significant (4): djangocms, nqueens, json_dumps, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250803-3.15.0a0-3ec3d05-JIT/bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.12x
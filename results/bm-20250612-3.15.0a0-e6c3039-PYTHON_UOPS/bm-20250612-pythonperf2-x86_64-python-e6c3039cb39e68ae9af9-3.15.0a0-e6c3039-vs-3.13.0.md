# Results vs. 3.13.0

- fork: python
- ref: e6c3039cb39e68ae9af9
- machine: linux-x86_64
- commit hash: e6c3039
- commit date: 2025-06-12
- overall geometric mean: 1.090x slower
- HPT reliability: 99.87%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 321 ms: 1.09x slower                                                        |
| docutils       | 2.83 sec                                                     | 3.13 sec: 1.11x slower                                                      |
| html5lib       | 73.5 ms                                                      | 70.2 ms: 1.05x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.14 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 357 ms: 1.31x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 356 ms: 1.27x faster                                                        |
| async_tree_io              | 843 ms                                                       | 666 ms: 1.27x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 676 ms: 1.23x faster                                                        |
| async_tree_none            | 376 ms                                                       | 307 ms: 1.22x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 291 ms: 1.19x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 531 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 530 ms: 1.10x faster                                                        |
| async_generators           | 457 ms                                                       | 460 ms: 1.01x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.15x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 260 ms: 1.03x slower                                                        |
| float          | 81.3 ms                                                      | 105 ms: 1.30x slower                                                        |
| nbody          | 89.3 ms                                                      | 187 ms: 2.09x slower                                                        |
| Geometric mean | (ref)                                                        | 1.41x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                       | 221 ms: 1.11x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 24.8 ms: 1.05x faster                                                       |
| regex_effbot   | 3.67 ms                                                      | 3.77 ms: 1.03x slower                                                       |
| regex_compile  | 143 ms                                                       | 160 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 150 ms                                                       | 143 ms: 1.05x faster                                                        |
| json_loads           | 24.7 us                                                      | 25.0 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 107 ms: 1.04x slower                                                        |
| xml_etree_process    | 61.2 ms                                                      | 75.0 ms: 1.23x slower                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 107 ms: 1.24x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 410 us: 1.27x slower                                                        |
| tomli_loads          | 2.46 sec                                                     | 3.17 sec: 1.29x slower                                                      |
| unpickle_pure_python | 217 us                                                       | 382 us: 1.76x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.18x slower                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.2 ms: 1.04x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.80 ms: 1.02x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.5 ms: 1.12x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 56.0 ms: 1.02x faster                                                       |
| django_template | 36.4 ms                                                      | 36.0 ms: 1.01x faster                                                       |
| mako            | 10.4 ms                                                      | 16.8 ms: 1.62x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.09x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.46 sec: 1.74x faster                                                      |
| deepcopy_memo              | 38.6 us                                                      | 27.4 us: 1.41x faster                                                       |
| deepcopy                   | 392 us                                                       | 280 us: 1.40x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 357 ms: 1.31x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 356 ms: 1.27x faster                                                        |
| async_tree_io              | 843 ms                                                       | 666 ms: 1.27x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 676 ms: 1.23x faster                                                        |
| async_tree_none            | 376 ms                                                       | 307 ms: 1.22x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.97 us: 1.19x faster                                                       |
| async_tree_none_tg         | 346 ms                                                       | 291 ms: 1.19x faster                                                        |
| scimark_sor                | 123 ms                                                       | 104 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 531 ms: 1.14x faster                                                        |
| generators                 | 33.6 ms                                                      | 29.9 ms: 1.12x faster                                                       |
| genshi_text                | 26.2 ms                                                      | 23.5 ms: 1.12x faster                                                       |
| regex_dna                  | 247 ms                                                       | 221 ms: 1.11x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 61.8 ms: 1.10x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 530 ms: 1.10x faster                                                        |
| json                       | 5.69 ms                                                      | 5.29 ms: 1.07x faster                                                       |
| thrift                     | 901 us                                                       | 843 us: 1.07x faster                                                        |
| scimark_lu                 | 98.7 ms                                                      | 93.5 ms: 1.06x faster                                                       |
| regex_v8                   | 26.1 ms                                                      | 24.8 ms: 1.05x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 143 ms: 1.05x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 70.2 ms: 1.05x faster                                                       |
| python_startup             | 15.9 ms                                                      | 15.2 ms: 1.04x faster                                                       |
| pylint                     | 347 ms                                                       | 333 ms: 1.04x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 56.0 ms: 1.02x faster                                                       |
| python_startup_no_site     | 8.96 ms                                                      | 8.80 ms: 1.02x faster                                                       |
| django_template            | 36.4 ms                                                      | 36.0 ms: 1.01x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 17.4 ms: 1.01x faster                                                       |
| coverage                   | 80.0 ms                                                      | 80.5 ms: 1.01x slower                                                       |
| async_generators           | 457 ms                                                       | 460 ms: 1.01x slower                                                        |
| json_loads                 | 24.7 us                                                      | 25.0 us: 1.01x slower                                                       |
| sphinx                     | 1.12 sec                                                     | 1.14 sec: 1.01x slower                                                      |
| richards                   | 52.9 ms                                                      | 54.2 ms: 1.02x slower                                                       |
| richards_super             | 59.6 ms                                                      | 61.1 ms: 1.03x slower                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.77 ms: 1.03x slower                                                       |
| pidigits                   | 252 ms                                                       | 260 ms: 1.03x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                       |
| logging_simple             | 6.39 us                                                      | 6.61 us: 1.03x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 107 ms: 1.04x slower                                                        |
| telco                      | 8.79 ms                                                      | 9.18 ms: 1.04x slower                                                       |
| sympy_sum                  | 155 ms                                                       | 162 ms: 1.04x slower                                                        |
| sqlite_synth               | 2.91 us                                                      | 3.04 us: 1.05x slower                                                       |
| logging_format             | 6.94 us                                                      | 7.26 us: 1.05x slower                                                       |
| sympy_str                  | 298 ms                                                       | 314 ms: 1.05x slower                                                        |
| chaos                      | 60.2 ms                                                      | 63.9 ms: 1.06x slower                                                       |
| sympy_expand               | 509 ms                                                       | 543 ms: 1.07x slower                                                        |
| k_core                     | 2.17 sec                                                     | 2.32 sec: 1.07x slower                                                      |
| create_gc_cycles           | 2.68 ms                                                      | 2.88 ms: 1.07x slower                                                       |
| shortest_path              | 460 ms                                                       | 498 ms: 1.08x slower                                                        |
| 2to3                       | 293 ms                                                       | 321 ms: 1.09x slower                                                        |
| docutils                   | 2.83 sec                                                     | 3.13 sec: 1.11x slower                                                      |
| regex_compile              | 143 ms                                                       | 160 ms: 1.12x slower                                                        |
| connected_components       | 432 ms                                                       | 487 ms: 1.13x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 104 ms: 1.14x slower                                                        |
| many_optionals             | 930 us                                                       | 1.09 ms: 1.18x slower                                                       |
| pycparser                  | 1.24 sec                                                     | 1.47 sec: 1.18x slower                                                      |
| typing_runtime_protocols   | 169 us                                                       | 202 us: 1.20x slower                                                        |
| raytrace                   | 273 ms                                                       | 334 ms: 1.22x slower                                                        |
| xml_etree_process          | 61.2 ms                                                      | 75.0 ms: 1.23x slower                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 107 ms: 1.24x slower                                                        |
| meteor_contest             | 130 ms                                                       | 164 ms: 1.27x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 410 us: 1.27x slower                                                        |
| tomli_loads                | 2.46 sec                                                     | 3.17 sec: 1.29x slower                                                      |
| pyflate                    | 503 ms                                                       | 650 ms: 1.29x slower                                                        |
| float                      | 81.3 ms                                                      | 105 ms: 1.30x slower                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 6.64 sec: 1.31x slower                                                      |
| scimark_monte_carlo        | 66.1 ms                                                      | 87.7 ms: 1.33x slower                                                       |
| go                         | 162 ms                                                       | 220 ms: 1.36x slower                                                        |
| pprint_pformat             | 1.72 sec                                                     | 2.40 sec: 1.40x slower                                                      |
| pprint_safe_repr           | 843 ms                                                       | 1.18 sec: 1.40x slower                                                      |
| gc_traversal               | 4.74 ms                                                      | 6.70 ms: 1.41x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 25.6 ms: 1.46x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 108 ms: 1.47x slower                                                        |
| scimark_fft                | 328 ms                                                       | 493 ms: 1.51x slower                                                        |
| hexiom                     | 6.55 ms                                                      | 10.4 ms: 1.59x slower                                                       |
| mako                       | 10.4 ms                                                      | 16.8 ms: 1.62x slower                                                       |
| deltablue                  | 3.42 ms                                                      | 5.92 ms: 1.73x slower                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 8.32 ms: 1.74x slower                                                       |
| unpickle_pure_python       | 217 us                                                       | 382 us: 1.76x slower                                                        |
| fannkuch                   | 363 ms                                                       | 644 ms: 1.77x slower                                                        |
| comprehensions             | 17.0 us                                                      | 30.3 us: 1.78x slower                                                       |
| spectral_norm              | 97.0 ms                                                      | 191 ms: 1.97x slower                                                        |
| nbody                      | 89.3 ms                                                      | 187 ms: 2.09x slower                                                        |
| logging_silent             | 97.9 ns                                                      | 504 ns: 5.15x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.11x slower                                                                |

Benchmark hidden because not significant (4): djangocms, asyncio_websockets, json_dumps, sympy_integrate
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250612-3.15.0a0-e6c3039-PYTHON_UOPS/bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.090x slower

# HPT report

- Reliability score: 99.87% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.08x
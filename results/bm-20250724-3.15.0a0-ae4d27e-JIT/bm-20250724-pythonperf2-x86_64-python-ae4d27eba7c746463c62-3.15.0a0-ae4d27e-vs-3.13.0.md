# Results vs. 3.13.0

- fork: python
- ref: ae4d27eba7c746463c62
- machine: linux-x86_64
- commit hash: ae4d27e
- commit date: 2025-07-24
- overall geometric mean: 1.043x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 286 ms: 1.02x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                                      |
| html5lib       | 73.5 ms                                                      | 67.1 ms: 1.10x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 333 ms: 1.40x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 327 ms: 1.39x faster                                                        |
| async_tree_io              | 843 ms                                                       | 618 ms: 1.36x faster                                                        |
| async_tree_none            | 376 ms                                                       | 280 ms: 1.34x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 636 ms: 1.31x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 270 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 501 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 506 ms: 1.15x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                        |
| async_generators           | 457 ms                                                       | 452 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.4 ms: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 63.6 ms: 1.28x faster                                                       |
| pidigits       | 252 ms                                                       | 256 ms: 1.01x slower                                                        |
| nbody          | 89.3 ms                                                      | 99.4 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                       | 227 ms: 1.09x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 24.4 ms: 1.07x faster                                                       |
| regex_compile  | 143 ms                                                       | 133 ms: 1.07x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.59 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.91 sec: 1.29x faster                                                      |
| unpickle_pure_python | 217 us                                                       | 193 us: 1.13x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 56.0 ms: 1.09x faster                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 80.4 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 99.1 ms: 1.04x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 145 ms: 1.04x faster                                                        |
| json_loads           | 24.7 us                                                      | 25.0 us: 1.01x slower                                                       |
| pickle_pure_python   | 323 us                                                       | 331 us: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.07x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.4 ms: 1.03x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.84 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.3 ms: 1.12x faster                                                       |
| mako            | 10.4 ms                                                      | 9.65 ms: 1.07x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 54.3 ms: 1.05x faster                                                       |
| django_template | 36.4 ms                                                      | 35.2 ms: 1.03x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.29 sec: 1.97x faster                                                      |
| richards                   | 52.9 ms                                                      | 35.1 ms: 1.51x faster                                                       |
| richards_super             | 59.6 ms                                                      | 40.7 ms: 1.46x faster                                                       |
| deepcopy                   | 392 us                                                       | 279 us: 1.41x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 333 ms: 1.40x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 327 ms: 1.39x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 27.9 us: 1.38x faster                                                       |
| async_tree_io              | 843 ms                                                       | 618 ms: 1.36x faster                                                        |
| async_tree_none            | 376 ms                                                       | 280 ms: 1.34x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 636 ms: 1.31x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 1.91 sec: 1.29x faster                                                      |
| async_tree_none_tg         | 346 ms                                                       | 270 ms: 1.28x faster                                                        |
| float                      | 81.3 ms                                                      | 63.6 ms: 1.28x faster                                                       |
| go                         | 162 ms                                                       | 129 ms: 1.26x faster                                                        |
| pyflate                    | 503 ms                                                       | 401 ms: 1.26x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 80.4 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 501 ms: 1.20x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 2.84 ms: 1.20x faster                                                       |
| scimark_sor                | 123 ms                                                       | 102 ms: 1.20x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.99 us: 1.18x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 58.5 ms: 1.17x faster                                                       |
| pprint_pformat             | 1.72 sec                                                     | 1.49 sec: 1.15x faster                                                      |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 506 ms: 1.15x faster                                                        |
| pprint_safe_repr           | 843 ms                                                       | 736 ms: 1.15x faster                                                        |
| unpickle_pure_python       | 217 us                                                       | 193 us: 1.13x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.52 sec: 1.12x faster                                                      |
| genshi_text                | 26.2 ms                                                      | 23.3 ms: 1.12x faster                                                       |
| generators                 | 33.6 ms                                                      | 30.1 ms: 1.12x faster                                                       |
| html5lib                   | 73.5 ms                                                      | 67.1 ms: 1.10x faster                                                       |
| xml_etree_process          | 61.2 ms                                                      | 56.0 ms: 1.09x faster                                                       |
| regex_dna                  | 247 ms                                                       | 227 ms: 1.09x faster                                                        |
| scimark_fft                | 328 ms                                                       | 301 ms: 1.09x faster                                                        |
| thrift                     | 901 us                                                       | 829 us: 1.09x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.01 sec: 1.08x faster                                                      |
| xml_etree_generate         | 86.5 ms                                                      | 80.4 ms: 1.08x faster                                                       |
| connected_components       | 432 ms                                                       | 402 ms: 1.07x faster                                                        |
| mako                       | 10.4 ms                                                      | 9.65 ms: 1.07x faster                                                       |
| logging_simple             | 6.39 us                                                      | 5.96 us: 1.07x faster                                                       |
| regex_v8                   | 26.1 ms                                                      | 24.4 ms: 1.07x faster                                                       |
| regex_compile              | 143 ms                                                       | 133 ms: 1.07x faster                                                        |
| meteor_contest             | 130 ms                                                       | 121 ms: 1.07x faster                                                        |
| pylint                     | 347 ms                                                       | 324 ms: 1.07x faster                                                        |
| logging_silent             | 97.9 ns                                                      | 92.4 ns: 1.06x faster                                                       |
| hexiom                     | 6.55 ms                                                      | 6.20 ms: 1.06x faster                                                       |
| sympy_integrate            | 23.6 ms                                                      | 22.4 ms: 1.05x faster                                                       |
| shortest_path              | 460 ms                                                       | 437 ms: 1.05x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 54.3 ms: 1.05x faster                                                       |
| logging_format             | 6.94 us                                                      | 6.61 us: 1.05x faster                                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 63.2 ms: 1.05x faster                                                       |
| scimark_lu                 | 98.7 ms                                                      | 94.4 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 99.1 ms: 1.04x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 145 ms: 1.04x faster                                                        |
| json                       | 5.69 ms                                                      | 5.49 ms: 1.04x faster                                                       |
| django_template            | 36.4 ms                                                      | 35.2 ms: 1.03x faster                                                       |
| python_startup             | 15.9 ms                                                      | 15.4 ms: 1.03x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 17.0 ms: 1.03x faster                                                       |
| sympy_str                  | 298 ms                                                       | 290 ms: 1.03x faster                                                        |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.03x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.83 us: 1.03x faster                                                       |
| 2to3                       | 293 ms                                                       | 286 ms: 1.02x faster                                                        |
| sympy_expand               | 509 ms                                                       | 499 ms: 1.02x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.59 ms: 1.02x faster                                                       |
| python_startup_no_site     | 8.96 ms                                                      | 8.84 ms: 1.01x faster                                                       |
| coverage                   | 80.0 ms                                                      | 79.0 ms: 1.01x faster                                                       |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                        |
| chaos                      | 60.2 ms                                                      | 59.6 ms: 1.01x faster                                                       |
| async_generators           | 457 ms                                                       | 452 ms: 1.01x faster                                                        |
| fannkuch                   | 363 ms                                                       | 366 ms: 1.01x slower                                                        |
| json_loads                 | 24.7 us                                                      | 25.0 us: 1.01x slower                                                       |
| pidigits                   | 252 ms                                                       | 256 ms: 1.01x slower                                                        |
| comprehensions             | 17.0 us                                                      | 17.3 us: 1.02x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 331 us: 1.02x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 93.3 ms: 1.03x slower                                                       |
| docutils                   | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                                      |
| coroutines                 | 21.6 ms                                                      | 22.4 ms: 1.04x slower                                                       |
| raytrace                   | 273 ms                                                       | 284 ms: 1.04x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 77.3 ms: 1.05x slower                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.09 ms: 1.07x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.88 ms: 1.07x slower                                                       |
| nbody                      | 89.3 ms                                                      | 99.4 ms: 1.11x slower                                                       |
| many_optionals             | 930 us                                                       | 1.23 ms: 1.32x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 6.54 ms: 1.38x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 42.6 ms: 2.44x slower                                                       |
| telco                      | 8.79 ms                                                      | 159 ms: 18.04x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (4): pycparser, djangocms, typing_runtime_protocols, json_dumps
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250724-3.15.0a0-ae4d27e-JIT/bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.12x
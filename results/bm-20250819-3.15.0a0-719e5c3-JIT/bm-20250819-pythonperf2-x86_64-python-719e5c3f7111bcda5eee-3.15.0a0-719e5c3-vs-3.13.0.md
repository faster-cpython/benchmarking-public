# Results vs. 3.13.0

- fork: python
- ref: 719e5c3f7111bcda5eee
- machine: linux-x86_64
- commit hash: 719e5c3
- commit date: 2025-08-19
- overall geometric mean: 1.039x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 288 ms: 1.02x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.92 sec: 1.03x slower                                                      |
| html5lib       | 73.5 ms                                                      | 67.1 ms: 1.09x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                      |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 332 ms: 1.40x faster                                                        |
| async_tree_none            | 376 ms                                                       | 272 ms: 1.38x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 329 ms: 1.38x faster                                                        |
| async_tree_io              | 843 ms                                                       | 617 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 624 ms: 1.33x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 271 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 500 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                        |
| async_generators           | 457 ms                                                       | 447 ms: 1.02x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 23.1 ms: 1.07x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 65.8 ms: 1.24x faster                                                       |
| pidigits       | 252 ms                                                       | 256 ms: 1.01x slower                                                        |
| nbody          | 89.3 ms                                                      | 103 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.6 ms: 1.11x faster                                                       |
| regex_dna      | 247 ms                                                       | 224 ms: 1.10x faster                                                        |
| regex_compile  | 143 ms                                                       | 134 ms: 1.06x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.62 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.93 sec: 1.27x faster                                                      |
| unpickle_pure_python | 217 us                                                       | 194 us: 1.12x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 55.8 ms: 1.10x faster                                                       |
| json_dumps           | 11.1 ms                                                      | 10.2 ms: 1.09x faster                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 80.9 ms: 1.07x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.02x faster                                                        |
| xml_etree_parse      | 150 ms                                                       | 149 ms: 1.01x faster                                                        |
| json_loads           | 24.7 us                                                      | 25.4 us: 1.03x slower                                                       |
| pickle_pure_python   | 323 us                                                       | 334 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.4 ms: 1.04x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.83 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.1 ms: 1.14x faster                                                       |
| mako            | 10.4 ms                                                      | 9.85 ms: 1.05x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 55.0 ms: 1.04x faster                                                       |
| django_template | 36.4 ms                                                      | 35.3 ms: 1.03x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.28 sec: 1.99x faster                                                      |
| richards                   | 52.9 ms                                                      | 34.2 ms: 1.55x faster                                                       |
| richards_super             | 59.6 ms                                                      | 39.4 ms: 1.51x faster                                                       |
| async_tree_memoization_tg  | 466 ms                                                       | 332 ms: 1.40x faster                                                        |
| deepcopy                   | 392 us                                                       | 282 us: 1.39x faster                                                        |
| async_tree_none            | 376 ms                                                       | 272 ms: 1.38x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 329 ms: 1.38x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 28.1 us: 1.38x faster                                                       |
| async_tree_io              | 843 ms                                                       | 617 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 624 ms: 1.33x faster                                                        |
| go                         | 162 ms                                                       | 127 ms: 1.28x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 271 ms: 1.28x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 1.93 sec: 1.27x faster                                                      |
| pyflate                    | 503 ms                                                       | 404 ms: 1.25x faster                                                        |
| float                      | 81.3 ms                                                      | 65.8 ms: 1.24x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 500 ms: 1.21x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 80.9 ms: 1.20x faster                                                       |
| scimark_sor                | 123 ms                                                       | 103 ms: 1.20x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 2.89 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 3.04 us: 1.17x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 59.2 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 23.1 ms: 1.14x faster                                                       |
| unpickle_pure_python       | 217 us                                                       | 194 us: 1.12x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.53 sec: 1.12x faster                                                      |
| bpe_tokeniser              | 5.09 sec                                                     | 4.54 sec: 1.12x faster                                                      |
| pprint_safe_repr           | 843 ms                                                       | 753 ms: 1.12x faster                                                        |
| generators                 | 33.6 ms                                                      | 30.1 ms: 1.12x faster                                                       |
| regex_v8                   | 26.1 ms                                                      | 23.6 ms: 1.11x faster                                                       |
| logging_simple             | 6.39 us                                                      | 5.78 us: 1.11x faster                                                       |
| regex_dna                  | 247 ms                                                       | 224 ms: 1.10x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 55.8 ms: 1.10x faster                                                       |
| html5lib                   | 73.5 ms                                                      | 67.1 ms: 1.09x faster                                                       |
| scimark_fft                | 328 ms                                                       | 299 ms: 1.09x faster                                                        |
| json_dumps                 | 11.1 ms                                                      | 10.2 ms: 1.09x faster                                                       |
| logging_format             | 6.94 us                                                      | 6.42 us: 1.08x faster                                                       |
| thrift                     | 901 us                                                       | 835 us: 1.08x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.01 sec: 1.08x faster                                                      |
| xml_etree_generate         | 86.5 ms                                                      | 80.9 ms: 1.07x faster                                                       |
| pylint                     | 347 ms                                                       | 325 ms: 1.07x faster                                                        |
| logging_silent             | 97.9 ns                                                      | 91.9 ns: 1.07x faster                                                       |
| regex_compile              | 143 ms                                                       | 134 ms: 1.06x faster                                                        |
| connected_components       | 432 ms                                                       | 407 ms: 1.06x faster                                                        |
| shortest_path              | 460 ms                                                       | 435 ms: 1.06x faster                                                        |
| json                       | 5.69 ms                                                      | 5.40 ms: 1.05x faster                                                       |
| mako                       | 10.4 ms                                                      | 9.85 ms: 1.05x faster                                                       |
| scimark_lu                 | 98.7 ms                                                      | 94.1 ms: 1.05x faster                                                       |
| hexiom                     | 6.55 ms                                                      | 6.25 ms: 1.05x faster                                                       |
| sympy_integrate            | 23.6 ms                                                      | 22.5 ms: 1.05x faster                                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 63.2 ms: 1.05x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 16.8 ms: 1.04x faster                                                       |
| meteor_contest             | 130 ms                                                       | 125 ms: 1.04x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 55.0 ms: 1.04x faster                                                       |
| python_startup             | 15.9 ms                                                      | 15.4 ms: 1.04x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.82 us: 1.03x faster                                                       |
| django_template            | 36.4 ms                                                      | 35.3 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.02x faster                                                        |
| sphinx                     | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                      |
| async_generators           | 457 ms                                                       | 447 ms: 1.02x faster                                                        |
| sympy_sum                  | 155 ms                                                       | 152 ms: 1.02x faster                                                        |
| sympy_str                  | 298 ms                                                       | 293 ms: 1.02x faster                                                        |
| 2to3                       | 293 ms                                                       | 288 ms: 1.02x faster                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 8.83 ms: 1.01x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.62 ms: 1.01x faster                                                       |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 149 ms: 1.01x faster                                                        |
| sympy_expand               | 509 ms                                                       | 505 ms: 1.01x faster                                                        |
| chaos                      | 60.2 ms                                                      | 59.9 ms: 1.00x faster                                                       |
| raytrace                   | 273 ms                                                       | 276 ms: 1.01x slower                                                        |
| pidigits                   | 252 ms                                                       | 256 ms: 1.01x slower                                                        |
| comprehensions             | 17.0 us                                                      | 17.4 us: 1.02x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.4 us: 1.03x slower                                                       |
| nqueens                    | 90.7 ms                                                      | 93.7 ms: 1.03x slower                                                       |
| docutils                   | 2.83 sec                                                     | 2.92 sec: 1.03x slower                                                      |
| pickle_pure_python         | 323 us                                                       | 334 us: 1.03x slower                                                        |
| fannkuch                   | 363 ms                                                       | 380 ms: 1.05x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.02 ms: 1.05x slower                                                       |
| coverage                   | 80.0 ms                                                      | 84.8 ms: 1.06x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 77.9 ms: 1.06x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 23.1 ms: 1.07x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.91 ms: 1.09x slower                                                       |
| nbody                      | 89.3 ms                                                      | 103 ms: 1.15x slower                                                        |
| many_optionals             | 930 us                                                       | 1.24 ms: 1.33x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 6.67 ms: 1.41x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 43.0 ms: 2.46x slower                                                       |
| telco                      | 8.79 ms                                                      | 161 ms: 18.29x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (3): djangocms, typing_runtime_protocols, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250819-3.15.0a0-719e5c3-JIT/bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.12x
# Results vs. 3.13.0

- fork: savannahostrowski
- ref: poptimize
- machine: linux-x86_64
- commit hash: c6edbf9
- commit date: 2025-09-15
- overall geometric mean: 1.041x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 286 ms: 1.02x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                                      |
| html5lib       | 73.5 ms                                                      | 66.4 ms: 1.11x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 334 ms: 1.40x faster                                                        |
| async_tree_none            | 376 ms                                                       | 273 ms: 1.38x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 330 ms: 1.37x faster                                                        |
| async_tree_io              | 843 ms                                                       | 616 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 632 ms: 1.32x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 276 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 503 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 507 ms: 1.15x faster                                                        |
| async_generators           | 457 ms                                                       | 445 ms: 1.03x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 67.7 ms: 1.20x faster                                                       |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                        |
| nbody          | 89.3 ms                                                      | 96.6 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.4 ms: 1.12x faster                                                       |
| regex_dna      | 247 ms                                                       | 226 ms: 1.09x faster                                                        |
| regex_compile  | 143 ms                                                       | 132 ms: 1.08x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.64 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.89 sec: 1.30x faster                                                      |
| unpickle_pure_python | 217 us                                                       | 192 us: 1.13x faster                                                        |
| json_dumps           | 11.1 ms                                                      | 10.1 ms: 1.10x faster                                                       |
| xml_etree_process    | 61.2 ms                                                      | 56.0 ms: 1.09x faster                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 79.7 ms: 1.09x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 141 ms: 1.06x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 97.4 ms: 1.06x faster                                                       |
| json_loads           | 24.7 us                                                      | 26.0 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.08x faster                                                                |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.85 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.4 ms: 1.12x faster                                                       |
| mako            | 10.4 ms                                                      | 9.62 ms: 1.08x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 53.7 ms: 1.06x faster                                                       |
| django_template | 36.4 ms                                                      | 35.5 ms: 1.02x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.29 sec: 1.96x faster                                                      |
| deepcopy                   | 392 us                                                       | 262 us: 1.50x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 26.1 us: 1.48x faster                                                       |
| async_tree_memoization_tg  | 466 ms                                                       | 334 ms: 1.40x faster                                                        |
| async_tree_none            | 376 ms                                                       | 273 ms: 1.38x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 330 ms: 1.37x faster                                                        |
| async_tree_io              | 843 ms                                                       | 616 ms: 1.37x faster                                                        |
| go                         | 162 ms                                                       | 120 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 632 ms: 1.32x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 1.89 sec: 1.30x faster                                                      |
| pyflate                    | 503 ms                                                       | 397 ms: 1.27x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 276 ms: 1.26x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 79.6 ms: 1.22x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.94 us: 1.21x faster                                                       |
| scimark_sor                | 123 ms                                                       | 102 ms: 1.20x faster                                                        |
| float                      | 81.3 ms                                                      | 67.7 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 503 ms: 1.20x faster                                                        |
| richards                   | 52.9 ms                                                      | 44.3 ms: 1.19x faster                                                       |
| richards_super             | 59.6 ms                                                      | 50.5 ms: 1.18x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 58.5 ms: 1.17x faster                                                       |
| pprint_pformat             | 1.72 sec                                                     | 1.49 sec: 1.15x faster                                                      |
| pprint_safe_repr           | 843 ms                                                       | 734 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 507 ms: 1.15x faster                                                        |
| generators                 | 33.6 ms                                                      | 29.5 ms: 1.14x faster                                                       |
| unpickle_pure_python       | 217 us                                                       | 192 us: 1.13x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 23.4 ms: 1.12x faster                                                       |
| regex_v8                   | 26.1 ms                                                      | 23.4 ms: 1.12x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 15.8 ms: 1.11x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.58 sec: 1.11x faster                                                      |
| hexiom                     | 6.55 ms                                                      | 5.90 ms: 1.11x faster                                                       |
| html5lib                   | 73.5 ms                                                      | 66.4 ms: 1.11x faster                                                       |
| json_dumps                 | 11.1 ms                                                      | 10.1 ms: 1.10x faster                                                       |
| scimark_fft                | 328 ms                                                       | 298 ms: 1.10x faster                                                        |
| regex_dna                  | 247 ms                                                       | 226 ms: 1.09x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 56.0 ms: 1.09x faster                                                       |
| logging_simple             | 6.39 us                                                      | 5.86 us: 1.09x faster                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 79.7 ms: 1.09x faster                                                       |
| k_core                     | 2.17 sec                                                     | 2.01 sec: 1.08x faster                                                      |
| regex_compile              | 143 ms                                                       | 132 ms: 1.08x faster                                                        |
| logging_format             | 6.94 us                                                      | 6.44 us: 1.08x faster                                                       |
| mako                       | 10.4 ms                                                      | 9.62 ms: 1.08x faster                                                       |
| pylint                     | 347 ms                                                       | 322 ms: 1.08x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 3.18 ms: 1.07x faster                                                       |
| logging_silent             | 97.9 ns                                                      | 91.9 ns: 1.07x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 141 ms: 1.06x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 62.2 ms: 1.06x faster                                                       |
| genshi_xml                 | 57.1 ms                                                      | 53.7 ms: 1.06x faster                                                       |
| meteor_contest             | 130 ms                                                       | 123 ms: 1.06x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 97.4 ms: 1.06x faster                                                       |
| thrift                     | 901 us                                                       | 854 us: 1.05x faster                                                        |
| connected_components       | 432 ms                                                       | 411 ms: 1.05x faster                                                        |
| sympy_integrate            | 23.6 ms                                                      | 22.4 ms: 1.05x faster                                                       |
| scimark_lu                 | 98.7 ms                                                      | 94.1 ms: 1.05x faster                                                       |
| json                       | 5.69 ms                                                      | 5.45 ms: 1.04x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.80 us: 1.04x faster                                                       |
| python_startup             | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                       |
| shortest_path              | 460 ms                                                       | 445 ms: 1.03x faster                                                        |
| async_generators           | 457 ms                                                       | 445 ms: 1.03x faster                                                        |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| sympy_str                  | 298 ms                                                       | 291 ms: 1.03x faster                                                        |
| django_template            | 36.4 ms                                                      | 35.5 ms: 1.02x faster                                                       |
| 2to3                       | 293 ms                                                       | 286 ms: 1.02x faster                                                        |
| sympy_expand               | 509 ms                                                       | 498 ms: 1.02x faster                                                        |
| sympy_sum                  | 155 ms                                                       | 152 ms: 1.02x faster                                                        |
| chaos                      | 60.2 ms                                                      | 59.2 ms: 1.02x faster                                                       |
| pycparser                  | 1.24 sec                                                     | 1.23 sec: 1.01x faster                                                      |
| python_startup_no_site     | 8.96 ms                                                      | 8.85 ms: 1.01x faster                                                       |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.64 ms: 1.01x faster                                                       |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 171 us: 1.01x slower                                                        |
| raytrace                   | 273 ms                                                       | 278 ms: 1.02x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.87 ms: 1.02x slower                                                       |
| comprehensions             | 17.0 us                                                      | 17.4 us: 1.02x slower                                                       |
| nqueens                    | 90.7 ms                                                      | 93.3 ms: 1.03x slower                                                       |
| docutils                   | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                                      |
| coverage                   | 80.0 ms                                                      | 82.6 ms: 1.03x slower                                                       |
| fannkuch                   | 363 ms                                                       | 380 ms: 1.05x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 77.1 ms: 1.05x slower                                                       |
| json_loads                 | 24.7 us                                                      | 26.0 us: 1.06x slower                                                       |
| nbody                      | 89.3 ms                                                      | 96.6 ms: 1.08x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.95 ms: 1.10x slower                                                       |
| many_optionals             | 930 us                                                       | 1.23 ms: 1.32x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 6.68 ms: 1.41x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 43.1 ms: 2.46x slower                                                       |
| telco                      | 8.79 ms                                                      | 160 ms: 18.18x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (2): djangocms, pickle_pure_python
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250915-3.15.0a0-c6edbf9-JIT/bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.12x
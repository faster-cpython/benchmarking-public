# Results vs. 3.13.0

- fork: mdboom
- ref: specialize_compact_i
- machine: linux-x86_64
- commit hash: 1cbd7aa
- commit date: 2025-02-03
- overall geometric mean: 1.070x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 279 ms: 1.05x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.85 sec: 1.01x slower                                                       |
| html5lib       | 73.5 ms                                                      | 66.0 ms: 1.11x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 337 ms: 1.38x faster                                                         |
| async_tree_none            | 376 ms                                                       | 290 ms: 1.30x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 350 ms: 1.30x faster                                                         |
| async_tree_io              | 843 ms                                                       | 651 ms: 1.29x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 645 ms: 1.29x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 278 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 520 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                         |
| async_generators           | 457 ms                                                       | 408 ms: 1.12x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 20.7 ms: 1.04x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 69.1 ms: 1.18x faster                                                        |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.14 ms: 1.17x faster                                                        |
| regex_dna      | 247 ms                                                       | 233 ms: 1.06x faster                                                         |
| regex_compile  | 143 ms                                                       | 135 ms: 1.06x faster                                                         |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.05 sec: 1.20x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 132 ms: 1.14x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 95.6 ms: 1.08x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 209 us: 1.04x faster                                                         |
| xml_etree_process    | 61.2 ms                                                      | 59.0 ms: 1.04x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 83.7 ms: 1.03x faster                                                        |
| json_dumps           | 11.1 ms                                                      | 11.6 ms: 1.05x slower                                                        |
| json_loads           | 24.7 us                                                      | 26.3 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 8.97 ms: 1.00x slower                                                        |
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 22.9 ms: 1.14x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 51.8 ms: 1.10x faster                                                        |
| django_template | 36.4 ms                                                      | 35.4 ms: 1.03x faster                                                        |
| mako            | 10.4 ms                                                      | 10.8 ms: 1.04x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                   | 392 us                                                       | 278 us: 1.41x faster                                                         |
| async_tree_memoization_tg  | 466 ms                                                       | 337 ms: 1.38x faster                                                         |
| go                         | 162 ms                                                       | 123 ms: 1.32x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 29.3 us: 1.32x faster                                                        |
| async_tree_none            | 376 ms                                                       | 290 ms: 1.30x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 350 ms: 1.30x faster                                                         |
| async_tree_io              | 843 ms                                                       | 651 ms: 1.29x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 645 ms: 1.29x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 278 ms: 1.24x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 2.90 us: 1.22x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 79.9 ms: 1.21x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.05 sec: 1.20x faster                                                       |
| float                      | 81.3 ms                                                      | 69.1 ms: 1.18x faster                                                        |
| richards                   | 52.9 ms                                                      | 45.1 ms: 1.17x faster                                                        |
| generators                 | 33.6 ms                                                      | 28.7 ms: 1.17x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.14 ms: 1.17x faster                                                        |
| richards_super             | 59.6 ms                                                      | 51.3 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 520 ms: 1.16x faster                                                         |
| scimark_sor                | 123 ms                                                       | 107 ms: 1.16x faster                                                         |
| genshi_text                | 26.2 ms                                                      | 22.9 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                         |
| pyflate                    | 503 ms                                                       | 442 ms: 1.14x faster                                                         |
| xml_etree_parse            | 150 ms                                                       | 132 ms: 1.14x faster                                                         |
| pathlib                    | 17.5 ms                                                      | 15.6 ms: 1.12x faster                                                        |
| async_generators           | 457 ms                                                       | 408 ms: 1.12x faster                                                         |
| telco                      | 8.79 ms                                                      | 7.86 ms: 1.12x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.56 sec: 1.11x faster                                                       |
| html5lib                   | 73.5 ms                                                      | 66.0 ms: 1.11x faster                                                        |
| pylint                     | 347 ms                                                       | 313 ms: 1.11x faster                                                         |
| genshi_xml                 | 57.1 ms                                                      | 51.8 ms: 1.10x faster                                                        |
| hexiom                     | 6.55 ms                                                      | 6.01 ms: 1.09x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.59 sec: 1.08x faster                                                       |
| pprint_safe_repr           | 843 ms                                                       | 781 ms: 1.08x faster                                                         |
| scimark_fft                | 328 ms                                                       | 305 ms: 1.08x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 95.6 ms: 1.08x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 62.0 ms: 1.07x faster                                                        |
| sqlglot_parse              | 1.40 ms                                                      | 1.32 ms: 1.06x faster                                                        |
| regex_dna                  | 247 ms                                                       | 233 ms: 1.06x faster                                                         |
| regex_compile              | 143 ms                                                       | 135 ms: 1.06x faster                                                         |
| deltablue                  | 3.42 ms                                                      | 3.23 ms: 1.06x faster                                                        |
| 2to3                       | 293 ms                                                       | 279 ms: 1.05x faster                                                         |
| sympy_expand               | 509 ms                                                       | 485 ms: 1.05x faster                                                         |
| scimark_lu                 | 98.7 ms                                                      | 94.0 ms: 1.05x faster                                                        |
| sqlglot_normalize          | 119 ms                                                       | 114 ms: 1.05x faster                                                         |
| sqlglot_optimize           | 59.3 ms                                                      | 56.5 ms: 1.05x faster                                                        |
| meteor_contest             | 130 ms                                                       | 124 ms: 1.05x faster                                                         |
| sqlglot_transpile          | 1.79 ms                                                      | 1.71 ms: 1.04x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 142 ms: 1.04x faster                                                         |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.6 ms: 1.04x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 20.7 ms: 1.04x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.08 sec: 1.04x faster                                                       |
| sympy_str                  | 298 ms                                                       | 287 ms: 1.04x faster                                                         |
| unpickle_pure_python       | 217 us                                                       | 209 us: 1.04x faster                                                         |
| thrift                     | 901 us                                                       | 868 us: 1.04x faster                                                         |
| xml_etree_process          | 61.2 ms                                                      | 59.0 ms: 1.04x faster                                                        |
| connected_components       | 432 ms                                                       | 417 ms: 1.04x faster                                                         |
| mdp                        | 2.54 sec                                                     | 2.45 sec: 1.04x faster                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 83.7 ms: 1.03x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.81 us: 1.03x faster                                                        |
| shortest_path              | 460 ms                                                       | 445 ms: 1.03x faster                                                         |
| sympy_sum                  | 155 ms                                                       | 150 ms: 1.03x faster                                                         |
| json                       | 5.69 ms                                                      | 5.52 ms: 1.03x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 66.2 ms: 1.03x faster                                                        |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.64 ms: 1.03x faster                                                        |
| django_template            | 36.4 ms                                                      | 35.4 ms: 1.03x faster                                                        |
| bench_thread_pool          | 942 us                                                       | 920 us: 1.02x faster                                                         |
| sympy_integrate            | 23.6 ms                                                      | 23.0 ms: 1.02x faster                                                        |
| nqueens                    | 90.7 ms                                                      | 88.9 ms: 1.02x faster                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 72.0 ms: 1.02x faster                                                        |
| coverage                   | 80.0 ms                                                      | 78.8 ms: 1.01x faster                                                        |
| raytrace                   | 273 ms                                                       | 269 ms: 1.01x faster                                                         |
| typing_runtime_protocols   | 169 us                                                       | 167 us: 1.01x faster                                                         |
| logging_silent             | 97.9 ns                                                      | 96.7 ns: 1.01x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                         |
| comprehensions             | 17.0 us                                                      | 16.9 us: 1.01x faster                                                        |
| pycparser                  | 1.24 sec                                                     | 1.23 sec: 1.01x faster                                                       |
| logging_simple             | 6.39 us                                                      | 6.35 us: 1.01x faster                                                        |
| fannkuch                   | 363 ms                                                       | 361 ms: 1.01x faster                                                         |
| chaos                      | 60.2 ms                                                      | 60.0 ms: 1.00x faster                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 8.97 ms: 1.00x slower                                                        |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                        |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| docutils                   | 2.83 sec                                                     | 2.85 sec: 1.01x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.71 ms: 1.01x slower                                                        |
| mako                       | 10.4 ms                                                      | 10.8 ms: 1.04x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.6 ms: 1.05x slower                                                        |
| json_loads                 | 24.7 us                                                      | 26.3 us: 1.07x slower                                                        |
| many_optionals             | 930 us                                                       | 1.01 ms: 1.08x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 22.7 ms: 1.30x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.33 ms: 1.34x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.26 sec: 246.05x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (4): regex_v8, nbody, logging_format, pickle_pure_python
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.070x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.02x
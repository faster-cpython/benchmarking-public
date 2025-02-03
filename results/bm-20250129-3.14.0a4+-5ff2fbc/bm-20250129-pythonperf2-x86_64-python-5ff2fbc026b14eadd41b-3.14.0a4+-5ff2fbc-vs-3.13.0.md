# Results vs. 3.13.0

- fork: python
- ref: 5ff2fbc026b14eadd41b
- machine: linux-x86_64
- commit hash: 5ff2fbc
- commit date: 2025-01-29
- overall geometric mean: 1.069x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 279 ms: 1.05x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.84 sec: 1.00x slower                                                       |
| html5lib       | 73.5 ms                                                      | 66.0 ms: 1.11x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 337 ms: 1.38x faster                                                         |
| async_tree_none            | 376 ms                                                       | 289 ms: 1.30x faster                                                         |
| async_tree_io              | 843 ms                                                       | 649 ms: 1.30x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 349 ms: 1.30x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 641 ms: 1.30x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 279 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 520 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 511 ms: 1.14x faster                                                         |
| async_generators           | 457 ms                                                       | 410 ms: 1.11x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 20.8 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 69.1 ms: 1.18x faster                                                        |
| nbody          | 89.3 ms                                                      | 86.5 ms: 1.03x faster                                                        |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.04 ms: 1.21x faster                                                        |
| regex_compile  | 143 ms                                                       | 134 ms: 1.07x faster                                                         |
| regex_dna      | 247 ms                                                       | 236 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.08 sec: 1.18x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.11x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 97.6 ms: 1.05x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 58.5 ms: 1.05x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 209 us: 1.04x faster                                                         |
| xml_etree_generate   | 86.5 ms                                                      | 83.5 ms: 1.04x faster                                                        |
| json_dumps           | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                        |
| json_loads           | 24.7 us                                                      | 26.9 us: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.02 ms: 1.01x slower                                                        |
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.5 ms: 1.07x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 55.0 ms: 1.04x faster                                                        |
| django_template | 36.4 ms                                                      | 35.1 ms: 1.03x faster                                                        |
| mako            | 10.4 ms                                                      | 10.8 ms: 1.04x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                   | 392 us                                                       | 278 us: 1.41x faster                                                         |
| async_tree_memoization_tg  | 466 ms                                                       | 337 ms: 1.38x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 29.2 us: 1.32x faster                                                        |
| go                         | 162 ms                                                       | 123 ms: 1.32x faster                                                         |
| async_tree_none            | 376 ms                                                       | 289 ms: 1.30x faster                                                         |
| async_tree_io              | 843 ms                                                       | 649 ms: 1.30x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 349 ms: 1.30x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 641 ms: 1.30x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 279 ms: 1.24x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 2.90 us: 1.22x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.04 ms: 1.21x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.08 sec: 1.18x faster                                                       |
| generators                 | 33.6 ms                                                      | 28.4 ms: 1.18x faster                                                        |
| float                      | 81.3 ms                                                      | 69.1 ms: 1.18x faster                                                        |
| pyflate                    | 503 ms                                                       | 430 ms: 1.17x faster                                                         |
| richards                   | 52.9 ms                                                      | 45.3 ms: 1.17x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 83.4 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 520 ms: 1.16x faster                                                         |
| richards_super             | 59.6 ms                                                      | 51.3 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 511 ms: 1.14x faster                                                         |
| scimark_sor                | 123 ms                                                       | 108 ms: 1.14x faster                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 4.48 sec: 1.13x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 15.7 ms: 1.12x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 66.0 ms: 1.11x faster                                                        |
| async_generators           | 457 ms                                                       | 410 ms: 1.11x faster                                                         |
| pylint                     | 347 ms                                                       | 312 ms: 1.11x faster                                                         |
| telco                      | 8.79 ms                                                      | 7.93 ms: 1.11x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.11x faster                                                         |
| hexiom                     | 6.55 ms                                                      | 6.06 ms: 1.08x faster                                                        |
| pprint_safe_repr           | 843 ms                                                       | 785 ms: 1.07x faster                                                         |
| scimark_fft                | 328 ms                                                       | 305 ms: 1.07x faster                                                         |
| genshi_text                | 26.2 ms                                                      | 24.5 ms: 1.07x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.61 sec: 1.07x faster                                                       |
| regex_compile              | 143 ms                                                       | 134 ms: 1.07x faster                                                         |
| sqlalchemy_declarative     | 148 ms                                                       | 141 ms: 1.06x faster                                                         |
| sqlglot_parse              | 1.40 ms                                                      | 1.33 ms: 1.05x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 97.6 ms: 1.05x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 62.8 ms: 1.05x faster                                                        |
| scimark_lu                 | 98.7 ms                                                      | 93.7 ms: 1.05x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 3.25 ms: 1.05x faster                                                        |
| 2to3                       | 293 ms                                                       | 279 ms: 1.05x faster                                                         |
| meteor_contest             | 130 ms                                                       | 124 ms: 1.05x faster                                                         |
| sympy_expand               | 509 ms                                                       | 487 ms: 1.05x faster                                                         |
| sqlglot_optimize           | 59.3 ms                                                      | 56.6 ms: 1.05x faster                                                        |
| regex_dna                  | 247 ms                                                       | 236 ms: 1.05x faster                                                         |
| sqlglot_transpile          | 1.79 ms                                                      | 1.71 ms: 1.05x faster                                                        |
| connected_components       | 432 ms                                                       | 413 ms: 1.05x faster                                                         |
| xml_etree_process          | 61.2 ms                                                      | 58.5 ms: 1.05x faster                                                        |
| sqlglot_normalize          | 119 ms                                                       | 114 ms: 1.04x faster                                                         |
| dulwich_log                | 68.2 ms                                                      | 65.4 ms: 1.04x faster                                                        |
| thrift                     | 901 us                                                       | 864 us: 1.04x faster                                                         |
| sympy_str                  | 298 ms                                                       | 286 ms: 1.04x faster                                                         |
| unpickle_pure_python       | 217 us                                                       | 209 us: 1.04x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 20.8 ms: 1.04x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 55.0 ms: 1.04x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 83.5 ms: 1.04x faster                                                        |
| logging_simple             | 6.39 us                                                      | 6.17 us: 1.04x faster                                                        |
| shortest_path              | 460 ms                                                       | 444 ms: 1.04x faster                                                         |
| django_template            | 36.4 ms                                                      | 35.1 ms: 1.03x faster                                                        |
| sympy_sum                  | 155 ms                                                       | 150 ms: 1.03x faster                                                         |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                       |
| k_core                     | 2.17 sec                                                     | 2.10 sec: 1.03x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.81 us: 1.03x faster                                                        |
| nbody                      | 89.3 ms                                                      | 86.5 ms: 1.03x faster                                                        |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.7 ms: 1.03x faster                                                        |
| chaos                      | 60.2 ms                                                      | 58.5 ms: 1.03x faster                                                        |
| logging_format             | 6.94 us                                                      | 6.75 us: 1.03x faster                                                        |
| sympy_integrate            | 23.6 ms                                                      | 22.9 ms: 1.03x faster                                                        |
| mdp                        | 2.54 sec                                                     | 2.47 sec: 1.03x faster                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.66 ms: 1.02x faster                                                        |
| fannkuch                   | 363 ms                                                       | 355 ms: 1.02x faster                                                         |
| json                       | 5.69 ms                                                      | 5.56 ms: 1.02x faster                                                        |
| nqueens                    | 90.7 ms                                                      | 88.8 ms: 1.02x faster                                                        |
| pycparser                  | 1.24 sec                                                     | 1.22 sec: 1.02x faster                                                       |
| logging_silent             | 97.9 ns                                                      | 96.8 ns: 1.01x faster                                                        |
| comprehensions             | 17.0 us                                                      | 16.8 us: 1.01x faster                                                        |
| raytrace                   | 273 ms                                                       | 270 ms: 1.01x faster                                                         |
| coverage                   | 80.0 ms                                                      | 79.3 ms: 1.01x faster                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 72.7 ms: 1.01x faster                                                        |
| docutils                   | 2.83 sec                                                     | 2.84 sec: 1.00x slower                                                       |
| python_startup_no_site     | 8.96 ms                                                      | 9.02 ms: 1.01x slower                                                        |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                        |
| mako                       | 10.4 ms                                                      | 10.8 ms: 1.04x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                        |
| many_optionals             | 930 us                                                       | 999 us: 1.07x slower                                                         |
| json_loads                 | 24.7 us                                                      | 26.9 us: 1.09x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.10 ms: 1.29x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 22.6 ms: 1.29x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.29 sec: 252.52x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (6): regex_v8, asyncio_websockets, typing_runtime_protocols, bench_thread_pool, create_gc_cycles, pickle_pure_python
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.069x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.02x
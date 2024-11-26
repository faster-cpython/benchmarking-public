# Results vs. 3.13.0

- fork: faster-cpython
- ref: mark_first_2
- machine: linux-x86_64
- commit hash: 79ab26c
- commit date: 2024-11-22
- overall geometric mean: 1.027x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 285 ms: 1.03x faster                                                           |
| docutils       | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                                         |
| html5lib       | 72.9 ms                                                      | 70.7 ms: 1.03x faster                                                          |
| sphinx         | 1.11 sec                                                     | 1.13 sec: 1.01x slower                                                         |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 337 ms: 1.36x faster                                                           |
| async_tree_io_tg           | 823 ms                                                       | 657 ms: 1.25x faster                                                           |
| async_tree_none            | 370 ms                                                       | 296 ms: 1.25x faster                                                           |
| async_tree_io              | 832 ms                                                       | 666 ms: 1.25x faster                                                           |
| async_tree_none_tg         | 342 ms                                                       | 277 ms: 1.24x faster                                                           |
| async_tree_memoization     | 447 ms                                                       | 363 ms: 1.23x faster                                                           |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 527 ms: 1.13x faster                                                           |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 511 ms: 1.12x faster                                                           |
| asyncio_websockets         | 395 ms                                                       | 384 ms: 1.03x faster                                                           |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                                          |
| async_generators           | 364 ms                                                       | 441 ms: 1.21x slower                                                           |
| Geometric mean             | (ref)                                                        | 1.15x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 81.6 ms                                                      | 79.3 ms: 1.03x faster                                                          |
| nbody          | 92.1 ms                                                      | 89.7 ms: 1.03x faster                                                          |
| pidigits       | 252 ms                                                       | 252 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.36 ms: 1.04x faster                                                          |
| regex_compile  | 143 ms                                                       | 140 ms: 1.02x faster                                                           |
| regex_dna      | 238 ms                                                       | 250 ms: 1.05x slower                                                           |
| regex_v8       | 24.9 ms                                                      | 26.5 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 139 ms: 1.03x faster                                                           |
| xml_etree_iterparse  | 99.8 ms                                                      | 96.7 ms: 1.03x faster                                                          |
| xml_etree_generate   | 85.2 ms                                                      | 83.7 ms: 1.02x faster                                                          |
| unpickle_pure_python | 216 us                                                       | 213 us: 1.02x faster                                                           |
| xml_etree_process    | 60.7 ms                                                      | 60.2 ms: 1.01x faster                                                          |
| json_loads           | 24.7 us                                                      | 25.6 us: 1.04x slower                                                          |
| tomli_loads          | 2.43 sec                                                     | 2.52 sec: 1.04x slower                                                         |
| pickle_pure_python   | 322 us                                                       | 336 us: 1.04x slower                                                           |
| json_dumps           | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                                          |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 8.93 ms                                                      | 9.04 ms: 1.01x slower                                                          |
| python_startup         | 15.6 ms                                                      | 16.0 ms: 1.02x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 24.2 ms: 1.12x faster                                                          |
| genshi_xml      | 58.0 ms                                                      | 53.7 ms: 1.08x faster                                                          |
| django_template | 38.9 ms                                                      | 37.9 ms: 1.03x faster                                                          |
| mako            | 10.3 ms                                                      | 10.7 ms: 1.03x slower                                                          |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 337 ms: 1.36x faster                                                           |
| deepcopy                   | 388 us                                                       | 297 us: 1.31x faster                                                           |
| deepcopy_memo              | 38.9 us                                                      | 30.7 us: 1.27x faster                                                          |
| async_tree_io_tg           | 823 ms                                                       | 657 ms: 1.25x faster                                                           |
| async_tree_none            | 370 ms                                                       | 296 ms: 1.25x faster                                                           |
| async_tree_io              | 832 ms                                                       | 666 ms: 1.25x faster                                                           |
| async_tree_none_tg         | 342 ms                                                       | 277 ms: 1.24x faster                                                           |
| async_tree_memoization     | 447 ms                                                       | 363 ms: 1.23x faster                                                           |
| go                         | 167 ms                                                       | 138 ms: 1.21x faster                                                           |
| deepcopy_reduce            | 3.49 us                                                      | 2.97 us: 1.18x faster                                                          |
| generators                 | 33.9 ms                                                      | 29.8 ms: 1.14x faster                                                          |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 527 ms: 1.13x faster                                                           |
| genshi_text                | 27.2 ms                                                      | 24.2 ms: 1.12x faster                                                          |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 511 ms: 1.12x faster                                                           |
| telco                      | 8.77 ms                                                      | 7.88 ms: 1.11x faster                                                          |
| genshi_xml                 | 58.0 ms                                                      | 53.7 ms: 1.08x faster                                                          |
| pathlib                    | 17.4 ms                                                      | 16.1 ms: 1.08x faster                                                          |
| json                       | 5.62 ms                                                      | 5.22 ms: 1.08x faster                                                          |
| pylint                     | 345 ms                                                       | 321 ms: 1.08x faster                                                           |
| richards_super             | 60.2 ms                                                      | 56.0 ms: 1.07x faster                                                          |
| thrift                     | 918 us                                                       | 865 us: 1.06x faster                                                           |
| richards                   | 52.5 ms                                                      | 49.7 ms: 1.06x faster                                                          |
| sqlalchemy_declarative     | 148 ms                                                       | 141 ms: 1.05x faster                                                           |
| pycparser                  | 1.28 sec                                                     | 1.22 sec: 1.05x faster                                                         |
| coverage                   | 84.5 ms                                                      | 80.9 ms: 1.05x faster                                                          |
| regex_effbot               | 3.51 ms                                                      | 3.36 ms: 1.04x faster                                                          |
| shortest_path              | 477 ms                                                       | 457 ms: 1.04x faster                                                           |
| bpe_tokeniser              | 5.09 sec                                                     | 4.89 sec: 1.04x faster                                                         |
| pprint_pformat             | 1.70 sec                                                     | 1.63 sec: 1.04x faster                                                         |
| pprint_safe_repr           | 835 ms                                                       | 802 ms: 1.04x faster                                                           |
| xml_etree_parse            | 144 ms                                                       | 139 ms: 1.03x faster                                                           |
| xml_etree_iterparse        | 99.8 ms                                                      | 96.7 ms: 1.03x faster                                                          |
| meteor_contest             | 130 ms                                                       | 127 ms: 1.03x faster                                                           |
| html5lib                   | 72.9 ms                                                      | 70.7 ms: 1.03x faster                                                          |
| float                      | 81.6 ms                                                      | 79.3 ms: 1.03x faster                                                          |
| asyncio_websockets         | 395 ms                                                       | 384 ms: 1.03x faster                                                           |
| 2to3                       | 293 ms                                                       | 285 ms: 1.03x faster                                                           |
| k_core                     | 2.18 sec                                                     | 2.12 sec: 1.03x faster                                                         |
| fannkuch                   | 384 ms                                                       | 374 ms: 1.03x faster                                                           |
| nbody                      | 92.1 ms                                                      | 89.7 ms: 1.03x faster                                                          |
| connected_components       | 443 ms                                                       | 431 ms: 1.03x faster                                                           |
| django_template            | 38.9 ms                                                      | 37.9 ms: 1.03x faster                                                          |
| nqueens                    | 92.3 ms                                                      | 90.0 ms: 1.03x faster                                                          |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                                          |
| regex_compile              | 143 ms                                                       | 140 ms: 1.02x faster                                                           |
| hexiom                     | 6.47 ms                                                      | 6.36 ms: 1.02x faster                                                          |
| xml_etree_generate         | 85.2 ms                                                      | 83.7 ms: 1.02x faster                                                          |
| unpickle_pure_python       | 216 us                                                       | 213 us: 1.02x faster                                                           |
| scimark_lu                 | 97.4 ms                                                      | 95.8 ms: 1.02x faster                                                          |
| mdp                        | 2.53 sec                                                     | 2.49 sec: 1.02x faster                                                         |
| sqlalchemy_imperative      | 18.1 ms                                                      | 17.9 ms: 1.01x faster                                                          |
| sympy_str                  | 297 ms                                                       | 293 ms: 1.01x faster                                                           |
| sympy_expand               | 506 ms                                                       | 501 ms: 1.01x faster                                                           |
| xml_etree_process          | 60.7 ms                                                      | 60.2 ms: 1.01x faster                                                          |
| spectral_norm              | 97.4 ms                                                      | 96.9 ms: 1.01x faster                                                          |
| pidigits                   | 252 ms                                                       | 252 ms: 1.00x faster                                                           |
| pyflate                    | 493 ms                                                       | 494 ms: 1.00x slower                                                           |
| sphinx                     | 1.11 sec                                                     | 1.13 sec: 1.01x slower                                                         |
| python_startup_no_site     | 8.93 ms                                                      | 9.04 ms: 1.01x slower                                                          |
| sqlglot_optimize           | 58.7 ms                                                      | 59.4 ms: 1.01x slower                                                          |
| python_startup             | 15.6 ms                                                      | 16.0 ms: 1.02x slower                                                          |
| scimark_sor                | 125 ms                                                       | 128 ms: 1.03x slower                                                           |
| scimark_monte_carlo        | 65.2 ms                                                      | 67.1 ms: 1.03x slower                                                          |
| comprehensions             | 17.3 us                                                      | 17.8 us: 1.03x slower                                                          |
| mako                       | 10.3 ms                                                      | 10.7 ms: 1.03x slower                                                          |
| json_loads                 | 24.7 us                                                      | 25.6 us: 1.04x slower                                                          |
| docutils                   | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                                         |
| tomli_loads                | 2.43 sec                                                     | 2.52 sec: 1.04x slower                                                         |
| scimark_fft                | 298 ms                                                       | 309 ms: 1.04x slower                                                           |
| sqlglot_transpile          | 1.76 ms                                                      | 1.83 ms: 1.04x slower                                                          |
| pickle_pure_python         | 322 us                                                       | 336 us: 1.04x slower                                                           |
| chaos                      | 60.6 ms                                                      | 63.2 ms: 1.04x slower                                                          |
| dulwich_log                | 65.5 ms                                                      | 68.5 ms: 1.05x slower                                                          |
| sqlglot_parse              | 1.37 ms                                                      | 1.43 ms: 1.05x slower                                                          |
| deltablue                  | 3.38 ms                                                      | 3.55 ms: 1.05x slower                                                          |
| regex_dna                  | 238 ms                                                       | 250 ms: 1.05x slower                                                           |
| logging_silent             | 97.5 ns                                                      | 103 ns: 1.05x slower                                                           |
| regex_v8                   | 24.9 ms                                                      | 26.5 ms: 1.06x slower                                                          |
| json_dumps                 | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                                          |
| logging_format             | 6.95 us                                                      | 7.46 us: 1.07x slower                                                          |
| raytrace                   | 267 ms                                                       | 288 ms: 1.08x slower                                                           |
| logging_simple             | 6.28 us                                                      | 6.88 us: 1.10x slower                                                          |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.79 ms: 1.14x slower                                                          |
| async_generators           | 364 ms                                                       | 441 ms: 1.21x slower                                                           |
| gc_traversal               | 4.48 ms                                                      | 6.33 ms: 1.41x slower                                                          |
| bench_mp_pool              | 4.82 ms                                                      | 1.88 sec: 390.66x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                   |

Benchmark hidden because not significant (7): sqlglot_normalize, sympy_integrate, sympy_sum, typing_runtime_protocols, crypto_pyaes, bench_thread_pool, create_gc_cycles
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241122-3.14.0a2+-79ab26c/bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.027x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x
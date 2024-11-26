# Results vs. 3.13.0

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: 47eb1b5
- commit date: 2024-11-13
- overall geometric mean: 1.040x faster
- HPT reliability: 99.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 289 ms: 1.01x faster                                                             |
| docutils       | 2.81 sec                                                     | 2.88 sec: 1.03x slower                                                           |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                     |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 357 ms: 1.28x faster                                                             |
| async_tree_io              | 832 ms                                                       | 653 ms: 1.27x faster                                                             |
| async_tree_io_tg           | 823 ms                                                       | 652 ms: 1.26x faster                                                             |
| async_tree_none            | 370 ms                                                       | 304 ms: 1.22x faster                                                             |
| async_tree_memoization     | 447 ms                                                       | 369 ms: 1.21x faster                                                             |
| async_tree_none_tg         | 342 ms                                                       | 300 ms: 1.14x faster                                                             |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 537 ms: 1.11x faster                                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 523 ms: 1.10x faster                                                             |
| asyncio_websockets         | 395 ms                                                       | 387 ms: 1.02x faster                                                             |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                            |
| async_generators           | 364 ms                                                       | 447 ms: 1.23x slower                                                             |
| Geometric mean             | (ref)                                                        | 1.12x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 88.1 ms: 1.05x faster                                                            |
| float          | 81.6 ms                                                      | 85.5 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 139 ms: 1.02x faster                                                             |
| regex_v8       | 24.9 ms                                                      | 25.3 ms: 1.01x slower                                                            |
| regex_effbot   | 3.51 ms                                                      | 3.62 ms: 1.03x slower                                                            |
| regex_dna      | 238 ms                                                       | 250 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                       | 215 us: 1.01x faster                                                             |
| json_loads           | 24.7 us                                                      | 24.9 us: 1.01x slower                                                            |
| tomli_loads          | 2.43 sec                                                     | 2.48 sec: 1.02x slower                                                           |
| pickle_pure_python   | 322 us                                                       | 332 us: 1.03x slower                                                             |
| xml_etree_process    | 60.7 ms                                                      | 62.8 ms: 1.03x slower                                                            |
| xml_etree_generate   | 85.2 ms                                                      | 88.4 ms: 1.04x slower                                                            |
| json_dumps           | 10.8 ms                                                      | 11.6 ms: 1.07x slower                                                            |
| xml_etree_parse      | 144 ms                                                       | 166 ms: 1.15x slower                                                             |
| xml_etree_iterparse  | 99.8 ms                                                      | 120 ms: 1.21x slower                                                             |
| Geometric mean       | (ref)                                                        | 1.06x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 8.93 ms                                                      | 8.59 ms: 1.04x faster                                                            |
| python_startup         | 15.6 ms                                                      | 15.5 ms: 1.01x faster                                                            |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 24.3 ms: 1.12x faster                                                            |
| genshi_xml      | 58.0 ms                                                      | 55.8 ms: 1.04x faster                                                            |
| django_template | 38.9 ms                                                      | 37.4 ms: 1.04x faster                                                            |
| mako            | 10.3 ms                                                      | 10.8 ms: 1.04x slower                                                            |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| gc_traversal               | 4.48 ms                                                      | 1.97 ms: 2.28x faster                                                            |
| create_gc_cycles           | 2.65 ms                                                      | 1.82 ms: 1.45x faster                                                            |
| deepcopy                   | 388 us                                                       | 287 us: 1.35x faster                                                             |
| deepcopy_memo              | 38.9 us                                                      | 29.5 us: 1.32x faster                                                            |
| async_tree_memoization_tg  | 458 ms                                                       | 357 ms: 1.28x faster                                                             |
| async_tree_io              | 832 ms                                                       | 653 ms: 1.27x faster                                                             |
| async_tree_io_tg           | 823 ms                                                       | 652 ms: 1.26x faster                                                             |
| go                         | 167 ms                                                       | 135 ms: 1.24x faster                                                             |
| async_tree_none            | 370 ms                                                       | 304 ms: 1.22x faster                                                             |
| async_tree_memoization     | 447 ms                                                       | 369 ms: 1.21x faster                                                             |
| deepcopy_reduce            | 3.49 us                                                      | 2.95 us: 1.18x faster                                                            |
| generators                 | 33.9 ms                                                      | 29.6 ms: 1.15x faster                                                            |
| async_tree_none_tg         | 342 ms                                                       | 300 ms: 1.14x faster                                                             |
| pylint                     | 345 ms                                                       | 306 ms: 1.13x faster                                                             |
| genshi_text                | 27.2 ms                                                      | 24.3 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 537 ms: 1.11x faster                                                             |
| json                       | 5.62 ms                                                      | 5.09 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 523 ms: 1.10x faster                                                             |
| telco                      | 8.77 ms                                                      | 8.03 ms: 1.09x faster                                                            |
| richards_super             | 60.2 ms                                                      | 55.5 ms: 1.09x faster                                                            |
| pathlib                    | 17.4 ms                                                      | 16.2 ms: 1.08x faster                                                            |
| thrift                     | 918 us                                                       | 857 us: 1.07x faster                                                             |
| pprint_pformat             | 1.70 sec                                                     | 1.59 sec: 1.07x faster                                                           |
| k_core                     | 2.18 sec                                                     | 2.04 sec: 1.07x faster                                                           |
| pprint_safe_repr           | 835 ms                                                       | 788 ms: 1.06x faster                                                             |
| fannkuch                   | 384 ms                                                       | 364 ms: 1.06x faster                                                             |
| scimark_sor                | 125 ms                                                       | 119 ms: 1.05x faster                                                             |
| richards                   | 52.5 ms                                                      | 49.9 ms: 1.05x faster                                                            |
| shortest_path              | 477 ms                                                       | 456 ms: 1.05x faster                                                             |
| nbody                      | 92.1 ms                                                      | 88.1 ms: 1.05x faster                                                            |
| sqlalchemy_declarative     | 148 ms                                                       | 142 ms: 1.04x faster                                                             |
| genshi_xml                 | 58.0 ms                                                      | 55.8 ms: 1.04x faster                                                            |
| python_startup_no_site     | 8.93 ms                                                      | 8.59 ms: 1.04x faster                                                            |
| django_template            | 38.9 ms                                                      | 37.4 ms: 1.04x faster                                                            |
| hexiom                     | 6.47 ms                                                      | 6.25 ms: 1.04x faster                                                            |
| pycparser                  | 1.28 sec                                                     | 1.24 sec: 1.03x faster                                                           |
| meteor_contest             | 130 ms                                                       | 126 ms: 1.03x faster                                                             |
| connected_components       | 443 ms                                                       | 431 ms: 1.03x faster                                                             |
| regex_compile              | 143 ms                                                       | 139 ms: 1.02x faster                                                             |
| coverage                   | 84.5 ms                                                      | 82.6 ms: 1.02x faster                                                            |
| asyncio_websockets         | 395 ms                                                       | 387 ms: 1.02x faster                                                             |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                            |
| spectral_norm              | 97.4 ms                                                      | 96.2 ms: 1.01x faster                                                            |
| sympy_str                  | 297 ms                                                       | 293 ms: 1.01x faster                                                             |
| 2to3                       | 293 ms                                                       | 289 ms: 1.01x faster                                                             |
| nqueens                    | 92.3 ms                                                      | 91.3 ms: 1.01x faster                                                            |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                             |
| python_startup             | 15.6 ms                                                      | 15.5 ms: 1.01x faster                                                            |
| scimark_lu                 | 97.4 ms                                                      | 96.6 ms: 1.01x faster                                                            |
| unpickle_pure_python       | 216 us                                                       | 215 us: 1.01x faster                                                             |
| sympy_expand               | 506 ms                                                       | 503 ms: 1.01x faster                                                             |
| mdp                        | 2.53 sec                                                     | 2.52 sec: 1.00x faster                                                           |
| sympy_integrate            | 23.4 ms                                                      | 23.3 ms: 1.00x faster                                                            |
| json_loads                 | 24.7 us                                                      | 24.9 us: 1.01x slower                                                            |
| regex_v8                   | 24.9 ms                                                      | 25.3 ms: 1.01x slower                                                            |
| tomli_loads                | 2.43 sec                                                     | 2.48 sec: 1.02x slower                                                           |
| scimark_monte_carlo        | 65.2 ms                                                      | 66.3 ms: 1.02x slower                                                            |
| bpe_tokeniser              | 5.09 sec                                                     | 5.18 sec: 1.02x slower                                                           |
| logging_format             | 6.95 us                                                      | 7.09 us: 1.02x slower                                                            |
| logging_simple             | 6.28 us                                                      | 6.42 us: 1.02x slower                                                            |
| docutils                   | 2.81 sec                                                     | 2.88 sec: 1.03x slower                                                           |
| sqlglot_normalize          | 119 ms                                                       | 122 ms: 1.03x slower                                                             |
| comprehensions             | 17.3 us                                                      | 17.8 us: 1.03x slower                                                            |
| regex_effbot               | 3.51 ms                                                      | 3.62 ms: 1.03x slower                                                            |
| pickle_pure_python         | 322 us                                                       | 332 us: 1.03x slower                                                             |
| dulwich_log                | 65.5 ms                                                      | 67.7 ms: 1.03x slower                                                            |
| xml_etree_process          | 60.7 ms                                                      | 62.8 ms: 1.03x slower                                                            |
| sqlglot_transpile          | 1.76 ms                                                      | 1.82 ms: 1.04x slower                                                            |
| chaos                      | 60.6 ms                                                      | 62.8 ms: 1.04x slower                                                            |
| xml_etree_generate         | 85.2 ms                                                      | 88.4 ms: 1.04x slower                                                            |
| sqlglot_optimize           | 58.7 ms                                                      | 61.0 ms: 1.04x slower                                                            |
| mako                       | 10.3 ms                                                      | 10.8 ms: 1.04x slower                                                            |
| logging_silent             | 97.5 ns                                                      | 102 ns: 1.04x slower                                                             |
| raytrace                   | 267 ms                                                       | 279 ms: 1.04x slower                                                             |
| float                      | 81.6 ms                                                      | 85.5 ms: 1.05x slower                                                            |
| regex_dna                  | 238 ms                                                       | 250 ms: 1.05x slower                                                             |
| scimark_fft                | 298 ms                                                       | 315 ms: 1.06x slower                                                             |
| sqlglot_parse              | 1.37 ms                                                      | 1.45 ms: 1.06x slower                                                            |
| deltablue                  | 3.38 ms                                                      | 3.60 ms: 1.06x slower                                                            |
| json_dumps                 | 10.8 ms                                                      | 11.6 ms: 1.07x slower                                                            |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.83 ms: 1.15x slower                                                            |
| xml_etree_parse            | 144 ms                                                       | 166 ms: 1.15x slower                                                             |
| xml_etree_iterparse        | 99.8 ms                                                      | 120 ms: 1.21x slower                                                             |
| async_generators           | 364 ms                                                       | 447 ms: 1.23x slower                                                             |
| bench_mp_pool              | 4.82 ms                                                      | 1.10 sec: 229.36x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                     |

Benchmark hidden because not significant (8): bench_thread_pool, sphinx, pyflate, sqlalchemy_imperative, typing_runtime_protocols, crypto_pyaes, html5lib, pidigits
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241113-3.14.0a1+-47eb1b5/bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.040x faster
# HPT report

- Reliability score: 99.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x
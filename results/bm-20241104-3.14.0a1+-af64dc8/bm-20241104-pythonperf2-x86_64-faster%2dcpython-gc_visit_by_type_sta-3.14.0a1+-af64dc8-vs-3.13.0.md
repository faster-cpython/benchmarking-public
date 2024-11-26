# Results vs. 3.13.0

- fork: faster-cpython
- ref: gc_visit_by_type_sta
- machine: linux-x86_64
- commit hash: af64dc8
- commit date: 2024-11-04
- overall geometric mean: 1.019x faster
- HPT reliability: 99.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 281 ms: 1.04x faster                                                                   |
| docutils       | 2.81 sec                                                     | 2.92 sec: 1.04x slower                                                                 |
| html5lib       | 72.9 ms                                                      | 70.9 ms: 1.03x faster                                                                  |
| sphinx         | 1.11 sec                                                     | 1.14 sec: 1.02x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 374 ms: 1.23x faster                                                                   |
| async_tree_none            | 370 ms                                                       | 330 ms: 1.12x faster                                                                   |
| async_tree_memoization     | 447 ms                                                       | 407 ms: 1.10x faster                                                                   |
| async_tree_none_tg         | 342 ms                                                       | 323 ms: 1.06x faster                                                                   |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 570 ms: 1.05x faster                                                                   |
| asyncio_websockets         | 395 ms                                                       | 380 ms: 1.04x faster                                                                   |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 560 ms: 1.03x faster                                                                   |
| async_generators           | 364 ms                                                       | 369 ms: 1.02x slower                                                                   |
| async_tree_io_tg           | 823 ms                                                       | 868 ms: 1.05x slower                                                                   |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                           |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 89.7 ms: 1.03x faster                                                                  |
| float          | 81.6 ms                                                      | 82.3 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 139 ms: 1.03x faster                                                                   |
| regex_dna      | 238 ms                                                       | 241 ms: 1.01x slower                                                                   |
| regex_effbot   | 3.51 ms                                                      | 3.56 ms: 1.01x slower                                                                  |
| regex_v8       | 24.9 ms                                                      | 25.8 ms: 1.03x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| xml_etree_process    | 60.7 ms                                                      | 59.7 ms: 1.02x faster                                                                  |
| json_loads           | 24.7 us                                                      | 24.4 us: 1.01x faster                                                                  |
| unpickle_pure_python | 216 us                                                       | 220 us: 1.02x slower                                                                   |
| tomli_loads          | 2.43 sec                                                     | 2.47 sec: 1.02x slower                                                                 |
| pickle_pure_python   | 322 us                                                       | 330 us: 1.03x slower                                                                   |
| xml_etree_iterparse  | 99.8 ms                                                      | 103 ms: 1.03x slower                                                                   |
| json_dumps           | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                           |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 15.8 ms: 1.01x slower                                                                  |
| python_startup_no_site | 8.93 ms                                                      | 9.05 ms: 1.01x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_xml      | 58.0 ms                                                      | 55.1 ms: 1.05x faster                                                                  |
| genshi_text     | 27.2 ms                                                      | 26.0 ms: 1.05x faster                                                                  |
| mako            | 10.3 ms                                                      | 10.7 ms: 1.04x slower                                                                  |
| django_template | 38.9 ms                                                      | 40.7 ms: 1.05x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 290 us: 1.34x faster                                                                   |
| deepcopy_memo              | 38.9 us                                                      | 29.5 us: 1.32x faster                                                                  |
| async_tree_memoization_tg  | 458 ms                                                       | 374 ms: 1.23x faster                                                                   |
| go                         | 167 ms                                                       | 137 ms: 1.22x faster                                                                   |
| deepcopy_reduce            | 3.49 us                                                      | 2.96 us: 1.18x faster                                                                  |
| telco                      | 8.77 ms                                                      | 7.73 ms: 1.13x faster                                                                  |
| scimark_sor                | 125 ms                                                       | 110 ms: 1.13x faster                                                                   |
| generators                 | 33.9 ms                                                      | 30.2 ms: 1.12x faster                                                                  |
| async_tree_none            | 370 ms                                                       | 330 ms: 1.12x faster                                                                   |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                                  |
| async_tree_memoization     | 447 ms                                                       | 407 ms: 1.10x faster                                                                   |
| json                       | 5.62 ms                                                      | 5.12 ms: 1.10x faster                                                                  |
| fannkuch                   | 384 ms                                                       | 352 ms: 1.09x faster                                                                   |
| richards_super             | 60.2 ms                                                      | 55.3 ms: 1.09x faster                                                                  |
| coverage                   | 84.5 ms                                                      | 78.2 ms: 1.08x faster                                                                  |
| richards                   | 52.5 ms                                                      | 49.0 ms: 1.07x faster                                                                  |
| pycparser                  | 1.28 sec                                                     | 1.20 sec: 1.06x faster                                                                 |
| pprint_pformat             | 1.70 sec                                                     | 1.60 sec: 1.06x faster                                                                 |
| bpe_tokeniser              | 5.09 sec                                                     | 4.80 sec: 1.06x faster                                                                 |
| pprint_safe_repr           | 835 ms                                                       | 788 ms: 1.06x faster                                                                   |
| async_tree_none_tg         | 342 ms                                                       | 323 ms: 1.06x faster                                                                   |
| bench_thread_pool          | 929 us                                                       | 879 us: 1.06x faster                                                                   |
| pyflate                    | 493 ms                                                       | 466 ms: 1.06x faster                                                                   |
| genshi_xml                 | 58.0 ms                                                      | 55.1 ms: 1.05x faster                                                                  |
| hexiom                     | 6.47 ms                                                      | 6.15 ms: 1.05x faster                                                                  |
| shortest_path              | 477 ms                                                       | 455 ms: 1.05x faster                                                                   |
| genshi_text                | 27.2 ms                                                      | 26.0 ms: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 570 ms: 1.05x faster                                                                   |
| meteor_contest             | 130 ms                                                       | 125 ms: 1.05x faster                                                                   |
| sqlalchemy_declarative     | 148 ms                                                       | 142 ms: 1.04x faster                                                                   |
| thrift                     | 918 us                                                       | 880 us: 1.04x faster                                                                   |
| 2to3                       | 293 ms                                                       | 281 ms: 1.04x faster                                                                   |
| asyncio_websockets         | 395 ms                                                       | 380 ms: 1.04x faster                                                                   |
| connected_components       | 443 ms                                                       | 426 ms: 1.04x faster                                                                   |
| nqueens                    | 92.3 ms                                                      | 88.9 ms: 1.04x faster                                                                  |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                                  |
| regex_compile              | 143 ms                                                       | 139 ms: 1.03x faster                                                                   |
| html5lib                   | 72.9 ms                                                      | 70.9 ms: 1.03x faster                                                                  |
| nbody                      | 92.1 ms                                                      | 89.7 ms: 1.03x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 560 ms: 1.03x faster                                                                   |
| sympy_str                  | 297 ms                                                       | 291 ms: 1.02x faster                                                                   |
| scimark_lu                 | 97.4 ms                                                      | 95.6 ms: 1.02x faster                                                                  |
| xml_etree_process          | 60.7 ms                                                      | 59.7 ms: 1.02x faster                                                                  |
| sympy_sum                  | 154 ms                                                       | 151 ms: 1.02x faster                                                                   |
| sympy_expand               | 506 ms                                                       | 498 ms: 1.02x faster                                                                   |
| spectral_norm              | 97.4 ms                                                      | 96.0 ms: 1.02x faster                                                                  |
| mdp                        | 2.53 sec                                                     | 2.50 sec: 1.01x faster                                                                 |
| json_loads                 | 24.7 us                                                      | 24.4 us: 1.01x faster                                                                  |
| sqlglot_normalize          | 119 ms                                                       | 118 ms: 1.01x faster                                                                   |
| sympy_integrate            | 23.4 ms                                                      | 23.2 ms: 1.01x faster                                                                  |
| sqlalchemy_imperative      | 18.1 ms                                                      | 18.3 ms: 1.01x slower                                                                  |
| float                      | 81.6 ms                                                      | 82.3 ms: 1.01x slower                                                                  |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.26 ms: 1.01x slower                                                                  |
| regex_dna                  | 238 ms                                                       | 241 ms: 1.01x slower                                                                   |
| crypto_pyaes               | 73.5 ms                                                      | 74.5 ms: 1.01x slower                                                                  |
| python_startup             | 15.6 ms                                                      | 15.8 ms: 1.01x slower                                                                  |
| python_startup_no_site     | 8.93 ms                                                      | 9.05 ms: 1.01x slower                                                                  |
| regex_effbot               | 3.51 ms                                                      | 3.56 ms: 1.01x slower                                                                  |
| comprehensions             | 17.3 us                                                      | 17.5 us: 1.01x slower                                                                  |
| unpickle_pure_python       | 216 us                                                       | 220 us: 1.02x slower                                                                   |
| async_generators           | 364 ms                                                       | 369 ms: 1.02x slower                                                                   |
| tomli_loads                | 2.43 sec                                                     | 2.47 sec: 1.02x slower                                                                 |
| deltablue                  | 3.38 ms                                                      | 3.45 ms: 1.02x slower                                                                  |
| sphinx                     | 1.11 sec                                                     | 1.14 sec: 1.02x slower                                                                 |
| dulwich_log                | 65.5 ms                                                      | 67.1 ms: 1.02x slower                                                                  |
| scimark_monte_carlo        | 65.2 ms                                                      | 66.8 ms: 1.02x slower                                                                  |
| pickle_pure_python         | 322 us                                                       | 330 us: 1.03x slower                                                                   |
| logging_silent             | 97.5 ns                                                      | 100 ns: 1.03x slower                                                                   |
| xml_etree_iterparse        | 99.8 ms                                                      | 103 ms: 1.03x slower                                                                   |
| regex_v8                   | 24.9 ms                                                      | 25.8 ms: 1.03x slower                                                                  |
| logging_simple             | 6.28 us                                                      | 6.49 us: 1.03x slower                                                                  |
| mako                       | 10.3 ms                                                      | 10.7 ms: 1.04x slower                                                                  |
| sqlglot_transpile          | 1.76 ms                                                      | 1.83 ms: 1.04x slower                                                                  |
| docutils                   | 2.81 sec                                                     | 2.92 sec: 1.04x slower                                                                 |
| django_template            | 38.9 ms                                                      | 40.7 ms: 1.05x slower                                                                  |
| json_dumps                 | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                                  |
| async_tree_io_tg           | 823 ms                                                       | 868 ms: 1.05x slower                                                                   |
| sqlglot_parse              | 1.37 ms                                                      | 1.45 ms: 1.07x slower                                                                  |
| raytrace                   | 267 ms                                                       | 285 ms: 1.07x slower                                                                   |
| create_gc_cycles           | 2.65 ms                                                      | 3.05 ms: 1.15x slower                                                                  |
| gc_traversal               | 4.48 ms                                                      | 5.78 ms: 1.29x slower                                                                  |
| k_core                     | 2.18 sec                                                     | 3.08 sec: 1.41x slower                                                                 |
| bench_mp_pool              | 4.82 ms                                                      | 2.11 sec: 438.30x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                           |

Benchmark hidden because not significant (10): xml_etree_generate, typing_runtime_protocols, pidigits, sqlglot_optimize, chaos, xml_etree_parse, async_tree_io, scimark_fft, logging_format, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241104-3.14.0a1+-af64dc8/bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8.json: sqlite_synth

- Geometric mean (including insignificant results): 1.019x faster
# HPT report

- Reliability score: 99.75% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x
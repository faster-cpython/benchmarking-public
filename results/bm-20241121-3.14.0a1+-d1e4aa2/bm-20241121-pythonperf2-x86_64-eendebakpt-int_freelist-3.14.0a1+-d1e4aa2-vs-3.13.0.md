# Results vs. 3.13.0

- fork: eendebakpt
- ref: int_freelist
- machine: linux-x86_64
- commit hash: d1e4aa2
- commit date: 2024-11-21
- overall geometric mean: 1.010x faster
- HPT reliability: 99.14%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 283 ms: 1.03x faster                                                     |
| docutils       | 2.81 sec                                                     | 2.92 sec: 1.04x slower                                                   |
| html5lib       | 72.9 ms                                                      | 71.0 ms: 1.03x faster                                                    |
| sphinx         | 1.11 sec                                                     | 1.13 sec: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 380 ms: 1.20x faster                                                     |
| async_tree_none            | 370 ms                                                       | 334 ms: 1.11x faster                                                     |
| async_tree_memoization     | 447 ms                                                       | 413 ms: 1.08x faster                                                     |
| async_tree_none_tg         | 342 ms                                                       | 325 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 580 ms: 1.03x faster                                                     |
| asyncio_websockets         | 395 ms                                                       | 388 ms: 1.02x faster                                                     |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 568 ms: 1.01x faster                                                     |
| async_tree_io              | 832 ms                                                       | 850 ms: 1.02x slower                                                     |
| async_tree_io_tg           | 823 ms                                                       | 871 ms: 1.06x slower                                                     |
| async_generators           | 364 ms                                                       | 436 ms: 1.20x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 81.6 ms                                                      | 80.5 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                             |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 139 ms: 1.03x faster                                                     |
| regex_dna      | 238 ms                                                       | 242 ms: 1.02x slower                                                     |
| regex_effbot   | 3.51 ms                                                      | 3.61 ms: 1.03x slower                                                    |
| regex_v8       | 24.9 ms                                                      | 26.2 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                        | 1.02x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_process    | 60.7 ms                                                      | 59.9 ms: 1.01x faster                                                    |
| unpickle_pure_python | 216 us                                                       | 215 us: 1.01x faster                                                     |
| tomli_loads          | 2.43 sec                                                     | 2.42 sec: 1.01x faster                                                   |
| xml_etree_generate   | 85.2 ms                                                      | 87.3 ms: 1.02x slower                                                    |
| pickle_pure_python   | 322 us                                                       | 333 us: 1.03x slower                                                     |
| json_loads           | 24.7 us                                                      | 25.6 us: 1.03x slower                                                    |
| xml_etree_iterparse  | 99.8 ms                                                      | 104 ms: 1.04x slower                                                     |
| xml_etree_parse      | 144 ms                                                       | 150 ms: 1.04x slower                                                     |
| json_dumps           | 10.8 ms                                                      | 11.5 ms: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.93 ms                                                      | 9.04 ms: 1.01x slower                                                    |
| python_startup         | 15.6 ms                                                      | 16.0 ms: 1.02x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 25.0 ms: 1.09x faster                                                    |
| genshi_xml      | 58.0 ms                                                      | 54.6 ms: 1.06x faster                                                    |
| django_template | 38.9 ms                                                      | 37.3 ms: 1.04x faster                                                    |
| mako            | 10.3 ms                                                      | 10.7 ms: 1.04x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 286 us: 1.36x faster                                                     |
| deepcopy_memo              | 38.9 us                                                      | 29.5 us: 1.32x faster                                                    |
| go                         | 167 ms                                                       | 136 ms: 1.22x faster                                                     |
| async_tree_memoization_tg  | 458 ms                                                       | 380 ms: 1.20x faster                                                     |
| deepcopy_reduce            | 3.49 us                                                      | 2.95 us: 1.18x faster                                                    |
| generators                 | 33.9 ms                                                      | 29.3 ms: 1.16x faster                                                    |
| spectral_norm              | 97.4 ms                                                      | 87.3 ms: 1.12x faster                                                    |
| telco                      | 8.77 ms                                                      | 7.88 ms: 1.11x faster                                                    |
| async_tree_none            | 370 ms                                                       | 334 ms: 1.11x faster                                                     |
| json                       | 5.62 ms                                                      | 5.17 ms: 1.09x faster                                                    |
| genshi_text                | 27.2 ms                                                      | 25.0 ms: 1.09x faster                                                    |
| richards_super             | 60.2 ms                                                      | 55.6 ms: 1.08x faster                                                    |
| async_tree_memoization     | 447 ms                                                       | 413 ms: 1.08x faster                                                     |
| thrift                     | 918 us                                                       | 858 us: 1.07x faster                                                     |
| pathlib                    | 17.4 ms                                                      | 16.3 ms: 1.07x faster                                                    |
| richards                   | 52.5 ms                                                      | 49.3 ms: 1.06x faster                                                    |
| genshi_xml                 | 58.0 ms                                                      | 54.6 ms: 1.06x faster                                                    |
| pycparser                  | 1.28 sec                                                     | 1.21 sec: 1.06x faster                                                   |
| async_tree_none_tg         | 342 ms                                                       | 325 ms: 1.05x faster                                                     |
| pprint_pformat             | 1.70 sec                                                     | 1.62 sec: 1.05x faster                                                   |
| pprint_safe_repr           | 835 ms                                                       | 798 ms: 1.05x faster                                                     |
| shortest_path              | 477 ms                                                       | 457 ms: 1.04x faster                                                     |
| meteor_contest             | 130 ms                                                       | 125 ms: 1.04x faster                                                     |
| sqlalchemy_declarative     | 148 ms                                                       | 142 ms: 1.04x faster                                                     |
| nqueens                    | 92.3 ms                                                      | 88.6 ms: 1.04x faster                                                    |
| django_template            | 38.9 ms                                                      | 37.3 ms: 1.04x faster                                                    |
| bpe_tokeniser              | 5.09 sec                                                     | 4.91 sec: 1.04x faster                                                   |
| 2to3                       | 293 ms                                                       | 283 ms: 1.03x faster                                                     |
| hexiom                     | 6.47 ms                                                      | 6.28 ms: 1.03x faster                                                    |
| regex_compile              | 143 ms                                                       | 139 ms: 1.03x faster                                                     |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 580 ms: 1.03x faster                                                     |
| html5lib                   | 72.9 ms                                                      | 71.0 ms: 1.03x faster                                                    |
| mdp                        | 2.53 sec                                                     | 2.47 sec: 1.02x faster                                                   |
| connected_components       | 443 ms                                                       | 433 ms: 1.02x faster                                                     |
| fannkuch                   | 384 ms                                                       | 376 ms: 1.02x faster                                                     |
| asyncio_websockets         | 395 ms                                                       | 388 ms: 1.02x faster                                                     |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                    |
| float                      | 81.6 ms                                                      | 80.5 ms: 1.01x faster                                                    |
| xml_etree_process          | 60.7 ms                                                      | 59.9 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 568 ms: 1.01x faster                                                     |
| pyflate                    | 493 ms                                                       | 488 ms: 1.01x faster                                                     |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                     |
| sympy_str                  | 297 ms                                                       | 294 ms: 1.01x faster                                                     |
| unpickle_pure_python       | 216 us                                                       | 215 us: 1.01x faster                                                     |
| tomli_loads                | 2.43 sec                                                     | 2.42 sec: 1.01x faster                                                   |
| sympy_expand               | 506 ms                                                       | 504 ms: 1.01x faster                                                     |
| sympy_integrate            | 23.4 ms                                                      | 23.3 ms: 1.00x faster                                                    |
| sqlglot_optimize           | 58.7 ms                                                      | 59.0 ms: 1.01x slower                                                    |
| scimark_sor                | 125 ms                                                       | 126 ms: 1.01x slower                                                     |
| typing_runtime_protocols   | 176 us                                                       | 177 us: 1.01x slower                                                     |
| logging_format             | 6.95 us                                                      | 7.03 us: 1.01x slower                                                    |
| scimark_lu                 | 97.4 ms                                                      | 98.4 ms: 1.01x slower                                                    |
| python_startup_no_site     | 8.93 ms                                                      | 9.04 ms: 1.01x slower                                                    |
| comprehensions             | 17.3 us                                                      | 17.5 us: 1.01x slower                                                    |
| regex_dna                  | 238 ms                                                       | 242 ms: 1.02x slower                                                     |
| sqlglot_transpile          | 1.76 ms                                                      | 1.79 ms: 1.02x slower                                                    |
| dulwich_log                | 65.5 ms                                                      | 66.7 ms: 1.02x slower                                                    |
| sphinx                     | 1.11 sec                                                     | 1.13 sec: 1.02x slower                                                   |
| scimark_monte_carlo        | 65.2 ms                                                      | 66.5 ms: 1.02x slower                                                    |
| crypto_pyaes               | 73.5 ms                                                      | 75.1 ms: 1.02x slower                                                    |
| chaos                      | 60.6 ms                                                      | 61.9 ms: 1.02x slower                                                    |
| async_tree_io              | 832 ms                                                       | 850 ms: 1.02x slower                                                     |
| python_startup             | 15.6 ms                                                      | 16.0 ms: 1.02x slower                                                    |
| xml_etree_generate         | 85.2 ms                                                      | 87.3 ms: 1.02x slower                                                    |
| logging_silent             | 97.5 ns                                                      | 100.0 ns: 1.03x slower                                                   |
| scimark_fft                | 298 ms                                                       | 306 ms: 1.03x slower                                                     |
| regex_effbot               | 3.51 ms                                                      | 3.61 ms: 1.03x slower                                                    |
| pickle_pure_python         | 322 us                                                       | 333 us: 1.03x slower                                                     |
| json_loads                 | 24.7 us                                                      | 25.6 us: 1.03x slower                                                    |
| sqlglot_parse              | 1.37 ms                                                      | 1.41 ms: 1.04x slower                                                    |
| xml_etree_iterparse        | 99.8 ms                                                      | 104 ms: 1.04x slower                                                     |
| raytrace                   | 267 ms                                                       | 278 ms: 1.04x slower                                                     |
| deltablue                  | 3.38 ms                                                      | 3.52 ms: 1.04x slower                                                    |
| xml_etree_parse            | 144 ms                                                       | 150 ms: 1.04x slower                                                     |
| mako                       | 10.3 ms                                                      | 10.7 ms: 1.04x slower                                                    |
| docutils                   | 2.81 sec                                                     | 2.92 sec: 1.04x slower                                                   |
| logging_simple             | 6.28 us                                                      | 6.54 us: 1.04x slower                                                    |
| regex_v8                   | 24.9 ms                                                      | 26.2 ms: 1.05x slower                                                    |
| async_tree_io_tg           | 823 ms                                                       | 871 ms: 1.06x slower                                                     |
| json_dumps                 | 10.8 ms                                                      | 11.5 ms: 1.06x slower                                                    |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.61 ms: 1.09x slower                                                    |
| create_gc_cycles           | 2.65 ms                                                      | 3.00 ms: 1.13x slower                                                    |
| async_generators           | 364 ms                                                       | 436 ms: 1.20x slower                                                     |
| gc_traversal               | 4.48 ms                                                      | 6.15 ms: 1.37x slower                                                    |
| k_core                     | 2.18 sec                                                     | 3.03 sec: 1.39x slower                                                   |
| bench_mp_pool              | 4.82 ms                                                      | 1.22 sec: 253.71x slower                                                 |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                             |

Benchmark hidden because not significant (7): coverage, nbody, bench_thread_pool, pidigits, sqlglot_normalize, sqlalchemy_imperative, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241121-3.14.0a1+-d1e4aa2/bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.010x faster
# HPT report

- Reliability score: 99.14% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x
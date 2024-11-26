# Results vs. 3.13.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: linux-x86_64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.022x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 283 ms: 1.03x faster                                                         |
| docutils       | 2.81 sec                                                     | 2.92 sec: 1.04x slower                                                       |
| html5lib       | 72.9 ms                                                      | 72.3 ms: 1.01x faster                                                        |
| sphinx         | 1.11 sec                                                     | 1.13 sec: 1.02x slower                                                       |
| tornado_http   | 119 ms                                                       | 117 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 373 ms: 1.23x faster                                                         |
| async_tree_none            | 370 ms                                                       | 333 ms: 1.11x faster                                                         |
| async_tree_memoization     | 447 ms                                                       | 417 ms: 1.07x faster                                                         |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 560 ms: 1.06x faster                                                         |
| async_tree_none_tg         | 342 ms                                                       | 322 ms: 1.06x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 386 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 563 ms: 1.02x faster                                                         |
| async_tree_io_tg           | 823 ms                                                       | 863 ms: 1.05x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                 |

Benchmark hidden because not significant (2): async_generators, async_tree_io

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 139 ms: 1.03x faster                                                         |
| regex_v8       | 24.9 ms                                                      | 25.4 ms: 1.02x slower                                                        |
| regex_dna      | 238 ms                                                       | 246 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_process    | 60.7 ms                                                      | 59.3 ms: 1.02x faster                                                        |
| json_loads           | 24.7 us                                                      | 24.5 us: 1.01x faster                                                        |
| pickle_pure_python   | 322 us                                                       | 325 us: 1.01x slower                                                         |
| xml_etree_iterparse  | 99.8 ms                                                      | 101 ms: 1.02x slower                                                         |
| tomli_loads          | 2.43 sec                                                     | 2.47 sec: 1.02x slower                                                       |
| unpickle_pure_python | 216 us                                                       | 220 us: 1.02x slower                                                         |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.02x slower                                                         |
| json_dumps           | 10.8 ms                                                      | 11.4 ms: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 15.7 ms: 1.01x slower                                                        |
| python_startup_no_site | 8.93 ms                                                      | 9.03 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 24.7 ms: 1.10x faster                                                        |
| genshi_xml      | 58.0 ms                                                      | 55.2 ms: 1.05x faster                                                        |
| django_template | 38.9 ms                                                      | 40.2 ms: 1.03x slower                                                        |
| mako            | 10.3 ms                                                      | 10.7 ms: 1.04x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 291 us: 1.33x faster                                                         |
| deepcopy_memo              | 38.9 us                                                      | 29.2 us: 1.33x faster                                                        |
| async_tree_memoization_tg  | 458 ms                                                       | 373 ms: 1.23x faster                                                         |
| go                         | 167 ms                                                       | 136 ms: 1.23x faster                                                         |
| deepcopy_reduce            | 3.49 us                                                      | 2.95 us: 1.19x faster                                                        |
| generators                 | 33.9 ms                                                      | 29.2 ms: 1.16x faster                                                        |
| async_tree_none            | 370 ms                                                       | 333 ms: 1.11x faster                                                         |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                        |
| telco                      | 8.77 ms                                                      | 7.94 ms: 1.10x faster                                                        |
| genshi_text                | 27.2 ms                                                      | 24.7 ms: 1.10x faster                                                        |
| fannkuch                   | 384 ms                                                       | 352 ms: 1.09x faster                                                         |
| json                       | 5.62 ms                                                      | 5.17 ms: 1.09x faster                                                        |
| richards_super             | 60.2 ms                                                      | 55.4 ms: 1.09x faster                                                        |
| thrift                     | 918 us                                                       | 855 us: 1.07x faster                                                         |
| async_tree_memoization     | 447 ms                                                       | 417 ms: 1.07x faster                                                         |
| scimark_sor                | 125 ms                                                       | 117 ms: 1.07x faster                                                         |
| coverage                   | 84.5 ms                                                      | 79.3 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 560 ms: 1.06x faster                                                         |
| richards                   | 52.5 ms                                                      | 49.5 ms: 1.06x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 322 ms: 1.06x faster                                                         |
| pprint_pformat             | 1.70 sec                                                     | 1.61 sec: 1.06x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.83 sec: 1.05x faster                                                       |
| genshi_xml                 | 58.0 ms                                                      | 55.2 ms: 1.05x faster                                                        |
| pprint_safe_repr           | 835 ms                                                       | 796 ms: 1.05x faster                                                         |
| sqlalchemy_declarative     | 148 ms                                                       | 142 ms: 1.04x faster                                                         |
| 2to3                       | 293 ms                                                       | 283 ms: 1.03x faster                                                         |
| meteor_contest             | 130 ms                                                       | 126 ms: 1.03x faster                                                         |
| bench_thread_pool          | 929 us                                                       | 901 us: 1.03x faster                                                         |
| pycparser                  | 1.28 sec                                                     | 1.24 sec: 1.03x faster                                                       |
| pyflate                    | 493 ms                                                       | 479 ms: 1.03x faster                                                         |
| regex_compile              | 143 ms                                                       | 139 ms: 1.03x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                        |
| xml_etree_process          | 60.7 ms                                                      | 59.3 ms: 1.02x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 386 ms: 1.02x faster                                                         |
| nqueens                    | 92.3 ms                                                      | 90.4 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 563 ms: 1.02x faster                                                         |
| tornado_http               | 119 ms                                                       | 117 ms: 1.02x faster                                                         |
| sympy_str                  | 297 ms                                                       | 292 ms: 1.02x faster                                                         |
| crypto_pyaes               | 73.5 ms                                                      | 72.3 ms: 1.02x faster                                                        |
| scimark_fft                | 298 ms                                                       | 294 ms: 1.01x faster                                                         |
| hexiom                     | 6.47 ms                                                      | 6.40 ms: 1.01x faster                                                        |
| scimark_lu                 | 97.4 ms                                                      | 96.4 ms: 1.01x faster                                                        |
| mdp                        | 2.53 sec                                                     | 2.51 sec: 1.01x faster                                                       |
| json_loads                 | 24.7 us                                                      | 24.5 us: 1.01x faster                                                        |
| html5lib                   | 72.9 ms                                                      | 72.3 ms: 1.01x faster                                                        |
| sympy_expand               | 506 ms                                                       | 502 ms: 1.01x faster                                                         |
| sympy_sum                  | 154 ms                                                       | 153 ms: 1.01x faster                                                         |
| sqlglot_normalize          | 119 ms                                                       | 118 ms: 1.00x faster                                                         |
| dulwich_log                | 65.5 ms                                                      | 65.2 ms: 1.00x faster                                                        |
| python_startup             | 15.6 ms                                                      | 15.7 ms: 1.01x slower                                                        |
| logging_silent             | 97.5 ns                                                      | 98.2 ns: 1.01x slower                                                        |
| pickle_pure_python         | 322 us                                                       | 325 us: 1.01x slower                                                         |
| deltablue                  | 3.38 ms                                                      | 3.42 ms: 1.01x slower                                                        |
| python_startup_no_site     | 8.93 ms                                                      | 9.03 ms: 1.01x slower                                                        |
| typing_runtime_protocols   | 176 us                                                       | 178 us: 1.01x slower                                                         |
| sqlglot_transpile          | 1.76 ms                                                      | 1.79 ms: 1.01x slower                                                        |
| xml_etree_iterparse        | 99.8 ms                                                      | 101 ms: 1.02x slower                                                         |
| sphinx                     | 1.11 sec                                                     | 1.13 sec: 1.02x slower                                                       |
| tomli_loads                | 2.43 sec                                                     | 2.47 sec: 1.02x slower                                                       |
| sqlalchemy_imperative      | 18.1 ms                                                      | 18.4 ms: 1.02x slower                                                        |
| regex_v8                   | 24.9 ms                                                      | 25.4 ms: 1.02x slower                                                        |
| unpickle_pure_python       | 216 us                                                       | 220 us: 1.02x slower                                                         |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.02x slower                                                         |
| spectral_norm              | 97.4 ms                                                      | 99.3 ms: 1.02x slower                                                        |
| scimark_monte_carlo        | 65.2 ms                                                      | 66.5 ms: 1.02x slower                                                        |
| comprehensions             | 17.3 us                                                      | 17.6 us: 1.02x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.32 ms: 1.03x slower                                                        |
| sqlglot_parse              | 1.37 ms                                                      | 1.41 ms: 1.03x slower                                                        |
| regex_dna                  | 238 ms                                                       | 246 ms: 1.03x slower                                                         |
| django_template            | 38.9 ms                                                      | 40.2 ms: 1.03x slower                                                        |
| logging_format             | 6.95 us                                                      | 7.21 us: 1.04x slower                                                        |
| mako                       | 10.3 ms                                                      | 10.7 ms: 1.04x slower                                                        |
| docutils                   | 2.81 sec                                                     | 2.92 sec: 1.04x slower                                                       |
| raytrace                   | 267 ms                                                       | 279 ms: 1.04x slower                                                         |
| async_tree_io_tg           | 823 ms                                                       | 863 ms: 1.05x slower                                                         |
| chaos                      | 60.6 ms                                                      | 63.5 ms: 1.05x slower                                                        |
| json_dumps                 | 10.8 ms                                                      | 11.4 ms: 1.05x slower                                                        |
| logging_simple             | 6.28 us                                                      | 6.60 us: 1.05x slower                                                        |
| create_gc_cycles           | 2.65 ms                                                      | 2.98 ms: 1.12x slower                                                        |
| gc_traversal               | 4.48 ms                                                      | 5.31 ms: 1.19x slower                                                        |
| bench_mp_pool              | 4.82 ms                                                      | 2.11 sec: 437.74x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                 |

Benchmark hidden because not significant (10): nbody, xml_etree_generate, float, sympy_integrate, sqlglot_optimize, regex_effbot, pidigits, async_generators, async_tree_io, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path

- Geometric mean (including insignificant results): 1.022x faster
# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x
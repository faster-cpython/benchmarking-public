# Results vs. base

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: ba20c7c
- commit date: 2024-12-04
- overall geometric mean: 1.007x slower
- HPT reliability: 99.78%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 257 ms: 1.01x slower                                                       |
| docutils       | 2.60 sec                                                               | 2.59 sec: 1.00x faster                                                     |
| html5lib       | 63.1 ms                                                                | 64.6 ms: 1.02x slower                                                      |
| sphinx         | 1.02 sec                                                               | 1.03 sec: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io              | 633 ms                                                                 | 608 ms: 1.04x faster                                                       |
| coroutines                 | 23.5 ms                                                                | 23.3 ms: 1.01x faster                                                      |
| async_generators           | 429 ms                                                                 | 426 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                 | 493 ms: 1.01x slower                                                       |
| async_tree_none            | 271 ms                                                                 | 275 ms: 1.02x slower                                                       |
| async_tree_memoization     | 341 ms                                                                 | 350 ms: 1.03x slower                                                       |
| async_tree_memoization_tg  | 315 ms                                                                 | 344 ms: 1.09x slower                                                       |
| async_tree_none_tg         | 252 ms                                                                 | 276 ms: 1.10x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.02x slower                                                               |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 191 ms: 1.02x slower                                                       |
| float          | 78.0 ms                                                                | 80.7 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                 | 128 ms: 1.00x slower                                                       |
| regex_dna      | 213 ms                                                                 | 220 ms: 1.03x slower                                                       |
| regex_v8       | 25.2 ms                                                                | 26.1 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 328 us                                                                 | 324 us: 1.01x faster                                                       |
| unpickle_pure_python | 219 us                                                                 | 217 us: 1.01x faster                                                       |
| tomli_loads          | 2.11 sec                                                               | 2.13 sec: 1.01x slower                                                     |
| xml_etree_process    | 59.0 ms                                                                | 61.6 ms: 1.04x slower                                                      |
| xml_etree_parse      | 139 ms                                                                 | 146 ms: 1.05x slower                                                       |
| xml_etree_generate   | 83.8 ms                                                                | 88.3 ms: 1.05x slower                                                      |
| xml_etree_iterparse  | 96.9 ms                                                                | 104 ms: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                               |

Benchmark hidden because not significant (2): json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                                | 12.7 ms: 1.00x slower                                                      |
| python_startup_no_site | 7.02 ms                                                                | 7.04 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text    | 22.4 ms                                                                | 22.2 ms: 1.01x faster                                                      |
| genshi_xml     | 49.6 ms                                                                | 50.3 ms: 1.01x slower                                                      |
| mako           | 11.2 ms                                                                | 11.4 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| create_gc_cycles           | 2.47 ms                                                                | 2.27 ms: 1.09x faster                                                      |
| async_tree_io              | 633 ms                                                                 | 608 ms: 1.04x faster                                                       |
| k_core                     | 2.29 sec                                                               | 2.21 sec: 1.04x faster                                                     |
| pycparser                  | 1.13 sec                                                               | 1.10 sec: 1.03x faster                                                     |
| pprint_pformat             | 1.52 sec                                                               | 1.49 sec: 1.03x faster                                                     |
| pprint_safe_repr           | 744 ms                                                                 | 726 ms: 1.02x faster                                                       |
| json                       | 5.00 ms                                                                | 4.89 ms: 1.02x faster                                                      |
| meteor_contest             | 107 ms                                                                 | 106 ms: 1.02x faster                                                       |
| pathlib                    | 16.5 ms                                                                | 16.2 ms: 1.01x faster                                                      |
| pickle_pure_python         | 328 us                                                                 | 324 us: 1.01x faster                                                       |
| richards                   | 47.3 ms                                                                | 46.8 ms: 1.01x faster                                                      |
| coroutines                 | 23.5 ms                                                                | 23.3 ms: 1.01x faster                                                      |
| genshi_text                | 22.4 ms                                                                | 22.2 ms: 1.01x faster                                                      |
| async_generators           | 429 ms                                                                 | 426 ms: 1.01x faster                                                       |
| unpickle_pure_python       | 219 us                                                                 | 217 us: 1.01x faster                                                       |
| bench_mp_pool              | 81.1 ms                                                                | 80.6 ms: 1.01x faster                                                      |
| scimark_monte_carlo        | 69.0 ms                                                                | 68.6 ms: 1.01x faster                                                      |
| thrift                     | 766 us                                                                 | 762 us: 1.00x faster                                                       |
| docutils                   | 2.60 sec                                                               | 2.59 sec: 1.00x faster                                                     |
| logging_silent             | 107 ns                                                                 | 107 ns: 1.00x faster                                                       |
| fannkuch                   | 406 ms                                                                 | 405 ms: 1.00x faster                                                       |
| sqlalchemy_declarative     | 127 ms                                                                 | 127 ms: 1.00x faster                                                       |
| crypto_pyaes               | 72.3 ms                                                                | 72.1 ms: 1.00x faster                                                      |
| python_startup             | 12.7 ms                                                                | 12.7 ms: 1.00x slower                                                      |
| python_startup_no_site     | 7.02 ms                                                                | 7.04 ms: 1.00x slower                                                      |
| regex_compile              | 128 ms                                                                 | 128 ms: 1.00x slower                                                       |
| sqlalchemy_imperative      | 16.5 ms                                                                | 16.6 ms: 1.00x slower                                                      |
| bench_thread_pool          | 850 us                                                                 | 854 us: 1.00x slower                                                       |
| dulwich_log                | 64.6 ms                                                                | 64.9 ms: 1.00x slower                                                      |
| deepcopy_memo              | 30.6 us                                                                | 30.7 us: 1.01x slower                                                      |
| comprehensions             | 17.0 us                                                                | 17.1 us: 1.01x slower                                                      |
| gc_traversal               | 4.79 ms                                                                | 4.82 ms: 1.01x slower                                                      |
| sqlglot_transpile          | 1.61 ms                                                                | 1.62 ms: 1.01x slower                                                      |
| nqueens                    | 80.2 ms                                                                | 80.7 ms: 1.01x slower                                                      |
| logging_simple             | 5.56 us                                                                | 5.60 us: 1.01x slower                                                      |
| tomli_loads                | 2.11 sec                                                               | 2.13 sec: 1.01x slower                                                     |
| scimark_fft                | 364 ms                                                                 | 367 ms: 1.01x slower                                                       |
| raytrace                   | 272 ms                                                                 | 275 ms: 1.01x slower                                                       |
| 2to3                       | 254 ms                                                                 | 257 ms: 1.01x slower                                                       |
| sqlglot_optimize           | 53.5 ms                                                                | 54.1 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                 | 493 ms: 1.01x slower                                                       |
| sphinx                     | 1.02 sec                                                               | 1.03 sec: 1.01x slower                                                     |
| chaos                      | 60.6 ms                                                                | 61.2 ms: 1.01x slower                                                      |
| sqlglot_parse              | 1.29 ms                                                                | 1.30 ms: 1.01x slower                                                      |
| hexiom                     | 6.23 ms                                                                | 6.30 ms: 1.01x slower                                                      |
| genshi_xml                 | 49.6 ms                                                                | 50.3 ms: 1.01x slower                                                      |
| async_tree_none            | 271 ms                                                                 | 275 ms: 1.02x slower                                                       |
| many_optionals             | 939 us                                                                 | 953 us: 1.02x slower                                                       |
| pyflate                    | 468 ms                                                                 | 475 ms: 1.02x slower                                                       |
| mako                       | 11.2 ms                                                                | 11.4 ms: 1.02x slower                                                      |
| go                         | 119 ms                                                                 | 121 ms: 1.02x slower                                                       |
| mdp                        | 2.55 sec                                                               | 2.60 sec: 1.02x slower                                                     |
| bpe_tokeniser              | 4.51 sec                                                               | 4.61 sec: 1.02x slower                                                     |
| subparsers                 | 20.7 ms                                                                | 21.2 ms: 1.02x slower                                                      |
| pidigits                   | 186 ms                                                                 | 191 ms: 1.02x slower                                                       |
| html5lib                   | 63.1 ms                                                                | 64.6 ms: 1.02x slower                                                      |
| async_tree_memoization     | 341 ms                                                                 | 350 ms: 1.03x slower                                                       |
| deltablue                  | 3.27 ms                                                                | 3.35 ms: 1.03x slower                                                      |
| coverage                   | 83.1 ms                                                                | 85.6 ms: 1.03x slower                                                      |
| regex_dna                  | 213 ms                                                                 | 220 ms: 1.03x slower                                                       |
| float                      | 78.0 ms                                                                | 80.7 ms: 1.03x slower                                                      |
| regex_v8                   | 25.2 ms                                                                | 26.1 ms: 1.03x slower                                                      |
| generators                 | 28.0 ms                                                                | 29.1 ms: 1.04x slower                                                      |
| spectral_norm              | 111 ms                                                                 | 116 ms: 1.04x slower                                                       |
| xml_etree_process          | 59.0 ms                                                                | 61.6 ms: 1.04x slower                                                      |
| xml_etree_parse            | 139 ms                                                                 | 146 ms: 1.05x slower                                                       |
| xml_etree_generate         | 83.8 ms                                                                | 88.3 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 96.9 ms                                                                | 104 ms: 1.08x slower                                                       |
| async_tree_memoization_tg  | 315 ms                                                                 | 344 ms: 1.09x slower                                                       |
| async_tree_none_tg         | 252 ms                                                                 | 276 ms: 1.10x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (27): pylint, connected_components, json_loads, sqlite_synth, json_dumps, deepcopy_reduce, nbody, shortest_path, async_tree_io_tg, sympy_sum, async_tree_cpu_io_mixed, scimark_sparse_mat_mult, scimark_sor, richards_super, typing_runtime_protocols, logging_format, sympy_integrate, regex_effbot, sympy_expand, asyncio_websockets, django_template, sqlglot_normalize, deepcopy, sympy_str, scimark_lu, telco, djangocms

- Geometric mean (including insignificant results): 1.007x slower

# HPT report

- Reliability score: 99.78% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.98x
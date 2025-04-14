# Results vs. base

- fork: faster-cpython
- ref: remove_most_conditio
- machine: linux-x86_64
- commit hash: 1e0f842
- commit date: 2025-01-24
- overall geometric mean: 1.000x faster
- HPT reliability: 76.79%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 337 ms                                                                       | 336 ms: 1.00x faster                                                                   |
| docutils       | 2.98 sec                                                                     | 2.99 sec: 1.00x slower                                                                 |
| html5lib       | 73.8 ms                                                                      | 74.2 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_generators           | 477 ms                                                                       | 469 ms: 1.02x faster                                                                   |
| async_tree_io              | 621 ms                                                                       | 616 ms: 1.01x faster                                                                   |
| async_tree_none            | 297 ms                                                                       | 295 ms: 1.01x faster                                                                   |
| async_tree_memoization     | 367 ms                                                                       | 364 ms: 1.01x faster                                                                   |
| coroutines                 | 21.9 ms                                                                      | 21.8 ms: 1.01x faster                                                                  |
| async_tree_memoization_tg  | 331 ms                                                                       | 329 ms: 1.01x faster                                                                   |
| async_tree_io_tg           | 580 ms                                                                       | 577 ms: 1.00x faster                                                                   |
| async_tree_none_tg         | 257 ms                                                                       | 256 ms: 1.00x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 496 ms                                                                       | 495 ms: 1.00x faster                                                                   |
| Geometric mean             | (ref)                                                                        | 1.01x faster                                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 75.5 ms                                                                      | 75.0 ms: 1.01x faster                                                                  |
| pidigits       | 248 ms                                                                       | 249 ms: 1.00x slower                                                                   |
| nbody          | 132 ms                                                                       | 138 ms: 1.05x slower                                                                   |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_dna      | 248 ms                                                                       | 241 ms: 1.03x faster                                                                   |
| regex_v8       | 25.8 ms                                                                      | 25.3 ms: 1.02x faster                                                                  |
| regex_compile  | 157 ms                                                                       | 156 ms: 1.01x faster                                                                   |
| regex_effbot   | 3.15 ms                                                                      | 3.16 ms: 1.00x slower                                                                  |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_loads           | 28.3 us                                                                      | 27.7 us: 1.02x faster                                                                  |
| pickle_pure_python   | 380 us                                                                       | 380 us: 1.00x faster                                                                   |
| json_dumps           | 13.5 ms                                                                      | 13.5 ms: 1.00x slower                                                                  |
| xml_etree_parse      | 136 ms                                                                       | 137 ms: 1.01x slower                                                                   |
| xml_etree_generate   | 99.1 ms                                                                      | 100 ms: 1.01x slower                                                                   |
| unpickle_pure_python | 237 us                                                                       | 242 us: 1.02x slower                                                                   |
| Geometric mean       | (ref)                                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (3): xml_etree_process, tomli_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 18.6 ms                                                                      | 18.6 ms: 1.00x slower                                                                  |
| python_startup_no_site | 11.7 ms                                                                      | 11.8 ms: 1.00x slower                                                                  |
| Geometric mean         | (ref)                                                                        | 1.00x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|-----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_xml      | 63.5 ms                                                                      | 62.4 ms: 1.02x faster                                                                  |
| django_template | 47.9 ms                                                                      | 47.2 ms: 1.01x faster                                                                  |
| genshi_text     | 29.3 ms                                                                      | 29.0 ms: 1.01x faster                                                                  |
| Geometric mean  | (ref)                                                                        | 1.01x faster                                                                           |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| coverage                   | 107 ms                                                                       | 100 ms: 1.07x faster                                                                   |
| regex_dna                  | 248 ms                                                                       | 241 ms: 1.03x faster                                                                   |
| regex_v8                   | 25.8 ms                                                                      | 25.3 ms: 1.02x faster                                                                  |
| logging_format             | 8.11 us                                                                      | 7.95 us: 1.02x faster                                                                  |
| json_loads                 | 28.3 us                                                                      | 27.7 us: 1.02x faster                                                                  |
| genshi_xml                 | 63.5 ms                                                                      | 62.4 ms: 1.02x faster                                                                  |
| async_generators           | 477 ms                                                                       | 469 ms: 1.02x faster                                                                   |
| deepcopy_memo              | 37.9 us                                                                      | 37.4 us: 1.02x faster                                                                  |
| django_template            | 47.9 ms                                                                      | 47.2 ms: 1.01x faster                                                                  |
| pathlib                    | 16.5 ms                                                                      | 16.3 ms: 1.01x faster                                                                  |
| logging_simple             | 7.26 us                                                                      | 7.16 us: 1.01x faster                                                                  |
| typing_runtime_protocols   | 224 us                                                                       | 221 us: 1.01x faster                                                                   |
| regex_compile              | 157 ms                                                                       | 156 ms: 1.01x faster                                                                   |
| gc_traversal               | 4.10 ms                                                                      | 4.05 ms: 1.01x faster                                                                  |
| genshi_text                | 29.3 ms                                                                      | 29.0 ms: 1.01x faster                                                                  |
| bpe_tokeniser              | 5.22 sec                                                                     | 5.17 sec: 1.01x faster                                                                 |
| deltablue                  | 4.56 ms                                                                      | 4.51 ms: 1.01x faster                                                                  |
| async_tree_io              | 621 ms                                                                       | 616 ms: 1.01x faster                                                                   |
| async_tree_none            | 297 ms                                                                       | 295 ms: 1.01x faster                                                                   |
| crypto_pyaes               | 93.7 ms                                                                      | 92.9 ms: 1.01x faster                                                                  |
| async_tree_memoization     | 367 ms                                                                       | 364 ms: 1.01x faster                                                                   |
| float                      | 75.5 ms                                                                      | 75.0 ms: 1.01x faster                                                                  |
| coroutines                 | 21.9 ms                                                                      | 21.8 ms: 1.01x faster                                                                  |
| sqlglot_optimize           | 66.3 ms                                                                      | 65.9 ms: 1.01x faster                                                                  |
| async_tree_memoization_tg  | 331 ms                                                                       | 329 ms: 1.01x faster                                                                   |
| mdp                        | 2.79 sec                                                                     | 2.77 sec: 1.01x faster                                                                 |
| pyflate                    | 498 ms                                                                       | 496 ms: 1.01x faster                                                                   |
| meteor_contest             | 156 ms                                                                       | 155 ms: 1.00x faster                                                                   |
| async_tree_io_tg           | 580 ms                                                                       | 577 ms: 1.00x faster                                                                   |
| hexiom                     | 7.24 ms                                                                      | 7.21 ms: 1.00x faster                                                                  |
| async_tree_none_tg         | 257 ms                                                                       | 256 ms: 1.00x faster                                                                   |
| 2to3                       | 337 ms                                                                       | 336 ms: 1.00x faster                                                                   |
| sqlalchemy_declarative     | 178 ms                                                                       | 177 ms: 1.00x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 496 ms                                                                       | 495 ms: 1.00x faster                                                                   |
| pprint_pformat             | 1.86 sec                                                                     | 1.86 sec: 1.00x faster                                                                 |
| pickle_pure_python         | 380 us                                                                       | 380 us: 1.00x faster                                                                   |
| connected_components       | 495 ms                                                                       | 494 ms: 1.00x faster                                                                   |
| pprint_safe_repr           | 899 ms                                                                       | 900 ms: 1.00x slower                                                                   |
| json_dumps                 | 13.5 ms                                                                      | 13.5 ms: 1.00x slower                                                                  |
| python_startup             | 18.6 ms                                                                      | 18.6 ms: 1.00x slower                                                                  |
| sqlglot_normalize          | 130 ms                                                                       | 131 ms: 1.00x slower                                                                   |
| python_startup_no_site     | 11.7 ms                                                                      | 11.8 ms: 1.00x slower                                                                  |
| sympy_sum                  | 176 ms                                                                       | 177 ms: 1.00x slower                                                                   |
| pidigits                   | 248 ms                                                                       | 249 ms: 1.00x slower                                                                   |
| many_optionals             | 1.12 ms                                                                      | 1.13 ms: 1.00x slower                                                                  |
| k_core                     | 2.40 sec                                                                     | 2.41 sec: 1.00x slower                                                                 |
| docutils                   | 2.98 sec                                                                     | 2.99 sec: 1.00x slower                                                                 |
| regex_effbot               | 3.15 ms                                                                      | 3.16 ms: 1.00x slower                                                                  |
| comprehensions             | 21.1 us                                                                      | 21.2 us: 1.00x slower                                                                  |
| logging_silent             | 102 ns                                                                       | 103 ns: 1.00x slower                                                                   |
| html5lib                   | 73.8 ms                                                                      | 74.2 ms: 1.01x slower                                                                  |
| xml_etree_parse            | 136 ms                                                                       | 137 ms: 1.01x slower                                                                   |
| scimark_sor                | 120 ms                                                                       | 121 ms: 1.01x slower                                                                   |
| deepcopy                   | 338 us                                                                       | 341 us: 1.01x slower                                                                   |
| chaos                      | 70.7 ms                                                                      | 71.3 ms: 1.01x slower                                                                  |
| sympy_expand               | 569 ms                                                                       | 575 ms: 1.01x slower                                                                   |
| go                         | 150 ms                                                                       | 151 ms: 1.01x slower                                                                   |
| dulwich_log                | 69.2 ms                                                                      | 70.0 ms: 1.01x slower                                                                  |
| xml_etree_generate         | 99.1 ms                                                                      | 100 ms: 1.01x slower                                                                   |
| scimark_lu                 | 118 ms                                                                       | 120 ms: 1.02x slower                                                                   |
| nqueens                    | 110 ms                                                                       | 111 ms: 1.02x slower                                                                   |
| fannkuch                   | 467 ms                                                                       | 475 ms: 1.02x slower                                                                   |
| deepcopy_reduce            | 3.59 us                                                                      | 3.65 us: 1.02x slower                                                                  |
| scimark_monte_carlo        | 86.0 ms                                                                      | 87.9 ms: 1.02x slower                                                                  |
| unpickle_pure_python       | 237 us                                                                       | 242 us: 1.02x slower                                                                   |
| raytrace                   | 334 ms                                                                       | 342 ms: 1.02x slower                                                                   |
| scimark_sparse_mat_mult    | 5.52 ms                                                                      | 5.66 ms: 1.03x slower                                                                  |
| spectral_norm              | 98.8 ms                                                                      | 102 ms: 1.03x slower                                                                   |
| scimark_fft                | 335 ms                                                                       | 347 ms: 1.04x slower                                                                   |
| nbody                      | 132 ms                                                                       | 138 ms: 1.05x slower                                                                   |
| Geometric mean             | (ref)                                                                        | 1.00x faster                                                                           |

Benchmark hidden because not significant (26): asyncio_websockets, sqlalchemy_imperative, generators, richards, pylint, mako, subparsers, sqlglot_transpile, async_tree_cpu_io_mixed, telco, richards_super, xml_etree_process, sqlglot_parse, json, sympy_integrate, bench_mp_pool, sphinx, sqlite_synth, tomli_loads, shortest_path, thrift, sympy_str, pycparser, xml_etree_iterparse, bench_thread_pool, create_gc_cycles

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 76.79% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x
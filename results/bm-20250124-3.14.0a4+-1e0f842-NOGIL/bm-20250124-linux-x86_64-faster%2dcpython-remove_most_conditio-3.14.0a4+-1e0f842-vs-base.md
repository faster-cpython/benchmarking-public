# Results vs. base

- fork: faster-cpython
- ref: remove_most_conditio
- machine: linux-x86_64
- commit hash: 1e0f842
- commit date: 2025-01-24
- overall geometric mean: 1.010x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                 | 313 ms: 1.01x slower                                                             |
| docutils       | 2.85 sec                                                               | 2.87 sec: 1.01x slower                                                           |
| html5lib       | 69.4 ms                                                                | 71.0 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| coroutines                 | 25.3 ms                                                                | 25.6 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed    | 527 ms                                                                 | 534 ms: 1.01x slower                                                             |
| async_tree_cpu_io_mixed_tg | 482 ms                                                                 | 491 ms: 1.02x slower                                                             |
| async_tree_io              | 610 ms                                                                 | 621 ms: 1.02x slower                                                             |
| async_tree_memoization     | 368 ms                                                                 | 375 ms: 1.02x slower                                                             |
| async_tree_none            | 289 ms                                                                 | 296 ms: 1.02x slower                                                             |
| async_tree_none_tg         | 246 ms                                                                 | 253 ms: 1.02x slower                                                             |
| async_tree_memoization_tg  | 326 ms                                                                 | 335 ms: 1.03x slower                                                             |
| async_tree_io_tg           | 557 ms                                                                 | 574 ms: 1.03x slower                                                             |
| Geometric mean             | (ref)                                                                  | 1.02x slower                                                                     |

Benchmark hidden because not significant (2): asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 181 ms                                                                 | 181 ms: 1.00x slower                                                             |
| float          | 78.0 ms                                                                | 78.4 ms: 1.01x slower                                                            |
| nbody          | 135 ms                                                                 | 143 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 24.9 ms                                                                | 25.1 ms: 1.01x slower                                                            |
| regex_compile  | 149 ms                                                                 | 151 ms: 1.01x slower                                                             |
| regex_dna      | 222 ms                                                                 | 228 ms: 1.03x slower                                                             |
| regex_effbot   | 3.35 ms                                                                | 3.50 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_process    | 68.3 ms                                                                | 68.7 ms: 1.01x slower                                                            |
| xml_etree_generate   | 95.3 ms                                                                | 96.0 ms: 1.01x slower                                                            |
| json_loads           | 31.6 us                                                                | 31.8 us: 1.01x slower                                                            |
| pickle_pure_python   | 372 us                                                                 | 376 us: 1.01x slower                                                             |
| json_dumps           | 12.6 ms                                                                | 12.8 ms: 1.02x slower                                                            |
| unpickle_pure_python | 255 us                                                                 | 261 us: 1.02x slower                                                             |
| tomli_loads          | 2.36 sec                                                               | 2.43 sec: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 9.36 ms                                                                | 9.39 ms: 1.00x slower                                                            |
| python_startup         | 15.0 ms                                                                | 15.1 ms: 1.00x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako           | 16.4 ms                                                                | 16.5 ms: 1.01x slower                                                            |
| genshi_text    | 28.1 ms                                                                | 28.8 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| gc_traversal               | 4.44 ms                                                                | 4.22 ms: 1.05x faster                                                            |
| logging_silent             | 122 ns                                                                 | 117 ns: 1.05x faster                                                             |
| pathlib                    | 16.6 ms                                                                | 16.2 ms: 1.02x faster                                                            |
| scimark_lu                 | 142 ms                                                                 | 140 ms: 1.02x faster                                                             |
| create_gc_cycles           | 1.73 ms                                                                | 1.70 ms: 1.02x faster                                                            |
| sqlite_synth               | 2.76 us                                                                | 2.74 us: 1.01x faster                                                            |
| nqueens                    | 100 ms                                                                 | 99.5 ms: 1.01x faster                                                            |
| bpe_tokeniser              | 5.07 sec                                                               | 5.05 sec: 1.01x faster                                                           |
| connected_components       | 531 ms                                                                 | 529 ms: 1.00x faster                                                             |
| pidigits                   | 181 ms                                                                 | 181 ms: 1.00x slower                                                             |
| fannkuch                   | 516 ms                                                                 | 517 ms: 1.00x slower                                                             |
| python_startup_no_site     | 9.36 ms                                                                | 9.39 ms: 1.00x slower                                                            |
| pprint_safe_repr           | 853 ms                                                                 | 856 ms: 1.00x slower                                                             |
| python_startup             | 15.0 ms                                                                | 15.1 ms: 1.00x slower                                                            |
| logging_format             | 7.51 us                                                                | 7.54 us: 1.01x slower                                                            |
| sympy_sum                  | 176 ms                                                                 | 177 ms: 1.01x slower                                                             |
| float                      | 78.0 ms                                                                | 78.4 ms: 1.01x slower                                                            |
| sqlglot_optimize           | 60.5 ms                                                                | 60.9 ms: 1.01x slower                                                            |
| mdp                        | 2.86 sec                                                               | 2.88 sec: 1.01x slower                                                           |
| hexiom                     | 7.84 ms                                                                | 7.89 ms: 1.01x slower                                                            |
| sympy_str                  | 318 ms                                                                 | 320 ms: 1.01x slower                                                             |
| xml_etree_process          | 68.3 ms                                                                | 68.7 ms: 1.01x slower                                                            |
| scimark_sor                | 142 ms                                                                 | 143 ms: 1.01x slower                                                             |
| pprint_pformat             | 1.76 sec                                                               | 1.77 sec: 1.01x slower                                                           |
| many_optionals             | 1.09 ms                                                                | 1.10 ms: 1.01x slower                                                            |
| xml_etree_generate         | 95.3 ms                                                                | 96.0 ms: 1.01x slower                                                            |
| mako                       | 16.4 ms                                                                | 16.5 ms: 1.01x slower                                                            |
| json_loads                 | 31.6 us                                                                | 31.8 us: 1.01x slower                                                            |
| docutils                   | 2.85 sec                                                               | 2.87 sec: 1.01x slower                                                           |
| dulwich_log                | 68.9 ms                                                                | 69.5 ms: 1.01x slower                                                            |
| pyflate                    | 526 ms                                                                 | 531 ms: 1.01x slower                                                             |
| sqlglot_transpile          | 1.95 ms                                                                | 1.97 ms: 1.01x slower                                                            |
| sympy_integrate            | 23.8 ms                                                                | 24.0 ms: 1.01x slower                                                            |
| coroutines                 | 25.3 ms                                                                | 25.6 ms: 1.01x slower                                                            |
| pickle_pure_python         | 372 us                                                                 | 376 us: 1.01x slower                                                             |
| regex_v8                   | 24.9 ms                                                                | 25.1 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed    | 527 ms                                                                 | 534 ms: 1.01x slower                                                             |
| sqlalchemy_declarative     | 162 ms                                                                 | 164 ms: 1.01x slower                                                             |
| logging_simple             | 6.65 us                                                                | 6.74 us: 1.01x slower                                                            |
| go                         | 143 ms                                                                 | 145 ms: 1.01x slower                                                             |
| 2to3                       | 308 ms                                                                 | 313 ms: 1.01x slower                                                             |
| regex_compile              | 149 ms                                                                 | 151 ms: 1.01x slower                                                             |
| scimark_monte_carlo        | 86.3 ms                                                                | 87.5 ms: 1.01x slower                                                            |
| thrift                     | 946 us                                                                 | 959 us: 1.01x slower                                                             |
| scimark_sparse_mat_mult    | 6.16 ms                                                                | 6.25 ms: 1.01x slower                                                            |
| json_dumps                 | 12.6 ms                                                                | 12.8 ms: 1.02x slower                                                            |
| sqlglot_normalize          | 120 ms                                                                 | 121 ms: 1.02x slower                                                             |
| async_tree_cpu_io_mixed_tg | 482 ms                                                                 | 491 ms: 1.02x slower                                                             |
| sqlglot_parse              | 1.55 ms                                                                | 1.58 ms: 1.02x slower                                                            |
| async_tree_io              | 610 ms                                                                 | 621 ms: 1.02x slower                                                             |
| async_tree_memoization     | 368 ms                                                                 | 375 ms: 1.02x slower                                                             |
| comprehensions             | 20.6 us                                                                | 21.0 us: 1.02x slower                                                            |
| chaos                      | 74.0 ms                                                                | 75.5 ms: 1.02x slower                                                            |
| richards_super             | 63.2 ms                                                                | 64.6 ms: 1.02x slower                                                            |
| spectral_norm              | 115 ms                                                                 | 118 ms: 1.02x slower                                                             |
| async_tree_none            | 289 ms                                                                 | 296 ms: 1.02x slower                                                             |
| scimark_fft                | 420 ms                                                                 | 429 ms: 1.02x slower                                                             |
| html5lib                   | 69.4 ms                                                                | 71.0 ms: 1.02x slower                                                            |
| richards                   | 54.8 ms                                                                | 56.1 ms: 1.02x slower                                                            |
| unpickle_pure_python       | 255 us                                                                 | 261 us: 1.02x slower                                                             |
| async_tree_none_tg         | 246 ms                                                                 | 253 ms: 1.02x slower                                                             |
| genshi_text                | 28.1 ms                                                                | 28.8 ms: 1.03x slower                                                            |
| generators                 | 31.3 ms                                                                | 32.1 ms: 1.03x slower                                                            |
| raytrace                   | 355 ms                                                                 | 364 ms: 1.03x slower                                                             |
| subparsers                 | 24.3 ms                                                                | 25.0 ms: 1.03x slower                                                            |
| async_tree_memoization_tg  | 326 ms                                                                 | 335 ms: 1.03x slower                                                             |
| regex_dna                  | 222 ms                                                                 | 228 ms: 1.03x slower                                                             |
| async_tree_io_tg           | 557 ms                                                                 | 574 ms: 1.03x slower                                                             |
| deltablue                  | 4.74 ms                                                                | 4.89 ms: 1.03x slower                                                            |
| tomli_loads                | 2.36 sec                                                               | 2.43 sec: 1.03x slower                                                           |
| regex_effbot               | 3.35 ms                                                                | 3.50 ms: 1.05x slower                                                            |
| nbody                      | 135 ms                                                                 | 143 ms: 1.06x slower                                                             |
| pycparser                  | 1.18 sec                                                               | 1.25 sec: 1.06x slower                                                           |
| coverage                   | 106 ms                                                                 | 114 ms: 1.08x slower                                                             |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (22): meteor_contest, asyncio_websockets, json, deepcopy_memo, k_core, xml_etree_iterparse, async_generators, sqlalchemy_imperative, deepcopy_reduce, shortest_path, crypto_pyaes, django_template, bench_thread_pool, genshi_xml, bench_mp_pool, deepcopy, sympy_expand, sphinx, telco, typing_runtime_protocols, xml_etree_parse, pylint

- Geometric mean (including insignificant results): 1.010x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x
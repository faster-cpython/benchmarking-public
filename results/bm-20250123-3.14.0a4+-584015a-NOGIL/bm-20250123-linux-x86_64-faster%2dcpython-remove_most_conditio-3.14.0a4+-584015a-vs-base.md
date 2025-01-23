# Results vs. base

- fork: faster-cpython
- ref: remove_most_conditio
- machine: linux-x86_64
- commit hash: 584015a
- commit date: 2025-01-23
- overall geometric mean: 1.013x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                 | 313 ms: 1.02x slower                                                             |
| docutils       | 2.85 sec                                                               | 2.91 sec: 1.02x slower                                                           |
| html5lib       | 69.4 ms                                                                | 68.9 ms: 1.01x faster                                                            |
| sphinx         | 1.14 sec                                                               | 1.16 sec: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_generators           | 440 ms                                                                 | 438 ms: 1.00x faster                                                             |
| async_tree_cpu_io_mixed_tg | 482 ms                                                                 | 487 ms: 1.01x slower                                                             |
| async_tree_io              | 610 ms                                                                 | 616 ms: 1.01x slower                                                             |
| async_tree_memoization     | 368 ms                                                                 | 373 ms: 1.01x slower                                                             |
| async_tree_none_tg         | 246 ms                                                                 | 250 ms: 1.01x slower                                                             |
| async_tree_none            | 289 ms                                                                 | 294 ms: 1.02x slower                                                             |
| async_tree_io_tg           | 557 ms                                                                 | 568 ms: 1.02x slower                                                             |
| async_tree_memoization_tg  | 326 ms                                                                 | 334 ms: 1.02x slower                                                             |
| coroutines                 | 25.3 ms                                                                | 25.9 ms: 1.02x slower                                                            |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 181 ms                                                                 | 182 ms: 1.00x slower                                                             |
| float          | 78.0 ms                                                                | 78.6 ms: 1.01x slower                                                            |
| nbody          | 135 ms                                                                 | 137 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 149 ms                                                                 | 152 ms: 1.02x slower                                                             |
| regex_v8       | 24.9 ms                                                                | 25.4 ms: 1.02x slower                                                            |
| regex_dna      | 222 ms                                                                 | 227 ms: 1.02x slower                                                             |
| regex_effbot   | 3.35 ms                                                                | 3.48 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 31.6 us                                                                | 31.4 us: 1.00x faster                                                            |
| xml_etree_process    | 68.3 ms                                                                | 68.6 ms: 1.01x slower                                                            |
| xml_etree_generate   | 95.3 ms                                                                | 96.2 ms: 1.01x slower                                                            |
| xml_etree_iterparse  | 94.9 ms                                                                | 95.9 ms: 1.01x slower                                                            |
| json_dumps           | 12.6 ms                                                                | 12.8 ms: 1.01x slower                                                            |
| pickle_pure_python   | 372 us                                                                 | 377 us: 1.01x slower                                                             |
| xml_etree_parse      | 148 ms                                                                 | 150 ms: 1.01x slower                                                             |
| unpickle_pure_python | 255 us                                                                 | 261 us: 1.02x slower                                                             |
| tomli_loads          | 2.36 sec                                                               | 2.43 sec: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 9.36 ms                                                                | 9.37 ms: 1.00x slower                                                            |
| python_startup         | 15.0 ms                                                                | 15.1 ms: 1.00x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 60.9 ms                                                                | 62.0 ms: 1.02x slower                                                            |
| mako            | 16.4 ms                                                                | 16.7 ms: 1.02x slower                                                            |
| genshi_text     | 28.1 ms                                                                | 29.0 ms: 1.03x slower                                                            |
| django_template | 41.4 ms                                                                | 42.9 ms: 1.04x slower                                                            |
| Geometric mean  | (ref)                                                                  | 1.03x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mdp                        | 2.86 sec                                                               | 2.76 sec: 1.04x faster                                                           |
| pathlib                    | 16.6 ms                                                                | 16.4 ms: 1.01x faster                                                            |
| html5lib                   | 69.4 ms                                                                | 68.9 ms: 1.01x faster                                                            |
| k_core                     | 2.46 sec                                                               | 2.45 sec: 1.01x faster                                                           |
| bench_thread_pool          | 3.49 ms                                                                | 3.47 ms: 1.01x faster                                                            |
| shortest_path              | 572 ms                                                                 | 569 ms: 1.00x faster                                                             |
| json_loads                 | 31.6 us                                                                | 31.4 us: 1.00x faster                                                            |
| connected_components       | 531 ms                                                                 | 528 ms: 1.00x faster                                                             |
| create_gc_cycles           | 1.73 ms                                                                | 1.72 ms: 1.00x faster                                                            |
| async_generators           | 440 ms                                                                 | 438 ms: 1.00x faster                                                             |
| crypto_pyaes               | 90.9 ms                                                                | 90.7 ms: 1.00x faster                                                            |
| gc_traversal               | 4.44 ms                                                                | 4.44 ms: 1.00x faster                                                            |
| python_startup_no_site     | 9.36 ms                                                                | 9.37 ms: 1.00x slower                                                            |
| python_startup             | 15.0 ms                                                                | 15.1 ms: 1.00x slower                                                            |
| pidigits                   | 181 ms                                                                 | 182 ms: 1.00x slower                                                             |
| deepcopy                   | 314 us                                                                 | 315 us: 1.00x slower                                                             |
| xml_etree_process          | 68.3 ms                                                                | 68.6 ms: 1.01x slower                                                            |
| hexiom                     | 7.84 ms                                                                | 7.89 ms: 1.01x slower                                                            |
| dulwich_log                | 68.9 ms                                                                | 69.3 ms: 1.01x slower                                                            |
| float                      | 78.0 ms                                                                | 78.6 ms: 1.01x slower                                                            |
| coverage                   | 106 ms                                                                 | 107 ms: 1.01x slower                                                             |
| many_optionals             | 1.09 ms                                                                | 1.10 ms: 1.01x slower                                                            |
| deepcopy_memo              | 39.6 us                                                                | 40.0 us: 1.01x slower                                                            |
| xml_etree_generate         | 95.3 ms                                                                | 96.2 ms: 1.01x slower                                                            |
| nqueens                    | 100 ms                                                                 | 101 ms: 1.01x slower                                                             |
| sympy_str                  | 318 ms                                                                 | 321 ms: 1.01x slower                                                             |
| sqlalchemy_declarative     | 162 ms                                                                 | 164 ms: 1.01x slower                                                             |
| xml_etree_iterparse        | 94.9 ms                                                                | 95.9 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 482 ms                                                                 | 487 ms: 1.01x slower                                                             |
| async_tree_io              | 610 ms                                                                 | 616 ms: 1.01x slower                                                             |
| sympy_sum                  | 176 ms                                                                 | 178 ms: 1.01x slower                                                             |
| fannkuch                   | 516 ms                                                                 | 522 ms: 1.01x slower                                                             |
| scimark_monte_carlo        | 86.3 ms                                                                | 87.3 ms: 1.01x slower                                                            |
| raytrace                   | 355 ms                                                                 | 359 ms: 1.01x slower                                                             |
| json_dumps                 | 12.6 ms                                                                | 12.8 ms: 1.01x slower                                                            |
| sqlglot_transpile          | 1.95 ms                                                                | 1.98 ms: 1.01x slower                                                            |
| async_tree_memoization     | 368 ms                                                                 | 373 ms: 1.01x slower                                                             |
| async_tree_none_tg         | 246 ms                                                                 | 250 ms: 1.01x slower                                                             |
| pickle_pure_python         | 372 us                                                                 | 377 us: 1.01x slower                                                             |
| nbody                      | 135 ms                                                                 | 137 ms: 1.01x slower                                                             |
| xml_etree_parse            | 148 ms                                                                 | 150 ms: 1.01x slower                                                             |
| subparsers                 | 24.3 ms                                                                | 24.7 ms: 1.02x slower                                                            |
| async_tree_none            | 289 ms                                                                 | 294 ms: 1.02x slower                                                             |
| 2to3                       | 308 ms                                                                 | 313 ms: 1.02x slower                                                             |
| chaos                      | 74.0 ms                                                                | 75.2 ms: 1.02x slower                                                            |
| sqlglot_optimize           | 60.5 ms                                                                | 61.5 ms: 1.02x slower                                                            |
| scimark_sor                | 142 ms                                                                 | 144 ms: 1.02x slower                                                             |
| pprint_safe_repr           | 853 ms                                                                 | 867 ms: 1.02x slower                                                             |
| sympy_expand               | 529 ms                                                                 | 538 ms: 1.02x slower                                                             |
| logging_format             | 7.51 us                                                                | 7.64 us: 1.02x slower                                                            |
| sympy_integrate            | 23.8 ms                                                                | 24.2 ms: 1.02x slower                                                            |
| sqlglot_parse              | 1.55 ms                                                                | 1.58 ms: 1.02x slower                                                            |
| genshi_xml                 | 60.9 ms                                                                | 62.0 ms: 1.02x slower                                                            |
| async_tree_io_tg           | 557 ms                                                                 | 568 ms: 1.02x slower                                                             |
| mako                       | 16.4 ms                                                                | 16.7 ms: 1.02x slower                                                            |
| spectral_norm              | 115 ms                                                                 | 117 ms: 1.02x slower                                                             |
| sphinx                     | 1.14 sec                                                               | 1.16 sec: 1.02x slower                                                           |
| regex_compile              | 149 ms                                                                 | 152 ms: 1.02x slower                                                             |
| deltablue                  | 4.74 ms                                                                | 4.84 ms: 1.02x slower                                                            |
| go                         | 143 ms                                                                 | 146 ms: 1.02x slower                                                             |
| comprehensions             | 20.6 us                                                                | 21.0 us: 1.02x slower                                                            |
| generators                 | 31.3 ms                                                                | 32.0 ms: 1.02x slower                                                            |
| pyflate                    | 526 ms                                                                 | 537 ms: 1.02x slower                                                             |
| regex_v8                   | 24.9 ms                                                                | 25.4 ms: 1.02x slower                                                            |
| docutils                   | 2.85 sec                                                               | 2.91 sec: 1.02x slower                                                           |
| pprint_pformat             | 1.76 sec                                                               | 1.79 sec: 1.02x slower                                                           |
| async_tree_memoization_tg  | 326 ms                                                                 | 334 ms: 1.02x slower                                                             |
| regex_dna                  | 222 ms                                                                 | 227 ms: 1.02x slower                                                             |
| coroutines                 | 25.3 ms                                                                | 25.9 ms: 1.02x slower                                                            |
| typing_runtime_protocols   | 209 us                                                                 | 213 us: 1.02x slower                                                             |
| unpickle_pure_python       | 255 us                                                                 | 261 us: 1.02x slower                                                             |
| logging_simple             | 6.65 us                                                                | 6.83 us: 1.03x slower                                                            |
| sqlglot_normalize          | 120 ms                                                                 | 123 ms: 1.03x slower                                                             |
| tomli_loads                | 2.36 sec                                                               | 2.43 sec: 1.03x slower                                                           |
| genshi_text                | 28.1 ms                                                                | 29.0 ms: 1.03x slower                                                            |
| django_template            | 41.4 ms                                                                | 42.9 ms: 1.04x slower                                                            |
| regex_effbot               | 3.35 ms                                                                | 3.48 ms: 1.04x slower                                                            |
| pycparser                  | 1.18 sec                                                               | 1.23 sec: 1.04x slower                                                           |
| richards_super             | 63.2 ms                                                                | 71.8 ms: 1.14x slower                                                            |
| richards                   | 54.8 ms                                                                | 62.4 ms: 1.14x slower                                                            |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (16): sqlalchemy_imperative, json, sqlite_synth, scimark_sparse_mat_mult, telco, scimark_lu, thrift, asyncio_websockets, bpe_tokeniser, logging_silent, deepcopy_reduce, scimark_fft, meteor_contest, bench_mp_pool, async_tree_cpu_io_mixed, pylint

- Geometric mean (including insignificant results): 1.013x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x
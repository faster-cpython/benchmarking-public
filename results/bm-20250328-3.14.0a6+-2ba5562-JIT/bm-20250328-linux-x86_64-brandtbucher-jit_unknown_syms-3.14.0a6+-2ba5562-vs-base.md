# Results vs. base

- fork: brandtbucher
- ref: jit_unknown_syms
- machine: linux-x86_64
- commit hash: 2ba5562
- commit date: 2025-03-28
- overall geometric mean: 1.007x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 261 ms: 1.01x faster                                                     |
| html5lib       | 62.2 ms                                                                | 63.2 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 481 ms                                                                 | 473 ms: 1.02x faster                                                     |
| async_tree_cpu_io_mixed    | 497 ms                                                                 | 489 ms: 1.02x faster                                                     |
| async_generators           | 417 ms                                                                 | 412 ms: 1.01x faster                                                     |
| coroutines                 | 23.7 ms                                                                | 23.5 ms: 1.01x faster                                                    |
| async_tree_memoization     | 319 ms                                                                 | 316 ms: 1.01x faster                                                     |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_io, async_tree_none_tg, async_tree_io_tg, asyncio_websockets, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 23.9 ms                                                                | 23.4 ms: 1.02x faster                                                    |
| regex_compile  | 128 ms                                                                 | 127 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 11.8 ms                                                                | 11.4 ms: 1.04x faster                                                    |
| xml_etree_process    | 56.2 ms                                                                | 55.2 ms: 1.02x faster                                                    |
| xml_etree_generate   | 80.4 ms                                                                | 79.1 ms: 1.02x faster                                                    |
| json_loads           | 30.2 us                                                                | 29.7 us: 1.01x faster                                                    |
| pickle_pure_python   | 326 us                                                                 | 322 us: 1.01x faster                                                     |
| unpickle_pure_python | 216 us                                                                 | 213 us: 1.01x faster                                                     |
| xml_etree_parse      | 142 ms                                                                 | 141 ms: 1.01x faster                                                     |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (2): tomli_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.22 ms                                                                | 8.19 ms: 1.00x faster                                                    |
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                    |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 21.6 ms                                                                | 21.1 ms: 1.02x faster                                                    |
| mako            | 11.1 ms                                                                | 11.0 ms: 1.01x faster                                                    |
| django_template | 31.9 ms                                                                | 31.5 ms: 1.01x faster                                                    |
| genshi_xml      | 51.0 ms                                                                | 50.5 ms: 1.01x faster                                                    |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps                 | 11.8 ms                                                                | 11.4 ms: 1.04x faster                                                    |
| hexiom                     | 6.90 ms                                                                | 6.69 ms: 1.03x faster                                                    |
| deepcopy_memo              | 30.0 us                                                                | 29.3 us: 1.03x faster                                                    |
| scimark_lu                 | 121 ms                                                                 | 118 ms: 1.03x faster                                                     |
| scimark_monte_carlo        | 68.9 ms                                                                | 67.1 ms: 1.03x faster                                                    |
| pyflate                    | 447 ms                                                                 | 436 ms: 1.03x faster                                                     |
| genshi_text                | 21.6 ms                                                                | 21.1 ms: 1.02x faster                                                    |
| scimark_sor                | 121 ms                                                                 | 118 ms: 1.02x faster                                                     |
| regex_v8                   | 23.9 ms                                                                | 23.4 ms: 1.02x faster                                                    |
| logging_silent             | 100 ns                                                                 | 98.1 ns: 1.02x faster                                                    |
| richards_super             | 40.8 ms                                                                | 40.0 ms: 1.02x faster                                                    |
| xml_etree_process          | 56.2 ms                                                                | 55.2 ms: 1.02x faster                                                    |
| go                         | 129 ms                                                                 | 127 ms: 1.02x faster                                                     |
| mdp                        | 2.50 sec                                                               | 2.46 sec: 1.02x faster                                                   |
| async_tree_cpu_io_mixed_tg | 481 ms                                                                 | 473 ms: 1.02x faster                                                     |
| xml_etree_generate         | 80.4 ms                                                                | 79.1 ms: 1.02x faster                                                    |
| crypto_pyaes               | 79.0 ms                                                                | 77.7 ms: 1.02x faster                                                    |
| scimark_sparse_mat_mult    | 4.76 ms                                                                | 4.68 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed    | 497 ms                                                                 | 489 ms: 1.02x faster                                                     |
| pathlib                    | 16.7 ms                                                                | 16.5 ms: 1.02x faster                                                    |
| json_loads                 | 30.2 us                                                                | 29.7 us: 1.01x faster                                                    |
| sympy_sum                  | 152 ms                                                                 | 149 ms: 1.01x faster                                                     |
| mako                       | 11.1 ms                                                                | 11.0 ms: 1.01x faster                                                    |
| sqlalchemy_imperative      | 17.1 ms                                                                | 16.9 ms: 1.01x faster                                                    |
| sqlglot_v2_optimize        | 54.2 ms                                                                | 53.5 ms: 1.01x faster                                                    |
| sqlglot_v2_transpile       | 1.61 ms                                                                | 1.59 ms: 1.01x faster                                                    |
| django_template            | 31.9 ms                                                                | 31.5 ms: 1.01x faster                                                    |
| pickle_pure_python         | 326 us                                                                 | 322 us: 1.01x faster                                                     |
| thrift                     | 779 us                                                                 | 770 us: 1.01x faster                                                     |
| async_generators           | 417 ms                                                                 | 412 ms: 1.01x faster                                                     |
| sympy_expand               | 474 ms                                                                 | 469 ms: 1.01x faster                                                     |
| chaos                      | 60.2 ms                                                                | 59.5 ms: 1.01x faster                                                    |
| sqlglot_v2_normalize       | 109 ms                                                                 | 107 ms: 1.01x faster                                                     |
| spectral_norm              | 95.2 ms                                                                | 94.2 ms: 1.01x faster                                                    |
| richards                   | 35.6 ms                                                                | 35.2 ms: 1.01x faster                                                    |
| sympy_str                  | 274 ms                                                                 | 272 ms: 1.01x faster                                                     |
| unpickle_pure_python       | 216 us                                                                 | 213 us: 1.01x faster                                                     |
| sqlglot_v2_parse           | 1.30 ms                                                                | 1.28 ms: 1.01x faster                                                    |
| generators                 | 28.3 ms                                                                | 28.1 ms: 1.01x faster                                                    |
| sqlite_synth               | 2.75 us                                                                | 2.73 us: 1.01x faster                                                    |
| xml_etree_parse            | 142 ms                                                                 | 141 ms: 1.01x faster                                                     |
| json                       | 5.36 ms                                                                | 5.31 ms: 1.01x faster                                                    |
| raytrace                   | 270 ms                                                                 | 267 ms: 1.01x faster                                                     |
| coroutines                 | 23.7 ms                                                                | 23.5 ms: 1.01x faster                                                    |
| genshi_xml                 | 51.0 ms                                                                | 50.5 ms: 1.01x faster                                                    |
| async_tree_memoization     | 319 ms                                                                 | 316 ms: 1.01x faster                                                     |
| subparsers                 | 21.1 ms                                                                | 20.9 ms: 1.01x faster                                                    |
| regex_compile              | 128 ms                                                                 | 127 ms: 1.01x faster                                                     |
| shortest_path              | 498 ms                                                                 | 495 ms: 1.01x faster                                                     |
| 2to3                       | 263 ms                                                                 | 261 ms: 1.01x faster                                                     |
| meteor_contest             | 110 ms                                                                 | 109 ms: 1.01x faster                                                     |
| deltablue                  | 3.08 ms                                                                | 3.06 ms: 1.01x faster                                                    |
| sympy_integrate            | 20.3 ms                                                                | 20.2 ms: 1.01x faster                                                    |
| connected_components       | 459 ms                                                                 | 457 ms: 1.01x faster                                                     |
| sqlalchemy_declarative     | 133 ms                                                                 | 132 ms: 1.00x faster                                                     |
| python_startup_no_site     | 8.22 ms                                                                | 8.19 ms: 1.00x faster                                                    |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                    |
| bench_thread_pool          | 883 us                                                                 | 882 us: 1.00x faster                                                     |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x slower                                                     |
| dulwich_log                | 60.2 ms                                                                | 60.5 ms: 1.00x slower                                                    |
| create_gc_cycles           | 2.49 ms                                                                | 2.50 ms: 1.01x slower                                                    |
| logging_simple             | 5.59 us                                                                | 5.63 us: 1.01x slower                                                    |
| pprint_pformat             | 1.56 sec                                                               | 1.57 sec: 1.01x slower                                                   |
| logging_format             | 6.17 us                                                                | 6.26 us: 1.01x slower                                                    |
| html5lib                   | 62.2 ms                                                                | 63.2 ms: 1.02x slower                                                    |
| pprint_safe_repr           | 755 ms                                                                 | 770 ms: 1.02x slower                                                     |
| scimark_fft                | 308 ms                                                                 | 314 ms: 1.02x slower                                                     |
| gc_traversal               | 4.85 ms                                                                | 4.99 ms: 1.03x slower                                                    |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (28): pylint, async_tree_memoization_tg, telco, typing_runtime_protocols, pycparser, bench_mp_pool, deepcopy_reduce, coverage, comprehensions, tomli_loads, float, async_tree_io, async_tree_none_tg, xml_etree_iterparse, sphinx, async_tree_io_tg, bpe_tokeniser, docutils, regex_effbot, fannkuch, asyncio_websockets, deepcopy, regex_dna, nbody, many_optionals, async_tree_none, nqueens, k_core

- Geometric mean (including insignificant results): 1.007x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x
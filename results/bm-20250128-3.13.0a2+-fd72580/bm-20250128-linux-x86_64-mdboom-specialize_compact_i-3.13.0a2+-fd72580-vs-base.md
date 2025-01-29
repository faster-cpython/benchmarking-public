# Results vs. base

- fork: mdboom
- ref: specialize_compact_i
- machine: linux-x86_64
- commit hash: fd72580
- commit date: 2025-01-28
- overall geometric mean: 1.002x slower
- HPT reliability: 50.59%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| chameleon      | 6.94 ms                                                                | 7.02 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (5): 2to3, docutils, html5lib, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none        | 472 ms                                                                 | 463 ms: 1.02x faster                                                   |
| async_tree_none_tg     | 461 ms                                                                 | 455 ms: 1.01x faster                                                   |
| async_tree_memoization | 571 ms                                                                 | 565 ms: 1.01x faster                                                   |
| async_tree_io_tg       | 1.23 sec                                                               | 1.24 sec: 1.00x slower                                                 |
| coroutines             | 22.1 ms                                                                | 22.3 ms: 1.01x slower                                                  |
| async_generators       | 451 ms                                                                 | 456 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (5): async_tree_io, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 82.5 ms                                                                | 83.0 ms: 1.01x slower                                                  |
| pidigits       | 187 ms                                                                 | 222 ms: 1.18x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.06x slower                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 223 ms                                                                 | 216 ms: 1.03x faster                                                   |
| regex_compile  | 135 ms                                                                 | 134 ms: 1.01x faster                                                   |
| regex_effbot   | 3.58 ms                                                                | 3.70 ms: 1.03x slower                                                  |
| regex_v8       | 24.5 ms                                                                | 26.1 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|---------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads         | 2.20 sec                                                               | 2.12 sec: 1.04x faster                                                 |
| xml_etree_iterparse | 109 ms                                                                 | 107 ms: 1.02x faster                                                   |
| xml_etree_process   | 59.9 ms                                                                | 58.9 ms: 1.02x faster                                                  |
| xml_etree_generate  | 87.3 ms                                                                | 86.0 ms: 1.02x faster                                                  |
| xml_etree_parse     | 160 ms                                                                 | 158 ms: 1.01x faster                                                   |
| json_loads          | 28.1 us                                                                | 28.4 us: 1.01x slower                                                  |
| pickle_pure_python  | 303 us                                                                 | 309 us: 1.02x slower                                                   |
| Geometric mean      | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (2): json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.03 ms                                                                | 9.00 ms: 1.00x faster                                                  |
| python_startup         | 12.6 ms                                                                | 12.6 ms: 1.00x faster                                                  |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.9 ms                                                                | 50.8 ms: 1.02x faster                                                  |
| mako            | 11.1 ms                                                                | 11.0 ms: 1.01x faster                                                  |
| genshi_text     | 23.2 ms                                                                | 23.1 ms: 1.01x faster                                                  |
| django_template | 31.7 ms                                                                | 32.2 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark              | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| gc_traversal           | 5.01 ms                                                                | 4.72 ms: 1.06x faster                                                  |
| tomli_loads            | 2.20 sec                                                               | 2.12 sec: 1.04x faster                                                 |
| nqueens                | 81.4 ms                                                                | 79.0 ms: 1.03x faster                                                  |
| regex_dna              | 223 ms                                                                 | 216 ms: 1.03x faster                                                   |
| xml_etree_iterparse    | 109 ms                                                                 | 107 ms: 1.02x faster                                                   |
| create_gc_cycles       | 2.47 ms                                                                | 2.42 ms: 1.02x faster                                                  |
| genshi_xml             | 51.9 ms                                                                | 50.8 ms: 1.02x faster                                                  |
| generators             | 29.8 ms                                                                | 29.3 ms: 1.02x faster                                                  |
| async_tree_none        | 472 ms                                                                 | 463 ms: 1.02x faster                                                   |
| chaos                  | 60.7 ms                                                                | 59.5 ms: 1.02x faster                                                  |
| go                     | 141 ms                                                                 | 139 ms: 1.02x faster                                                   |
| xml_etree_process      | 59.9 ms                                                                | 58.9 ms: 1.02x faster                                                  |
| xml_etree_generate     | 87.3 ms                                                                | 86.0 ms: 1.02x faster                                                  |
| coverage               | 95.6 ms                                                                | 94.2 ms: 1.01x faster                                                  |
| mako                   | 11.1 ms                                                                | 11.0 ms: 1.01x faster                                                  |
| comprehensions         | 16.8 us                                                                | 16.6 us: 1.01x faster                                                  |
| async_tree_none_tg     | 461 ms                                                                 | 455 ms: 1.01x faster                                                   |
| async_tree_memoization | 571 ms                                                                 | 565 ms: 1.01x faster                                                   |
| shortest_path          | 488 ms                                                                 | 483 ms: 1.01x faster                                                   |
| bpe_tokeniser          | 5.03 sec                                                               | 4.97 sec: 1.01x faster                                                 |
| thrift                 | 802 us                                                                 | 794 us: 1.01x faster                                                   |
| hexiom                 | 6.20 ms                                                                | 6.15 ms: 1.01x faster                                                  |
| pathlib                | 18.6 ms                                                                | 18.4 ms: 1.01x faster                                                  |
| xml_etree_parse        | 160 ms                                                                 | 158 ms: 1.01x faster                                                   |
| regex_compile          | 135 ms                                                                 | 134 ms: 1.01x faster                                                   |
| spectral_norm          | 111 ms                                                                 | 110 ms: 1.01x faster                                                   |
| bench_thread_pool      | 846 us                                                                 | 840 us: 1.01x faster                                                   |
| genshi_text            | 23.2 ms                                                                | 23.1 ms: 1.01x faster                                                  |
| pyflate                | 460 ms                                                                 | 458 ms: 1.01x faster                                                   |
| python_startup_no_site | 9.03 ms                                                                | 9.00 ms: 1.00x faster                                                  |
| sqlglot_optimize       | 53.5 ms                                                                | 53.4 ms: 1.00x faster                                                  |
| python_startup         | 12.6 ms                                                                | 12.6 ms: 1.00x faster                                                  |
| sqlglot_normalize      | 106 ms                                                                 | 106 ms: 1.00x slower                                                   |
| async_tree_io_tg       | 1.23 sec                                                               | 1.24 sec: 1.00x slower                                                 |
| deepcopy               | 349 us                                                                 | 351 us: 1.00x slower                                                   |
| sqlite_synth           | 2.82 us                                                                | 2.83 us: 1.01x slower                                                  |
| meteor_contest         | 109 ms                                                                 | 110 ms: 1.01x slower                                                   |
| sympy_sum              | 147 ms                                                                 | 148 ms: 1.01x slower                                                   |
| float                  | 82.5 ms                                                                | 83.0 ms: 1.01x slower                                                  |
| json                   | 5.16 ms                                                                | 5.20 ms: 1.01x slower                                                  |
| coroutines             | 22.1 ms                                                                | 22.3 ms: 1.01x slower                                                  |
| richards               | 48.8 ms                                                                | 49.1 ms: 1.01x slower                                                  |
| json_loads             | 28.1 us                                                                | 28.4 us: 1.01x slower                                                  |
| logging_silent         | 105 ns                                                                 | 105 ns: 1.01x slower                                                   |
| chameleon              | 6.94 ms                                                                | 7.02 ms: 1.01x slower                                                  |
| logging_format         | 6.36 us                                                                | 6.43 us: 1.01x slower                                                  |
| async_generators       | 451 ms                                                                 | 456 ms: 1.01x slower                                                   |
| scimark_sor            | 122 ms                                                                 | 124 ms: 1.01x slower                                                   |
| deltablue              | 3.29 ms                                                                | 3.33 ms: 1.01x slower                                                  |
| deepcopy_reduce        | 3.12 us                                                                | 3.16 us: 1.01x slower                                                  |
| logging_simple         | 5.83 us                                                                | 5.91 us: 1.01x slower                                                  |
| raytrace               | 272 ms                                                                 | 276 ms: 1.01x slower                                                   |
| richards_super         | 54.4 ms                                                                | 55.3 ms: 1.02x slower                                                  |
| scimark_lu             | 114 ms                                                                 | 116 ms: 1.02x slower                                                   |
| django_template        | 31.7 ms                                                                | 32.2 ms: 1.02x slower                                                  |
| scimark_fft            | 367 ms                                                                 | 374 ms: 1.02x slower                                                   |
| sympy_expand           | 450 ms                                                                 | 457 ms: 1.02x slower                                                   |
| fannkuch               | 388 ms                                                                 | 395 ms: 1.02x slower                                                   |
| sympy_str              | 266 ms                                                                 | 271 ms: 1.02x slower                                                   |
| pickle_pure_python     | 303 us                                                                 | 309 us: 1.02x slower                                                   |
| regex_effbot           | 3.58 ms                                                                | 3.70 ms: 1.03x slower                                                  |
| pycparser              | 1.18 sec                                                               | 1.22 sec: 1.04x slower                                                 |
| crypto_pyaes           | 71.3 ms                                                                | 74.3 ms: 1.04x slower                                                  |
| mdp                    | 2.58 sec                                                               | 2.69 sec: 1.04x slower                                                 |
| regex_v8               | 24.5 ms                                                                | 26.1 ms: 1.07x slower                                                  |
| pidigits               | 187 ms                                                                 | 222 ms: 1.18x slower                                                   |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (33): connected_components, html5lib, gunicorn, scimark_monte_carlo, deepcopy_memo, pylint, bench_mp_pool, subparsers, sphinx, sqlglot_parse, async_tree_io, 2to3, scimark_sparse_mat_mult, typing_runtime_protocols, sqlglot_transpile, sympy_integrate, pprint_safe_repr, sqlalchemy_imperative, asyncio_websockets, docutils, k_core, sqlalchemy_declarative, many_optionals, json_dumps, tornado_http, nbody, telco, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, pprint_pformat, async_tree_cpu_io_mixed, dulwich_log, unpickle_pure_python

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 50.59% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x
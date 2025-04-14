# Results vs. base

- fork: brandtbucher
- ref: trace_generators
- machine: linux-x86_64
- commit hash: 983a1ff
- commit date: 2025-02-17
- overall geometric mean: 1.011x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-983a1ff |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 265 ms: 1.03x slower                                                     |
| html5lib       | 60.6 ms                                                                | 62.2 ms: 1.03x slower                                                    |
| sphinx         | 1.00 sec                                                               | 1.02 sec: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-983a1ff |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 323 ms                                                                 | 326 ms: 1.01x slower                                                     |
| coroutines                 | 23.4 ms                                                                | 23.6 ms: 1.01x slower                                                    |
| async_tree_none_tg         | 258 ms                                                                 | 261 ms: 1.01x slower                                                     |
| async_generators           | 403 ms                                                                 | 412 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed_tg | 482 ms                                                                 | 494 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed    | 489 ms                                                                 | 502 ms: 1.03x slower                                                     |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_none, asyncio_websockets, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-983a1ff |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                 | 186 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-983a1ff |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 24.0 ms                                                                | 24.1 ms: 1.00x slower                                                    |
| regex_dna      | 202 ms                                                                 | 203 ms: 1.01x slower                                                     |
| regex_effbot   | 3.01 ms                                                                | 3.04 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-983a1ff |
|---------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python  | 326 us                                                                 | 321 us: 1.02x faster                                                     |
| json_dumps          | 11.8 ms                                                                | 11.7 ms: 1.01x faster                                                    |
| xml_etree_process   | 56.0 ms                                                                | 56.5 ms: 1.01x slower                                                    |
| xml_etree_parse     | 138 ms                                                                 | 140 ms: 1.01x slower                                                     |
| xml_etree_iterparse | 96.2 ms                                                                | 98.3 ms: 1.02x slower                                                    |
| xml_etree_generate  | 78.2 ms                                                                | 80.0 ms: 1.02x slower                                                    |
| Geometric mean      | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (3): unpickle_pure_python, json_loads, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-983a1ff |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 12.9 ms                                                                | 12.9 ms: 1.00x slower                                                    |
| python_startup_no_site | 7.08 ms                                                                | 7.09 ms: 1.00x slower                                                    |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-983a1ff |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 9.92 ms                                                                | 10.3 ms: 1.04x slower                                                    |
| genshi_xml     | 48.8 ms                                                                | 52.9 ms: 1.08x slower                                                    |
| genshi_text    | 21.3 ms                                                                | 23.4 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.06x slower                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-983a1ff |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pyflate                    | 467 ms                                                                 | 432 ms: 1.08x faster                                                     |
| nqueens                    | 83.3 ms                                                                | 81.0 ms: 1.03x faster                                                    |
| deepcopy_reduce            | 2.70 us                                                                | 2.64 us: 1.02x faster                                                    |
| subparsers                 | 20.7 ms                                                                | 20.3 ms: 1.02x faster                                                    |
| pickle_pure_python         | 326 us                                                                 | 321 us: 1.02x faster                                                     |
| pycparser                  | 1.17 sec                                                               | 1.16 sec: 1.02x faster                                                   |
| pidigits                   | 188 ms                                                                 | 186 ms: 1.01x faster                                                     |
| json_dumps                 | 11.8 ms                                                                | 11.7 ms: 1.01x faster                                                    |
| many_optionals             | 954 us                                                                 | 946 us: 1.01x faster                                                     |
| logging_format             | 6.15 us                                                                | 6.10 us: 1.01x faster                                                    |
| deepcopy                   | 261 us                                                                 | 259 us: 1.01x faster                                                     |
| sqlite_synth               | 2.72 us                                                                | 2.70 us: 1.01x faster                                                    |
| fannkuch                   | 402 ms                                                                 | 399 ms: 1.01x faster                                                     |
| hexiom                     | 6.67 ms                                                                | 6.64 ms: 1.00x faster                                                    |
| python_startup             | 12.9 ms                                                                | 12.9 ms: 1.00x slower                                                    |
| python_startup_no_site     | 7.08 ms                                                                | 7.09 ms: 1.00x slower                                                    |
| create_gc_cycles           | 2.48 ms                                                                | 2.49 ms: 1.00x slower                                                    |
| sympy_str                  | 273 ms                                                                 | 274 ms: 1.00x slower                                                     |
| sympy_expand               | 466 ms                                                                 | 468 ms: 1.00x slower                                                     |
| regex_v8                   | 24.0 ms                                                                | 24.1 ms: 1.00x slower                                                    |
| chaos                      | 58.7 ms                                                                | 58.9 ms: 1.00x slower                                                    |
| sqlalchemy_declarative     | 130 ms                                                                 | 131 ms: 1.01x slower                                                     |
| regex_dna                  | 202 ms                                                                 | 203 ms: 1.01x slower                                                     |
| shortest_path              | 480 ms                                                                 | 483 ms: 1.01x slower                                                     |
| spectral_norm              | 94.6 ms                                                                | 95.3 ms: 1.01x slower                                                    |
| mdp                        | 2.48 sec                                                               | 2.50 sec: 1.01x slower                                                   |
| comprehensions             | 17.2 us                                                                | 17.4 us: 1.01x slower                                                    |
| go                         | 125 ms                                                                 | 126 ms: 1.01x slower                                                     |
| async_tree_memoization     | 323 ms                                                                 | 326 ms: 1.01x slower                                                     |
| deepcopy_memo              | 30.4 us                                                                | 30.7 us: 1.01x slower                                                    |
| xml_etree_process          | 56.0 ms                                                                | 56.5 ms: 1.01x slower                                                    |
| sqlglot_optimize           | 53.2 ms                                                                | 53.7 ms: 1.01x slower                                                    |
| regex_effbot               | 3.01 ms                                                                | 3.04 ms: 1.01x slower                                                    |
| coroutines                 | 23.4 ms                                                                | 23.6 ms: 1.01x slower                                                    |
| scimark_monte_carlo        | 66.4 ms                                                                | 67.1 ms: 1.01x slower                                                    |
| sympy_sum                  | 149 ms                                                                 | 151 ms: 1.01x slower                                                     |
| xml_etree_parse            | 138 ms                                                                 | 140 ms: 1.01x slower                                                     |
| connected_components       | 440 ms                                                                 | 445 ms: 1.01x slower                                                     |
| richards                   | 43.6 ms                                                                | 44.1 ms: 1.01x slower                                                    |
| scimark_sor                | 119 ms                                                                 | 121 ms: 1.01x slower                                                     |
| scimark_sparse_mat_mult    | 4.49 ms                                                                | 4.55 ms: 1.01x slower                                                    |
| async_tree_none_tg         | 258 ms                                                                 | 261 ms: 1.01x slower                                                     |
| raytrace                   | 272 ms                                                                 | 276 ms: 1.01x slower                                                     |
| bench_thread_pool          | 872 us                                                                 | 885 us: 1.01x slower                                                     |
| typing_runtime_protocols   | 162 us                                                                 | 164 us: 1.02x slower                                                     |
| sphinx                     | 1.00 sec                                                               | 1.02 sec: 1.02x slower                                                   |
| dulwich_log                | 66.5 ms                                                                | 67.8 ms: 1.02x slower                                                    |
| pathlib                    | 16.1 ms                                                                | 16.5 ms: 1.02x slower                                                    |
| scimark_lu                 | 116 ms                                                                 | 118 ms: 1.02x slower                                                     |
| async_generators           | 403 ms                                                                 | 412 ms: 1.02x slower                                                     |
| xml_etree_iterparse        | 96.2 ms                                                                | 98.3 ms: 1.02x slower                                                    |
| deltablue                  | 3.28 ms                                                                | 3.35 ms: 1.02x slower                                                    |
| xml_etree_generate         | 78.2 ms                                                                | 80.0 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed_tg | 482 ms                                                                 | 494 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed    | 489 ms                                                                 | 502 ms: 1.03x slower                                                     |
| sqlglot_normalize          | 105 ms                                                                 | 107 ms: 1.03x slower                                                     |
| html5lib                   | 60.6 ms                                                                | 62.2 ms: 1.03x slower                                                    |
| logging_silent             | 102 ns                                                                 | 104 ns: 1.03x slower                                                     |
| 2to3                       | 258 ms                                                                 | 265 ms: 1.03x slower                                                     |
| gc_traversal               | 4.80 ms                                                                | 4.96 ms: 1.03x slower                                                    |
| mako                       | 9.92 ms                                                                | 10.3 ms: 1.04x slower                                                    |
| coverage                   | 88.6 ms                                                                | 92.1 ms: 1.04x slower                                                    |
| genshi_xml                 | 48.8 ms                                                                | 52.9 ms: 1.08x slower                                                    |
| genshi_text                | 21.3 ms                                                                | 23.4 ms: 1.10x slower                                                    |
| generators                 | 27.7 ms                                                                | 41.9 ms: 1.51x slower                                                    |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (31): nbody, telco, k_core, async_tree_io_tg, pprint_safe_repr, json, async_tree_none, crypto_pyaes, sqlalchemy_imperative, sqlglot_transpile, bench_mp_pool, thrift, unpickle_pure_python, logging_simple, bpe_tokeniser, scimark_fft, docutils, sqlglot_parse, asyncio_websockets, meteor_contest, regex_compile, sympy_integrate, float, json_loads, richards_super, django_template, async_tree_memoization_tg, pprint_pformat, async_tree_io, tomli_loads, pylint

- Geometric mean (including insignificant results): 1.011x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x
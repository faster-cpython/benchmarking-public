# Results vs. base

- fork: brandtbucher
- ref: trace_generators
- machine: linux-x86_64
- commit hash: d740bda
- commit date: 2025-02-13
- overall geometric mean: 1.008x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 262 ms: 1.02x slower                                                     |
| html5lib       | 60.6 ms                                                                | 61.2 ms: 1.01x slower                                                    |
| sphinx         | 1.00 sec                                                               | 1.02 sec: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization | 323 ms                                                                 | 325 ms: 1.00x slower                                                     |
| async_generators       | 403 ms                                                                 | 416 ms: 1.03x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (9): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io_tg, asyncio_websockets, async_tree_none_tg, coroutines, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 70.5 ms                                                                | 69.4 ms: 1.02x faster                                                    |
| pidigits       | 188 ms                                                                 | 186 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.01 ms                                                                | 3.09 ms: 1.03x slower                                                    |
| regex_dna      | 202 ms                                                                 | 210 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                             |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|---------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 138 ms                                                                 | 137 ms: 1.01x faster                                                     |
| xml_etree_generate  | 78.2 ms                                                                | 78.7 ms: 1.01x slower                                                    |
| xml_etree_iterparse | 96.2 ms                                                                | 96.9 ms: 1.01x slower                                                    |
| tomli_loads         | 1.84 sec                                                               | 1.86 sec: 1.01x slower                                                   |
| json_loads          | 28.5 us                                                                | 28.8 us: 1.01x slower                                                    |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (4): pickle_pure_python, json_dumps, xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 7.08 ms                                                                | 7.06 ms: 1.00x faster                                                    |
| python_startup         | 12.9 ms                                                                | 12.9 ms: 1.00x faster                                                    |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 9.92 ms                                                                | 10.2 ms: 1.02x slower                                                    |
| genshi_xml     | 48.8 ms                                                                | 52.6 ms: 1.08x slower                                                    |
| genshi_text    | 21.3 ms                                                                | 23.1 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.05x slower                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark              | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pyflate                | 467 ms                                                                 | 444 ms: 1.05x faster                                                     |
| nqueens                | 83.3 ms                                                                | 80.4 ms: 1.04x faster                                                    |
| float                  | 70.5 ms                                                                | 69.4 ms: 1.02x faster                                                    |
| logging_format         | 6.15 us                                                                | 6.08 us: 1.01x faster                                                    |
| logging_simple         | 5.53 us                                                                | 5.47 us: 1.01x faster                                                    |
| pidigits               | 188 ms                                                                 | 186 ms: 1.01x faster                                                     |
| create_gc_cycles       | 2.48 ms                                                                | 2.46 ms: 1.01x faster                                                    |
| xml_etree_parse        | 138 ms                                                                 | 137 ms: 1.01x faster                                                     |
| hexiom                 | 6.67 ms                                                                | 6.64 ms: 1.00x faster                                                    |
| python_startup_no_site | 7.08 ms                                                                | 7.06 ms: 1.00x faster                                                    |
| python_startup         | 12.9 ms                                                                | 12.9 ms: 1.00x faster                                                    |
| sqlalchemy_declarative | 130 ms                                                                 | 130 ms: 1.00x slower                                                     |
| deepcopy_memo          | 30.4 us                                                                | 30.5 us: 1.00x slower                                                    |
| deepcopy               | 261 us                                                                 | 262 us: 1.00x slower                                                     |
| sqlglot_parse          | 1.29 ms                                                                | 1.30 ms: 1.00x slower                                                    |
| async_tree_memoization | 323 ms                                                                 | 325 ms: 1.00x slower                                                     |
| shortest_path          | 480 ms                                                                 | 482 ms: 1.00x slower                                                     |
| chaos                  | 58.7 ms                                                                | 59.0 ms: 1.01x slower                                                    |
| go                     | 125 ms                                                                 | 125 ms: 1.01x slower                                                     |
| xml_etree_generate     | 78.2 ms                                                                | 78.7 ms: 1.01x slower                                                    |
| raytrace               | 272 ms                                                                 | 274 ms: 1.01x slower                                                     |
| sqlglot_transpile      | 1.60 ms                                                                | 1.61 ms: 1.01x slower                                                    |
| comprehensions         | 17.2 us                                                                | 17.4 us: 1.01x slower                                                    |
| xml_etree_iterparse    | 96.2 ms                                                                | 96.9 ms: 1.01x slower                                                    |
| sqlglot_optimize       | 53.2 ms                                                                | 53.6 ms: 1.01x slower                                                    |
| richards_super         | 50.2 ms                                                                | 50.7 ms: 1.01x slower                                                    |
| telco                  | 7.72 ms                                                                | 7.79 ms: 1.01x slower                                                    |
| tomli_loads            | 1.84 sec                                                               | 1.86 sec: 1.01x slower                                                   |
| subparsers             | 20.7 ms                                                                | 20.9 ms: 1.01x slower                                                    |
| bench_thread_pool      | 872 us                                                                 | 882 us: 1.01x slower                                                     |
| json_loads             | 28.5 us                                                                | 28.8 us: 1.01x slower                                                    |
| html5lib               | 60.6 ms                                                                | 61.2 ms: 1.01x slower                                                    |
| thrift                 | 751 us                                                                 | 760 us: 1.01x slower                                                     |
| sphinx                 | 1.00 sec                                                               | 1.02 sec: 1.01x slower                                                   |
| scimark_monte_carlo    | 66.4 ms                                                                | 67.4 ms: 1.01x slower                                                    |
| richards               | 43.6 ms                                                                | 44.2 ms: 1.02x slower                                                    |
| coverage               | 88.6 ms                                                                | 90.1 ms: 1.02x slower                                                    |
| pprint_pformat         | 1.49 sec                                                               | 1.52 sec: 1.02x slower                                                   |
| pprint_safe_repr       | 727 ms                                                                 | 740 ms: 1.02x slower                                                     |
| deltablue              | 3.28 ms                                                                | 3.34 ms: 1.02x slower                                                    |
| 2to3                   | 258 ms                                                                 | 262 ms: 1.02x slower                                                     |
| dulwich_log            | 66.5 ms                                                                | 67.8 ms: 1.02x slower                                                    |
| pathlib                | 16.1 ms                                                                | 16.5 ms: 1.02x slower                                                    |
| sqlglot_normalize      | 105 ms                                                                 | 107 ms: 1.02x slower                                                     |
| spectral_norm          | 94.6 ms                                                                | 96.7 ms: 1.02x slower                                                    |
| logging_silent         | 102 ns                                                                 | 104 ns: 1.02x slower                                                     |
| mako                   | 9.92 ms                                                                | 10.2 ms: 1.02x slower                                                    |
| regex_effbot           | 3.01 ms                                                                | 3.09 ms: 1.03x slower                                                    |
| async_generators       | 403 ms                                                                 | 416 ms: 1.03x slower                                                     |
| gc_traversal           | 4.80 ms                                                                | 4.96 ms: 1.03x slower                                                    |
| regex_dna              | 202 ms                                                                 | 210 ms: 1.04x slower                                                     |
| genshi_xml             | 48.8 ms                                                                | 52.6 ms: 1.08x slower                                                    |
| genshi_text            | 21.3 ms                                                                | 23.1 ms: 1.09x slower                                                    |
| generators             | 27.7 ms                                                                | 34.9 ms: 1.26x slower                                                    |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (42): async_tree_memoization_tg, pickle_pure_python, scimark_fft, async_tree_cpu_io_mixed_tg, sympy_sum, sqlalchemy_imperative, sympy_str, deepcopy_reduce, json, async_tree_cpu_io_mixed, meteor_contest, regex_compile, async_tree_io_tg, many_optionals, asyncio_websockets, sympy_expand, connected_components, regex_v8, json_dumps, scimark_sparse_mat_mult, async_tree_none_tg, bench_mp_pool, coroutines, async_tree_none, mdp, sqlite_synth, sympy_integrate, xml_etree_process, docutils, scimark_lu, bpe_tokeniser, django_template, k_core, crypto_pyaes, fannkuch, unpickle_pure_python, pycparser, scimark_sor, typing_runtime_protocols, async_tree_io, nbody, pylint

- Geometric mean (including insignificant results): 1.008x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x
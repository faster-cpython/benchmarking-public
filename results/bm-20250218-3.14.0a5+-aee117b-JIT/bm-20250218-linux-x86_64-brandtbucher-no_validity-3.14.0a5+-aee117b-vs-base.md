# Results vs. base

- fork: brandtbucher
- ref: no_validity
- machine: linux-x86_64
- commit hash: aee117b
- commit date: 2025-02-18
- overall geometric mean: 1.002x faster
- HPT reliability: 99.59%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 257 ms: 1.00x faster                                                |
| html5lib       | 60.6 ms                                                                | 61.4 ms: 1.01x slower                                               |
| sphinx         | 1.00 sec                                                               | 1.01 sec: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization     | 323 ms                                                                 | 322 ms: 1.00x faster                                                |
| async_tree_cpu_io_mixed_tg | 482 ms                                                                 | 490 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed    | 489 ms                                                                 | 498 ms: 1.02x slower                                                |
| async_generators           | 403 ms                                                                 | 415 ms: 1.03x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_none_tg, async_tree_none, async_tree_io, async_tree_memoization_tg, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                 | 186 ms: 1.01x faster                                                |
| nbody          | 90.0 ms                                                                | 91.6 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 24.0 ms                                                                | 23.8 ms: 1.01x faster                                               |
| regex_compile  | 126 ms                                                                 | 125 ms: 1.01x faster                                                |
| regex_dna      | 202 ms                                                                 | 213 ms: 1.05x slower                                                |
| regex_effbot   | 3.01 ms                                                                | 3.26 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 205 us                                                                 | 200 us: 1.03x faster                                                |
| tomli_loads          | 1.84 sec                                                               | 1.80 sec: 1.02x faster                                              |
| xml_etree_process    | 56.0 ms                                                                | 55.4 ms: 1.01x faster                                               |
| xml_etree_generate   | 78.2 ms                                                                | 77.6 ms: 1.01x faster                                               |
| xml_etree_parse      | 138 ms                                                                 | 137 ms: 1.01x faster                                                |
| xml_etree_iterparse  | 96.2 ms                                                                | 96.4 ms: 1.00x slower                                               |
| json_dumps           | 11.8 ms                                                                | 11.9 ms: 1.01x slower                                               |
| json_loads           | 28.5 us                                                                | 28.7 us: 1.01x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 7.08 ms                                                                | 7.04 ms: 1.01x faster                                               |
| python_startup         | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                               |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 31.6 ms                                                                | 31.8 ms: 1.01x slower                                               |
| mako            | 9.92 ms                                                                | 10.2 ms: 1.03x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pycparser                  | 1.17 sec                                                               | 1.10 sec: 1.07x faster                                              |
| scimark_sparse_mat_mult    | 4.49 ms                                                                | 4.32 ms: 1.04x faster                                               |
| comprehensions             | 17.2 us                                                                | 16.7 us: 1.04x faster                                               |
| pprint_pformat             | 1.49 sec                                                               | 1.44 sec: 1.04x faster                                              |
| pprint_safe_repr           | 727 ms                                                                 | 705 ms: 1.03x faster                                                |
| unpickle_pure_python       | 205 us                                                                 | 200 us: 1.03x faster                                                |
| scimark_fft                | 313 ms                                                                 | 305 ms: 1.03x faster                                                |
| typing_runtime_protocols   | 162 us                                                                 | 158 us: 1.02x faster                                                |
| telco                      | 7.72 ms                                                                | 7.54 ms: 1.02x faster                                               |
| tomli_loads                | 1.84 sec                                                               | 1.80 sec: 1.02x faster                                              |
| hexiom                     | 6.67 ms                                                                | 6.53 ms: 1.02x faster                                               |
| fannkuch                   | 402 ms                                                                 | 393 ms: 1.02x faster                                                |
| connected_components       | 440 ms                                                                 | 432 ms: 1.02x faster                                                |
| shortest_path              | 480 ms                                                                 | 472 ms: 1.02x faster                                                |
| bpe_tokeniser              | 4.41 sec                                                               | 4.34 sec: 1.02x faster                                              |
| logging_simple             | 5.53 us                                                                | 5.45 us: 1.02x faster                                               |
| pyflate                    | 467 ms                                                                 | 460 ms: 1.02x faster                                                |
| meteor_contest             | 108 ms                                                                 | 107 ms: 1.01x faster                                                |
| logging_format             | 6.15 us                                                                | 6.08 us: 1.01x faster                                               |
| pidigits                   | 188 ms                                                                 | 186 ms: 1.01x faster                                                |
| xml_etree_process          | 56.0 ms                                                                | 55.4 ms: 1.01x faster                                               |
| json                       | 5.16 ms                                                                | 5.11 ms: 1.01x faster                                               |
| crypto_pyaes               | 71.4 ms                                                                | 70.8 ms: 1.01x faster                                               |
| scimark_lu                 | 116 ms                                                                 | 115 ms: 1.01x faster                                                |
| regex_v8                   | 24.0 ms                                                                | 23.8 ms: 1.01x faster                                               |
| sqlglot_transpile          | 1.60 ms                                                                | 1.59 ms: 1.01x faster                                               |
| sqlglot_parse              | 1.29 ms                                                                | 1.28 ms: 1.01x faster                                               |
| xml_etree_generate         | 78.2 ms                                                                | 77.6 ms: 1.01x faster                                               |
| xml_etree_parse            | 138 ms                                                                 | 137 ms: 1.01x faster                                                |
| dulwich_log                | 66.5 ms                                                                | 66.1 ms: 1.01x faster                                               |
| go                         | 125 ms                                                                 | 124 ms: 1.01x faster                                                |
| sqlalchemy_imperative      | 16.8 ms                                                                | 16.7 ms: 1.01x faster                                               |
| sympy_integrate            | 20.0 ms                                                                | 19.9 ms: 1.01x faster                                               |
| regex_compile              | 126 ms                                                                 | 125 ms: 1.01x faster                                                |
| python_startup_no_site     | 7.08 ms                                                                | 7.04 ms: 1.01x faster                                               |
| sympy_str                  | 273 ms                                                                 | 271 ms: 1.01x faster                                                |
| sqlglot_optimize           | 53.2 ms                                                                | 52.9 ms: 1.00x faster                                               |
| sqlalchemy_declarative     | 130 ms                                                                 | 129 ms: 1.00x faster                                                |
| async_tree_memoization     | 323 ms                                                                 | 322 ms: 1.00x faster                                                |
| python_startup             | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                               |
| 2to3                       | 258 ms                                                                 | 257 ms: 1.00x faster                                                |
| xml_etree_iterparse        | 96.2 ms                                                                | 96.4 ms: 1.00x slower                                               |
| deepcopy                   | 261 us                                                                 | 262 us: 1.00x slower                                                |
| generators                 | 27.7 ms                                                                | 27.9 ms: 1.01x slower                                               |
| raytrace                   | 272 ms                                                                 | 274 ms: 1.01x slower                                                |
| json_dumps                 | 11.8 ms                                                                | 11.9 ms: 1.01x slower                                               |
| django_template            | 31.6 ms                                                                | 31.8 ms: 1.01x slower                                               |
| json_loads                 | 28.5 us                                                                | 28.7 us: 1.01x slower                                               |
| sphinx                     | 1.00 sec                                                               | 1.01 sec: 1.01x slower                                              |
| mdp                        | 2.48 sec                                                               | 2.51 sec: 1.01x slower                                              |
| richards                   | 43.6 ms                                                                | 44.1 ms: 1.01x slower                                               |
| chaos                      | 58.7 ms                                                                | 59.5 ms: 1.01x slower                                               |
| deltablue                  | 3.28 ms                                                                | 3.32 ms: 1.01x slower                                               |
| html5lib                   | 60.6 ms                                                                | 61.4 ms: 1.01x slower                                               |
| gc_traversal               | 4.80 ms                                                                | 4.88 ms: 1.02x slower                                               |
| async_tree_cpu_io_mixed_tg | 482 ms                                                                 | 490 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed    | 489 ms                                                                 | 498 ms: 1.02x slower                                                |
| nbody                      | 90.0 ms                                                                | 91.6 ms: 1.02x slower                                               |
| coverage                   | 88.6 ms                                                                | 90.3 ms: 1.02x slower                                               |
| logging_silent             | 102 ns                                                                 | 103 ns: 1.02x slower                                                |
| mako                       | 9.92 ms                                                                | 10.2 ms: 1.03x slower                                               |
| spectral_norm              | 94.6 ms                                                                | 97.4 ms: 1.03x slower                                               |
| async_generators           | 403 ms                                                                 | 415 ms: 1.03x slower                                                |
| regex_dna                  | 202 ms                                                                 | 213 ms: 1.05x slower                                                |
| regex_effbot               | 3.01 ms                                                                | 3.26 ms: 1.08x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (31): float, nqueens, async_tree_io_tg, async_tree_none_tg, async_tree_none, async_tree_io, sqlglot_normalize, deepcopy_reduce, async_tree_memoization_tg, scimark_sor, pylint, genshi_text, pickle_pure_python, docutils, k_core, bench_mp_pool, coroutines, create_gc_cycles, thrift, bench_thread_pool, sympy_expand, many_optionals, genshi_xml, asyncio_websockets, sympy_sum, pathlib, deepcopy_memo, subparsers, scimark_monte_carlo, richards_super, sqlite_synth

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 99.59% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x
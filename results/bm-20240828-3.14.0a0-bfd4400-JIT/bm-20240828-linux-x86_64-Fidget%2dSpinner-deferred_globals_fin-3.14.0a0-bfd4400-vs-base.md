# Results vs. base

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-x86_64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.002x faster
- HPT reliability: 87.65%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 279 ms                                                                | 281 ms: 1.01x slower                                                            |
| html5lib       | 67.2 ms                                                               | 65.9 ms: 1.02x faster                                                           |
| tornado_http   | 93.4 ms                                                               | 93.0 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines      | 23.4 ms                                                               | 22.9 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                                          |
| async_tree_none | 323 ms                                                                | 328 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_io, async_generators, asyncio_tcp, async_tree_memoization, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.75 ms                                                               | 3.50 ms: 1.07x faster                                                           |
| regex_dna      | 221 ms                                                                | 217 ms: 1.02x faster                                                            |
| regex_compile  | 142 ms                                                                | 141 ms: 1.01x faster                                                            |
| regex_v8       | 24.5 ms                                                               | 24.4 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 212 us                                                                | 209 us: 1.02x faster                                                            |
| xml_etree_iterparse  | 98.4 ms                                                               | 98.8 ms: 1.00x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (7): json_dumps, pickle_pure_python, tomli_loads, xml_etree_process, json_loads, xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.12 ms                                                               | 7.15 ms: 1.00x slower                                                           |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 36.8 ms                                                               | 35.7 ms: 1.03x faster                                                           |
| genshi_text     | 26.6 ms                                                               | 26.0 ms: 1.03x faster                                                           |
| mako            | 9.98 ms                                                               | 9.85 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark              | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot           | 3.75 ms                                                               | 3.50 ms: 1.07x faster                                                           |
| pycparser              | 1.20 sec                                                              | 1.15 sec: 1.05x faster                                                          |
| spectral_norm          | 102 ms                                                                | 98.6 ms: 1.04x faster                                                           |
| django_template        | 36.8 ms                                                               | 35.7 ms: 1.03x faster                                                           |
| coverage               | 87.5 ms                                                               | 84.9 ms: 1.03x faster                                                           |
| logging_silent         | 101 ns                                                                | 98.7 ns: 1.03x faster                                                           |
| genshi_text            | 26.6 ms                                                               | 26.0 ms: 1.03x faster                                                           |
| html5lib               | 67.2 ms                                                               | 65.9 ms: 1.02x faster                                                           |
| coroutines             | 23.4 ms                                                               | 22.9 ms: 1.02x faster                                                           |
| regex_dna              | 221 ms                                                                | 217 ms: 1.02x faster                                                            |
| scimark_monte_carlo    | 63.6 ms                                                               | 62.4 ms: 1.02x faster                                                           |
| deepcopy_memo          | 27.0 us                                                               | 26.5 us: 1.02x faster                                                           |
| unpickle_pure_python   | 212 us                                                                | 209 us: 1.02x faster                                                            |
| mako                   | 9.98 ms                                                               | 9.85 ms: 1.01x faster                                                           |
| crypto_pyaes           | 66.4 ms                                                               | 65.5 ms: 1.01x faster                                                           |
| meteor_contest         | 107 ms                                                                | 106 ms: 1.01x faster                                                            |
| richards               | 39.4 ms                                                               | 39.0 ms: 1.01x faster                                                           |
| regex_compile          | 142 ms                                                                | 141 ms: 1.01x faster                                                            |
| richards_super         | 44.7 ms                                                               | 44.3 ms: 1.01x faster                                                           |
| hexiom                 | 6.81 ms                                                               | 6.76 ms: 1.01x faster                                                           |
| scimark_fft            | 308 ms                                                                | 306 ms: 1.01x faster                                                            |
| bpe_tokeniser          | 4.59 sec                                                              | 4.57 sec: 1.00x faster                                                          |
| tornado_http           | 93.4 ms                                                               | 93.0 ms: 1.00x faster                                                           |
| sqlglot_normalize      | 113 ms                                                                | 113 ms: 1.00x faster                                                            |
| regex_v8               | 24.5 ms                                                               | 24.4 ms: 1.00x faster                                                           |
| pidigits               | 185 ms                                                                | 186 ms: 1.00x slower                                                            |
| asyncio_tcp_ssl        | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                                          |
| sqlglot_optimize       | 57.8 ms                                                               | 57.9 ms: 1.00x slower                                                           |
| xml_etree_iterparse    | 98.4 ms                                                               | 98.8 ms: 1.00x slower                                                           |
| python_startup_no_site | 7.12 ms                                                               | 7.15 ms: 1.00x slower                                                           |
| gc_traversal           | 3.67 ms                                                               | 3.69 ms: 1.00x slower                                                           |
| create_gc_cycles       | 1.75 ms                                                               | 1.76 ms: 1.00x slower                                                           |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                           |
| 2to3                   | 279 ms                                                                | 281 ms: 1.01x slower                                                            |
| sympy_sum              | 175 ms                                                                | 176 ms: 1.01x slower                                                            |
| logging_simple         | 5.47 us                                                               | 5.51 us: 1.01x slower                                                           |
| generators             | 32.6 ms                                                               | 32.8 ms: 1.01x slower                                                           |
| pathlib                | 16.1 ms                                                               | 16.2 ms: 1.01x slower                                                           |
| json                   | 5.32 ms                                                               | 5.37 ms: 1.01x slower                                                           |
| async_tree_none        | 323 ms                                                                | 328 ms: 1.01x slower                                                            |
| sympy_str              | 301 ms                                                                | 305 ms: 1.01x slower                                                            |
| sympy_expand           | 506 ms                                                                | 513 ms: 1.01x slower                                                            |
| nqueens                | 85.2 ms                                                               | 86.6 ms: 1.02x slower                                                           |
| deepcopy               | 263 us                                                                | 268 us: 1.02x slower                                                            |
| fannkuch               | 369 ms                                                                | 377 ms: 1.02x slower                                                            |
| pyflate                | 445 ms                                                                | 456 ms: 1.02x slower                                                            |
| scimark_lu             | 109 ms                                                                | 112 ms: 1.03x slower                                                            |
| deepcopy_reduce        | 2.64 us                                                               | 2.77 us: 1.05x slower                                                           |
| mdp                    | 2.54 sec                                                              | 2.66 sec: 1.05x slower                                                          |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (40): pprint_safe_repr, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, thrift, docutils, genshi_xml, float, scimark_sor, json_dumps, asyncio_websockets, scimark_sparse_mat_mult, raytrace, async_tree_io, sqlglot_transpile, bench_thread_pool, bench_mp_pool, async_generators, pylint, chaos, sympy_integrate, nbody, pickle_pure_python, telco, asyncio_tcp, tomli_loads, deltablue, sqlglot_parse, comprehensions, go, logging_format, typing_runtime_protocols, xml_etree_process, pprint_pformat, json_loads, xml_etree_generate, async_tree_memoization, xml_etree_parse, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.002x faster
# HPT report

- Reliability score: 87.65% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x
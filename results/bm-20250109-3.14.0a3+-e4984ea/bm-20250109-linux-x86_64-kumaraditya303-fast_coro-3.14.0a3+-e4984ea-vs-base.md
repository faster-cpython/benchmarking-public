# Results vs. base

- fork: kumaraditya303
- ref: fast_coro
- machine: linux-x86_64
- commit hash: e4984ea
- commit date: 2025-01-09
- overall geometric mean: 1.001x slower
- HPT reliability: 77.73%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3+-7dc41ad | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 254 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): asyncio_websockets, coroutines, async_generators, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization_tg, async_tree_memoization, async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3+-7dc41ad | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 95.3 ms                                                                | 94.0 ms: 1.01x faster                                               |
| float          | 71.6 ms                                                                | 72.6 ms: 1.01x slower                                               |
| pidigits       | 186 ms                                                                 | 190 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3+-7dc41ad | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 25.6 ms                                                                | 25.5 ms: 1.01x faster                                               |
| regex_compile  | 127 ms                                                                 | 127 ms: 1.00x faster                                                |
| regex_effbot   | 3.32 ms                                                                | 3.34 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3+-7dc41ad | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|---------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_iterparse | 97.6 ms                                                                | 96.5 ms: 1.01x faster                                               |
| xml_etree_process   | 59.8 ms                                                                | 59.3 ms: 1.01x faster                                               |
| pickle_pure_python  | 323 us                                                                 | 322 us: 1.00x faster                                                |
| json_loads          | 26.4 us                                                                | 26.6 us: 1.01x slower                                               |
| tomli_loads         | 1.97 sec                                                               | 1.99 sec: 1.01x slower                                              |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (4): json_dumps, unpickle_pure_python, xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3+-7dc41ad | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                               |
| python_startup_no_site | 7.05 ms                                                                | 7.06 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3+-7dc41ad | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml     | 49.2 ms                                                                | 49.7 ms: 1.01x slower                                               |
| genshi_text    | 22.2 ms                                                                | 22.5 ms: 1.02x slower                                               |
| mako           | 11.5 ms                                                                | 11.6 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3+-7dc41ad | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| thrift                  | 786 us                                                                 | 767 us: 1.02x faster                                                |
| scimark_sparse_mat_mult | 4.90 ms                                                                | 4.80 ms: 1.02x faster                                               |
| logging_format          | 6.32 us                                                                | 6.20 us: 1.02x faster                                               |
| scimark_lu              | 117 ms                                                                 | 115 ms: 1.02x faster                                                |
| richards                | 45.0 ms                                                                | 44.3 ms: 1.02x faster                                               |
| richards_super          | 50.9 ms                                                                | 50.1 ms: 1.01x faster                                               |
| nbody                   | 95.3 ms                                                                | 94.0 ms: 1.01x faster                                               |
| bpe_tokeniser           | 4.59 sec                                                               | 4.52 sec: 1.01x faster                                              |
| subparsers              | 20.7 ms                                                                | 20.4 ms: 1.01x faster                                               |
| xml_etree_iterparse     | 97.6 ms                                                                | 96.5 ms: 1.01x faster                                               |
| shortest_path           | 478 ms                                                                 | 474 ms: 1.01x faster                                                |
| xml_etree_process       | 59.8 ms                                                                | 59.3 ms: 1.01x faster                                               |
| sqlglot_optimize        | 52.6 ms                                                                | 52.2 ms: 1.01x faster                                               |
| regex_v8                | 25.6 ms                                                                | 25.5 ms: 1.01x faster                                               |
| many_optionals          | 945 us                                                                 | 938 us: 1.01x faster                                                |
| mdp                     | 2.55 sec                                                               | 2.53 sec: 1.01x faster                                              |
| logging_simple          | 5.65 us                                                                | 5.62 us: 1.01x faster                                               |
| fannkuch                | 399 ms                                                                 | 397 ms: 1.00x faster                                                |
| pickle_pure_python      | 323 us                                                                 | 322 us: 1.00x faster                                                |
| deltablue               | 3.26 ms                                                                | 3.25 ms: 1.00x faster                                               |
| regex_compile           | 127 ms                                                                 | 127 ms: 1.00x faster                                                |
| sympy_integrate         | 19.8 ms                                                                | 19.7 ms: 1.00x faster                                               |
| python_startup          | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                               |
| 2to3                    | 254 ms                                                                 | 254 ms: 1.00x slower                                                |
| python_startup_no_site  | 7.05 ms                                                                | 7.06 ms: 1.00x slower                                               |
| regex_effbot            | 3.32 ms                                                                | 3.34 ms: 1.00x slower                                               |
| dulwich_log             | 63.5 ms                                                                | 63.8 ms: 1.00x slower                                               |
| chaos                   | 60.7 ms                                                                | 61.0 ms: 1.01x slower                                               |
| pprint_safe_repr        | 728 ms                                                                 | 732 ms: 1.01x slower                                                |
| deepcopy                | 259 us                                                                 | 261 us: 1.01x slower                                                |
| deepcopy_memo           | 30.4 us                                                                | 30.6 us: 1.01x slower                                               |
| json_loads              | 26.4 us                                                                | 26.6 us: 1.01x slower                                               |
| nqueens                 | 78.4 ms                                                                | 79.0 ms: 1.01x slower                                               |
| scimark_sor             | 121 ms                                                                 | 122 ms: 1.01x slower                                                |
| comprehensions          | 16.5 us                                                                | 16.7 us: 1.01x slower                                               |
| scimark_fft             | 351 ms                                                                 | 354 ms: 1.01x slower                                                |
| genshi_xml              | 49.2 ms                                                                | 49.7 ms: 1.01x slower                                               |
| tomli_loads             | 1.97 sec                                                               | 1.99 sec: 1.01x slower                                              |
| logging_silent          | 105 ns                                                                 | 106 ns: 1.01x slower                                                |
| sqlite_synth            | 2.81 us                                                                | 2.84 us: 1.01x slower                                               |
| hexiom                  | 6.14 ms                                                                | 6.22 ms: 1.01x slower                                               |
| float                   | 71.6 ms                                                                | 72.6 ms: 1.01x slower                                               |
| sqlglot_transpile       | 1.56 ms                                                                | 1.58 ms: 1.01x slower                                               |
| genshi_text             | 22.2 ms                                                                | 22.5 ms: 1.02x slower                                               |
| json                    | 4.88 ms                                                                | 4.95 ms: 1.02x slower                                               |
| mako                    | 11.5 ms                                                                | 11.6 ms: 1.02x slower                                               |
| telco                   | 7.74 ms                                                                | 7.87 ms: 1.02x slower                                               |
| gc_traversal            | 4.92 ms                                                                | 5.02 ms: 1.02x slower                                               |
| sqlglot_parse           | 1.25 ms                                                                | 1.27 ms: 1.02x slower                                               |
| pidigits                | 186 ms                                                                 | 190 ms: 1.02x slower                                                |
| crypto_pyaes            | 70.2 ms                                                                | 71.9 ms: 1.02x slower                                               |
| pathlib                 | 15.9 ms                                                                | 16.3 ms: 1.02x slower                                               |
| deepcopy_reduce         | 2.63 us                                                                | 2.71 us: 1.03x slower                                               |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (43): raytrace, regex_dna, sphinx, connected_components, sqlglot_normalize, pylint, sqlalchemy_imperative, sympy_expand, asyncio_websockets, generators, pycparser, docutils, scimark_monte_carlo, json_dumps, coroutines, pyflate, meteor_contest, async_generators, bench_thread_pool, sympy_sum, pprint_pformat, unpickle_pure_python, async_tree_io_tg, sqlalchemy_declarative, bench_mp_pool, create_gc_cycles, async_tree_cpu_io_mixed_tg, typing_runtime_protocols, xml_etree_generate, django_template, xml_etree_parse, async_tree_cpu_io_mixed, go, coverage, sympy_str, k_core, async_tree_io, spectral_norm, async_tree_memoization_tg, html5lib, async_tree_memoization, async_tree_none_tg, async_tree_none

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 77.73% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x
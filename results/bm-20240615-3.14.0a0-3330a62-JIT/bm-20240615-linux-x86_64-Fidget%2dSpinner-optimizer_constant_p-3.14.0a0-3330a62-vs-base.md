# Results vs. base

- fork: Fidget-Spinner
- ref: optimizer_constant_p
- machine: linux-x86_64
- commit hash: 3330a62
- commit date: 2024-06-15
- overall geometric mean: 1.01x faster
- HPT reliability: 85.04%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240615-linux-x86_64-python-99d62f902e43c08ebec5-3.14.0a0-99d62f9 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 2.95 sec                                                              | 2.92 sec: 1.01x faster                                                          |
| tornado_http   | 97.5 ms                                                               | 96.2 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240615-linux-x86_64-python-99d62f902e43c08ebec5-3.14.0a0-99d62f9 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg | 1.01 sec                                                              | 1.02 sec: 1.01x slower                                                          |
| Geometric mean   | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg, async_tree_none, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240615-linux-x86_64-python-99d62f902e43c08ebec5-3.14.0a0-99d62f9 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 80.9 ms                                                               | 80.4 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240615-linux-x86_64-python-99d62f902e43c08ebec5-3.14.0a0-99d62f9 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                               | 23.7 ms: 1.13x faster                                                           |
| regex_effbot   | 3.89 ms                                                               | 3.59 ms: 1.08x faster                                                           |
| regex_dna      | 230 ms                                                                | 226 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240615-linux-x86_64-python-99d62f902e43c08ebec5-3.14.0a0-99d62f9 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle             | 17.1 us                                                               | 15.1 us: 1.14x faster                                                           |
| pickle_list          | 5.34 us                                                               | 5.19 us: 1.03x faster                                                           |
| unpickle_list        | 5.39 us                                                               | 5.25 us: 1.03x faster                                                           |
| pickle_dict          | 36.2 us                                                               | 35.4 us: 1.02x faster                                                           |
| json_dumps           | 10.6 ms                                                               | 10.5 ms: 1.02x faster                                                           |
| pickle_pure_python   | 299 us                                                                | 295 us: 1.01x faster                                                            |
| unpickle_pure_python | 223 us                                                                | 221 us: 1.01x faster                                                            |
| xml_etree_generate   | 83.0 ms                                                               | 82.5 ms: 1.01x faster                                                           |
| json_loads           | 28.8 us                                                               | 28.9 us: 1.00x slower                                                           |
| pickle               | 12.1 us                                                               | 12.2 us: 1.00x slower                                                           |
| xml_etree_parse      | 148 ms                                                                | 152 ms: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                                 | 1.02x faster                                                                    |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240615-linux-x86_64-python-99d62f902e43c08ebec5-3.14.0a0-99d62f9 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 11.3 ms                                                               | 11.2 ms: 1.00x faster                                                           |
| python_startup_no_site | 7.66 ms                                                               | 7.65 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240615-linux-x86_64-python-99d62f902e43c08ebec5-3.14.0a0-99d62f9 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 9.85 ms                                                               | 10.0 ms: 1.02x slower                                                           |
| genshi_xml     | 57.2 ms                                                               | 58.8 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark              | bm-20240615-linux-x86_64-python-99d62f902e43c08ebec5-3.14.0a0-99d62f9 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle               | 17.1 us                                                               | 15.1 us: 1.14x faster                                                           |
| regex_v8               | 26.9 ms                                                               | 23.7 ms: 1.13x faster                                                           |
| regex_effbot           | 3.89 ms                                                               | 3.59 ms: 1.08x faster                                                           |
| pyflate                | 456 ms                                                                | 437 ms: 1.04x faster                                                            |
| spectral_norm          | 107 ms                                                                | 104 ms: 1.03x faster                                                            |
| pickle_list            | 5.34 us                                                               | 5.19 us: 1.03x faster                                                           |
| unpickle_list          | 5.39 us                                                               | 5.25 us: 1.03x faster                                                           |
| deepcopy               | 279 us                                                                | 272 us: 1.03x faster                                                            |
| dulwich_log            | 70.4 ms                                                               | 68.7 ms: 1.02x faster                                                           |
| pickle_dict            | 36.2 us                                                               | 35.4 us: 1.02x faster                                                           |
| deepcopy_reduce        | 2.79 us                                                               | 2.74 us: 1.02x faster                                                           |
| regex_dna              | 230 ms                                                                | 226 ms: 1.02x faster                                                            |
| meteor_contest         | 109 ms                                                                | 107 ms: 1.02x faster                                                            |
| json_dumps             | 10.6 ms                                                               | 10.5 ms: 1.02x faster                                                           |
| deltablue              | 3.66 ms                                                               | 3.61 ms: 1.01x faster                                                           |
| pickle_pure_python     | 299 us                                                                | 295 us: 1.01x faster                                                            |
| scimark_sor            | 135 ms                                                                | 134 ms: 1.01x faster                                                            |
| tornado_http           | 97.5 ms                                                               | 96.2 ms: 1.01x faster                                                           |
| logging_simple         | 5.71 us                                                               | 5.63 us: 1.01x faster                                                           |
| docutils               | 2.95 sec                                                              | 2.92 sec: 1.01x faster                                                          |
| deepcopy_memo          | 29.2 us                                                               | 28.9 us: 1.01x faster                                                           |
| unpickle_pure_python   | 223 us                                                                | 221 us: 1.01x faster                                                            |
| bpe_tokeniser          | 4.92 sec                                                              | 4.87 sec: 1.01x faster                                                          |
| raytrace               | 278 ms                                                                | 276 ms: 1.01x faster                                                            |
| mdp                    | 2.60 sec                                                              | 2.58 sec: 1.01x faster                                                          |
| hexiom                 | 6.68 ms                                                               | 6.63 ms: 1.01x faster                                                           |
| sympy_integrate        | 22.5 ms                                                               | 22.4 ms: 1.01x faster                                                           |
| sqlite_synth           | 2.88 us                                                               | 2.86 us: 1.01x faster                                                           |
| sympy_sum              | 171 ms                                                                | 170 ms: 1.01x faster                                                            |
| coverage               | 95.7 ms                                                               | 95.0 ms: 1.01x faster                                                           |
| nbody                  | 80.9 ms                                                               | 80.4 ms: 1.01x faster                                                           |
| xml_etree_generate     | 83.0 ms                                                               | 82.5 ms: 1.01x faster                                                           |
| logging_silent         | 107 ns                                                                | 107 ns: 1.01x faster                                                            |
| go                     | 148 ms                                                                | 147 ms: 1.01x faster                                                            |
| sqlglot_normalize      | 115 ms                                                                | 114 ms: 1.01x faster                                                            |
| sympy_str              | 302 ms                                                                | 300 ms: 1.01x faster                                                            |
| scimark_fft            | 316 ms                                                                | 315 ms: 1.01x faster                                                            |
| python_startup         | 11.3 ms                                                               | 11.2 ms: 1.00x faster                                                           |
| sympy_expand           | 511 ms                                                                | 509 ms: 1.00x faster                                                            |
| bench_thread_pool      | 876 us                                                                | 873 us: 1.00x faster                                                            |
| python_startup_no_site | 7.66 ms                                                               | 7.65 ms: 1.00x faster                                                           |
| generators             | 30.2 ms                                                               | 30.2 ms: 1.00x slower                                                           |
| json_loads             | 28.8 us                                                               | 28.9 us: 1.00x slower                                                           |
| pickle                 | 12.1 us                                                               | 12.2 us: 1.00x slower                                                           |
| asyncio_tcp_ssl        | 1.85 sec                                                              | 1.86 sec: 1.00x slower                                                          |
| async_generators       | 467 ms                                                                | 469 ms: 1.01x slower                                                            |
| comprehensions         | 16.6 us                                                               | 16.6 us: 1.01x slower                                                           |
| sqlglot_transpile      | 1.63 ms                                                               | 1.64 ms: 1.01x slower                                                           |
| asyncio_tcp            | 517 ms                                                                | 520 ms: 1.01x slower                                                            |
| crypto_pyaes           | 67.7 ms                                                               | 68.2 ms: 1.01x slower                                                           |
| sqlglot_parse          | 1.31 ms                                                               | 1.32 ms: 1.01x slower                                                           |
| async_tree_io_tg       | 1.01 sec                                                              | 1.02 sec: 1.01x slower                                                          |
| scimark_lu             | 124 ms                                                                | 126 ms: 1.01x slower                                                            |
| richards               | 42.2 ms                                                               | 42.9 ms: 1.02x slower                                                           |
| pathlib                | 16.2 ms                                                               | 16.5 ms: 1.02x slower                                                           |
| mako                   | 9.85 ms                                                               | 10.0 ms: 1.02x slower                                                           |
| xml_etree_parse        | 148 ms                                                                | 152 ms: 1.02x slower                                                            |
| pycparser              | 1.17 sec                                                              | 1.20 sec: 1.02x slower                                                          |
| genshi_xml             | 57.2 ms                                                               | 58.8 ms: 1.03x slower                                                           |
| gc_traversal           | 3.71 ms                                                               | 3.90 ms: 1.05x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (37): fannkuch, scimark_sparse_mat_mult, chaos, nqueens, telco, xml_etree_process, async_tree_cpu_io_mixed_tg, pylint, async_tree_cpu_io_mixed, regex_compile, sqlglot_optimize, asyncio_websockets, pprint_pformat, richards_super, bench_mp_pool, 2to3, xml_etree_iterparse, genshi_text, float, pidigits, logging_format, html5lib, coroutines, create_gc_cycles, scimark_monte_carlo, django_template, thrift, tomli_loads, pprint_safe_repr, async_tree_memoization, async_tree_none_tg, typing_runtime_protocols, dask, async_tree_none, json, async_tree_memoization_tg, async_tree_io

# HPT report

- Reliability score: 85.04% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x
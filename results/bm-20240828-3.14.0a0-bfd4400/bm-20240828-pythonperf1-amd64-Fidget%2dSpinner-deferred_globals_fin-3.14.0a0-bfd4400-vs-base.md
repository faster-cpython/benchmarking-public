# Results vs. base

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: windows-amd64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.00x faster
- HPT reliability: 99.39%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| docutils       | 1.75 sec                                                                   | 1.74 sec: 1.01x faster                                                               |
| html5lib       | 42.0 ms                                                                    | 41.4 ms: 1.02x faster                                                                |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_generators | 247 ms                                                                     | 250 ms: 1.01x slower                                                                 |
| coroutines       | 14.1 ms                                                                    | 14.2 ms: 1.01x slower                                                                |
| Geometric mean   | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg, async_tree_none, async_tree_io_tg, asyncio_tcp, async_tree_io, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 151 ms                                                                     | 152 ms: 1.01x slower                                                                 |
| nbody          | 82.3 ms                                                                    | 83.5 ms: 1.01x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 16.5 ms                                                                    | 14.7 ms: 1.12x faster                                                                |
| regex_dna      | 118 ms                                                                     | 114 ms: 1.03x faster                                                                 |
| regex_compile  | 91.7 ms                                                                    | 90.4 ms: 1.01x faster                                                                |
| regex_effbot   | 1.56 ms                                                                    | 1.55 ms: 1.01x faster                                                                |
| Geometric mean | (ref)                                                                      | 1.04x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| unpickle_pure_python | 148 us                                                                     | 146 us: 1.01x faster                                                                 |
| json_loads           | 14.2 us                                                                    | 14.0 us: 1.01x faster                                                                |
| xml_etree_process    | 41.2 ms                                                                    | 40.7 ms: 1.01x faster                                                                |
| json_dumps           | 6.22 ms                                                                    | 6.16 ms: 1.01x faster                                                                |
| tomli_loads          | 1.58 sec                                                                   | 1.57 sec: 1.01x faster                                                               |
| xml_etree_parse      | 94.6 ms                                                                    | 95.9 ms: 1.01x slower                                                                |
| Geometric mean       | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text    | 17.5 ms                                                                    | 17.0 ms: 1.03x faster                                                                |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (3): genshi_xml, mako, django_template

All benchmarks:
===============

| Benchmark               | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8                | 16.5 ms                                                                    | 14.7 ms: 1.12x faster                                                                |
| scimark_lu              | 65.5 ms                                                                    | 61.6 ms: 1.06x faster                                                                |
| regex_dna               | 118 ms                                                                     | 114 ms: 1.03x faster                                                                 |
| hexiom                  | 4.46 ms                                                                    | 4.33 ms: 1.03x faster                                                                |
| genshi_text             | 17.5 ms                                                                    | 17.0 ms: 1.03x faster                                                                |
| scimark_monte_carlo     | 50.3 ms                                                                    | 49.0 ms: 1.03x faster                                                                |
| pyflate                 | 324 ms                                                                     | 316 ms: 1.02x faster                                                                 |
| scimark_sor             | 92.2 ms                                                                    | 90.2 ms: 1.02x faster                                                                |
| generators              | 21.2 ms                                                                    | 20.8 ms: 1.02x faster                                                                |
| deepcopy_memo           | 20.4 us                                                                    | 20.0 us: 1.02x faster                                                                |
| pprint_pformat          | 1.14 sec                                                                   | 1.13 sec: 1.02x faster                                                               |
| logging_silent          | 63.7 ns                                                                    | 62.7 ns: 1.02x faster                                                                |
| fannkuch                | 294 ms                                                                     | 290 ms: 1.02x faster                                                                 |
| html5lib                | 42.0 ms                                                                    | 41.4 ms: 1.02x faster                                                                |
| unpickle_pure_python    | 148 us                                                                     | 146 us: 1.01x faster                                                                 |
| json_loads              | 14.2 us                                                                    | 14.0 us: 1.01x faster                                                                |
| regex_compile           | 91.7 ms                                                                    | 90.4 ms: 1.01x faster                                                                |
| sympy_integrate         | 13.4 ms                                                                    | 13.2 ms: 1.01x faster                                                                |
| sympy_str               | 180 ms                                                                     | 178 ms: 1.01x faster                                                                 |
| sympy_sum               | 92.3 ms                                                                    | 91.2 ms: 1.01x faster                                                                |
| xml_etree_process       | 41.2 ms                                                                    | 40.7 ms: 1.01x faster                                                                |
| sympy_expand            | 312 ms                                                                     | 308 ms: 1.01x faster                                                                 |
| json_dumps              | 6.22 ms                                                                    | 6.16 ms: 1.01x faster                                                                |
| scimark_fft             | 205 ms                                                                     | 203 ms: 1.01x faster                                                                 |
| sqlglot_transpile       | 1.11 ms                                                                    | 1.10 ms: 1.01x faster                                                                |
| bench_mp_pool           | 68.8 ms                                                                    | 68.2 ms: 1.01x faster                                                                |
| regex_effbot            | 1.56 ms                                                                    | 1.55 ms: 1.01x faster                                                                |
| chaos                   | 43.7 ms                                                                    | 43.3 ms: 1.01x faster                                                                |
| docutils                | 1.75 sec                                                                   | 1.74 sec: 1.01x faster                                                               |
| sqlglot_normalize       | 193 ms                                                                     | 192 ms: 1.01x faster                                                                 |
| scimark_sparse_mat_mult | 2.68 ms                                                                    | 2.66 ms: 1.01x faster                                                                |
| tomli_loads             | 1.58 sec                                                                   | 1.57 sec: 1.01x faster                                                               |
| raytrace                | 195 ms                                                                     | 194 ms: 1.01x faster                                                                 |
| pprint_safe_repr        | 549 ms                                                                     | 551 ms: 1.00x slower                                                                 |
| gc_traversal            | 1.57 ms                                                                    | 1.57 ms: 1.01x slower                                                                |
| pidigits                | 151 ms                                                                     | 152 ms: 1.01x slower                                                                 |
| go                      | 98.5 ms                                                                    | 99.2 ms: 1.01x slower                                                                |
| mdp                     | 1.49 sec                                                                   | 1.50 sec: 1.01x slower                                                               |
| logging_format          | 6.72 us                                                                    | 6.77 us: 1.01x slower                                                                |
| richards                | 32.3 ms                                                                    | 32.5 ms: 1.01x slower                                                                |
| pathlib                 | 78.3 ms                                                                    | 78.9 ms: 1.01x slower                                                                |
| logging_simple          | 6.29 us                                                                    | 6.34 us: 1.01x slower                                                                |
| richards_super          | 36.2 ms                                                                    | 36.5 ms: 1.01x slower                                                                |
| async_generators        | 247 ms                                                                     | 250 ms: 1.01x slower                                                                 |
| nqueens                 | 62.4 ms                                                                    | 63.1 ms: 1.01x slower                                                                |
| spectral_norm           | 67.6 ms                                                                    | 68.3 ms: 1.01x slower                                                                |
| coroutines              | 14.1 ms                                                                    | 14.2 ms: 1.01x slower                                                                |
| xml_etree_parse         | 94.6 ms                                                                    | 95.9 ms: 1.01x slower                                                                |
| nbody                   | 82.3 ms                                                                    | 83.5 ms: 1.01x slower                                                                |
| meteor_contest          | 77.2 ms                                                                    | 78.5 ms: 1.02x slower                                                                |
| telco                   | 4.87 ms                                                                    | 5.02 ms: 1.03x slower                                                                |
| json                    | 2.98 ms                                                                    | 3.10 ms: 1.04x slower                                                                |
| Geometric mean          | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (36): genshi_xml, async_tree_cpu_io_mixed, pylint, mako, async_tree_cpu_io_mixed_tg, async_tree_memoization, thrift, async_tree_none_tg, tornado_http, pycparser, dulwich_log, python_startup, 2to3, async_tree_memoization_tg, async_tree_none, async_tree_io_tg, typing_runtime_protocols, deltablue, comprehensions, python_startup_no_site, deepcopy, bench_thread_pool, django_template, xml_etree_iterparse, create_gc_cycles, coverage, asyncio_tcp, xml_etree_generate, deepcopy_reduce, sqlglot_parse, pickle_pure_python, sqlglot_optimize, crypto_pyaes, float, async_tree_io, asyncio_tcp_ssl

# HPT report

- Reliability score: 99.39% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
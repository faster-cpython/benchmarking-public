# Results vs. base

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: windows-amd64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.00x faster
- HPT reliability: 99.60%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| docutils       | 1.93 sec                                                                   | 1.91 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                                 |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_generators | 261 ms                                                                     | 257 ms: 1.02x faster                                                         |
| coroutines       | 14.1 ms                                                                    | 14.0 ms: 1.01x faster                                                        |
| asyncio_tcp      | 542 ms                                                                     | 611 ms: 1.13x slower                                                         |
| Geometric mean   | (ref)                                                                      | 1.01x slower                                                                 |

Benchmark hidden because not significant (9): async_tree_none, async_tree_io_tg, async_tree_memoization, async_tree_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 149 ms                                                                     | 149 ms: 1.00x faster                                                         |
| nbody          | 49.2 ms                                                                    | 49.8 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 123 ms                                                                     | 121 ms: 1.02x faster                                                         |
| regex_compile  | 96.5 ms                                                                    | 95.1 ms: 1.01x faster                                                        |
| regex_effbot   | 1.63 ms                                                                    | 1.61 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 1.28 sec                                                                   | 1.25 sec: 1.02x faster                                                       |
| unpickle             | 9.16 us                                                                    | 9.03 us: 1.01x faster                                                        |
| pickle               | 7.31 us                                                                    | 7.25 us: 1.01x faster                                                        |
| pickle_dict          | 17.7 us                                                                    | 17.7 us: 1.00x faster                                                        |
| pickle_pure_python   | 198 us                                                                     | 197 us: 1.00x faster                                                         |
| unpickle_pure_python | 141 us                                                                     | 142 us: 1.01x slower                                                         |
| json_dumps           | 5.84 ms                                                                    | 5.91 ms: 1.01x slower                                                        |
| unpickle_list        | 2.82 us                                                                    | 2.86 us: 1.01x slower                                                        |
| xml_etree_parse      | 92.9 ms                                                                    | 94.1 ms: 1.01x slower                                                        |
| Geometric mean       | (ref)                                                                      | 1.00x faster                                                                 |

Benchmark hidden because not significant (5): pickle_list, xml_etree_iterparse, xml_etree_generate, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 26.8 ms                                                                    | 26.6 ms: 1.01x faster                                                        |
| genshi_text     | 19.2 ms                                                                    | 19.3 ms: 1.01x slower                                                        |
| mako            | 4.92 ms                                                                    | 5.00 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                                      | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark            | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pprint_pformat       | 1.12 sec                                                                   | 1.07 sec: 1.05x faster                                                       |
| pprint_safe_repr     | 539 ms                                                                     | 523 ms: 1.03x faster                                                         |
| pycparser            | 736 ms                                                                     | 716 ms: 1.03x faster                                                         |
| chaos                | 41.7 ms                                                                    | 40.6 ms: 1.03x faster                                                        |
| pathlib              | 81.6 ms                                                                    | 79.6 ms: 1.03x faster                                                        |
| hexiom               | 5.03 ms                                                                    | 4.90 ms: 1.02x faster                                                        |
| nqueens              | 62.2 ms                                                                    | 60.8 ms: 1.02x faster                                                        |
| sympy_expand         | 337 ms                                                                     | 329 ms: 1.02x faster                                                         |
| scimark_lu           | 55.6 ms                                                                    | 54.3 ms: 1.02x faster                                                        |
| tomli_loads          | 1.28 sec                                                                   | 1.25 sec: 1.02x faster                                                       |
| generators           | 22.9 ms                                                                    | 22.5 ms: 1.02x faster                                                        |
| sympy_str            | 192 ms                                                                     | 188 ms: 1.02x faster                                                         |
| async_generators     | 261 ms                                                                     | 257 ms: 1.02x faster                                                         |
| regex_dna            | 123 ms                                                                     | 121 ms: 1.02x faster                                                         |
| deepcopy             | 188 us                                                                     | 185 us: 1.02x faster                                                         |
| unpickle             | 9.16 us                                                                    | 9.03 us: 1.01x faster                                                        |
| thrift               | 518 us                                                                     | 510 us: 1.01x faster                                                         |
| regex_compile        | 96.5 ms                                                                    | 95.1 ms: 1.01x faster                                                        |
| sympy_sum            | 99.7 ms                                                                    | 98.3 ms: 1.01x faster                                                        |
| pyflate              | 265 ms                                                                     | 261 ms: 1.01x faster                                                         |
| regex_effbot         | 1.63 ms                                                                    | 1.61 ms: 1.01x faster                                                        |
| scimark_sor          | 61.1 ms                                                                    | 60.5 ms: 1.01x faster                                                        |
| sqlglot_normalize    | 203 ms                                                                     | 201 ms: 1.01x faster                                                         |
| gc_traversal         | 1.55 ms                                                                    | 1.54 ms: 1.01x faster                                                        |
| sympy_integrate      | 15.0 ms                                                                    | 14.8 ms: 1.01x faster                                                        |
| sqlglot_optimize     | 40.8 ms                                                                    | 40.4 ms: 1.01x faster                                                        |
| django_template      | 26.8 ms                                                                    | 26.6 ms: 1.01x faster                                                        |
| docutils             | 1.93 sec                                                                   | 1.91 sec: 1.01x faster                                                       |
| pickle               | 7.31 us                                                                    | 7.25 us: 1.01x faster                                                        |
| coroutines           | 14.1 ms                                                                    | 14.0 ms: 1.01x faster                                                        |
| go                   | 93.2 ms                                                                    | 92.7 ms: 1.00x faster                                                        |
| pidigits             | 149 ms                                                                     | 149 ms: 1.00x faster                                                         |
| pickle_dict          | 17.7 us                                                                    | 17.7 us: 1.00x faster                                                        |
| pickle_pure_python   | 198 us                                                                     | 197 us: 1.00x faster                                                         |
| crypto_pyaes         | 38.7 ms                                                                    | 38.8 ms: 1.00x slower                                                        |
| scimark_monte_carlo  | 42.8 ms                                                                    | 43.0 ms: 1.00x slower                                                        |
| sqlite_synth         | 1.59 us                                                                    | 1.61 us: 1.01x slower                                                        |
| genshi_text          | 19.2 ms                                                                    | 19.3 ms: 1.01x slower                                                        |
| unpickle_pure_python | 141 us                                                                     | 142 us: 1.01x slower                                                         |
| bench_mp_pool        | 71.5 ms                                                                    | 72.1 ms: 1.01x slower                                                        |
| coverage             | 47.3 ms                                                                    | 47.7 ms: 1.01x slower                                                        |
| raytrace             | 207 ms                                                                     | 209 ms: 1.01x slower                                                         |
| json_dumps           | 5.84 ms                                                                    | 5.91 ms: 1.01x slower                                                        |
| unpickle_list        | 2.82 us                                                                    | 2.86 us: 1.01x slower                                                        |
| richards_super       | 39.3 ms                                                                    | 39.8 ms: 1.01x slower                                                        |
| xml_etree_parse      | 92.9 ms                                                                    | 94.1 ms: 1.01x slower                                                        |
| nbody                | 49.2 ms                                                                    | 49.8 ms: 1.01x slower                                                        |
| deepcopy_memo        | 15.5 us                                                                    | 15.7 us: 1.01x slower                                                        |
| fannkuch             | 243 ms                                                                     | 247 ms: 1.01x slower                                                         |
| mako                 | 4.92 ms                                                                    | 5.00 ms: 1.02x slower                                                        |
| json                 | 2.93 ms                                                                    | 2.99 ms: 1.02x slower                                                        |
| deepcopy_reduce      | 1.80 us                                                                    | 1.86 us: 1.03x slower                                                        |
| mdp                  | 1.41 sec                                                                   | 1.47 sec: 1.04x slower                                                       |
| unpack_sequence      | 56.3 ns                                                                    | 58.8 ns: 1.04x slower                                                        |
| asyncio_tcp          | 542 ms                                                                     | 611 ms: 1.13x slower                                                         |
| Geometric mean       | (ref)                                                                      | 1.00x faster                                                                 |

Benchmark hidden because not significant (40): pickle_list, logging_silent, async_tree_none, regex_v8, async_tree_io_tg, scimark_sparse_mat_mult, pylint, async_tree_memoization, xml_etree_iterparse, async_tree_io, async_tree_none_tg, xml_etree_generate, sqlglot_transpile, async_tree_memoization_tg, logging_format, dulwich_log, json_loads, typing_runtime_protocols, meteor_contest, richards, tornado_http, logging_simple, deltablue, create_gc_cycles, comprehensions, xml_etree_process, scimark_fft, 2to3, sqlglot_parse, telco, python_startup, spectral_norm, async_tree_cpu_io_mixed, html5lib, async_tree_cpu_io_mixed_tg, python_startup_no_site, bench_thread_pool, float, genshi_xml, asyncio_tcp_ssl

# HPT report

- Reliability score: 99.60% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
# Results vs. base

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: linux-x86_64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.00x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 273 ms                                                                | 274 ms: 1.00x slower                                                    |
| html5lib       | 64.5 ms                                                               | 62.0 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_generators           | 460 ms                                                                | 455 ms: 1.01x faster                                                    |
| asyncio_tcp                | 496 ms                                                                | 491 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed_tg | 547 ms                                                                | 556 ms: 1.02x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (10): asyncio_tcp_ssl, async_tree_none, asyncio_websockets, async_tree_none_tg, coroutines, async_tree_memoization_tg, async_tree_memoization, async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                | 186 ms: 1.00x slower                                                    |
| float          | 69.5 ms                                                               | 70.1 ms: 1.01x slower                                                   |
| nbody          | 79.6 ms                                                               | 81.8 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 225 ms                                                                | 212 ms: 1.06x faster                                                    |
| regex_v8       | 24.7 ms                                                               | 24.2 ms: 1.02x faster                                                   |
| regex_compile  | 142 ms                                                                | 142 ms: 1.00x slower                                                    |
| regex_effbot   | 3.70 ms                                                               | 3.72 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_dict          | 35.0 us                                                               | 33.3 us: 1.05x faster                                                   |
| pickle               | 11.8 us                                                               | 11.6 us: 1.02x faster                                                   |
| unpickle_pure_python | 214 us                                                                | 215 us: 1.00x slower                                                    |
| json_loads           | 26.9 us                                                               | 27.2 us: 1.01x slower                                                   |
| unpickle_list        | 5.19 us                                                               | 5.30 us: 1.02x slower                                                   |
| tomli_loads          | 1.92 sec                                                              | 1.96 sec: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (8): unpickle, xml_etree_parse, pickle_pure_python, xml_etree_process, pickle_list, json_dumps, xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.01x slower                                                   |
| python_startup_no_site | 7.04 ms                                                               | 7.08 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 56.5 ms                                                               | 57.2 ms: 1.01x slower                                                   |
| mako           | 9.96 ms                                                               | 10.1 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna                  | 225 ms                                                                | 212 ms: 1.06x faster                                                    |
| pickle_dict                | 35.0 us                                                               | 33.3 us: 1.05x faster                                                   |
| html5lib                   | 64.5 ms                                                               | 62.0 ms: 1.04x faster                                                   |
| pycparser                  | 1.20 sec                                                              | 1.16 sec: 1.04x faster                                                  |
| regex_v8                   | 24.7 ms                                                               | 24.2 ms: 1.02x faster                                                   |
| pickle                     | 11.8 us                                                               | 11.6 us: 1.02x faster                                                   |
| telco                      | 7.99 ms                                                               | 7.86 ms: 1.02x faster                                                   |
| async_generators           | 460 ms                                                                | 455 ms: 1.01x faster                                                    |
| asyncio_tcp                | 496 ms                                                                | 491 ms: 1.01x faster                                                    |
| richards_super             | 45.2 ms                                                               | 44.9 ms: 1.01x faster                                                   |
| deepcopy_memo              | 26.8 us                                                               | 26.7 us: 1.01x faster                                                   |
| sqlglot_transpile          | 1.68 ms                                                               | 1.67 ms: 1.00x faster                                                   |
| pidigits                   | 186 ms                                                                | 186 ms: 1.00x slower                                                    |
| sympy_expand               | 500 ms                                                                | 502 ms: 1.00x slower                                                    |
| regex_compile              | 142 ms                                                                | 142 ms: 1.00x slower                                                    |
| 2to3                       | 273 ms                                                                | 274 ms: 1.00x slower                                                    |
| mdp                        | 2.59 sec                                                              | 2.60 sec: 1.00x slower                                                  |
| sympy_str                  | 296 ms                                                                | 298 ms: 1.00x slower                                                    |
| bpe_tokeniser              | 4.43 sec                                                              | 4.45 sec: 1.00x slower                                                  |
| unpickle_pure_python       | 214 us                                                                | 215 us: 1.00x slower                                                    |
| go                         | 131 ms                                                                | 132 ms: 1.00x slower                                                    |
| python_startup             | 10.5 ms                                                               | 10.5 ms: 1.01x slower                                                   |
| sympy_sum                  | 171 ms                                                                | 172 ms: 1.01x slower                                                    |
| python_startup_no_site     | 7.04 ms                                                               | 7.08 ms: 1.01x slower                                                   |
| sympy_integrate            | 22.6 ms                                                               | 22.7 ms: 1.01x slower                                                   |
| logging_silent             | 104 ns                                                                | 104 ns: 1.01x slower                                                    |
| raytrace                   | 274 ms                                                                | 276 ms: 1.01x slower                                                    |
| regex_effbot               | 3.70 ms                                                               | 3.72 ms: 1.01x slower                                                   |
| logging_format             | 6.01 us                                                               | 6.05 us: 1.01x slower                                                   |
| scimark_sor                | 116 ms                                                                | 117 ms: 1.01x slower                                                    |
| pathlib                    | 15.8 ms                                                               | 15.9 ms: 1.01x slower                                                   |
| float                      | 69.5 ms                                                               | 70.1 ms: 1.01x slower                                                   |
| deltablue                  | 3.16 ms                                                               | 3.19 ms: 1.01x slower                                                   |
| fannkuch                   | 380 ms                                                                | 384 ms: 1.01x slower                                                    |
| deepcopy_reduce            | 2.62 us                                                               | 2.65 us: 1.01x slower                                                   |
| json_loads                 | 26.9 us                                                               | 27.2 us: 1.01x slower                                                   |
| bench_thread_pool          | 831 us                                                                | 841 us: 1.01x slower                                                    |
| sqlite_synth               | 2.71 us                                                               | 2.74 us: 1.01x slower                                                   |
| genshi_xml                 | 56.5 ms                                                               | 57.2 ms: 1.01x slower                                                   |
| mako                       | 9.96 ms                                                               | 10.1 ms: 1.01x slower                                                   |
| crypto_pyaes               | 65.8 ms                                                               | 66.8 ms: 1.01x slower                                                   |
| logging_simple             | 5.49 us                                                               | 5.58 us: 1.02x slower                                                   |
| async_tree_cpu_io_mixed_tg | 547 ms                                                                | 556 ms: 1.02x slower                                                    |
| gc_traversal               | 3.90 ms                                                               | 3.97 ms: 1.02x slower                                                   |
| meteor_contest             | 105 ms                                                                | 107 ms: 1.02x slower                                                    |
| scimark_fft                | 306 ms                                                                | 312 ms: 1.02x slower                                                    |
| pprint_pformat             | 1.51 sec                                                              | 1.54 sec: 1.02x slower                                                  |
| unpickle_list              | 5.19 us                                                               | 5.30 us: 1.02x slower                                                   |
| tomli_loads                | 1.92 sec                                                              | 1.96 sec: 1.02x slower                                                  |
| pyflate                    | 447 ms                                                                | 458 ms: 1.02x slower                                                    |
| spectral_norm              | 98.8 ms                                                               | 101 ms: 1.02x slower                                                    |
| unpack_sequence            | 109 ns                                                                | 112 ns: 1.02x slower                                                    |
| deepcopy                   | 255 us                                                                | 261 us: 1.02x slower                                                    |
| nbody                      | 79.6 ms                                                               | 81.8 ms: 1.03x slower                                                   |
| scimark_sparse_mat_mult    | 4.23 ms                                                               | 4.39 ms: 1.04x slower                                                   |
| pprint_safe_repr           | 740 ms                                                                | 772 ms: 1.04x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (41): unpickle, coverage, xml_etree_parse, sqlglot_parse, scimark_lu, typing_runtime_protocols, django_template, pickle_pure_python, comprehensions, sqlglot_normalize, pylint, docutils, asyncio_tcp_ssl, create_gc_cycles, xml_etree_process, richards, hexiom, scimark_monte_carlo, tornado_http, genshi_text, async_tree_none, generators, bench_mp_pool, asyncio_websockets, sqlglot_optimize, dulwich_log, async_tree_none_tg, pickle_list, json_dumps, thrift, coroutines, async_tree_memoization_tg, xml_etree_iterparse, async_tree_memoization, xml_etree_generate, nqueens, async_tree_io, json, async_tree_io_tg, chaos, async_tree_cpu_io_mixed

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x
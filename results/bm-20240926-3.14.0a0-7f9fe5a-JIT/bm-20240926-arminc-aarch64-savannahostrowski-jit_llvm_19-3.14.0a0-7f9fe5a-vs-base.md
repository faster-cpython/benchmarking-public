# Results vs. base

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: linux-aarch64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 382 ms                                                                  | 374 ms: 1.02x faster                                                      |
| docutils       | 3.93 sec                                                                | 3.85 sec: 1.02x faster                                                    |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                              |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| asyncio_tcp     | 627 ms                                                                  | 610 ms: 1.03x faster                                                      |
| async_tree_io   | 1.17 sec                                                                | 1.15 sec: 1.02x faster                                                    |
| asyncio_tcp_ssl | 2.25 sec                                                                | 2.23 sec: 1.01x faster                                                    |
| Geometric mean  | (ref)                                                                   | 1.01x faster                                                              |

Benchmark hidden because not significant (10): async_tree_none_tg, async_tree_none, coroutines, async_tree_memoization, async_generators, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                                  | 189 ms: 1.03x faster                                                      |
| regex_dna      | 254 ms                                                                  | 259 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                              |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|--------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python | 404 us                                                                  | 377 us: 1.07x faster                                                      |
| pickle             | 13.9 us                                                                 | 13.6 us: 1.02x faster                                                     |
| tomli_loads        | 2.62 sec                                                                | 2.58 sec: 1.02x faster                                                    |
| pickle_list        | 5.23 us                                                                 | 5.16 us: 1.01x faster                                                     |
| unpickle           | 19.5 us                                                                 | 19.3 us: 1.01x faster                                                     |
| unpickle_list      | 6.36 us                                                                 | 6.40 us: 1.01x slower                                                     |
| Geometric mean     | (ref)                                                                   | 1.01x faster                                                              |

Benchmark hidden because not significant (8): xml_etree_process, xml_etree_iterparse, unpickle_pure_python, json_loads, xml_etree_parse, pickle_dict, json_dumps, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                                 | 13.1 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                              |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 51.7 ms                                                                 | 50.0 ms: 1.03x faster                                                     |
| genshi_text     | 35.1 ms                                                                 | 34.6 ms: 1.01x faster                                                     |
| Geometric mean  | (ref)                                                                   | 1.01x faster                                                              |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|--------------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo            | 39.8 us                                                                 | 36.5 us: 1.09x faster                                                     |
| deepcopy                 | 417 us                                                                  | 385 us: 1.08x faster                                                      |
| pickle_pure_python       | 404 us                                                                  | 377 us: 1.07x faster                                                      |
| pyflate                  | 664 ms                                                                  | 623 ms: 1.07x faster                                                      |
| nqueens                  | 127 ms                                                                  | 119 ms: 1.06x faster                                                      |
| pprint_pformat           | 2.64 sec                                                                | 2.50 sec: 1.06x faster                                                    |
| pycparser                | 1.56 sec                                                                | 1.48 sec: 1.06x faster                                                    |
| scimark_monte_carlo      | 95.3 ms                                                                 | 91.0 ms: 1.05x faster                                                     |
| richards_super           | 75.9 ms                                                                 | 72.8 ms: 1.04x faster                                                     |
| hexiom                   | 10.2 ms                                                                 | 9.84 ms: 1.04x faster                                                     |
| chaos                    | 92.3 ms                                                                 | 88.7 ms: 1.04x faster                                                     |
| deepcopy_reduce          | 3.93 us                                                                 | 3.79 us: 1.04x faster                                                     |
| pprint_safe_repr         | 1.26 sec                                                                | 1.21 sec: 1.04x faster                                                    |
| django_template          | 51.7 ms                                                                 | 50.0 ms: 1.03x faster                                                     |
| richards                 | 67.0 ms                                                                 | 64.8 ms: 1.03x faster                                                     |
| fannkuch                 | 505 ms                                                                  | 490 ms: 1.03x faster                                                      |
| typing_runtime_protocols | 213 us                                                                  | 207 us: 1.03x faster                                                      |
| asyncio_tcp              | 627 ms                                                                  | 610 ms: 1.03x faster                                                      |
| regex_compile            | 194 ms                                                                  | 189 ms: 1.03x faster                                                      |
| comprehensions           | 24.7 us                                                                 | 24.1 us: 1.03x faster                                                     |
| go                       | 189 ms                                                                  | 185 ms: 1.02x faster                                                      |
| telco                    | 10.3 ms                                                                 | 10.0 ms: 1.02x faster                                                     |
| sqlglot_transpile        | 2.20 ms                                                                 | 2.16 ms: 1.02x faster                                                     |
| sympy_str                | 366 ms                                                                  | 359 ms: 1.02x faster                                                      |
| scimark_fft              | 458 ms                                                                  | 448 ms: 1.02x faster                                                      |
| sympy_expand             | 613 ms                                                                  | 600 ms: 1.02x faster                                                      |
| 2to3                     | 382 ms                                                                  | 374 ms: 1.02x faster                                                      |
| pickle                   | 13.9 us                                                                 | 13.6 us: 1.02x faster                                                     |
| docutils                 | 3.93 sec                                                                | 3.85 sec: 1.02x faster                                                    |
| async_tree_io            | 1.17 sec                                                                | 1.15 sec: 1.02x faster                                                    |
| crypto_pyaes             | 89.4 ms                                                                 | 87.9 ms: 1.02x faster                                                     |
| tomli_loads              | 2.62 sec                                                                | 2.58 sec: 1.02x faster                                                    |
| meteor_contest           | 125 ms                                                                  | 123 ms: 1.02x faster                                                      |
| scimark_sor              | 152 ms                                                                  | 150 ms: 1.01x faster                                                      |
| spectral_norm            | 147 ms                                                                  | 144 ms: 1.01x faster                                                      |
| coverage                 | 102 ms                                                                  | 100 ms: 1.01x faster                                                      |
| raytrace                 | 346 ms                                                                  | 342 ms: 1.01x faster                                                      |
| deltablue                | 4.40 ms                                                                 | 4.34 ms: 1.01x faster                                                     |
| genshi_text              | 35.1 ms                                                                 | 34.6 ms: 1.01x faster                                                     |
| pickle_list              | 5.23 us                                                                 | 5.16 us: 1.01x faster                                                     |
| bpe_tokeniser            | 5.92 sec                                                                | 5.86 sec: 1.01x faster                                                    |
| asyncio_tcp_ssl          | 2.25 sec                                                                | 2.23 sec: 1.01x faster                                                    |
| unpickle                 | 19.5 us                                                                 | 19.3 us: 1.01x faster                                                     |
| sympy_integrate          | 28.5 ms                                                                 | 28.2 ms: 1.01x faster                                                     |
| unpickle_list            | 6.36 us                                                                 | 6.40 us: 1.01x slower                                                     |
| python_startup           | 13.0 ms                                                                 | 13.1 ms: 1.01x slower                                                     |
| regex_dna                | 254 ms                                                                  | 259 ms: 1.02x slower                                                      |
| Geometric mean           | (ref)                                                                   | 1.01x faster                                                              |

Benchmark hidden because not significant (50): async_tree_none_tg, xml_etree_process, xml_etree_iterparse, sympy_sum, gc_traversal, bench_mp_pool, async_tree_none, sqlglot_normalize, dulwich_log, coroutines, async_tree_memoization, json, async_generators, unpickle_pure_python, logging_simple, sqlglot_parse, pylint, mako, thrift, async_tree_cpu_io_mixed_tg, genshi_xml, async_tree_cpu_io_mixed, generators, sqlite_synth, scimark_sparse_mat_mult, json_loads, bench_thread_pool, logging_format, asyncio_websockets, tornado_http, mdp, float, pidigits, python_startup_no_site, scimark_lu, async_tree_memoization_tg, xml_etree_parse, html5lib, nbody, async_tree_io_tg, pickle_dict, regex_v8, logging_silent, create_gc_cycles, json_dumps, sqlglot_optimize, regex_effbot, unpack_sequence, pathlib, xml_etree_generate

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x
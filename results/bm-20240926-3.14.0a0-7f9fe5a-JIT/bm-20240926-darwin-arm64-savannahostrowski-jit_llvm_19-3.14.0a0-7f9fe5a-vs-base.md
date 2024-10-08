# Results vs. base

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: darwin-arm64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.00x slower
- HPT reliability: 80.11%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 1.56 sec                                                              | 1.57 sec: 1.00x slower                                                  |
| html5lib       | 32.3 ms                                                               | 33.0 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_tcp_ssl     | 1.29 sec                                                              | 1.28 sec: 1.01x faster                                                  |
| async_generators    | 292 ms                                                                | 292 ms: 1.00x slower                                                    |
| async_tree_eager    | 64.1 ms                                                               | 64.7 ms: 1.01x slower                                                   |
| coroutines          | 16.4 ms                                                               | 16.6 ms: 1.01x slower                                                   |
| async_tree_eager_tg | 42.2 ms                                                               | 43.0 ms: 1.02x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (16): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, asyncio_websockets, async_tree_io, async_tree_eager_io, async_tree_memoization_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_memoization, async_tree_eager_io_tg, async_tree_memoization, async_tree_none, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 46.1 ms                                                               | 45.8 ms: 1.01x faster                                                   |
| nbody          | 63.5 ms                                                               | 64.2 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 16.5 ms                                                               | 16.5 ms: 1.00x slower                                                   |
| regex_compile  | 75.6 ms                                                               | 76.0 ms: 1.01x slower                                                   |
| regex_effbot   | 2.46 ms                                                               | 2.48 ms: 1.01x slower                                                   |
| regex_dna      | 145 ms                                                                | 146 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|--------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python | 179 us                                                                | 176 us: 1.01x faster                                                    |
| pickle_dict        | 18.5 us                                                               | 18.3 us: 1.01x faster                                                   |
| xml_etree_generate | 51.1 ms                                                               | 50.5 ms: 1.01x faster                                                   |
| unpickle           | 9.28 us                                                               | 9.18 us: 1.01x faster                                                   |
| pickle             | 7.47 us                                                               | 7.44 us: 1.00x faster                                                   |
| xml_etree_parse    | 106 ms                                                                | 107 ms: 1.01x slower                                                    |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (8): xml_etree_iterparse, tomli_loads, xml_etree_process, unpickle_pure_python, json_dumps, json_loads, unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 13.8 ms                                                               | 13.7 ms: 1.01x faster                                                   |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 16.8 ms                                                               | 16.5 ms: 1.02x faster                                                   |
| django_template | 22.8 ms                                                               | 22.4 ms: 1.02x faster                                                   |
| mako            | 6.47 ms                                                               | 6.43 ms: 1.01x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| richards                | 45.9 ms                                                               | 44.6 ms: 1.03x faster                                                   |
| telco                   | 4.78 ms                                                               | 4.65 ms: 1.03x faster                                                   |
| richards_super          | 47.9 ms                                                               | 46.7 ms: 1.03x faster                                                   |
| genshi_text             | 16.8 ms                                                               | 16.5 ms: 1.02x faster                                                   |
| django_template         | 22.8 ms                                                               | 22.4 ms: 1.02x faster                                                   |
| fannkuch                | 269 ms                                                                | 266 ms: 1.01x faster                                                    |
| pickle_pure_python      | 179 us                                                                | 176 us: 1.01x faster                                                    |
| pickle_dict             | 18.5 us                                                               | 18.3 us: 1.01x faster                                                   |
| xml_etree_generate      | 51.1 ms                                                               | 50.5 ms: 1.01x faster                                                   |
| scimark_lu              | 63.9 ms                                                               | 63.2 ms: 1.01x faster                                                   |
| unpickle                | 9.28 us                                                               | 9.18 us: 1.01x faster                                                   |
| python_startup_no_site  | 13.8 ms                                                               | 13.7 ms: 1.01x faster                                                   |
| create_gc_cycles        | 905 us                                                                | 898 us: 1.01x faster                                                    |
| meteor_contest          | 74.9 ms                                                               | 74.4 ms: 1.01x faster                                                   |
| float                   | 46.1 ms                                                               | 45.8 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl         | 1.29 sec                                                              | 1.28 sec: 1.01x faster                                                  |
| logging_format          | 3.31 us                                                               | 3.29 us: 1.01x faster                                                   |
| mako                    | 6.47 ms                                                               | 6.43 ms: 1.01x faster                                                   |
| scimark_fft             | 185 ms                                                                | 184 ms: 1.01x faster                                                    |
| logging_simple          | 3.02 us                                                               | 3.01 us: 1.00x faster                                                   |
| sqlite_synth            | 1.58 us                                                               | 1.57 us: 1.00x faster                                                   |
| nqueens                 | 57.9 ms                                                               | 57.7 ms: 1.00x faster                                                   |
| pickle                  | 7.47 us                                                               | 7.44 us: 1.00x faster                                                   |
| gc_traversal            | 2.46 ms                                                               | 2.46 ms: 1.00x faster                                                   |
| async_generators        | 292 ms                                                                | 292 ms: 1.00x slower                                                    |
| regex_v8                | 16.5 ms                                                               | 16.5 ms: 1.00x slower                                                   |
| docutils                | 1.56 sec                                                              | 1.57 sec: 1.00x slower                                                  |
| sqlglot_optimize        | 35.3 ms                                                               | 35.4 ms: 1.00x slower                                                   |
| chaos                   | 39.9 ms                                                               | 40.1 ms: 1.00x slower                                                   |
| go                      | 100 ms                                                                | 101 ms: 1.00x slower                                                    |
| hexiom                  | 4.73 ms                                                               | 4.75 ms: 1.00x slower                                                   |
| sympy_str               | 144 ms                                                                | 144 ms: 1.00x slower                                                    |
| regex_compile           | 75.6 ms                                                               | 76.0 ms: 1.01x slower                                                   |
| coverage                | 44.4 ms                                                               | 44.7 ms: 1.01x slower                                                   |
| logging_silent          | 62.5 ns                                                               | 63.0 ns: 1.01x slower                                                   |
| scimark_sparse_mat_mult | 2.96 ms                                                               | 2.98 ms: 1.01x slower                                                   |
| comprehensions          | 12.7 us                                                               | 12.8 us: 1.01x slower                                                   |
| json                    | 2.90 ms                                                               | 2.92 ms: 1.01x slower                                                   |
| regex_effbot            | 2.46 ms                                                               | 2.48 ms: 1.01x slower                                                   |
| pprint_safe_repr        | 504 ms                                                                | 509 ms: 1.01x slower                                                    |
| sympy_sum               | 75.8 ms                                                               | 76.4 ms: 1.01x slower                                                   |
| bench_thread_pool       | 470 us                                                                | 474 us: 1.01x slower                                                    |
| sympy_integrate         | 11.6 ms                                                               | 11.7 ms: 1.01x slower                                                   |
| pyflate                 | 327 ms                                                                | 330 ms: 1.01x slower                                                    |
| async_tree_eager        | 64.1 ms                                                               | 64.7 ms: 1.01x slower                                                   |
| nbody                   | 63.5 ms                                                               | 64.2 ms: 1.01x slower                                                   |
| deepcopy                | 152 us                                                                | 154 us: 1.01x slower                                                    |
| coroutines              | 16.4 ms                                                               | 16.6 ms: 1.01x slower                                                   |
| regex_dna               | 145 ms                                                                | 146 ms: 1.01x slower                                                    |
| xml_etree_parse         | 106 ms                                                                | 107 ms: 1.01x slower                                                    |
| sqlglot_normalize       | 180 ms                                                                | 182 ms: 1.02x slower                                                    |
| mdp                     | 1.44 sec                                                              | 1.47 sec: 1.02x slower                                                  |
| async_tree_eager_tg     | 42.2 ms                                                               | 43.0 ms: 1.02x slower                                                   |
| html5lib                | 32.3 ms                                                               | 33.0 ms: 1.02x slower                                                   |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (51): pathlib, xml_etree_iterparse, deltablue, genshi_xml, async_tree_none_tg, async_tree_cpu_io_mixed_tg, python_startup, 2to3, async_tree_io_tg, generators, bench_mp_pool, tomli_loads, xml_etree_process, crypto_pyaes, pidigits, asyncio_websockets, async_tree_io, bpe_tokeniser, unpickle_pure_python, typing_runtime_protocols, async_tree_eager_io, sqlglot_parse, async_tree_memoization_tg, async_tree_eager_cpu_io_mixed_tg, deepcopy_memo, sympy_expand, sqlglot_transpile, dulwich_log, async_tree_eager_memoization, thrift, spectral_norm, async_tree_eager_io_tg, async_tree_memoization, scimark_monte_carlo, async_tree_none, raytrace, deepcopy_reduce, scimark_sor, json_dumps, async_tree_eager_cpu_io_mixed, json_loads, unpickle_list, async_tree_cpu_io_mixed, pprint_pformat, unpack_sequence, pickle_list, pycparser, async_tree_eager_memoization_tg, pylint, asyncio_tcp, tornado_http

# HPT report

- Reliability score: 80.11% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x
# Results vs. base

- fork: Fidget-Spinner
- ref: partial_evaluator_un
- machine: linux-x86_64
- commit hash: aaab6a6
- commit date: 2024-09-20
- overall geometric mean: 1.003x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.53x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 273 ms                                                                | 276 ms: 1.01x slower                                                            |
| docutils       | 2.96 sec                                                              | 2.97 sec: 1.00x slower                                                          |
| html5lib       | 64.2 ms                                                               | 65.1 ms: 1.02x slower                                                           |
| tornado_http   | 94.3 ms                                                               | 95.1 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines             | 22.8 ms                                                               | 22.5 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl        | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                                          |
| asyncio_tcp            | 487 ms                                                                | 497 ms: 1.02x slower                                                            |
| async_tree_none        | 312 ms                                                                | 320 ms: 1.02x slower                                                            |
| async_tree_memoization | 393 ms                                                                | 403 ms: 1.03x slower                                                            |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (8): async_tree_memoization_tg, asyncio_websockets, async_generators, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 185 ms                                                                | 187 ms: 1.01x slower                                                            |
| nbody          | 80.5 ms                                                               | 81.1 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 24.5 ms                                                               | 24.3 ms: 1.01x faster                                                           |
| regex_effbot   | 3.81 ms                                                               | 3.92 ms: 1.03x slower                                                           |
| regex_dna      | 216 ms                                                                | 226 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle             | 14.9 us                                                               | 14.4 us: 1.03x faster                                                           |
| json_loads           | 27.4 us                                                               | 26.6 us: 1.03x faster                                                           |
| xml_etree_iterparse  | 99.1 ms                                                               | 98.1 ms: 1.01x faster                                                           |
| json_dumps           | 10.1 ms                                                               | 10.1 ms: 1.01x slower                                                           |
| pickle_dict          | 34.0 us                                                               | 34.4 us: 1.01x slower                                                           |
| unpickle_pure_python | 213 us                                                                | 216 us: 1.01x slower                                                            |
| unpickle_list        | 5.21 us                                                               | 5.29 us: 1.01x slower                                                           |
| pickle_list          | 5.05 us                                                               | 5.17 us: 1.02x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (6): xml_etree_process, xml_etree_generate, pickle, tomli_loads, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                           |
| python_startup_no_site | 7.08 ms                                                               | 7.12 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 25.5 ms                                                               | 24.6 ms: 1.04x faster                                                           |
| genshi_xml      | 58.8 ms                                                               | 58.1 ms: 1.01x faster                                                           |
| mako            | 9.95 ms                                                               | 9.92 ms: 1.00x faster                                                           |
| django_template | 35.4 ms                                                               | 36.2 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark               | bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| scimark_sparse_mat_mult | 4.55 ms                                                               | 4.37 ms: 1.04x faster                                                           |
| genshi_text             | 25.5 ms                                                               | 24.6 ms: 1.04x faster                                                           |
| unpickle                | 14.9 us                                                               | 14.4 us: 1.03x faster                                                           |
| json_loads              | 27.4 us                                                               | 26.6 us: 1.03x faster                                                           |
| json                    | 5.10 ms                                                               | 4.97 ms: 1.02x faster                                                           |
| deepcopy_reduce         | 2.69 us                                                               | 2.63 us: 1.02x faster                                                           |
| mdp                     | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                                          |
| deepcopy                | 264 us                                                                | 260 us: 1.02x faster                                                            |
| coverage                | 85.6 ms                                                               | 84.2 ms: 1.02x faster                                                           |
| genshi_xml              | 58.8 ms                                                               | 58.1 ms: 1.01x faster                                                           |
| telco                   | 7.98 ms                                                               | 7.88 ms: 1.01x faster                                                           |
| xml_etree_iterparse     | 99.1 ms                                                               | 98.1 ms: 1.01x faster                                                           |
| coroutines              | 22.8 ms                                                               | 22.5 ms: 1.01x faster                                                           |
| regex_v8                | 24.5 ms                                                               | 24.3 ms: 1.01x faster                                                           |
| dulwich_log             | 67.6 ms                                                               | 67.2 ms: 1.01x faster                                                           |
| bench_thread_pool       | 838 us                                                                | 835 us: 1.00x faster                                                            |
| bpe_tokeniser           | 4.47 sec                                                              | 4.46 sec: 1.00x faster                                                          |
| mako                    | 9.95 ms                                                               | 9.92 ms: 1.00x faster                                                           |
| python_startup          | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                           |
| meteor_contest          | 105 ms                                                                | 106 ms: 1.00x slower                                                            |
| gc_traversal            | 3.90 ms                                                               | 3.91 ms: 1.00x slower                                                           |
| docutils                | 2.96 sec                                                              | 2.97 sec: 1.00x slower                                                          |
| asyncio_tcp_ssl         | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                                          |
| hexiom                  | 6.83 ms                                                               | 6.86 ms: 1.00x slower                                                           |
| generators              | 32.8 ms                                                               | 33.0 ms: 1.00x slower                                                           |
| json_dumps              | 10.1 ms                                                               | 10.1 ms: 1.01x slower                                                           |
| unpack_sequence         | 111 ns                                                                | 111 ns: 1.01x slower                                                            |
| deepcopy_memo           | 26.7 us                                                               | 26.9 us: 1.01x slower                                                           |
| python_startup_no_site  | 7.08 ms                                                               | 7.12 ms: 1.01x slower                                                           |
| sympy_integrate         | 22.7 ms                                                               | 22.8 ms: 1.01x slower                                                           |
| pidigits                | 185 ms                                                                | 187 ms: 1.01x slower                                                            |
| nbody                   | 80.5 ms                                                               | 81.1 ms: 1.01x slower                                                           |
| tornado_http            | 94.3 ms                                                               | 95.1 ms: 1.01x slower                                                           |
| sympy_sum               | 171 ms                                                                | 173 ms: 1.01x slower                                                            |
| richards_super          | 45.3 ms                                                               | 45.7 ms: 1.01x slower                                                           |
| sympy_expand            | 500 ms                                                                | 505 ms: 1.01x slower                                                            |
| sqlglot_normalize       | 112 ms                                                                | 113 ms: 1.01x slower                                                            |
| 2to3                    | 273 ms                                                                | 276 ms: 1.01x slower                                                            |
| pickle_dict             | 34.0 us                                                               | 34.4 us: 1.01x slower                                                           |
| logging_simple          | 5.56 us                                                               | 5.62 us: 1.01x slower                                                           |
| sqlglot_optimize        | 57.7 ms                                                               | 58.4 ms: 1.01x slower                                                           |
| go                      | 131 ms                                                                | 132 ms: 1.01x slower                                                            |
| unpickle_pure_python    | 213 us                                                                | 216 us: 1.01x slower                                                            |
| sqlglot_parse           | 1.34 ms                                                               | 1.35 ms: 1.01x slower                                                           |
| thrift                  | 781 us                                                                | 792 us: 1.01x slower                                                            |
| fannkuch                | 370 ms                                                                | 375 ms: 1.01x slower                                                            |
| unpickle_list           | 5.21 us                                                               | 5.29 us: 1.01x slower                                                           |
| html5lib                | 64.2 ms                                                               | 65.1 ms: 1.02x slower                                                           |
| scimark_fft             | 314 ms                                                                | 320 ms: 1.02x slower                                                            |
| pyflate                 | 456 ms                                                                | 464 ms: 1.02x slower                                                            |
| sqlglot_transpile       | 1.68 ms                                                               | 1.71 ms: 1.02x slower                                                           |
| asyncio_tcp             | 487 ms                                                                | 497 ms: 1.02x slower                                                            |
| django_template         | 35.4 ms                                                               | 36.2 ms: 1.02x slower                                                           |
| pickle_list             | 5.05 us                                                               | 5.17 us: 1.02x slower                                                           |
| scimark_sor             | 116 ms                                                                | 119 ms: 1.02x slower                                                            |
| async_tree_none         | 312 ms                                                                | 320 ms: 1.02x slower                                                            |
| regex_effbot            | 3.81 ms                                                               | 3.92 ms: 1.03x slower                                                           |
| scimark_monte_carlo     | 62.5 ms                                                               | 64.2 ms: 1.03x slower                                                           |
| async_tree_memoization  | 393 ms                                                                | 403 ms: 1.03x slower                                                            |
| pprint_safe_repr        | 733 ms                                                                | 754 ms: 1.03x slower                                                            |
| regex_dna               | 216 ms                                                                | 226 ms: 1.05x slower                                                            |
| spectral_norm           | 101 ms                                                                | 107 ms: 1.05x slower                                                            |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (35): async_tree_memoization_tg, pylint, scimark_lu, pprint_pformat, raytrace, logging_silent, xml_etree_process, sqlite_synth, xml_etree_generate, typing_runtime_protocols, pathlib, float, create_gc_cycles, asyncio_websockets, comprehensions, pickle, bench_mp_pool, async_generators, regex_compile, nqueens, richards, tomli_loads, chaos, sympy_str, pycparser, deltablue, async_tree_cpu_io_mixed_tg, crypto_pyaes, logging_format, xml_etree_parse, pickle_pure_python, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_io_tg

- Geometric mean (including insignificant results): 1.003x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.53x
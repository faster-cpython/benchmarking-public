# Results vs. base

- fork: eendebakpt
- ref: int_freelist
- machine: linux-x86_64
- commit hash: d1e4aa2
- commit date: 2024-11-21
- overall geometric mean: 1.004x faster
- HPT reliability: 54.04%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                 | 257 ms: 1.00x slower                                               |
| docutils       | 2.68 sec                                                               | 2.69 sec: 1.00x slower                                             |
| html5lib       | 65.1 ms                                                                | 63.6 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none  | 330 ms                                                                 | 327 ms: 1.01x faster                                               |
| async_generators | 426 ms                                                                 | 432 ms: 1.01x slower                                               |
| coroutines       | 23.1 ms                                                                | 23.9 ms: 1.03x slower                                              |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (8): async_tree_io, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io_tg, asyncio_websockets, async_tree_none_tg, async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_dna      | 220 ms                                                                 | 212 ms: 1.04x faster                                               |
| regex_effbot   | 3.58 ms                                                                | 3.55 ms: 1.01x faster                                              |
| regex_compile  | 129 ms                                                                 | 128 ms: 1.00x faster                                               |
| regex_v8       | 24.2 ms                                                                | 24.6 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                               | 2.02 sec: 1.05x faster                                             |
| json_dumps           | 11.4 ms                                                                | 11.4 ms: 1.00x faster                                              |
| unpickle_pure_python | 218 us                                                                 | 219 us: 1.00x slower                                               |
| pickle_pure_python   | 326 us                                                                 | 327 us: 1.00x slower                                               |
| json_loads           | 27.0 us                                                                | 27.1 us: 1.01x slower                                              |
| xml_etree_process    | 59.0 ms                                                                | 59.5 ms: 1.01x slower                                              |
| xml_etree_generate   | 85.1 ms                                                                | 85.9 ms: 1.01x slower                                              |
| xml_etree_iterparse  | 105 ms                                                                 | 106 ms: 1.01x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 7.04 ms                                                                | 7.07 ms: 1.00x slower                                              |
| python_startup         | 12.7 ms                                                                | 12.8 ms: 1.00x slower                                              |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 11.7 ms                                                                | 11.6 ms: 1.01x faster                                              |
| genshi_xml      | 51.0 ms                                                                | 50.6 ms: 1.01x faster                                              |
| django_template | 32.3 ms                                                                | 32.0 ms: 1.01x faster                                              |
| genshi_text     | 22.5 ms                                                                | 22.7 ms: 1.01x slower                                              |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| spectral_norm           | 116 ms                                                                 | 103 ms: 1.13x faster                                               |
| scimark_sparse_mat_mult | 5.08 ms                                                                | 4.67 ms: 1.09x faster                                              |
| scimark_fft             | 374 ms                                                                 | 345 ms: 1.08x faster                                               |
| tomli_loads             | 2.12 sec                                                               | 2.02 sec: 1.05x faster                                             |
| scimark_sor             | 128 ms                                                                 | 122 ms: 1.05x faster                                               |
| regex_dna               | 220 ms                                                                 | 212 ms: 1.04x faster                                               |
| logging_silent          | 105 ns                                                                 | 102 ns: 1.04x faster                                               |
| html5lib                | 65.1 ms                                                                | 63.6 ms: 1.02x faster                                              |
| pyflate                 | 465 ms                                                                 | 456 ms: 1.02x faster                                               |
| sqlglot_transpile       | 1.62 ms                                                                | 1.59 ms: 1.02x faster                                              |
| scimark_lu              | 119 ms                                                                 | 117 ms: 1.02x faster                                               |
| mako                    | 11.7 ms                                                                | 11.6 ms: 1.01x faster                                              |
| sqlglot_parse           | 1.31 ms                                                                | 1.29 ms: 1.01x faster                                              |
| scimark_monte_carlo     | 69.5 ms                                                                | 68.6 ms: 1.01x faster                                              |
| go                      | 121 ms                                                                 | 119 ms: 1.01x faster                                               |
| deltablue               | 3.33 ms                                                                | 3.29 ms: 1.01x faster                                              |
| telco                   | 7.86 ms                                                                | 7.77 ms: 1.01x faster                                              |
| deepcopy_reduce         | 2.78 us                                                                | 2.75 us: 1.01x faster                                              |
| async_tree_none         | 330 ms                                                                 | 327 ms: 1.01x faster                                               |
| regex_effbot            | 3.58 ms                                                                | 3.55 ms: 1.01x faster                                              |
| sympy_expand            | 461 ms                                                                 | 457 ms: 1.01x faster                                               |
| genshi_xml              | 51.0 ms                                                                | 50.6 ms: 1.01x faster                                              |
| sqlite_synth            | 2.86 us                                                                | 2.83 us: 1.01x faster                                              |
| django_template         | 32.3 ms                                                                | 32.0 ms: 1.01x faster                                              |
| regex_compile           | 129 ms                                                                 | 128 ms: 1.00x faster                                               |
| json_dumps              | 11.4 ms                                                                | 11.4 ms: 1.00x faster                                              |
| crypto_pyaes            | 72.0 ms                                                                | 71.7 ms: 1.00x faster                                              |
| fannkuch                | 407 ms                                                                 | 406 ms: 1.00x faster                                               |
| gc_traversal            | 4.76 ms                                                                | 4.75 ms: 1.00x faster                                              |
| pidigits                | 187 ms                                                                 | 187 ms: 1.00x faster                                               |
| sqlglot_optimize        | 53.4 ms                                                                | 53.6 ms: 1.00x slower                                              |
| sympy_integrate         | 19.9 ms                                                                | 19.9 ms: 1.00x slower                                              |
| docutils                | 2.68 sec                                                               | 2.69 sec: 1.00x slower                                             |
| python_startup_no_site  | 7.04 ms                                                                | 7.07 ms: 1.00x slower                                              |
| comprehensions          | 17.0 us                                                                | 17.1 us: 1.00x slower                                              |
| unpickle_pure_python    | 218 us                                                                 | 219 us: 1.00x slower                                               |
| python_startup          | 12.7 ms                                                                | 12.8 ms: 1.00x slower                                              |
| pickle_pure_python      | 326 us                                                                 | 327 us: 1.00x slower                                               |
| 2to3                    | 256 ms                                                                 | 257 ms: 1.00x slower                                               |
| sqlglot_normalize       | 107 ms                                                                 | 107 ms: 1.01x slower                                               |
| json_loads              | 27.0 us                                                                | 27.1 us: 1.01x slower                                              |
| deepcopy                | 263 us                                                                 | 264 us: 1.01x slower                                               |
| richards                | 46.5 ms                                                                | 46.9 ms: 1.01x slower                                              |
| bench_mp_pool           | 78.5 ms                                                                | 79.1 ms: 1.01x slower                                              |
| sqlalchemy_declarative  | 128 ms                                                                 | 129 ms: 1.01x slower                                               |
| xml_etree_process       | 59.0 ms                                                                | 59.5 ms: 1.01x slower                                              |
| pprint_safe_repr        | 728 ms                                                                 | 734 ms: 1.01x slower                                               |
| bench_thread_pool       | 849 us                                                                 | 856 us: 1.01x slower                                               |
| chaos                   | 60.4 ms                                                                | 60.9 ms: 1.01x slower                                              |
| many_optionals          | 940 us                                                                 | 948 us: 1.01x slower                                               |
| pathlib                 | 15.9 ms                                                                | 16.0 ms: 1.01x slower                                              |
| genshi_text             | 22.5 ms                                                                | 22.7 ms: 1.01x slower                                              |
| xml_etree_generate      | 85.1 ms                                                                | 85.9 ms: 1.01x slower                                              |
| meteor_contest          | 106 ms                                                                 | 107 ms: 1.01x slower                                               |
| deepcopy_memo           | 30.4 us                                                                | 30.7 us: 1.01x slower                                              |
| generators              | 27.6 ms                                                                | 27.9 ms: 1.01x slower                                              |
| pprint_pformat          | 1.49 sec                                                               | 1.51 sec: 1.01x slower                                             |
| xml_etree_iterparse     | 105 ms                                                                 | 106 ms: 1.01x slower                                               |
| nqueens                 | 80.3 ms                                                                | 81.3 ms: 1.01x slower                                              |
| async_generators        | 426 ms                                                                 | 432 ms: 1.01x slower                                               |
| regex_v8                | 24.2 ms                                                                | 24.6 ms: 1.02x slower                                              |
| coroutines              | 23.1 ms                                                                | 23.9 ms: 1.03x slower                                              |
| mdp                     | 2.56 sec                                                               | 2.67 sec: 1.05x slower                                             |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (34): async_tree_io, k_core, async_tree_cpu_io_mixed, sphinx, subparsers, json, bpe_tokeniser, float, raytrace, nbody, logging_format, sympy_str, async_tree_cpu_io_mixed_tg, shortest_path, hexiom, dulwich_log, richards_super, coverage, pylint, create_gc_cycles, connected_components, sympy_sum, djangocms, typing_runtime_protocols, async_tree_io_tg, asyncio_websockets, xml_etree_parse, logging_simple, async_tree_none_tg, async_tree_memoization, async_tree_memoization_tg, thrift, sqlalchemy_imperative, pycparser

- Geometric mean (including insignificant results): 1.004x faster
# HPT report

- Reliability score: 54.04% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x
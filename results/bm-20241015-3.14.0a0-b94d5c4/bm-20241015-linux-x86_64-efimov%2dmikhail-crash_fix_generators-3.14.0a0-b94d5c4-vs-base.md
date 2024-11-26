# Results vs. base

- fork: efimov-mikhail
- ref: crash_fix_generators
- machine: linux-x86_64
- commit hash: b94d5c4
- commit date: 2024-10-15
- overall geometric mean: 1.000x faster
- HPT reliability: 77.15%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241015-linux-x86_64-python-703227dd021491ceb934-3.14.0a0-703227d | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 2.64 sec                                                              | 2.62 sec: 1.01x faster                                                          |
| html5lib       | 62.6 ms                                                               | 61.1 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241015-linux-x86_64-python-703227dd021491ceb934-3.14.0a0-703227d | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_generators | 438 ms                                                                | 440 ms: 1.00x slower                                                            |
| asyncio_tcp      | 478 ms                                                                | 480 ms: 1.01x slower                                                            |
| coroutines       | 23.2 ms                                                               | 24.0 ms: 1.04x slower                                                           |
| Geometric mean   | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241015-linux-x86_64-python-703227dd021491ceb934-3.14.0a0-703227d | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 94.6 ms                                                               | 89.4 ms: 1.06x faster                                                           |
| float          | 79.2 ms                                                               | 78.0 ms: 1.02x faster                                                           |
| pidigits       | 187 ms                                                                | 187 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241015-linux-x86_64-python-703227dd021491ceb934-3.14.0a0-703227d | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.63 ms                                                               | 3.49 ms: 1.04x faster                                                           |
| regex_dna      | 216 ms                                                                | 212 ms: 1.02x faster                                                            |
| regex_v8       | 24.7 ms                                                               | 24.4 ms: 1.01x faster                                                           |
| regex_compile  | 127 ms                                                                | 129 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241015-linux-x86_64-python-703227dd021491ceb934-3.14.0a0-703227d | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_iterparse | 105 ms                                                                | 104 ms: 1.02x faster                                                            |
| unpickle_list       | 5.24 us                                                               | 5.16 us: 1.02x faster                                                           |
| pickle_list         | 5.11 us                                                               | 5.06 us: 1.01x faster                                                           |
| pickle_pure_python  | 311 us                                                                | 308 us: 1.01x faster                                                            |
| json_dumps          | 11.3 ms                                                               | 11.2 ms: 1.01x faster                                                           |
| xml_etree_generate  | 85.9 ms                                                               | 85.5 ms: 1.01x faster                                                           |
| xml_etree_process   | 59.6 ms                                                               | 59.3 ms: 1.00x faster                                                           |
| json_loads          | 26.7 us                                                               | 26.8 us: 1.01x slower                                                           |
| pickle              | 11.7 us                                                               | 11.9 us: 1.02x slower                                                           |
| pickle_dict         | 33.4 us                                                               | 35.0 us: 1.05x slower                                                           |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (4): tomli_loads, xml_etree_parse, unpickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241015-linux-x86_64-python-703227dd021491ceb934-3.14.0a0-703227d | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                           |
| python_startup_no_site | 6.99 ms                                                               | 7.03 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241015-linux-x86_64-python-703227dd021491ceb934-3.14.0a0-703227d | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.7 ms                                                               | 11.3 ms: 1.04x faster                                                           |
| django_template | 34.4 ms                                                               | 33.8 ms: 1.02x faster                                                           |
| genshi_text     | 22.3 ms                                                               | 22.8 ms: 1.02x slower                                                           |
| genshi_xml      | 48.8 ms                                                               | 50.0 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                                    |

All benchmarks:
===============

| Benchmark               | bm-20241015-linux-x86_64-python-703227dd021491ceb934-3.14.0a0-703227d | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                     | 2.70 sec                                                              | 2.49 sec: 1.08x faster                                                          |
| unpack_sequence         | 43.3 ns                                                               | 40.0 ns: 1.08x faster                                                           |
| nbody                   | 94.6 ms                                                               | 89.4 ms: 1.06x faster                                                           |
| mako                    | 11.7 ms                                                               | 11.3 ms: 1.04x faster                                                           |
| regex_effbot            | 3.63 ms                                                               | 3.49 ms: 1.04x faster                                                           |
| html5lib                | 62.6 ms                                                               | 61.1 ms: 1.03x faster                                                           |
| richards                | 46.8 ms                                                               | 45.9 ms: 1.02x faster                                                           |
| richards_super          | 53.1 ms                                                               | 52.1 ms: 1.02x faster                                                           |
| regex_dna               | 216 ms                                                                | 212 ms: 1.02x faster                                                            |
| django_template         | 34.4 ms                                                               | 33.8 ms: 1.02x faster                                                           |
| logging_silent          | 106 ns                                                                | 104 ns: 1.02x faster                                                            |
| xml_etree_iterparse     | 105 ms                                                                | 104 ms: 1.02x faster                                                            |
| unpickle_list           | 5.24 us                                                               | 5.16 us: 1.02x faster                                                           |
| float                   | 79.2 ms                                                               | 78.0 ms: 1.02x faster                                                           |
| regex_v8                | 24.7 ms                                                               | 24.4 ms: 1.01x faster                                                           |
| deltablue               | 3.30 ms                                                               | 3.27 ms: 1.01x faster                                                           |
| pickle_list             | 5.11 us                                                               | 5.06 us: 1.01x faster                                                           |
| pickle_pure_python      | 311 us                                                                | 308 us: 1.01x faster                                                            |
| go                      | 120 ms                                                                | 120 ms: 1.01x faster                                                            |
| sqlglot_transpile       | 1.61 ms                                                               | 1.60 ms: 1.01x faster                                                           |
| meteor_contest          | 106 ms                                                                | 105 ms: 1.01x faster                                                            |
| docutils                | 2.64 sec                                                              | 2.62 sec: 1.01x faster                                                          |
| bench_thread_pool       | 842 us                                                                | 837 us: 1.01x faster                                                            |
| json_dumps              | 11.3 ms                                                               | 11.2 ms: 1.01x faster                                                           |
| pathlib                 | 16.0 ms                                                               | 15.9 ms: 1.01x faster                                                           |
| scimark_monte_carlo     | 68.1 ms                                                               | 67.8 ms: 1.01x faster                                                           |
| xml_etree_generate      | 85.9 ms                                                               | 85.5 ms: 1.01x faster                                                           |
| xml_etree_process       | 59.6 ms                                                               | 59.3 ms: 1.00x faster                                                           |
| raytrace                | 269 ms                                                                | 268 ms: 1.00x faster                                                            |
| scimark_fft             | 361 ms                                                                | 360 ms: 1.00x faster                                                            |
| pyflate                 | 458 ms                                                                | 457 ms: 1.00x faster                                                            |
| pidigits                | 187 ms                                                                | 187 ms: 1.00x slower                                                            |
| async_generators        | 438 ms                                                                | 440 ms: 1.00x slower                                                            |
| sympy_integrate         | 19.7 ms                                                               | 19.8 ms: 1.00x slower                                                           |
| python_startup          | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                           |
| crypto_pyaes            | 72.9 ms                                                               | 73.2 ms: 1.00x slower                                                           |
| chaos                   | 60.6 ms                                                               | 60.9 ms: 1.01x slower                                                           |
| python_startup_no_site  | 6.99 ms                                                               | 7.03 ms: 1.01x slower                                                           |
| asyncio_tcp             | 478 ms                                                                | 480 ms: 1.01x slower                                                            |
| json_loads              | 26.7 us                                                               | 26.8 us: 1.01x slower                                                           |
| comprehensions          | 16.6 us                                                               | 16.7 us: 1.01x slower                                                           |
| deepcopy_reduce         | 2.68 us                                                               | 2.70 us: 1.01x slower                                                           |
| deepcopy_memo           | 31.0 us                                                               | 31.2 us: 1.01x slower                                                           |
| create_gc_cycles        | 1.78 ms                                                               | 1.79 ms: 1.01x slower                                                           |
| sympy_str               | 266 ms                                                                | 268 ms: 1.01x slower                                                            |
| scimark_sor             | 126 ms                                                                | 127 ms: 1.01x slower                                                            |
| sympy_expand            | 454 ms                                                                | 458 ms: 1.01x slower                                                            |
| hexiom                  | 6.26 ms                                                               | 6.31 ms: 1.01x slower                                                           |
| sympy_sum               | 146 ms                                                                | 148 ms: 1.01x slower                                                            |
| regex_compile           | 127 ms                                                                | 129 ms: 1.01x slower                                                            |
| scimark_sparse_mat_mult | 4.63 ms                                                               | 4.70 ms: 1.02x slower                                                           |
| telco                   | 7.85 ms                                                               | 7.98 ms: 1.02x slower                                                           |
| logging_simple          | 5.45 us                                                               | 5.55 us: 1.02x slower                                                           |
| pickle                  | 11.7 us                                                               | 11.9 us: 1.02x slower                                                           |
| genshi_text             | 22.3 ms                                                               | 22.8 ms: 1.02x slower                                                           |
| pycparser               | 1.14 sec                                                              | 1.17 sec: 1.02x slower                                                          |
| genshi_xml              | 48.8 ms                                                               | 50.0 ms: 1.02x slower                                                           |
| coroutines              | 23.2 ms                                                               | 24.0 ms: 1.04x slower                                                           |
| spectral_norm           | 113 ms                                                                | 117 ms: 1.04x slower                                                            |
| logging_format          | 6.01 us                                                               | 6.25 us: 1.04x slower                                                           |
| generators              | 26.7 ms                                                               | 27.8 ms: 1.04x slower                                                           |
| pickle_dict             | 33.4 us                                                               | 35.0 us: 1.05x slower                                                           |
| gc_traversal            | 3.79 ms                                                               | 4.02 ms: 1.06x slower                                                           |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (26): tomli_loads, asyncio_websockets, fannkuch, json, sqlglot_parse, xml_etree_parse, nqueens, bpe_tokeniser, thrift, unpickle_pure_python, 2to3, coverage, typing_runtime_protocols, sqlglot_normalize, sqlglot_optimize, deepcopy, dulwich_log, asyncio_tcp_ssl, pprint_pformat, tornado_http, bench_mp_pool, pprint_safe_repr, scimark_lu, pylint, sqlite_synth, unpickle

- Geometric mean (including insignificant results): 1.000x faster
# HPT report

- Reliability score: 77.15% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x
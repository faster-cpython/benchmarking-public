# Results vs. base

- fork: brandtbucher
- ref: deopt_tracing_16
- machine: linux-x86_64
- commit hash: 124d124
- commit date: 2024-09-12
- overall geometric mean: 1.01x slower
- HPT reliability: 88.14%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 283 ms: 1.02x slower                                                    |
| docutils       | 2.96 sec                                                              | 2.97 sec: 1.00x slower                                                  |
| html5lib       | 64.5 ms                                                               | 65.1 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_generators | 461 ms                                                                | 455 ms: 1.01x faster                                                    |
| coroutines       | 22.9 ms                                                               | 22.7 ms: 1.01x faster                                                   |
| async_tree_io    | 857 ms                                                                | 885 ms: 1.03x slower                                                    |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (10): async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none_tg, asyncio_websockets, async_tree_memoization_tg, asyncio_tcp_ssl, asyncio_tcp, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 70.0 ms                                                               | 69.4 ms: 1.01x faster                                                   |
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                                    |
| nbody          | 80.2 ms                                                               | 81.1 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 24.7 ms                                                               | 24.0 ms: 1.03x faster                                                   |
| regex_effbot   | 3.80 ms                                                               | 3.78 ms: 1.00x faster                                                   |
| regex_compile  | 141 ms                                                                | 144 ms: 1.02x slower                                                    |
| regex_dna      | 216 ms                                                                | 221 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_dict          | 34.5 us                                                               | 33.8 us: 1.02x faster                                                   |
| xml_etree_process    | 55.6 ms                                                               | 54.5 ms: 1.02x faster                                                   |
| pickle_list          | 5.17 us                                                               | 5.08 us: 1.02x faster                                                   |
| xml_etree_generate   | 78.7 ms                                                               | 77.6 ms: 1.01x faster                                                   |
| unpickle_list        | 5.17 us                                                               | 5.12 us: 1.01x faster                                                   |
| unpickle_pure_python | 216 us                                                                | 217 us: 1.00x slower                                                    |
| tomli_loads          | 1.93 sec                                                              | 1.94 sec: 1.00x slower                                                  |
| xml_etree_iterparse  | 97.9 ms                                                               | 98.7 ms: 1.01x slower                                                   |
| pickle               | 11.6 us                                                               | 11.8 us: 1.02x slower                                                   |
| pickle_pure_python   | 305 us                                                                | 313 us: 1.03x slower                                                    |
| json_loads           | 26.7 us                                                               | 27.4 us: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (3): json_dumps, xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.01x faster                                                   |
| python_startup_no_site | 7.07 ms                                                               | 7.02 ms: 1.01x faster                                                   |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 9.88 ms                                                               | 9.71 ms: 1.02x faster                                                   |
| genshi_text     | 25.4 ms                                                               | 25.7 ms: 1.01x slower                                                   |
| django_template | 35.3 ms                                                               | 37.4 ms: 1.06x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal            | 3.94 ms                                                               | 3.53 ms: 1.12x faster                                                   |
| mdp                     | 2.66 sec                                                              | 2.54 sec: 1.05x faster                                                  |
| logging_simple          | 5.75 us                                                               | 5.52 us: 1.04x faster                                                   |
| logging_format          | 6.24 us                                                               | 6.05 us: 1.03x faster                                                   |
| pprint_pformat          | 1.60 sec                                                              | 1.55 sec: 1.03x faster                                                  |
| regex_v8                | 24.7 ms                                                               | 24.0 ms: 1.03x faster                                                   |
| pyflate                 | 448 ms                                                                | 437 ms: 1.03x faster                                                    |
| telco                   | 8.05 ms                                                               | 7.86 ms: 1.02x faster                                                   |
| pickle_dict             | 34.5 us                                                               | 33.8 us: 1.02x faster                                                   |
| xml_etree_process       | 55.6 ms                                                               | 54.5 ms: 1.02x faster                                                   |
| unpack_sequence         | 112 ns                                                                | 110 ns: 1.02x faster                                                    |
| pickle_list             | 5.17 us                                                               | 5.08 us: 1.02x faster                                                   |
| mako                    | 9.88 ms                                                               | 9.71 ms: 1.02x faster                                                   |
| logging_silent          | 104 ns                                                                | 102 ns: 1.02x faster                                                    |
| xml_etree_generate      | 78.7 ms                                                               | 77.6 ms: 1.01x faster                                                   |
| meteor_contest          | 107 ms                                                                | 105 ms: 1.01x faster                                                    |
| scimark_lu              | 110 ms                                                                | 109 ms: 1.01x faster                                                    |
| async_generators        | 461 ms                                                                | 455 ms: 1.01x faster                                                    |
| deepcopy_reduce         | 2.68 us                                                               | 2.65 us: 1.01x faster                                                   |
| float                   | 70.0 ms                                                               | 69.4 ms: 1.01x faster                                                   |
| unpickle_list           | 5.17 us                                                               | 5.12 us: 1.01x faster                                                   |
| coroutines              | 22.9 ms                                                               | 22.7 ms: 1.01x faster                                                   |
| python_startup          | 10.5 ms                                                               | 10.5 ms: 1.01x faster                                                   |
| scimark_fft             | 308 ms                                                                | 306 ms: 1.01x faster                                                    |
| bench_thread_pool       | 839 us                                                                | 833 us: 1.01x faster                                                    |
| coverage                | 85.2 ms                                                               | 84.6 ms: 1.01x faster                                                   |
| python_startup_no_site  | 7.07 ms                                                               | 7.02 ms: 1.01x faster                                                   |
| regex_effbot            | 3.80 ms                                                               | 3.78 ms: 1.00x faster                                                   |
| pidigits                | 185 ms                                                                | 186 ms: 1.00x slower                                                    |
| unpickle_pure_python    | 216 us                                                                | 217 us: 1.00x slower                                                    |
| tomli_loads             | 1.93 sec                                                              | 1.94 sec: 1.00x slower                                                  |
| docutils                | 2.96 sec                                                              | 2.97 sec: 1.00x slower                                                  |
| xml_etree_iterparse     | 97.9 ms                                                               | 98.7 ms: 1.01x slower                                                   |
| html5lib                | 64.5 ms                                                               | 65.1 ms: 1.01x slower                                                   |
| create_gc_cycles        | 1.74 ms                                                               | 1.76 ms: 1.01x slower                                                   |
| nbody                   | 80.2 ms                                                               | 81.1 ms: 1.01x slower                                                   |
| sqlglot_transpile       | 1.69 ms                                                               | 1.71 ms: 1.01x slower                                                   |
| genshi_text             | 25.4 ms                                                               | 25.7 ms: 1.01x slower                                                   |
| sqlglot_parse           | 1.35 ms                                                               | 1.37 ms: 1.01x slower                                                   |
| sqlglot_optimize        | 58.2 ms                                                               | 59.1 ms: 1.01x slower                                                   |
| pickle                  | 11.6 us                                                               | 11.8 us: 1.02x slower                                                   |
| hexiom                  | 6.86 ms                                                               | 7.00 ms: 1.02x slower                                                   |
| raytrace                | 281 ms                                                                | 286 ms: 1.02x slower                                                    |
| regex_compile           | 141 ms                                                                | 144 ms: 1.02x slower                                                    |
| 2to3                    | 276 ms                                                                | 283 ms: 1.02x slower                                                    |
| generators              | 32.8 ms                                                               | 33.6 ms: 1.02x slower                                                   |
| regex_dna               | 216 ms                                                                | 221 ms: 1.02x slower                                                    |
| sympy_integrate         | 22.8 ms                                                               | 23.4 ms: 1.02x slower                                                   |
| pickle_pure_python      | 305 us                                                                | 313 us: 1.03x slower                                                    |
| sympy_sum               | 173 ms                                                                | 177 ms: 1.03x slower                                                    |
| json_loads              | 26.7 us                                                               | 27.4 us: 1.03x slower                                                   |
| sympy_str               | 299 ms                                                                | 307 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult | 4.21 ms                                                               | 4.33 ms: 1.03x slower                                                   |
| sympy_expand            | 506 ms                                                                | 521 ms: 1.03x slower                                                    |
| pycparser               | 1.15 sec                                                              | 1.19 sec: 1.03x slower                                                  |
| async_tree_io           | 857 ms                                                                | 885 ms: 1.03x slower                                                    |
| spectral_norm           | 98.4 ms                                                               | 102 ms: 1.04x slower                                                    |
| deepcopy                | 258 us                                                                | 268 us: 1.04x slower                                                    |
| json                    | 4.94 ms                                                               | 5.14 ms: 1.04x slower                                                   |
| go                      | 131 ms                                                                | 137 ms: 1.05x slower                                                    |
| django_template         | 35.3 ms                                                               | 37.4 ms: 1.06x slower                                                   |
| sqlglot_normalize       | 113 ms                                                                | 122 ms: 1.08x slower                                                    |
| richards_super          | 45.6 ms                                                               | 51.1 ms: 1.12x slower                                                   |
| deltablue               | 3.21 ms                                                               | 3.66 ms: 1.14x slower                                                   |
| richards                | 39.9 ms                                                               | 46.7 ms: 1.17x slower                                                   |
| Geometric mean          | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (32): async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization, typing_runtime_protocols, async_tree_cpu_io_mixed_tg, deepcopy_memo, pprint_safe_repr, genshi_xml, async_tree_none_tg, scimark_sor, json_dumps, bpe_tokeniser, xml_etree_parse, asyncio_websockets, async_tree_memoization_tg, fannkuch, bench_mp_pool, asyncio_tcp_ssl, asyncio_tcp, thrift, scimark_monte_carlo, tornado_http, sqlite_synth, crypto_pyaes, pathlib, dulwich_log, async_tree_io_tg, comprehensions, chaos, nqueens, unpickle, pylint

# HPT report

- Reliability score: 88.14% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x
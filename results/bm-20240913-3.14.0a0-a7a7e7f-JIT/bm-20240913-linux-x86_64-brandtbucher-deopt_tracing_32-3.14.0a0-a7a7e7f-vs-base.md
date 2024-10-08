# Results vs. base

- fork: brandtbucher
- ref: deopt_tracing_32
- machine: linux-x86_64
- commit hash: a7a7e7f
- commit date: 2024-09-13
- overall geometric mean: 1.00x slower
- HPT reliability: 52.37%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 279 ms: 1.01x slower                                                    |
| html5lib       | 64.5 ms                                                               | 64.7 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 555 ms                                                                | 547 ms: 1.02x faster                                                    |
| async_generators           | 461 ms                                                                | 455 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl            | 1.81 sec                                                              | 1.80 sec: 1.00x faster                                                  |
| coroutines                 | 22.9 ms                                                               | 24.9 ms: 1.09x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (9): async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg, async_tree_io, async_tree_memoization_tg, asyncio_tcp, async_tree_io_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 70.0 ms                                                               | 69.4 ms: 1.01x faster                                                   |
| nbody          | 80.2 ms                                                               | 81.9 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.80 ms                                                               | 3.73 ms: 1.02x faster                                                   |
| regex_compile  | 141 ms                                                                | 142 ms: 1.00x slower                                                    |
| regex_v8       | 24.7 ms                                                               | 25.1 ms: 1.02x slower                                                   |
| regex_dna      | 216 ms                                                                | 221 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_dict          | 34.5 us                                                               | 33.2 us: 1.04x faster                                                   |
| pickle_list          | 5.17 us                                                               | 5.04 us: 1.03x faster                                                   |
| pickle               | 11.6 us                                                               | 11.3 us: 1.02x faster                                                   |
| xml_etree_process    | 55.6 ms                                                               | 54.7 ms: 1.02x faster                                                   |
| xml_etree_generate   | 78.7 ms                                                               | 77.5 ms: 1.02x faster                                                   |
| unpickle_pure_python | 216 us                                                                | 213 us: 1.01x faster                                                    |
| tomli_loads          | 1.93 sec                                                              | 1.92 sec: 1.01x faster                                                  |
| xml_etree_parse      | 145 ms                                                                | 147 ms: 1.01x slower                                                    |
| json_loads           | 26.7 us                                                               | 27.1 us: 1.02x slower                                                   |
| xml_etree_iterparse  | 97.9 ms                                                               | 99.7 ms: 1.02x slower                                                   |
| unpickle_list        | 5.17 us                                                               | 5.30 us: 1.03x slower                                                   |
| unpickle             | 14.6 us                                                               | 15.2 us: 1.04x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (2): json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 7.07 ms                                                               | 7.08 ms: 1.00x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 25.4 ms                                                               | 25.1 ms: 1.01x faster                                                   |
| genshi_xml      | 60.0 ms                                                               | 59.4 ms: 1.01x faster                                                   |
| mako            | 9.88 ms                                                               | 9.79 ms: 1.01x faster                                                   |
| django_template | 35.3 ms                                                               | 35.8 ms: 1.01x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pprint_pformat             | 1.60 sec                                                              | 1.48 sec: 1.08x faster                                                  |
| gc_traversal               | 3.94 ms                                                               | 3.65 ms: 1.08x faster                                                   |
| mdp                        | 2.66 sec                                                              | 2.52 sec: 1.05x faster                                                  |
| pprint_safe_repr           | 748 ms                                                                | 720 ms: 1.04x faster                                                    |
| pickle_dict                | 34.5 us                                                               | 33.2 us: 1.04x faster                                                   |
| logging_simple             | 5.75 us                                                               | 5.58 us: 1.03x faster                                                   |
| typing_runtime_protocols   | 166 us                                                                | 161 us: 1.03x faster                                                    |
| pickle_list                | 5.17 us                                                               | 5.04 us: 1.03x faster                                                   |
| logging_format             | 6.24 us                                                               | 6.10 us: 1.02x faster                                                   |
| deepcopy_reduce            | 2.68 us                                                               | 2.62 us: 1.02x faster                                                   |
| logging_silent             | 104 ns                                                                | 102 ns: 1.02x faster                                                    |
| pickle                     | 11.6 us                                                               | 11.3 us: 1.02x faster                                                   |
| raytrace                   | 281 ms                                                                | 276 ms: 1.02x faster                                                    |
| regex_effbot               | 3.80 ms                                                               | 3.73 ms: 1.02x faster                                                   |
| unpack_sequence            | 112 ns                                                                | 110 ns: 1.02x faster                                                    |
| xml_etree_process          | 55.6 ms                                                               | 54.7 ms: 1.02x faster                                                   |
| dulwich_log                | 67.8 ms                                                               | 66.7 ms: 1.02x faster                                                   |
| xml_etree_generate         | 78.7 ms                                                               | 77.5 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed_tg | 555 ms                                                                | 547 ms: 1.02x faster                                                    |
| telco                      | 8.05 ms                                                               | 7.93 ms: 1.01x faster                                                   |
| unpickle_pure_python       | 216 us                                                                | 213 us: 1.01x faster                                                    |
| comprehensions             | 16.6 us                                                               | 16.4 us: 1.01x faster                                                   |
| async_generators           | 461 ms                                                                | 455 ms: 1.01x faster                                                    |
| genshi_text                | 25.4 ms                                                               | 25.1 ms: 1.01x faster                                                   |
| genshi_xml                 | 60.0 ms                                                               | 59.4 ms: 1.01x faster                                                   |
| mako                       | 9.88 ms                                                               | 9.79 ms: 1.01x faster                                                   |
| float                      | 70.0 ms                                                               | 69.4 ms: 1.01x faster                                                   |
| tomli_loads                | 1.93 sec                                                              | 1.92 sec: 1.01x faster                                                  |
| deepcopy_memo              | 27.2 us                                                               | 27.0 us: 1.01x faster                                                   |
| crypto_pyaes               | 65.8 ms                                                               | 65.3 ms: 1.01x faster                                                   |
| bench_thread_pool          | 839 us                                                                | 835 us: 1.00x faster                                                    |
| scimark_sor                | 117 ms                                                                | 117 ms: 1.00x faster                                                    |
| asyncio_tcp_ssl            | 1.81 sec                                                              | 1.80 sec: 1.00x faster                                                  |
| python_startup_no_site     | 7.07 ms                                                               | 7.08 ms: 1.00x slower                                                   |
| regex_compile              | 141 ms                                                                | 142 ms: 1.00x slower                                                    |
| html5lib                   | 64.5 ms                                                               | 64.7 ms: 1.00x slower                                                   |
| hexiom                     | 6.86 ms                                                               | 6.89 ms: 1.00x slower                                                   |
| sympy_integrate            | 22.8 ms                                                               | 23.0 ms: 1.01x slower                                                   |
| scimark_lu                 | 110 ms                                                                | 111 ms: 1.01x slower                                                    |
| sympy_sum                  | 173 ms                                                                | 174 ms: 1.01x slower                                                    |
| 2to3                       | 276 ms                                                                | 279 ms: 1.01x slower                                                    |
| chaos                      | 58.0 ms                                                               | 58.5 ms: 1.01x slower                                                   |
| sqlite_synth               | 2.74 us                                                               | 2.77 us: 1.01x slower                                                   |
| generators                 | 32.8 ms                                                               | 33.2 ms: 1.01x slower                                                   |
| sqlglot_normalize          | 113 ms                                                                | 115 ms: 1.01x slower                                                    |
| pathlib                    | 15.9 ms                                                               | 16.1 ms: 1.01x slower                                                   |
| sqlglot_transpile          | 1.69 ms                                                               | 1.72 ms: 1.01x slower                                                   |
| xml_etree_parse            | 145 ms                                                                | 147 ms: 1.01x slower                                                    |
| fannkuch                   | 375 ms                                                                | 380 ms: 1.01x slower                                                    |
| sqlglot_optimize           | 58.2 ms                                                               | 59.0 ms: 1.01x slower                                                   |
| django_template            | 35.3 ms                                                               | 35.8 ms: 1.01x slower                                                   |
| json_loads                 | 26.7 us                                                               | 27.1 us: 1.02x slower                                                   |
| regex_v8                   | 24.7 ms                                                               | 25.1 ms: 1.02x slower                                                   |
| xml_etree_iterparse        | 97.9 ms                                                               | 99.7 ms: 1.02x slower                                                   |
| create_gc_cycles           | 1.74 ms                                                               | 1.77 ms: 1.02x slower                                                   |
| spectral_norm              | 98.4 ms                                                               | 100 ms: 1.02x slower                                                    |
| sympy_str                  | 299 ms                                                                | 305 ms: 1.02x slower                                                    |
| sympy_expand               | 506 ms                                                                | 517 ms: 1.02x slower                                                    |
| nbody                      | 80.2 ms                                                               | 81.9 ms: 1.02x slower                                                   |
| pyflate                    | 448 ms                                                                | 458 ms: 1.02x slower                                                    |
| regex_dna                  | 216 ms                                                                | 221 ms: 1.02x slower                                                    |
| deepcopy                   | 258 us                                                                | 264 us: 1.02x slower                                                    |
| unpickle_list              | 5.17 us                                                               | 5.30 us: 1.03x slower                                                   |
| richards                   | 39.9 ms                                                               | 41.1 ms: 1.03x slower                                                   |
| go                         | 131 ms                                                                | 135 ms: 1.03x slower                                                    |
| richards_super             | 45.6 ms                                                               | 47.3 ms: 1.04x slower                                                   |
| unpickle                   | 14.6 us                                                               | 15.2 us: 1.04x slower                                                   |
| coverage                   | 85.2 ms                                                               | 89.6 ms: 1.05x slower                                                   |
| pycparser                  | 1.15 sec                                                              | 1.21 sec: 1.05x slower                                                  |
| coroutines                 | 22.9 ms                                                               | 24.9 ms: 1.09x slower                                                   |
| deltablue                  | 3.21 ms                                                               | 3.55 ms: 1.11x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (26): async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization, nqueens, async_tree_none_tg, json_dumps, pickle_pure_python, async_tree_io, scimark_monte_carlo, meteor_contest, async_tree_memoization_tg, scimark_fft, sqlglot_parse, docutils, thrift, scimark_sparse_mat_mult, asyncio_tcp, python_startup, pidigits, bench_mp_pool, tornado_http, async_tree_io_tg, asyncio_websockets, json, bpe_tokeniser, pylint

# HPT report

- Reliability score: 52.37% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x
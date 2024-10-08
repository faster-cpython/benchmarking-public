# Results vs. base

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: cae9e43
- commit date: 2024-09-19
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 277 ms: 1.00x slower                                                        |
| docutils       | 2.96 sec                                                              | 2.92 sec: 1.01x faster                                                      |
| tornado_http   | 94.6 ms                                                               | 94.0 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 575 ms                                                                | 536 ms: 1.07x faster                                                        |
| async_tree_memoization     | 401 ms                                                                | 380 ms: 1.05x faster                                                        |
| async_tree_memoization_tg  | 388 ms                                                                | 371 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 555 ms                                                                | 540 ms: 1.03x faster                                                        |
| async_generators           | 461 ms                                                                | 458 ms: 1.01x faster                                                        |
| asyncio_tcp                | 498 ms                                                                | 499 ms: 1.00x slower                                                        |
| coroutines                 | 22.9 ms                                                               | 23.1 ms: 1.01x slower                                                       |
| async_tree_io              | 857 ms                                                                | 929 ms: 1.08x slower                                                        |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_none, asyncio_websockets, asyncio_tcp_ssl, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                                        |
| nbody          | 80.2 ms                                                               | 80.5 ms: 1.00x slower                                                       |
| float          | 70.0 ms                                                               | 70.4 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.80 ms                                                               | 3.63 ms: 1.05x faster                                                       |
| regex_compile  | 141 ms                                                                | 137 ms: 1.03x faster                                                        |
| regex_v8       | 24.7 ms                                                               | 24.0 ms: 1.03x faster                                                       |
| regex_dna      | 216 ms                                                                | 215 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 34.5 us                                                               | 32.9 us: 1.05x faster                                                       |
| xml_etree_process    | 55.6 ms                                                               | 53.7 ms: 1.04x faster                                                       |
| xml_etree_generate   | 78.7 ms                                                               | 76.0 ms: 1.04x faster                                                       |
| unpickle_pure_python | 216 us                                                                | 213 us: 1.01x faster                                                        |
| pickle_pure_python   | 305 us                                                                | 302 us: 1.01x faster                                                        |
| tomli_loads          | 1.93 sec                                                              | 1.91 sec: 1.01x faster                                                      |
| xml_etree_iterparse  | 97.9 ms                                                               | 97.4 ms: 1.00x faster                                                       |
| pickle               | 11.6 us                                                               | 11.5 us: 1.00x faster                                                       |
| unpickle_list        | 5.17 us                                                               | 5.19 us: 1.00x slower                                                       |
| json_loads           | 26.7 us                                                               | 27.2 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (4): pickle_list, json_dumps, xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                       |
| python_startup_no_site | 7.07 ms                                                               | 7.07 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 60.0 ms                                                               | 56.4 ms: 1.06x faster                                                       |
| genshi_text     | 25.4 ms                                                               | 24.4 ms: 1.04x faster                                                       |
| mako            | 9.88 ms                                                               | 9.72 ms: 1.02x faster                                                       |
| django_template | 35.3 ms                                                               | 36.0 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.03x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pprint_pformat             | 1.60 sec                                                              | 1.49 sec: 1.08x faster                                                      |
| async_tree_cpu_io_mixed    | 575 ms                                                                | 536 ms: 1.07x faster                                                        |
| genshi_xml                 | 60.0 ms                                                               | 56.4 ms: 1.06x faster                                                       |
| gc_traversal               | 3.94 ms                                                               | 3.72 ms: 1.06x faster                                                       |
| async_tree_memoization     | 401 ms                                                                | 380 ms: 1.05x faster                                                        |
| mdp                        | 2.66 sec                                                              | 2.52 sec: 1.05x faster                                                      |
| pickle_dict                | 34.5 us                                                               | 32.9 us: 1.05x faster                                                       |
| async_tree_memoization_tg  | 388 ms                                                                | 371 ms: 1.05x faster                                                        |
| go                         | 131 ms                                                                | 125 ms: 1.05x faster                                                        |
| regex_effbot               | 3.80 ms                                                               | 3.63 ms: 1.05x faster                                                       |
| genshi_text                | 25.4 ms                                                               | 24.4 ms: 1.04x faster                                                       |
| typing_runtime_protocols   | 166 us                                                                | 160 us: 1.04x faster                                                        |
| xml_etree_process          | 55.6 ms                                                               | 53.7 ms: 1.04x faster                                                       |
| pprint_safe_repr           | 748 ms                                                                | 722 ms: 1.04x faster                                                        |
| xml_etree_generate         | 78.7 ms                                                               | 76.0 ms: 1.04x faster                                                       |
| unpack_sequence            | 112 ns                                                                | 109 ns: 1.03x faster                                                        |
| logging_simple             | 5.75 us                                                               | 5.57 us: 1.03x faster                                                       |
| sqlglot_normalize          | 113 ms                                                                | 110 ms: 1.03x faster                                                        |
| regex_compile              | 141 ms                                                                | 137 ms: 1.03x faster                                                        |
| sqlglot_optimize           | 58.2 ms                                                               | 56.5 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 555 ms                                                                | 540 ms: 1.03x faster                                                        |
| regex_v8                   | 24.7 ms                                                               | 24.0 ms: 1.03x faster                                                       |
| sqlglot_parse              | 1.35 ms                                                               | 1.32 ms: 1.02x faster                                                       |
| deltablue                  | 3.21 ms                                                               | 3.14 ms: 1.02x faster                                                       |
| deepcopy_memo              | 27.2 us                                                               | 26.7 us: 1.02x faster                                                       |
| raytrace                   | 281 ms                                                                | 275 ms: 1.02x faster                                                        |
| mako                       | 9.88 ms                                                               | 9.72 ms: 1.02x faster                                                       |
| logging_format             | 6.24 us                                                               | 6.14 us: 1.02x faster                                                       |
| deepcopy                   | 258 us                                                                | 254 us: 1.02x faster                                                        |
| generators                 | 32.8 ms                                                               | 32.4 ms: 1.01x faster                                                       |
| bpe_tokeniser              | 4.44 sec                                                              | 4.38 sec: 1.01x faster                                                      |
| pathlib                    | 15.9 ms                                                               | 15.7 ms: 1.01x faster                                                       |
| telco                      | 8.05 ms                                                               | 7.95 ms: 1.01x faster                                                       |
| unpickle_pure_python       | 216 us                                                                | 213 us: 1.01x faster                                                        |
| docutils                   | 2.96 sec                                                              | 2.92 sec: 1.01x faster                                                      |
| pickle_pure_python         | 305 us                                                                | 302 us: 1.01x faster                                                        |
| tomli_loads                | 1.93 sec                                                              | 1.91 sec: 1.01x faster                                                      |
| sympy_sum                  | 173 ms                                                                | 171 ms: 1.01x faster                                                        |
| sympy_expand               | 506 ms                                                                | 502 ms: 1.01x faster                                                        |
| dulwich_log                | 67.8 ms                                                               | 67.3 ms: 1.01x faster                                                       |
| logging_silent             | 104 ns                                                                | 103 ns: 1.01x faster                                                        |
| async_generators           | 461 ms                                                                | 458 ms: 1.01x faster                                                        |
| sympy_str                  | 299 ms                                                                | 297 ms: 1.01x faster                                                        |
| tornado_http               | 94.6 ms                                                               | 94.0 ms: 1.01x faster                                                       |
| coverage                   | 85.2 ms                                                               | 84.7 ms: 1.01x faster                                                       |
| sympy_integrate            | 22.8 ms                                                               | 22.7 ms: 1.01x faster                                                       |
| xml_etree_iterparse        | 97.9 ms                                                               | 97.4 ms: 1.00x faster                                                       |
| pickle                     | 11.6 us                                                               | 11.5 us: 1.00x faster                                                       |
| bench_thread_pool          | 839 us                                                                | 837 us: 1.00x faster                                                        |
| regex_dna                  | 216 ms                                                                | 215 ms: 1.00x faster                                                        |
| python_startup             | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                       |
| python_startup_no_site     | 7.07 ms                                                               | 7.07 ms: 1.00x slower                                                       |
| pidigits                   | 185 ms                                                                | 186 ms: 1.00x slower                                                        |
| 2to3                       | 276 ms                                                                | 277 ms: 1.00x slower                                                        |
| asyncio_tcp                | 498 ms                                                                | 499 ms: 1.00x slower                                                        |
| nbody                      | 80.2 ms                                                               | 80.5 ms: 1.00x slower                                                       |
| unpickle_list              | 5.17 us                                                               | 5.19 us: 1.00x slower                                                       |
| float                      | 70.0 ms                                                               | 70.4 ms: 1.01x slower                                                       |
| coroutines                 | 22.9 ms                                                               | 23.1 ms: 1.01x slower                                                       |
| fannkuch                   | 375 ms                                                                | 380 ms: 1.01x slower                                                        |
| nqueens                    | 85.5 ms                                                               | 86.8 ms: 1.02x slower                                                       |
| spectral_norm              | 98.4 ms                                                               | 100 ms: 1.02x slower                                                        |
| django_template            | 35.3 ms                                                               | 36.0 ms: 1.02x slower                                                       |
| pyflate                    | 448 ms                                                                | 457 ms: 1.02x slower                                                        |
| richards                   | 39.9 ms                                                               | 40.7 ms: 1.02x slower                                                       |
| json_loads                 | 26.7 us                                                               | 27.2 us: 1.02x slower                                                       |
| json                       | 4.94 ms                                                               | 5.09 ms: 1.03x slower                                                       |
| async_tree_io              | 857 ms                                                                | 929 ms: 1.08x slower                                                        |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (27): pylint, async_tree_none_tg, scimark_fft, scimark_monte_carlo, thrift, sqlite_synth, scimark_sor, comprehensions, scimark_lu, deepcopy_reduce, async_tree_none, create_gc_cycles, asyncio_websockets, bench_mp_pool, hexiom, asyncio_tcp_ssl, scimark_sparse_mat_mult, pickle_list, meteor_contest, richards_super, sqlglot_transpile, crypto_pyaes, json_dumps, chaos, async_tree_io_tg, xml_etree_parse, unpickle
Ignored benchmarks (2) of results/bm-20240912-3.14.0a0-6e06e01-JIT/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: html5lib, pycparser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x
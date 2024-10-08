# Results vs. base

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.01x slower
- HPT reliability: 80.86%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 253 ms                                                                | 255 ms: 1.01x slower                                         |
| docutils       | 2.66 sec                                                              | 2.65 sec: 1.00x faster                                       |
| html5lib       | 62.4 ms                                                               | 63.8 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 558 ms                                                                | 552 ms: 1.01x faster                                         |
| async_generators           | 437 ms                                                                | 434 ms: 1.01x faster                                         |
| asyncio_websockets         | 559 ms                                                                | 555 ms: 1.01x faster                                         |
| asyncio_tcp                | 471 ms                                                                | 468 ms: 1.01x faster                                         |
| asyncio_tcp_ssl            | 1.78 sec                                                              | 1.78 sec: 1.00x faster                                       |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                 |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_none, coroutines, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 89.5 ms                                                               | 87.1 ms: 1.03x faster                                        |
| float          | 76.7 ms                                                               | 76.3 ms: 1.00x faster                                        |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                | 129 ms: 1.00x slower                                         |
| regex_effbot   | 3.65 ms                                                               | 3.70 ms: 1.01x slower                                        |
| regex_v8       | 24.6 ms                                                               | 25.0 ms: 1.02x slower                                        |
| regex_dna      | 216 ms                                                                | 221 ms: 1.02x slower                                         |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_generate   | 85.4 ms                                                               | 84.7 ms: 1.01x faster                                        |
| unpickle_pure_python | 213 us                                                                | 215 us: 1.01x slower                                         |
| pickle               | 11.4 us                                                               | 11.6 us: 1.01x slower                                        |
| json_loads           | 27.0 us                                                               | 27.5 us: 1.02x slower                                        |
| json_dumps           | 10.3 ms                                                               | 10.6 ms: 1.02x slower                                        |
| tomli_loads          | 2.04 sec                                                              | 2.11 sec: 1.03x slower                                       |
| pickle_dict          | 33.8 us                                                               | 35.1 us: 1.04x slower                                        |
| pickle_list          | 4.87 us                                                               | 5.12 us: 1.05x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                 |

Benchmark hidden because not significant (6): unpickle_list, pickle_pure_python, xml_etree_process, xml_etree_parse, xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                               | 7.00 ms: 1.00x slower                                        |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 34.6 ms                                                               | 34.1 ms: 1.01x faster                                        |
| mako            | 11.1 ms                                                               | 11.3 ms: 1.02x slower                                        |
| genshi_xml      | 48.6 ms                                                               | 50.0 ms: 1.03x slower                                        |
| genshi_text     | 21.7 ms                                                               | 22.4 ms: 1.04x slower                                        |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pyflate                    | 476 ms                                                                | 460 ms: 1.03x faster                                         |
| nbody                      | 89.5 ms                                                               | 87.1 ms: 1.03x faster                                        |
| generators                 | 28.2 ms                                                               | 27.7 ms: 1.02x faster                                        |
| meteor_contest             | 108 ms                                                                | 106 ms: 1.01x faster                                         |
| sqlglot_normalize          | 108 ms                                                                | 107 ms: 1.01x faster                                         |
| django_template            | 34.6 ms                                                               | 34.1 ms: 1.01x faster                                        |
| async_tree_cpu_io_mixed_tg | 558 ms                                                                | 552 ms: 1.01x faster                                         |
| scimark_lu                 | 113 ms                                                                | 112 ms: 1.01x faster                                         |
| json                       | 5.15 ms                                                               | 5.09 ms: 1.01x faster                                        |
| bpe_tokeniser              | 4.86 sec                                                              | 4.81 sec: 1.01x faster                                       |
| async_generators           | 437 ms                                                                | 434 ms: 1.01x faster                                         |
| pprint_pformat             | 1.47 sec                                                              | 1.46 sec: 1.01x faster                                       |
| xml_etree_generate         | 85.4 ms                                                               | 84.7 ms: 1.01x faster                                        |
| asyncio_websockets         | 559 ms                                                                | 555 ms: 1.01x faster                                         |
| telco                      | 8.46 ms                                                               | 8.40 ms: 1.01x faster                                        |
| asyncio_tcp                | 471 ms                                                                | 468 ms: 1.01x faster                                         |
| coverage                   | 85.7 ms                                                               | 85.2 ms: 1.01x faster                                        |
| gc_traversal               | 3.90 ms                                                               | 3.88 ms: 1.01x faster                                        |
| float                      | 76.7 ms                                                               | 76.3 ms: 1.00x faster                                        |
| docutils                   | 2.66 sec                                                              | 2.65 sec: 1.00x faster                                       |
| pprint_safe_repr           | 714 ms                                                                | 711 ms: 1.00x faster                                         |
| asyncio_tcp_ssl            | 1.78 sec                                                              | 1.78 sec: 1.00x faster                                       |
| python_startup_no_site     | 6.99 ms                                                               | 7.00 ms: 1.00x slower                                        |
| python_startup             | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                        |
| dulwich_log                | 64.5 ms                                                               | 64.7 ms: 1.00x slower                                        |
| regex_compile              | 129 ms                                                                | 129 ms: 1.00x slower                                         |
| sympy_sum                  | 147 ms                                                                | 147 ms: 1.00x slower                                         |
| create_gc_cycles           | 1.73 ms                                                               | 1.74 ms: 1.00x slower                                        |
| sqlglot_optimize           | 53.2 ms                                                               | 53.5 ms: 1.00x slower                                        |
| 2to3                       | 253 ms                                                                | 255 ms: 1.01x slower                                         |
| deepcopy_memo              | 29.5 us                                                               | 29.7 us: 1.01x slower                                        |
| unpickle_pure_python       | 213 us                                                                | 215 us: 1.01x slower                                         |
| chaos                      | 58.3 ms                                                               | 58.8 ms: 1.01x slower                                        |
| logging_format             | 6.12 us                                                               | 6.17 us: 1.01x slower                                        |
| typing_runtime_protocols   | 158 us                                                                | 160 us: 1.01x slower                                         |
| deepcopy                   | 255 us                                                                | 258 us: 1.01x slower                                         |
| raytrace                   | 262 ms                                                                | 264 ms: 1.01x slower                                         |
| sympy_integrate            | 19.5 ms                                                               | 19.7 ms: 1.01x slower                                        |
| nqueens                    | 80.4 ms                                                               | 81.4 ms: 1.01x slower                                        |
| comprehensions             | 16.8 us                                                               | 17.0 us: 1.01x slower                                        |
| pickle                     | 11.4 us                                                               | 11.6 us: 1.01x slower                                        |
| scimark_fft                | 363 ms                                                                | 368 ms: 1.01x slower                                         |
| regex_effbot               | 3.65 ms                                                               | 3.70 ms: 1.01x slower                                        |
| richards                   | 45.8 ms                                                               | 46.4 ms: 1.01x slower                                        |
| mdp                        | 2.69 sec                                                              | 2.73 sec: 1.01x slower                                       |
| regex_v8                   | 24.6 ms                                                               | 25.0 ms: 1.02x slower                                        |
| pathlib                    | 15.9 ms                                                               | 16.1 ms: 1.02x slower                                        |
| hexiom                     | 6.16 ms                                                               | 6.26 ms: 1.02x slower                                        |
| fannkuch                   | 403 ms                                                                | 410 ms: 1.02x slower                                         |
| logging_silent             | 99.9 ns                                                               | 102 ns: 1.02x slower                                         |
| json_loads                 | 27.0 us                                                               | 27.5 us: 1.02x slower                                        |
| regex_dna                  | 216 ms                                                                | 221 ms: 1.02x slower                                         |
| richards_super             | 51.7 ms                                                               | 52.7 ms: 1.02x slower                                        |
| mako                       | 11.1 ms                                                               | 11.3 ms: 1.02x slower                                        |
| html5lib                   | 62.4 ms                                                               | 63.8 ms: 1.02x slower                                        |
| json_dumps                 | 10.3 ms                                                               | 10.6 ms: 1.02x slower                                        |
| deepcopy_reduce            | 2.63 us                                                               | 2.69 us: 1.02x slower                                        |
| scimark_sor                | 122 ms                                                                | 125 ms: 1.03x slower                                         |
| deltablue                  | 3.14 ms                                                               | 3.23 ms: 1.03x slower                                        |
| genshi_xml                 | 48.6 ms                                                               | 50.0 ms: 1.03x slower                                        |
| go                         | 117 ms                                                                | 120 ms: 1.03x slower                                         |
| bench_thread_pool          | 787 us                                                                | 809 us: 1.03x slower                                         |
| logging_simple             | 5.49 us                                                               | 5.65 us: 1.03x slower                                        |
| crypto_pyaes               | 71.1 ms                                                               | 73.2 ms: 1.03x slower                                        |
| tomli_loads                | 2.04 sec                                                              | 2.11 sec: 1.03x slower                                       |
| genshi_text                | 21.7 ms                                                               | 22.4 ms: 1.04x slower                                        |
| pickle_dict                | 33.8 us                                                               | 35.1 us: 1.04x slower                                        |
| spectral_norm              | 113 ms                                                                | 118 ms: 1.04x slower                                         |
| pickle_list                | 4.87 us                                                               | 5.12 us: 1.05x slower                                        |
| scimark_sparse_mat_mult    | 4.60 ms                                                               | 4.96 ms: 1.08x slower                                        |
| unpack_sequence            | 46.3 ns                                                               | 50.3 ns: 1.08x slower                                        |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                 |

Benchmark hidden because not significant (26): async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_none, unpickle_list, pickle_pure_python, xml_etree_process, tornado_http, pidigits, sqlglot_transpile, bench_mp_pool, sympy_expand, sqlglot_parse, xml_etree_parse, pylint, coroutines, thrift, xml_etree_iterparse, scimark_monte_carlo, sympy_str, sqlite_synth, async_tree_io, pycparser, unpickle

# HPT report

- Reliability score: 80.86% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x
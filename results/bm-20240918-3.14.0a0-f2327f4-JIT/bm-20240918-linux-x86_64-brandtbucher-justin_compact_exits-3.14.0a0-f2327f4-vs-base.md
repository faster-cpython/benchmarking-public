# Results vs. base

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: f2327f4
- commit date: 2024-09-18
- overall geometric mean: 1.01x slower
- HPT reliability: 75.53%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 282 ms: 1.02x slower                                                        |
| docutils       | 2.96 sec                                                              | 3.20 sec: 1.08x slower                                                      |
| html5lib       | 64.5 ms                                                               | 66.5 ms: 1.03x slower                                                       |
| tornado_http   | 94.6 ms                                                               | 95.0 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_generators           | 461 ms                                                                | 457 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                      |
| asyncio_tcp                | 498 ms                                                                | 505 ms: 1.01x slower                                                        |
| coroutines                 | 22.9 ms                                                               | 23.2 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed    | 575 ms                                                                | 605 ms: 1.05x slower                                                        |
| async_tree_io              | 857 ms                                                                | 941 ms: 1.10x slower                                                        |
| async_tree_none            | 321 ms                                                                | 360 ms: 1.12x slower                                                        |
| async_tree_memoization     | 401 ms                                                                | 455 ms: 1.14x slower                                                        |
| async_tree_io_tg           | 868 ms                                                                | 1.02 sec: 1.17x slower                                                      |
| async_tree_cpu_io_mixed_tg | 555 ms                                                                | 666 ms: 1.20x slower                                                        |
| async_tree_none_tg         | 309 ms                                                                | 401 ms: 1.30x slower                                                        |
| async_tree_memoization_tg  | 388 ms                                                                | 513 ms: 1.32x slower                                                        |
| Geometric mean             | (ref)                                                                 | 1.10x slower                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 80.2 ms                                                               | 81.1 ms: 1.01x slower                                                       |
| float          | 70.0 ms                                                               | 72.1 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.80 ms                                                               | 3.65 ms: 1.04x faster                                                       |
| regex_compile  | 141 ms                                                                | 138 ms: 1.03x faster                                                        |
| regex_v8       | 24.7 ms                                                               | 25.2 ms: 1.02x slower                                                       |
| regex_dna      | 216 ms                                                                | 221 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 55.6 ms                                                               | 54.2 ms: 1.03x faster                                                       |
| pickle_list          | 5.17 us                                                               | 5.09 us: 1.02x faster                                                       |
| xml_etree_generate   | 78.7 ms                                                               | 77.4 ms: 1.02x faster                                                       |
| unpickle_pure_python | 216 us                                                                | 214 us: 1.01x faster                                                        |
| pickle               | 11.6 us                                                               | 11.5 us: 1.00x faster                                                       |
| json_loads           | 26.7 us                                                               | 27.0 us: 1.01x slower                                                       |
| unpickle             | 14.6 us                                                               | 14.8 us: 1.02x slower                                                       |
| pickle_dict          | 34.5 us                                                               | 35.1 us: 1.02x slower                                                       |
| xml_etree_parse      | 145 ms                                                                | 150 ms: 1.04x slower                                                        |
| unpickle_list        | 5.17 us                                                               | 5.41 us: 1.05x slower                                                       |
| xml_etree_iterparse  | 97.9 ms                                                               | 104 ms: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (3): tomli_loads, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                       |
| python_startup_no_site | 7.07 ms                                                               | 7.09 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 60.0 ms                                                               | 58.8 ms: 1.02x faster                                                       |
| django_template | 35.3 ms                                                               | 35.7 ms: 1.01x slower                                                       |
| mako            | 9.88 ms                                                               | 10.0 ms: 1.01x slower                                                       |
| genshi_text     | 25.4 ms                                                               | 26.0 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pylint                     | 375 ms                                                                | 314 ms: 1.20x faster                                                        |
| pprint_pformat             | 1.60 sec                                                              | 1.46 sec: 1.09x faster                                                      |
| mdp                        | 2.66 sec                                                              | 2.52 sec: 1.05x faster                                                      |
| unpack_sequence            | 112 ns                                                                | 107 ns: 1.05x faster                                                        |
| regex_effbot               | 3.80 ms                                                               | 3.65 ms: 1.04x faster                                                       |
| go                         | 131 ms                                                                | 126 ms: 1.04x faster                                                        |
| pprint_safe_repr           | 748 ms                                                                | 725 ms: 1.03x faster                                                        |
| deepcopy                   | 258 us                                                                | 250 us: 1.03x faster                                                        |
| xml_etree_process          | 55.6 ms                                                               | 54.2 ms: 1.03x faster                                                       |
| regex_compile              | 141 ms                                                                | 138 ms: 1.03x faster                                                        |
| genshi_xml                 | 60.0 ms                                                               | 58.8 ms: 1.02x faster                                                       |
| logging_simple             | 5.75 us                                                               | 5.64 us: 1.02x faster                                                       |
| sqlglot_optimize           | 58.2 ms                                                               | 57.1 ms: 1.02x faster                                                       |
| sqlglot_normalize          | 113 ms                                                                | 111 ms: 1.02x faster                                                        |
| pickle_list                | 5.17 us                                                               | 5.09 us: 1.02x faster                                                       |
| xml_etree_generate         | 78.7 ms                                                               | 77.4 ms: 1.02x faster                                                       |
| raytrace                   | 281 ms                                                                | 277 ms: 1.01x faster                                                        |
| typing_runtime_protocols   | 166 us                                                                | 164 us: 1.01x faster                                                        |
| sympy_str                  | 299 ms                                                                | 296 ms: 1.01x faster                                                        |
| richards                   | 39.9 ms                                                               | 39.5 ms: 1.01x faster                                                       |
| nqueens                    | 85.5 ms                                                               | 84.6 ms: 1.01x faster                                                       |
| sympy_sum                  | 173 ms                                                                | 171 ms: 1.01x faster                                                        |
| async_generators           | 461 ms                                                                | 457 ms: 1.01x faster                                                        |
| pathlib                    | 15.9 ms                                                               | 15.8 ms: 1.01x faster                                                       |
| sympy_expand               | 506 ms                                                                | 503 ms: 1.01x faster                                                        |
| unpickle_pure_python       | 216 us                                                                | 214 us: 1.01x faster                                                        |
| sympy_integrate            | 22.8 ms                                                               | 22.7 ms: 1.01x faster                                                       |
| generators                 | 32.8 ms                                                               | 32.6 ms: 1.01x faster                                                       |
| hexiom                     | 6.86 ms                                                               | 6.83 ms: 1.00x faster                                                       |
| pickle                     | 11.6 us                                                               | 11.5 us: 1.00x faster                                                       |
| bench_thread_pool          | 839 us                                                                | 837 us: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                      |
| python_startup             | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                       |
| python_startup_no_site     | 7.07 ms                                                               | 7.09 ms: 1.00x slower                                                       |
| tornado_http               | 94.6 ms                                                               | 95.0 ms: 1.01x slower                                                       |
| sqlite_synth               | 2.74 us                                                               | 2.76 us: 1.01x slower                                                       |
| pyflate                    | 448 ms                                                                | 452 ms: 1.01x slower                                                        |
| json                       | 4.94 ms                                                               | 4.99 ms: 1.01x slower                                                       |
| nbody                      | 80.2 ms                                                               | 81.1 ms: 1.01x slower                                                       |
| crypto_pyaes               | 65.8 ms                                                               | 66.5 ms: 1.01x slower                                                       |
| django_template            | 35.3 ms                                                               | 35.7 ms: 1.01x slower                                                       |
| mako                       | 9.88 ms                                                               | 10.0 ms: 1.01x slower                                                       |
| logging_silent             | 104 ns                                                                | 105 ns: 1.01x slower                                                        |
| asyncio_tcp                | 498 ms                                                                | 505 ms: 1.01x slower                                                        |
| json_loads                 | 26.7 us                                                               | 27.0 us: 1.01x slower                                                       |
| coroutines                 | 22.9 ms                                                               | 23.2 ms: 1.01x slower                                                       |
| chaos                      | 58.0 ms                                                               | 58.9 ms: 1.02x slower                                                       |
| regex_v8                   | 24.7 ms                                                               | 25.2 ms: 1.02x slower                                                       |
| unpickle                   | 14.6 us                                                               | 14.8 us: 1.02x slower                                                       |
| pickle_dict                | 34.5 us                                                               | 35.1 us: 1.02x slower                                                       |
| create_gc_cycles           | 1.74 ms                                                               | 1.77 ms: 1.02x slower                                                       |
| 2to3                       | 276 ms                                                                | 282 ms: 1.02x slower                                                        |
| genshi_text                | 25.4 ms                                                               | 26.0 ms: 1.02x slower                                                       |
| sqlglot_transpile          | 1.69 ms                                                               | 1.73 ms: 1.02x slower                                                       |
| regex_dna                  | 216 ms                                                                | 221 ms: 1.02x slower                                                        |
| gc_traversal               | 3.94 ms                                                               | 4.04 ms: 1.02x slower                                                       |
| float                      | 70.0 ms                                                               | 72.1 ms: 1.03x slower                                                       |
| html5lib                   | 64.5 ms                                                               | 66.5 ms: 1.03x slower                                                       |
| xml_etree_parse            | 145 ms                                                                | 150 ms: 1.04x slower                                                        |
| unpickle_list              | 5.17 us                                                               | 5.41 us: 1.05x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                               | 4.42 ms: 1.05x slower                                                       |
| pycparser                  | 1.15 sec                                                              | 1.21 sec: 1.05x slower                                                      |
| async_tree_cpu_io_mixed    | 575 ms                                                                | 605 ms: 1.05x slower                                                        |
| bpe_tokeniser              | 4.44 sec                                                              | 4.71 sec: 1.06x slower                                                      |
| xml_etree_iterparse        | 97.9 ms                                                               | 104 ms: 1.06x slower                                                        |
| docutils                   | 2.96 sec                                                              | 3.20 sec: 1.08x slower                                                      |
| async_tree_io              | 857 ms                                                                | 941 ms: 1.10x slower                                                        |
| async_tree_none            | 321 ms                                                                | 360 ms: 1.12x slower                                                        |
| async_tree_memoization     | 401 ms                                                                | 455 ms: 1.14x slower                                                        |
| async_tree_io_tg           | 868 ms                                                                | 1.02 sec: 1.17x slower                                                      |
| async_tree_cpu_io_mixed_tg | 555 ms                                                                | 666 ms: 1.20x slower                                                        |
| async_tree_none_tg         | 309 ms                                                                | 401 ms: 1.30x slower                                                        |
| async_tree_memoization_tg  | 388 ms                                                                | 513 ms: 1.32x slower                                                        |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (24): deepcopy_memo, deepcopy_reduce, logging_format, scimark_monte_carlo, tomli_loads, sqlglot_parse, dulwich_log, pickle_pure_python, pidigits, bench_mp_pool, scimark_fft, richards_super, deltablue, scimark_sor, thrift, asyncio_websockets, spectral_norm, comprehensions, telco, meteor_contest, json_dumps, scimark_lu, fannkuch, coverage

# HPT report

- Reliability score: 75.53% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x
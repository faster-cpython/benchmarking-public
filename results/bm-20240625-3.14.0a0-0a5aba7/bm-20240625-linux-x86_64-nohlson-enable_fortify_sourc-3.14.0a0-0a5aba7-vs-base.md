# Results vs. base

- fork: nohlson
- ref: enable_fortify_sourc
- machine: linux-x86_64
- commit hash: 0a5aba7
- commit date: 2024-06-25
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240625-linux-x86_64-python-a905721b9c5c15279e67-3.14.0a0-a905721 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 264 ms                                                                | 267 ms: 1.01x slower                                                   |
| docutils       | 2.70 sec                                                              | 2.74 sec: 1.01x slower                                                 |
| html5lib       | 64.7 ms                                                               | 66.8 ms: 1.03x slower                                                  |
| tornado_http   | 90.6 ms                                                               | 96.2 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240625-linux-x86_64-python-a905721b9c5c15279e67-3.14.0a0-a905721 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 542 ms                                                                | 548 ms: 1.01x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (7): async_tree_io, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240625-linux-x86_64-python-a905721b9c5c15279e67-3.14.0a0-a905721 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 76.8 ms                                                               | 77.0 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240625-linux-x86_64-python-a905721b9c5c15279e67-3.14.0a0-a905721 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 231 ms                                                                | 219 ms: 1.06x faster                                                   |
| regex_effbot   | 3.78 ms                                                               | 3.69 ms: 1.03x faster                                                  |
| regex_v8       | 26.3 ms                                                               | 25.9 ms: 1.01x faster                                                  |
| regex_compile  | 130 ms                                                                | 133 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240625-linux-x86_64-python-a905721b9c5c15279e67-3.14.0a0-a905721 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                  |
| pickle               | 11.9 us                                                               | 11.9 us: 1.00x faster                                                  |
| json_loads           | 27.5 us                                                               | 27.6 us: 1.00x slower                                                  |
| xml_etree_process    | 60.0 ms                                                               | 60.3 ms: 1.00x slower                                                  |
| pickle_dict          | 34.4 us                                                               | 34.6 us: 1.00x slower                                                  |
| xml_etree_generate   | 85.4 ms                                                               | 86.3 ms: 1.01x slower                                                  |
| pickle_pure_python   | 301 us                                                                | 308 us: 1.02x slower                                                   |
| unpickle_list        | 5.13 us                                                               | 5.27 us: 1.03x slower                                                  |
| unpickle_pure_python | 212 us                                                                | 220 us: 1.04x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (5): unpickle, xml_etree_parse, pickle_list, tomli_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240625-linux-x86_64-python-a905721b9c5c15279e67-3.14.0a0-a905721 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.02 ms                                                               | 7.10 ms: 1.01x slower                                                  |
| python_startup         | 10.5 ms                                                               | 10.7 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240625-linux-x86_64-python-a905721b9c5c15279e67-3.14.0a0-a905721 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.9 ms                                                               | 11.1 ms: 1.01x slower                                                  |
| django_template | 33.7 ms                                                               | 34.5 ms: 1.02x slower                                                  |
| genshi_text     | 22.8 ms                                                               | 23.4 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240625-linux-x86_64-python-a905721b9c5c15279e67-3.14.0a0-a905721 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| scimark_sor                | 131 ms                                                                | 123 ms: 1.07x faster                                                   |
| regex_dna                  | 231 ms                                                                | 219 ms: 1.06x faster                                                   |
| regex_effbot               | 3.78 ms                                                               | 3.69 ms: 1.03x faster                                                  |
| coverage                   | 93.1 ms                                                               | 91.3 ms: 1.02x faster                                                  |
| scimark_lu                 | 112 ms                                                                | 110 ms: 1.02x faster                                                   |
| regex_v8                   | 26.3 ms                                                               | 25.9 ms: 1.01x faster                                                  |
| spectral_norm              | 111 ms                                                                | 110 ms: 1.01x faster                                                   |
| go                         | 143 ms                                                                | 142 ms: 1.01x faster                                                   |
| chaos                      | 59.3 ms                                                               | 58.8 ms: 1.01x faster                                                  |
| json_dumps                 | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                  |
| gc_traversal               | 3.57 ms                                                               | 3.54 ms: 1.01x faster                                                  |
| generators                 | 29.4 ms                                                               | 29.1 ms: 1.01x faster                                                  |
| nqueens                    | 79.7 ms                                                               | 79.1 ms: 1.01x faster                                                  |
| scimark_fft                | 360 ms                                                                | 357 ms: 1.01x faster                                                   |
| comprehensions             | 16.8 us                                                               | 16.7 us: 1.01x faster                                                  |
| create_gc_cycles           | 1.73 ms                                                               | 1.72 ms: 1.01x faster                                                  |
| deepcopy_reduce            | 2.70 us                                                               | 2.68 us: 1.01x faster                                                  |
| raytrace                   | 267 ms                                                                | 266 ms: 1.00x faster                                                   |
| hexiom                     | 6.13 ms                                                               | 6.10 ms: 1.00x faster                                                  |
| pickle                     | 11.9 us                                                               | 11.9 us: 1.00x faster                                                  |
| json_loads                 | 27.5 us                                                               | 27.6 us: 1.00x slower                                                  |
| float                      | 76.8 ms                                                               | 77.0 ms: 1.00x slower                                                  |
| xml_etree_process          | 60.0 ms                                                               | 60.3 ms: 1.00x slower                                                  |
| pickle_dict                | 34.4 us                                                               | 34.6 us: 1.00x slower                                                  |
| asyncio_websockets         | 554 ms                                                                | 558 ms: 1.01x slower                                                   |
| meteor_contest             | 106 ms                                                                | 107 ms: 1.01x slower                                                   |
| scimark_monte_carlo        | 66.5 ms                                                               | 67.1 ms: 1.01x slower                                                  |
| xml_etree_generate         | 85.4 ms                                                               | 86.3 ms: 1.01x slower                                                  |
| asyncio_tcp                | 477 ms                                                                | 482 ms: 1.01x slower                                                   |
| mako                       | 10.9 ms                                                               | 11.1 ms: 1.01x slower                                                  |
| python_startup_no_site     | 7.02 ms                                                               | 7.10 ms: 1.01x slower                                                  |
| 2to3                       | 264 ms                                                                | 267 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed_tg | 542 ms                                                                | 548 ms: 1.01x slower                                                   |
| scimark_sparse_mat_mult    | 5.00 ms                                                               | 5.06 ms: 1.01x slower                                                  |
| sqlglot_parse              | 1.29 ms                                                               | 1.30 ms: 1.01x slower                                                  |
| pprint_safe_repr           | 735 ms                                                                | 745 ms: 1.01x slower                                                   |
| sqlite_synth               | 2.92 us                                                               | 2.96 us: 1.01x slower                                                  |
| docutils                   | 2.70 sec                                                              | 2.74 sec: 1.01x slower                                                 |
| python_startup             | 10.5 ms                                                               | 10.7 ms: 1.01x slower                                                  |
| sqlglot_transpile          | 1.58 ms                                                               | 1.61 ms: 1.02x slower                                                  |
| logging_format             | 6.04 us                                                               | 6.14 us: 1.02x slower                                                  |
| async_generators           | 430 ms                                                                | 437 ms: 1.02x slower                                                   |
| richards_super             | 53.3 ms                                                               | 54.2 ms: 1.02x slower                                                  |
| coroutines                 | 22.8 ms                                                               | 23.2 ms: 1.02x slower                                                  |
| pprint_pformat             | 1.49 sec                                                              | 1.52 sec: 1.02x slower                                                 |
| deepcopy                   | 261 us                                                                | 265 us: 1.02x slower                                                   |
| richards                   | 47.5 ms                                                               | 48.4 ms: 1.02x slower                                                  |
| sqlglot_optimize           | 53.5 ms                                                               | 54.5 ms: 1.02x slower                                                  |
| thrift                     | 788 us                                                                | 805 us: 1.02x slower                                                   |
| bench_thread_pool          | 787 us                                                                | 804 us: 1.02x slower                                                   |
| django_template            | 33.7 ms                                                               | 34.5 ms: 1.02x slower                                                  |
| typing_runtime_protocols   | 164 us                                                                | 168 us: 1.02x slower                                                   |
| regex_compile              | 130 ms                                                                | 133 ms: 1.02x slower                                                   |
| sqlglot_normalize          | 106 ms                                                                | 109 ms: 1.02x slower                                                   |
| crypto_pyaes               | 72.2 ms                                                               | 74.0 ms: 1.02x slower                                                  |
| pickle_pure_python         | 301 us                                                                | 308 us: 1.02x slower                                                   |
| genshi_text                | 22.8 ms                                                               | 23.4 ms: 1.03x slower                                                  |
| unpickle_list              | 5.13 us                                                               | 5.27 us: 1.03x slower                                                  |
| sympy_integrate            | 19.9 ms                                                               | 20.5 ms: 1.03x slower                                                  |
| fannkuch                   | 396 ms                                                                | 408 ms: 1.03x slower                                                   |
| sympy_str                  | 274 ms                                                                | 282 ms: 1.03x slower                                                   |
| html5lib                   | 64.7 ms                                                               | 66.8 ms: 1.03x slower                                                  |
| pyflate                    | 465 ms                                                                | 479 ms: 1.03x slower                                                   |
| logging_silent             | 98.4 ns                                                               | 102 ns: 1.03x slower                                                   |
| deltablue                  | 3.16 ms                                                               | 3.27 ms: 1.03x slower                                                  |
| unpickle_pure_python       | 212 us                                                                | 220 us: 1.04x slower                                                   |
| deepcopy_memo              | 29.3 us                                                               | 30.4 us: 1.04x slower                                                  |
| sympy_sum                  | 151 ms                                                                | 158 ms: 1.05x slower                                                   |
| dulwich_log                | 64.9 ms                                                               | 68.8 ms: 1.06x slower                                                  |
| tornado_http               | 90.6 ms                                                               | 96.2 ms: 1.06x slower                                                  |
| mdp                        | 2.52 sec                                                              | 2.72 sec: 1.08x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (26): unpickle, genshi_xml, pathlib, xml_etree_parse, async_tree_io, bpe_tokeniser, bench_mp_pool, nbody, asyncio_tcp_ssl, logging_simple, pidigits, pickle_list, json, tomli_loads, xml_etree_iterparse, async_tree_none, async_tree_memoization, dask, pycparser, async_tree_cpu_io_mixed, sympy_expand, telco, async_tree_memoization_tg, async_tree_io_tg, async_tree_none_tg, pylint

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x
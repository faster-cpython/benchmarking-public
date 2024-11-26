# Results vs. 3.13.0

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: windows-x86
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.036x faster
- HPT reliability: 99.65%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 248 ms: 1.03x faster                                                           |
| docutils       | 1.80 sec                                                        | 1.87 sec: 1.04x slower                                                         |
| html5lib       | 47.1 ms                                                         | 48.1 ms: 1.02x slower                                                          |
| tornado_http   | 105 ms                                                          | 95.1 ms: 1.10x faster                                                          |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 250 ms: 1.15x faster                                                           |
| async_tree_none            | 245 ms                                                          | 217 ms: 1.13x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 271 ms: 1.11x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 198 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 466 ms: 1.05x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 461 ms: 1.02x faster                                                           |
| async_tree_io_tg           | 499 ms                                                          | 515 ms: 1.03x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 18.0 ms: 1.11x slower                                                          |
| async_generators           | 267 ms                                                          | 300 ms: 1.12x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 197 ms: 1.03x faster                                                           |
| float          | 56.4 ms                                                         | 62.2 ms: 1.10x slower                                                          |
| nbody          | 81.4 ms                                                         | 91.3 ms: 1.12x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.82 ms                                                         | 1.88 ms: 1.03x slower                                                          |
| regex_v8       | 15.5 ms                                                         | 16.1 ms: 1.04x slower                                                          |
| regex_dna      | 112 ms                                                          | 118 ms: 1.05x slower                                                           |
| regex_compile  | 101 ms                                                          | 108 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.8 us: 1.04x faster                                                          |
| json_dumps           | 7.53 ms                                                         | 7.69 ms: 1.02x slower                                                          |
| xml_etree_parse      | 102 ms                                                          | 107 ms: 1.04x slower                                                           |
| pickle_pure_python   | 239 us                                                          | 257 us: 1.08x slower                                                           |
| xml_etree_iterparse  | 61.3 ms                                                         | 66.8 ms: 1.09x slower                                                          |
| xml_etree_generate   | 61.9 ms                                                         | 68.3 ms: 1.10x slower                                                          |
| tomli_loads          | 1.74 sec                                                        | 1.93 sec: 1.11x slower                                                         |
| unpickle_pure_python | 162 us                                                          | 181 us: 1.12x slower                                                           |
| xml_etree_process    | 44.6 ms                                                         | 50.7 ms: 1.14x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 23.8 ms: 1.19x faster                                                          |
| python_startup_no_site | 20.2 ms                                                         | 19.8 ms: 1.02x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 21.7 ms                                                         | 22.3 ms: 1.03x slower                                                          |
| django_template | 32.0 ms                                                         | 33.7 ms: 1.05x slower                                                          |
| mako            | 7.02 ms                                                         | 7.99 ms: 1.14x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.05x slower                                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 742 us: 13.83x faster                                                          |
| coverage                   | 326 ms                                                          | 52.7 ms: 6.19x faster                                                          |
| create_gc_cycles           | 1.08 ms                                                         | 733 us: 1.48x faster                                                           |
| bench_mp_pool              | 93.6 ms                                                         | 71.5 ms: 1.31x faster                                                          |
| gc_traversal               | 1.76 ms                                                         | 1.41 ms: 1.25x faster                                                          |
| deepcopy                   | 311 us                                                          | 250 us: 1.24x faster                                                           |
| deepcopy_memo              | 26.2 us                                                         | 21.9 us: 1.19x faster                                                          |
| python_startup             | 28.3 ms                                                         | 23.8 ms: 1.19x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 250 ms: 1.15x faster                                                           |
| deepcopy_reduce            | 2.94 us                                                         | 2.60 us: 1.13x faster                                                          |
| async_tree_none            | 245 ms                                                          | 217 ms: 1.13x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 271 ms: 1.11x faster                                                           |
| tornado_http               | 105 ms                                                          | 95.1 ms: 1.10x faster                                                          |
| async_tree_none_tg         | 216 ms                                                          | 198 ms: 1.09x faster                                                           |
| go                         | 111 ms                                                          | 103 ms: 1.07x faster                                                           |
| pathlib                    | 89.1 ms                                                         | 83.3 ms: 1.07x faster                                                          |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 466 ms: 1.05x faster                                                           |
| json_loads                 | 21.7 us                                                         | 20.8 us: 1.04x faster                                                          |
| pidigits                   | 204 ms                                                          | 197 ms: 1.03x faster                                                           |
| 2to3                       | 255 ms                                                          | 248 ms: 1.03x faster                                                           |
| json                       | 4.40 ms                                                         | 4.28 ms: 1.03x faster                                                          |
| typing_runtime_protocols   | 141 us                                                          | 137 us: 1.02x faster                                                           |
| python_startup_no_site     | 20.2 ms                                                         | 19.8 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 461 ms: 1.02x faster                                                           |
| sympy_sum                  | 108 ms                                                          | 106 ms: 1.02x faster                                                           |
| dulwich_log                | 50.2 ms                                                         | 49.9 ms: 1.01x faster                                                          |
| sympy_str                  | 214 ms                                                          | 216 ms: 1.01x slower                                                           |
| pprint_safe_repr           | 658 ms                                                          | 665 ms: 1.01x slower                                                           |
| crypto_pyaes               | 56.6 ms                                                         | 57.3 ms: 1.01x slower                                                          |
| logging_simple             | 7.89 us                                                         | 8.00 us: 1.01x slower                                                          |
| logging_format             | 8.59 us                                                         | 8.71 us: 1.01x slower                                                          |
| sqlglot_optimize           | 42.4 ms                                                         | 43.0 ms: 1.01x slower                                                          |
| telco                      | 6.27 ms                                                         | 6.37 ms: 1.02x slower                                                          |
| sympy_expand               | 377 ms                                                          | 383 ms: 1.02x slower                                                           |
| sympy_integrate            | 15.2 ms                                                         | 15.5 ms: 1.02x slower                                                          |
| pycparser                  | 869 ms                                                          | 884 ms: 1.02x slower                                                           |
| json_dumps                 | 7.53 ms                                                         | 7.69 ms: 1.02x slower                                                          |
| meteor_contest             | 78.1 ms                                                         | 79.8 ms: 1.02x slower                                                          |
| html5lib                   | 47.1 ms                                                         | 48.1 ms: 1.02x slower                                                          |
| genshi_text                | 21.7 ms                                                         | 22.3 ms: 1.03x slower                                                          |
| async_tree_io_tg           | 499 ms                                                          | 515 ms: 1.03x slower                                                           |
| sqlglot_transpile          | 1.26 ms                                                         | 1.30 ms: 1.03x slower                                                          |
| sqlglot_parse              | 1.02 ms                                                         | 1.05 ms: 1.03x slower                                                          |
| regex_effbot               | 1.82 ms                                                         | 1.88 ms: 1.03x slower                                                          |
| docutils                   | 1.80 sec                                                        | 1.87 sec: 1.04x slower                                                         |
| regex_v8                   | 15.5 ms                                                         | 16.1 ms: 1.04x slower                                                          |
| xml_etree_parse            | 102 ms                                                          | 107 ms: 1.04x slower                                                           |
| comprehensions             | 13.1 us                                                         | 13.8 us: 1.05x slower                                                          |
| regex_dna                  | 112 ms                                                          | 118 ms: 1.05x slower                                                           |
| pprint_pformat             | 1.32 sec                                                        | 1.39 sec: 1.05x slower                                                         |
| django_template            | 32.0 ms                                                         | 33.7 ms: 1.05x slower                                                          |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.07 ms: 1.07x slower                                                          |
| regex_compile              | 101 ms                                                          | 108 ms: 1.07x slower                                                           |
| spectral_norm              | 70.0 ms                                                         | 75.2 ms: 1.07x slower                                                          |
| pickle_pure_python         | 239 us                                                          | 257 us: 1.08x slower                                                           |
| chaos                      | 49.4 ms                                                         | 53.4 ms: 1.08x slower                                                          |
| xml_etree_iterparse        | 61.3 ms                                                         | 66.8 ms: 1.09x slower                                                          |
| fannkuch                   | 288 ms                                                          | 314 ms: 1.09x slower                                                           |
| pyflate                    | 322 ms                                                          | 352 ms: 1.09x slower                                                           |
| float                      | 56.4 ms                                                         | 62.2 ms: 1.10x slower                                                          |
| xml_etree_generate         | 61.9 ms                                                         | 68.3 ms: 1.10x slower                                                          |
| tomli_loads                | 1.74 sec                                                        | 1.93 sec: 1.11x slower                                                         |
| hexiom                     | 4.60 ms                                                         | 5.10 ms: 1.11x slower                                                          |
| coroutines                 | 16.1 ms                                                         | 18.0 ms: 1.11x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 181 us: 1.12x slower                                                           |
| scimark_lu                 | 60.7 ms                                                         | 68.1 ms: 1.12x slower                                                          |
| nbody                      | 81.4 ms                                                         | 91.3 ms: 1.12x slower                                                          |
| async_generators           | 267 ms                                                          | 300 ms: 1.12x slower                                                           |
| richards                   | 33.4 ms                                                         | 37.9 ms: 1.13x slower                                                          |
| xml_etree_process          | 44.6 ms                                                         | 50.7 ms: 1.14x slower                                                          |
| scimark_monte_carlo        | 48.7 ms                                                         | 55.4 ms: 1.14x slower                                                          |
| mako                       | 7.02 ms                                                         | 7.99 ms: 1.14x slower                                                          |
| deltablue                  | 2.35 ms                                                         | 2.68 ms: 1.14x slower                                                          |
| scimark_fft                | 204 ms                                                          | 233 ms: 1.14x slower                                                           |
| scimark_sor                | 85.8 ms                                                         | 98.3 ms: 1.15x slower                                                          |
| raytrace                   | 203 ms                                                          | 236 ms: 1.16x slower                                                           |
| richards_super             | 37.0 ms                                                         | 43.5 ms: 1.18x slower                                                          |
| logging_silent             | 62.4 ns                                                         | 74.5 ns: 1.19x slower                                                          |
| generators                 | 21.5 ms                                                         | 26.2 ms: 1.22x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (7): bench_thread_pool, genshi_xml, nqueens, sqlglot_normalize, mdp, async_tree_io, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.036x faster
# HPT report

- Reliability score: 99.65% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
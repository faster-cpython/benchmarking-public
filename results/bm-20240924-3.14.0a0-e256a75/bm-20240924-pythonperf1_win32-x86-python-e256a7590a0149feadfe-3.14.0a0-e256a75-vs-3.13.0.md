# Results vs. 3.13.0

- fork: python
- ref: e256a7590a0149feadfe
- machine: windows-x86
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.026x faster
- HPT reliability: 99.72%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 249 ms: 1.02x faster                                                           |
| docutils       | 1.80 sec                                                        | 1.87 sec: 1.04x slower                                                         |
| html5lib       | 47.1 ms                                                         | 46.5 ms: 1.01x faster                                                          |
| tornado_http   | 105 ms                                                          | 94.9 ms: 1.10x faster                                                          |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 253 ms: 1.13x faster                                                           |
| async_tree_none            | 245 ms                                                          | 218 ms: 1.12x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 273 ms: 1.11x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 201 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 464 ms: 1.05x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 455 ms: 1.03x faster                                                           |
| async_tree_io_tg           | 499 ms                                                          | 518 ms: 1.04x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 18.0 ms: 1.12x slower                                                          |
| async_generators           | 267 ms                                                          | 301 ms: 1.13x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 197 ms: 1.03x faster                                                           |
| float          | 56.4 ms                                                         | 62.8 ms: 1.11x slower                                                          |
| nbody          | 81.4 ms                                                         | 93.0 ms: 1.14x slower                                                          |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.82 ms                                                         | 1.90 ms: 1.05x slower                                                          |
| regex_v8       | 15.5 ms                                                         | 16.2 ms: 1.05x slower                                                          |
| regex_dna      | 112 ms                                                          | 121 ms: 1.08x slower                                                           |
| regex_compile  | 101 ms                                                          | 109 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 21.0 us: 1.03x faster                                                          |
| json_dumps           | 7.53 ms                                                         | 7.68 ms: 1.02x slower                                                          |
| xml_etree_parse      | 102 ms                                                          | 107 ms: 1.05x slower                                                           |
| tomli_loads          | 1.74 sec                                                        | 1.85 sec: 1.06x slower                                                         |
| xml_etree_generate   | 61.9 ms                                                         | 67.5 ms: 1.09x slower                                                          |
| pickle_pure_python   | 239 us                                                          | 262 us: 1.10x slower                                                           |
| xml_etree_iterparse  | 61.3 ms                                                         | 67.5 ms: 1.10x slower                                                          |
| xml_etree_process    | 44.6 ms                                                         | 49.4 ms: 1.11x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 180 us: 1.12x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 23.5 ms: 1.20x faster                                                          |
| python_startup_no_site | 20.2 ms                                                         | 19.4 ms: 1.04x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.12x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 50.3 ms: 1.03x slower                                                          |
| django_template | 32.0 ms                                                         | 33.6 ms: 1.05x slower                                                          |
| genshi_text     | 21.7 ms                                                         | 24.2 ms: 1.11x slower                                                          |
| mako            | 7.02 ms                                                         | 8.16 ms: 1.16x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.09x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 746 us: 13.75x faster                                                          |
| coverage                   | 326 ms                                                          | 53.2 ms: 6.14x faster                                                          |
| create_gc_cycles           | 1.08 ms                                                         | 727 us: 1.49x faster                                                           |
| bench_mp_pool              | 93.6 ms                                                         | 69.9 ms: 1.34x faster                                                          |
| gc_traversal               | 1.76 ms                                                         | 1.42 ms: 1.25x faster                                                          |
| deepcopy                   | 311 us                                                          | 250 us: 1.25x faster                                                           |
| python_startup             | 28.3 ms                                                         | 23.5 ms: 1.20x faster                                                          |
| deepcopy_reduce            | 2.94 us                                                         | 2.50 us: 1.18x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 22.6 us: 1.16x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 253 ms: 1.13x faster                                                           |
| async_tree_none            | 245 ms                                                          | 218 ms: 1.12x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 273 ms: 1.11x faster                                                           |
| tornado_http               | 105 ms                                                          | 94.9 ms: 1.10x faster                                                          |
| async_tree_none_tg         | 216 ms                                                          | 201 ms: 1.07x faster                                                           |
| pathlib                    | 89.1 ms                                                         | 83.5 ms: 1.07x faster                                                          |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 464 ms: 1.05x faster                                                           |
| bench_thread_pool          | 1.04 ms                                                         | 998 us: 1.04x faster                                                           |
| python_startup_no_site     | 20.2 ms                                                         | 19.4 ms: 1.04x faster                                                          |
| go                         | 111 ms                                                          | 107 ms: 1.04x faster                                                           |
| json_loads                 | 21.7 us                                                         | 21.0 us: 1.03x faster                                                          |
| pidigits                   | 204 ms                                                          | 197 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 455 ms: 1.03x faster                                                           |
| mdp                        | 1.70 sec                                                        | 1.66 sec: 1.03x faster                                                         |
| 2to3                       | 255 ms                                                          | 249 ms: 1.02x faster                                                           |
| json                       | 4.40 ms                                                         | 4.32 ms: 1.02x faster                                                          |
| html5lib                   | 47.1 ms                                                         | 46.5 ms: 1.01x faster                                                          |
| logging_simple             | 7.89 us                                                         | 7.93 us: 1.00x slower                                                          |
| sympy_integrate            | 15.2 ms                                                         | 15.3 ms: 1.01x slower                                                          |
| logging_format             | 8.59 us                                                         | 8.66 us: 1.01x slower                                                          |
| sympy_str                  | 214 ms                                                          | 216 ms: 1.01x slower                                                           |
| crypto_pyaes               | 56.6 ms                                                         | 57.2 ms: 1.01x slower                                                          |
| pycparser                  | 869 ms                                                          | 877 ms: 1.01x slower                                                           |
| sympy_expand               | 377 ms                                                          | 381 ms: 1.01x slower                                                           |
| typing_runtime_protocols   | 141 us                                                          | 143 us: 1.02x slower                                                           |
| json_dumps                 | 7.53 ms                                                         | 7.68 ms: 1.02x slower                                                          |
| dulwich_log                | 50.2 ms                                                         | 51.2 ms: 1.02x slower                                                          |
| genshi_xml                 | 49.0 ms                                                         | 50.3 ms: 1.03x slower                                                          |
| nqueens                    | 75.1 ms                                                         | 77.3 ms: 1.03x slower                                                          |
| docutils                   | 1.80 sec                                                        | 1.87 sec: 1.04x slower                                                         |
| async_tree_io_tg           | 499 ms                                                          | 518 ms: 1.04x slower                                                           |
| pprint_safe_repr           | 658 ms                                                          | 684 ms: 1.04x slower                                                           |
| meteor_contest             | 78.1 ms                                                         | 81.4 ms: 1.04x slower                                                          |
| sqlglot_normalize          | 223 ms                                                          | 233 ms: 1.05x slower                                                           |
| regex_effbot               | 1.82 ms                                                         | 1.90 ms: 1.05x slower                                                          |
| regex_v8                   | 15.5 ms                                                         | 16.2 ms: 1.05x slower                                                          |
| xml_etree_parse            | 102 ms                                                          | 107 ms: 1.05x slower                                                           |
| django_template            | 32.0 ms                                                         | 33.6 ms: 1.05x slower                                                          |
| sqlglot_optimize           | 42.4 ms                                                         | 44.6 ms: 1.05x slower                                                          |
| telco                      | 6.27 ms                                                         | 6.61 ms: 1.05x slower                                                          |
| pprint_pformat             | 1.32 sec                                                        | 1.40 sec: 1.06x slower                                                         |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.06 ms: 1.06x slower                                                          |
| tomli_loads                | 1.74 sec                                                        | 1.85 sec: 1.06x slower                                                         |
| sqlglot_transpile          | 1.26 ms                                                         | 1.35 ms: 1.07x slower                                                          |
| comprehensions             | 13.1 us                                                         | 14.1 us: 1.07x slower                                                          |
| sqlglot_parse              | 1.02 ms                                                         | 1.10 ms: 1.07x slower                                                          |
| regex_dna                  | 112 ms                                                          | 121 ms: 1.08x slower                                                           |
| regex_compile              | 101 ms                                                          | 109 ms: 1.08x slower                                                           |
| spectral_norm              | 70.0 ms                                                         | 75.9 ms: 1.08x slower                                                          |
| xml_etree_generate         | 61.9 ms                                                         | 67.5 ms: 1.09x slower                                                          |
| pickle_pure_python         | 239 us                                                          | 262 us: 1.10x slower                                                           |
| chaos                      | 49.4 ms                                                         | 54.3 ms: 1.10x slower                                                          |
| xml_etree_iterparse        | 61.3 ms                                                         | 67.5 ms: 1.10x slower                                                          |
| xml_etree_process          | 44.6 ms                                                         | 49.4 ms: 1.11x slower                                                          |
| float                      | 56.4 ms                                                         | 62.8 ms: 1.11x slower                                                          |
| genshi_text                | 21.7 ms                                                         | 24.2 ms: 1.11x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 180 us: 1.12x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 18.0 ms: 1.12x slower                                                          |
| pyflate                    | 322 ms                                                          | 362 ms: 1.12x slower                                                           |
| hexiom                     | 4.60 ms                                                         | 5.17 ms: 1.12x slower                                                          |
| async_generators           | 267 ms                                                          | 301 ms: 1.13x slower                                                           |
| scimark_lu                 | 60.7 ms                                                         | 68.7 ms: 1.13x slower                                                          |
| deltablue                  | 2.35 ms                                                         | 2.67 ms: 1.14x slower                                                          |
| nbody                      | 81.4 ms                                                         | 93.0 ms: 1.14x slower                                                          |
| raytrace                   | 203 ms                                                          | 233 ms: 1.15x slower                                                           |
| mako                       | 7.02 ms                                                         | 8.16 ms: 1.16x slower                                                          |
| fannkuch                   | 288 ms                                                          | 336 ms: 1.16x slower                                                           |
| scimark_monte_carlo        | 48.7 ms                                                         | 56.9 ms: 1.17x slower                                                          |
| scimark_fft                | 204 ms                                                          | 239 ms: 1.17x slower                                                           |
| richards                   | 33.4 ms                                                         | 39.4 ms: 1.18x slower                                                          |
| logging_silent             | 62.4 ns                                                         | 74.6 ns: 1.20x slower                                                          |
| richards_super             | 37.0 ms                                                         | 44.3 ms: 1.20x slower                                                          |
| generators                 | 21.5 ms                                                         | 26.0 ms: 1.21x slower                                                          |
| scimark_sor                | 85.8 ms                                                         | 105 ms: 1.22x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (3): sympy_sum, async_tree_io, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240924-3.14.0a0-e256a75/bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.026x faster
# HPT report

- Reliability score: 99.72% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
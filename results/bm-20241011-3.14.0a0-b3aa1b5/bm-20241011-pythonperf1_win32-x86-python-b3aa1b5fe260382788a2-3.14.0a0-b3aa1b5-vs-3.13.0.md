# Results vs. 3.13.0

- fork: python
- ref: b3aa1b5fe260382788a2
- machine: windows-x86
- commit hash: b3aa1b5
- commit date: 2024-10-11
- overall geometric mean: 1.033x faster
- HPT reliability: 98.68%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 248 ms: 1.03x faster                                                           |
| docutils       | 1.80 sec                                                        | 1.88 sec: 1.04x slower                                                         |
| html5lib       | 47.1 ms                                                         | 47.3 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 249 ms: 1.15x faster                                                           |
| async_tree_none            | 245 ms                                                          | 213 ms: 1.15x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 270 ms: 1.12x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 196 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 471 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 459 ms: 1.02x faster                                                           |
| async_tree_io_tg           | 499 ms                                                          | 519 ms: 1.04x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 17.5 ms: 1.09x slower                                                          |
| async_generators           | 267 ms                                                          | 301 ms: 1.13x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 199 ms: 1.02x faster                                                           |
| nbody          | 81.4 ms                                                         | 86.7 ms: 1.06x slower                                                          |
| float          | 56.4 ms                                                         | 60.9 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.82 ms                                                         | 1.84 ms: 1.01x slower                                                          |
| regex_v8       | 15.5 ms                                                         | 15.7 ms: 1.01x slower                                                          |
| regex_dna      | 112 ms                                                          | 117 ms: 1.04x slower                                                           |
| regex_compile  | 101 ms                                                          | 107 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 21.0 us: 1.03x faster                                                          |
| tomli_loads          | 1.74 sec                                                        | 1.87 sec: 1.07x slower                                                         |
| xml_etree_process    | 44.6 ms                                                         | 48.3 ms: 1.08x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 177 us: 1.09x slower                                                           |
| xml_etree_generate   | 61.9 ms                                                         | 67.7 ms: 1.09x slower                                                          |
| xml_etree_parse      | 102 ms                                                          | 113 ms: 1.10x slower                                                           |
| pickle_pure_python   | 239 us                                                          | 265 us: 1.11x slower                                                           |
| xml_etree_iterparse  | 61.3 ms                                                         | 68.7 ms: 1.12x slower                                                          |
| json_dumps           | 7.53 ms                                                         | 9.01 ms: 1.20x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.09x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 24.9 ms: 1.14x faster                                                          |
| python_startup_no_site | 20.2 ms                                                         | 20.7 ms: 1.03x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 47.0 ms: 1.04x faster                                                          |
| genshi_text     | 21.7 ms                                                         | 21.5 ms: 1.01x faster                                                          |
| django_template | 32.0 ms                                                         | 34.8 ms: 1.09x slower                                                          |
| mako            | 7.02 ms                                                         | 7.76 ms: 1.11x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.03x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 738 us: 13.90x faster                                                          |
| coverage                   | 326 ms                                                          | 52.7 ms: 6.19x faster                                                          |
| create_gc_cycles           | 1.08 ms                                                         | 783 us: 1.38x faster                                                           |
| deepcopy                   | 311 us                                                          | 245 us: 1.27x faster                                                           |
| bench_mp_pool              | 93.6 ms                                                         | 74.0 ms: 1.27x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 21.3 us: 1.23x faster                                                          |
| gc_traversal               | 1.76 ms                                                         | 1.45 ms: 1.22x faster                                                          |
| deepcopy_reduce            | 2.94 us                                                         | 2.49 us: 1.18x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 249 ms: 1.15x faster                                                           |
| async_tree_none            | 245 ms                                                          | 213 ms: 1.15x faster                                                           |
| python_startup             | 28.3 ms                                                         | 24.9 ms: 1.14x faster                                                          |
| async_tree_memoization     | 302 ms                                                          | 270 ms: 1.12x faster                                                           |
| go                         | 111 ms                                                          | 99.3 ms: 1.12x faster                                                          |
| async_tree_none_tg         | 216 ms                                                          | 196 ms: 1.10x faster                                                           |
| genshi_xml                 | 49.0 ms                                                         | 47.0 ms: 1.04x faster                                                          |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 471 ms: 1.04x faster                                                           |
| pycparser                  | 869 ms                                                          | 836 ms: 1.04x faster                                                           |
| json_loads                 | 21.7 us                                                         | 21.0 us: 1.03x faster                                                          |
| bench_thread_pool          | 1.04 ms                                                         | 1.01 ms: 1.03x faster                                                          |
| json                       | 4.40 ms                                                         | 4.27 ms: 1.03x faster                                                          |
| 2to3                       | 255 ms                                                          | 248 ms: 1.03x faster                                                           |
| pidigits                   | 204 ms                                                          | 199 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 459 ms: 1.02x faster                                                           |
| pprint_safe_repr           | 658 ms                                                          | 645 ms: 1.02x faster                                                           |
| typing_runtime_protocols   | 141 us                                                          | 139 us: 1.02x faster                                                           |
| pathlib                    | 89.1 ms                                                         | 88.1 ms: 1.01x faster                                                          |
| genshi_text                | 21.7 ms                                                         | 21.5 ms: 1.01x faster                                                          |
| mdp                        | 1.70 sec                                                        | 1.71 sec: 1.00x slower                                                         |
| html5lib                   | 47.1 ms                                                         | 47.3 ms: 1.01x slower                                                          |
| regex_effbot               | 1.82 ms                                                         | 1.84 ms: 1.01x slower                                                          |
| regex_v8                   | 15.5 ms                                                         | 15.7 ms: 1.01x slower                                                          |
| sympy_str                  | 214 ms                                                          | 219 ms: 1.02x slower                                                           |
| meteor_contest             | 78.1 ms                                                         | 80.0 ms: 1.02x slower                                                          |
| sympy_expand               | 377 ms                                                          | 386 ms: 1.02x slower                                                           |
| sympy_integrate            | 15.2 ms                                                         | 15.6 ms: 1.03x slower                                                          |
| python_startup_no_site     | 20.2 ms                                                         | 20.7 ms: 1.03x slower                                                          |
| sqlglot_normalize          | 223 ms                                                          | 229 ms: 1.03x slower                                                           |
| dulwich_log                | 50.2 ms                                                         | 51.7 ms: 1.03x slower                                                          |
| sqlglot_transpile          | 1.26 ms                                                         | 1.30 ms: 1.03x slower                                                          |
| sqlglot_parse              | 1.02 ms                                                         | 1.06 ms: 1.04x slower                                                          |
| sqlglot_optimize           | 42.4 ms                                                         | 44.0 ms: 1.04x slower                                                          |
| async_tree_io_tg           | 499 ms                                                          | 519 ms: 1.04x slower                                                           |
| docutils                   | 1.80 sec                                                        | 1.88 sec: 1.04x slower                                                         |
| regex_dna                  | 112 ms                                                          | 117 ms: 1.04x slower                                                           |
| spectral_norm              | 70.0 ms                                                         | 74.0 ms: 1.06x slower                                                          |
| regex_compile              | 101 ms                                                          | 107 ms: 1.06x slower                                                           |
| nbody                      | 81.4 ms                                                         | 86.7 ms: 1.06x slower                                                          |
| fannkuch                   | 288 ms                                                          | 308 ms: 1.07x slower                                                           |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.09 ms: 1.07x slower                                                          |
| tomli_loads                | 1.74 sec                                                        | 1.87 sec: 1.07x slower                                                         |
| hexiom                     | 4.60 ms                                                         | 4.96 ms: 1.08x slower                                                          |
| crypto_pyaes               | 56.6 ms                                                         | 61.1 ms: 1.08x slower                                                          |
| float                      | 56.4 ms                                                         | 60.9 ms: 1.08x slower                                                          |
| logging_silent             | 62.4 ns                                                         | 67.4 ns: 1.08x slower                                                          |
| xml_etree_process          | 44.6 ms                                                         | 48.3 ms: 1.08x slower                                                          |
| django_template            | 32.0 ms                                                         | 34.8 ms: 1.09x slower                                                          |
| coroutines                 | 16.1 ms                                                         | 17.5 ms: 1.09x slower                                                          |
| generators                 | 21.5 ms                                                         | 23.5 ms: 1.09x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 177 us: 1.09x slower                                                           |
| xml_etree_generate         | 61.9 ms                                                         | 67.7 ms: 1.09x slower                                                          |
| xml_etree_parse            | 102 ms                                                          | 113 ms: 1.10x slower                                                           |
| mako                       | 7.02 ms                                                         | 7.76 ms: 1.11x slower                                                          |
| pyflate                    | 322 ms                                                          | 356 ms: 1.11x slower                                                           |
| pickle_pure_python         | 239 us                                                          | 265 us: 1.11x slower                                                           |
| chaos                      | 49.4 ms                                                         | 55.0 ms: 1.11x slower                                                          |
| telco                      | 6.27 ms                                                         | 6.98 ms: 1.11x slower                                                          |
| xml_etree_iterparse        | 61.3 ms                                                         | 68.7 ms: 1.12x slower                                                          |
| scimark_fft                | 204 ms                                                          | 229 ms: 1.12x slower                                                           |
| async_generators           | 267 ms                                                          | 301 ms: 1.13x slower                                                           |
| scimark_lu                 | 60.7 ms                                                         | 68.5 ms: 1.13x slower                                                          |
| deltablue                  | 2.35 ms                                                         | 2.70 ms: 1.15x slower                                                          |
| scimark_monte_carlo        | 48.7 ms                                                         | 55.9 ms: 1.15x slower                                                          |
| scimark_sor                | 85.8 ms                                                         | 99.4 ms: 1.16x slower                                                          |
| json_dumps                 | 7.53 ms                                                         | 9.01 ms: 1.20x slower                                                          |
| raytrace                   | 203 ms                                                          | 243 ms: 1.20x slower                                                           |
| richards                   | 33.4 ms                                                         | 40.5 ms: 1.21x slower                                                          |
| richards_super             | 37.0 ms                                                         | 45.3 ms: 1.22x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (9): tornado_http, logging_simple, nqueens, pprint_pformat, logging_format, comprehensions, sympy_sum, async_tree_io, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241011-3.14.0a0-b3aa1b5/bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.033x faster
# HPT report

- Reliability score: 98.68% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
# Results vs. 3.13.0

- fork: python
- ref: 9c4347ef8b60f54dd357
- machine: windows-x86
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.084x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 268 ms: 1.05x slower                                                           |
| chameleon      | 6.24 ms                                                         | 6.15 ms: 1.01x faster                                                          |
| docutils       | 1.80 sec                                                        | 1.94 sec: 1.08x slower                                                         |
| tornado_http   | 105 ms                                                          | 112 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 490 ms                                                          | 523 ms: 1.07x slower                                                           |
| async_tree_memoization     | 302 ms                                                          | 329 ms: 1.09x slower                                                           |
| async_tree_none            | 245 ms                                                          | 270 ms: 1.10x slower                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 518 ms: 1.10x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 18.3 ms: 1.14x slower                                                          |
| async_generators           | 267 ms                                                          | 304 ms: 1.14x slower                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 327 ms: 1.14x slower                                                           |
| async_tree_none_tg         | 216 ms                                                          | 264 ms: 1.22x slower                                                           |
| async_tree_io              | 530 ms                                                          | 651 ms: 1.23x slower                                                           |
| async_tree_io_tg           | 499 ms                                                          | 634 ms: 1.27x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.15x slower                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 198 ms: 1.03x faster                                                           |
| float          | 56.4 ms                                                         | 62.3 ms: 1.10x slower                                                          |
| nbody          | 81.4 ms                                                         | 91.9 ms: 1.13x slower                                                          |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 16.3 ms: 1.05x slower                                                          |
| regex_effbot   | 1.82 ms                                                         | 2.01 ms: 1.11x slower                                                          |
| regex_dna      | 112 ms                                                          | 132 ms: 1.17x slower                                                           |
| regex_compile  | 101 ms                                                          | 131 ms: 1.30x slower                                                           |
| Geometric mean | (ref)                                                           | 1.15x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 19.9 us: 1.09x faster                                                          |
| json_dumps           | 7.53 ms                                                         | 7.11 ms: 1.06x faster                                                          |
| pickle_pure_python   | 239 us                                                          | 235 us: 1.02x faster                                                           |
| tomli_loads          | 1.74 sec                                                        | 1.79 sec: 1.03x slower                                                         |
| unpickle_pure_python | 162 us                                                          | 173 us: 1.07x slower                                                           |
| xml_etree_process    | 44.6 ms                                                         | 47.9 ms: 1.07x slower                                                          |
| xml_etree_parse      | 102 ms                                                          | 111 ms: 1.08x slower                                                           |
| xml_etree_generate   | 61.9 ms                                                         | 67.3 ms: 1.09x slower                                                          |
| xml_etree_iterparse  | 61.3 ms                                                         | 71.7 ms: 1.17x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 23.3 ms: 1.22x faster                                                          |
| python_startup_no_site | 20.2 ms                                                         | 21.2 ms: 1.05x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.08x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|-----------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako      | 7.02 ms                                                         | 8.20 ms: 1.17x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| create_gc_cycles           | 1.08 ms                                                         | 648 us: 1.67x faster                                                           |
| typing_runtime_protocols   | 141 us                                                          | 105 us: 1.34x faster                                                           |
| gc_traversal               | 1.76 ms                                                         | 1.40 ms: 1.26x faster                                                          |
| bench_mp_pool              | 93.6 ms                                                         | 75.2 ms: 1.24x faster                                                          |
| python_startup             | 28.3 ms                                                         | 23.3 ms: 1.22x faster                                                          |
| deepcopy_reduce            | 2.94 us                                                         | 2.64 us: 1.12x faster                                                          |
| json_loads                 | 21.7 us                                                         | 19.9 us: 1.09x faster                                                          |
| json                       | 4.40 ms                                                         | 4.12 ms: 1.07x faster                                                          |
| json_dumps                 | 7.53 ms                                                         | 7.11 ms: 1.06x faster                                                          |
| pidigits                   | 204 ms                                                          | 198 ms: 1.03x faster                                                           |
| pickle_pure_python         | 239 us                                                          | 235 us: 1.02x faster                                                           |
| chameleon                  | 6.24 ms                                                         | 6.15 ms: 1.01x faster                                                          |
| pprint_safe_repr           | 658 ms                                                          | 649 ms: 1.01x faster                                                           |
| deepcopy                   | 311 us                                                          | 310 us: 1.00x faster                                                           |
| pprint_pformat             | 1.32 sec                                                        | 1.33 sec: 1.01x slower                                                         |
| telco                      | 6.27 ms                                                         | 6.40 ms: 1.02x slower                                                          |
| tomli_loads                | 1.74 sec                                                        | 1.79 sec: 1.03x slower                                                         |
| crypto_pyaes               | 56.6 ms                                                         | 58.8 ms: 1.04x slower                                                          |
| sqlglot_parse              | 1.02 ms                                                         | 1.06 ms: 1.04x slower                                                          |
| bench_thread_pool          | 1.04 ms                                                         | 1.09 ms: 1.05x slower                                                          |
| python_startup_no_site     | 20.2 ms                                                         | 21.2 ms: 1.05x slower                                                          |
| 2to3                       | 255 ms                                                          | 268 ms: 1.05x slower                                                           |
| regex_v8                   | 15.5 ms                                                         | 16.3 ms: 1.05x slower                                                          |
| sqlglot_transpile          | 1.26 ms                                                         | 1.33 ms: 1.06x slower                                                          |
| deepcopy_memo              | 26.2 us                                                         | 27.8 us: 1.06x slower                                                          |
| sqlglot_normalize          | 223 ms                                                          | 237 ms: 1.06x slower                                                           |
| logging_format             | 8.59 us                                                         | 9.15 us: 1.06x slower                                                          |
| meteor_contest             | 78.1 ms                                                         | 83.2 ms: 1.06x slower                                                          |
| mdp                        | 1.70 sec                                                        | 1.81 sec: 1.07x slower                                                         |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 523 ms: 1.07x slower                                                           |
| richards                   | 33.4 ms                                                         | 35.6 ms: 1.07x slower                                                          |
| tornado_http               | 105 ms                                                          | 112 ms: 1.07x slower                                                           |
| unpickle_pure_python       | 162 us                                                          | 173 us: 1.07x slower                                                           |
| xml_etree_process          | 44.6 ms                                                         | 47.9 ms: 1.07x slower                                                          |
| docutils                   | 1.80 sec                                                        | 1.94 sec: 1.08x slower                                                         |
| xml_etree_parse            | 102 ms                                                          | 111 ms: 1.08x slower                                                           |
| sympy_expand               | 377 ms                                                          | 408 ms: 1.08x slower                                                           |
| logging_simple             | 7.89 us                                                         | 8.58 us: 1.09x slower                                                          |
| xml_etree_generate         | 61.9 ms                                                         | 67.3 ms: 1.09x slower                                                          |
| async_tree_memoization     | 302 ms                                                          | 329 ms: 1.09x slower                                                           |
| go                         | 111 ms                                                          | 121 ms: 1.09x slower                                                           |
| richards_super             | 37.0 ms                                                         | 40.6 ms: 1.10x slower                                                          |
| pycparser                  | 869 ms                                                          | 955 ms: 1.10x slower                                                           |
| sqlglot_optimize           | 42.4 ms                                                         | 46.8 ms: 1.10x slower                                                          |
| float                      | 56.4 ms                                                         | 62.3 ms: 1.10x slower                                                          |
| async_tree_none            | 245 ms                                                          | 270 ms: 1.10x slower                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 518 ms: 1.10x slower                                                           |
| regex_effbot               | 1.82 ms                                                         | 2.01 ms: 1.11x slower                                                          |
| fannkuch                   | 288 ms                                                          | 321 ms: 1.11x slower                                                           |
| sympy_str                  | 214 ms                                                          | 241 ms: 1.13x slower                                                           |
| nbody                      | 81.4 ms                                                         | 91.9 ms: 1.13x slower                                                          |
| coroutines                 | 16.1 ms                                                         | 18.3 ms: 1.14x slower                                                          |
| async_generators           | 267 ms                                                          | 304 ms: 1.14x slower                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 327 ms: 1.14x slower                                                           |
| sympy_sum                  | 108 ms                                                          | 123 ms: 1.14x slower                                                           |
| pyflate                    | 322 ms                                                          | 367 ms: 1.14x slower                                                           |
| sympy_integrate            | 15.2 ms                                                         | 17.4 ms: 1.14x slower                                                          |
| chaos                      | 49.4 ms                                                         | 57.2 ms: 1.16x slower                                                          |
| mako                       | 7.02 ms                                                         | 8.20 ms: 1.17x slower                                                          |
| xml_etree_iterparse        | 61.3 ms                                                         | 71.7 ms: 1.17x slower                                                          |
| regex_dna                  | 112 ms                                                          | 132 ms: 1.17x slower                                                           |
| scimark_monte_carlo        | 48.7 ms                                                         | 57.8 ms: 1.19x slower                                                          |
| scimark_sor                | 85.8 ms                                                         | 102 ms: 1.19x slower                                                           |
| scimark_fft                | 204 ms                                                          | 243 ms: 1.19x slower                                                           |
| comprehensions             | 13.1 us                                                         | 15.7 us: 1.19x slower                                                          |
| nqueens                    | 75.1 ms                                                         | 91.2 ms: 1.21x slower                                                          |
| async_tree_none_tg         | 216 ms                                                          | 264 ms: 1.22x slower                                                           |
| async_tree_io              | 530 ms                                                          | 651 ms: 1.23x slower                                                           |
| logging_silent             | 62.4 ns                                                         | 76.8 ns: 1.23x slower                                                          |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.63 ms: 1.26x slower                                                          |
| raytrace                   | 203 ms                                                          | 257 ms: 1.27x slower                                                           |
| async_tree_io_tg           | 499 ms                                                          | 634 ms: 1.27x slower                                                           |
| regex_compile              | 101 ms                                                          | 131 ms: 1.30x slower                                                           |
| scimark_lu                 | 60.7 ms                                                         | 79.2 ms: 1.30x slower                                                          |
| deltablue                  | 2.35 ms                                                         | 3.08 ms: 1.31x slower                                                          |
| hexiom                     | 4.60 ms                                                         | 6.24 ms: 1.36x slower                                                          |
| generators                 | 21.5 ms                                                         | 29.6 ms: 1.38x slower                                                          |
| spectral_norm              | 70.0 ms                                                         | 96.9 ms: 1.38x slower                                                          |
| coverage                   | 326 ms                                                          | 510 ms: 1.56x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.09x slower                                                                   |

Benchmark hidden because not significant (1): pathlib
Ignored benchmarks (16) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, django_template, dulwich_log, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (10) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e.json: asyncio_tcp, asyncio_tcp_ssl, dask, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.084x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown
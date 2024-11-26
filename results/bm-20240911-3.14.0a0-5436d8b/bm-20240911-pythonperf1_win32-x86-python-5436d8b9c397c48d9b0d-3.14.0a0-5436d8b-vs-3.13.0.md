# Results vs. 3.13.0

- fork: python
- ref: 5436d8b9c397c48d9b0d
- machine: windows-x86
- commit hash: 5436d8b
- commit date: 2024-09-11
- overall geometric mean: 1.031x faster
- HPT reliability: 99.07%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 249 ms: 1.03x faster                                                           |
| docutils       | 1.80 sec                                                        | 1.86 sec: 1.03x slower                                                         |
| html5lib       | 47.1 ms                                                         | 44.1 ms: 1.07x faster                                                          |
| tornado_http   | 105 ms                                                          | 94.8 ms: 1.10x faster                                                          |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 250 ms: 1.15x faster                                                           |
| async_tree_none            | 245 ms                                                          | 218 ms: 1.12x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 271 ms: 1.11x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 198 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 464 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 457 ms: 1.03x faster                                                           |
| async_tree_io_tg           | 499 ms                                                          | 510 ms: 1.02x slower                                                           |
| async_generators           | 267 ms                                                          | 305 ms: 1.14x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 18.7 ms: 1.16x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 196 ms: 1.04x faster                                                           |
| float          | 56.4 ms                                                         | 62.2 ms: 1.10x slower                                                          |
| nbody          | 81.4 ms                                                         | 91.9 ms: 1.13x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 16.3 ms: 1.05x slower                                                          |
| regex_effbot   | 1.82 ms                                                         | 1.92 ms: 1.06x slower                                                          |
| regex_dna      | 112 ms                                                          | 119 ms: 1.06x slower                                                           |
| regex_compile  | 101 ms                                                          | 108 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.6 us: 1.05x faster                                                          |
| json_dumps           | 7.53 ms                                                         | 7.62 ms: 1.01x slower                                                          |
| xml_etree_parse      | 102 ms                                                          | 108 ms: 1.06x slower                                                           |
| tomli_loads          | 1.74 sec                                                        | 1.89 sec: 1.08x slower                                                         |
| xml_etree_iterparse  | 61.3 ms                                                         | 66.9 ms: 1.09x slower                                                          |
| pickle_pure_python   | 239 us                                                          | 262 us: 1.09x slower                                                           |
| xml_etree_generate   | 61.9 ms                                                         | 68.2 ms: 1.10x slower                                                          |
| xml_etree_process    | 44.6 ms                                                         | 49.8 ms: 1.12x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 181 us: 1.12x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 24.0 ms: 1.18x faster                                                          |
| python_startup_no_site | 20.2 ms                                                         | 19.8 ms: 1.02x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 46.9 ms: 1.04x faster                                                          |
| django_template | 32.0 ms                                                         | 32.6 ms: 1.02x slower                                                          |
| genshi_text     | 21.7 ms                                                         | 22.2 ms: 1.02x slower                                                          |
| mako            | 7.02 ms                                                         | 8.18 ms: 1.17x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.04x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 737 us: 13.92x faster                                                          |
| coverage                   | 326 ms                                                          | 54.7 ms: 5.96x faster                                                          |
| create_gc_cycles           | 1.08 ms                                                         | 731 us: 1.48x faster                                                           |
| bench_mp_pool              | 93.6 ms                                                         | 69.9 ms: 1.34x faster                                                          |
| gc_traversal               | 1.76 ms                                                         | 1.39 ms: 1.26x faster                                                          |
| deepcopy                   | 311 us                                                          | 246 us: 1.26x faster                                                           |
| python_startup             | 28.3 ms                                                         | 24.0 ms: 1.18x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 22.3 us: 1.18x faster                                                          |
| deepcopy_reduce            | 2.94 us                                                         | 2.54 us: 1.16x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 250 ms: 1.15x faster                                                           |
| async_tree_none            | 245 ms                                                          | 218 ms: 1.12x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 271 ms: 1.11x faster                                                           |
| tornado_http               | 105 ms                                                          | 94.8 ms: 1.10x faster                                                          |
| async_tree_none_tg         | 216 ms                                                          | 198 ms: 1.09x faster                                                           |
| pathlib                    | 89.1 ms                                                         | 81.8 ms: 1.09x faster                                                          |
| html5lib                   | 47.1 ms                                                         | 44.1 ms: 1.07x faster                                                          |
| go                         | 111 ms                                                          | 104 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 464 ms: 1.06x faster                                                           |
| json_loads                 | 21.7 us                                                         | 20.6 us: 1.05x faster                                                          |
| genshi_xml                 | 49.0 ms                                                         | 46.9 ms: 1.04x faster                                                          |
| pidigits                   | 204 ms                                                          | 196 ms: 1.04x faster                                                           |
| json                       | 4.40 ms                                                         | 4.25 ms: 1.03x faster                                                          |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 457 ms: 1.03x faster                                                           |
| 2to3                       | 255 ms                                                          | 249 ms: 1.03x faster                                                           |
| python_startup_no_site     | 20.2 ms                                                         | 19.8 ms: 1.02x faster                                                          |
| pycparser                  | 869 ms                                                          | 864 ms: 1.00x faster                                                           |
| json_dumps                 | 7.53 ms                                                         | 7.62 ms: 1.01x slower                                                          |
| dulwich_log                | 50.2 ms                                                         | 50.8 ms: 1.01x slower                                                          |
| sqlglot_normalize          | 223 ms                                                          | 226 ms: 1.01x slower                                                           |
| sympy_integrate            | 15.2 ms                                                         | 15.4 ms: 1.01x slower                                                          |
| sympy_str                  | 214 ms                                                          | 218 ms: 1.02x slower                                                           |
| telco                      | 6.27 ms                                                         | 6.37 ms: 1.02x slower                                                          |
| django_template            | 32.0 ms                                                         | 32.6 ms: 1.02x slower                                                          |
| logging_simple             | 7.89 us                                                         | 8.04 us: 1.02x slower                                                          |
| sqlglot_optimize           | 42.4 ms                                                         | 43.2 ms: 1.02x slower                                                          |
| logging_format             | 8.59 us                                                         | 8.77 us: 1.02x slower                                                          |
| genshi_text                | 21.7 ms                                                         | 22.2 ms: 1.02x slower                                                          |
| async_tree_io_tg           | 499 ms                                                          | 510 ms: 1.02x slower                                                           |
| pprint_pformat             | 1.32 sec                                                        | 1.35 sec: 1.02x slower                                                         |
| crypto_pyaes               | 56.6 ms                                                         | 58.1 ms: 1.03x slower                                                          |
| typing_runtime_protocols   | 141 us                                                          | 145 us: 1.03x slower                                                           |
| sympy_expand               | 377 ms                                                          | 388 ms: 1.03x slower                                                           |
| docutils                   | 1.80 sec                                                        | 1.86 sec: 1.03x slower                                                         |
| meteor_contest             | 78.1 ms                                                         | 81.9 ms: 1.05x slower                                                          |
| regex_v8                   | 15.5 ms                                                         | 16.3 ms: 1.05x slower                                                          |
| regex_effbot               | 1.82 ms                                                         | 1.92 ms: 1.06x slower                                                          |
| xml_etree_parse            | 102 ms                                                          | 108 ms: 1.06x slower                                                           |
| sqlglot_parse              | 1.02 ms                                                         | 1.08 ms: 1.06x slower                                                          |
| regex_dna                  | 112 ms                                                          | 119 ms: 1.06x slower                                                           |
| comprehensions             | 13.1 us                                                         | 14.0 us: 1.06x slower                                                          |
| sqlglot_transpile          | 1.26 ms                                                         | 1.35 ms: 1.07x slower                                                          |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.08 ms: 1.07x slower                                                          |
| regex_compile              | 101 ms                                                          | 108 ms: 1.07x slower                                                           |
| tomli_loads                | 1.74 sec                                                        | 1.89 sec: 1.08x slower                                                         |
| spectral_norm              | 70.0 ms                                                         | 76.1 ms: 1.09x slower                                                          |
| chaos                      | 49.4 ms                                                         | 53.7 ms: 1.09x slower                                                          |
| xml_etree_iterparse        | 61.3 ms                                                         | 66.9 ms: 1.09x slower                                                          |
| pickle_pure_python         | 239 us                                                          | 262 us: 1.09x slower                                                           |
| xml_etree_generate         | 61.9 ms                                                         | 68.2 ms: 1.10x slower                                                          |
| float                      | 56.4 ms                                                         | 62.2 ms: 1.10x slower                                                          |
| xml_etree_process          | 44.6 ms                                                         | 49.8 ms: 1.12x slower                                                          |
| pyflate                    | 322 ms                                                          | 360 ms: 1.12x slower                                                           |
| hexiom                     | 4.60 ms                                                         | 5.15 ms: 1.12x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 181 us: 1.12x slower                                                           |
| scimark_lu                 | 60.7 ms                                                         | 68.1 ms: 1.12x slower                                                          |
| nbody                      | 81.4 ms                                                         | 91.9 ms: 1.13x slower                                                          |
| async_generators           | 267 ms                                                          | 305 ms: 1.14x slower                                                           |
| scimark_fft                | 204 ms                                                          | 236 ms: 1.16x slower                                                           |
| deltablue                  | 2.35 ms                                                         | 2.72 ms: 1.16x slower                                                          |
| raytrace                   | 203 ms                                                          | 235 ms: 1.16x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 18.7 ms: 1.16x slower                                                          |
| mako                       | 7.02 ms                                                         | 8.18 ms: 1.17x slower                                                          |
| fannkuch                   | 288 ms                                                          | 338 ms: 1.17x slower                                                           |
| scimark_monte_carlo        | 48.7 ms                                                         | 57.5 ms: 1.18x slower                                                          |
| richards                   | 33.4 ms                                                         | 39.8 ms: 1.19x slower                                                          |
| logging_silent             | 62.4 ns                                                         | 75.0 ns: 1.20x slower                                                          |
| scimark_sor                | 85.8 ms                                                         | 104 ms: 1.21x slower                                                           |
| richards_super             | 37.0 ms                                                         | 45.0 ms: 1.22x slower                                                          |
| generators                 | 21.5 ms                                                         | 26.2 ms: 1.22x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (7): bench_thread_pool, sympy_sum, nqueens, async_tree_io, mdp, pprint_safe_repr, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240911-3.14.0a0-5436d8b/bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.031x faster
# HPT report

- Reliability score: 99.07% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
# Results vs. 3.13.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: windows-x86
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.010x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 252 ms: 1.01x faster                                                           |
| docutils       | 1.80 sec                                                        | 1.87 sec: 1.04x slower                                                         |
| html5lib       | 47.1 ms                                                         | 46.7 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 287 ms                                                          | 253 ms: 1.14x faster                                                           |
| async_tree_none           | 245 ms                                                          | 219 ms: 1.12x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 275 ms: 1.10x faster                                                           |
| async_tree_none_tg        | 216 ms                                                          | 199 ms: 1.08x faster                                                           |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 479 ms: 1.02x faster                                                           |
| async_tree_io             | 530 ms                                                          | 540 ms: 1.02x slower                                                           |
| async_tree_io_tg          | 499 ms                                                          | 521 ms: 1.04x slower                                                           |
| coroutines                | 16.1 ms                                                         | 18.5 ms: 1.15x slower                                                          |
| async_generators          | 267 ms                                                          | 310 ms: 1.16x slower                                                           |
| Geometric mean            | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 196 ms: 1.04x faster                                                           |
| float          | 56.4 ms                                                         | 62.7 ms: 1.11x slower                                                          |
| nbody          | 81.4 ms                                                         | 93.9 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 16.1 ms: 1.04x slower                                                          |
| regex_dna      | 112 ms                                                          | 118 ms: 1.05x slower                                                           |
| regex_effbot   | 1.82 ms                                                         | 1.92 ms: 1.05x slower                                                          |
| regex_compile  | 101 ms                                                          | 111 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.7 us: 1.05x faster                                                          |
| json_dumps           | 7.53 ms                                                         | 7.61 ms: 1.01x slower                                                          |
| xml_etree_parse      | 102 ms                                                          | 107 ms: 1.05x slower                                                           |
| tomli_loads          | 1.74 sec                                                        | 1.91 sec: 1.10x slower                                                         |
| xml_etree_iterparse  | 61.3 ms                                                         | 67.3 ms: 1.10x slower                                                          |
| pickle_pure_python   | 239 us                                                          | 263 us: 1.10x slower                                                           |
| xml_etree_generate   | 61.9 ms                                                         | 70.2 ms: 1.13x slower                                                          |
| xml_etree_process    | 44.6 ms                                                         | 51.8 ms: 1.16x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 188 us: 1.16x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 24.8 ms: 1.14x faster                                                          |
| python_startup_no_site | 20.2 ms                                                         | 20.5 ms: 1.02x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 21.7 ms                                                         | 22.3 ms: 1.02x slower                                                          |
| django_template | 32.0 ms                                                         | 34.7 ms: 1.08x slower                                                          |
| mako            | 7.02 ms                                                         | 8.31 ms: 1.18x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.07x slower                                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                    | 10.3 ms                                                         | 743 us: 13.82x faster                                                          |
| coverage                  | 326 ms                                                          | 51.0 ms: 6.40x faster                                                          |
| create_gc_cycles          | 1.08 ms                                                         | 723 us: 1.50x faster                                                           |
| gc_traversal              | 1.76 ms                                                         | 1.41 ms: 1.25x faster                                                          |
| deepcopy                  | 311 us                                                          | 250 us: 1.24x faster                                                           |
| bench_mp_pool             | 93.6 ms                                                         | 77.0 ms: 1.22x faster                                                          |
| python_startup            | 28.3 ms                                                         | 24.8 ms: 1.14x faster                                                          |
| deepcopy_reduce           | 2.94 us                                                         | 2.59 us: 1.14x faster                                                          |
| async_tree_memoization_tg | 287 ms                                                          | 253 ms: 1.14x faster                                                           |
| async_tree_none           | 245 ms                                                          | 219 ms: 1.12x faster                                                           |
| deepcopy_memo             | 26.2 us                                                         | 23.5 us: 1.12x faster                                                          |
| async_tree_memoization    | 302 ms                                                          | 275 ms: 1.10x faster                                                           |
| async_tree_none_tg        | 216 ms                                                          | 199 ms: 1.08x faster                                                           |
| json_loads                | 21.7 us                                                         | 20.7 us: 1.05x faster                                                          |
| pidigits                  | 204 ms                                                          | 196 ms: 1.04x faster                                                           |
| json                      | 4.40 ms                                                         | 4.29 ms: 1.02x faster                                                          |
| pathlib                   | 89.1 ms                                                         | 87.2 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 479 ms: 1.02x faster                                                           |
| 2to3                      | 255 ms                                                          | 252 ms: 1.01x faster                                                           |
| html5lib                  | 47.1 ms                                                         | 46.7 ms: 1.01x faster                                                          |
| pycparser                 | 869 ms                                                          | 863 ms: 1.01x faster                                                           |
| nqueens                   | 75.1 ms                                                         | 75.5 ms: 1.01x slower                                                          |
| go                        | 111 ms                                                          | 111 ms: 1.01x slower                                                           |
| json_dumps                | 7.53 ms                                                         | 7.61 ms: 1.01x slower                                                          |
| pprint_safe_repr          | 658 ms                                                          | 668 ms: 1.01x slower                                                           |
| python_startup_no_site    | 20.2 ms                                                         | 20.5 ms: 1.02x slower                                                          |
| async_tree_io             | 530 ms                                                          | 540 ms: 1.02x slower                                                           |
| sympy_expand              | 377 ms                                                          | 384 ms: 1.02x slower                                                           |
| sympy_str                 | 214 ms                                                          | 218 ms: 1.02x slower                                                           |
| genshi_text               | 21.7 ms                                                         | 22.3 ms: 1.02x slower                                                          |
| sympy_integrate           | 15.2 ms                                                         | 15.6 ms: 1.03x slower                                                          |
| meteor_contest            | 78.1 ms                                                         | 80.6 ms: 1.03x slower                                                          |
| typing_runtime_protocols  | 141 us                                                          | 145 us: 1.03x slower                                                           |
| logging_format            | 8.59 us                                                         | 8.91 us: 1.04x slower                                                          |
| docutils                  | 1.80 sec                                                        | 1.87 sec: 1.04x slower                                                         |
| regex_v8                  | 15.5 ms                                                         | 16.1 ms: 1.04x slower                                                          |
| crypto_pyaes              | 56.6 ms                                                         | 59.0 ms: 1.04x slower                                                          |
| async_tree_io_tg          | 499 ms                                                          | 521 ms: 1.04x slower                                                           |
| logging_simple            | 7.89 us                                                         | 8.23 us: 1.04x slower                                                          |
| dulwich_log               | 50.2 ms                                                         | 52.5 ms: 1.05x slower                                                          |
| pylint                    | 225 ms                                                          | 235 ms: 1.05x slower                                                           |
| xml_etree_parse           | 102 ms                                                          | 107 ms: 1.05x slower                                                           |
| regex_dna                 | 112 ms                                                          | 118 ms: 1.05x slower                                                           |
| regex_effbot              | 1.82 ms                                                         | 1.92 ms: 1.05x slower                                                          |
| comprehensions            | 13.1 us                                                         | 13.9 us: 1.06x slower                                                          |
| pprint_pformat            | 1.32 sec                                                        | 1.40 sec: 1.06x slower                                                         |
| sqlglot_normalize         | 223 ms                                                          | 238 ms: 1.07x slower                                                           |
| sqlglot_optimize          | 42.4 ms                                                         | 45.8 ms: 1.08x slower                                                          |
| django_template           | 32.0 ms                                                         | 34.7 ms: 1.08x slower                                                          |
| sqlglot_parse             | 1.02 ms                                                         | 1.10 ms: 1.08x slower                                                          |
| sqlglot_transpile         | 1.26 ms                                                         | 1.37 ms: 1.09x slower                                                          |
| telco                     | 6.27 ms                                                         | 6.82 ms: 1.09x slower                                                          |
| scimark_sparse_mat_mult   | 2.88 ms                                                         | 3.15 ms: 1.09x slower                                                          |
| regex_compile             | 101 ms                                                          | 111 ms: 1.09x slower                                                           |
| tomli_loads               | 1.74 sec                                                        | 1.91 sec: 1.10x slower                                                         |
| xml_etree_iterparse       | 61.3 ms                                                         | 67.3 ms: 1.10x slower                                                          |
| pickle_pure_python        | 239 us                                                          | 263 us: 1.10x slower                                                           |
| float                     | 56.4 ms                                                         | 62.7 ms: 1.11x slower                                                          |
| spectral_norm             | 70.0 ms                                                         | 78.6 ms: 1.12x slower                                                          |
| xml_etree_generate        | 61.9 ms                                                         | 70.2 ms: 1.13x slower                                                          |
| coroutines                | 16.1 ms                                                         | 18.5 ms: 1.15x slower                                                          |
| pyflate                   | 322 ms                                                          | 370 ms: 1.15x slower                                                           |
| nbody                     | 81.4 ms                                                         | 93.9 ms: 1.15x slower                                                          |
| scimark_lu                | 60.7 ms                                                         | 70.5 ms: 1.16x slower                                                          |
| xml_etree_process         | 44.6 ms                                                         | 51.8 ms: 1.16x slower                                                          |
| async_generators          | 267 ms                                                          | 310 ms: 1.16x slower                                                           |
| unpickle_pure_python      | 162 us                                                          | 188 us: 1.16x slower                                                           |
| hexiom                    | 4.60 ms                                                         | 5.36 ms: 1.17x slower                                                          |
| scimark_fft               | 204 ms                                                          | 238 ms: 1.17x slower                                                           |
| chaos                     | 49.4 ms                                                         | 58.0 ms: 1.17x slower                                                          |
| fannkuch                  | 288 ms                                                          | 340 ms: 1.18x slower                                                           |
| logging_silent            | 62.4 ns                                                         | 73.7 ns: 1.18x slower                                                          |
| mako                      | 7.02 ms                                                         | 8.31 ms: 1.18x slower                                                          |
| deltablue                 | 2.35 ms                                                         | 2.81 ms: 1.20x slower                                                          |
| scimark_monte_carlo       | 48.7 ms                                                         | 58.3 ms: 1.20x slower                                                          |
| scimark_sor               | 85.8 ms                                                         | 104 ms: 1.21x slower                                                           |
| richards                  | 33.4 ms                                                         | 41.4 ms: 1.24x slower                                                          |
| raytrace                  | 203 ms                                                          | 252 ms: 1.24x slower                                                           |
| generators                | 21.5 ms                                                         | 26.8 ms: 1.25x slower                                                          |
| richards_super            | 37.0 ms                                                         | 46.8 ms: 1.26x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (6): bench_thread_pool, genshi_xml, sympy_sum, async_tree_cpu_io_mixed_tg, mdp, tornado_http
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.010x faster
# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown
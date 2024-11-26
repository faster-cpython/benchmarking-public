# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: windows-x86
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.030x faster
- HPT reliability: 99.18%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 250 ms: 1.02x faster                                                           |
| docutils       | 1.80 sec                                                        | 1.85 sec: 1.03x slower                                                         |
| html5lib       | 47.1 ms                                                         | 45.1 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 253 ms: 1.13x faster                                                           |
| async_tree_none            | 245 ms                                                          | 221 ms: 1.11x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 278 ms: 1.09x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 201 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 471 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 464 ms: 1.01x faster                                                           |
| async_tree_io_tg           | 499 ms                                                          | 518 ms: 1.04x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 17.4 ms: 1.08x slower                                                          |
| async_generators           | 267 ms                                                          | 300 ms: 1.12x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 200 ms: 1.02x faster                                                           |
| float          | 56.4 ms                                                         | 60.6 ms: 1.07x slower                                                          |
| nbody          | 81.4 ms                                                         | 96.5 ms: 1.19x slower                                                          |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 16.2 ms: 1.05x slower                                                          |
| regex_compile  | 101 ms                                                          | 107 ms: 1.05x slower                                                           |
| regex_effbot   | 1.82 ms                                                         | 2.00 ms: 1.10x slower                                                          |
| regex_dna      | 112 ms                                                          | 127 ms: 1.13x slower                                                           |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.4 us: 1.06x faster                                                          |
| json_dumps           | 7.53 ms                                                         | 7.21 ms: 1.04x faster                                                          |
| xml_etree_parse      | 102 ms                                                          | 109 ms: 1.06x slower                                                           |
| pickle_pure_python   | 239 us                                                          | 254 us: 1.06x slower                                                           |
| unpickle_pure_python | 162 us                                                          | 176 us: 1.09x slower                                                           |
| tomli_loads          | 1.74 sec                                                        | 1.90 sec: 1.09x slower                                                         |
| xml_etree_generate   | 61.9 ms                                                         | 69.1 ms: 1.12x slower                                                          |
| xml_etree_iterparse  | 61.3 ms                                                         | 68.5 ms: 1.12x slower                                                          |
| xml_etree_process    | 44.6 ms                                                         | 50.8 ms: 1.14x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 24.1 ms: 1.18x faster                                                          |
| python_startup_no_site | 20.2 ms                                                         | 19.9 ms: 1.01x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 46.4 ms: 1.06x faster                                                          |
| genshi_text     | 21.7 ms                                                         | 21.2 ms: 1.02x faster                                                          |
| django_template | 32.0 ms                                                         | 33.3 ms: 1.04x slower                                                          |
| mako            | 7.02 ms                                                         | 8.10 ms: 1.15x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.03x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 738 us: 13.91x faster                                                          |
| coverage                   | 326 ms                                                          | 52.5 ms: 6.21x faster                                                          |
| create_gc_cycles           | 1.08 ms                                                         | 741 us: 1.46x faster                                                           |
| deepcopy                   | 311 us                                                          | 243 us: 1.28x faster                                                           |
| bench_mp_pool              | 93.6 ms                                                         | 73.5 ms: 1.27x faster                                                          |
| gc_traversal               | 1.76 ms                                                         | 1.42 ms: 1.24x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 21.6 us: 1.21x faster                                                          |
| deepcopy_reduce            | 2.94 us                                                         | 2.50 us: 1.18x faster                                                          |
| python_startup             | 28.3 ms                                                         | 24.1 ms: 1.18x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 253 ms: 1.13x faster                                                           |
| async_tree_none            | 245 ms                                                          | 221 ms: 1.11x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 278 ms: 1.09x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 201 ms: 1.07x faster                                                           |
| go                         | 111 ms                                                          | 103 ms: 1.07x faster                                                           |
| json_loads                 | 21.7 us                                                         | 20.4 us: 1.06x faster                                                          |
| genshi_xml                 | 49.0 ms                                                         | 46.4 ms: 1.06x faster                                                          |
| json                       | 4.40 ms                                                         | 4.18 ms: 1.05x faster                                                          |
| html5lib                   | 47.1 ms                                                         | 45.1 ms: 1.04x faster                                                          |
| json_dumps                 | 7.53 ms                                                         | 7.21 ms: 1.04x faster                                                          |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 471 ms: 1.04x faster                                                           |
| genshi_text                | 21.7 ms                                                         | 21.2 ms: 1.02x faster                                                          |
| pathlib                    | 89.1 ms                                                         | 87.2 ms: 1.02x faster                                                          |
| 2to3                       | 255 ms                                                          | 250 ms: 1.02x faster                                                           |
| pprint_safe_repr           | 658 ms                                                          | 645 ms: 1.02x faster                                                           |
| pidigits                   | 204 ms                                                          | 200 ms: 1.02x faster                                                           |
| python_startup_no_site     | 20.2 ms                                                         | 19.9 ms: 1.01x faster                                                          |
| sympy_sum                  | 108 ms                                                          | 107 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 464 ms: 1.01x faster                                                           |
| sympy_expand               | 377 ms                                                          | 375 ms: 1.01x faster                                                           |
| pycparser                  | 869 ms                                                          | 864 ms: 1.01x faster                                                           |
| pprint_pformat             | 1.32 sec                                                        | 1.33 sec: 1.00x slower                                                         |
| logging_simple             | 7.89 us                                                         | 7.94 us: 1.01x slower                                                          |
| mdp                        | 1.70 sec                                                        | 1.72 sec: 1.01x slower                                                         |
| crypto_pyaes               | 56.6 ms                                                         | 57.8 ms: 1.02x slower                                                          |
| typing_runtime_protocols   | 141 us                                                          | 144 us: 1.02x slower                                                           |
| docutils                   | 1.80 sec                                                        | 1.85 sec: 1.03x slower                                                         |
| sqlglot_normalize          | 223 ms                                                          | 229 ms: 1.03x slower                                                           |
| async_tree_io_tg           | 499 ms                                                          | 518 ms: 1.04x slower                                                           |
| comprehensions             | 13.1 us                                                         | 13.6 us: 1.04x slower                                                          |
| django_template            | 32.0 ms                                                         | 33.3 ms: 1.04x slower                                                          |
| meteor_contest             | 78.1 ms                                                         | 81.3 ms: 1.04x slower                                                          |
| sqlglot_optimize           | 42.4 ms                                                         | 44.2 ms: 1.04x slower                                                          |
| sqlglot_transpile          | 1.26 ms                                                         | 1.32 ms: 1.05x slower                                                          |
| regex_v8                   | 15.5 ms                                                         | 16.2 ms: 1.05x slower                                                          |
| nqueens                    | 75.1 ms                                                         | 79.0 ms: 1.05x slower                                                          |
| regex_compile              | 101 ms                                                          | 107 ms: 1.05x slower                                                           |
| sqlglot_parse              | 1.02 ms                                                         | 1.08 ms: 1.06x slower                                                          |
| xml_etree_parse            | 102 ms                                                          | 109 ms: 1.06x slower                                                           |
| pickle_pure_python         | 239 us                                                          | 254 us: 1.06x slower                                                           |
| pylint                     | 225 ms                                                          | 239 ms: 1.07x slower                                                           |
| float                      | 56.4 ms                                                         | 60.6 ms: 1.07x slower                                                          |
| spectral_norm              | 70.0 ms                                                         | 75.5 ms: 1.08x slower                                                          |
| telco                      | 6.27 ms                                                         | 6.78 ms: 1.08x slower                                                          |
| coroutines                 | 16.1 ms                                                         | 17.4 ms: 1.08x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 176 us: 1.09x slower                                                           |
| tomli_loads                | 1.74 sec                                                        | 1.90 sec: 1.09x slower                                                         |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.17 ms: 1.10x slower                                                          |
| regex_effbot               | 1.82 ms                                                         | 2.00 ms: 1.10x slower                                                          |
| chaos                      | 49.4 ms                                                         | 54.6 ms: 1.11x slower                                                          |
| pyflate                    | 322 ms                                                          | 358 ms: 1.11x slower                                                           |
| xml_etree_generate         | 61.9 ms                                                         | 69.1 ms: 1.12x slower                                                          |
| xml_etree_iterparse        | 61.3 ms                                                         | 68.5 ms: 1.12x slower                                                          |
| raytrace                   | 203 ms                                                          | 227 ms: 1.12x slower                                                           |
| async_generators           | 267 ms                                                          | 300 ms: 1.12x slower                                                           |
| scimark_fft                | 204 ms                                                          | 231 ms: 1.13x slower                                                           |
| regex_dna                  | 112 ms                                                          | 127 ms: 1.13x slower                                                           |
| xml_etree_process          | 44.6 ms                                                         | 50.8 ms: 1.14x slower                                                          |
| scimark_sor                | 85.8 ms                                                         | 98.2 ms: 1.14x slower                                                          |
| scimark_monte_carlo        | 48.7 ms                                                         | 55.8 ms: 1.15x slower                                                          |
| deltablue                  | 2.35 ms                                                         | 2.70 ms: 1.15x slower                                                          |
| hexiom                     | 4.60 ms                                                         | 5.29 ms: 1.15x slower                                                          |
| fannkuch                   | 288 ms                                                          | 332 ms: 1.15x slower                                                           |
| mako                       | 7.02 ms                                                         | 8.10 ms: 1.15x slower                                                          |
| scimark_lu                 | 60.7 ms                                                         | 70.3 ms: 1.16x slower                                                          |
| logging_silent             | 62.4 ns                                                         | 72.8 ns: 1.17x slower                                                          |
| nbody                      | 81.4 ms                                                         | 96.5 ms: 1.19x slower                                                          |
| richards                   | 33.4 ms                                                         | 39.8 ms: 1.19x slower                                                          |
| richards_super             | 37.0 ms                                                         | 44.3 ms: 1.20x slower                                                          |
| generators                 | 21.5 ms                                                         | 26.7 ms: 1.24x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (7): logging_format, sympy_str, sympy_integrate, dulwich_log, tornado_http, async_tree_io, bench_thread_pool
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.030x faster
# HPT report

- Reliability score: 99.18% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
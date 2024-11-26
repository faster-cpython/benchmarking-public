# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: windows-x86
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.103x faster
- HPT reliability: 90.34%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 263 ms: 1.03x slower                                                           |
| docutils       | 1.80 sec                                                        | 2.00 sec: 1.11x slower                                                         |
| html5lib       | 47.1 ms                                                         | 47.5 ms: 1.01x slower                                                          |
| tornado_http   | 105 ms                                                          | 108 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 251 ms: 1.14x faster                                                           |
| async_tree_none            | 245 ms                                                          | 215 ms: 1.14x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 274 ms: 1.10x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 202 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 473 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 464 ms: 1.01x faster                                                           |
| async_tree_io_tg           | 499 ms                                                          | 515 ms: 1.03x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 17.9 ms: 1.11x slower                                                          |
| async_generators           | 267 ms                                                          | 309 ms: 1.16x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 47.8 ms: 1.70x faster                                                          |
| float          | 56.4 ms                                                         | 43.9 ms: 1.29x faster                                                          |
| pidigits       | 204 ms                                                          | 195 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                           | 1.32x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 102 ms: 1.01x slower                                                           |
| regex_v8       | 15.5 ms                                                         | 15.8 ms: 1.02x slower                                                          |
| regex_effbot   | 1.82 ms                                                         | 1.95 ms: 1.07x slower                                                          |
| regex_dna      | 112 ms                                                          | 122 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|---------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads         | 1.74 sec                                                        | 1.48 sec: 1.17x faster                                                         |
| xml_etree_generate  | 61.9 ms                                                         | 54.5 ms: 1.14x faster                                                          |
| json_dumps          | 7.53 ms                                                         | 6.86 ms: 1.10x faster                                                          |
| xml_etree_process   | 44.6 ms                                                         | 41.4 ms: 1.08x faster                                                          |
| json_loads          | 21.7 us                                                         | 20.9 us: 1.04x faster                                                          |
| pickle_pure_python  | 239 us                                                          | 233 us: 1.03x faster                                                           |
| xml_etree_parse     | 102 ms                                                          | 104 ms: 1.02x slower                                                           |
| xml_etree_iterparse | 61.3 ms                                                         | 62.5 ms: 1.02x slower                                                          |
| Geometric mean      | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 24.9 ms: 1.14x faster                                                          |
| python_startup_no_site | 20.2 ms                                                         | 21.0 ms: 1.04x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 5.60 ms: 1.25x faster                                                          |
| django_template | 32.0 ms                                                         | 33.6 ms: 1.05x slower                                                          |
| genshi_text     | 21.7 ms                                                         | 24.9 ms: 1.15x slower                                                          |
| genshi_xml      | 49.0 ms                                                         | 56.4 ms: 1.15x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.03x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 788 us: 13.02x faster                                                          |
| coverage                   | 326 ms                                                          | 51.6 ms: 6.33x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 15.0 us: 1.75x faster                                                          |
| nbody                      | 81.4 ms                                                         | 47.8 ms: 1.70x faster                                                          |
| spectral_norm              | 70.0 ms                                                         | 46.3 ms: 1.51x faster                                                          |
| create_gc_cycles           | 1.08 ms                                                         | 769 us: 1.41x faster                                                           |
| deepcopy                   | 311 us                                                          | 230 us: 1.35x faster                                                           |
| float                      | 56.4 ms                                                         | 43.9 ms: 1.29x faster                                                          |
| mako                       | 7.02 ms                                                         | 5.60 ms: 1.25x faster                                                          |
| scimark_sor                | 85.8 ms                                                         | 69.4 ms: 1.24x faster                                                          |
| scimark_fft                | 204 ms                                                          | 168 ms: 1.22x faster                                                           |
| fannkuch                   | 288 ms                                                          | 237 ms: 1.21x faster                                                           |
| gc_traversal               | 1.76 ms                                                         | 1.46 ms: 1.21x faster                                                          |
| crypto_pyaes               | 56.6 ms                                                         | 48.2 ms: 1.18x faster                                                          |
| deepcopy_reduce            | 2.94 us                                                         | 2.51 us: 1.17x faster                                                          |
| tomli_loads                | 1.74 sec                                                        | 1.48 sec: 1.17x faster                                                         |
| pyflate                    | 322 ms                                                          | 279 ms: 1.15x faster                                                           |
| deltablue                  | 2.35 ms                                                         | 2.06 ms: 1.14x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 251 ms: 1.14x faster                                                           |
| async_tree_none            | 245 ms                                                          | 215 ms: 1.14x faster                                                           |
| python_startup             | 28.3 ms                                                         | 24.9 ms: 1.14x faster                                                          |
| xml_etree_generate         | 61.9 ms                                                         | 54.5 ms: 1.14x faster                                                          |
| bench_mp_pool              | 93.6 ms                                                         | 82.7 ms: 1.13x faster                                                          |
| comprehensions             | 13.1 us                                                         | 11.8 us: 1.12x faster                                                          |
| pprint_safe_repr           | 658 ms                                                          | 596 ms: 1.10x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 274 ms: 1.10x faster                                                           |
| json_dumps                 | 7.53 ms                                                         | 6.86 ms: 1.10x faster                                                          |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 2.64 ms: 1.09x faster                                                          |
| go                         | 111 ms                                                          | 102 ms: 1.08x faster                                                           |
| xml_etree_process          | 44.6 ms                                                         | 41.4 ms: 1.08x faster                                                          |
| async_tree_none_tg         | 216 ms                                                          | 202 ms: 1.07x faster                                                           |
| meteor_contest             | 78.1 ms                                                         | 73.2 ms: 1.07x faster                                                          |
| pprint_pformat             | 1.32 sec                                                        | 1.24 sec: 1.07x faster                                                         |
| json                       | 4.40 ms                                                         | 4.14 ms: 1.06x faster                                                          |
| pycparser                  | 869 ms                                                          | 819 ms: 1.06x faster                                                           |
| logging_silent             | 62.4 ns                                                         | 59.4 ns: 1.05x faster                                                          |
| richards_super             | 37.0 ms                                                         | 35.5 ms: 1.04x faster                                                          |
| pidigits                   | 204 ms                                                          | 195 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 473 ms: 1.04x faster                                                           |
| json_loads                 | 21.7 us                                                         | 20.9 us: 1.04x faster                                                          |
| logging_format             | 8.59 us                                                         | 8.34 us: 1.03x faster                                                          |
| richards                   | 33.4 ms                                                         | 32.4 ms: 1.03x faster                                                          |
| pickle_pure_python         | 239 us                                                          | 233 us: 1.03x faster                                                           |
| pathlib                    | 89.1 ms                                                         | 86.8 ms: 1.03x faster                                                          |
| logging_simple             | 7.89 us                                                         | 7.71 us: 1.02x faster                                                          |
| telco                      | 6.27 ms                                                         | 6.14 ms: 1.02x faster                                                          |
| scimark_lu                 | 60.7 ms                                                         | 59.5 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 464 ms: 1.01x faster                                                           |
| dulwich_log                | 50.2 ms                                                         | 49.9 ms: 1.01x faster                                                          |
| regex_compile              | 101 ms                                                          | 102 ms: 1.01x slower                                                           |
| html5lib                   | 47.1 ms                                                         | 47.5 ms: 1.01x slower                                                          |
| sqlglot_parse              | 1.02 ms                                                         | 1.04 ms: 1.02x slower                                                          |
| xml_etree_parse            | 102 ms                                                          | 104 ms: 1.02x slower                                                           |
| xml_etree_iterparse        | 61.3 ms                                                         | 62.5 ms: 1.02x slower                                                          |
| regex_v8                   | 15.5 ms                                                         | 15.8 ms: 1.02x slower                                                          |
| mdp                        | 1.70 sec                                                        | 1.73 sec: 1.02x slower                                                         |
| typing_runtime_protocols   | 141 us                                                          | 144 us: 1.02x slower                                                           |
| scimark_monte_carlo        | 48.7 ms                                                         | 49.8 ms: 1.02x slower                                                          |
| async_tree_io_tg           | 499 ms                                                          | 515 ms: 1.03x slower                                                           |
| 2to3                       | 255 ms                                                          | 263 ms: 1.03x slower                                                           |
| tornado_http               | 105 ms                                                          | 108 ms: 1.03x slower                                                           |
| python_startup_no_site     | 20.2 ms                                                         | 21.0 ms: 1.04x slower                                                          |
| sqlglot_normalize          | 223 ms                                                          | 232 ms: 1.04x slower                                                           |
| sympy_str                  | 214 ms                                                          | 223 ms: 1.04x slower                                                           |
| nqueens                    | 75.1 ms                                                         | 78.3 ms: 1.04x slower                                                          |
| django_template            | 32.0 ms                                                         | 33.6 ms: 1.05x slower                                                          |
| sympy_expand               | 377 ms                                                          | 398 ms: 1.06x slower                                                           |
| sympy_sum                  | 108 ms                                                          | 114 ms: 1.06x slower                                                           |
| sqlglot_transpile          | 1.26 ms                                                         | 1.34 ms: 1.06x slower                                                          |
| hexiom                     | 4.60 ms                                                         | 4.91 ms: 1.07x slower                                                          |
| regex_effbot               | 1.82 ms                                                         | 1.95 ms: 1.07x slower                                                          |
| sqlglot_optimize           | 42.4 ms                                                         | 45.9 ms: 1.08x slower                                                          |
| chaos                      | 49.4 ms                                                         | 53.6 ms: 1.09x slower                                                          |
| regex_dna                  | 112 ms                                                          | 122 ms: 1.09x slower                                                           |
| sympy_integrate            | 15.2 ms                                                         | 16.8 ms: 1.10x slower                                                          |
| coroutines                 | 16.1 ms                                                         | 17.9 ms: 1.11x slower                                                          |
| docutils                   | 1.80 sec                                                        | 2.00 sec: 1.11x slower                                                         |
| generators                 | 21.5 ms                                                         | 24.5 ms: 1.14x slower                                                          |
| genshi_text                | 21.7 ms                                                         | 24.9 ms: 1.15x slower                                                          |
| genshi_xml                 | 49.0 ms                                                         | 56.4 ms: 1.15x slower                                                          |
| async_generators           | 267 ms                                                          | 309 ms: 1.16x slower                                                           |
| pylint                     | 225 ms                                                          | 269 ms: 1.20x slower                                                           |
| raytrace                   | 203 ms                                                          | 245 ms: 1.21x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.10x faster                                                                   |

Benchmark hidden because not significant (3): bench_thread_pool, unpickle_pure_python, async_tree_io
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.103x faster
# HPT report

- Reliability score: 90.34% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
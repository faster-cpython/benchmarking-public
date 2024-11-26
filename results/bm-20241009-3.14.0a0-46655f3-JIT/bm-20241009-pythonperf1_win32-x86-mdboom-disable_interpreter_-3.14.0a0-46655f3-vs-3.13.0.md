# Results vs. 3.13.0

- fork: mdboom
- ref: disable_interpreter_
- machine: windows-x86
- commit hash: 46655f3
- commit date: 2024-10-09
- overall geometric mean: 1.109x faster
- HPT reliability: 90.10%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 262 ms: 1.03x slower                                                           |
| docutils       | 1.80 sec                                                        | 2.05 sec: 1.14x slower                                                         |
| html5lib       | 47.1 ms                                                         | 45.3 ms: 1.04x faster                                                          |
| tornado_http   | 105 ms                                                          | 108 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 251 ms: 1.14x faster                                                           |
| async_tree_none            | 245 ms                                                          | 219 ms: 1.12x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 274 ms: 1.10x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 196 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 494 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 477 ms: 1.02x slower                                                           |
| async_tree_io_tg           | 499 ms                                                          | 510 ms: 1.02x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 18.1 ms: 1.12x slower                                                          |
| async_generators           | 267 ms                                                          | 326 ms: 1.22x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 52.9 ms: 1.54x faster                                                          |
| float          | 56.4 ms                                                         | 45.3 ms: 1.24x faster                                                          |
| pidigits       | 204 ms                                                          | 205 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.82 ms                                                         | 1.84 ms: 1.01x slower                                                          |
| regex_v8       | 15.5 ms                                                         | 15.7 ms: 1.02x slower                                                          |
| regex_dna      | 112 ms                                                          | 114 ms: 1.02x slower                                                           |
| regex_compile  | 101 ms                                                          | 106 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_generate   | 61.9 ms                                                         | 54.1 ms: 1.15x faster                                                          |
| tomli_loads          | 1.74 sec                                                        | 1.53 sec: 1.14x faster                                                         |
| json_dumps           | 7.53 ms                                                         | 6.79 ms: 1.11x faster                                                          |
| xml_etree_process    | 44.6 ms                                                         | 40.6 ms: 1.10x faster                                                          |
| json_loads           | 21.7 us                                                         | 21.2 us: 1.02x faster                                                          |
| unpickle_pure_python | 162 us                                                          | 159 us: 1.02x faster                                                           |
| xml_etree_iterparse  | 61.3 ms                                                         | 63.4 ms: 1.03x slower                                                          |
| pickle_pure_python   | 239 us                                                          | 250 us: 1.05x slower                                                           |
| xml_etree_parse      | 102 ms                                                          | 109 ms: 1.07x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 24.4 ms: 1.16x faster                                                          |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 5.69 ms: 1.23x faster                                                          |
| django_template | 32.0 ms                                                         | 32.8 ms: 1.02x slower                                                          |
| genshi_text     | 21.7 ms                                                         | 23.4 ms: 1.08x slower                                                          |
| genshi_xml      | 49.0 ms                                                         | 54.6 ms: 1.11x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.00x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 756 us: 13.57x faster                                                          |
| coverage                   | 326 ms                                                          | 51.6 ms: 6.32x faster                                                          |
| sqlglot_normalize          | 223 ms                                                          | 104 ms: 2.14x faster                                                           |
| deepcopy_memo              | 26.2 us                                                         | 15.2 us: 1.73x faster                                                          |
| nbody                      | 81.4 ms                                                         | 52.9 ms: 1.54x faster                                                          |
| create_gc_cycles           | 1.08 ms                                                         | 784 us: 1.38x faster                                                           |
| spectral_norm              | 70.0 ms                                                         | 50.9 ms: 1.37x faster                                                          |
| deepcopy                   | 311 us                                                          | 232 us: 1.34x faster                                                           |
| float                      | 56.4 ms                                                         | 45.3 ms: 1.24x faster                                                          |
| mako                       | 7.02 ms                                                         | 5.69 ms: 1.23x faster                                                          |
| deepcopy_reduce            | 2.94 us                                                         | 2.39 us: 1.23x faster                                                          |
| scimark_sor                | 85.8 ms                                                         | 69.6 ms: 1.23x faster                                                          |
| gc_traversal               | 1.76 ms                                                         | 1.44 ms: 1.22x faster                                                          |
| fannkuch                   | 288 ms                                                          | 239 ms: 1.21x faster                                                           |
| bench_mp_pool              | 93.6 ms                                                         | 77.8 ms: 1.20x faster                                                          |
| scimark_fft                | 204 ms                                                          | 170 ms: 1.20x faster                                                           |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 2.41 ms: 1.19x faster                                                          |
| crypto_pyaes               | 56.6 ms                                                         | 47.8 ms: 1.18x faster                                                          |
| python_startup             | 28.3 ms                                                         | 24.4 ms: 1.16x faster                                                          |
| deltablue                  | 2.35 ms                                                         | 2.03 ms: 1.15x faster                                                          |
| pprint_safe_repr           | 658 ms                                                          | 572 ms: 1.15x faster                                                           |
| xml_etree_generate         | 61.9 ms                                                         | 54.1 ms: 1.15x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 251 ms: 1.14x faster                                                           |
| tomli_loads                | 1.74 sec                                                        | 1.53 sec: 1.14x faster                                                         |
| async_tree_none            | 245 ms                                                          | 219 ms: 1.12x faster                                                           |
| pyflate                    | 322 ms                                                          | 288 ms: 1.12x faster                                                           |
| json_dumps                 | 7.53 ms                                                         | 6.79 ms: 1.11x faster                                                          |
| pprint_pformat             | 1.32 sec                                                        | 1.19 sec: 1.11x faster                                                         |
| go                         | 111 ms                                                          | 100 ms: 1.11x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 274 ms: 1.10x faster                                                           |
| logging_silent             | 62.4 ns                                                         | 56.7 ns: 1.10x faster                                                          |
| async_tree_none_tg         | 216 ms                                                          | 196 ms: 1.10x faster                                                           |
| xml_etree_process          | 44.6 ms                                                         | 40.6 ms: 1.10x faster                                                          |
| comprehensions             | 13.1 us                                                         | 12.1 us: 1.09x faster                                                          |
| json                       | 4.40 ms                                                         | 4.14 ms: 1.06x faster                                                          |
| pycparser                  | 869 ms                                                          | 824 ms: 1.05x faster                                                           |
| meteor_contest             | 78.1 ms                                                         | 74.3 ms: 1.05x faster                                                          |
| scimark_lu                 | 60.7 ms                                                         | 57.9 ms: 1.05x faster                                                          |
| scimark_monte_carlo        | 48.7 ms                                                         | 46.8 ms: 1.04x faster                                                          |
| telco                      | 6.27 ms                                                         | 6.02 ms: 1.04x faster                                                          |
| html5lib                   | 47.1 ms                                                         | 45.3 ms: 1.04x faster                                                          |
| bench_thread_pool          | 1.04 ms                                                         | 1.01 ms: 1.03x faster                                                          |
| logging_format             | 8.59 us                                                         | 8.36 us: 1.03x faster                                                          |
| logging_simple             | 7.89 us                                                         | 7.69 us: 1.03x faster                                                          |
| json_loads                 | 21.7 us                                                         | 21.2 us: 1.02x faster                                                          |
| unpickle_pure_python       | 162 us                                                          | 159 us: 1.02x faster                                                           |
| dulwich_log                | 50.2 ms                                                         | 49.7 ms: 1.01x faster                                                          |
| pathlib                    | 89.1 ms                                                         | 88.4 ms: 1.01x faster                                                          |
| pidigits                   | 204 ms                                                          | 205 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 494 ms: 1.01x slower                                                           |
| richards_super             | 37.0 ms                                                         | 37.4 ms: 1.01x slower                                                          |
| regex_effbot               | 1.82 ms                                                         | 1.84 ms: 1.01x slower                                                          |
| richards                   | 33.4 ms                                                         | 33.8 ms: 1.01x slower                                                          |
| regex_v8                   | 15.5 ms                                                         | 15.7 ms: 1.02x slower                                                          |
| regex_dna                  | 112 ms                                                          | 114 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 477 ms: 1.02x slower                                                           |
| async_tree_io_tg           | 499 ms                                                          | 510 ms: 1.02x slower                                                           |
| django_template            | 32.0 ms                                                         | 32.8 ms: 1.02x slower                                                          |
| 2to3                       | 255 ms                                                          | 262 ms: 1.03x slower                                                           |
| typing_runtime_protocols   | 141 us                                                          | 145 us: 1.03x slower                                                           |
| xml_etree_iterparse        | 61.3 ms                                                         | 63.4 ms: 1.03x slower                                                          |
| tornado_http               | 105 ms                                                          | 108 ms: 1.04x slower                                                           |
| pickle_pure_python         | 239 us                                                          | 250 us: 1.05x slower                                                           |
| regex_compile              | 101 ms                                                          | 106 ms: 1.05x slower                                                           |
| sqlglot_transpile          | 1.26 ms                                                         | 1.34 ms: 1.06x slower                                                          |
| xml_etree_parse            | 102 ms                                                          | 109 ms: 1.07x slower                                                           |
| sympy_expand               | 377 ms                                                          | 403 ms: 1.07x slower                                                           |
| sympy_str                  | 214 ms                                                          | 230 ms: 1.08x slower                                                           |
| genshi_text                | 21.7 ms                                                         | 23.4 ms: 1.08x slower                                                          |
| sympy_sum                  | 108 ms                                                          | 117 ms: 1.09x slower                                                           |
| chaos                      | 49.4 ms                                                         | 53.9 ms: 1.09x slower                                                          |
| hexiom                     | 4.60 ms                                                         | 5.08 ms: 1.11x slower                                                          |
| genshi_xml                 | 49.0 ms                                                         | 54.6 ms: 1.11x slower                                                          |
| coroutines                 | 16.1 ms                                                         | 18.1 ms: 1.12x slower                                                          |
| generators                 | 21.5 ms                                                         | 24.4 ms: 1.13x slower                                                          |
| docutils                   | 1.80 sec                                                        | 2.05 sec: 1.14x slower                                                         |
| sympy_integrate            | 15.2 ms                                                         | 17.6 ms: 1.16x slower                                                          |
| sqlglot_optimize           | 42.4 ms                                                         | 50.1 ms: 1.18x slower                                                          |
| async_generators           | 267 ms                                                          | 326 ms: 1.22x slower                                                           |
| raytrace                   | 203 ms                                                          | 253 ms: 1.25x slower                                                           |
| pylint                     | 225 ms                                                          | 281 ms: 1.25x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                                   |

Benchmark hidden because not significant (5): nqueens, mdp, sqlglot_parse, python_startup_no_site, async_tree_io
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241009-3.14.0a0-46655f3-JIT/bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.109x faster
# HPT report

- Reliability score: 90.10% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
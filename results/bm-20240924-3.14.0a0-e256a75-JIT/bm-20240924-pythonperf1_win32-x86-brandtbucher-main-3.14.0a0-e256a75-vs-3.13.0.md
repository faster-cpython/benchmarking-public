# Results vs. 3.13.0

- fork: brandtbucher
- ref: main
- machine: windows-x86
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.116x faster
- HPT reliability: 98.91%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 258 ms: 1.01x slower                                                 |
| docutils       | 1.80 sec                                                        | 2.01 sec: 1.12x slower                                               |
| html5lib       | 47.1 ms                                                         | 46.6 ms: 1.01x faster                                                |
| tornado_http   | 105 ms                                                          | 99.4 ms: 1.05x faster                                                |
| Geometric mean | (ref)                                                           | 1.02x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg | 287 ms                                                          | 253 ms: 1.13x faster                                                 |
| async_tree_none           | 245 ms                                                          | 216 ms: 1.13x faster                                                 |
| async_tree_memoization    | 302 ms                                                          | 272 ms: 1.11x faster                                                 |
| async_tree_none_tg        | 216 ms                                                          | 199 ms: 1.08x faster                                                 |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 475 ms: 1.03x faster                                                 |
| async_tree_io_tg          | 499 ms                                                          | 517 ms: 1.04x slower                                                 |
| coroutines                | 16.1 ms                                                         | 19.2 ms: 1.19x slower                                                |
| async_generators          | 267 ms                                                          | 327 ms: 1.23x slower                                                 |
| Geometric mean            | (ref)                                                           | 1.00x faster                                                         |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 49.5 ms: 1.64x faster                                                |
| float          | 56.4 ms                                                         | 44.1 ms: 1.28x faster                                                |
| pidigits       | 204 ms                                                          | 198 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                           | 1.29x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 103 ms: 1.02x slower                                                 |
| regex_v8       | 15.5 ms                                                         | 15.8 ms: 1.02x slower                                                |
| regex_effbot   | 1.82 ms                                                         | 1.95 ms: 1.07x slower                                                |
| regex_dna      | 112 ms                                                          | 121 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                           | 1.05x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|---------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate  | 61.9 ms                                                         | 53.6 ms: 1.15x faster                                                |
| tomli_loads         | 1.74 sec                                                        | 1.54 sec: 1.13x faster                                               |
| xml_etree_process   | 44.6 ms                                                         | 39.6 ms: 1.13x faster                                                |
| json_dumps          | 7.53 ms                                                         | 7.06 ms: 1.07x faster                                                |
| json_loads          | 21.7 us                                                         | 20.9 us: 1.04x faster                                                |
| pickle_pure_python  | 239 us                                                          | 236 us: 1.01x faster                                                 |
| xml_etree_iterparse | 61.3 ms                                                         | 61.9 ms: 1.01x slower                                                |
| xml_etree_parse     | 102 ms                                                          | 104 ms: 1.02x slower                                                 |
| Geometric mean      | (ref)                                                           | 1.05x faster                                                         |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 24.3 ms: 1.16x faster                                                |
| Geometric mean | (ref)                                                           | 1.08x faster                                                         |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 5.52 ms: 1.27x faster                                                |
| django_template | 32.0 ms                                                         | 33.4 ms: 1.04x slower                                                |
| genshi_text     | 21.7 ms                                                         | 23.6 ms: 1.09x slower                                                |
| genshi_xml      | 49.0 ms                                                         | 55.9 ms: 1.14x slower                                                |
| Geometric mean  | (ref)                                                           | 1.00x slower                                                         |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| thrift                    | 10.3 ms                                                         | 762 us: 13.46x faster                                                |
| coverage                  | 326 ms                                                          | 51.6 ms: 6.33x faster                                                |
| sqlglot_normalize         | 223 ms                                                          | 102 ms: 2.18x faster                                                 |
| deepcopy_memo             | 26.2 us                                                         | 15.1 us: 1.74x faster                                                |
| nbody                     | 81.4 ms                                                         | 49.5 ms: 1.64x faster                                                |
| spectral_norm             | 70.0 ms                                                         | 46.1 ms: 1.52x faster                                                |
| create_gc_cycles          | 1.08 ms                                                         | 742 us: 1.46x faster                                                 |
| deepcopy                  | 311 us                                                          | 238 us: 1.31x faster                                                 |
| float                     | 56.4 ms                                                         | 44.1 ms: 1.28x faster                                                |
| scimark_sor               | 85.8 ms                                                         | 67.4 ms: 1.27x faster                                                |
| mako                      | 7.02 ms                                                         | 5.52 ms: 1.27x faster                                                |
| bench_mp_pool             | 93.6 ms                                                         | 75.9 ms: 1.23x faster                                                |
| gc_traversal              | 1.76 ms                                                         | 1.44 ms: 1.23x faster                                                |
| fannkuch                  | 288 ms                                                          | 243 ms: 1.19x faster                                                 |
| scimark_fft               | 204 ms                                                          | 173 ms: 1.18x faster                                                 |
| deepcopy_reduce           | 2.94 us                                                         | 2.51 us: 1.17x faster                                                |
| crypto_pyaes              | 56.6 ms                                                         | 48.6 ms: 1.17x faster                                                |
| python_startup            | 28.3 ms                                                         | 24.3 ms: 1.16x faster                                                |
| xml_etree_generate        | 61.9 ms                                                         | 53.6 ms: 1.15x faster                                                |
| pyflate                   | 322 ms                                                          | 279 ms: 1.15x faster                                                 |
| deltablue                 | 2.35 ms                                                         | 2.07 ms: 1.14x faster                                                |
| async_tree_memoization_tg | 287 ms                                                          | 253 ms: 1.13x faster                                                 |
| async_tree_none           | 245 ms                                                          | 216 ms: 1.13x faster                                                 |
| tomli_loads               | 1.74 sec                                                        | 1.54 sec: 1.13x faster                                               |
| xml_etree_process         | 44.6 ms                                                         | 39.6 ms: 1.13x faster                                                |
| go                        | 111 ms                                                          | 99.3 ms: 1.12x faster                                                |
| async_tree_memoization    | 302 ms                                                          | 272 ms: 1.11x faster                                                 |
| comprehensions            | 13.1 us                                                         | 11.9 us: 1.11x faster                                                |
| pprint_safe_repr          | 658 ms                                                          | 595 ms: 1.11x faster                                                 |
| telco                     | 6.27 ms                                                         | 5.68 ms: 1.10x faster                                                |
| scimark_sparse_mat_mult   | 2.88 ms                                                         | 2.62 ms: 1.10x faster                                                |
| async_tree_none_tg        | 216 ms                                                          | 199 ms: 1.08x faster                                                 |
| json                      | 4.40 ms                                                         | 4.06 ms: 1.08x faster                                                |
| logging_silent            | 62.4 ns                                                         | 58.5 ns: 1.07x faster                                                |
| pathlib                   | 89.1 ms                                                         | 83.5 ms: 1.07x faster                                                |
| json_dumps                | 7.53 ms                                                         | 7.06 ms: 1.07x faster                                                |
| pycparser                 | 869 ms                                                          | 819 ms: 1.06x faster                                                 |
| meteor_contest            | 78.1 ms                                                         | 74.2 ms: 1.05x faster                                                |
| tornado_http              | 105 ms                                                          | 99.4 ms: 1.05x faster                                                |
| pprint_pformat            | 1.32 sec                                                        | 1.26 sec: 1.05x faster                                               |
| dulwich_log               | 50.2 ms                                                         | 48.1 ms: 1.04x faster                                                |
| bench_thread_pool         | 1.04 ms                                                         | 1.00 ms: 1.04x faster                                                |
| json_loads                | 21.7 us                                                         | 20.9 us: 1.04x faster                                                |
| richards_super            | 37.0 ms                                                         | 35.9 ms: 1.03x faster                                                |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 475 ms: 1.03x faster                                                 |
| pidigits                  | 204 ms                                                          | 198 ms: 1.03x faster                                                 |
| mdp                       | 1.70 sec                                                        | 1.66 sec: 1.02x faster                                               |
| scimark_lu                | 60.7 ms                                                         | 59.7 ms: 1.02x faster                                                |
| richards                  | 33.4 ms                                                         | 32.9 ms: 1.02x faster                                                |
| pickle_pure_python        | 239 us                                                          | 236 us: 1.01x faster                                                 |
| logging_simple            | 7.89 us                                                         | 7.80 us: 1.01x faster                                                |
| html5lib                  | 47.1 ms                                                         | 46.6 ms: 1.01x faster                                                |
| logging_format            | 8.59 us                                                         | 8.51 us: 1.01x faster                                                |
| xml_etree_iterparse       | 61.3 ms                                                         | 61.9 ms: 1.01x slower                                                |
| 2to3                      | 255 ms                                                          | 258 ms: 1.01x slower                                                 |
| regex_compile             | 101 ms                                                          | 103 ms: 1.02x slower                                                 |
| xml_etree_parse           | 102 ms                                                          | 104 ms: 1.02x slower                                                 |
| regex_v8                  | 15.5 ms                                                         | 15.8 ms: 1.02x slower                                                |
| typing_runtime_protocols  | 141 us                                                          | 144 us: 1.03x slower                                                 |
| sqlglot_parse             | 1.02 ms                                                         | 1.06 ms: 1.03x slower                                                |
| async_tree_io_tg          | 499 ms                                                          | 517 ms: 1.04x slower                                                 |
| scimark_monte_carlo       | 48.7 ms                                                         | 50.6 ms: 1.04x slower                                                |
| nqueens                   | 75.1 ms                                                         | 78.2 ms: 1.04x slower                                                |
| sympy_str                 | 214 ms                                                          | 223 ms: 1.04x slower                                                 |
| django_template           | 32.0 ms                                                         | 33.4 ms: 1.04x slower                                                |
| sympy_sum                 | 108 ms                                                          | 114 ms: 1.05x slower                                                 |
| sympy_expand              | 377 ms                                                          | 399 ms: 1.06x slower                                                 |
| hexiom                    | 4.60 ms                                                         | 4.91 ms: 1.07x slower                                                |
| regex_effbot              | 1.82 ms                                                         | 1.95 ms: 1.07x slower                                                |
| sqlglot_transpile         | 1.26 ms                                                         | 1.35 ms: 1.07x slower                                                |
| regex_dna                 | 112 ms                                                          | 121 ms: 1.08x slower                                                 |
| genshi_text               | 21.7 ms                                                         | 23.6 ms: 1.09x slower                                                |
| generators                | 21.5 ms                                                         | 23.7 ms: 1.10x slower                                                |
| sympy_integrate           | 15.2 ms                                                         | 16.8 ms: 1.11x slower                                                |
| docutils                  | 1.80 sec                                                        | 2.01 sec: 1.12x slower                                               |
| chaos                     | 49.4 ms                                                         | 55.1 ms: 1.12x slower                                                |
| sqlglot_optimize          | 42.4 ms                                                         | 47.7 ms: 1.12x slower                                                |
| genshi_xml                | 49.0 ms                                                         | 55.9 ms: 1.14x slower                                                |
| coroutines                | 16.1 ms                                                         | 19.2 ms: 1.19x slower                                                |
| pylint                    | 225 ms                                                          | 268 ms: 1.19x slower                                                 |
| raytrace                  | 203 ms                                                          | 248 ms: 1.22x slower                                                 |
| async_generators          | 267 ms                                                          | 327 ms: 1.23x slower                                                 |
| Geometric mean            | (ref)                                                           | 1.12x faster                                                         |

Benchmark hidden because not significant (4): python_startup_no_site, unpickle_pure_python, async_tree_cpu_io_mixed_tg, async_tree_io
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.116x faster
# HPT report

- Reliability score: 98.91% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
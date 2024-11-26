# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: windows-x86
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.106x faster
- HPT reliability: 98.48%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 258 ms: 1.01x slower                                                           |
| docutils       | 1.80 sec                                                        | 1.97 sec: 1.09x slower                                                         |
| html5lib       | 47.1 ms                                                         | 46.8 ms: 1.01x faster                                                          |
| tornado_http   | 105 ms                                                          | 100 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 287 ms                                                          | 255 ms: 1.12x faster                                                           |
| async_tree_none           | 245 ms                                                          | 221 ms: 1.11x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 275 ms: 1.10x faster                                                           |
| async_tree_none_tg        | 216 ms                                                          | 201 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 472 ms: 1.04x faster                                                           |
| async_tree_io             | 530 ms                                                          | 541 ms: 1.02x slower                                                           |
| async_tree_io_tg          | 499 ms                                                          | 521 ms: 1.04x slower                                                           |
| coroutines                | 16.1 ms                                                         | 18.1 ms: 1.13x slower                                                          |
| async_generators          | 267 ms                                                          | 335 ms: 1.26x slower                                                           |
| Geometric mean            | (ref)                                                           | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 50.5 ms: 1.61x faster                                                          |
| float          | 56.4 ms                                                         | 43.5 ms: 1.30x faster                                                          |
| pidigits       | 204 ms                                                          | 199 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.29x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 102 ms: 1.01x slower                                                           |
| regex_v8       | 15.5 ms                                                         | 15.8 ms: 1.02x slower                                                          |
| regex_dna      | 112 ms                                                          | 119 ms: 1.06x slower                                                           |
| regex_effbot   | 1.82 ms                                                         | 1.97 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_generate   | 61.9 ms                                                         | 53.5 ms: 1.16x faster                                                          |
| tomli_loads          | 1.74 sec                                                        | 1.53 sec: 1.14x faster                                                         |
| xml_etree_process    | 44.6 ms                                                         | 39.7 ms: 1.12x faster                                                          |
| json_dumps           | 7.53 ms                                                         | 7.03 ms: 1.07x faster                                                          |
| json_loads           | 21.7 us                                                         | 21.4 us: 1.01x faster                                                          |
| xml_etree_iterparse  | 61.3 ms                                                         | 60.9 ms: 1.01x faster                                                          |
| unpickle_pure_python | 162 us                                                          | 163 us: 1.01x slower                                                           |
| pickle_pure_python   | 239 us                                                          | 242 us: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 24.0 ms: 1.18x faster                                                          |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 5.47 ms: 1.28x faster                                                          |
| django_template | 32.0 ms                                                         | 34.0 ms: 1.06x slower                                                          |
| genshi_xml      | 49.0 ms                                                         | 53.8 ms: 1.10x slower                                                          |
| genshi_text     | 21.7 ms                                                         | 24.1 ms: 1.11x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.00x slower                                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                    | 10.3 ms                                                         | 790 us: 12.99x faster                                                          |
| coverage                  | 326 ms                                                          | 53.8 ms: 6.06x faster                                                          |
| deepcopy_memo             | 26.2 us                                                         | 15.2 us: 1.73x faster                                                          |
| nbody                     | 81.4 ms                                                         | 50.5 ms: 1.61x faster                                                          |
| spectral_norm             | 70.0 ms                                                         | 46.6 ms: 1.50x faster                                                          |
| create_gc_cycles          | 1.08 ms                                                         | 745 us: 1.45x faster                                                           |
| deepcopy                  | 311 us                                                          | 233 us: 1.33x faster                                                           |
| float                     | 56.4 ms                                                         | 43.5 ms: 1.30x faster                                                          |
| mako                      | 7.02 ms                                                         | 5.47 ms: 1.28x faster                                                          |
| scimark_sor               | 85.8 ms                                                         | 68.0 ms: 1.26x faster                                                          |
| bench_mp_pool             | 93.6 ms                                                         | 74.2 ms: 1.26x faster                                                          |
| gc_traversal              | 1.76 ms                                                         | 1.44 ms: 1.22x faster                                                          |
| scimark_sparse_mat_mult   | 2.88 ms                                                         | 2.36 ms: 1.22x faster                                                          |
| fannkuch                  | 288 ms                                                          | 237 ms: 1.21x faster                                                           |
| python_startup            | 28.3 ms                                                         | 24.0 ms: 1.18x faster                                                          |
| crypto_pyaes              | 56.6 ms                                                         | 48.4 ms: 1.17x faster                                                          |
| scimark_fft               | 204 ms                                                          | 175 ms: 1.16x faster                                                           |
| deltablue                 | 2.35 ms                                                         | 2.02 ms: 1.16x faster                                                          |
| deepcopy_reduce           | 2.94 us                                                         | 2.53 us: 1.16x faster                                                          |
| xml_etree_generate        | 61.9 ms                                                         | 53.5 ms: 1.16x faster                                                          |
| pyflate                   | 322 ms                                                          | 282 ms: 1.14x faster                                                           |
| tomli_loads               | 1.74 sec                                                        | 1.53 sec: 1.14x faster                                                         |
| comprehensions            | 13.1 us                                                         | 11.6 us: 1.14x faster                                                          |
| async_tree_memoization_tg | 287 ms                                                          | 255 ms: 1.12x faster                                                           |
| xml_etree_process         | 44.6 ms                                                         | 39.7 ms: 1.12x faster                                                          |
| async_tree_none           | 245 ms                                                          | 221 ms: 1.11x faster                                                           |
| pprint_safe_repr          | 658 ms                                                          | 598 ms: 1.10x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 275 ms: 1.10x faster                                                           |
| go                        | 111 ms                                                          | 102 ms: 1.09x faster                                                           |
| meteor_contest            | 78.1 ms                                                         | 71.8 ms: 1.09x faster                                                          |
| pathlib                   | 89.1 ms                                                         | 83.1 ms: 1.07x faster                                                          |
| async_tree_none_tg        | 216 ms                                                          | 201 ms: 1.07x faster                                                           |
| json_dumps                | 7.53 ms                                                         | 7.03 ms: 1.07x faster                                                          |
| pprint_pformat            | 1.32 sec                                                        | 1.25 sec: 1.06x faster                                                         |
| pycparser                 | 869 ms                                                          | 825 ms: 1.05x faster                                                           |
| telco                     | 6.27 ms                                                         | 6.00 ms: 1.05x faster                                                          |
| logging_silent            | 62.4 ns                                                         | 59.7 ns: 1.04x faster                                                          |
| json                      | 4.40 ms                                                         | 4.22 ms: 1.04x faster                                                          |
| tornado_http              | 105 ms                                                          | 100 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 472 ms: 1.04x faster                                                           |
| richards_super            | 37.0 ms                                                         | 35.9 ms: 1.03x faster                                                          |
| logging_format            | 8.59 us                                                         | 8.34 us: 1.03x faster                                                          |
| dulwich_log               | 50.2 ms                                                         | 48.8 ms: 1.03x faster                                                          |
| pidigits                  | 204 ms                                                          | 199 ms: 1.02x faster                                                           |
| logging_simple            | 7.89 us                                                         | 7.72 us: 1.02x faster                                                          |
| richards                  | 33.4 ms                                                         | 32.8 ms: 1.02x faster                                                          |
| scimark_lu                | 60.7 ms                                                         | 60.0 ms: 1.01x faster                                                          |
| json_loads                | 21.7 us                                                         | 21.4 us: 1.01x faster                                                          |
| mdp                       | 1.70 sec                                                        | 1.69 sec: 1.01x faster                                                         |
| html5lib                  | 47.1 ms                                                         | 46.8 ms: 1.01x faster                                                          |
| xml_etree_iterparse       | 61.3 ms                                                         | 60.9 ms: 1.01x faster                                                          |
| regex_compile             | 101 ms                                                          | 102 ms: 1.01x slower                                                           |
| unpickle_pure_python      | 162 us                                                          | 163 us: 1.01x slower                                                           |
| 2to3                      | 255 ms                                                          | 258 ms: 1.01x slower                                                           |
| pickle_pure_python        | 239 us                                                          | 242 us: 1.01x slower                                                           |
| nqueens                   | 75.1 ms                                                         | 76.2 ms: 1.01x slower                                                          |
| sqlglot_parse             | 1.02 ms                                                         | 1.04 ms: 1.02x slower                                                          |
| async_tree_io             | 530 ms                                                          | 541 ms: 1.02x slower                                                           |
| regex_v8                  | 15.5 ms                                                         | 15.8 ms: 1.02x slower                                                          |
| sympy_str                 | 214 ms                                                          | 220 ms: 1.03x slower                                                           |
| scimark_monte_carlo       | 48.7 ms                                                         | 50.4 ms: 1.03x slower                                                          |
| sqlglot_normalize         | 223 ms                                                          | 231 ms: 1.04x slower                                                           |
| typing_runtime_protocols  | 141 us                                                          | 146 us: 1.04x slower                                                           |
| async_tree_io_tg          | 499 ms                                                          | 521 ms: 1.04x slower                                                           |
| sympy_expand              | 377 ms                                                          | 394 ms: 1.05x slower                                                           |
| sympy_sum                 | 108 ms                                                          | 113 ms: 1.05x slower                                                           |
| sqlglot_transpile         | 1.26 ms                                                         | 1.33 ms: 1.05x slower                                                          |
| hexiom                    | 4.60 ms                                                         | 4.86 ms: 1.06x slower                                                          |
| regex_dna                 | 112 ms                                                          | 119 ms: 1.06x slower                                                           |
| django_template           | 32.0 ms                                                         | 34.0 ms: 1.06x slower                                                          |
| chaos                     | 49.4 ms                                                         | 53.3 ms: 1.08x slower                                                          |
| sqlglot_optimize          | 42.4 ms                                                         | 46.0 ms: 1.08x slower                                                          |
| regex_effbot              | 1.82 ms                                                         | 1.97 ms: 1.08x slower                                                          |
| docutils                  | 1.80 sec                                                        | 1.97 sec: 1.09x slower                                                         |
| sympy_integrate           | 15.2 ms                                                         | 16.7 ms: 1.10x slower                                                          |
| genshi_xml                | 49.0 ms                                                         | 53.8 ms: 1.10x slower                                                          |
| generators                | 21.5 ms                                                         | 23.8 ms: 1.11x slower                                                          |
| genshi_text               | 21.7 ms                                                         | 24.1 ms: 1.11x slower                                                          |
| coroutines                | 16.1 ms                                                         | 18.1 ms: 1.13x slower                                                          |
| pylint                    | 225 ms                                                          | 268 ms: 1.19x slower                                                           |
| raytrace                  | 203 ms                                                          | 244 ms: 1.20x slower                                                           |
| async_generators          | 267 ms                                                          | 335 ms: 1.26x slower                                                           |
| Geometric mean            | (ref)                                                           | 1.11x faster                                                                   |

Benchmark hidden because not significant (4): bench_thread_pool, python_startup_no_site, async_tree_cpu_io_mixed_tg, xml_etree_parse
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.106x faster
# HPT report

- Reliability score: 98.48% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
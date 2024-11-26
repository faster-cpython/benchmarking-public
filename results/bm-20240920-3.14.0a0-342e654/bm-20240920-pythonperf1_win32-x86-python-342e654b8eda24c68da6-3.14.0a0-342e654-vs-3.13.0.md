# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: windows-x86
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.021x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 1.80 sec                                                        | 1.87 sec: 1.04x slower                                                         |
| tornado_http   | 105 ms                                                          | 95.6 ms: 1.09x faster                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 252 ms: 1.14x faster                                                           |
| async_tree_none            | 245 ms                                                          | 223 ms: 1.10x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 277 ms: 1.09x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 200 ms: 1.08x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 475 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 460 ms: 1.02x faster                                                           |
| async_tree_io              | 530 ms                                                          | 544 ms: 1.03x slower                                                           |
| async_tree_io_tg           | 499 ms                                                          | 521 ms: 1.04x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 18.1 ms: 1.12x slower                                                          |
| async_generators           | 267 ms                                                          | 300 ms: 1.13x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 197 ms: 1.03x faster                                                           |
| float          | 56.4 ms                                                         | 61.2 ms: 1.09x slower                                                          |
| nbody          | 81.4 ms                                                         | 91.0 ms: 1.12x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 16.1 ms: 1.04x slower                                                          |
| regex_compile  | 101 ms                                                          | 110 ms: 1.09x slower                                                           |
| regex_effbot   | 1.82 ms                                                         | 1.99 ms: 1.09x slower                                                          |
| regex_dna      | 112 ms                                                          | 128 ms: 1.14x slower                                                           |
| Geometric mean | (ref)                                                           | 1.09x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 7.53 ms                                                         | 7.45 ms: 1.01x faster                                                          |
| json_loads           | 21.7 us                                                         | 21.5 us: 1.01x faster                                                          |
| xml_etree_parse      | 102 ms                                                          | 109 ms: 1.06x slower                                                           |
| xml_etree_generate   | 61.9 ms                                                         | 67.3 ms: 1.09x slower                                                          |
| pickle_pure_python   | 239 us                                                          | 261 us: 1.09x slower                                                           |
| unpickle_pure_python | 162 us                                                          | 177 us: 1.09x slower                                                           |
| xml_etree_process    | 44.6 ms                                                         | 49.2 ms: 1.10x slower                                                          |
| tomli_loads          | 1.74 sec                                                        | 1.92 sec: 1.10x slower                                                         |
| xml_etree_iterparse  | 61.3 ms                                                         | 67.7 ms: 1.11x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 24.4 ms: 1.16x faster                                                          |
| python_startup_no_site | 20.2 ms                                                         | 20.5 ms: 1.02x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 21.7 ms                                                         | 22.5 ms: 1.04x slower                                                          |
| django_template | 32.0 ms                                                         | 33.3 ms: 1.04x slower                                                          |
| mako            | 7.02 ms                                                         | 8.09 ms: 1.15x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.05x slower                                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 742 us: 13.83x faster                                                          |
| coverage                   | 326 ms                                                          | 51.3 ms: 6.36x faster                                                          |
| create_gc_cycles           | 1.08 ms                                                         | 739 us: 1.46x faster                                                           |
| deepcopy                   | 311 us                                                          | 243 us: 1.28x faster                                                           |
| bench_mp_pool              | 93.6 ms                                                         | 74.4 ms: 1.26x faster                                                          |
| gc_traversal               | 1.76 ms                                                         | 1.43 ms: 1.23x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 21.9 us: 1.20x faster                                                          |
| python_startup             | 28.3 ms                                                         | 24.4 ms: 1.16x faster                                                          |
| deepcopy_reduce            | 2.94 us                                                         | 2.53 us: 1.16x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 252 ms: 1.14x faster                                                           |
| async_tree_none            | 245 ms                                                          | 223 ms: 1.10x faster                                                           |
| tornado_http               | 105 ms                                                          | 95.6 ms: 1.09x faster                                                          |
| async_tree_memoization     | 302 ms                                                          | 277 ms: 1.09x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 200 ms: 1.08x faster                                                           |
| pathlib                    | 89.1 ms                                                         | 83.2 ms: 1.07x faster                                                          |
| pidigits                   | 204 ms                                                          | 197 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 475 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 460 ms: 1.02x faster                                                           |
| go                         | 111 ms                                                          | 109 ms: 1.02x faster                                                           |
| json_dumps                 | 7.53 ms                                                         | 7.45 ms: 1.01x faster                                                          |
| json_loads                 | 21.7 us                                                         | 21.5 us: 1.01x faster                                                          |
| nqueens                    | 75.1 ms                                                         | 75.6 ms: 1.01x slower                                                          |
| sympy_integrate            | 15.2 ms                                                         | 15.4 ms: 1.01x slower                                                          |
| pycparser                  | 869 ms                                                          | 880 ms: 1.01x slower                                                           |
| logging_simple             | 7.89 us                                                         | 8.02 us: 1.02x slower                                                          |
| python_startup_no_site     | 20.2 ms                                                         | 20.5 ms: 1.02x slower                                                          |
| dulwich_log                | 50.2 ms                                                         | 51.1 ms: 1.02x slower                                                          |
| logging_format             | 8.59 us                                                         | 8.74 us: 1.02x slower                                                          |
| typing_runtime_protocols   | 141 us                                                          | 144 us: 1.02x slower                                                           |
| sympy_str                  | 214 ms                                                          | 219 ms: 1.02x slower                                                           |
| sympy_expand               | 377 ms                                                          | 386 ms: 1.02x slower                                                           |
| async_tree_io              | 530 ms                                                          | 544 ms: 1.03x slower                                                           |
| meteor_contest             | 78.1 ms                                                         | 80.1 ms: 1.03x slower                                                          |
| genshi_text                | 21.7 ms                                                         | 22.5 ms: 1.04x slower                                                          |
| regex_v8                   | 15.5 ms                                                         | 16.1 ms: 1.04x slower                                                          |
| django_template            | 32.0 ms                                                         | 33.3 ms: 1.04x slower                                                          |
| docutils                   | 1.80 sec                                                        | 1.87 sec: 1.04x slower                                                         |
| telco                      | 6.27 ms                                                         | 6.53 ms: 1.04x slower                                                          |
| pylint                     | 225 ms                                                          | 234 ms: 1.04x slower                                                           |
| sqlglot_normalize          | 223 ms                                                          | 232 ms: 1.04x slower                                                           |
| async_tree_io_tg           | 499 ms                                                          | 521 ms: 1.04x slower                                                           |
| pprint_safe_repr           | 658 ms                                                          | 687 ms: 1.04x slower                                                           |
| crypto_pyaes               | 56.6 ms                                                         | 59.8 ms: 1.06x slower                                                          |
| sqlglot_optimize           | 42.4 ms                                                         | 44.9 ms: 1.06x slower                                                          |
| xml_etree_parse            | 102 ms                                                          | 109 ms: 1.06x slower                                                           |
| comprehensions             | 13.1 us                                                         | 14.0 us: 1.06x slower                                                          |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.06 ms: 1.06x slower                                                          |
| sqlglot_parse              | 1.02 ms                                                         | 1.09 ms: 1.07x slower                                                          |
| sqlglot_transpile          | 1.26 ms                                                         | 1.35 ms: 1.07x slower                                                          |
| pprint_pformat             | 1.32 sec                                                        | 1.41 sec: 1.07x slower                                                         |
| mdp                        | 1.70 sec                                                        | 1.82 sec: 1.07x slower                                                         |
| spectral_norm              | 70.0 ms                                                         | 75.8 ms: 1.08x slower                                                          |
| float                      | 56.4 ms                                                         | 61.2 ms: 1.09x slower                                                          |
| xml_etree_generate         | 61.9 ms                                                         | 67.3 ms: 1.09x slower                                                          |
| pickle_pure_python         | 239 us                                                          | 261 us: 1.09x slower                                                           |
| unpickle_pure_python       | 162 us                                                          | 177 us: 1.09x slower                                                           |
| regex_compile              | 101 ms                                                          | 110 ms: 1.09x slower                                                           |
| regex_effbot               | 1.82 ms                                                         | 1.99 ms: 1.09x slower                                                          |
| xml_etree_process          | 44.6 ms                                                         | 49.2 ms: 1.10x slower                                                          |
| tomli_loads                | 1.74 sec                                                        | 1.92 sec: 1.10x slower                                                         |
| xml_etree_iterparse        | 61.3 ms                                                         | 67.7 ms: 1.11x slower                                                          |
| pyflate                    | 322 ms                                                          | 357 ms: 1.11x slower                                                           |
| chaos                      | 49.4 ms                                                         | 55.1 ms: 1.12x slower                                                          |
| nbody                      | 81.4 ms                                                         | 91.0 ms: 1.12x slower                                                          |
| coroutines                 | 16.1 ms                                                         | 18.1 ms: 1.12x slower                                                          |
| async_generators           | 267 ms                                                          | 300 ms: 1.13x slower                                                           |
| regex_dna                  | 112 ms                                                          | 128 ms: 1.14x slower                                                           |
| scimark_lu                 | 60.7 ms                                                         | 69.2 ms: 1.14x slower                                                          |
| scimark_sor                | 85.8 ms                                                         | 98.2 ms: 1.14x slower                                                          |
| hexiom                     | 4.60 ms                                                         | 5.26 ms: 1.14x slower                                                          |
| fannkuch                   | 288 ms                                                          | 330 ms: 1.15x slower                                                           |
| mako                       | 7.02 ms                                                         | 8.09 ms: 1.15x slower                                                          |
| scimark_fft                | 204 ms                                                          | 236 ms: 1.16x slower                                                           |
| deltablue                  | 2.35 ms                                                         | 2.73 ms: 1.16x slower                                                          |
| scimark_monte_carlo        | 48.7 ms                                                         | 56.7 ms: 1.16x slower                                                          |
| raytrace                   | 203 ms                                                          | 243 ms: 1.20x slower                                                           |
| richards                   | 33.4 ms                                                         | 40.6 ms: 1.22x slower                                                          |
| logging_silent             | 62.4 ns                                                         | 76.1 ns: 1.22x slower                                                          |
| generators                 | 21.5 ms                                                         | 26.2 ms: 1.22x slower                                                          |
| richards_super             | 37.0 ms                                                         | 45.9 ms: 1.24x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (6): bench_thread_pool, json, genshi_xml, sympy_sum, html5lib, 2to3
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.021x faster
# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown
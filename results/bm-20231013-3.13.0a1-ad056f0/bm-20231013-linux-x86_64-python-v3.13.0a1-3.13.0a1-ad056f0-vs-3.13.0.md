# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a1
- machine: linux-x86_64
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.029x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.86x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 269 ms: 1.01x slower                                       |
| chameleon      | 6.94 ms                                                | 7.07 ms: 1.02x slower                                      |
| docutils       | 2.59 sec                                               | 2.64 sec: 1.02x slower                                     |
| tornado_http   | 92.4 ms                                                | 96.0 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                 | 22.7 ms                                                | 23.4 ms: 1.03x slower                                      |
| async_generators           | 436 ms                                                 | 453 ms: 1.04x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 712 ms: 1.23x slower                                       |
| async_tree_none            | 351 ms                                                 | 437 ms: 1.25x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 564 ms: 1.27x slower                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 595 ms: 1.28x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 741 ms: 1.36x slower                                       |
| async_tree_io              | 842 ms                                                 | 1.19 sec: 1.41x slower                                     |
| async_tree_none_tg         | 321 ms                                                 | 453 ms: 1.41x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 1.23 sec: 1.43x slower                                     |
| Geometric mean             | (ref)                                                  | 1.24x slower                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 88.6 ms: 1.02x slower                                      |
| float          | 79.2 ms                                                | 81.6 ms: 1.03x slower                                      |
| pidigits       | 186 ms                                                 | 195 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.7 ms: 1.06x faster                                      |
| regex_dna      | 218 ms                                                 | 212 ms: 1.03x faster                                       |
| regex_effbot   | 3.73 ms                                                | 3.67 ms: 1.02x faster                                      |
| regex_compile  | 132 ms                                                 | 138 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 310 us                                                 | 300 us: 1.04x faster                                       |
| xml_etree_process    | 60.6 ms                                                | 59.9 ms: 1.01x faster                                      |
| json_dumps           | 10.6 ms                                                | 10.5 ms: 1.01x faster                                      |
| xml_etree_parse      | 156 ms                                                 | 157 ms: 1.01x slower                                       |
| json_loads           | 27.2 us                                                | 27.8 us: 1.02x slower                                      |
| unpickle_pure_python | 216 us                                                 | 222 us: 1.03x slower                                       |
| xml_etree_iterparse  | 101 ms                                                 | 106 ms: 1.04x slower                                       |
| Geometric mean       | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (2): xml_etree_generate, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.1 ms: 1.24x faster                                      |
| python_startup_no_site | 6.96 ms                                                | 6.87 ms: 1.01x faster                                      |
| Geometric mean         | (ref)                                                  | 1.12x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 11.1 ms                                                | 11.2 ms: 1.01x slower                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.48 ms: 1.63x faster                                      |
| python_startup             | 12.5 ms                                                | 10.1 ms: 1.24x faster                                      |
| gc_traversal               | 4.37 ms                                                | 3.87 ms: 1.13x faster                                      |
| regex_v8                   | 26.2 ms                                                | 24.7 ms: 1.06x faster                                      |
| typing_runtime_protocols   | 165 us                                                 | 156 us: 1.06x faster                                       |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.79 ms: 1.05x faster                                      |
| crypto_pyaes               | 75.3 ms                                                | 71.8 ms: 1.05x faster                                      |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.05x faster                                       |
| telco                      | 8.54 ms                                                | 8.17 ms: 1.05x faster                                      |
| json                       | 5.36 ms                                                | 5.16 ms: 1.04x faster                                      |
| pickle_pure_python         | 310 us                                                 | 300 us: 1.04x faster                                       |
| regex_dna                  | 218 ms                                                 | 212 ms: 1.03x faster                                       |
| sympy_expand               | 463 ms                                                 | 452 ms: 1.03x faster                                       |
| deepcopy_reduce            | 3.20 us                                                | 3.14 us: 1.02x faster                                      |
| go                         | 144 ms                                                 | 141 ms: 1.02x faster                                       |
| regex_effbot               | 3.73 ms                                                | 3.67 ms: 1.02x faster                                      |
| deepcopy                   | 358 us                                                 | 353 us: 1.02x faster                                       |
| python_startup_no_site     | 6.96 ms                                                | 6.87 ms: 1.01x faster                                      |
| xml_etree_process          | 60.6 ms                                                | 59.9 ms: 1.01x faster                                      |
| deepcopy_memo              | 39.1 us                                                | 38.7 us: 1.01x faster                                      |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                       |
| json_dumps                 | 10.6 ms                                                | 10.5 ms: 1.01x faster                                      |
| bench_thread_pool          | 822 us                                                 | 815 us: 1.01x faster                                       |
| sqlglot_optimize           | 53.7 ms                                                | 53.9 ms: 1.00x slower                                      |
| pyflate                    | 471 ms                                                 | 473 ms: 1.01x slower                                       |
| meteor_contest             | 109 ms                                                 | 109 ms: 1.01x slower                                       |
| 2to3                       | 267 ms                                                 | 269 ms: 1.01x slower                                       |
| mdp                        | 2.72 sec                                               | 2.74 sec: 1.01x slower                                     |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.01x slower                                      |
| logging_format             | 6.40 us                                                | 6.47 us: 1.01x slower                                      |
| xml_etree_parse            | 156 ms                                                 | 157 ms: 1.01x slower                                       |
| sqlglot_transpile          | 1.58 ms                                                | 1.60 ms: 1.01x slower                                      |
| scimark_fft                | 364 ms                                                 | 369 ms: 1.01x slower                                       |
| mako                       | 11.1 ms                                                | 11.2 ms: 1.01x slower                                      |
| sympy_integrate            | 19.9 ms                                                | 20.2 ms: 1.02x slower                                      |
| docutils                   | 2.59 sec                                               | 2.64 sec: 1.02x slower                                     |
| nbody                      | 87.0 ms                                                | 88.6 ms: 1.02x slower                                      |
| chameleon                  | 6.94 ms                                                | 7.07 ms: 1.02x slower                                      |
| scimark_lu                 | 113 ms                                                 | 115 ms: 1.02x slower                                       |
| sympy_str                  | 275 ms                                                 | 281 ms: 1.02x slower                                       |
| json_loads                 | 27.2 us                                                | 27.8 us: 1.02x slower                                      |
| pprint_pformat             | 1.49 sec                                               | 1.53 sec: 1.02x slower                                     |
| raytrace                   | 267 ms                                                 | 274 ms: 1.03x slower                                       |
| unpickle_pure_python       | 216 us                                                 | 222 us: 1.03x slower                                       |
| float                      | 79.2 ms                                                | 81.6 ms: 1.03x slower                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 69.5 ms: 1.03x slower                                      |
| coroutines                 | 22.7 ms                                                | 23.4 ms: 1.03x slower                                      |
| logging_simple             | 5.72 us                                                | 5.90 us: 1.03x slower                                      |
| pprint_safe_repr           | 728 ms                                                 | 752 ms: 1.03x slower                                       |
| generators                 | 29.0 ms                                                | 29.9 ms: 1.03x slower                                      |
| deltablue                  | 3.23 ms                                                | 3.34 ms: 1.04x slower                                      |
| sympy_sum                  | 150 ms                                                 | 156 ms: 1.04x slower                                       |
| tornado_http               | 92.4 ms                                                | 96.0 ms: 1.04x slower                                      |
| async_generators           | 436 ms                                                 | 453 ms: 1.04x slower                                       |
| xml_etree_iterparse        | 101 ms                                                 | 106 ms: 1.04x slower                                       |
| dulwich_log                | 64.3 ms                                                | 67.1 ms: 1.04x slower                                      |
| nqueens                    | 78.4 ms                                                | 81.9 ms: 1.05x slower                                      |
| pidigits                   | 186 ms                                                 | 195 ms: 1.05x slower                                       |
| regex_compile              | 132 ms                                                 | 138 ms: 1.05x slower                                       |
| logging_silent             | 102 ns                                                 | 107 ns: 1.05x slower                                       |
| chaos                      | 58.1 ms                                                | 61.7 ms: 1.06x slower                                      |
| pathlib                    | 17.5 ms                                                | 19.4 ms: 1.10x slower                                      |
| coverage                   | 84.0 ms                                                | 94.4 ms: 1.12x slower                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 712 ms: 1.23x slower                                       |
| async_tree_none            | 351 ms                                                 | 437 ms: 1.25x slower                                       |
| comprehensions             | 16.5 us                                                | 20.8 us: 1.26x slower                                      |
| async_tree_memoization     | 442 ms                                                 | 564 ms: 1.27x slower                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 595 ms: 1.28x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 741 ms: 1.36x slower                                       |
| async_tree_io              | 842 ms                                                 | 1.19 sec: 1.41x slower                                     |
| async_tree_none_tg         | 321 ms                                                 | 453 ms: 1.41x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 1.23 sec: 1.43x slower                                     |
| Geometric mean             | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (10): fannkuch, scimark_sor, richards, hexiom, asyncio_websockets, bench_mp_pool, pycparser, richards_super, xml_etree_generate, tomli_loads
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, django_template, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, mypy2, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (9) of results/bm-20231013-3.13.0a1-ad056f0/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.029x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.86x
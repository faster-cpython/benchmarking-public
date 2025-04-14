# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a1
- machine: linux-x86_64
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.090x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.52x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 276 ms: 1.03x slower                                       |
| chameleon      | 6.94 ms                                                | 7.13 ms: 1.03x slower                                      |
| docutils       | 2.59 sec                                               | 2.71 sec: 1.04x slower                                     |
| html5lib       | 64.2 ms                                                | 67.3 ms: 1.05x slower                                      |
| tornado_http   | 92.4 ms                                                | 99.1 ms: 1.07x slower                                      |
| Geometric mean | (ref)                                                  | 1.05x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| asyncio_websockets         | 552 ms                                                 | 563 ms: 1.02x slower                                       |
| coroutines                 | 22.7 ms                                                | 23.7 ms: 1.04x slower                                      |
| async_generators           | 436 ms                                                 | 472 ms: 1.08x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 726 ms: 1.26x slower                                       |
| async_tree_none            | 351 ms                                                 | 446 ms: 1.27x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 572 ms: 1.29x slower                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 610 ms: 1.32x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 759 ms: 1.39x slower                                       |
| async_tree_io              | 842 ms                                                 | 1.21 sec: 1.44x slower                                     |
| async_tree_none_tg         | 321 ms                                                 | 463 ms: 1.45x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 1.25 sec: 1.46x slower                                     |
| Geometric mean             | (ref)                                                  | 1.26x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 190 ms: 1.02x slower                                       |
| float          | 79.2 ms                                                | 83.4 ms: 1.05x slower                                      |
| nbody          | 87.0 ms                                                | 95.7 ms: 1.10x slower                                      |
| Geometric mean | (ref)                                                  | 1.06x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.56 ms: 1.05x faster                                      |
| regex_dna      | 218 ms                                                 | 209 ms: 1.05x faster                                       |
| regex_v8       | 26.2 ms                                                | 25.3 ms: 1.04x faster                                      |
| regex_compile  | 132 ms                                                 | 142 ms: 1.07x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 310 us                                                 | 307 us: 1.01x faster                                       |
| json_dumps           | 10.6 ms                                                | 10.5 ms: 1.01x faster                                      |
| xml_etree_generate   | 86.7 ms                                                | 87.7 ms: 1.01x slower                                      |
| json_loads           | 27.2 us                                                | 27.9 us: 1.02x slower                                      |
| xml_etree_parse      | 156 ms                                                 | 160 ms: 1.03x slower                                       |
| unpickle_pure_python | 216 us                                                 | 226 us: 1.05x slower                                       |
| tomli_loads          | 2.14 sec                                               | 2.25 sec: 1.05x slower                                     |
| xml_etree_iterparse  | 101 ms                                                 | 107 ms: 1.06x slower                                       |
| Geometric mean       | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.4 ms: 1.20x faster                                      |
| python_startup_no_site | 6.96 ms                                                | 7.05 ms: 1.01x slower                                      |
| Geometric mean         | (ref)                                                  | 1.09x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 23.1 ms: 1.02x faster                                      |
| django_template | 35.2 ms                                                | 34.7 ms: 1.01x faster                                      |
| genshi_xml      | 50.9 ms                                                | 52.0 ms: 1.02x slower                                      |
| mako            | 11.1 ms                                                | 11.7 ms: 1.06x slower                                      |
| Geometric mean  | (ref)                                                  | 1.01x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.50 ms: 1.60x faster                                      |
| mypy2                      | 1.04 sec                                               | 863 ms: 1.21x faster                                       |
| python_startup             | 12.5 ms                                                | 10.4 ms: 1.20x faster                                      |
| typing_runtime_protocols   | 165 us                                                 | 153 us: 1.07x faster                                       |
| mdp                        | 2.72 sec                                               | 2.58 sec: 1.06x faster                                     |
| gc_traversal               | 4.37 ms                                                | 4.15 ms: 1.05x faster                                      |
| regex_effbot               | 3.73 ms                                                | 3.56 ms: 1.05x faster                                      |
| regex_dna                  | 218 ms                                                 | 209 ms: 1.05x faster                                       |
| regex_v8                   | 26.2 ms                                                | 25.3 ms: 1.04x faster                                      |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.93 ms: 1.02x faster                                      |
| genshi_text                | 23.5 ms                                                | 23.1 ms: 1.02x faster                                      |
| json                       | 5.36 ms                                                | 5.27 ms: 1.02x faster                                      |
| telco                      | 8.54 ms                                                | 8.41 ms: 1.02x faster                                      |
| django_template            | 35.2 ms                                                | 34.7 ms: 1.01x faster                                      |
| pickle_pure_python         | 310 us                                                 | 307 us: 1.01x faster                                       |
| json_dumps                 | 10.6 ms                                                | 10.5 ms: 1.01x faster                                      |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.01x faster                                      |
| crypto_pyaes               | 75.3 ms                                                | 75.1 ms: 1.00x faster                                      |
| sqlglot_normalize          | 108 ms                                                 | 108 ms: 1.00x slower                                       |
| deepcopy                   | 358 us                                                 | 361 us: 1.01x slower                                       |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                       |
| xml_etree_generate         | 86.7 ms                                                | 87.7 ms: 1.01x slower                                      |
| deepcopy_memo              | 39.1 us                                                | 39.6 us: 1.01x slower                                      |
| python_startup_no_site     | 6.96 ms                                                | 7.05 ms: 1.01x slower                                      |
| bench_thread_pool          | 822 us                                                 | 833 us: 1.01x slower                                       |
| sqlglot_optimize           | 53.7 ms                                                | 54.5 ms: 1.01x slower                                      |
| meteor_contest             | 109 ms                                                 | 111 ms: 1.02x slower                                       |
| go                         | 144 ms                                                 | 146 ms: 1.02x slower                                       |
| generators                 | 29.0 ms                                                | 29.5 ms: 1.02x slower                                      |
| pidigits                   | 186 ms                                                 | 190 ms: 1.02x slower                                       |
| richards_super             | 54.9 ms                                                | 56.0 ms: 1.02x slower                                      |
| asyncio_websockets         | 552 ms                                                 | 563 ms: 1.02x slower                                       |
| genshi_xml                 | 50.9 ms                                                | 52.0 ms: 1.02x slower                                      |
| pyflate                    | 471 ms                                                 | 482 ms: 1.02x slower                                       |
| json_loads                 | 27.2 us                                                | 27.9 us: 1.02x slower                                      |
| richards                   | 48.7 ms                                                | 49.9 ms: 1.03x slower                                      |
| xml_etree_parse            | 156 ms                                                 | 160 ms: 1.03x slower                                       |
| chameleon                  | 6.94 ms                                                | 7.13 ms: 1.03x slower                                      |
| scimark_sor                | 124 ms                                                 | 127 ms: 1.03x slower                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.31 ms: 1.03x slower                                      |
| scimark_fft                | 364 ms                                                 | 375 ms: 1.03x slower                                       |
| sqlglot_transpile          | 1.58 ms                                                | 1.63 ms: 1.03x slower                                      |
| pprint_pformat             | 1.49 sec                                               | 1.54 sec: 1.03x slower                                     |
| nqueens                    | 78.4 ms                                                | 81.0 ms: 1.03x slower                                      |
| pprint_safe_repr           | 728 ms                                                 | 752 ms: 1.03x slower                                       |
| 2to3                       | 267 ms                                                 | 276 ms: 1.03x slower                                       |
| pycparser                  | 1.20 sec                                               | 1.24 sec: 1.04x slower                                     |
| hexiom                     | 6.16 ms                                                | 6.40 ms: 1.04x slower                                      |
| fannkuch                   | 404 ms                                                 | 420 ms: 1.04x slower                                       |
| scimark_lu                 | 113 ms                                                 | 117 ms: 1.04x slower                                       |
| sympy_str                  | 275 ms                                                 | 286 ms: 1.04x slower                                       |
| scimark_monte_carlo        | 67.4 ms                                                | 70.2 ms: 1.04x slower                                      |
| docutils                   | 2.59 sec                                               | 2.71 sec: 1.04x slower                                     |
| sympy_integrate            | 19.9 ms                                                | 20.8 ms: 1.04x slower                                      |
| coroutines                 | 22.7 ms                                                | 23.7 ms: 1.04x slower                                      |
| unpickle_pure_python       | 216 us                                                 | 226 us: 1.05x slower                                       |
| tomli_loads                | 2.14 sec                                               | 2.25 sec: 1.05x slower                                     |
| html5lib                   | 64.2 ms                                                | 67.3 ms: 1.05x slower                                      |
| logging_format             | 6.40 us                                                | 6.71 us: 1.05x slower                                      |
| logging_simple             | 5.72 us                                                | 6.02 us: 1.05x slower                                      |
| deltablue                  | 3.23 ms                                                | 3.40 ms: 1.05x slower                                      |
| float                      | 79.2 ms                                                | 83.4 ms: 1.05x slower                                      |
| xml_etree_iterparse        | 101 ms                                                 | 107 ms: 1.06x slower                                       |
| mako                       | 11.1 ms                                                | 11.7 ms: 1.06x slower                                      |
| sympy_sum                  | 150 ms                                                 | 160 ms: 1.06x slower                                       |
| dulwich_log                | 64.3 ms                                                | 68.5 ms: 1.06x slower                                      |
| logging_silent             | 102 ns                                                 | 109 ns: 1.07x slower                                       |
| raytrace                   | 267 ms                                                 | 285 ms: 1.07x slower                                       |
| tornado_http               | 92.4 ms                                                | 99.1 ms: 1.07x slower                                      |
| regex_compile              | 132 ms                                                 | 142 ms: 1.07x slower                                       |
| async_generators           | 436 ms                                                 | 472 ms: 1.08x slower                                       |
| nbody                      | 87.0 ms                                                | 95.7 ms: 1.10x slower                                      |
| chaos                      | 58.1 ms                                                | 64.0 ms: 1.10x slower                                      |
| pathlib                    | 17.5 ms                                                | 19.6 ms: 1.12x slower                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 726 ms: 1.26x slower                                       |
| async_tree_none            | 351 ms                                                 | 446 ms: 1.27x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 572 ms: 1.29x slower                                       |
| comprehensions             | 16.5 us                                                | 21.5 us: 1.31x slower                                      |
| async_tree_memoization_tg  | 464 ms                                                 | 610 ms: 1.32x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 759 ms: 1.39x slower                                       |
| async_tree_io              | 842 ms                                                 | 1.21 sec: 1.44x slower                                     |
| async_tree_none_tg         | 321 ms                                                 | 463 ms: 1.45x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 1.25 sec: 1.46x slower                                     |
| coverage                   | 84.0 ms                                                | 700 ms: 8.33x slower                                       |
| thrift                     | 809 us                                                 | 9.24 ms: 11.42x slower                                     |
| Geometric mean             | (ref)                                                  | 1.10x slower                                               |

Benchmark hidden because not significant (4): xml_etree_process, sympy_expand, deepcopy_reduce, pylint
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20231013-3.13.0a1-ad056f0-NOGIL/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.090x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 0.52x
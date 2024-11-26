# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a1
- machine: linux-x86_64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.006x faster
- HPT reliability: 62.80%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 277 ms: 1.04x slower                                       |
| docutils       | 2.59 sec                                               | 2.91 sec: 1.12x slower                                     |
| html5lib       | 64.2 ms                                                | 63.7 ms: 1.01x faster                                      |
| sphinx         | 1.03 sec                                               | 1.18 sec: 1.14x slower                                     |
| tornado_http   | 92.4 ms                                                | 94.3 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                  | 1.06x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 376 ms: 1.23x faster                                       |
| async_tree_memoization     | 442 ms                                                 | 416 ms: 1.06x faster                                       |
| async_tree_none            | 351 ms                                                 | 331 ms: 1.06x faster                                       |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 559 ms: 1.02x slower                                       |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                      |
| async_generators           | 436 ms                                                 | 478 ms: 1.10x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 966 ms: 1.13x slower                                       |
| Geometric mean             | (ref)                                                  | 1.00x faster                                               |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 81.3 ms: 1.07x faster                                      |
| float          | 79.2 ms                                                | 75.4 ms: 1.05x faster                                      |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.67 ms: 1.02x faster                                      |
| regex_dna      | 218 ms                                                 | 217 ms: 1.00x faster                                       |
| regex_v8       | 26.2 ms                                                | 26.4 ms: 1.01x slower                                      |
| regex_compile  | 132 ms                                                 | 140 ms: 1.06x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 1.92 sec: 1.12x faster                                     |
| xml_etree_generate   | 86.7 ms                                                | 78.6 ms: 1.10x faster                                      |
| xml_etree_process    | 60.6 ms                                                | 55.5 ms: 1.09x faster                                      |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                       |
| xml_etree_iterparse  | 101 ms                                                 | 99.9 ms: 1.01x faster                                      |
| json_loads           | 27.2 us                                                | 26.9 us: 1.01x faster                                      |
| unpickle_pure_python | 216 us                                                 | 216 us: 1.00x slower                                       |
| json_dumps           | 10.6 ms                                                | 10.8 ms: 1.02x slower                                      |
| Geometric mean       | (ref)                                                  | 1.04x faster                                               |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 11.9 ms: 1.05x faster                                      |
| python_startup_no_site | 6.96 ms                                                | 7.10 ms: 1.02x slower                                      |
| Geometric mean         | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.1 ms: 1.10x faster                                      |
| django_template | 35.2 ms                                                | 37.2 ms: 1.06x slower                                      |
| genshi_text     | 23.5 ms                                                | 25.2 ms: 1.07x slower                                      |
| genshi_xml      | 50.9 ms                                                | 58.9 ms: 1.16x slower                                      |
| Geometric mean  | (ref)                                                  | 1.04x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 29.4 us: 1.33x faster                                      |
| deepcopy                   | 358 us                                                 | 273 us: 1.31x faster                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 376 ms: 1.23x faster                                       |
| richards                   | 48.7 ms                                                | 41.0 ms: 1.19x faster                                      |
| deepcopy_reduce            | 3.20 us                                                | 2.75 us: 1.16x faster                                      |
| scimark_fft                | 364 ms                                                 | 319 ms: 1.14x faster                                       |
| richards_super             | 54.9 ms                                                | 48.0 ms: 1.14x faster                                      |
| tomli_loads                | 2.14 sec                                               | 1.92 sec: 1.12x faster                                     |
| crypto_pyaes               | 75.3 ms                                                | 67.5 ms: 1.12x faster                                      |
| telco                      | 8.54 ms                                                | 7.68 ms: 1.11x faster                                      |
| xml_etree_generate         | 86.7 ms                                                | 78.6 ms: 1.10x faster                                      |
| mako                       | 11.1 ms                                                | 10.1 ms: 1.10x faster                                      |
| xml_etree_process          | 60.6 ms                                                | 55.5 ms: 1.09x faster                                      |
| pathlib                    | 17.5 ms                                                | 16.2 ms: 1.08x faster                                      |
| json                       | 5.36 ms                                                | 4.95 ms: 1.08x faster                                      |
| go                         | 144 ms                                                 | 133 ms: 1.08x faster                                       |
| fannkuch                   | 404 ms                                                 | 377 ms: 1.07x faster                                       |
| nbody                      | 87.0 ms                                                | 81.3 ms: 1.07x faster                                      |
| bpe_tokeniser              | 4.75 sec                                               | 4.44 sec: 1.07x faster                                     |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.72 ms: 1.07x faster                                      |
| mdp                        | 2.72 sec                                               | 2.56 sec: 1.06x faster                                     |
| async_tree_memoization     | 442 ms                                                 | 416 ms: 1.06x faster                                       |
| async_tree_none            | 351 ms                                                 | 331 ms: 1.06x faster                                       |
| pyflate                    | 471 ms                                                 | 446 ms: 1.06x faster                                       |
| scimark_monte_carlo        | 67.4 ms                                                | 64.1 ms: 1.05x faster                                      |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                       |
| float                      | 79.2 ms                                                | 75.4 ms: 1.05x faster                                      |
| python_startup             | 12.5 ms                                                | 11.9 ms: 1.05x faster                                      |
| scimark_sor                | 124 ms                                                 | 118 ms: 1.04x faster                                       |
| logging_format             | 6.40 us                                                | 6.13 us: 1.04x faster                                      |
| logging_silent             | 102 ns                                                 | 98.0 ns: 1.04x faster                                      |
| thrift                     | 809 us                                                 | 787 us: 1.03x faster                                       |
| pprint_pformat             | 1.49 sec                                               | 1.46 sec: 1.02x faster                                     |
| regex_effbot               | 3.73 ms                                                | 3.67 ms: 1.02x faster                                      |
| logging_simple             | 5.72 us                                                | 5.63 us: 1.02x faster                                      |
| typing_runtime_protocols   | 165 us                                                 | 162 us: 1.01x faster                                       |
| xml_etree_iterparse        | 101 ms                                                 | 99.9 ms: 1.01x faster                                      |
| json_loads                 | 27.2 us                                                | 26.9 us: 1.01x faster                                      |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                       |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                       |
| html5lib                   | 64.2 ms                                                | 63.7 ms: 1.01x faster                                      |
| regex_dna                  | 218 ms                                                 | 217 ms: 1.00x faster                                       |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                       |
| unpickle_pure_python       | 216 us                                                 | 216 us: 1.00x slower                                       |
| gc_traversal               | 4.37 ms                                                | 4.40 ms: 1.01x slower                                      |
| regex_v8                   | 26.2 ms                                                | 26.4 ms: 1.01x slower                                      |
| coverage                   | 84.0 ms                                                | 84.6 ms: 1.01x slower                                      |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                       |
| scimark_lu                 | 113 ms                                                 | 114 ms: 1.01x slower                                       |
| chaos                      | 58.1 ms                                                | 59.1 ms: 1.02x slower                                      |
| tornado_http               | 92.4 ms                                                | 94.3 ms: 1.02x slower                                      |
| python_startup_no_site     | 6.96 ms                                                | 7.10 ms: 1.02x slower                                      |
| deltablue                  | 3.23 ms                                                | 3.29 ms: 1.02x slower                                      |
| json_dumps                 | 10.6 ms                                                | 10.8 ms: 1.02x slower                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 559 ms: 1.02x slower                                       |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                      |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                      |
| raytrace                   | 267 ms                                                 | 276 ms: 1.03x slower                                       |
| dulwich_log                | 64.3 ms                                                | 66.5 ms: 1.03x slower                                      |
| 2to3                       | 267 ms                                                 | 277 ms: 1.04x slower                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.05x slower                                      |
| django_template            | 35.2 ms                                                | 37.2 ms: 1.06x slower                                      |
| regex_compile              | 132 ms                                                 | 140 ms: 1.06x slower                                       |
| sqlglot_transpile          | 1.58 ms                                                | 1.69 ms: 1.06x slower                                      |
| bench_thread_pool          | 822 us                                                 | 877 us: 1.07x slower                                       |
| sqlglot_normalize          | 108 ms                                                 | 115 ms: 1.07x slower                                       |
| genshi_text                | 23.5 ms                                                | 25.2 ms: 1.07x slower                                      |
| sympy_expand               | 463 ms                                                 | 502 ms: 1.08x slower                                       |
| async_generators           | 436 ms                                                 | 478 ms: 1.10x slower                                       |
| sympy_str                  | 275 ms                                                 | 303 ms: 1.10x slower                                       |
| nqueens                    | 78.4 ms                                                | 86.7 ms: 1.11x slower                                      |
| create_gc_cycles           | 2.41 ms                                                | 2.67 ms: 1.11x slower                                      |
| sqlglot_optimize           | 53.7 ms                                                | 60.2 ms: 1.12x slower                                      |
| docutils                   | 2.59 sec                                               | 2.91 sec: 1.12x slower                                     |
| async_tree_io_tg           | 857 ms                                                 | 966 ms: 1.13x slower                                       |
| sphinx                     | 1.03 sec                                               | 1.18 sec: 1.14x slower                                     |
| hexiom                     | 6.16 ms                                                | 7.03 ms: 1.14x slower                                      |
| genshi_xml                 | 50.9 ms                                                | 58.9 ms: 1.16x slower                                      |
| sympy_sum                  | 150 ms                                                 | 176 ms: 1.17x slower                                       |
| sympy_integrate            | 19.9 ms                                                | 23.6 ms: 1.19x slower                                      |
| pylint                     | 313 ms                                                 | 376 ms: 1.20x slower                                       |
| generators                 | 29.0 ms                                                | 35.4 ms: 1.22x slower                                      |
| bench_mp_pool              | 24.0 ms                                                | 84.2 ms: 3.51x slower                                      |
| Geometric mean             | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (6): async_tree_none_tg, pprint_safe_repr, pickle_pure_python, async_tree_cpu_io_mixed, pycparser, async_tree_io
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.006x faster
# HPT report

- Reliability score: 62.80% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x
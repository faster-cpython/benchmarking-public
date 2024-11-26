# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc3
- machine: linux-x86_64
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.018x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 264 ms: 1.01x faster                                         |
| chameleon      | 6.94 ms                                                | 6.85 ms: 1.01x faster                                        |
| docutils       | 2.59 sec                                               | 2.56 sec: 1.01x faster                                       |
| html5lib       | 64.2 ms                                                | 63.1 ms: 1.02x faster                                        |
| tornado_http   | 92.4 ms                                                | 91.2 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 857 ms                                                 | 813 ms: 1.05x faster                                         |
| coroutines                 | 22.7 ms                                                | 22.1 ms: 1.03x faster                                        |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 569 ms: 1.01x faster                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 539 ms: 1.01x faster                                         |
| async_tree_memoization_tg  | 464 ms                                                 | 459 ms: 1.01x faster                                         |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (6): async_tree_memoization, async_tree_io, async_tree_none_tg, async_tree_none, async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                         |
| nbody          | 87.0 ms                                                | 88.4 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 23.7 ms: 1.11x faster                                        |
| regex_effbot   | 3.73 ms                                                | 3.51 ms: 1.06x faster                                        |
| regex_dna      | 218 ms                                                 | 208 ms: 1.05x faster                                         |
| regex_compile  | 132 ms                                                 | 131 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 310 us                                                 | 302 us: 1.03x faster                                         |
| unpickle_pure_python | 216 us                                                 | 211 us: 1.02x faster                                         |
| xml_etree_process    | 60.6 ms                                                | 59.8 ms: 1.01x faster                                        |
| tomli_loads          | 2.14 sec                                               | 2.12 sec: 1.01x faster                                       |
| xml_etree_generate   | 86.7 ms                                                | 86.1 ms: 1.01x faster                                        |
| xml_etree_iterparse  | 101 ms                                                 | 103 ms: 1.02x slower                                         |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (3): xml_etree_parse, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                        |
| python_startup_no_site | 6.96 ms                                                | 6.95 ms: 1.00x faster                                        |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 35.2 ms                                                | 33.7 ms: 1.04x faster                                        |
| genshi_text     | 23.5 ms                                                | 23.0 ms: 1.02x faster                                        |
| genshi_xml      | 50.9 ms                                                | 50.2 ms: 1.01x faster                                        |
| mako            | 11.1 ms                                                | 11.0 ms: 1.01x faster                                        |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.63 ms: 1.48x faster                                        |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.19x faster                                        |
| gc_traversal               | 4.37 ms                                                | 3.78 ms: 1.16x faster                                        |
| regex_v8                   | 26.2 ms                                                | 23.7 ms: 1.11x faster                                        |
| regex_effbot               | 3.73 ms                                                | 3.51 ms: 1.06x faster                                        |
| async_tree_io_tg           | 857 ms                                                 | 813 ms: 1.05x faster                                         |
| regex_dna                  | 218 ms                                                 | 208 ms: 1.05x faster                                         |
| django_template            | 35.2 ms                                                | 33.7 ms: 1.04x faster                                        |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                       |
| json                       | 5.36 ms                                                | 5.21 ms: 1.03x faster                                        |
| pickle_pure_python         | 310 us                                                 | 302 us: 1.03x faster                                         |
| coroutines                 | 22.7 ms                                                | 22.1 ms: 1.03x faster                                        |
| fannkuch                   | 404 ms                                                 | 394 ms: 1.03x faster                                         |
| genshi_text                | 23.5 ms                                                | 23.0 ms: 1.02x faster                                        |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                         |
| thrift                     | 809 us                                                 | 792 us: 1.02x faster                                         |
| unpickle_pure_python       | 216 us                                                 | 211 us: 1.02x faster                                         |
| pathlib                    | 17.5 ms                                                | 17.2 ms: 1.02x faster                                        |
| richards                   | 48.7 ms                                                | 47.8 ms: 1.02x faster                                        |
| richards_super             | 54.9 ms                                                | 53.8 ms: 1.02x faster                                        |
| go                         | 144 ms                                                 | 141 ms: 1.02x faster                                         |
| dulwich_log                | 64.3 ms                                                | 63.2 ms: 1.02x faster                                        |
| crypto_pyaes               | 75.3 ms                                                | 74.0 ms: 1.02x faster                                        |
| html5lib                   | 64.2 ms                                                | 63.1 ms: 1.02x faster                                        |
| logging_format             | 6.40 us                                                | 6.29 us: 1.02x faster                                        |
| comprehensions             | 16.5 us                                                | 16.2 us: 1.02x faster                                        |
| raytrace                   | 267 ms                                                 | 263 ms: 1.02x faster                                         |
| genshi_xml                 | 50.9 ms                                                | 50.2 ms: 1.01x faster                                        |
| xml_etree_process          | 60.6 ms                                                | 59.8 ms: 1.01x faster                                        |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 569 ms: 1.01x faster                                         |
| tornado_http               | 92.4 ms                                                | 91.2 ms: 1.01x faster                                        |
| deepcopy_memo              | 39.1 us                                                | 38.6 us: 1.01x faster                                        |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 539 ms: 1.01x faster                                         |
| docutils                   | 2.59 sec                                               | 2.56 sec: 1.01x faster                                       |
| chameleon                  | 6.94 ms                                                | 6.85 ms: 1.01x faster                                        |
| tomli_loads                | 2.14 sec                                               | 2.12 sec: 1.01x faster                                       |
| hexiom                     | 6.16 ms                                                | 6.10 ms: 1.01x faster                                        |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                         |
| bench_thread_pool          | 822 us                                                 | 813 us: 1.01x faster                                         |
| async_tree_memoization_tg  | 464 ms                                                 | 459 ms: 1.01x faster                                         |
| deltablue                  | 3.23 ms                                                | 3.19 ms: 1.01x faster                                        |
| sqlglot_transpile          | 1.58 ms                                                | 1.57 ms: 1.01x faster                                        |
| 2to3                       | 267 ms                                                 | 264 ms: 1.01x faster                                         |
| sympy_str                  | 275 ms                                                 | 273 ms: 1.01x faster                                         |
| xml_etree_generate         | 86.7 ms                                                | 86.1 ms: 1.01x faster                                        |
| sympy_expand               | 463 ms                                                 | 460 ms: 1.01x faster                                         |
| sqlglot_parse              | 1.27 ms                                                | 1.26 ms: 1.01x faster                                        |
| regex_compile              | 132 ms                                                 | 131 ms: 1.01x faster                                         |
| pyflate                    | 471 ms                                                 | 468 ms: 1.01x faster                                         |
| mako                       | 11.1 ms                                                | 11.0 ms: 1.01x faster                                        |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                         |
| sympy_integrate            | 19.9 ms                                                | 19.8 ms: 1.01x faster                                        |
| bpe_tokeniser              | 4.75 sec                                               | 4.72 sec: 1.00x faster                                       |
| logging_silent             | 102 ns                                                 | 101 ns: 1.00x faster                                         |
| python_startup_no_site     | 6.96 ms                                                | 6.95 ms: 1.00x faster                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                         |
| sqlglot_optimize           | 53.7 ms                                                | 53.9 ms: 1.00x slower                                        |
| mdp                        | 2.72 sec                                               | 2.73 sec: 1.00x slower                                       |
| scimark_monte_carlo        | 67.4 ms                                                | 67.8 ms: 1.01x slower                                        |
| deepcopy                   | 358 us                                                 | 360 us: 1.01x slower                                         |
| pprint_pformat             | 1.49 sec                                               | 1.51 sec: 1.01x slower                                       |
| scimark_fft                | 364 ms                                                 | 368 ms: 1.01x slower                                         |
| scimark_sor                | 124 ms                                                 | 125 ms: 1.01x slower                                         |
| scimark_lu                 | 113 ms                                                 | 114 ms: 1.01x slower                                         |
| nbody                      | 87.0 ms                                                | 88.4 ms: 1.02x slower                                        |
| xml_etree_iterparse        | 101 ms                                                 | 103 ms: 1.02x slower                                         |
| deepcopy_reduce            | 3.20 us                                                | 3.26 us: 1.02x slower                                        |
| pprint_safe_repr           | 728 ms                                                 | 741 ms: 1.02x slower                                         |
| chaos                      | 58.1 ms                                                | 59.2 ms: 1.02x slower                                        |
| nqueens                    | 78.4 ms                                                | 81.2 ms: 1.04x slower                                        |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                 |

Benchmark hidden because not significant (20): async_tree_memoization, async_tree_io, async_tree_none_tg, pylint, xml_etree_parse, async_tree_none, telco, json_dumps, float, logging_simple, scimark_sparse_mat_mult, async_generators, sympy_sum, generators, typing_runtime_protocols, bench_mp_pool, coverage, json_loads, asyncio_websockets, mypy2
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20241001-3.13.0rc3-fae84c7/bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.018x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x
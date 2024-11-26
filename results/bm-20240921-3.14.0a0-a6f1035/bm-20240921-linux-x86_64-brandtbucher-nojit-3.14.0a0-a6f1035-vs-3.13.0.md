# Results vs. 3.13.0

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.032x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 255 ms: 1.05x faster                                         |
| docutils       | 2.59 sec                                               | 2.65 sec: 1.02x slower                                       |
| html5lib       | 64.2 ms                                                | 63.8 ms: 1.01x faster                                        |
| tornado_http   | 92.4 ms                                                | 89.8 ms: 1.03x faster                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 387 ms: 1.20x faster                                         |
| async_tree_memoization     | 442 ms                                                 | 389 ms: 1.14x faster                                         |
| async_tree_none            | 351 ms                                                 | 312 ms: 1.12x faster                                         |
| async_tree_none_tg         | 321 ms                                                 | 307 ms: 1.05x faster                                         |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 561 ms: 1.03x faster                                         |
| async_generators           | 436 ms                                                 | 434 ms: 1.00x faster                                         |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 552 ms: 1.01x slower                                         |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                        |
| async_tree_io              | 842 ms                                                 | 879 ms: 1.04x slower                                         |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                 |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 79.2 ms                                                | 76.3 ms: 1.04x faster                                        |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.0 ms: 1.05x faster                                        |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                         |
| regex_effbot   | 3.73 ms                                                | 3.70 ms: 1.01x faster                                        |
| regex_dna      | 218 ms                                                 | 221 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 310 us                                                 | 301 us: 1.03x faster                                         |
| xml_etree_process    | 60.6 ms                                                | 59.0 ms: 1.03x faster                                        |
| xml_etree_generate   | 86.7 ms                                                | 84.7 ms: 1.02x faster                                        |
| tomli_loads          | 2.14 sec                                               | 2.11 sec: 1.02x faster                                       |
| unpickle_pure_python | 216 us                                                 | 215 us: 1.00x faster                                         |
| json_loads           | 27.2 us                                                | 27.5 us: 1.01x slower                                        |
| xml_etree_iterparse  | 101 ms                                                 | 105 ms: 1.04x slower                                         |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (2): json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.18x faster                                        |
| python_startup_no_site | 6.96 ms                                                | 7.00 ms: 1.01x slower                                        |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 22.4 ms: 1.05x faster                                        |
| django_template | 35.2 ms                                                | 34.1 ms: 1.03x faster                                        |
| genshi_xml      | 50.9 ms                                                | 50.0 ms: 1.02x faster                                        |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                        |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 258 us: 1.39x faster                                         |
| create_gc_cycles           | 2.41 ms                                                | 1.74 ms: 1.39x faster                                        |
| deepcopy_memo              | 39.1 us                                                | 29.7 us: 1.31x faster                                        |
| async_tree_memoization_tg  | 464 ms                                                 | 387 ms: 1.20x faster                                         |
| go                         | 144 ms                                                 | 120 ms: 1.20x faster                                         |
| deepcopy_reduce            | 3.20 us                                                | 2.69 us: 1.19x faster                                        |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.18x faster                                        |
| async_tree_memoization     | 442 ms                                                 | 389 ms: 1.14x faster                                         |
| gc_traversal               | 4.37 ms                                                | 3.88 ms: 1.13x faster                                        |
| async_tree_none            | 351 ms                                                 | 312 ms: 1.12x faster                                         |
| pathlib                    | 17.5 ms                                                | 16.1 ms: 1.09x faster                                        |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                       |
| json                       | 5.36 ms                                                | 5.09 ms: 1.05x faster                                        |
| genshi_text                | 23.5 ms                                                | 22.4 ms: 1.05x faster                                        |
| richards                   | 48.7 ms                                                | 46.4 ms: 1.05x faster                                        |
| 2to3                       | 267 ms                                                 | 255 ms: 1.05x faster                                         |
| regex_v8                   | 26.2 ms                                                | 25.0 ms: 1.05x faster                                        |
| async_tree_none_tg         | 321 ms                                                 | 307 ms: 1.05x faster                                         |
| generators                 | 29.0 ms                                                | 27.7 ms: 1.05x faster                                        |
| richards_super             | 54.9 ms                                                | 52.7 ms: 1.04x faster                                        |
| float                      | 79.2 ms                                                | 76.3 ms: 1.04x faster                                        |
| thrift                     | 809 us                                                 | 780 us: 1.04x faster                                         |
| logging_format             | 6.40 us                                                | 6.17 us: 1.04x faster                                        |
| typing_runtime_protocols   | 165 us                                                 | 160 us: 1.03x faster                                         |
| pickle_pure_python         | 310 us                                                 | 301 us: 1.03x faster                                         |
| django_template            | 35.2 ms                                                | 34.1 ms: 1.03x faster                                        |
| crypto_pyaes               | 75.3 ms                                                | 73.2 ms: 1.03x faster                                        |
| tornado_http               | 92.4 ms                                                | 89.8 ms: 1.03x faster                                        |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 561 ms: 1.03x faster                                         |
| xml_etree_process          | 60.6 ms                                                | 59.0 ms: 1.03x faster                                        |
| pprint_pformat             | 1.49 sec                                               | 1.46 sec: 1.03x faster                                       |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.02x faster                                         |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                         |
| xml_etree_generate         | 86.7 ms                                                | 84.7 ms: 1.02x faster                                        |
| pprint_safe_repr           | 728 ms                                                 | 711 ms: 1.02x faster                                         |
| sympy_str                  | 275 ms                                                 | 269 ms: 1.02x faster                                         |
| pyflate                    | 471 ms                                                 | 460 ms: 1.02x faster                                         |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                         |
| genshi_xml                 | 50.9 ms                                                | 50.0 ms: 1.02x faster                                        |
| telco                      | 8.54 ms                                                | 8.40 ms: 1.02x faster                                        |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.96 ms: 1.02x faster                                        |
| sympy_expand               | 463 ms                                                 | 456 ms: 1.02x faster                                         |
| tomli_loads                | 2.14 sec                                               | 2.11 sec: 1.02x faster                                       |
| bench_thread_pool          | 822 us                                                 | 809 us: 1.02x faster                                         |
| logging_simple             | 5.72 us                                                | 5.65 us: 1.01x faster                                        |
| scimark_lu                 | 113 ms                                                 | 112 ms: 1.01x faster                                         |
| raytrace                   | 267 ms                                                 | 264 ms: 1.01x faster                                         |
| sympy_integrate            | 19.9 ms                                                | 19.7 ms: 1.01x faster                                        |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                         |
| regex_effbot               | 3.73 ms                                                | 3.70 ms: 1.01x faster                                        |
| html5lib                   | 64.2 ms                                                | 63.8 ms: 1.01x faster                                        |
| sqlglot_optimize           | 53.7 ms                                                | 53.5 ms: 1.01x faster                                        |
| async_generators           | 436 ms                                                 | 434 ms: 1.00x faster                                         |
| sqlglot_transpile          | 1.58 ms                                                | 1.58 ms: 1.00x faster                                        |
| unpickle_pure_python       | 216 us                                                 | 215 us: 1.00x faster                                         |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                         |
| mdp                        | 2.72 sec                                               | 2.73 sec: 1.00x slower                                       |
| dulwich_log                | 64.3 ms                                                | 64.7 ms: 1.01x slower                                        |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                         |
| python_startup_no_site     | 6.96 ms                                                | 7.00 ms: 1.01x slower                                        |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                        |
| json_loads                 | 27.2 us                                                | 27.5 us: 1.01x slower                                        |
| regex_dna                  | 218 ms                                                 | 221 ms: 1.01x slower                                         |
| scimark_fft                | 364 ms                                                 | 368 ms: 1.01x slower                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 552 ms: 1.01x slower                                         |
| scimark_sor                | 124 ms                                                 | 125 ms: 1.01x slower                                         |
| chaos                      | 58.1 ms                                                | 58.8 ms: 1.01x slower                                        |
| fannkuch                   | 404 ms                                                 | 410 ms: 1.01x slower                                         |
| bpe_tokeniser              | 4.75 sec                                               | 4.81 sec: 1.01x slower                                       |
| coverage                   | 84.0 ms                                                | 85.2 ms: 1.01x slower                                        |
| hexiom                     | 6.16 ms                                                | 6.26 ms: 1.02x slower                                        |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.02x slower                                         |
| docutils                   | 2.59 sec                                               | 2.65 sec: 1.02x slower                                       |
| mako                       | 11.1 ms                                                | 11.3 ms: 1.02x slower                                        |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                        |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                        |
| nqueens                    | 78.4 ms                                                | 81.4 ms: 1.04x slower                                        |
| xml_etree_iterparse        | 101 ms                                                 | 105 ms: 1.04x slower                                         |
| async_tree_io              | 842 ms                                                 | 879 ms: 1.04x slower                                         |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                 |

Benchmark hidden because not significant (9): json_dumps, scimark_monte_carlo, logging_silent, deltablue, bench_mp_pool, xml_etree_parse, nbody, async_tree_io_tg, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.032x faster
# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x
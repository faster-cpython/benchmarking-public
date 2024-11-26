# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc1
- machine: linux-x86_64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.012x faster
- HPT reliability: 64.36%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 266 ms: 1.00x faster                                         |
| chameleon      | 6.94 ms                                                | 6.88 ms: 1.01x faster                                        |
| docutils       | 2.59 sec                                               | 2.77 sec: 1.07x slower                                       |
| html5lib       | 64.2 ms                                                | 66.6 ms: 1.04x slower                                        |
| tornado_http   | 92.4 ms                                                | 91.0 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 440 ms: 1.05x faster                                         |
| coroutines                 | 22.7 ms                                                | 22.0 ms: 1.03x faster                                        |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                         |
| async_generators           | 436 ms                                                 | 439 ms: 1.01x slower                                         |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 594 ms: 1.03x slower                                         |
| async_tree_io_tg           | 857 ms                                                 | 895 ms: 1.04x slower                                         |
| async_tree_none            | 351 ms                                                 | 367 ms: 1.05x slower                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 572 ms: 1.05x slower                                         |
| async_tree_io              | 842 ms                                                 | 893 ms: 1.06x slower                                         |
| async_tree_none_tg         | 321 ms                                                 | 341 ms: 1.06x slower                                         |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                 |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 79.2 ms                                                | 76.7 ms: 1.03x faster                                        |
| nbody          | 87.0 ms                                                | 85.6 ms: 1.02x faster                                        |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 132 ms                                                 | 132 ms: 1.00x faster                                         |
| regex_v8       | 26.2 ms                                                | 26.3 ms: 1.00x slower                                        |
| regex_effbot   | 3.73 ms                                                | 3.85 ms: 1.03x slower                                        |
| regex_dna      | 218 ms                                                 | 237 ms: 1.08x slower                                         |
| Geometric mean | (ref)                                                  | 1.03x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|---------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python  | 310 us                                                 | 302 us: 1.03x faster                                         |
| json_dumps          | 10.6 ms                                                | 10.3 ms: 1.02x faster                                        |
| tomli_loads         | 2.14 sec                                               | 2.12 sec: 1.01x faster                                       |
| json_loads          | 27.2 us                                                | 27.0 us: 1.01x faster                                        |
| xml_etree_generate  | 86.7 ms                                                | 88.0 ms: 1.01x slower                                        |
| xml_etree_iterparse | 101 ms                                                 | 104 ms: 1.03x slower                                         |
| Geometric mean      | (ref)                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (3): unpickle_pure_python, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.4 ms: 1.20x faster                                        |
| python_startup_no_site | 6.96 ms                                                | 6.99 ms: 1.00x slower                                        |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 35.2 ms                                                | 33.6 ms: 1.05x faster                                        |
| genshi_text     | 23.5 ms                                                | 22.9 ms: 1.03x faster                                        |
| genshi_xml      | 50.9 ms                                                | 50.4 ms: 1.01x faster                                        |
| mako            | 11.1 ms                                                | 11.1 ms: 1.00x faster                                        |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mypy2                      | 1.04 sec                                               | 714 ms: 1.46x faster                                         |
| create_gc_cycles           | 2.41 ms                                                | 1.76 ms: 1.37x faster                                        |
| python_startup             | 12.5 ms                                                | 10.4 ms: 1.20x faster                                        |
| gc_traversal               | 4.37 ms                                                | 3.73 ms: 1.17x faster                                        |
| json                       | 5.36 ms                                                | 5.04 ms: 1.06x faster                                        |
| async_tree_memoization_tg  | 464 ms                                                 | 440 ms: 1.05x faster                                         |
| django_template            | 35.2 ms                                                | 33.6 ms: 1.05x faster                                        |
| telco                      | 8.54 ms                                                | 8.23 ms: 1.04x faster                                        |
| pathlib                    | 17.5 ms                                                | 16.9 ms: 1.04x faster                                        |
| float                      | 79.2 ms                                                | 76.7 ms: 1.03x faster                                        |
| coroutines                 | 22.7 ms                                                | 22.0 ms: 1.03x faster                                        |
| logging_format             | 6.40 us                                                | 6.22 us: 1.03x faster                                        |
| crypto_pyaes               | 75.3 ms                                                | 73.3 ms: 1.03x faster                                        |
| pickle_pure_python         | 310 us                                                 | 302 us: 1.03x faster                                         |
| genshi_text                | 23.5 ms                                                | 22.9 ms: 1.03x faster                                        |
| richards                   | 48.7 ms                                                | 47.5 ms: 1.03x faster                                        |
| mdp                        | 2.72 sec                                               | 2.66 sec: 1.02x faster                                       |
| hexiom                     | 6.16 ms                                                | 6.02 ms: 1.02x faster                                        |
| logging_silent             | 102 ns                                                 | 99.5 ns: 1.02x faster                                        |
| json_dumps                 | 10.6 ms                                                | 10.3 ms: 1.02x faster                                        |
| thrift                     | 809 us                                                 | 793 us: 1.02x faster                                         |
| raytrace                   | 267 ms                                                 | 262 ms: 1.02x faster                                         |
| dulwich_log                | 64.3 ms                                                | 63.2 ms: 1.02x faster                                        |
| deltablue                  | 3.23 ms                                                | 3.17 ms: 1.02x faster                                        |
| tornado_http               | 92.4 ms                                                | 91.0 ms: 1.02x faster                                        |
| nbody                      | 87.0 ms                                                | 85.6 ms: 1.02x faster                                        |
| richards_super             | 54.9 ms                                                | 54.0 ms: 1.02x faster                                        |
| go                         | 144 ms                                                 | 142 ms: 1.02x faster                                         |
| typing_runtime_protocols   | 165 us                                                 | 162 us: 1.02x faster                                         |
| deepcopy_memo              | 39.1 us                                                | 38.5 us: 1.02x faster                                        |
| pycparser                  | 1.20 sec                                               | 1.19 sec: 1.01x faster                                       |
| generators                 | 29.0 ms                                                | 28.6 ms: 1.01x faster                                        |
| logging_simple             | 5.72 us                                                | 5.65 us: 1.01x faster                                        |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.01x faster                                         |
| bench_thread_pool          | 822 us                                                 | 812 us: 1.01x faster                                         |
| deepcopy_reduce            | 3.20 us                                                | 3.16 us: 1.01x faster                                        |
| tomli_loads                | 2.14 sec                                               | 2.12 sec: 1.01x faster                                       |
| deepcopy                   | 358 us                                                 | 354 us: 1.01x faster                                         |
| comprehensions             | 16.5 us                                                | 16.3 us: 1.01x faster                                        |
| genshi_xml                 | 50.9 ms                                                | 50.4 ms: 1.01x faster                                        |
| chameleon                  | 6.94 ms                                                | 6.88 ms: 1.01x faster                                        |
| json_loads                 | 27.2 us                                                | 27.0 us: 1.01x faster                                        |
| sqlglot_transpile          | 1.58 ms                                                | 1.57 ms: 1.01x faster                                        |
| spectral_norm              | 115 ms                                                 | 115 ms: 1.01x faster                                         |
| sympy_expand               | 463 ms                                                 | 461 ms: 1.00x faster                                         |
| regex_compile              | 132 ms                                                 | 132 ms: 1.00x faster                                         |
| 2to3                       | 267 ms                                                 | 266 ms: 1.00x faster                                         |
| mako                       | 11.1 ms                                                | 11.1 ms: 1.00x faster                                        |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                         |
| regex_v8                   | 26.2 ms                                                | 26.3 ms: 1.00x slower                                        |
| sqlglot_optimize           | 53.7 ms                                                | 54.0 ms: 1.00x slower                                        |
| python_startup_no_site     | 6.96 ms                                                | 6.99 ms: 1.00x slower                                        |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                         |
| pprint_pformat             | 1.49 sec                                               | 1.50 sec: 1.01x slower                                       |
| sympy_integrate            | 19.9 ms                                                | 20.0 ms: 1.01x slower                                        |
| async_generators           | 436 ms                                                 | 439 ms: 1.01x slower                                         |
| scimark_fft                | 364 ms                                                 | 367 ms: 1.01x slower                                         |
| pprint_safe_repr           | 728 ms                                                 | 734 ms: 1.01x slower                                         |
| scimark_monte_carlo        | 67.4 ms                                                | 68.1 ms: 1.01x slower                                        |
| pyflate                    | 471 ms                                                 | 477 ms: 1.01x slower                                         |
| xml_etree_generate         | 86.7 ms                                                | 88.0 ms: 1.01x slower                                        |
| scimark_lu                 | 113 ms                                                 | 115 ms: 1.02x slower                                         |
| fannkuch                   | 404 ms                                                 | 411 ms: 1.02x slower                                         |
| chaos                      | 58.1 ms                                                | 59.1 ms: 1.02x slower                                        |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 594 ms: 1.03x slower                                         |
| xml_etree_iterparse        | 101 ms                                                 | 104 ms: 1.03x slower                                         |
| regex_effbot               | 3.73 ms                                                | 3.85 ms: 1.03x slower                                        |
| bpe_tokeniser              | 4.75 sec                                               | 4.91 sec: 1.04x slower                                       |
| html5lib                   | 64.2 ms                                                | 66.6 ms: 1.04x slower                                        |
| nqueens                    | 78.4 ms                                                | 81.4 ms: 1.04x slower                                        |
| async_tree_io_tg           | 857 ms                                                 | 895 ms: 1.04x slower                                         |
| async_tree_none            | 351 ms                                                 | 367 ms: 1.05x slower                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 572 ms: 1.05x slower                                         |
| async_tree_io              | 842 ms                                                 | 893 ms: 1.06x slower                                         |
| async_tree_none_tg         | 321 ms                                                 | 341 ms: 1.06x slower                                         |
| docutils                   | 2.59 sec                                               | 2.77 sec: 1.07x slower                                       |
| scimark_sor                | 124 ms                                                 | 132 ms: 1.07x slower                                         |
| regex_dna                  | 218 ms                                                 | 237 ms: 1.08x slower                                         |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (12): scimark_sparse_mat_mult, unpickle_pure_python, xml_etree_parse, xml_etree_process, coverage, sqlglot_parse, bench_mp_pool, sqlglot_normalize, sympy_sum, sympy_str, async_tree_memoization, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (3) of results/bm-20240731-3.13.0rc1-e4a3e78/bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json: asyncio_tcp, asyncio_tcp_ssl, dask

- Geometric mean (including insignificant results): 1.012x faster
# HPT report

- Reliability score: 64.36% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x
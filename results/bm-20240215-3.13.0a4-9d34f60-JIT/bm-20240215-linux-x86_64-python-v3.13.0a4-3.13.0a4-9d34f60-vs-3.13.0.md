# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.037x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 276 ms: 1.04x slower                                       |
| chameleon      | 6.94 ms                                                | 6.75 ms: 1.03x faster                                      |
| docutils       | 2.59 sec                                               | 2.64 sec: 1.02x slower                                     |
| tornado_http   | 92.4 ms                                                | 96.9 ms: 1.05x slower                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                 | 22.7 ms                                                | 23.7 ms: 1.04x slower                                      |
| async_generators           | 436 ms                                                 | 463 ms: 1.06x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 716 ms: 1.24x slower                                       |
| async_tree_none            | 351 ms                                                 | 439 ms: 1.25x slower                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 592 ms: 1.28x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 568 ms: 1.28x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 727 ms: 1.33x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 1.20 sec: 1.40x slower                                     |
| async_tree_io              | 842 ms                                                 | 1.18 sec: 1.40x slower                                     |
| async_tree_none_tg         | 321 ms                                                 | 452 ms: 1.41x slower                                       |
| Geometric mean             | (ref)                                                  | 1.24x slower                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                       |
| float          | 79.2 ms                                                | 86.1 ms: 1.09x slower                                      |
| nbody          | 87.0 ms                                                | 102 ms: 1.18x slower                                       |
| Geometric mean | (ref)                                                  | 1.09x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.57 ms: 1.05x faster                                      |
| regex_v8       | 26.2 ms                                                | 25.1 ms: 1.04x faster                                      |
| regex_dna      | 218 ms                                                 | 225 ms: 1.03x slower                                       |
| regex_compile  | 132 ms                                                 | 141 ms: 1.06x slower                                       |
| Geometric mean | (ref)                                                  | 1.00x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 310 us                                                 | 296 us: 1.05x faster                                       |
| xml_etree_process    | 60.6 ms                                                | 57.9 ms: 1.05x faster                                      |
| xml_etree_generate   | 86.7 ms                                                | 85.7 ms: 1.01x faster                                      |
| xml_etree_parse      | 156 ms                                                 | 157 ms: 1.01x slower                                       |
| tomli_loads          | 2.14 sec                                               | 2.19 sec: 1.02x slower                                     |
| unpickle_pure_python | 216 us                                                 | 228 us: 1.06x slower                                       |
| xml_etree_iterparse  | 101 ms                                                 | 108 ms: 1.06x slower                                       |
| Geometric mean       | (ref)                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (2): json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.3 ms: 1.21x faster                                      |
| python_startup_no_site | 6.96 ms                                                | 8.95 ms: 1.29x slower                                      |
| Geometric mean         | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 11.1 ms                                                | 12.4 ms: 1.12x slower                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.49 ms: 1.61x faster                                      |
| typing_runtime_protocols   | 165 us                                                 | 110 us: 1.50x faster                                       |
| python_startup             | 12.5 ms                                                | 10.3 ms: 1.21x faster                                      |
| mypy2                      | 1.04 sec                                               | 861 ms: 1.21x faster                                       |
| gc_traversal               | 4.37 ms                                                | 3.76 ms: 1.16x faster                                      |
| richards                   | 48.7 ms                                                | 44.8 ms: 1.09x faster                                      |
| richards_super             | 54.9 ms                                                | 50.8 ms: 1.08x faster                                      |
| deepcopy_reduce            | 3.20 us                                                | 3.04 us: 1.05x faster                                      |
| pickle_pure_python         | 310 us                                                 | 296 us: 1.05x faster                                       |
| xml_etree_process          | 60.6 ms                                                | 57.9 ms: 1.05x faster                                      |
| regex_effbot               | 3.73 ms                                                | 3.57 ms: 1.05x faster                                      |
| json                       | 5.36 ms                                                | 5.12 ms: 1.05x faster                                      |
| regex_v8                   | 26.2 ms                                                | 25.1 ms: 1.04x faster                                      |
| deepcopy                   | 358 us                                                 | 345 us: 1.04x faster                                       |
| chameleon                  | 6.94 ms                                                | 6.75 ms: 1.03x faster                                      |
| deepcopy_memo              | 39.1 us                                                | 38.1 us: 1.03x faster                                      |
| telco                      | 8.54 ms                                                | 8.40 ms: 1.02x faster                                      |
| scimark_sor                | 124 ms                                                 | 122 ms: 1.02x faster                                       |
| logging_format             | 6.40 us                                                | 6.30 us: 1.02x faster                                      |
| xml_etree_generate         | 86.7 ms                                                | 85.7 ms: 1.01x faster                                      |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                       |
| logging_silent             | 102 ns                                                 | 101 ns: 1.00x faster                                       |
| scimark_fft                | 364 ms                                                 | 366 ms: 1.00x slower                                       |
| generators                 | 29.0 ms                                                | 29.1 ms: 1.00x slower                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                      |
| xml_etree_parse            | 156 ms                                                 | 157 ms: 1.01x slower                                       |
| meteor_contest             | 109 ms                                                 | 110 ms: 1.01x slower                                       |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                       |
| pycparser                  | 1.20 sec                                               | 1.22 sec: 1.01x slower                                     |
| go                         | 144 ms                                                 | 146 ms: 1.02x slower                                       |
| sqlglot_transpile          | 1.58 ms                                                | 1.61 ms: 1.02x slower                                      |
| bench_thread_pool          | 822 us                                                 | 836 us: 1.02x slower                                       |
| docutils                   | 2.59 sec                                               | 2.64 sec: 1.02x slower                                     |
| sympy_str                  | 275 ms                                                 | 281 ms: 1.02x slower                                       |
| sympy_integrate            | 19.9 ms                                                | 20.3 ms: 1.02x slower                                      |
| tomli_loads                | 2.14 sec                                               | 2.19 sec: 1.02x slower                                     |
| mdp                        | 2.72 sec                                               | 2.78 sec: 1.02x slower                                     |
| sqlglot_optimize           | 53.7 ms                                                | 55.1 ms: 1.03x slower                                      |
| deltablue                  | 3.23 ms                                                | 3.32 ms: 1.03x slower                                      |
| regex_dna                  | 218 ms                                                 | 225 ms: 1.03x slower                                       |
| pathlib                    | 17.5 ms                                                | 18.1 ms: 1.03x slower                                      |
| 2to3                       | 267 ms                                                 | 276 ms: 1.04x slower                                       |
| sympy_expand               | 463 ms                                                 | 480 ms: 1.04x slower                                       |
| coroutines                 | 22.7 ms                                                | 23.7 ms: 1.04x slower                                      |
| sympy_sum                  | 150 ms                                                 | 157 ms: 1.04x slower                                       |
| fannkuch                   | 404 ms                                                 | 422 ms: 1.04x slower                                       |
| raytrace                   | 267 ms                                                 | 280 ms: 1.05x slower                                       |
| tornado_http               | 92.4 ms                                                | 96.9 ms: 1.05x slower                                      |
| crypto_pyaes               | 75.3 ms                                                | 79.1 ms: 1.05x slower                                      |
| unpickle_pure_python       | 216 us                                                 | 228 us: 1.06x slower                                       |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.35 ms: 1.06x slower                                      |
| dulwich_log                | 64.3 ms                                                | 68.2 ms: 1.06x slower                                      |
| async_generators           | 436 ms                                                 | 463 ms: 1.06x slower                                       |
| regex_compile              | 132 ms                                                 | 141 ms: 1.06x slower                                       |
| xml_etree_iterparse        | 101 ms                                                 | 108 ms: 1.06x slower                                       |
| pprint_safe_repr           | 728 ms                                                 | 775 ms: 1.07x slower                                       |
| pprint_pformat             | 1.49 sec                                               | 1.61 sec: 1.08x slower                                     |
| float                      | 79.2 ms                                                | 86.1 ms: 1.09x slower                                      |
| pyflate                    | 471 ms                                                 | 514 ms: 1.09x slower                                       |
| scimark_monte_carlo        | 67.4 ms                                                | 74.0 ms: 1.10x slower                                      |
| comprehensions             | 16.5 us                                                | 18.2 us: 1.10x slower                                      |
| mako                       | 11.1 ms                                                | 12.4 ms: 1.12x slower                                      |
| spectral_norm              | 115 ms                                                 | 132 ms: 1.14x slower                                       |
| coverage                   | 84.0 ms                                                | 95.8 ms: 1.14x slower                                      |
| nqueens                    | 78.4 ms                                                | 89.8 ms: 1.15x slower                                      |
| nbody                      | 87.0 ms                                                | 102 ms: 1.18x slower                                       |
| chaos                      | 58.1 ms                                                | 69.1 ms: 1.19x slower                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 716 ms: 1.24x slower                                       |
| async_tree_none            | 351 ms                                                 | 439 ms: 1.25x slower                                       |
| hexiom                     | 6.16 ms                                                | 7.72 ms: 1.25x slower                                      |
| async_tree_memoization_tg  | 464 ms                                                 | 592 ms: 1.28x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 568 ms: 1.28x slower                                       |
| python_startup_no_site     | 6.96 ms                                                | 8.95 ms: 1.29x slower                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 727 ms: 1.33x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 1.20 sec: 1.40x slower                                     |
| async_tree_io              | 842 ms                                                 | 1.18 sec: 1.40x slower                                     |
| async_tree_none_tg         | 321 ms                                                 | 452 ms: 1.41x slower                                       |
| Geometric mean             | (ref)                                                  | 1.04x slower                                               |

Benchmark hidden because not significant (6): scimark_lu, json_dumps, asyncio_websockets, bench_mp_pool, json_loads, logging_simple
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, django_template, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (10) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: asyncio_tcp, asyncio_tcp_ssl, dask, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.037x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 0.90x
# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a5
- machine: linux-x86_64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.016x slower
- HPT reliability: 99.60%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.88x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 270 ms: 1.01x slower                                       |
| chameleon      | 6.94 ms                                                | 6.83 ms: 1.02x faster                                      |
| docutils       | 2.59 sec                                               | 2.66 sec: 1.03x slower                                     |
| html5lib       | 64.2 ms                                                | 67.4 ms: 1.05x slower                                      |
| tornado_http   | 92.4 ms                                                | 98.6 ms: 1.07x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                 | 22.7 ms                                                | 22.0 ms: 1.03x faster                                      |
| asyncio_websockets         | 552 ms                                                 | 563 ms: 1.02x slower                                       |
| async_generators           | 436 ms                                                 | 449 ms: 1.03x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 729 ms: 1.26x slower                                       |
| async_tree_none            | 351 ms                                                 | 449 ms: 1.28x slower                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 595 ms: 1.28x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 581 ms: 1.31x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 745 ms: 1.36x slower                                       |
| async_tree_none_tg         | 321 ms                                                 | 463 ms: 1.44x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 1.24 sec: 1.44x slower                                     |
| async_tree_io              | 842 ms                                                 | 1.22 sec: 1.45x slower                                     |
| Geometric mean             | (ref)                                                  | 1.25x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 189 ms: 1.02x slower                                       |
| float          | 79.2 ms                                                | 82.6 ms: 1.04x slower                                      |
| nbody          | 87.0 ms                                                | 93.6 ms: 1.08x slower                                      |
| Geometric mean | (ref)                                                  | 1.04x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.7 ms: 1.06x faster                                      |
| regex_effbot   | 3.73 ms                                                | 3.54 ms: 1.06x faster                                      |
| regex_dna      | 218 ms                                                 | 216 ms: 1.01x faster                                       |
| regex_compile  | 132 ms                                                 | 133 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 310 us                                                 | 302 us: 1.03x faster                                       |
| xml_etree_process    | 60.6 ms                                                | 59.8 ms: 1.01x faster                                      |
| unpickle_pure_python | 216 us                                                 | 217 us: 1.00x slower                                       |
| xml_etree_generate   | 86.7 ms                                                | 87.3 ms: 1.01x slower                                      |
| tomli_loads          | 2.14 sec                                               | 2.16 sec: 1.01x slower                                     |
| json_loads           | 27.2 us                                                | 27.7 us: 1.02x slower                                      |
| json_dumps           | 10.6 ms                                                | 10.8 ms: 1.02x slower                                      |
| xml_etree_parse      | 156 ms                                                 | 159 ms: 1.02x slower                                       |
| xml_etree_iterparse  | 101 ms                                                 | 106 ms: 1.05x slower                                       |
| Geometric mean       | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.4 ms: 1.20x faster                                      |
| python_startup_no_site | 6.96 ms                                                | 8.99 ms: 1.29x slower                                      |
| Geometric mean         | (ref)                                                  | 1.04x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 35.2 ms                                                | 33.8 ms: 1.04x faster                                      |
| genshi_text     | 23.5 ms                                                | 23.0 ms: 1.02x faster                                      |
| genshi_xml      | 50.9 ms                                                | 52.0 ms: 1.02x slower                                      |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                      |
| Geometric mean  | (ref)                                                  | 1.01x faster                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.52 ms: 1.59x faster                                      |
| typing_runtime_protocols   | 165 us                                                 | 112 us: 1.47x faster                                       |
| python_startup             | 12.5 ms                                                | 10.4 ms: 1.20x faster                                      |
| mypy2                      | 1.04 sec                                               | 871 ms: 1.20x faster                                       |
| gc_traversal               | 4.37 ms                                                | 3.78 ms: 1.16x faster                                      |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.68 ms: 1.08x faster                                      |
| mdp                        | 2.72 sec                                               | 2.53 sec: 1.07x faster                                     |
| spectral_norm              | 115 ms                                                 | 108 ms: 1.07x faster                                       |
| regex_v8                   | 26.2 ms                                                | 24.7 ms: 1.06x faster                                      |
| richards                   | 48.7 ms                                                | 45.9 ms: 1.06x faster                                      |
| richards_super             | 54.9 ms                                                | 51.9 ms: 1.06x faster                                      |
| regex_effbot               | 3.73 ms                                                | 3.54 ms: 1.06x faster                                      |
| deepcopy_reduce            | 3.20 us                                                | 3.04 us: 1.05x faster                                      |
| json                       | 5.36 ms                                                | 5.15 ms: 1.04x faster                                      |
| django_template            | 35.2 ms                                                | 33.8 ms: 1.04x faster                                      |
| go                         | 144 ms                                                 | 139 ms: 1.04x faster                                       |
| deepcopy                   | 358 us                                                 | 346 us: 1.04x faster                                       |
| crypto_pyaes               | 75.3 ms                                                | 73.0 ms: 1.03x faster                                      |
| coroutines                 | 22.7 ms                                                | 22.0 ms: 1.03x faster                                      |
| pickle_pure_python         | 310 us                                                 | 302 us: 1.03x faster                                       |
| deepcopy_memo              | 39.1 us                                                | 38.1 us: 1.03x faster                                      |
| genshi_text                | 23.5 ms                                                | 23.0 ms: 1.02x faster                                      |
| thrift                     | 809 us                                                 | 790 us: 1.02x faster                                       |
| logging_silent             | 102 ns                                                 | 99.5 ns: 1.02x faster                                      |
| chameleon                  | 6.94 ms                                                | 6.83 ms: 1.02x faster                                      |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                     |
| raytrace                   | 267 ms                                                 | 263 ms: 1.01x faster                                       |
| xml_etree_process          | 60.6 ms                                                | 59.8 ms: 1.01x faster                                      |
| regex_dna                  | 218 ms                                                 | 216 ms: 1.01x faster                                       |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                       |
| scimark_fft                | 364 ms                                                 | 362 ms: 1.01x faster                                       |
| scimark_sor                | 124 ms                                                 | 123 ms: 1.01x faster                                       |
| hexiom                     | 6.16 ms                                                | 6.13 ms: 1.00x faster                                      |
| comprehensions             | 16.5 us                                                | 16.4 us: 1.00x faster                                      |
| pyflate                    | 471 ms                                                 | 469 ms: 1.00x faster                                       |
| sqlglot_optimize           | 53.7 ms                                                | 53.9 ms: 1.00x slower                                      |
| unpickle_pure_python       | 216 us                                                 | 217 us: 1.00x slower                                       |
| regex_compile              | 132 ms                                                 | 133 ms: 1.01x slower                                       |
| sympy_integrate            | 19.9 ms                                                | 20.0 ms: 1.01x slower                                      |
| sqlglot_transpile          | 1.58 ms                                                | 1.59 ms: 1.01x slower                                      |
| xml_etree_generate         | 86.7 ms                                                | 87.3 ms: 1.01x slower                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 67.9 ms: 1.01x slower                                      |
| telco                      | 8.54 ms                                                | 8.60 ms: 1.01x slower                                      |
| tomli_loads                | 2.14 sec                                               | 2.16 sec: 1.01x slower                                     |
| 2to3                       | 267 ms                                                 | 270 ms: 1.01x slower                                       |
| pidigits                   | 186 ms                                                 | 189 ms: 1.02x slower                                       |
| sympy_sum                  | 150 ms                                                 | 153 ms: 1.02x slower                                       |
| json_loads                 | 27.2 us                                                | 27.7 us: 1.02x slower                                      |
| generators                 | 29.0 ms                                                | 29.5 ms: 1.02x slower                                      |
| logging_format             | 6.40 us                                                | 6.53 us: 1.02x slower                                      |
| json_dumps                 | 10.6 ms                                                | 10.8 ms: 1.02x slower                                      |
| asyncio_websockets         | 552 ms                                                 | 563 ms: 1.02x slower                                       |
| genshi_xml                 | 50.9 ms                                                | 52.0 ms: 1.02x slower                                      |
| mako                       | 11.1 ms                                                | 11.3 ms: 1.02x slower                                      |
| logging_simple             | 5.72 us                                                | 5.85 us: 1.02x slower                                      |
| bench_thread_pool          | 822 us                                                 | 842 us: 1.02x slower                                       |
| xml_etree_parse            | 156 ms                                                 | 159 ms: 1.02x slower                                       |
| docutils                   | 2.59 sec                                               | 2.66 sec: 1.03x slower                                     |
| nqueens                    | 78.4 ms                                                | 80.7 ms: 1.03x slower                                      |
| async_generators           | 436 ms                                                 | 449 ms: 1.03x slower                                       |
| pprint_safe_repr           | 728 ms                                                 | 757 ms: 1.04x slower                                       |
| pprint_pformat             | 1.49 sec                                               | 1.55 sec: 1.04x slower                                     |
| float                      | 79.2 ms                                                | 82.6 ms: 1.04x slower                                      |
| dulwich_log                | 64.3 ms                                                | 67.3 ms: 1.05x slower                                      |
| xml_etree_iterparse        | 101 ms                                                 | 106 ms: 1.05x slower                                       |
| chaos                      | 58.1 ms                                                | 60.9 ms: 1.05x slower                                      |
| html5lib                   | 64.2 ms                                                | 67.4 ms: 1.05x slower                                      |
| pathlib                    | 17.5 ms                                                | 18.5 ms: 1.06x slower                                      |
| tornado_http               | 92.4 ms                                                | 98.6 ms: 1.07x slower                                      |
| nbody                      | 87.0 ms                                                | 93.6 ms: 1.08x slower                                      |
| coverage                   | 84.0 ms                                                | 95.6 ms: 1.14x slower                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 729 ms: 1.26x slower                                       |
| async_tree_none            | 351 ms                                                 | 449 ms: 1.28x slower                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 595 ms: 1.28x slower                                       |
| python_startup_no_site     | 6.96 ms                                                | 8.99 ms: 1.29x slower                                      |
| async_tree_memoization     | 442 ms                                                 | 581 ms: 1.31x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 745 ms: 1.36x slower                                       |
| async_tree_none_tg         | 321 ms                                                 | 463 ms: 1.44x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 1.24 sec: 1.44x slower                                     |
| async_tree_io              | 842 ms                                                 | 1.22 sec: 1.45x slower                                     |
| Geometric mean             | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (9): fannkuch, bench_mp_pool, pylint, sqlglot_parse, sympy_str, deltablue, meteor_contest, scimark_lu, sympy_expand
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240312-3.13.0a5-076d169/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.016x slower
# HPT report

- Reliability score: 99.60% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.88x
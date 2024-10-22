# Results vs. 3.13.0

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: linux-x86_64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.02x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 260 ms: 1.02x faster                                                  |
| docutils       | 2.58 sec                                               | 2.70 sec: 1.04x slower                                                |
| tornado_http   | 91.5 ms                                                | 90.2 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 388 ms: 1.20x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 397 ms: 1.11x faster                                                  |
| async_tree_none            | 354 ms                                                 | 322 ms: 1.10x faster                                                  |
| async_tree_none_tg         | 320 ms                                                 | 297 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 556 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 527 ms: 1.03x faster                                                  |
| asyncio_tcp                | 488 ms                                                 | 487 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.01x slower                                                  |
| async_generators           | 433 ms                                                 | 436 ms: 1.01x slower                                                  |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                 |
| async_tree_io              | 843 ms                                                 | 901 ms: 1.07x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 885 ms: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 85.7 ms                                                | 84.7 ms: 1.01x faster                                                 |
| float          | 78.5 ms                                                | 77.9 ms: 1.01x faster                                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.62 ms: 1.07x faster                                                 |
| regex_v8       | 25.3 ms                                                | 23.9 ms: 1.06x faster                                                 |
| regex_compile  | 131 ms                                                 | 129 ms: 1.02x faster                                                  |
| regex_dna      | 220 ms                                                 | 219 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 2.06 sec: 1.02x faster                                                |
| xml_etree_process    | 60.4 ms                                                | 59.1 ms: 1.02x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 209 us: 1.02x faster                                                  |
| xml_etree_generate   | 87.0 ms                                                | 86.3 ms: 1.01x faster                                                 |
| pickle_pure_python   | 300 us                                                 | 298 us: 1.01x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.4 ms: 1.01x faster                                                 |
| xml_etree_iterparse  | 102 ms                                                 | 104 ms: 1.02x slower                                                  |
| json_loads           | 27.0 us                                                | 28.5 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.06 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 33.8 ms: 1.02x faster                                                 |
| genshi_text     | 22.9 ms                                                | 22.5 ms: 1.02x faster                                                 |
| genshi_xml      | 50.3 ms                                                | 50.0 ms: 1.01x faster                                                 |
| mako            | 11.1 ms                                                | 11.1 ms: 1.00x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 258 us: 1.37x faster                                                  |
| deepcopy_memo              | 38.0 us                                                | 29.1 us: 1.30x faster                                                 |
| async_tree_memoization_tg  | 465 ms                                                 | 388 ms: 1.20x faster                                                  |
| deepcopy_reduce            | 3.17 us                                                | 2.68 us: 1.18x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 397 ms: 1.11x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.52 ms: 1.11x faster                                                 |
| async_tree_none            | 354 ms                                                 | 322 ms: 1.10x faster                                                  |
| async_tree_none_tg         | 320 ms                                                 | 297 ms: 1.08x faster                                                  |
| regex_effbot               | 3.88 ms                                                | 3.62 ms: 1.07x faster                                                 |
| richards                   | 48.1 ms                                                | 45.1 ms: 1.07x faster                                                 |
| gc_traversal               | 3.81 ms                                                | 3.57 ms: 1.07x faster                                                 |
| richards_super             | 54.4 ms                                                | 51.2 ms: 1.06x faster                                                 |
| regex_v8                   | 25.3 ms                                                | 23.9 ms: 1.06x faster                                                 |
| logging_silent             | 102 ns                                                 | 96.5 ns: 1.06x faster                                                 |
| pathlib                    | 17.1 ms                                                | 16.2 ms: 1.05x faster                                                 |
| pycparser                  | 1.19 sec                                               | 1.13 sec: 1.05x faster                                                |
| generators                 | 28.8 ms                                                | 27.7 ms: 1.04x faster                                                 |
| logging_simple             | 5.66 us                                                | 5.46 us: 1.04x faster                                                 |
| telco                      | 8.45 ms                                                | 8.15 ms: 1.04x faster                                                 |
| logging_format             | 6.25 us                                                | 6.03 us: 1.04x faster                                                 |
| scimark_fft                | 369 ms                                                 | 356 ms: 1.04x faster                                                  |
| raytrace                   | 262 ms                                                 | 253 ms: 1.04x faster                                                  |
| bench_thread_pool          | 815 us                                                 | 787 us: 1.04x faster                                                  |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 556 ms: 1.03x faster                                                  |
| scimark_lu                 | 115 ms                                                 | 111 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 527 ms: 1.03x faster                                                  |
| nqueens                    | 80.6 ms                                                | 78.7 ms: 1.02x faster                                                 |
| go                         | 142 ms                                                 | 138 ms: 1.02x faster                                                  |
| tomli_loads                | 2.11 sec                                               | 2.06 sec: 1.02x faster                                                |
| xml_etree_process          | 60.4 ms                                                | 59.1 ms: 1.02x faster                                                 |
| unpickle_pure_python       | 213 us                                                 | 209 us: 1.02x faster                                                  |
| regex_compile              | 131 ms                                                 | 129 ms: 1.02x faster                                                  |
| 2to3                       | 265 ms                                                 | 260 ms: 1.02x faster                                                  |
| django_template            | 34.4 ms                                                | 33.8 ms: 1.02x faster                                                 |
| genshi_text                | 22.9 ms                                                | 22.5 ms: 1.02x faster                                                 |
| thrift                     | 796 us                                                 | 784 us: 1.02x faster                                                  |
| tornado_http               | 91.5 ms                                                | 90.2 ms: 1.02x faster                                                 |
| sqlglot_optimize           | 53.9 ms                                                | 53.1 ms: 1.01x faster                                                 |
| nbody                      | 85.7 ms                                                | 84.7 ms: 1.01x faster                                                 |
| pprint_safe_repr           | 744 ms                                                 | 736 ms: 1.01x faster                                                  |
| mdp                        | 2.74 sec                                               | 2.71 sec: 1.01x faster                                                |
| sympy_str                  | 274 ms                                                 | 271 ms: 1.01x faster                                                  |
| sympy_integrate            | 19.9 ms                                                | 19.7 ms: 1.01x faster                                                 |
| float                      | 78.5 ms                                                | 77.9 ms: 1.01x faster                                                 |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| xml_etree_generate         | 87.0 ms                                                | 86.3 ms: 1.01x faster                                                 |
| genshi_xml                 | 50.3 ms                                                | 50.0 ms: 1.01x faster                                                 |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| pprint_pformat             | 1.51 sec                                               | 1.50 sec: 1.01x faster                                                |
| pickle_pure_python         | 300 us                                                 | 298 us: 1.01x faster                                                  |
| json_dumps                 | 10.4 ms                                                | 10.4 ms: 1.01x faster                                                 |
| sqlglot_transpile          | 1.57 ms                                                | 1.57 ms: 1.01x faster                                                 |
| mako                       | 11.1 ms                                                | 11.1 ms: 1.00x faster                                                 |
| sqlglot_normalize          | 107 ms                                                 | 107 ms: 1.00x faster                                                  |
| asyncio_tcp                | 488 ms                                                 | 487 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                |
| regex_dna                  | 220 ms                                                 | 219 ms: 1.00x faster                                                  |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.01x slower                                                  |
| async_generators           | 433 ms                                                 | 436 ms: 1.01x slower                                                  |
| deltablue                  | 3.15 ms                                                | 3.17 ms: 1.01x slower                                                 |
| hexiom                     | 6.13 ms                                                | 6.17 ms: 1.01x slower                                                 |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.01x slower                                                  |
| python_startup_no_site     | 6.99 ms                                                | 7.06 ms: 1.01x slower                                                 |
| scimark_sor                | 122 ms                                                 | 124 ms: 1.01x slower                                                  |
| pyflate                    | 460 ms                                                 | 466 ms: 1.01x slower                                                  |
| json                       | 5.20 ms                                                | 5.28 ms: 1.02x slower                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.77 sec: 1.02x slower                                                |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                 |
| typing_runtime_protocols   | 159 us                                                 | 162 us: 1.02x slower                                                  |
| comprehensions             | 16.4 us                                                | 16.7 us: 1.02x slower                                                 |
| crypto_pyaes               | 73.0 ms                                                | 74.4 ms: 1.02x slower                                                 |
| xml_etree_iterparse        | 102 ms                                                 | 104 ms: 1.02x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.70 sec: 1.04x slower                                                |
| json_loads                 | 27.0 us                                                | 28.5 us: 1.06x slower                                                 |
| fannkuch                   | 381 ms                                                 | 405 ms: 1.06x slower                                                  |
| async_tree_io              | 843 ms                                                 | 901 ms: 1.07x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 885 ms: 1.07x slower                                                  |
| create_gc_cycles           | 1.61 ms                                                | 1.74 ms: 1.08x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (9): sympy_expand, chaos, spectral_norm, scimark_monte_carlo, html5lib, bench_mp_pool, coverage, xml_etree_parse, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x
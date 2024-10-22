# Results vs. 3.13.0

- fork: brandtbucher
- ref: exit_if
- machine: linux-x86_64
- commit hash: b298d3a
- commit date: 2024-07-25
- overall geometric mean: 1.01x faster
- HPT reliability: 53.58%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 273 ms: 1.03x slower                                           |
| docutils       | 2.58 sec                                               | 2.89 sec: 1.12x slower                                         |
| tornado_http   | 91.5 ms                                                | 93.5 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                  | 1.04x slower                                                   |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 392 ms: 1.18x faster                                           |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                           |
| async_tree_none_tg         | 320 ms                                                 | 301 ms: 1.06x faster                                           |
| async_tree_memoization     | 442 ms                                                 | 418 ms: 1.06x faster                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 533 ms: 1.02x faster                                           |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 564 ms: 1.02x faster                                           |
| asyncio_websockets         | 555 ms                                                 | 559 ms: 1.01x slower                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                         |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                          |
| asyncio_tcp                | 488 ms                                                 | 504 ms: 1.03x slower                                           |
| async_generators           | 433 ms                                                 | 453 ms: 1.05x slower                                           |
| async_tree_io_tg           | 825 ms                                                 | 872 ms: 1.06x slower                                           |
| async_tree_io              | 843 ms                                                 | 896 ms: 1.06x slower                                           |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.8 ms: 1.11x faster                                          |
| nbody          | 85.7 ms                                                | 79.4 ms: 1.08x faster                                          |
| Geometric mean | (ref)                                                  | 1.06x faster                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.77 ms: 1.03x faster                                          |
| regex_v8       | 25.3 ms                                                | 25.8 ms: 1.02x slower                                          |
| regex_compile  | 131 ms                                                 | 135 ms: 1.03x slower                                           |
| regex_dna      | 220 ms                                                 | 227 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.96 sec: 1.08x faster                                         |
| xml_etree_generate   | 87.0 ms                                                | 80.8 ms: 1.08x faster                                          |
| xml_etree_process    | 60.4 ms                                                | 56.8 ms: 1.06x faster                                          |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.06x faster                                           |
| xml_etree_iterparse  | 102 ms                                                 | 98.3 ms: 1.04x faster                                          |
| pickle_pure_python   | 300 us                                                 | 295 us: 1.02x faster                                           |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                           |
| json_loads           | 27.0 us                                                | 28.1 us: 1.04x slower                                          |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                   |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                          |
| python_startup_no_site | 6.99 ms                                                | 7.17 ms: 1.03x slower                                          |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.73 ms: 1.14x faster                                          |
| django_template | 34.4 ms                                                | 35.8 ms: 1.04x slower                                          |
| genshi_text     | 22.9 ms                                                | 24.6 ms: 1.08x slower                                          |
| genshi_xml      | 50.3 ms                                                | 58.4 ms: 1.16x slower                                          |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 28.7 us: 1.32x faster                                          |
| deepcopy                   | 352 us                                                 | 270 us: 1.31x faster                                           |
| scimark_fft                | 369 ms                                                 | 302 ms: 1.22x faster                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.21 ms: 1.19x faster                                          |
| richards                   | 48.1 ms                                                | 40.4 ms: 1.19x faster                                          |
| async_tree_memoization_tg  | 465 ms                                                 | 392 ms: 1.18x faster                                           |
| richards_super             | 54.4 ms                                                | 46.6 ms: 1.17x faster                                          |
| deepcopy_reduce            | 3.17 us                                                | 2.74 us: 1.16x faster                                          |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.15x faster                                           |
| mako                       | 11.1 ms                                                | 9.73 ms: 1.14x faster                                          |
| float                      | 78.5 ms                                                | 70.8 ms: 1.11x faster                                          |
| crypto_pyaes               | 73.0 ms                                                | 66.5 ms: 1.10x faster                                          |
| scimark_monte_carlo        | 66.3 ms                                                | 60.9 ms: 1.09x faster                                          |
| mdp                        | 2.74 sec                                               | 2.53 sec: 1.09x faster                                         |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                           |
| nbody                      | 85.7 ms                                                | 79.4 ms: 1.08x faster                                          |
| tomli_loads                | 2.11 sec                                               | 1.96 sec: 1.08x faster                                         |
| xml_etree_generate         | 87.0 ms                                                | 80.8 ms: 1.08x faster                                          |
| pathlib                    | 17.1 ms                                                | 16.0 ms: 1.07x faster                                          |
| gc_traversal               | 3.81 ms                                                | 3.58 ms: 1.06x faster                                          |
| async_tree_none_tg         | 320 ms                                                 | 301 ms: 1.06x faster                                           |
| telco                      | 8.45 ms                                                | 7.95 ms: 1.06x faster                                          |
| pyflate                    | 460 ms                                                 | 432 ms: 1.06x faster                                           |
| xml_etree_process          | 60.4 ms                                                | 56.8 ms: 1.06x faster                                          |
| async_tree_memoization     | 442 ms                                                 | 418 ms: 1.06x faster                                           |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.06x faster                                           |
| pprint_safe_repr           | 744 ms                                                 | 710 ms: 1.05x faster                                           |
| xml_etree_iterparse        | 102 ms                                                 | 98.3 ms: 1.04x faster                                          |
| bpe_tokeniser              | 4.69 sec                                               | 4.52 sec: 1.04x faster                                         |
| regex_effbot               | 3.88 ms                                                | 3.77 ms: 1.03x faster                                          |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.02x faster                                         |
| fannkuch                   | 381 ms                                                 | 372 ms: 1.02x faster                                           |
| pprint_pformat             | 1.51 sec                                               | 1.48 sec: 1.02x faster                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 533 ms: 1.02x faster                                           |
| pickle_pure_python         | 300 us                                                 | 295 us: 1.02x faster                                           |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 564 ms: 1.02x faster                                           |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                           |
| chaos                      | 58.4 ms                                                | 57.7 ms: 1.01x faster                                          |
| logging_format             | 6.25 us                                                | 6.18 us: 1.01x faster                                          |
| logging_simple             | 5.66 us                                                | 5.60 us: 1.01x faster                                          |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x slower                                          |
| asyncio_websockets         | 555 ms                                                 | 559 ms: 1.01x slower                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                         |
| sqlglot_parse              | 1.27 ms                                                | 1.27 ms: 1.01x slower                                          |
| thrift                     | 796 us                                                 | 804 us: 1.01x slower                                           |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                           |
| bench_thread_pool          | 815 us                                                 | 824 us: 1.01x slower                                           |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                          |
| regex_v8                   | 25.3 ms                                                | 25.8 ms: 1.02x slower                                          |
| tornado_http               | 91.5 ms                                                | 93.5 ms: 1.02x slower                                          |
| sqlglot_transpile          | 1.57 ms                                                | 1.61 ms: 1.02x slower                                          |
| regex_compile              | 131 ms                                                 | 135 ms: 1.03x slower                                           |
| python_startup_no_site     | 6.99 ms                                                | 7.17 ms: 1.03x slower                                          |
| 2to3                       | 265 ms                                                 | 273 ms: 1.03x slower                                           |
| go                         | 142 ms                                                 | 146 ms: 1.03x slower                                           |
| regex_dna                  | 220 ms                                                 | 227 ms: 1.03x slower                                           |
| sqlglot_optimize           | 53.9 ms                                                | 55.7 ms: 1.03x slower                                          |
| asyncio_tcp                | 488 ms                                                 | 504 ms: 1.03x slower                                           |
| logging_silent             | 102 ns                                                 | 106 ns: 1.03x slower                                           |
| raytrace                   | 262 ms                                                 | 271 ms: 1.04x slower                                           |
| django_template            | 34.4 ms                                                | 35.8 ms: 1.04x slower                                          |
| sqlglot_normalize          | 107 ms                                                 | 112 ms: 1.04x slower                                           |
| json_loads                 | 27.0 us                                                | 28.1 us: 1.04x slower                                          |
| async_generators           | 433 ms                                                 | 453 ms: 1.05x slower                                           |
| async_tree_io_tg           | 825 ms                                                 | 872 ms: 1.06x slower                                           |
| scimark_sor                | 122 ms                                                 | 130 ms: 1.06x slower                                           |
| typing_runtime_protocols   | 159 us                                                 | 169 us: 1.06x slower                                           |
| nqueens                    | 80.6 ms                                                | 85.7 ms: 1.06x slower                                          |
| async_tree_io              | 843 ms                                                 | 896 ms: 1.06x slower                                           |
| hexiom                     | 6.13 ms                                                | 6.53 ms: 1.07x slower                                          |
| dask                       | 338 ms                                                 | 362 ms: 1.07x slower                                           |
| genshi_text                | 22.9 ms                                                | 24.6 ms: 1.08x slower                                          |
| sympy_str                  | 274 ms                                                 | 296 ms: 1.08x slower                                           |
| sympy_expand               | 462 ms                                                 | 499 ms: 1.08x slower                                           |
| create_gc_cycles           | 1.61 ms                                                | 1.75 ms: 1.09x slower                                          |
| dulwich_log                | 63.0 ms                                                | 68.5 ms: 1.09x slower                                          |
| coverage                   | 83.7 ms                                                | 91.4 ms: 1.09x slower                                          |
| scimark_lu                 | 115 ms                                                 | 127 ms: 1.11x slower                                           |
| sympy_integrate            | 19.9 ms                                                | 22.2 ms: 1.12x slower                                          |
| pylint                     | 313 ms                                                 | 350 ms: 1.12x slower                                           |
| docutils                   | 2.58 sec                                               | 2.89 sec: 1.12x slower                                         |
| sympy_sum                  | 150 ms                                                 | 168 ms: 1.13x slower                                           |
| deltablue                  | 3.15 ms                                                | 3.61 ms: 1.15x slower                                          |
| genshi_xml                 | 50.3 ms                                                | 58.4 ms: 1.16x slower                                          |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (7): json_dumps, generators, pidigits, bench_mp_pool, html5lib, comprehensions, json
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 53.58% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x
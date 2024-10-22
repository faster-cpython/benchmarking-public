# Results vs. 3.13.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.46x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 394 ms: 1.49x slower                                                  |
| docutils       | 2.58 sec                                               | 3.35 sec: 1.30x slower                                                |
| html5lib       | 64.5 ms                                                | 97.3 ms: 1.51x slower                                                 |
| tornado_http   | 91.5 ms                                                | 136 ms: 1.48x slower                                                  |
| Geometric mean | (ref)                                                  | 1.44x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 453 ms: 1.02x faster                                                  |
| async_tree_io_tg           | 825 ms                                                 | 845 ms: 1.02x slower                                                  |
| async_tree_io              | 843 ms                                                 | 908 ms: 1.08x slower                                                  |
| async_tree_none_tg         | 320 ms                                                 | 346 ms: 1.08x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 597 ms: 1.10x slower                                                  |
| async_tree_none            | 354 ms                                                 | 406 ms: 1.15x slower                                                  |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 662 ms: 1.15x slower                                                  |
| async_tree_memoization     | 442 ms                                                 | 510 ms: 1.15x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 2.08 sec: 1.16x slower                                                |
| asyncio_tcp                | 488 ms                                                 | 567 ms: 1.16x slower                                                  |
| async_generators           | 433 ms                                                 | 565 ms: 1.31x slower                                                  |
| coroutines                 | 22.5 ms                                                | 31.2 ms: 1.39x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.13x slower                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 184 ms: 1.01x faster                                                  |
| float          | 78.5 ms                                                | 142 ms: 1.81x slower                                                  |
| nbody          | 85.7 ms                                                | 217 ms: 2.54x slower                                                  |
| Geometric mean | (ref)                                                  | 1.66x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.56 ms: 1.09x faster                                                 |
| regex_dna      | 220 ms                                                 | 221 ms: 1.01x slower                                                  |
| regex_v8       | 25.3 ms                                                | 26.8 ms: 1.06x slower                                                 |
| regex_compile  | 131 ms                                                 | 217 ms: 1.66x slower                                                  |
| Geometric mean | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 142 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 102 ms                                                 | 111 ms: 1.09x slower                                                  |
| json_loads           | 27.0 us                                                | 32.2 us: 1.19x slower                                                 |
| xml_etree_generate   | 87.0 ms                                                | 111 ms: 1.27x slower                                                  |
| json_dumps           | 10.4 ms                                                | 13.4 ms: 1.28x slower                                                 |
| xml_etree_process    | 60.4 ms                                                | 89.5 ms: 1.48x slower                                                 |
| tomli_loads          | 2.11 sec                                               | 3.22 sec: 1.53x slower                                                |
| unpickle_pure_python | 213 us                                                 | 399 us: 1.87x slower                                                  |
| pickle_pure_python   | 300 us                                                 | 571 us: 1.90x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.36x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 13.4 ms: 1.27x slower                                                 |
| python_startup_no_site | 6.99 ms                                                | 9.08 ms: 1.30x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 50.3 ms                                                | 83.9 ms: 1.67x slower                                                 |
| genshi_text     | 22.9 ms                                                | 40.2 ms: 1.76x slower                                                 |
| django_template | 34.4 ms                                                | 60.9 ms: 1.77x slower                                                 |
| mako            | 11.1 ms                                                | 21.1 ms: 1.90x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.77x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal               | 3.81 ms                                                | 2.89 ms: 1.31x faster                                                 |
| create_gc_cycles           | 1.61 ms                                                | 1.37 ms: 1.18x faster                                                 |
| xml_etree_parse            | 156 ms                                                 | 142 ms: 1.10x faster                                                  |
| regex_effbot               | 3.88 ms                                                | 3.56 ms: 1.09x faster                                                 |
| async_tree_memoization_tg  | 465 ms                                                 | 453 ms: 1.02x faster                                                  |
| pidigits                   | 186 ms                                                 | 184 ms: 1.01x faster                                                  |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.00x faster                                                 |
| regex_dna                  | 220 ms                                                 | 221 ms: 1.01x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 845 ms: 1.02x slower                                                  |
| regex_v8                   | 25.3 ms                                                | 26.8 ms: 1.06x slower                                                 |
| async_tree_io              | 843 ms                                                 | 908 ms: 1.08x slower                                                  |
| async_tree_none_tg         | 320 ms                                                 | 346 ms: 1.08x slower                                                  |
| xml_etree_iterparse        | 102 ms                                                 | 111 ms: 1.09x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 597 ms: 1.10x slower                                                  |
| pathlib                    | 17.1 ms                                                | 19.2 ms: 1.13x slower                                                 |
| async_tree_none            | 354 ms                                                 | 406 ms: 1.15x slower                                                  |
| json                       | 5.20 ms                                                | 5.99 ms: 1.15x slower                                                 |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 662 ms: 1.15x slower                                                  |
| async_tree_memoization     | 442 ms                                                 | 510 ms: 1.15x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 2.08 sec: 1.16x slower                                                |
| asyncio_tcp                | 488 ms                                                 | 567 ms: 1.16x slower                                                  |
| telco                      | 8.45 ms                                                | 10.0 ms: 1.18x slower                                                 |
| json_loads                 | 27.0 us                                                | 32.2 us: 1.19x slower                                                 |
| deepcopy                   | 352 us                                                 | 423 us: 1.20x slower                                                  |
| mdp                        | 2.74 sec                                               | 3.37 sec: 1.23x slower                                                |
| pylint                     | 313 ms                                                 | 394 ms: 1.26x slower                                                  |
| python_startup             | 10.6 ms                                                | 13.4 ms: 1.27x slower                                                 |
| xml_etree_generate         | 87.0 ms                                                | 111 ms: 1.27x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 13.4 ms: 1.28x slower                                                 |
| scimark_fft                | 369 ms                                                 | 475 ms: 1.29x slower                                                  |
| docutils                   | 2.58 sec                                               | 3.35 sec: 1.30x slower                                                |
| python_startup_no_site     | 6.99 ms                                                | 9.08 ms: 1.30x slower                                                 |
| async_generators           | 433 ms                                                 | 565 ms: 1.31x slower                                                  |
| coverage                   | 83.7 ms                                                | 110 ms: 1.32x slower                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.63 ms: 1.32x slower                                                 |
| generators                 | 28.8 ms                                                | 38.0 ms: 1.32x slower                                                 |
| pycparser                  | 1.19 sec                                               | 1.64 sec: 1.37x slower                                                |
| meteor_contest             | 108 ms                                                 | 148 ms: 1.37x slower                                                  |
| deepcopy_memo              | 38.0 us                                                | 52.3 us: 1.38x slower                                                 |
| coroutines                 | 22.5 ms                                                | 31.2 ms: 1.39x slower                                                 |
| deepcopy_reduce            | 3.17 us                                                | 4.42 us: 1.40x slower                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 6.61 sec: 1.41x slower                                                |
| sympy_integrate            | 19.9 ms                                                | 28.7 ms: 1.44x slower                                                 |
| nqueens                    | 80.6 ms                                                | 119 ms: 1.48x slower                                                  |
| xml_etree_process          | 60.4 ms                                                | 89.5 ms: 1.48x slower                                                 |
| tornado_http               | 91.5 ms                                                | 136 ms: 1.48x slower                                                  |
| 2to3                       | 265 ms                                                 | 394 ms: 1.49x slower                                                  |
| html5lib                   | 64.5 ms                                                | 97.3 ms: 1.51x slower                                                 |
| tomli_loads                | 2.11 sec                                               | 3.22 sec: 1.53x slower                                                |
| crypto_pyaes               | 73.0 ms                                                | 112 ms: 1.54x slower                                                  |
| sympy_str                  | 274 ms                                                 | 424 ms: 1.55x slower                                                  |
| thrift                     | 796 us                                                 | 1.25 ms: 1.57x slower                                                 |
| typing_runtime_protocols   | 159 us                                                 | 254 us: 1.60x slower                                                  |
| fannkuch                   | 381 ms                                                 | 608 ms: 1.60x slower                                                  |
| spectral_norm              | 115 ms                                                 | 186 ms: 1.61x slower                                                  |
| richards                   | 48.1 ms                                                | 78.0 ms: 1.62x slower                                                 |
| sympy_expand               | 462 ms                                                 | 753 ms: 1.63x slower                                                  |
| sqlglot_normalize          | 107 ms                                                 | 177 ms: 1.65x slower                                                  |
| sqlglot_optimize           | 53.9 ms                                                | 88.8 ms: 1.65x slower                                                 |
| regex_compile              | 131 ms                                                 | 217 ms: 1.66x slower                                                  |
| genshi_xml                 | 50.3 ms                                                | 83.9 ms: 1.67x slower                                                 |
| pyflate                    | 460 ms                                                 | 777 ms: 1.69x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 254 ms: 1.70x slower                                                  |
| richards_super             | 54.4 ms                                                | 94.6 ms: 1.74x slower                                                 |
| comprehensions             | 16.4 us                                                | 28.7 us: 1.75x slower                                                 |
| genshi_text                | 22.9 ms                                                | 40.2 ms: 1.76x slower                                                 |
| pprint_safe_repr           | 744 ms                                                 | 1.32 sec: 1.77x slower                                                |
| django_template            | 34.4 ms                                                | 60.9 ms: 1.77x slower                                                 |
| pprint_pformat             | 1.51 sec                                               | 2.72 sec: 1.80x slower                                                |
| float                      | 78.5 ms                                                | 142 ms: 1.81x slower                                                  |
| logging_silent             | 102 ns                                                 | 185 ns: 1.81x slower                                                  |
| scimark_monte_carlo        | 66.3 ms                                                | 124 ms: 1.87x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 399 us: 1.87x slower                                                  |
| logging_simple             | 5.66 us                                                | 10.7 us: 1.88x slower                                                 |
| pickle_pure_python         | 300 us                                                 | 571 us: 1.90x slower                                                  |
| mako                       | 11.1 ms                                                | 21.1 ms: 1.90x slower                                                 |
| logging_format             | 6.25 us                                                | 12.0 us: 1.92x slower                                                 |
| hexiom                     | 6.13 ms                                                | 12.0 ms: 1.97x slower                                                 |
| sqlglot_transpile          | 1.57 ms                                                | 3.20 ms: 2.03x slower                                                 |
| chaos                      | 58.4 ms                                                | 124 ms: 2.13x slower                                                  |
| scimark_lu                 | 115 ms                                                 | 245 ms: 2.13x slower                                                  |
| sqlglot_parse              | 1.27 ms                                                | 2.71 ms: 2.14x slower                                                 |
| scimark_sor                | 122 ms                                                 | 264 ms: 2.15x slower                                                  |
| go                         | 142 ms                                                 | 307 ms: 2.17x slower                                                  |
| raytrace                   | 262 ms                                                 | 593 ms: 2.27x slower                                                  |
| nbody                      | 85.7 ms                                                | 217 ms: 2.54x slower                                                  |
| deltablue                  | 3.15 ms                                                | 8.28 ms: 2.63x slower                                                 |
| bench_thread_pool          | 815 us                                                 | 3.03 ms: 3.71x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.46x slower                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.36x
- 95% likely to have a slowdown of 1.34x
- 99% likely to have a slowdown of 1.30x

# Memory
- memory change: 1.16x
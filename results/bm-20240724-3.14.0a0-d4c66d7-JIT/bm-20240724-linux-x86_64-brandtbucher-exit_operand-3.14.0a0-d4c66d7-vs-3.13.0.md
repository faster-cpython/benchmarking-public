# Results vs. 3.13.0

- fork: brandtbucher
- ref: exit_operand
- machine: linux-x86_64
- commit hash: d4c66d7
- commit date: 2024-07-24
- overall geometric mean: 1.00x faster
- HPT reliability: 53.06%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 274 ms: 1.03x slower                                                |
| docutils       | 2.58 sec                                               | 2.91 sec: 1.13x slower                                              |
| html5lib       | 64.5 ms                                                | 63.9 ms: 1.01x faster                                               |
| tornado_http   | 91.5 ms                                                | 94.1 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.04x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 391 ms: 1.19x faster                                                |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                                |
| async_tree_memoization     | 442 ms                                                 | 420 ms: 1.05x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 533 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 565 ms: 1.02x faster                                                |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                              |
| coroutines                 | 22.5 ms                                                | 23.1 ms: 1.03x slower                                               |
| asyncio_tcp                | 488 ms                                                 | 505 ms: 1.04x slower                                                |
| async_tree_io_tg           | 825 ms                                                 | 860 ms: 1.04x slower                                                |
| async_tree_io              | 843 ms                                                 | 891 ms: 1.06x slower                                                |
| async_generators           | 433 ms                                                 | 465 ms: 1.07x slower                                                |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.8 ms: 1.11x faster                                               |
| nbody          | 85.7 ms                                                | 80.4 ms: 1.07x faster                                               |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.94 ms: 1.01x slower                                               |
| regex_dna      | 220 ms                                                 | 229 ms: 1.04x slower                                                |
| regex_compile  | 131 ms                                                 | 139 ms: 1.06x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x slower                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 80.7 ms: 1.08x faster                                               |
| tomli_loads          | 2.11 sec                                               | 1.97 sec: 1.07x faster                                              |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                |
| xml_etree_process    | 60.4 ms                                                | 57.9 ms: 1.04x faster                                               |
| xml_etree_iterparse  | 102 ms                                                 | 100 ms: 1.02x faster                                                |
| pickle_pure_python   | 300 us                                                 | 298 us: 1.01x faster                                                |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                |
| json_loads           | 27.0 us                                                | 28.2 us: 1.04x slower                                               |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.01x slower                                               |
| python_startup_no_site | 6.99 ms                                                | 7.19 ms: 1.03x slower                                               |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.79 ms: 1.13x faster                                               |
| django_template | 34.4 ms                                                | 35.9 ms: 1.04x slower                                               |
| genshi_text     | 22.9 ms                                                | 25.0 ms: 1.09x slower                                               |
| genshi_xml      | 50.3 ms                                                | 57.8 ms: 1.15x slower                                               |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 29.4 us: 1.29x faster                                               |
| deepcopy                   | 352 us                                                 | 277 us: 1.27x faster                                                |
| async_tree_memoization_tg  | 465 ms                                                 | 391 ms: 1.19x faster                                                |
| scimark_fft                | 369 ms                                                 | 313 ms: 1.18x faster                                                |
| richards                   | 48.1 ms                                                | 41.0 ms: 1.17x faster                                               |
| richards_super             | 54.4 ms                                                | 47.1 ms: 1.16x faster                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.36 ms: 1.15x faster                                               |
| mako                       | 11.1 ms                                                | 9.79 ms: 1.13x faster                                               |
| deepcopy_reduce            | 3.17 us                                                | 2.85 us: 1.11x faster                                               |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.11x faster                                                |
| float                      | 78.5 ms                                                | 70.8 ms: 1.11x faster                                               |
| scimark_monte_carlo        | 66.3 ms                                                | 60.9 ms: 1.09x faster                                               |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                |
| xml_etree_generate         | 87.0 ms                                                | 80.7 ms: 1.08x faster                                               |
| mdp                        | 2.74 sec                                               | 2.55 sec: 1.08x faster                                              |
| crypto_pyaes               | 73.0 ms                                                | 68.0 ms: 1.07x faster                                               |
| tomli_loads                | 2.11 sec                                               | 1.97 sec: 1.07x faster                                              |
| telco                      | 8.45 ms                                                | 7.91 ms: 1.07x faster                                               |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                                |
| nbody                      | 85.7 ms                                                | 80.4 ms: 1.07x faster                                               |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                               |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                |
| async_tree_memoization     | 442 ms                                                 | 420 ms: 1.05x faster                                                |
| pyflate                    | 460 ms                                                 | 437 ms: 1.05x faster                                                |
| xml_etree_process          | 60.4 ms                                                | 57.9 ms: 1.04x faster                                               |
| pprint_pformat             | 1.51 sec                                               | 1.45 sec: 1.04x faster                                              |
| pprint_safe_repr           | 744 ms                                                 | 715 ms: 1.04x faster                                                |
| fannkuch                   | 381 ms                                                 | 368 ms: 1.03x faster                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.54 sec: 1.03x faster                                              |
| logging_format             | 6.25 us                                                | 6.10 us: 1.02x faster                                               |
| logging_simple             | 5.66 us                                                | 5.54 us: 1.02x faster                                               |
| gc_traversal               | 3.81 ms                                                | 3.72 ms: 1.02x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 533 ms: 1.02x faster                                                |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.02x faster                                              |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                |
| xml_etree_iterparse        | 102 ms                                                 | 100 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 565 ms: 1.02x faster                                                |
| html5lib                   | 64.5 ms                                                | 63.9 ms: 1.01x faster                                               |
| pickle_pure_python         | 300 us                                                 | 298 us: 1.01x faster                                                |
| pidigits                   | 186 ms                                                 | 185 ms: 1.00x faster                                                |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.01x slower                                               |
| comprehensions             | 16.4 us                                                | 16.5 us: 1.01x slower                                               |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                              |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                               |
| regex_effbot               | 3.88 ms                                                | 3.94 ms: 1.01x slower                                               |
| generators                 | 28.8 ms                                                | 29.4 ms: 1.02x slower                                               |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                |
| bench_thread_pool          | 815 us                                                 | 834 us: 1.02x slower                                                |
| sqlglot_transpile          | 1.57 ms                                                | 1.61 ms: 1.03x slower                                               |
| coroutines                 | 22.5 ms                                                | 23.1 ms: 1.03x slower                                               |
| tornado_http               | 91.5 ms                                                | 94.1 ms: 1.03x slower                                               |
| logging_silent             | 102 ns                                                 | 105 ns: 1.03x slower                                                |
| python_startup_no_site     | 6.99 ms                                                | 7.19 ms: 1.03x slower                                               |
| 2to3                       | 265 ms                                                 | 274 ms: 1.03x slower                                                |
| asyncio_tcp                | 488 ms                                                 | 505 ms: 1.04x slower                                                |
| regex_dna                  | 220 ms                                                 | 229 ms: 1.04x slower                                                |
| sqlglot_optimize           | 53.9 ms                                                | 56.1 ms: 1.04x slower                                               |
| async_tree_io_tg           | 825 ms                                                 | 860 ms: 1.04x slower                                                |
| django_template            | 34.4 ms                                                | 35.9 ms: 1.04x slower                                               |
| json_loads                 | 27.0 us                                                | 28.2 us: 1.04x slower                                               |
| go                         | 142 ms                                                 | 148 ms: 1.05x slower                                                |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                                |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.05x slower                                                |
| typing_runtime_protocols   | 159 us                                                 | 168 us: 1.06x slower                                                |
| async_tree_io              | 843 ms                                                 | 891 ms: 1.06x slower                                                |
| scimark_sor                | 122 ms                                                 | 130 ms: 1.06x slower                                                |
| regex_compile              | 131 ms                                                 | 139 ms: 1.06x slower                                                |
| async_generators           | 433 ms                                                 | 465 ms: 1.07x slower                                                |
| hexiom                     | 6.13 ms                                                | 6.62 ms: 1.08x slower                                               |
| dask                       | 338 ms                                                 | 366 ms: 1.08x slower                                                |
| coverage                   | 83.7 ms                                                | 90.9 ms: 1.09x slower                                               |
| create_gc_cycles           | 1.61 ms                                                | 1.75 ms: 1.09x slower                                               |
| sympy_str                  | 274 ms                                                 | 299 ms: 1.09x slower                                                |
| genshi_text                | 22.9 ms                                                | 25.0 ms: 1.09x slower                                               |
| sympy_expand               | 462 ms                                                 | 506 ms: 1.10x slower                                                |
| nqueens                    | 80.6 ms                                                | 88.7 ms: 1.10x slower                                               |
| scimark_lu                 | 115 ms                                                 | 127 ms: 1.10x slower                                                |
| dulwich_log                | 63.0 ms                                                | 69.8 ms: 1.11x slower                                               |
| sympy_integrate            | 19.9 ms                                                | 22.3 ms: 1.12x slower                                               |
| docutils                   | 2.58 sec                                               | 2.91 sec: 1.13x slower                                              |
| pylint                     | 313 ms                                                 | 353 ms: 1.13x slower                                                |
| sympy_sum                  | 150 ms                                                 | 170 ms: 1.14x slower                                                |
| genshi_xml                 | 50.3 ms                                                | 57.8 ms: 1.15x slower                                               |
| deltablue                  | 3.15 ms                                                | 3.64 ms: 1.16x slower                                               |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (7): json, json_dumps, chaos, bench_mp_pool, regex_v8, thrift, asyncio_websockets
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 53.06% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x
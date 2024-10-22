# Results vs. 3.13.0

- fork: brandtbucher
- ref: inline_class_call_de
- machine: linux-x86_64
- commit hash: 5f50be9
- commit date: 2024-07-26
- overall geometric mean: 1.01x faster
- HPT reliability: 65.43%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 272 ms: 1.03x slower                                                        |
| docutils       | 2.58 sec                                               | 2.91 sec: 1.12x slower                                                      |
| tornado_http   | 91.5 ms                                                | 92.9 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 395 ms: 1.18x faster                                                        |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                        |
| async_tree_none_tg         | 320 ms                                                 | 303 ms: 1.06x faster                                                        |
| async_tree_memoization     | 442 ms                                                 | 420 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 535 ms: 1.02x faster                                                        |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                      |
| asyncio_tcp                | 488 ms                                                 | 497 ms: 1.02x slower                                                        |
| coroutines                 | 22.5 ms                                                | 23.1 ms: 1.03x slower                                                       |
| async_tree_io_tg           | 825 ms                                                 | 872 ms: 1.06x slower                                                        |
| async_generators           | 433 ms                                                 | 462 ms: 1.07x slower                                                        |
| async_tree_io              | 843 ms                                                 | 902 ms: 1.07x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.2 ms: 1.10x faster                                                       |
| nbody          | 85.7 ms                                                | 78.9 ms: 1.09x faster                                                       |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.74 ms: 1.04x faster                                                       |
| regex_dna      | 220 ms                                                 | 221 ms: 1.01x slower                                                        |
| regex_compile  | 131 ms                                                 | 135 ms: 1.03x slower                                                        |
| regex_v8       | 25.3 ms                                                | 26.1 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 79.9 ms: 1.09x faster                                                       |
| tomli_loads          | 2.11 sec                                               | 1.95 sec: 1.08x faster                                                      |
| xml_etree_parse      | 156 ms                                                 | 144 ms: 1.08x faster                                                        |
| xml_etree_process    | 60.4 ms                                                | 56.3 ms: 1.07x faster                                                       |
| xml_etree_iterparse  | 102 ms                                                 | 99.2 ms: 1.03x faster                                                       |
| pickle_pure_python   | 300 us                                                 | 293 us: 1.02x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                        |
| json_loads           | 27.0 us                                                | 28.0 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                       |
| python_startup_no_site | 6.99 ms                                                | 7.20 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.81 ms: 1.13x faster                                                       |
| django_template | 34.4 ms                                                | 35.0 ms: 1.02x slower                                                       |
| genshi_text     | 22.9 ms                                                | 25.4 ms: 1.11x slower                                                       |
| genshi_xml      | 50.3 ms                                                | 58.8 ms: 1.17x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 28.8 us: 1.32x faster                                                       |
| deepcopy                   | 352 us                                                 | 269 us: 1.31x faster                                                        |
| scimark_fft                | 369 ms                                                 | 307 ms: 1.20x faster                                                        |
| richards                   | 48.1 ms                                                | 40.4 ms: 1.19x faster                                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 395 ms: 1.18x faster                                                        |
| richards_super             | 54.4 ms                                                | 46.6 ms: 1.17x faster                                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.40 ms: 1.14x faster                                                       |
| mako                       | 11.1 ms                                                | 9.81 ms: 1.13x faster                                                       |
| deepcopy_reduce            | 3.17 us                                                | 2.81 us: 1.13x faster                                                       |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                        |
| float                      | 78.5 ms                                                | 71.2 ms: 1.10x faster                                                       |
| scimark_monte_carlo        | 66.3 ms                                                | 60.2 ms: 1.10x faster                                                       |
| xml_etree_generate         | 87.0 ms                                                | 79.9 ms: 1.09x faster                                                       |
| nbody                      | 85.7 ms                                                | 78.9 ms: 1.09x faster                                                       |
| crypto_pyaes               | 73.0 ms                                                | 67.2 ms: 1.09x faster                                                       |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                        |
| tomli_loads                | 2.11 sec                                               | 1.95 sec: 1.08x faster                                                      |
| xml_etree_parse            | 156 ms                                                 | 144 ms: 1.08x faster                                                        |
| pathlib                    | 17.1 ms                                                | 15.9 ms: 1.08x faster                                                       |
| xml_etree_process          | 60.4 ms                                                | 56.3 ms: 1.07x faster                                                       |
| telco                      | 8.45 ms                                                | 7.94 ms: 1.06x faster                                                       |
| async_tree_none_tg         | 320 ms                                                 | 303 ms: 1.06x faster                                                        |
| mdp                        | 2.74 sec                                               | 2.60 sec: 1.05x faster                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.45 sec: 1.05x faster                                                      |
| pprint_safe_repr           | 744 ms                                                 | 706 ms: 1.05x faster                                                        |
| async_tree_memoization     | 442 ms                                                 | 420 ms: 1.05x faster                                                        |
| pyflate                    | 460 ms                                                 | 438 ms: 1.05x faster                                                        |
| regex_effbot               | 3.88 ms                                                | 3.74 ms: 1.04x faster                                                       |
| pprint_pformat             | 1.51 sec                                               | 1.46 sec: 1.04x faster                                                      |
| fannkuch                   | 381 ms                                                 | 368 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 102 ms                                                 | 99.2 ms: 1.03x faster                                                       |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                      |
| pickle_pure_python         | 300 us                                                 | 293 us: 1.02x faster                                                        |
| logging_simple             | 5.66 us                                                | 5.55 us: 1.02x faster                                                       |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                        |
| logging_format             | 6.25 us                                                | 6.15 us: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 535 ms: 1.02x faster                                                        |
| chaos                      | 58.4 ms                                                | 57.7 ms: 1.01x faster                                                       |
| pidigits                   | 186 ms                                                 | 185 ms: 1.01x faster                                                        |
| generators                 | 28.8 ms                                                | 28.7 ms: 1.01x faster                                                       |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                        |
| sqlglot_parse              | 1.27 ms                                                | 1.27 ms: 1.01x slower                                                       |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                       |
| regex_dna                  | 220 ms                                                 | 221 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                      |
| comprehensions             | 16.4 us                                                | 16.5 us: 1.01x slower                                                       |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                        |
| bench_thread_pool          | 815 us                                                 | 827 us: 1.01x slower                                                        |
| typing_runtime_protocols   | 159 us                                                 | 162 us: 1.02x slower                                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                       |
| tornado_http               | 91.5 ms                                                | 92.9 ms: 1.02x slower                                                       |
| go                         | 142 ms                                                 | 144 ms: 1.02x slower                                                        |
| gc_traversal               | 3.81 ms                                                | 3.87 ms: 1.02x slower                                                       |
| asyncio_tcp                | 488 ms                                                 | 497 ms: 1.02x slower                                                        |
| django_template            | 34.4 ms                                                | 35.0 ms: 1.02x slower                                                       |
| raytrace                   | 262 ms                                                 | 268 ms: 1.03x slower                                                        |
| regex_compile              | 131 ms                                                 | 135 ms: 1.03x slower                                                        |
| logging_silent             | 102 ns                                                 | 105 ns: 1.03x slower                                                        |
| 2to3                       | 265 ms                                                 | 272 ms: 1.03x slower                                                        |
| coroutines                 | 22.5 ms                                                | 23.1 ms: 1.03x slower                                                       |
| python_startup_no_site     | 6.99 ms                                                | 7.20 ms: 1.03x slower                                                       |
| regex_v8                   | 25.3 ms                                                | 26.1 ms: 1.03x slower                                                       |
| sqlglot_optimize           | 53.9 ms                                                | 55.9 ms: 1.04x slower                                                       |
| json_loads                 | 27.0 us                                                | 28.0 us: 1.04x slower                                                       |
| sqlglot_normalize          | 107 ms                                                 | 112 ms: 1.05x slower                                                        |
| scimark_sor                | 122 ms                                                 | 129 ms: 1.05x slower                                                        |
| async_tree_io_tg           | 825 ms                                                 | 872 ms: 1.06x slower                                                        |
| hexiom                     | 6.13 ms                                                | 6.52 ms: 1.06x slower                                                       |
| async_generators           | 433 ms                                                 | 462 ms: 1.07x slower                                                        |
| nqueens                    | 80.6 ms                                                | 86.2 ms: 1.07x slower                                                       |
| async_tree_io              | 843 ms                                                 | 902 ms: 1.07x slower                                                        |
| sympy_str                  | 274 ms                                                 | 295 ms: 1.08x slower                                                        |
| dask                       | 338 ms                                                 | 365 ms: 1.08x slower                                                        |
| sympy_expand               | 462 ms                                                 | 502 ms: 1.09x slower                                                        |
| scimark_lu                 | 115 ms                                                 | 125 ms: 1.09x slower                                                        |
| create_gc_cycles           | 1.61 ms                                                | 1.77 ms: 1.10x slower                                                       |
| coverage                   | 83.7 ms                                                | 92.3 ms: 1.10x slower                                                       |
| genshi_text                | 22.9 ms                                                | 25.4 ms: 1.11x slower                                                       |
| deltablue                  | 3.15 ms                                                | 3.50 ms: 1.11x slower                                                       |
| pylint                     | 313 ms                                                 | 350 ms: 1.12x slower                                                        |
| sympy_integrate            | 19.9 ms                                                | 22.3 ms: 1.12x slower                                                       |
| sympy_sum                  | 150 ms                                                 | 168 ms: 1.12x slower                                                        |
| docutils                   | 2.58 sec                                               | 2.91 sec: 1.12x slower                                                      |
| genshi_xml                 | 50.3 ms                                                | 58.8 ms: 1.17x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, json, json_dumps, html5lib, bench_mp_pool, thrift
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 65.43% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x
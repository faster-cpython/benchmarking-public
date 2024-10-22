# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: 858ee75
- commit date: 2024-07-13
- overall geometric mean: 1.01x faster
- HPT reliability: 58.41%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 273 ms: 1.03x slower                                                        |
| docutils       | 2.58 sec                                               | 2.89 sec: 1.12x slower                                                      |
| html5lib       | 64.5 ms                                                | 63.6 ms: 1.02x faster                                                       |
| tornado_http   | 91.5 ms                                                | 93.0 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 376 ms: 1.24x faster                                                        |
| async_tree_none            | 354 ms                                                 | 325 ms: 1.09x faster                                                        |
| async_tree_memoization     | 442 ms                                                 | 407 ms: 1.09x faster                                                        |
| async_tree_none_tg         | 320 ms                                                 | 298 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 562 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 536 ms: 1.01x faster                                                        |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| async_tree_io_tg           | 825 ms                                                 | 843 ms: 1.02x slower                                                        |
| asyncio_tcp                | 488 ms                                                 | 503 ms: 1.03x slower                                                        |
| async_generators           | 433 ms                                                 | 451 ms: 1.04x slower                                                        |
| coroutines                 | 22.5 ms                                                | 23.7 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.9 ms: 1.11x faster                                                       |
| nbody          | 85.7 ms                                                | 79.5 ms: 1.08x faster                                                       |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 131 ms                                                 | 134 ms: 1.02x slower                                                        |
| regex_effbot   | 3.88 ms                                                | 4.03 ms: 1.04x slower                                                       |
| regex_v8       | 25.3 ms                                                | 26.3 ms: 1.04x slower                                                       |
| regex_dna      | 220 ms                                                 | 238 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.93 sec: 1.09x faster                                                      |
| xml_etree_generate   | 87.0 ms                                                | 81.4 ms: 1.07x faster                                                       |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                        |
| xml_etree_process    | 60.4 ms                                                | 57.3 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 102 ms                                                 | 98.5 ms: 1.04x faster                                                       |
| pickle_pure_python   | 300 us                                                 | 297 us: 1.01x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                        |
| json_loads           | 27.0 us                                                | 28.5 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.4 ms: 1.01x faster                                                       |
| python_startup_no_site | 6.99 ms                                                | 7.06 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.73 ms: 1.14x faster                                                       |
| django_template | 34.4 ms                                                | 35.5 ms: 1.03x slower                                                       |
| genshi_text     | 22.9 ms                                                | 25.1 ms: 1.10x slower                                                       |
| genshi_xml      | 50.3 ms                                                | 58.8 ms: 1.17x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 28.3 us: 1.34x faster                                                       |
| deepcopy                   | 352 us                                                 | 272 us: 1.30x faster                                                        |
| async_tree_memoization_tg  | 465 ms                                                 | 376 ms: 1.24x faster                                                        |
| scimark_fft                | 369 ms                                                 | 313 ms: 1.18x faster                                                        |
| deepcopy_reduce            | 3.17 us                                                | 2.74 us: 1.16x faster                                                       |
| richards                   | 48.1 ms                                                | 42.0 ms: 1.14x faster                                                       |
| mako                       | 11.1 ms                                                | 9.73 ms: 1.14x faster                                                       |
| richards_super             | 54.4 ms                                                | 47.7 ms: 1.14x faster                                                       |
| float                      | 78.5 ms                                                | 70.9 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.54 ms: 1.11x faster                                                       |
| spectral_norm              | 115 ms                                                 | 105 ms: 1.10x faster                                                        |
| scimark_monte_carlo        | 66.3 ms                                                | 60.4 ms: 1.10x faster                                                       |
| tomli_loads                | 2.11 sec                                               | 1.93 sec: 1.09x faster                                                      |
| crypto_pyaes               | 73.0 ms                                                | 66.9 ms: 1.09x faster                                                       |
| async_tree_none            | 354 ms                                                 | 325 ms: 1.09x faster                                                        |
| async_tree_memoization     | 442 ms                                                 | 407 ms: 1.09x faster                                                        |
| mdp                        | 2.74 sec                                               | 2.53 sec: 1.08x faster                                                      |
| nbody                      | 85.7 ms                                                | 79.5 ms: 1.08x faster                                                       |
| async_tree_none_tg         | 320 ms                                                 | 298 ms: 1.07x faster                                                        |
| gc_traversal               | 3.81 ms                                                | 3.55 ms: 1.07x faster                                                       |
| xml_etree_generate         | 87.0 ms                                                | 81.4 ms: 1.07x faster                                                       |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                        |
| pathlib                    | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                       |
| xml_etree_process          | 60.4 ms                                                | 57.3 ms: 1.05x faster                                                       |
| pyflate                    | 460 ms                                                 | 439 ms: 1.05x faster                                                        |
| telco                      | 8.45 ms                                                | 8.08 ms: 1.05x faster                                                       |
| pprint_safe_repr           | 744 ms                                                 | 713 ms: 1.04x faster                                                        |
| logging_simple             | 5.66 us                                                | 5.43 us: 1.04x faster                                                       |
| fannkuch                   | 381 ms                                                 | 366 ms: 1.04x faster                                                        |
| xml_etree_iterparse        | 102 ms                                                 | 98.5 ms: 1.04x faster                                                       |
| logging_format             | 6.25 us                                                | 6.08 us: 1.03x faster                                                       |
| pprint_pformat             | 1.51 sec                                               | 1.48 sec: 1.02x faster                                                      |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 562 ms: 1.02x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.61 sec: 1.02x faster                                                      |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                        |
| html5lib                   | 64.5 ms                                                | 63.6 ms: 1.02x faster                                                       |
| json                       | 5.20 ms                                                | 5.12 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 536 ms: 1.01x faster                                                        |
| python_startup             | 10.6 ms                                                | 10.4 ms: 1.01x faster                                                       |
| pickle_pure_python         | 300 us                                                 | 297 us: 1.01x faster                                                        |
| chaos                      | 58.4 ms                                                | 57.9 ms: 1.01x faster                                                       |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                        |
| python_startup_no_site     | 6.99 ms                                                | 7.06 ms: 1.01x slower                                                       |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                                       |
| tornado_http               | 91.5 ms                                                | 93.0 ms: 1.02x slower                                                       |
| go                         | 142 ms                                                 | 144 ms: 1.02x slower                                                        |
| async_tree_io_tg           | 825 ms                                                 | 843 ms: 1.02x slower                                                        |
| regex_compile              | 131 ms                                                 | 134 ms: 1.02x slower                                                        |
| bench_thread_pool          | 815 us                                                 | 833 us: 1.02x slower                                                        |
| raytrace                   | 262 ms                                                 | 268 ms: 1.02x slower                                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.61 ms: 1.02x slower                                                       |
| 2to3                       | 265 ms                                                 | 273 ms: 1.03x slower                                                        |
| django_template            | 34.4 ms                                                | 35.5 ms: 1.03x slower                                                       |
| asyncio_tcp                | 488 ms                                                 | 503 ms: 1.03x slower                                                        |
| sqlglot_optimize           | 53.9 ms                                                | 55.7 ms: 1.03x slower                                                       |
| regex_effbot               | 3.88 ms                                                | 4.03 ms: 1.04x slower                                                       |
| sqlglot_normalize          | 107 ms                                                 | 111 ms: 1.04x slower                                                        |
| regex_v8                   | 25.3 ms                                                | 26.3 ms: 1.04x slower                                                       |
| async_generators           | 433 ms                                                 | 451 ms: 1.04x slower                                                        |
| logging_silent             | 102 ns                                                 | 106 ns: 1.04x slower                                                        |
| generators                 | 28.8 ms                                                | 30.2 ms: 1.05x slower                                                       |
| coroutines                 | 22.5 ms                                                | 23.7 ms: 1.05x slower                                                       |
| json_loads                 | 27.0 us                                                | 28.5 us: 1.06x slower                                                       |
| nqueens                    | 80.6 ms                                                | 85.2 ms: 1.06x slower                                                       |
| scimark_sor                | 122 ms                                                 | 131 ms: 1.07x slower                                                        |
| hexiom                     | 6.13 ms                                                | 6.54 ms: 1.07x slower                                                       |
| dulwich_log                | 63.0 ms                                                | 67.3 ms: 1.07x slower                                                       |
| typing_runtime_protocols   | 159 us                                                 | 170 us: 1.07x slower                                                        |
| pylint                     | 313 ms                                                 | 335 ms: 1.07x slower                                                        |
| sympy_expand               | 462 ms                                                 | 495 ms: 1.07x slower                                                        |
| dask                       | 338 ms                                                 | 362 ms: 1.07x slower                                                        |
| sympy_str                  | 274 ms                                                 | 294 ms: 1.08x slower                                                        |
| regex_dna                  | 220 ms                                                 | 238 ms: 1.08x slower                                                        |
| create_gc_cycles           | 1.61 ms                                                | 1.74 ms: 1.08x slower                                                       |
| genshi_text                | 22.9 ms                                                | 25.1 ms: 1.10x slower                                                       |
| sympy_integrate            | 19.9 ms                                                | 22.1 ms: 1.11x slower                                                       |
| sympy_sum                  | 150 ms                                                 | 167 ms: 1.12x slower                                                        |
| docutils                   | 2.58 sec                                               | 2.89 sec: 1.12x slower                                                      |
| scimark_lu                 | 115 ms                                                 | 129 ms: 1.12x slower                                                        |
| coverage                   | 83.7 ms                                                | 93.9 ms: 1.12x slower                                                       |
| deltablue                  | 3.15 ms                                                | 3.54 ms: 1.13x slower                                                       |
| genshi_xml                 | 50.3 ms                                                | 58.8 ms: 1.17x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (5): async_tree_io, thrift, json_dumps, bench_mp_pool, pycparser
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 58.41% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x
# Results vs. 3.12.0

- fork: faster-cpython
- ref: binary_subscr_getite
- machine: linux-x86_64
- commit hash: d4df441
- commit date: 2024-08-01
- overall geometric mean: 1.08x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 273 ms: 1.01x faster                                                            |
| docutils       | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                          |
| tornado_http   | 103 ms                                                 | 92.3 ms: 1.11x faster                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 302 ms: 1.49x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                            |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 422 ms: 1.37x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 872 ms: 1.36x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 537 ms: 1.35x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 908 ms: 1.27x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.6 ms: 1.22x faster                                                           |
| float          | 84.7 ms                                                | 69.8 ms: 1.21x faster                                                           |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 133 ms: 1.12x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.89 ms: 1.08x slower                                                           |
| regex_dna      | 212 ms                                                 | 230 ms: 1.08x slower                                                            |
| regex_v8       | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                          |
| xml_etree_generate   | 89.2 ms                                                | 79.3 ms: 1.12x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 55.5 ms: 1.11x faster                                                           |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                            |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                                            |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 99.3 ms: 1.08x faster                                                           |
| json_loads           | 28.5 us                                                | 28.0 us: 1.02x faster                                                           |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.92 ms: 1.20x faster                                                           |
| django_template | 34.6 ms                                                | 35.6 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 302 ms: 1.49x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                            |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 28.5 us: 1.43x faster                                                           |
| async_tree_memoization     | 578 ms                                                 | 422 ms: 1.37x faster                                                            |
| deepcopy                   | 371 us                                                 | 271 us: 1.37x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 872 ms: 1.36x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 537 ms: 1.35x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.3 us: 1.34x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 908 ms: 1.27x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 60.1 ms: 1.25x faster                                                           |
| scimark_fft                | 382 ms                                                 | 306 ms: 1.25x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.22x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                          |
| nbody                      | 97.0 ms                                                | 79.6 ms: 1.22x faster                                                           |
| float                      | 84.7 ms                                                | 69.8 ms: 1.21x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 67.5 ms: 1.21x faster                                                           |
| mako                       | 11.9 ms                                                | 9.92 ms: 1.20x faster                                                           |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.20x faster                                                           |
| raytrace                   | 312 ms                                                 | 262 ms: 1.19x faster                                                            |
| logging_format             | 7.23 us                                                | 6.06 us: 1.19x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.46 us: 1.18x faster                                                           |
| chaos                      | 67.0 ms                                                | 57.4 ms: 1.17x faster                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.38 ms: 1.16x faster                                                           |
| richards                   | 45.8 ms                                                | 39.9 ms: 1.15x faster                                                           |
| scimark_sor                | 129 ms                                                 | 114 ms: 1.13x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 79.3 ms: 1.12x faster                                                           |
| fannkuch                   | 417 ms                                                 | 372 ms: 1.12x faster                                                            |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                            |
| regex_compile              | 148 ms                                                 | 133 ms: 1.12x faster                                                            |
| tornado_http               | 103 ms                                                 | 92.3 ms: 1.11x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 55.5 ms: 1.11x faster                                                           |
| pyflate                    | 482 ms                                                 | 435 ms: 1.11x faster                                                            |
| richards_super             | 51.5 ms                                                | 46.9 ms: 1.10x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                            |
| pprint_safe_repr           | 776 ms                                                 | 717 ms: 1.08x faster                                                            |
| scimark_lu                 | 118 ms                                                 | 109 ms: 1.08x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 99.3 ms: 1.08x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.49 ms: 1.07x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                          |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.05x faster                                                           |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                           |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                                            |
| bench_thread_pool          | 842 us                                                 | 815 us: 1.03x faster                                                            |
| gc_traversal               | 3.79 ms                                                | 3.68 ms: 1.03x faster                                                           |
| dask                       | 372 ms                                                 | 363 ms: 1.02x faster                                                            |
| json_loads                 | 28.5 us                                                | 28.0 us: 1.02x faster                                                           |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.02x faster                                                           |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                           |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                            |
| 2to3                       | 274 ms                                                 | 273 ms: 1.01x faster                                                            |
| sympy_sum                  | 169 ms                                                 | 170 ms: 1.01x slower                                                            |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 55.4 ms: 1.01x slower                                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                          |
| nqueens                    | 83.3 ms                                                | 84.6 ms: 1.02x slower                                                           |
| asyncio_tcp                | 491 ms                                                 | 499 ms: 1.02x slower                                                            |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                            |
| mdp                        | 2.63 sec                                               | 2.70 sec: 1.03x slower                                                          |
| django_template            | 34.6 ms                                                | 35.6 ms: 1.03x slower                                                           |
| python_startup_no_site     | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                           |
| hexiom                     | 6.41 ms                                                | 6.70 ms: 1.04x slower                                                           |
| sympy_integrate            | 21.4 ms                                                | 22.4 ms: 1.05x slower                                                           |
| go                         | 139 ms                                                 | 146 ms: 1.05x slower                                                            |
| docutils                   | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                          |
| generators                 | 31.2 ms                                                | 32.8 ms: 1.05x slower                                                           |
| sympy_expand               | 478 ms                                                 | 503 ms: 1.05x slower                                                            |
| regex_effbot               | 3.61 ms                                                | 3.89 ms: 1.08x slower                                                           |
| regex_dna                  | 212 ms                                                 | 230 ms: 1.08x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 172 us: 1.09x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                           |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                           |
| telco                      | 7.10 ms                                                | 7.97 ms: 1.12x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                           |
| coverage                   | 72.7 ms                                                | 90.9 ms: 1.25x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (5): pycparser, sympy_str, bench_mp_pool, async_generators, json
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240801-3.14.0a0-d4df441-JIT/bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.05x
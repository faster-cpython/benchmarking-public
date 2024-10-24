# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: 858ee75
- commit date: 2024-07-13
- overall geometric mean: 1.04x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 273 ms: 1.01x faster                                                        |
| docutils       | 2.83 sec                                                   | 2.89 sec: 1.02x slower                                                      |
| html5lib       | 67.2 ms                                                    | 63.6 ms: 1.06x faster                                                       |
| tornado_http   | 94.6 ms                                                    | 93.0 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 376 ms: 1.18x faster                                                        |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 407 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                        |
| async_tree_io              | 939 ms                                                     | 837 ms: 1.12x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 843 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 536 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 562 ms: 1.09x faster                                                        |
| Geometric mean             | (ref)                                                      | 1.13x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.9 ms: 1.11x faster                                                       |
| nbody          | 88.3 ms                                                    | 79.5 ms: 1.11x faster                                                       |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                      | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 134 ms: 1.02x faster                                                        |
| regex_v8       | 25.1 ms                                                    | 26.3 ms: 1.05x slower                                                       |
| regex_dna      | 221 ms                                                     | 238 ms: 1.08x slower                                                        |
| regex_effbot   | 3.67 ms                                                    | 4.03 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                      | 1.05x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                        |
| tomli_loads          | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                     | 98.5 ms: 1.09x faster                                                       |
| xml_etree_generate   | 87.4 ms                                                    | 81.4 ms: 1.07x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 57.3 ms: 1.07x faster                                                       |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                       |
| pickle_pure_python   | 305 us                                                     | 297 us: 1.03x faster                                                        |
| json_loads           | 28.9 us                                                    | 28.5 us: 1.01x faster                                                       |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                        |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.73 ms: 1.15x faster                                                       |
| django_template | 34.8 ms                                                    | 35.5 ms: 1.02x slower                                                       |
| genshi_text     | 23.7 ms                                                    | 25.1 ms: 1.06x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 58.8 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.3 us: 1.40x faster                                                       |
| deepcopy                   | 367 us                                                     | 272 us: 1.35x faster                                                        |
| scimark_fft                | 392 ms                                                     | 313 ms: 1.25x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                    | 2.74 us: 1.22x faster                                                       |
| richards                   | 50.9 ms                                                    | 42.0 ms: 1.21x faster                                                       |
| richards_super             | 57.4 ms                                                    | 47.7 ms: 1.20x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 376 ms: 1.18x faster                                                        |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                        |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.54 ms: 1.16x faster                                                       |
| crypto_pyaes               | 77.5 ms                                                    | 66.9 ms: 1.16x faster                                                       |
| mako                       | 11.2 ms                                                    | 9.73 ms: 1.15x faster                                                       |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.4 ms: 1.15x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 407 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                        |
| async_tree_io              | 939 ms                                                     | 837 ms: 1.12x faster                                                        |
| gc_traversal               | 3.98 ms                                                    | 3.55 ms: 1.12x faster                                                       |
| float                      | 78.9 ms                                                    | 70.9 ms: 1.11x faster                                                       |
| spectral_norm              | 116 ms                                                     | 105 ms: 1.11x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 843 ms: 1.11x faster                                                        |
| nbody                      | 88.3 ms                                                    | 79.5 ms: 1.11x faster                                                       |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                        |
| pyflate                    | 484 ms                                                     | 439 ms: 1.10x faster                                                        |
| mdp                        | 2.79 sec                                                   | 2.53 sec: 1.10x faster                                                      |
| fannkuch                   | 402 ms                                                     | 366 ms: 1.10x faster                                                        |
| tomli_loads                | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 536 ms: 1.10x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                     | 98.5 ms: 1.09x faster                                                       |
| bpe_tokeniser              | 5.02 sec                                                   | 4.61 sec: 1.09x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 562 ms: 1.09x faster                                                        |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                                       |
| xml_etree_generate         | 87.4 ms                                                    | 81.4 ms: 1.07x faster                                                       |
| xml_etree_process          | 61.2 ms                                                    | 57.3 ms: 1.07x faster                                                       |
| logging_format             | 6.47 us                                                    | 6.08 us: 1.06x faster                                                       |
| pprint_safe_repr           | 758 ms                                                     | 713 ms: 1.06x faster                                                        |
| chaos                      | 61.3 ms                                                    | 57.9 ms: 1.06x faster                                                       |
| html5lib                   | 67.2 ms                                                    | 63.6 ms: 1.06x faster                                                       |
| logging_simple             | 5.74 us                                                    | 5.43 us: 1.06x faster                                                       |
| pprint_pformat             | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                                      |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.04x faster                                                       |
| telco                      | 8.41 ms                                                    | 8.08 ms: 1.04x faster                                                       |
| thrift                     | 823 us                                                     | 793 us: 1.04x faster                                                        |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                        |
| json                       | 5.31 ms                                                    | 5.12 ms: 1.04x faster                                                       |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                                       |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                        |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                       |
| python_startup             | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                                       |
| pickle_pure_python         | 305 us                                                     | 297 us: 1.03x faster                                                        |
| regex_compile              | 137 ms                                                     | 134 ms: 1.02x faster                                                        |
| dask                       | 369 ms                                                     | 362 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                      |
| tornado_http               | 94.6 ms                                                    | 93.0 ms: 1.02x faster                                                       |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                        |
| json_loads                 | 28.9 us                                                    | 28.5 us: 1.01x faster                                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.61 ms: 1.01x faster                                                       |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                                        |
| asyncio_tcp                | 508 ms                                                     | 503 ms: 1.01x faster                                                        |
| python_startup_no_site     | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                                       |
| go                         | 145 ms                                                     | 144 ms: 1.01x faster                                                        |
| 2to3                       | 274 ms                                                     | 273 ms: 1.01x faster                                                        |
| raytrace                   | 267 ms                                                     | 268 ms: 1.00x slower                                                        |
| sqlglot_optimize           | 55.5 ms                                                    | 55.7 ms: 1.00x slower                                                       |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                       |
| coverage                   | 93.1 ms                                                    | 93.9 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 110 ms                                                     | 111 ms: 1.01x slower                                                        |
| logging_silent             | 105 ns                                                     | 106 ns: 1.02x slower                                                        |
| generators                 | 29.6 ms                                                    | 30.2 ms: 1.02x slower                                                       |
| django_template            | 34.8 ms                                                    | 35.5 ms: 1.02x slower                                                       |
| async_generators           | 442 ms                                                     | 451 ms: 1.02x slower                                                        |
| docutils                   | 2.83 sec                                                   | 2.89 sec: 1.02x slower                                                      |
| coroutines                 | 23.2 ms                                                    | 23.7 ms: 1.02x slower                                                       |
| scimark_sor                | 127 ms                                                     | 131 ms: 1.03x slower                                                        |
| pycparser                  | 1.16 sec                                                   | 1.20 sec: 1.03x slower                                                      |
| typing_runtime_protocols   | 165 us                                                     | 170 us: 1.03x slower                                                        |
| hexiom                     | 6.30 ms                                                    | 6.54 ms: 1.04x slower                                                       |
| sympy_str                  | 282 ms                                                     | 294 ms: 1.04x slower                                                        |
| nqueens                    | 81.4 ms                                                    | 85.2 ms: 1.05x slower                                                       |
| regex_v8                   | 25.1 ms                                                    | 26.3 ms: 1.05x slower                                                       |
| sympy_expand               | 473 ms                                                     | 495 ms: 1.05x slower                                                        |
| scimark_lu                 | 122 ms                                                     | 129 ms: 1.06x slower                                                        |
| genshi_text                | 23.7 ms                                                    | 25.1 ms: 1.06x slower                                                       |
| sympy_sum                  | 156 ms                                                     | 167 ms: 1.07x slower                                                        |
| regex_dna                  | 221 ms                                                     | 238 ms: 1.08x slower                                                        |
| sympy_integrate            | 20.5 ms                                                    | 22.1 ms: 1.08x slower                                                       |
| deltablue                  | 3.25 ms                                                    | 3.54 ms: 1.09x slower                                                       |
| regex_effbot               | 3.67 ms                                                    | 4.03 ms: 1.10x slower                                                       |
| genshi_xml                 | 51.6 ms                                                    | 58.8 ms: 1.14x slower                                                       |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                                |

Benchmark hidden because not significant (4): bench_thread_pool, comprehensions, dulwich_log, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x
# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: for_iter_tier_two_ex
- machine: linux-x86_64
- commit hash: e627230
- commit date: 2024-07-12
- overall geometric mean: 1.05x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 272 ms: 1.01x faster                                                        |
| docutils       | 2.83 sec                                                   | 2.87 sec: 1.02x slower                                                      |
| html5lib       | 67.2 ms                                                    | 64.2 ms: 1.05x faster                                                       |
| tornado_http   | 94.6 ms                                                    | 92.8 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 378 ms: 1.17x faster                                                        |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 409 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                        |
| async_tree_io              | 939 ms                                                     | 845 ms: 1.11x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 848 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 542 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                                        |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.7 ms: 1.13x faster                                                       |
| nbody          | 88.3 ms                                                    | 80.3 ms: 1.10x faster                                                       |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                      | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 134 ms: 1.02x faster                                                        |
| regex_dna      | 221 ms                                                     | 221 ms: 1.00x faster                                                        |
| regex_effbot   | 3.67 ms                                                    | 3.81 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                      | 1.00x slower                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.90 sec: 1.11x faster                                                      |
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.09x faster                                                        |
| xml_etree_generate   | 87.4 ms                                                    | 80.6 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                     | 99.0 ms: 1.08x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 56.9 ms: 1.08x faster                                                       |
| json_loads           | 28.9 us                                                    | 27.6 us: 1.05x faster                                                       |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                       |
| pickle_pure_python   | 305 us                                                     | 295 us: 1.04x faster                                                        |
| unpickle_pure_python | 218 us                                                     | 217 us: 1.01x faster                                                        |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.12 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.70 ms: 1.16x faster                                                       |
| django_template | 34.8 ms                                                    | 35.6 ms: 1.02x slower                                                       |
| genshi_text     | 23.7 ms                                                    | 25.0 ms: 1.06x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 56.1 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.00x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.5 us: 1.40x faster                                                       |
| deepcopy                   | 367 us                                                     | 273 us: 1.35x faster                                                        |
| scimark_fft                | 392 ms                                                     | 316 ms: 1.24x faster                                                        |
| richards                   | 50.9 ms                                                    | 41.2 ms: 1.23x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                    | 2.72 us: 1.23x faster                                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.33 ms: 1.22x faster                                                       |
| richards_super             | 57.4 ms                                                    | 48.3 ms: 1.19x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 378 ms: 1.17x faster                                                        |
| crypto_pyaes               | 77.5 ms                                                    | 66.8 ms: 1.16x faster                                                       |
| mako                       | 11.2 ms                                                    | 9.70 ms: 1.16x faster                                                       |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                        |
| spectral_norm              | 116 ms                                                     | 101 ms: 1.15x faster                                                        |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.5 ms: 1.14x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 409 ms: 1.13x faster                                                        |
| float                      | 78.9 ms                                                    | 69.7 ms: 1.13x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                        |
| tomli_loads                | 2.12 sec                                                   | 1.90 sec: 1.11x faster                                                      |
| async_tree_io              | 939 ms                                                     | 845 ms: 1.11x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 848 ms: 1.10x faster                                                        |
| fannkuch                   | 402 ms                                                     | 365 ms: 1.10x faster                                                        |
| nbody                      | 88.3 ms                                                    | 80.3 ms: 1.10x faster                                                       |
| pyflate                    | 484 ms                                                     | 441 ms: 1.10x faster                                                        |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.10x faster                                                       |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.09x faster                                                        |
| xml_etree_generate         | 87.4 ms                                                    | 80.6 ms: 1.08x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                     | 99.0 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 542 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                                        |
| xml_etree_process          | 61.2 ms                                                    | 56.9 ms: 1.08x faster                                                       |
| gc_traversal               | 3.98 ms                                                    | 3.71 ms: 1.07x faster                                                       |
| logging_format             | 6.47 us                                                    | 6.05 us: 1.07x faster                                                       |
| telco                      | 8.41 ms                                                    | 7.88 ms: 1.07x faster                                                       |
| pprint_safe_repr           | 758 ms                                                     | 712 ms: 1.07x faster                                                        |
| pprint_pformat             | 1.56 sec                                                   | 1.46 sec: 1.06x faster                                                      |
| chaos                      | 61.3 ms                                                    | 57.9 ms: 1.06x faster                                                       |
| meteor_contest             | 110 ms                                                     | 104 ms: 1.05x faster                                                        |
| logging_simple             | 5.74 us                                                    | 5.46 us: 1.05x faster                                                       |
| json_loads                 | 28.9 us                                                    | 27.6 us: 1.05x faster                                                       |
| html5lib                   | 67.2 ms                                                    | 64.2 ms: 1.05x faster                                                       |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                       |
| bpe_tokeniser              | 5.02 sec                                                   | 4.83 sec: 1.04x faster                                                      |
| mdp                        | 2.79 sec                                                   | 2.68 sec: 1.04x faster                                                      |
| pickle_pure_python         | 305 us                                                     | 295 us: 1.04x faster                                                        |
| json                       | 5.31 ms                                                    | 5.12 ms: 1.04x faster                                                       |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.04x faster                                                       |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                        |
| thrift                     | 823 us                                                     | 797 us: 1.03x faster                                                        |
| create_gc_cycles           | 1.82 ms                                                    | 1.77 ms: 1.03x faster                                                       |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                       |
| dask                       | 369 ms                                                     | 362 ms: 1.02x faster                                                        |
| tornado_http               | 94.6 ms                                                    | 92.8 ms: 1.02x faster                                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                      |
| regex_compile              | 137 ms                                                     | 134 ms: 1.02x faster                                                        |
| asyncio_tcp                | 508 ms                                                     | 501 ms: 1.02x faster                                                        |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.01x faster                                                        |
| sqlglot_transpile          | 1.63 ms                                                    | 1.61 ms: 1.01x faster                                                       |
| coverage                   | 93.1 ms                                                    | 92.0 ms: 1.01x faster                                                       |
| go                         | 145 ms                                                     | 143 ms: 1.01x faster                                                        |
| 2to3                       | 274 ms                                                     | 272 ms: 1.01x faster                                                        |
| unpickle_pure_python       | 218 us                                                     | 217 us: 1.01x faster                                                        |
| bench_thread_pool          | 834 us                                                     | 830 us: 1.00x faster                                                        |
| regex_dna                  | 221 ms                                                     | 221 ms: 1.00x faster                                                        |
| python_startup_no_site     | 7.11 ms                                                    | 7.12 ms: 1.00x slower                                                       |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                       |
| raytrace                   | 267 ms                                                     | 269 ms: 1.01x slower                                                        |
| generators                 | 29.6 ms                                                    | 30.0 ms: 1.01x slower                                                       |
| logging_silent             | 105 ns                                                     | 106 ns: 1.01x slower                                                        |
| coroutines                 | 23.2 ms                                                    | 23.4 ms: 1.01x slower                                                       |
| comprehensions             | 16.6 us                                                    | 16.8 us: 1.01x slower                                                       |
| docutils                   | 2.83 sec                                                   | 2.87 sec: 1.02x slower                                                      |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                                        |
| scimark_sor                | 127 ms                                                     | 130 ms: 1.02x slower                                                        |
| scimark_lu                 | 122 ms                                                     | 124 ms: 1.02x slower                                                        |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                                      |
| django_template            | 34.8 ms                                                    | 35.6 ms: 1.02x slower                                                       |
| typing_runtime_protocols   | 165 us                                                     | 170 us: 1.03x slower                                                        |
| hexiom                     | 6.30 ms                                                    | 6.50 ms: 1.03x slower                                                       |
| async_generators           | 442 ms                                                     | 459 ms: 1.04x slower                                                        |
| regex_effbot               | 3.67 ms                                                    | 3.81 ms: 1.04x slower                                                       |
| sympy_str                  | 282 ms                                                     | 294 ms: 1.04x slower                                                        |
| sympy_expand               | 473 ms                                                     | 496 ms: 1.05x slower                                                        |
| genshi_text                | 23.7 ms                                                    | 25.0 ms: 1.06x slower                                                       |
| nqueens                    | 81.4 ms                                                    | 86.7 ms: 1.06x slower                                                       |
| sympy_sum                  | 156 ms                                                     | 167 ms: 1.07x slower                                                        |
| sympy_integrate            | 20.5 ms                                                    | 22.1 ms: 1.08x slower                                                       |
| genshi_xml                 | 51.6 ms                                                    | 56.1 ms: 1.09x slower                                                       |
| deltablue                  | 3.25 ms                                                    | 3.56 ms: 1.09x slower                                                       |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                |

Benchmark hidden because not significant (4): sqlglot_optimize, regex_v8, dulwich_log, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x
# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 272 ms: 1.01x faster                                                        |
| docutils       | 2.83 sec                                                   | 2.87 sec: 1.01x slower                                                      |
| html5lib       | 67.2 ms                                                    | 66.0 ms: 1.02x faster                                                       |
| tornado_http   | 94.6 ms                                                    | 93.0 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 372 ms: 1.19x faster                                                        |
| async_tree_none            | 378 ms                                                     | 321 ms: 1.18x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 403 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 295 ms: 1.14x faster                                                        |
| async_tree_io              | 939 ms                                                     | 840 ms: 1.12x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 841 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 539 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                                        |
| Geometric mean             | (ref)                                                      | 1.13x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.3 ms: 1.14x faster                                                       |
| nbody          | 88.3 ms                                                    | 79.2 ms: 1.11x faster                                                       |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                      | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                       |
| regex_compile  | 137 ms                                                     | 135 ms: 1.02x faster                                                        |
| regex_effbot   | 3.67 ms                                                    | 3.73 ms: 1.02x slower                                                       |
| regex_dna      | 221 ms                                                     | 229 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                      | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                      |
| xml_etree_parse      | 162 ms                                                     | 147 ms: 1.10x faster                                                        |
| xml_etree_generate   | 87.4 ms                                                    | 80.6 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                     | 99.1 ms: 1.08x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 57.0 ms: 1.07x faster                                                       |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.04x faster                                                       |
| json_loads           | 28.9 us                                                    | 27.9 us: 1.04x faster                                                       |
| pickle_pure_python   | 305 us                                                     | 297 us: 1.03x faster                                                        |
| unpickle_pure_python | 218 us                                                     | 217 us: 1.00x faster                                                        |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako           | 11.2 ms                                                    | 9.86 ms: 1.14x faster                                                       |
| genshi_text    | 23.7 ms                                                    | 24.6 ms: 1.04x slower                                                       |
| genshi_xml     | 51.6 ms                                                    | 56.3 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                      | 1.00x slower                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.9 us: 1.37x faster                                                       |
| deepcopy                   | 367 us                                                     | 278 us: 1.32x faster                                                        |
| scimark_fft                | 392 ms                                                     | 315 ms: 1.25x faster                                                        |
| richards                   | 50.9 ms                                                    | 41.3 ms: 1.23x faster                                                       |
| richards_super             | 57.4 ms                                                    | 47.6 ms: 1.20x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                    | 2.78 us: 1.20x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 372 ms: 1.19x faster                                                        |
| async_tree_none            | 378 ms                                                     | 321 ms: 1.18x faster                                                        |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.50 ms: 1.17x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 403 ms: 1.15x faster                                                        |
| crypto_pyaes               | 77.5 ms                                                    | 67.5 ms: 1.15x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 295 ms: 1.14x faster                                                        |
| mako                       | 11.2 ms                                                    | 9.86 ms: 1.14x faster                                                       |
| float                      | 78.9 ms                                                    | 69.3 ms: 1.14x faster                                                       |
| pyflate                    | 484 ms                                                     | 426 ms: 1.14x faster                                                        |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.9 ms: 1.14x faster                                                       |
| spectral_norm              | 116 ms                                                     | 103 ms: 1.13x faster                                                        |
| gc_traversal               | 3.98 ms                                                    | 3.55 ms: 1.12x faster                                                       |
| async_tree_io              | 939 ms                                                     | 840 ms: 1.12x faster                                                        |
| nbody                      | 88.3 ms                                                    | 79.2 ms: 1.11x faster                                                       |
| async_tree_io_tg           | 936 ms                                                     | 841 ms: 1.11x faster                                                        |
| fannkuch                   | 402 ms                                                     | 363 ms: 1.11x faster                                                        |
| tomli_loads                | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                      |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                                        |
| bpe_tokeniser              | 5.02 sec                                                   | 4.59 sec: 1.09x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 539 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                                        |
| xml_etree_generate         | 87.4 ms                                                    | 80.6 ms: 1.08x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                     | 99.1 ms: 1.08x faster                                                       |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                       |
| xml_etree_process          | 61.2 ms                                                    | 57.0 ms: 1.07x faster                                                       |
| logging_format             | 6.47 us                                                    | 6.07 us: 1.07x faster                                                       |
| pprint_pformat             | 1.56 sec                                                   | 1.46 sec: 1.06x faster                                                      |
| chaos                      | 61.3 ms                                                    | 58.1 ms: 1.06x faster                                                       |
| pprint_safe_repr           | 758 ms                                                     | 720 ms: 1.05x faster                                                        |
| logging_simple             | 5.74 us                                                    | 5.49 us: 1.05x faster                                                       |
| telco                      | 8.41 ms                                                    | 8.04 ms: 1.05x faster                                                       |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.04x faster                                                        |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                       |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.04x faster                                                       |
| json_loads                 | 28.9 us                                                    | 27.9 us: 1.04x faster                                                       |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                                       |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                        |
| regex_v8                   | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                       |
| json                       | 5.31 ms                                                    | 5.15 ms: 1.03x faster                                                       |
| thrift                     | 823 us                                                     | 800 us: 1.03x faster                                                        |
| pickle_pure_python         | 305 us                                                     | 297 us: 1.03x faster                                                        |
| pycparser                  | 1.16 sec                                                   | 1.13 sec: 1.03x faster                                                      |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                      |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                        |
| html5lib                   | 67.2 ms                                                    | 66.0 ms: 1.02x faster                                                       |
| tornado_http               | 94.6 ms                                                    | 93.0 ms: 1.02x faster                                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.61 ms: 1.02x faster                                                       |
| mdp                        | 2.79 sec                                                   | 2.74 sec: 1.02x faster                                                      |
| regex_compile              | 137 ms                                                     | 135 ms: 1.02x faster                                                        |
| dask                       | 369 ms                                                     | 364 ms: 1.01x faster                                                        |
| asyncio_tcp                | 508 ms                                                     | 502 ms: 1.01x faster                                                        |
| go                         | 145 ms                                                     | 144 ms: 1.01x faster                                                        |
| 2to3                       | 274 ms                                                     | 272 ms: 1.01x faster                                                        |
| unpickle_pure_python       | 218 us                                                     | 217 us: 1.00x faster                                                        |
| sqlglot_optimize           | 55.5 ms                                                    | 55.3 ms: 1.00x faster                                                       |
| python_startup_no_site     | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                       |
| raytrace                   | 267 ms                                                     | 268 ms: 1.00x slower                                                        |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                       |
| scimark_lu                 | 122 ms                                                     | 123 ms: 1.01x slower                                                        |
| docutils                   | 2.83 sec                                                   | 2.87 sec: 1.01x slower                                                      |
| coroutines                 | 23.2 ms                                                    | 23.5 ms: 1.01x slower                                                       |
| logging_silent             | 105 ns                                                     | 106 ns: 1.01x slower                                                        |
| regex_effbot               | 3.67 ms                                                    | 3.73 ms: 1.02x slower                                                       |
| async_generators           | 442 ms                                                     | 449 ms: 1.02x slower                                                        |
| typing_runtime_protocols   | 165 us                                                     | 168 us: 1.02x slower                                                        |
| scimark_sor                | 127 ms                                                     | 130 ms: 1.02x slower                                                        |
| generators                 | 29.6 ms                                                    | 30.4 ms: 1.03x slower                                                       |
| nqueens                    | 81.4 ms                                                    | 84.3 ms: 1.04x slower                                                       |
| regex_dna                  | 221 ms                                                     | 229 ms: 1.04x slower                                                        |
| genshi_text                | 23.7 ms                                                    | 24.6 ms: 1.04x slower                                                       |
| sympy_str                  | 282 ms                                                     | 294 ms: 1.04x slower                                                        |
| hexiom                     | 6.30 ms                                                    | 6.58 ms: 1.04x slower                                                       |
| sympy_expand               | 473 ms                                                     | 497 ms: 1.05x slower                                                        |
| sympy_sum                  | 156 ms                                                     | 167 ms: 1.07x slower                                                        |
| sympy_integrate            | 20.5 ms                                                    | 22.1 ms: 1.08x slower                                                       |
| deltablue                  | 3.25 ms                                                    | 3.54 ms: 1.09x slower                                                       |
| genshi_xml                 | 51.6 ms                                                    | 56.3 ms: 1.09x slower                                                       |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                |

Benchmark hidden because not significant (7): comprehensions, dulwich_log, bench_thread_pool, coverage, django_template, sqlglot_normalize, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x
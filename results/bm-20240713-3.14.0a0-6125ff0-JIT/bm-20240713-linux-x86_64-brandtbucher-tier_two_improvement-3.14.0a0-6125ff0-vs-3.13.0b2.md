# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: 6125ff0
- commit date: 2024-07-13
- overall geometric mean: 1.04x faster
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 275 ms: 1.00x slower                                                        |
| docutils       | 2.83 sec                                                   | 2.89 sec: 1.02x slower                                                      |
| html5lib       | 67.2 ms                                                    | 65.2 ms: 1.03x faster                                                       |
| tornado_http   | 94.6 ms                                                    | 93.3 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 381 ms: 1.17x faster                                                        |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 412 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                        |
| async_tree_io              | 939 ms                                                     | 846 ms: 1.11x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 851 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 541 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                                        |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.2 ms: 1.12x faster                                                       |
| nbody          | 88.3 ms                                                    | 79.9 ms: 1.10x faster                                                       |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                      | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 219 ms: 1.01x faster                                                        |
| regex_compile  | 137 ms                                                     | 136 ms: 1.01x faster                                                        |
| regex_v8       | 25.1 ms                                                    | 25.7 ms: 1.02x slower                                                       |
| regex_effbot   | 3.67 ms                                                    | 3.80 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.09x faster                                                        |
| tomli_loads          | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                     | 99.1 ms: 1.08x faster                                                       |
| xml_etree_generate   | 87.4 ms                                                    | 81.5 ms: 1.07x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 57.0 ms: 1.07x faster                                                       |
| json_loads           | 28.9 us                                                    | 27.9 us: 1.03x faster                                                       |
| pickle_pure_python   | 305 us                                                     | 298 us: 1.03x faster                                                        |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                       |
| unpickle_pure_python | 218 us                                                     | 217 us: 1.00x faster                                                        |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.79 ms: 1.15x faster                                                       |
| django_template | 34.8 ms                                                    | 35.7 ms: 1.03x slower                                                       |
| genshi_text     | 23.7 ms                                                    | 26.2 ms: 1.11x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 59.3 ms: 1.15x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.5 us: 1.39x faster                                                       |
| deepcopy                   | 367 us                                                     | 275 us: 1.34x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                    | 2.72 us: 1.23x faster                                                       |
| scimark_fft                | 392 ms                                                     | 319 ms: 1.23x faster                                                        |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.49 ms: 1.17x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 381 ms: 1.17x faster                                                        |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                        |
| crypto_pyaes               | 77.5 ms                                                    | 66.6 ms: 1.16x faster                                                       |
| richards                   | 50.9 ms                                                    | 43.9 ms: 1.16x faster                                                       |
| mako                       | 11.2 ms                                                    | 9.79 ms: 1.15x faster                                                       |
| richards_super             | 57.4 ms                                                    | 50.2 ms: 1.14x faster                                                       |
| float                      | 78.9 ms                                                    | 70.2 ms: 1.12x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 412 ms: 1.12x faster                                                        |
| scimark_monte_carlo        | 69.2 ms                                                    | 61.6 ms: 1.12x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                        |
| async_tree_io              | 939 ms                                                     | 846 ms: 1.11x faster                                                        |
| spectral_norm              | 116 ms                                                     | 105 ms: 1.10x faster                                                        |
| nbody                      | 88.3 ms                                                    | 79.9 ms: 1.10x faster                                                       |
| async_tree_io_tg           | 936 ms                                                     | 851 ms: 1.10x faster                                                        |
| pyflate                    | 484 ms                                                     | 442 ms: 1.10x faster                                                        |
| fannkuch                   | 402 ms                                                     | 368 ms: 1.09x faster                                                        |
| bpe_tokeniser              | 5.02 sec                                                   | 4.60 sec: 1.09x faster                                                      |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.09x faster                                                        |
| tomli_loads                | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 541 ms: 1.09x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                     | 99.1 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                                        |
| pprint_safe_repr           | 758 ms                                                     | 701 ms: 1.08x faster                                                        |
| pprint_pformat             | 1.56 sec                                                   | 1.45 sec: 1.07x faster                                                      |
| xml_etree_generate         | 87.4 ms                                                    | 81.5 ms: 1.07x faster                                                       |
| xml_etree_process          | 61.2 ms                                                    | 57.0 ms: 1.07x faster                                                       |
| gc_traversal               | 3.98 ms                                                    | 3.73 ms: 1.07x faster                                                       |
| logging_format             | 6.47 us                                                    | 6.12 us: 1.06x faster                                                       |
| pathlib                    | 17.3 ms                                                    | 16.4 ms: 1.06x faster                                                       |
| telco                      | 8.41 ms                                                    | 8.01 ms: 1.05x faster                                                       |
| chaos                      | 61.3 ms                                                    | 58.6 ms: 1.05x faster                                                       |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.04x faster                                                        |
| mdp                        | 2.79 sec                                                   | 2.68 sec: 1.04x faster                                                      |
| json                       | 5.31 ms                                                    | 5.12 ms: 1.04x faster                                                       |
| json_loads                 | 28.9 us                                                    | 27.9 us: 1.03x faster                                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                       |
| logging_simple             | 5.74 us                                                    | 5.56 us: 1.03x faster                                                       |
| html5lib                   | 67.2 ms                                                    | 65.2 ms: 1.03x faster                                                       |
| thrift                     | 823 us                                                     | 799 us: 1.03x faster                                                        |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                        |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.03x faster                                                       |
| pickle_pure_python         | 305 us                                                     | 298 us: 1.03x faster                                                        |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                       |
| asyncio_websockets         | 567 ms                                                     | 554 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                      |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                       |
| dask                       | 369 ms                                                     | 363 ms: 1.02x faster                                                        |
| tornado_http               | 94.6 ms                                                    | 93.3 ms: 1.01x faster                                                       |
| asyncio_tcp                | 508 ms                                                     | 503 ms: 1.01x faster                                                        |
| regex_dna                  | 221 ms                                                     | 219 ms: 1.01x faster                                                        |
| regex_compile              | 137 ms                                                     | 136 ms: 1.01x faster                                                        |
| sqlglot_transpile          | 1.63 ms                                                    | 1.62 ms: 1.01x faster                                                       |
| unpickle_pure_python       | 218 us                                                     | 217 us: 1.00x faster                                                        |
| 2to3                       | 274 ms                                                     | 275 ms: 1.00x slower                                                        |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.00x slower                                                       |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                       |
| dulwich_log                | 67.2 ms                                                    | 67.5 ms: 1.01x slower                                                       |
| coroutines                 | 23.2 ms                                                    | 23.4 ms: 1.01x slower                                                       |
| scimark_sor                | 127 ms                                                     | 129 ms: 1.01x slower                                                        |
| go                         | 145 ms                                                     | 147 ms: 1.01x slower                                                        |
| sqlglot_optimize           | 55.5 ms                                                    | 56.3 ms: 1.01x slower                                                       |
| raytrace                   | 267 ms                                                     | 271 ms: 1.02x slower                                                        |
| logging_silent             | 105 ns                                                     | 107 ns: 1.02x slower                                                        |
| docutils                   | 2.83 sec                                                   | 2.89 sec: 1.02x slower                                                      |
| regex_v8                   | 25.1 ms                                                    | 25.7 ms: 1.02x slower                                                       |
| django_template            | 34.8 ms                                                    | 35.7 ms: 1.03x slower                                                       |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.03x slower                                                      |
| regex_effbot               | 3.67 ms                                                    | 3.80 ms: 1.04x slower                                                       |
| async_generators           | 442 ms                                                     | 459 ms: 1.04x slower                                                        |
| hexiom                     | 6.30 ms                                                    | 6.55 ms: 1.04x slower                                                       |
| typing_runtime_protocols   | 165 us                                                     | 172 us: 1.04x slower                                                        |
| sqlglot_normalize          | 110 ms                                                     | 115 ms: 1.04x slower                                                        |
| scimark_lu                 | 122 ms                                                     | 127 ms: 1.04x slower                                                        |
| sympy_str                  | 282 ms                                                     | 296 ms: 1.05x slower                                                        |
| nqueens                    | 81.4 ms                                                    | 85.7 ms: 1.05x slower                                                       |
| sympy_expand               | 473 ms                                                     | 502 ms: 1.06x slower                                                        |
| sympy_sum                  | 156 ms                                                     | 168 ms: 1.08x slower                                                        |
| pylint                     | 317 ms                                                     | 342 ms: 1.08x slower                                                        |
| sympy_integrate            | 20.5 ms                                                    | 22.4 ms: 1.09x slower                                                       |
| deltablue                  | 3.25 ms                                                    | 3.59 ms: 1.10x slower                                                       |
| genshi_text                | 23.7 ms                                                    | 26.2 ms: 1.11x slower                                                       |
| genshi_xml                 | 51.6 ms                                                    | 59.3 ms: 1.15x slower                                                       |
| generators                 | 29.6 ms                                                    | 38.6 ms: 1.30x slower                                                       |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                                |

Benchmark hidden because not significant (3): bench_thread_pool, coverage, python_startup_no_site
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.83% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x
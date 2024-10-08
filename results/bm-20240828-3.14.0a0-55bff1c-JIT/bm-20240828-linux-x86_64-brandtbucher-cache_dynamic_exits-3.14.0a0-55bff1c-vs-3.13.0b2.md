# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: cache_dynamic_exits
- machine: linux-x86_64
- commit hash: 55bff1c
- commit date: 2024-08-28
- overall geometric mean: 1.04x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 2.83 sec                                                   | 3.05 sec: 1.08x slower                                                     |
| html5lib       | 67.2 ms                                                    | 66.8 ms: 1.01x faster                                                      |
| tornado_http   | 94.6 ms                                                    | 94.3 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                      | 1.02x slower                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 322 ms: 1.17x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 398 ms: 1.16x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 403 ms: 1.10x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.10x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 542 ms: 1.08x faster                                                       |
| async_tree_io_tg           | 936 ms                                                     | 897 ms: 1.04x faster                                                       |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                               |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.5 ms: 1.12x faster                                                      |
| nbody          | 88.3 ms                                                    | 79.7 ms: 1.11x faster                                                      |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                      | 1.09x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                      |
| regex_effbot   | 3.67 ms                                                    | 3.56 ms: 1.03x faster                                                      |
| regex_dna      | 221 ms                                                     | 217 ms: 1.02x faster                                                       |
| regex_compile  | 137 ms                                                     | 143 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                      | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 76.6 ms: 1.14x faster                                                      |
| xml_etree_process    | 61.2 ms                                                    | 54.2 ms: 1.13x faster                                                      |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                       |
| tomli_loads          | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                     | 98.3 ms: 1.09x faster                                                      |
| json_dumps           | 10.7 ms                                                    | 9.99 ms: 1.07x faster                                                      |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.01x faster                                                       |
| json_loads           | 28.9 us                                                    | 28.6 us: 1.01x faster                                                      |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                               |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                      |
| python_startup_no_site | 7.11 ms                                                    | 7.14 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.87 ms: 1.14x faster                                                      |
| django_template | 34.8 ms                                                    | 37.7 ms: 1.08x slower                                                      |
| genshi_xml      | 51.6 ms                                                    | 56.4 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.1 us: 1.47x faster                                                      |
| deepcopy                   | 367 us                                                     | 269 us: 1.36x faster                                                       |
| richards                   | 50.9 ms                                                    | 39.6 ms: 1.28x faster                                                      |
| richards_super             | 57.4 ms                                                    | 45.4 ms: 1.26x faster                                                      |
| scimark_fft                | 392 ms                                                     | 311 ms: 1.26x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                    | 2.69 us: 1.24x faster                                                      |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.44 ms: 1.19x faster                                                      |
| crypto_pyaes               | 77.5 ms                                                    | 65.9 ms: 1.17x faster                                                      |
| async_tree_none            | 378 ms                                                     | 322 ms: 1.17x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 398 ms: 1.16x faster                                                       |
| spectral_norm              | 116 ms                                                     | 101 ms: 1.15x faster                                                       |
| xml_etree_generate         | 87.4 ms                                                    | 76.6 ms: 1.14x faster                                                      |
| mako                       | 11.2 ms                                                    | 9.87 ms: 1.14x faster                                                      |
| bpe_tokeniser              | 5.02 sec                                                   | 4.43 sec: 1.13x faster                                                     |
| xml_etree_process          | 61.2 ms                                                    | 54.2 ms: 1.13x faster                                                      |
| float                      | 78.9 ms                                                    | 70.5 ms: 1.12x faster                                                      |
| nbody                      | 88.3 ms                                                    | 79.7 ms: 1.11x faster                                                      |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                       |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.6 ms: 1.10x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 403 ms: 1.10x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.10x faster                                                       |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                                     |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.10x faster                                                      |
| tomli_loads                | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                     | 98.3 ms: 1.09x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                                       |
| pyflate                    | 484 ms                                                     | 445 ms: 1.09x faster                                                       |
| fannkuch                   | 402 ms                                                     | 370 ms: 1.09x faster                                                       |
| telco                      | 8.41 ms                                                    | 7.75 ms: 1.09x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 542 ms: 1.08x faster                                                       |
| coverage                   | 93.1 ms                                                    | 86.2 ms: 1.08x faster                                                      |
| json_dumps                 | 10.7 ms                                                    | 9.99 ms: 1.07x faster                                                      |
| scimark_lu                 | 122 ms                                                     | 114 ms: 1.07x faster                                                       |
| logging_format             | 6.47 us                                                    | 6.06 us: 1.07x faster                                                      |
| gc_traversal               | 3.98 ms                                                    | 3.75 ms: 1.06x faster                                                      |
| chaos                      | 61.3 ms                                                    | 58.4 ms: 1.05x faster                                                      |
| logging_simple             | 5.74 us                                                    | 5.49 us: 1.05x faster                                                      |
| thrift                     | 823 us                                                     | 788 us: 1.04x faster                                                       |
| pprint_safe_repr           | 758 ms                                                     | 726 ms: 1.04x faster                                                       |
| async_tree_io_tg           | 936 ms                                                     | 897 ms: 1.04x faster                                                       |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                       |
| pprint_pformat             | 1.56 sec                                                   | 1.50 sec: 1.04x faster                                                     |
| asyncio_tcp                | 508 ms                                                     | 491 ms: 1.03x faster                                                       |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                       |
| coroutines                 | 23.2 ms                                                    | 22.5 ms: 1.03x faster                                                      |
| regex_v8                   | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                      |
| regex_effbot               | 3.67 ms                                                    | 3.56 ms: 1.03x faster                                                      |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                      |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                      |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                     |
| regex_dna                  | 221 ms                                                     | 217 ms: 1.02x faster                                                       |
| bench_thread_pool          | 834 us                                                     | 820 us: 1.02x faster                                                       |
| deltablue                  | 3.25 ms                                                    | 3.20 ms: 1.02x faster                                                      |
| logging_silent             | 105 ns                                                     | 103 ns: 1.01x faster                                                       |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.01x faster                                                       |
| json_loads                 | 28.9 us                                                    | 28.6 us: 1.01x faster                                                      |
| html5lib                   | 67.2 ms                                                    | 66.8 ms: 1.01x faster                                                      |
| tornado_http               | 94.6 ms                                                    | 94.3 ms: 1.00x faster                                                      |
| python_startup_no_site     | 7.11 ms                                                    | 7.14 ms: 1.00x slower                                                      |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.01x slower                                                      |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                      |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.01x slower                                                     |
| sqlglot_parse              | 1.32 ms                                                    | 1.35 ms: 1.02x slower                                                      |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.03x slower                                                       |
| nqueens                    | 81.4 ms                                                    | 83.8 ms: 1.03x slower                                                      |
| async_generators           | 442 ms                                                     | 461 ms: 1.04x slower                                                       |
| regex_compile              | 137 ms                                                     | 143 ms: 1.04x slower                                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 58.0 ms: 1.04x slower                                                      |
| sqlglot_transpile          | 1.63 ms                                                    | 1.71 ms: 1.05x slower                                                      |
| raytrace                   | 267 ms                                                     | 281 ms: 1.05x slower                                                       |
| sympy_str                  | 282 ms                                                     | 299 ms: 1.06x slower                                                       |
| docutils                   | 2.83 sec                                                   | 3.05 sec: 1.08x slower                                                     |
| sympy_sum                  | 156 ms                                                     | 169 ms: 1.08x slower                                                       |
| django_template            | 34.8 ms                                                    | 37.7 ms: 1.08x slower                                                      |
| sympy_expand               | 473 ms                                                     | 514 ms: 1.09x slower                                                       |
| sympy_integrate            | 20.5 ms                                                    | 22.3 ms: 1.09x slower                                                      |
| genshi_xml                 | 51.6 ms                                                    | 56.4 ms: 1.09x slower                                                      |
| hexiom                     | 6.30 ms                                                    | 6.95 ms: 1.10x slower                                                      |
| generators                 | 29.6 ms                                                    | 33.9 ms: 1.14x slower                                                      |
| pylint                     | 317 ms                                                     | 367 ms: 1.16x slower                                                       |
| go                         | 145 ms                                                     | 171 ms: 1.18x slower                                                       |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                               |

Benchmark hidden because not significant (7): async_tree_io, scimark_sor, typing_runtime_protocols, pickle_pure_python, json, 2to3, genshi_text
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.09x
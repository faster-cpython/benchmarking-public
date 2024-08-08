# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: tier_two_constants_i
- machine: linux-x86_64
- commit hash: 8756bc0
- commit date: 2024-08-07
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.83 sec                                                   | 2.90 sec: 1.03x slower                                                      |
| html5lib       | 67.2 ms                                                    | 65.9 ms: 1.02x faster                                                       |
| tornado_http   | 94.6 ms                                                    | 92.6 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                      | 1.00x faster                                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 392 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 528 ms: 1.11x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 418 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 562 ms: 1.09x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 867 ms: 1.08x faster                                                        |
| async_tree_io              | 939 ms                                                     | 904 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 79.0 ms: 1.12x faster                                                       |
| float          | 78.9 ms                                                    | 70.6 ms: 1.12x faster                                                       |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                      | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.58 ms: 1.03x faster                                                       |
| regex_v8       | 25.1 ms                                                    | 24.5 ms: 1.02x faster                                                       |
| regex_compile  | 137 ms                                                     | 134 ms: 1.02x faster                                                        |
| regex_dna      | 221 ms                                                     | 224 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.92 sec: 1.11x faster                                                      |
| xml_etree_parse      | 162 ms                                                     | 147 ms: 1.10x faster                                                        |
| xml_etree_generate   | 87.4 ms                                                    | 79.7 ms: 1.10x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 56.3 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                     | 99.0 ms: 1.08x faster                                                       |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                       |
| pickle_pure_python   | 305 us                                                     | 295 us: 1.03x faster                                                        |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                                        |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.71 ms: 1.16x faster                                                       |
| genshi_text     | 23.7 ms                                                    | 24.0 ms: 1.01x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 53.2 ms: 1.03x slower                                                       |
| django_template | 34.8 ms                                                    | 35.9 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.02x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.8 us: 1.38x faster                                                       |
| deepcopy                   | 367 us                                                     | 271 us: 1.36x faster                                                        |
| scimark_fft                | 392 ms                                                     | 310 ms: 1.27x faster                                                        |
| richards                   | 50.9 ms                                                    | 41.2 ms: 1.23x faster                                                       |
| richards_super             | 57.4 ms                                                    | 47.2 ms: 1.22x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                    | 2.76 us: 1.21x faster                                                       |
| crypto_pyaes               | 77.5 ms                                                    | 66.2 ms: 1.17x faster                                                       |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                        |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.54 ms: 1.16x faster                                                       |
| mako                       | 11.2 ms                                                    | 9.71 ms: 1.16x faster                                                       |
| spectral_norm              | 116 ms                                                     | 102 ms: 1.14x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 392 ms: 1.13x faster                                                        |
| bpe_tokeniser              | 5.02 sec                                                   | 4.45 sec: 1.13x faster                                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 61.4 ms: 1.13x faster                                                       |
| scimark_lu                 | 122 ms                                                     | 108 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                        |
| nbody                      | 88.3 ms                                                    | 79.0 ms: 1.12x faster                                                       |
| float                      | 78.9 ms                                                    | 70.6 ms: 1.12x faster                                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 528 ms: 1.11x faster                                                        |
| pyflate                    | 484 ms                                                     | 435 ms: 1.11x faster                                                        |
| scimark_sor                | 127 ms                                                     | 115 ms: 1.11x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 418 ms: 1.11x faster                                                        |
| tomli_loads                | 2.12 sec                                                   | 1.92 sec: 1.11x faster                                                      |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                                        |
| xml_etree_generate         | 87.4 ms                                                    | 79.7 ms: 1.10x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 562 ms: 1.09x faster                                                        |
| mdp                        | 2.79 sec                                                   | 2.56 sec: 1.09x faster                                                      |
| xml_etree_process          | 61.2 ms                                                    | 56.3 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                     | 99.0 ms: 1.08x faster                                                       |
| fannkuch                   | 402 ms                                                     | 371 ms: 1.08x faster                                                        |
| gc_traversal               | 3.98 ms                                                    | 3.67 ms: 1.08x faster                                                       |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                                       |
| async_tree_io_tg           | 936 ms                                                     | 867 ms: 1.08x faster                                                        |
| telco                      | 8.41 ms                                                    | 7.80 ms: 1.08x faster                                                       |
| chaos                      | 61.3 ms                                                    | 58.1 ms: 1.06x faster                                                       |
| logging_format             | 6.47 us                                                    | 6.13 us: 1.06x faster                                                       |
| thrift                     | 823 us                                                     | 787 us: 1.05x faster                                                        |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.04x faster                                                        |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                       |
| pprint_safe_repr           | 758 ms                                                     | 729 ms: 1.04x faster                                                        |
| async_tree_io              | 939 ms                                                     | 904 ms: 1.04x faster                                                        |
| json                       | 5.31 ms                                                    | 5.12 ms: 1.04x faster                                                       |
| logging_simple             | 5.74 us                                                    | 5.55 us: 1.03x faster                                                       |
| pickle_pure_python         | 305 us                                                     | 295 us: 1.03x faster                                                        |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                       |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                                      |
| regex_effbot               | 3.67 ms                                                    | 3.58 ms: 1.03x faster                                                       |
| pycparser                  | 1.16 sec                                                   | 1.13 sec: 1.03x faster                                                      |
| regex_v8                   | 25.1 ms                                                    | 24.5 ms: 1.02x faster                                                       |
| comprehensions             | 16.6 us                                                    | 16.2 us: 1.02x faster                                                       |
| tornado_http               | 94.6 ms                                                    | 92.6 ms: 1.02x faster                                                       |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                        |
| regex_compile              | 137 ms                                                     | 134 ms: 1.02x faster                                                        |
| html5lib                   | 67.2 ms                                                    | 65.9 ms: 1.02x faster                                                       |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                       |
| bench_thread_pool          | 834 us                                                     | 819 us: 1.02x faster                                                        |
| logging_silent             | 105 ns                                                     | 103 ns: 1.02x faster                                                        |
| asyncio_tcp                | 508 ms                                                     | 499 ms: 1.02x faster                                                        |
| unpickle_pure_python       | 218 us                                                     | 214 us: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.30 ms: 1.02x faster                                                       |
| coverage                   | 93.1 ms                                                    | 92.0 ms: 1.01x faster                                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.62 ms: 1.01x faster                                                       |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                       |
| raytrace                   | 267 ms                                                     | 268 ms: 1.01x slower                                                        |
| python_startup_no_site     | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                                       |
| go                         | 145 ms                                                     | 146 ms: 1.01x slower                                                        |
| regex_dna                  | 221 ms                                                     | 224 ms: 1.01x slower                                                        |
| genshi_text                | 23.7 ms                                                    | 24.0 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.02x slower                                                        |
| docutils                   | 2.83 sec                                                   | 2.90 sec: 1.03x slower                                                      |
| genshi_xml                 | 51.6 ms                                                    | 53.2 ms: 1.03x slower                                                       |
| nqueens                    | 81.4 ms                                                    | 83.9 ms: 1.03x slower                                                       |
| django_template            | 34.8 ms                                                    | 35.9 ms: 1.03x slower                                                       |
| typing_runtime_protocols   | 165 us                                                     | 170 us: 1.03x slower                                                        |
| async_generators           | 442 ms                                                     | 456 ms: 1.03x slower                                                        |
| hexiom                     | 6.30 ms                                                    | 6.66 ms: 1.06x slower                                                       |
| sympy_str                  | 282 ms                                                     | 299 ms: 1.06x slower                                                        |
| sympy_expand               | 473 ms                                                     | 510 ms: 1.08x slower                                                        |
| deltablue                  | 3.25 ms                                                    | 3.54 ms: 1.09x slower                                                       |
| sympy_sum                  | 156 ms                                                     | 170 ms: 1.09x slower                                                        |
| sympy_integrate            | 20.5 ms                                                    | 22.5 ms: 1.10x slower                                                       |
| generators                 | 29.6 ms                                                    | 32.6 ms: 1.10x slower                                                       |
| pylint                     | 317 ms                                                     | 355 ms: 1.12x slower                                                        |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                |

Benchmark hidden because not significant (4): coroutines, json_loads, 2to3, sqlglot_optimize
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x
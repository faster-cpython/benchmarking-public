# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: 6f4aaba
- commit date: 2024-07-15
- overall geometric mean: 1.04x faster
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 272 ms: 1.01x faster                                                        |
| docutils       | 2.83 sec                                                   | 2.88 sec: 1.02x slower                                                      |
| html5lib       | 67.2 ms                                                    | 63.2 ms: 1.06x faster                                                       |
| tornado_http   | 94.6 ms                                                    | 93.5 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 378 ms: 1.18x faster                                                        |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 408 ms: 1.13x faster                                                        |
| async_tree_io              | 939 ms                                                     | 845 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 303 ms: 1.11x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 849 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 545 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 571 ms: 1.07x faster                                                        |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.4 ms: 1.12x faster                                                       |
| nbody          | 88.3 ms                                                    | 81.2 ms: 1.09x faster                                                       |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                      | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 134 ms: 1.02x faster                                                        |
| regex_v8       | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                                       |
| regex_effbot   | 3.67 ms                                                    | 3.81 ms: 1.04x slower                                                       |
| regex_dna      | 221 ms                                                     | 229 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                      | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                      |
| xml_etree_parse      | 162 ms                                                     | 147 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                     | 98.9 ms: 1.09x faster                                                       |
| xml_etree_generate   | 87.4 ms                                                    | 81.0 ms: 1.08x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 56.9 ms: 1.08x faster                                                       |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                       |
| json_loads           | 28.9 us                                                    | 27.9 us: 1.04x faster                                                       |
| pickle_pure_python   | 305 us                                                     | 298 us: 1.03x faster                                                        |
| unpickle_pure_python | 218 us                                                     | 226 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.13 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.74 ms: 1.15x faster                                                       |
| django_template | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                       |
| genshi_text     | 23.7 ms                                                    | 25.8 ms: 1.09x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 57.4 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.8 us: 1.38x faster                                                       |
| deepcopy                   | 367 us                                                     | 274 us: 1.34x faster                                                        |
| scimark_fft                | 392 ms                                                     | 310 ms: 1.27x faster                                                        |
| richards                   | 50.9 ms                                                    | 41.1 ms: 1.24x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                    | 2.75 us: 1.22x faster                                                       |
| richards_super             | 57.4 ms                                                    | 47.3 ms: 1.21x faster                                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.44 ms: 1.19x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 378 ms: 1.18x faster                                                        |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                        |
| crypto_pyaes               | 77.5 ms                                                    | 67.0 ms: 1.16x faster                                                       |
| mako                       | 11.2 ms                                                    | 9.74 ms: 1.15x faster                                                       |
| spectral_norm              | 116 ms                                                     | 101 ms: 1.15x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 408 ms: 1.13x faster                                                        |
| scimark_monte_carlo        | 69.2 ms                                                    | 61.3 ms: 1.13x faster                                                       |
| float                      | 78.9 ms                                                    | 70.4 ms: 1.12x faster                                                       |
| pyflate                    | 484 ms                                                     | 433 ms: 1.12x faster                                                        |
| tomli_loads                | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                      |
| async_tree_io              | 939 ms                                                     | 845 ms: 1.11x faster                                                        |
| gc_traversal               | 3.98 ms                                                    | 3.58 ms: 1.11x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 303 ms: 1.11x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 849 ms: 1.10x faster                                                        |
| mdp                        | 2.79 sec                                                   | 2.53 sec: 1.10x faster                                                      |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                                        |
| fannkuch                   | 402 ms                                                     | 367 ms: 1.10x faster                                                        |
| pprint_safe_repr           | 758 ms                                                     | 694 ms: 1.09x faster                                                        |
| bpe_tokeniser              | 5.02 sec                                                   | 4.60 sec: 1.09x faster                                                      |
| nbody                      | 88.3 ms                                                    | 81.2 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                     | 98.9 ms: 1.09x faster                                                       |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                                       |
| xml_etree_generate         | 87.4 ms                                                    | 81.0 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 545 ms: 1.08x faster                                                        |
| xml_etree_process          | 61.2 ms                                                    | 56.9 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 571 ms: 1.07x faster                                                        |
| html5lib                   | 67.2 ms                                                    | 63.2 ms: 1.06x faster                                                       |
| pprint_pformat             | 1.56 sec                                                   | 1.46 sec: 1.06x faster                                                      |
| telco                      | 8.41 ms                                                    | 7.96 ms: 1.06x faster                                                       |
| chaos                      | 61.3 ms                                                    | 58.3 ms: 1.05x faster                                                       |
| logging_format             | 6.47 us                                                    | 6.15 us: 1.05x faster                                                       |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                       |
| coroutines                 | 23.2 ms                                                    | 22.2 ms: 1.04x faster                                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.04x faster                                                       |
| logging_simple             | 5.74 us                                                    | 5.53 us: 1.04x faster                                                       |
| json_loads                 | 28.9 us                                                    | 27.9 us: 1.04x faster                                                       |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                                        |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                                       |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                        |
| pickle_pure_python         | 305 us                                                     | 298 us: 1.03x faster                                                        |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                       |
| json                       | 5.31 ms                                                    | 5.21 ms: 1.02x faster                                                       |
| thrift                     | 823 us                                                     | 808 us: 1.02x faster                                                        |
| sqlglot_transpile          | 1.63 ms                                                    | 1.61 ms: 1.02x faster                                                       |
| regex_compile              | 137 ms                                                     | 134 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                      |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                        |
| dask                       | 369 ms                                                     | 364 ms: 1.01x faster                                                        |
| tornado_http               | 94.6 ms                                                    | 93.5 ms: 1.01x faster                                                       |
| 2to3                       | 274 ms                                                     | 272 ms: 1.01x faster                                                        |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                       |
| python_startup_no_site     | 7.11 ms                                                    | 7.13 ms: 1.00x slower                                                       |
| dulwich_log                | 67.2 ms                                                    | 67.5 ms: 1.01x slower                                                       |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 56.0 ms: 1.01x slower                                                       |
| go                         | 145 ms                                                     | 146 ms: 1.01x slower                                                        |
| generators                 | 29.6 ms                                                    | 29.9 ms: 1.01x slower                                                       |
| raytrace                   | 267 ms                                                     | 269 ms: 1.01x slower                                                        |
| regex_v8                   | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                                       |
| coverage                   | 93.1 ms                                                    | 94.5 ms: 1.02x slower                                                       |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                                      |
| docutils                   | 2.83 sec                                                   | 2.88 sec: 1.02x slower                                                      |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.02x slower                                                        |
| async_generators           | 442 ms                                                     | 455 ms: 1.03x slower                                                        |
| django_template            | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                       |
| logging_silent             | 105 ns                                                     | 108 ns: 1.03x slower                                                        |
| scimark_sor                | 127 ms                                                     | 131 ms: 1.03x slower                                                        |
| regex_effbot               | 3.67 ms                                                    | 3.81 ms: 1.04x slower                                                       |
| unpickle_pure_python       | 218 us                                                     | 226 us: 1.04x slower                                                        |
| regex_dna                  | 221 ms                                                     | 229 ms: 1.04x slower                                                        |
| typing_runtime_protocols   | 165 us                                                     | 172 us: 1.04x slower                                                        |
| scimark_lu                 | 122 ms                                                     | 127 ms: 1.05x slower                                                        |
| hexiom                     | 6.30 ms                                                    | 6.59 ms: 1.05x slower                                                       |
| sympy_str                  | 282 ms                                                     | 298 ms: 1.06x slower                                                        |
| nqueens                    | 81.4 ms                                                    | 86.5 ms: 1.06x slower                                                       |
| sympy_expand               | 473 ms                                                     | 503 ms: 1.06x slower                                                        |
| sympy_sum                  | 156 ms                                                     | 169 ms: 1.08x slower                                                        |
| sympy_integrate            | 20.5 ms                                                    | 22.3 ms: 1.09x slower                                                       |
| genshi_text                | 23.7 ms                                                    | 25.8 ms: 1.09x slower                                                       |
| genshi_xml                 | 51.6 ms                                                    | 57.4 ms: 1.11x slower                                                       |
| deltablue                  | 3.25 ms                                                    | 3.65 ms: 1.12x slower                                                       |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                                |

Benchmark hidden because not significant (3): bench_thread_pool, asyncio_tcp, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.87% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x
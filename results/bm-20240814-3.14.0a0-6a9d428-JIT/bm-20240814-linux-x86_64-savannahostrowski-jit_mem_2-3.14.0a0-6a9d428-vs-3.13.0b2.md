# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: jit_mem_2
- machine: linux-x86_64
- commit hash: 6a9d428
- commit date: 2024-08-14
- overall geometric mean: 1.04x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 282 ms: 1.03x slower                                                  |
| docutils       | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                                |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 330 ms: 1.15x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 397 ms: 1.12x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 305 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 539 ms: 1.09x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 432 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 572 ms: 1.07x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 879 ms: 1.07x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.08x faster                                                          |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.7 ms: 1.10x faster                                                 |
| nbody          | 88.3 ms                                                    | 80.3 ms: 1.10x faster                                                 |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                      | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.3 ms: 1.03x faster                                                 |
| regex_dna      | 221 ms                                                     | 220 ms: 1.00x faster                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.69 ms: 1.01x slower                                                 |
| regex_compile  | 137 ms                                                     | 142 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 147 ms: 1.10x faster                                                  |
| tomli_loads          | 2.12 sec                                                   | 1.94 sec: 1.10x faster                                                |
| xml_etree_iterparse  | 107 ms                                                     | 98.7 ms: 1.09x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 58.7 ms: 1.04x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 211 us: 1.03x faster                                                  |
| xml_etree_generate   | 87.4 ms                                                    | 85.3 ms: 1.03x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 298 us: 1.02x faster                                                  |
| json_loads           | 28.9 us                                                    | 28.6 us: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.0 ms: 1.12x faster                                                 |
| genshi_text     | 23.7 ms                                                    | 24.6 ms: 1.04x slower                                                 |
| django_template | 34.8 ms                                                    | 36.8 ms: 1.06x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 56.3 ms: 1.09x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.0 us: 1.47x faster                                                 |
| deepcopy                   | 367 us                                                     | 263 us: 1.39x faster                                                  |
| scimark_fft                | 392 ms                                                     | 305 ms: 1.29x faster                                                  |
| richards_super             | 57.4 ms                                                    | 46.1 ms: 1.25x faster                                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.24 ms: 1.24x faster                                                 |
| richards                   | 50.9 ms                                                    | 41.1 ms: 1.24x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.70 us: 1.24x faster                                                 |
| spectral_norm              | 116 ms                                                     | 99.2 ms: 1.17x faster                                                 |
| async_tree_none            | 378 ms                                                     | 330 ms: 1.15x faster                                                  |
| gc_traversal               | 3.98 ms                                                    | 3.51 ms: 1.13x faster                                                 |
| crypto_pyaes               | 77.5 ms                                                    | 68.6 ms: 1.13x faster                                                 |
| mako                       | 11.2 ms                                                    | 10.0 ms: 1.12x faster                                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 397 ms: 1.12x faster                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.1 ms: 1.11x faster                                                 |
| scimark_lu                 | 122 ms                                                     | 110 ms: 1.10x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 305 ms: 1.10x faster                                                  |
| float                      | 78.9 ms                                                    | 71.7 ms: 1.10x faster                                                 |
| nbody                      | 88.3 ms                                                    | 80.3 ms: 1.10x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 1.94 sec: 1.10x faster                                                |
| coverage                   | 93.1 ms                                                    | 85.0 ms: 1.09x faster                                                 |
| mdp                        | 2.79 sec                                                   | 2.55 sec: 1.09x faster                                                |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 539 ms: 1.09x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 98.7 ms: 1.09x faster                                                 |
| fannkuch                   | 402 ms                                                     | 371 ms: 1.08x faster                                                  |
| scimark_sor                | 127 ms                                                     | 118 ms: 1.08x faster                                                  |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                 |
| pyflate                    | 484 ms                                                     | 451 ms: 1.07x faster                                                  |
| telco                      | 8.41 ms                                                    | 7.84 ms: 1.07x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 432 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 572 ms: 1.07x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 879 ms: 1.07x faster                                                  |
| chaos                      | 61.3 ms                                                    | 57.9 ms: 1.06x faster                                                 |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                                 |
| deltablue                  | 3.25 ms                                                    | 3.11 ms: 1.05x faster                                                 |
| thrift                     | 823 us                                                     | 788 us: 1.04x faster                                                  |
| logging_format             | 6.47 us                                                    | 6.21 us: 1.04x faster                                                 |
| xml_etree_process          | 61.2 ms                                                    | 58.7 ms: 1.04x faster                                                 |
| pprint_safe_repr           | 758 ms                                                     | 729 ms: 1.04x faster                                                  |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                  |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| unpickle_pure_python       | 218 us                                                     | 211 us: 1.03x faster                                                  |
| regex_v8                   | 25.1 ms                                                    | 24.3 ms: 1.03x faster                                                 |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                  |
| asyncio_tcp                | 508 ms                                                     | 493 ms: 1.03x faster                                                  |
| python_startup             | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                                |
| xml_etree_generate         | 87.4 ms                                                    | 85.3 ms: 1.03x faster                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.03x faster                                                |
| pickle_pure_python         | 305 us                                                     | 298 us: 1.02x faster                                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.90 sec: 1.02x faster                                                |
| logging_simple             | 5.74 us                                                    | 5.62 us: 1.02x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                  |
| logging_silent             | 105 ns                                                     | 103 ns: 1.02x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 821 us: 1.02x faster                                                  |
| coroutines                 | 23.2 ms                                                    | 22.9 ms: 1.01x faster                                                 |
| json_loads                 | 28.9 us                                                    | 28.6 us: 1.01x faster                                                 |
| raytrace                   | 267 ms                                                     | 264 ms: 1.01x faster                                                  |
| regex_dna                  | 221 ms                                                     | 220 ms: 1.00x faster                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| regex_effbot               | 3.67 ms                                                    | 3.69 ms: 1.01x slower                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.33 ms: 1.01x slower                                                 |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.02x slower                                                  |
| 2to3                       | 274 ms                                                     | 282 ms: 1.03x slower                                                  |
| typing_runtime_protocols   | 165 us                                                     | 170 us: 1.03x slower                                                  |
| async_generators           | 442 ms                                                     | 457 ms: 1.03x slower                                                  |
| pycparser                  | 1.16 sec                                                   | 1.20 sec: 1.04x slower                                                |
| sqlglot_transpile          | 1.63 ms                                                    | 1.70 ms: 1.04x slower                                                 |
| regex_compile              | 137 ms                                                     | 142 ms: 1.04x slower                                                  |
| genshi_text                | 23.7 ms                                                    | 24.6 ms: 1.04x slower                                                 |
| docutils                   | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                                |
| sympy_str                  | 282 ms                                                     | 296 ms: 1.05x slower                                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 58.5 ms: 1.05x slower                                                 |
| django_template            | 34.8 ms                                                    | 36.8 ms: 1.06x slower                                                 |
| sympy_expand               | 473 ms                                                     | 501 ms: 1.06x slower                                                  |
| nqueens                    | 81.4 ms                                                    | 87.7 ms: 1.08x slower                                                 |
| hexiom                     | 6.30 ms                                                    | 6.86 ms: 1.09x slower                                                 |
| genshi_xml                 | 51.6 ms                                                    | 56.3 ms: 1.09x slower                                                 |
| sympy_sum                  | 156 ms                                                     | 171 ms: 1.10x slower                                                  |
| sympy_integrate            | 20.5 ms                                                    | 22.7 ms: 1.11x slower                                                 |
| pylint                     | 317 ms                                                     | 365 ms: 1.15x slower                                                  |
| generators                 | 29.6 ms                                                    | 34.6 ms: 1.17x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                          |

Benchmark hidden because not significant (6): async_tree_io, html5lib, tornado_http, comprehensions, go, json
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x
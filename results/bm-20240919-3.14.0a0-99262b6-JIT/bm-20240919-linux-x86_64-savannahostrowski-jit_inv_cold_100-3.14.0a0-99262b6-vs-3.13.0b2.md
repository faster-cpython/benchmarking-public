# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: jit_inv_cold_100
- machine: linux-x86_64
- commit hash: 99262b6
- commit date: 2024-09-19
- overall geometric mean: 1.02x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 318 ms: 1.16x slower                                                         |
| docutils       | 2.83 sec                                                   | 2.70 sec: 1.05x faster                                                       |
| html5lib       | 67.2 ms                                                    | 63.2 ms: 1.06x faster                                                        |
| tornado_http   | 94.6 ms                                                    | 110 ms: 1.16x slower                                                         |
| Geometric mean | (ref)                                                      | 1.05x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 322 ms: 1.18x faster                                                         |
| async_tree_memoization     | 463 ms                                                     | 403 ms: 1.15x faster                                                         |
| async_tree_memoization_tg  | 444 ms                                                     | 390 ms: 1.14x faster                                                         |
| async_tree_none_tg         | 336 ms                                                     | 306 ms: 1.10x faster                                                         |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 570 ms: 1.07x faster                                                         |
| async_tree_io_tg           | 936 ms                                                     | 875 ms: 1.07x faster                                                         |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 554 ms: 1.06x faster                                                         |
| async_tree_io              | 939 ms                                                     | 892 ms: 1.05x faster                                                         |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.3 ms: 1.11x faster                                                        |
| nbody          | 88.3 ms                                                    | 85.5 ms: 1.03x faster                                                        |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                      | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 130 ms: 1.05x faster                                                         |
| regex_dna      | 221 ms                                                     | 215 ms: 1.03x faster                                                         |
| regex_effbot   | 3.67 ms                                                    | 3.62 ms: 1.01x faster                                                        |
| regex_v8       | 25.1 ms                                                    | 26.4 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                     | 99.7 ms: 1.08x faster                                                        |
| json_loads           | 28.9 us                                                    | 26.8 us: 1.08x faster                                                        |
| json_dumps           | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                        |
| unpickle             | 15.1 us                                                    | 14.5 us: 1.04x faster                                                        |
| xml_etree_process    | 61.2 ms                                                    | 59.3 ms: 1.03x faster                                                        |
| xml_etree_generate   | 87.4 ms                                                    | 85.6 ms: 1.02x faster                                                        |
| unpickle_list        | 5.34 us                                                    | 5.26 us: 1.02x faster                                                        |
| unpickle_pure_python | 218 us                                                     | 220 us: 1.01x slower                                                         |
| pickle_list          | 5.11 us                                                    | 5.17 us: 1.01x slower                                                        |
| pickle_dict          | 34.8 us                                                    | 35.4 us: 1.02x slower                                                        |
| pickle               | 11.5 us                                                    | 11.8 us: 1.02x slower                                                        |
| pickle_pure_python   | 305 us                                                     | 331 us: 1.08x slower                                                         |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                        |
| python_startup_no_site | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                                        |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.1 ms: 1.11x faster                                                        |
| genshi_text     | 23.7 ms                                                    | 24.3 ms: 1.03x slower                                                        |
| django_template | 34.8 ms                                                    | 38.4 ms: 1.10x slower                                                        |
| genshi_xml      | 51.6 ms                                                    | 57.8 ms: 1.12x slower                                                        |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.5 us: 1.45x faster                                                        |
| deepcopy                   | 367 us                                                     | 270 us: 1.36x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                    | 2.64 us: 1.27x faster                                                        |
| go                         | 145 ms                                                     | 122 ms: 1.18x faster                                                         |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.47 ms: 1.18x faster                                                        |
| async_tree_none            | 378 ms                                                     | 322 ms: 1.18x faster                                                         |
| async_tree_memoization     | 463 ms                                                     | 403 ms: 1.15x faster                                                         |
| crypto_pyaes               | 77.5 ms                                                    | 67.5 ms: 1.15x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 390 ms: 1.14x faster                                                         |
| mako                       | 11.2 ms                                                    | 10.1 ms: 1.11x faster                                                        |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                         |
| float                      | 78.9 ms                                                    | 71.3 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 306 ms: 1.10x faster                                                         |
| coverage                   | 93.1 ms                                                    | 84.9 ms: 1.10x faster                                                        |
| sqlite_synth               | 2.99 us                                                    | 2.75 us: 1.09x faster                                                        |
| scimark_sor                | 127 ms                                                     | 118 ms: 1.08x faster                                                         |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.08x faster                                                         |
| richards_super             | 57.4 ms                                                    | 53.2 ms: 1.08x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                     | 99.7 ms: 1.08x faster                                                        |
| json_loads                 | 28.9 us                                                    | 26.8 us: 1.08x faster                                                        |
| json                       | 5.31 ms                                                    | 4.94 ms: 1.07x faster                                                        |
| scimark_fft                | 392 ms                                                     | 366 ms: 1.07x faster                                                         |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 570 ms: 1.07x faster                                                         |
| async_tree_io_tg           | 936 ms                                                     | 875 ms: 1.07x faster                                                         |
| html5lib                   | 67.2 ms                                                    | 63.2 ms: 1.06x faster                                                        |
| pathlib                    | 17.3 ms                                                    | 16.3 ms: 1.06x faster                                                        |
| spectral_norm              | 116 ms                                                     | 110 ms: 1.06x faster                                                         |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 554 ms: 1.06x faster                                                         |
| richards                   | 50.9 ms                                                    | 48.2 ms: 1.06x faster                                                        |
| async_tree_io              | 939 ms                                                     | 892 ms: 1.05x faster                                                         |
| regex_compile              | 137 ms                                                     | 130 ms: 1.05x faster                                                         |
| scimark_monte_carlo        | 69.2 ms                                                    | 65.9 ms: 1.05x faster                                                        |
| json_dumps                 | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                        |
| docutils                   | 2.83 sec                                                   | 2.70 sec: 1.05x faster                                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.05x faster                                                        |
| pprint_pformat             | 1.56 sec                                                   | 1.49 sec: 1.05x faster                                                       |
| thrift                     | 823 us                                                     | 788 us: 1.04x faster                                                         |
| unpickle                   | 15.1 us                                                    | 14.5 us: 1.04x faster                                                        |
| telco                      | 8.41 ms                                                    | 8.08 ms: 1.04x faster                                                        |
| pyflate                    | 484 ms                                                     | 466 ms: 1.04x faster                                                         |
| pprint_safe_repr           | 758 ms                                                     | 732 ms: 1.04x faster                                                         |
| logging_format             | 6.47 us                                                    | 6.25 us: 1.03x faster                                                        |
| bpe_tokeniser              | 5.02 sec                                                   | 4.86 sec: 1.03x faster                                                       |
| nbody                      | 88.3 ms                                                    | 85.5 ms: 1.03x faster                                                        |
| fannkuch                   | 402 ms                                                     | 389 ms: 1.03x faster                                                         |
| mdp                        | 2.79 sec                                                   | 2.70 sec: 1.03x faster                                                       |
| xml_etree_process          | 61.2 ms                                                    | 59.3 ms: 1.03x faster                                                        |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                         |
| regex_dna                  | 221 ms                                                     | 215 ms: 1.03x faster                                                         |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                        |
| logging_silent             | 105 ns                                                     | 102 ns: 1.02x faster                                                         |
| asyncio_websockets         | 567 ms                                                     | 554 ms: 1.02x faster                                                         |
| xml_etree_generate         | 87.4 ms                                                    | 85.6 ms: 1.02x faster                                                        |
| unpickle_list              | 5.34 us                                                    | 5.26 us: 1.02x faster                                                        |
| regex_effbot               | 3.67 ms                                                    | 3.62 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.82 sec: 1.01x faster                                                       |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                        |
| python_startup_no_site     | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                                        |
| asyncio_tcp                | 508 ms                                                     | 504 ms: 1.01x faster                                                         |
| gc_traversal               | 3.98 ms                                                    | 3.96 ms: 1.01x faster                                                        |
| sympy_expand               | 473 ms                                                     | 470 ms: 1.00x faster                                                         |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                        |
| sympy_sum                  | 156 ms                                                     | 157 ms: 1.01x slower                                                         |
| unpickle_pure_python       | 218 us                                                     | 220 us: 1.01x slower                                                         |
| typing_runtime_protocols   | 165 us                                                     | 167 us: 1.01x slower                                                         |
| pickle_list                | 5.11 us                                                    | 5.17 us: 1.01x slower                                                        |
| pickle_dict                | 34.8 us                                                    | 35.4 us: 1.02x slower                                                        |
| chaos                      | 61.3 ms                                                    | 62.5 ms: 1.02x slower                                                        |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                                       |
| pickle                     | 11.5 us                                                    | 11.8 us: 1.02x slower                                                        |
| meteor_contest             | 110 ms                                                     | 113 ms: 1.03x slower                                                         |
| async_generators           | 442 ms                                                     | 454 ms: 1.03x slower                                                         |
| genshi_text                | 23.7 ms                                                    | 24.3 ms: 1.03x slower                                                        |
| dulwich_log                | 67.2 ms                                                    | 69.2 ms: 1.03x slower                                                        |
| raytrace                   | 267 ms                                                     | 275 ms: 1.03x slower                                                         |
| regex_v8                   | 25.1 ms                                                    | 26.4 ms: 1.05x slower                                                        |
| sqlglot_normalize          | 110 ms                                                     | 116 ms: 1.05x slower                                                         |
| nqueens                    | 81.4 ms                                                    | 87.5 ms: 1.07x slower                                                        |
| hexiom                     | 6.30 ms                                                    | 6.81 ms: 1.08x slower                                                        |
| sqlglot_optimize           | 55.5 ms                                                    | 60.1 ms: 1.08x slower                                                        |
| pickle_pure_python         | 305 us                                                     | 331 us: 1.08x slower                                                         |
| deltablue                  | 3.25 ms                                                    | 3.58 ms: 1.10x slower                                                        |
| django_template            | 34.8 ms                                                    | 38.4 ms: 1.10x slower                                                        |
| bench_thread_pool          | 834 us                                                     | 928 us: 1.11x slower                                                         |
| genshi_xml                 | 51.6 ms                                                    | 57.8 ms: 1.12x slower                                                        |
| sqlglot_transpile          | 1.63 ms                                                    | 1.83 ms: 1.12x slower                                                        |
| tornado_http               | 94.6 ms                                                    | 110 ms: 1.16x slower                                                         |
| 2to3                       | 274 ms                                                     | 318 ms: 1.16x slower                                                         |
| pylint                     | 317 ms                                                     | 376 ms: 1.18x slower                                                         |
| generators                 | 29.6 ms                                                    | 36.8 ms: 1.24x slower                                                        |
| sympy_integrate            | 20.5 ms                                                    | 28.0 ms: 1.37x slower                                                        |
| Geometric mean             | (ref)                                                      | 1.02x faster                                                                 |

Benchmark hidden because not significant (5): tomli_loads, logging_simple, sqlglot_parse, coroutines, sympy_str
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240919-3.14.0a0-99262b6-JIT/bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6.json: unpack_sequence

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x
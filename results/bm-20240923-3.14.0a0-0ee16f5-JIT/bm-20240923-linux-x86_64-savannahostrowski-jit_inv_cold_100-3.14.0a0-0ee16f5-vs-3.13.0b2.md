# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: jit_inv_cold_100
- machine: linux-x86_64
- commit hash: 0ee16f5
- commit date: 2024-09-23
- overall geometric mean: 1.02x faster
- HPT reliability: 99.37%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 318 ms: 1.16x slower                                                         |
| docutils       | 2.83 sec                                                   | 2.72 sec: 1.04x faster                                                       |
| html5lib       | 67.2 ms                                                    | 65.4 ms: 1.03x faster                                                        |
| tornado_http   | 94.6 ms                                                    | 110 ms: 1.16x slower                                                         |
| Geometric mean | (ref)                                                      | 1.06x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 319 ms: 1.18x faster                                                         |
| async_tree_memoization_tg  | 444 ms                                                     | 390 ms: 1.14x faster                                                         |
| async_tree_memoization     | 463 ms                                                     | 407 ms: 1.14x faster                                                         |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.09x faster                                                         |
| async_tree_io_tg           | 936 ms                                                     | 874 ms: 1.07x faster                                                         |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 574 ms: 1.06x faster                                                         |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 557 ms: 1.05x faster                                                         |
| async_tree_io              | 939 ms                                                     | 892 ms: 1.05x faster                                                         |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.9 ms: 1.11x faster                                                        |
| nbody          | 88.3 ms                                                    | 80.6 ms: 1.10x faster                                                        |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                      | 1.08x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 132 ms: 1.04x faster                                                         |
| regex_effbot   | 3.67 ms                                                    | 3.65 ms: 1.01x faster                                                        |
| regex_v8       | 25.1 ms                                                    | 27.3 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 149 ms: 1.09x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                     | 100.0 ms: 1.07x faster                                                       |
| json_loads           | 28.9 us                                                    | 27.3 us: 1.06x faster                                                        |
| json_dumps           | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                        |
| unpickle_list        | 5.34 us                                                    | 5.25 us: 1.02x faster                                                        |
| unpickle_pure_python | 218 us                                                     | 220 us: 1.01x slower                                                         |
| tomli_loads          | 2.12 sec                                                   | 2.14 sec: 1.01x slower                                                       |
| pickle_dict          | 34.8 us                                                    | 35.2 us: 1.01x slower                                                        |
| xml_etree_generate   | 87.4 ms                                                    | 88.8 ms: 1.02x slower                                                        |
| pickle_pure_python   | 305 us                                                     | 332 us: 1.09x slower                                                         |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                                 |

Benchmark hidden because not significant (4): pickle_list, xml_etree_process, pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.5 ms: 1.07x faster                                                        |
| genshi_text     | 23.7 ms                                                    | 24.5 ms: 1.04x slower                                                        |
| django_template | 34.8 ms                                                    | 37.1 ms: 1.06x slower                                                        |
| genshi_xml      | 51.6 ms                                                    | 58.3 ms: 1.13x slower                                                        |
| Geometric mean  | (ref)                                                      | 1.04x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.8 us: 1.43x faster                                                        |
| deepcopy                   | 367 us                                                     | 272 us: 1.35x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                    | 2.64 us: 1.27x faster                                                        |
| async_tree_none            | 378 ms                                                     | 319 ms: 1.18x faster                                                         |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.45 ms: 1.18x faster                                                        |
| go                         | 145 ms                                                     | 122 ms: 1.18x faster                                                         |
| crypto_pyaes               | 77.5 ms                                                    | 67.7 ms: 1.14x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 390 ms: 1.14x faster                                                         |
| async_tree_memoization     | 463 ms                                                     | 407 ms: 1.14x faster                                                         |
| float                      | 78.9 ms                                                    | 70.9 ms: 1.11x faster                                                        |
| coverage                   | 93.1 ms                                                    | 84.6 ms: 1.10x faster                                                        |
| nbody                      | 88.3 ms                                                    | 80.6 ms: 1.10x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.09x faster                                                         |
| sqlite_synth               | 2.99 us                                                    | 2.74 us: 1.09x faster                                                        |
| scimark_sor                | 127 ms                                                     | 117 ms: 1.09x faster                                                         |
| mdp                        | 2.79 sec                                                   | 2.57 sec: 1.09x faster                                                       |
| xml_etree_parse            | 162 ms                                                     | 149 ms: 1.09x faster                                                         |
| richards_super             | 57.4 ms                                                    | 52.9 ms: 1.08x faster                                                        |
| scimark_fft                | 392 ms                                                     | 365 ms: 1.08x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                     | 100.0 ms: 1.07x faster                                                       |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.07x faster                                                         |
| mako                       | 11.2 ms                                                    | 10.5 ms: 1.07x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 874 ms: 1.07x faster                                                         |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 574 ms: 1.06x faster                                                         |
| richards                   | 50.9 ms                                                    | 47.9 ms: 1.06x faster                                                        |
| pathlib                    | 17.3 ms                                                    | 16.3 ms: 1.06x faster                                                        |
| spectral_norm              | 116 ms                                                     | 110 ms: 1.06x faster                                                         |
| json_loads                 | 28.9 us                                                    | 27.3 us: 1.06x faster                                                        |
| scimark_monte_carlo        | 69.2 ms                                                    | 65.5 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 557 ms: 1.05x faster                                                         |
| async_tree_io              | 939 ms                                                     | 892 ms: 1.05x faster                                                         |
| json_dumps                 | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                        |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                                        |
| json                       | 5.31 ms                                                    | 5.09 ms: 1.04x faster                                                        |
| regex_compile              | 137 ms                                                     | 132 ms: 1.04x faster                                                         |
| telco                      | 8.41 ms                                                    | 8.09 ms: 1.04x faster                                                        |
| docutils                   | 2.83 sec                                                   | 2.72 sec: 1.04x faster                                                       |
| pprint_pformat             | 1.56 sec                                                   | 1.50 sec: 1.04x faster                                                       |
| pprint_safe_repr           | 758 ms                                                     | 732 ms: 1.04x faster                                                         |
| thrift                     | 823 us                                                     | 798 us: 1.03x faster                                                         |
| logging_format             | 6.47 us                                                    | 6.27 us: 1.03x faster                                                        |
| bpe_tokeniser              | 5.02 sec                                                   | 4.88 sec: 1.03x faster                                                       |
| logging_silent             | 105 ns                                                     | 102 ns: 1.03x faster                                                         |
| fannkuch                   | 402 ms                                                     | 390 ms: 1.03x faster                                                         |
| html5lib                   | 67.2 ms                                                    | 65.4 ms: 1.03x faster                                                        |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                                         |
| unpickle_list              | 5.34 us                                                    | 5.25 us: 1.02x faster                                                        |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.82 sec: 1.01x faster                                                       |
| asyncio_websockets         | 567 ms                                                     | 560 ms: 1.01x faster                                                         |
| gc_traversal               | 3.98 ms                                                    | 3.93 ms: 1.01x faster                                                        |
| asyncio_tcp                | 508 ms                                                     | 505 ms: 1.01x faster                                                         |
| regex_effbot               | 3.67 ms                                                    | 3.65 ms: 1.01x faster                                                        |
| pyflate                    | 484 ms                                                     | 486 ms: 1.00x slower                                                         |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                        |
| logging_simple             | 5.74 us                                                    | 5.79 us: 1.01x slower                                                        |
| unpickle_pure_python       | 218 us                                                     | 220 us: 1.01x slower                                                         |
| comprehensions             | 16.6 us                                                    | 16.8 us: 1.01x slower                                                        |
| tomli_loads                | 2.12 sec                                                   | 2.14 sec: 1.01x slower                                                       |
| pickle_dict                | 34.8 us                                                    | 35.2 us: 1.01x slower                                                        |
| sympy_str                  | 282 ms                                                     | 287 ms: 1.01x slower                                                         |
| xml_etree_generate         | 87.4 ms                                                    | 88.8 ms: 1.02x slower                                                        |
| sqlglot_parse              | 1.32 ms                                                    | 1.34 ms: 1.02x slower                                                        |
| sympy_sum                  | 156 ms                                                     | 159 ms: 1.02x slower                                                         |
| raytrace                   | 267 ms                                                     | 274 ms: 1.03x slower                                                         |
| dulwich_log                | 67.2 ms                                                    | 69.1 ms: 1.03x slower                                                        |
| meteor_contest             | 110 ms                                                     | 113 ms: 1.03x slower                                                         |
| genshi_text                | 23.7 ms                                                    | 24.5 ms: 1.04x slower                                                        |
| async_generators           | 442 ms                                                     | 460 ms: 1.04x slower                                                         |
| pycparser                  | 1.16 sec                                                   | 1.21 sec: 1.05x slower                                                       |
| sqlglot_normalize          | 110 ms                                                     | 116 ms: 1.05x slower                                                         |
| django_template            | 34.8 ms                                                    | 37.1 ms: 1.06x slower                                                        |
| nqueens                    | 81.4 ms                                                    | 87.1 ms: 1.07x slower                                                        |
| regex_v8                   | 25.1 ms                                                    | 27.3 ms: 1.09x slower                                                        |
| pickle_pure_python         | 305 us                                                     | 332 us: 1.09x slower                                                         |
| sqlglot_optimize           | 55.5 ms                                                    | 60.3 ms: 1.09x slower                                                        |
| hexiom                     | 6.30 ms                                                    | 6.84 ms: 1.09x slower                                                        |
| deltablue                  | 3.25 ms                                                    | 3.58 ms: 1.10x slower                                                        |
| bench_thread_pool          | 834 us                                                     | 932 us: 1.12x slower                                                         |
| genshi_xml                 | 51.6 ms                                                    | 58.3 ms: 1.13x slower                                                        |
| sqlglot_transpile          | 1.63 ms                                                    | 1.85 ms: 1.13x slower                                                        |
| tornado_http               | 94.6 ms                                                    | 110 ms: 1.16x slower                                                         |
| 2to3                       | 274 ms                                                     | 318 ms: 1.16x slower                                                         |
| pylint                     | 317 ms                                                     | 377 ms: 1.19x slower                                                         |
| generators                 | 29.6 ms                                                    | 35.5 ms: 1.20x slower                                                        |
| sympy_integrate            | 20.5 ms                                                    | 28.1 ms: 1.37x slower                                                        |
| Geometric mean             | (ref)                                                      | 1.02x faster                                                                 |

Benchmark hidden because not significant (10): coroutines, python_startup_no_site, pickle_list, xml_etree_process, regex_dna, sympy_expand, pickle, chaos, typing_runtime_protocols, unpickle
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240923-3.14.0a0-0ee16f5-JIT/bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5.json: unpack_sequence

# HPT report

- Reliability score: 99.37% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x
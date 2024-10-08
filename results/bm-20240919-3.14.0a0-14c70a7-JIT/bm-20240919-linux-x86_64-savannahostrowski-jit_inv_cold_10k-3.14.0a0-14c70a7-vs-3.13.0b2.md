# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: jit_inv_cold_10k
- machine: linux-x86_64
- commit hash: 14c70a7
- commit date: 2024-09-19
- overall geometric mean: 1.03x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 285 ms: 1.04x slower                                                         |
| docutils       | 2.83 sec                                                   | 2.88 sec: 1.02x slower                                                       |
| html5lib       | 67.2 ms                                                    | 63.9 ms: 1.05x faster                                                        |
| tornado_http   | 94.6 ms                                                    | 95.5 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                      | 1.00x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 321 ms: 1.18x faster                                                         |
| async_tree_memoization     | 463 ms                                                     | 395 ms: 1.17x faster                                                         |
| async_tree_memoization_tg  | 444 ms                                                     | 387 ms: 1.15x faster                                                         |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.12x faster                                                         |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 558 ms: 1.10x faster                                                         |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 546 ms: 1.08x faster                                                         |
| async_tree_io_tg           | 936 ms                                                     | 874 ms: 1.07x faster                                                         |
| async_tree_io              | 939 ms                                                     | 883 ms: 1.06x faster                                                         |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 79.7 ms: 1.11x faster                                                        |
| float          | 78.9 ms                                                    | 71.5 ms: 1.10x faster                                                        |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                      | 1.08x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 215 ms: 1.03x faster                                                         |
| regex_effbot   | 3.67 ms                                                    | 3.65 ms: 1.01x faster                                                        |
| regex_compile  | 137 ms                                                     | 139 ms: 1.02x slower                                                         |
| regex_v8       | 25.1 ms                                                    | 25.5 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                      | 1.00x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|---------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse     | 162 ms                                                     | 145 ms: 1.12x faster                                                         |
| xml_etree_process   | 61.2 ms                                                    | 55.5 ms: 1.10x faster                                                        |
| xml_etree_generate  | 87.4 ms                                                    | 79.8 ms: 1.10x faster                                                        |
| tomli_loads         | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                                       |
| xml_etree_iterparse | 107 ms                                                     | 99.4 ms: 1.08x faster                                                        |
| json_loads          | 28.9 us                                                    | 26.8 us: 1.08x faster                                                        |
| json_dumps          | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                                        |
| pickle_dict         | 34.8 us                                                    | 33.4 us: 1.04x faster                                                        |
| unpickle            | 15.1 us                                                    | 14.7 us: 1.03x faster                                                        |
| pickle_list         | 5.11 us                                                    | 5.00 us: 1.02x faster                                                        |
| unpickle_list       | 5.34 us                                                    | 5.31 us: 1.01x faster                                                        |
| pickle              | 11.5 us                                                    | 11.7 us: 1.02x slower                                                        |
| Geometric mean      | (ref)                                                      | 1.05x faster                                                                 |

Benchmark hidden because not significant (2): unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                        |
| python_startup_no_site | 7.11 ms                                                    | 7.04 ms: 1.01x faster                                                        |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.0 ms: 1.12x faster                                                        |
| django_template | 34.8 ms                                                    | 35.4 ms: 1.02x slower                                                        |
| genshi_text     | 23.7 ms                                                    | 25.5 ms: 1.08x slower                                                        |
| genshi_xml      | 51.6 ms                                                    | 61.0 ms: 1.18x slower                                                        |
| Geometric mean  | (ref)                                                      | 1.04x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.1 us: 1.47x faster                                                        |
| deepcopy                   | 367 us                                                     | 265 us: 1.38x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                    | 2.63 us: 1.27x faster                                                        |
| scimark_fft                | 392 ms                                                     | 309 ms: 1.27x faster                                                         |
| richards_super             | 57.4 ms                                                    | 47.0 ms: 1.22x faster                                                        |
| async_tree_none            | 378 ms                                                     | 321 ms: 1.18x faster                                                         |
| async_tree_memoization     | 463 ms                                                     | 395 ms: 1.17x faster                                                         |
| richards                   | 50.9 ms                                                    | 43.5 ms: 1.17x faster                                                        |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.56 ms: 1.16x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 387 ms: 1.15x faster                                                         |
| crypto_pyaes               | 77.5 ms                                                    | 68.2 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.12x faster                                                         |
| mako                       | 11.2 ms                                                    | 10.0 ms: 1.12x faster                                                        |
| xml_etree_parse            | 162 ms                                                     | 145 ms: 1.12x faster                                                         |
| scimark_monte_carlo        | 69.2 ms                                                    | 61.9 ms: 1.12x faster                                                        |
| nbody                      | 88.3 ms                                                    | 79.7 ms: 1.11x faster                                                        |
| xml_etree_process          | 61.2 ms                                                    | 55.5 ms: 1.10x faster                                                        |
| float                      | 78.9 ms                                                    | 71.5 ms: 1.10x faster                                                        |
| xml_etree_generate         | 87.4 ms                                                    | 79.8 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 558 ms: 1.10x faster                                                         |
| coverage                   | 93.1 ms                                                    | 85.3 ms: 1.09x faster                                                        |
| sqlite_synth               | 2.99 us                                                    | 2.74 us: 1.09x faster                                                        |
| scimark_sor                | 127 ms                                                     | 117 ms: 1.09x faster                                                         |
| tomli_loads                | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                     | 99.4 ms: 1.08x faster                                                        |
| json_loads                 | 28.9 us                                                    | 26.8 us: 1.08x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 546 ms: 1.08x faster                                                         |
| gc_traversal               | 3.98 ms                                                    | 3.71 ms: 1.07x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 874 ms: 1.07x faster                                                         |
| pathlib                    | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                                        |
| mdp                        | 2.79 sec                                                   | 2.62 sec: 1.07x faster                                                       |
| async_tree_io              | 939 ms                                                     | 883 ms: 1.06x faster                                                         |
| json_dumps                 | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                                        |
| pyflate                    | 484 ms                                                     | 456 ms: 1.06x faster                                                         |
| scimark_lu                 | 122 ms                                                     | 115 ms: 1.06x faster                                                         |
| json                       | 5.31 ms                                                    | 5.02 ms: 1.06x faster                                                        |
| go                         | 145 ms                                                     | 137 ms: 1.06x faster                                                         |
| create_gc_cycles           | 1.82 ms                                                    | 1.72 ms: 1.05x faster                                                        |
| html5lib                   | 67.2 ms                                                    | 63.9 ms: 1.05x faster                                                        |
| pickle_dict                | 34.8 us                                                    | 33.4 us: 1.04x faster                                                        |
| thrift                     | 823 us                                                     | 790 us: 1.04x faster                                                         |
| fannkuch                   | 402 ms                                                     | 386 ms: 1.04x faster                                                         |
| telco                      | 8.41 ms                                                    | 8.10 ms: 1.04x faster                                                        |
| asyncio_tcp                | 508 ms                                                     | 491 ms: 1.04x faster                                                         |
| unpickle                   | 15.1 us                                                    | 14.7 us: 1.03x faster                                                        |
| logging_format             | 6.47 us                                                    | 6.28 us: 1.03x faster                                                        |
| bpe_tokeniser              | 5.02 sec                                                   | 4.88 sec: 1.03x faster                                                       |
| chaos                      | 61.3 ms                                                    | 59.6 ms: 1.03x faster                                                        |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                         |
| spectral_norm              | 116 ms                                                     | 113 ms: 1.03x faster                                                         |
| regex_dna                  | 221 ms                                                     | 215 ms: 1.03x faster                                                         |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                        |
| pickle_list                | 5.11 us                                                    | 5.00 us: 1.02x faster                                                        |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                                         |
| pprint_safe_repr           | 758 ms                                                     | 742 ms: 1.02x faster                                                         |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                       |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                                         |
| logging_silent             | 105 ns                                                     | 103 ns: 1.02x faster                                                         |
| logging_simple             | 5.74 us                                                    | 5.67 us: 1.01x faster                                                        |
| python_startup_no_site     | 7.11 ms                                                    | 7.04 ms: 1.01x faster                                                        |
| regex_effbot               | 3.67 ms                                                    | 3.65 ms: 1.01x faster                                                        |
| unpickle_list              | 5.34 us                                                    | 5.31 us: 1.01x faster                                                        |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                        |
| bench_thread_pool          | 834 us                                                     | 841 us: 1.01x slower                                                         |
| coroutines                 | 23.2 ms                                                    | 23.4 ms: 1.01x slower                                                        |
| comprehensions             | 16.6 us                                                    | 16.8 us: 1.01x slower                                                        |
| tornado_http               | 94.6 ms                                                    | 95.5 ms: 1.01x slower                                                        |
| docutils                   | 2.83 sec                                                   | 2.88 sec: 1.02x slower                                                       |
| regex_compile              | 137 ms                                                     | 139 ms: 1.02x slower                                                         |
| sqlglot_parse              | 1.32 ms                                                    | 1.34 ms: 1.02x slower                                                        |
| regex_v8                   | 25.1 ms                                                    | 25.5 ms: 1.02x slower                                                        |
| django_template            | 34.8 ms                                                    | 35.4 ms: 1.02x slower                                                        |
| pickle                     | 11.5 us                                                    | 11.7 us: 1.02x slower                                                        |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.03x slower                                                       |
| dulwich_log                | 67.2 ms                                                    | 68.9 ms: 1.03x slower                                                        |
| sqlglot_transpile          | 1.63 ms                                                    | 1.69 ms: 1.03x slower                                                        |
| 2to3                       | 274 ms                                                     | 285 ms: 1.04x slower                                                         |
| async_generators           | 442 ms                                                     | 460 ms: 1.04x slower                                                         |
| sqlglot_normalize          | 110 ms                                                     | 116 ms: 1.06x slower                                                         |
| raytrace                   | 267 ms                                                     | 281 ms: 1.06x slower                                                         |
| sympy_expand               | 473 ms                                                     | 505 ms: 1.07x slower                                                         |
| genshi_text                | 23.7 ms                                                    | 25.5 ms: 1.08x slower                                                        |
| nqueens                    | 81.4 ms                                                    | 88.1 ms: 1.08x slower                                                        |
| sympy_str                  | 282 ms                                                     | 306 ms: 1.08x slower                                                         |
| sympy_sum                  | 156 ms                                                     | 173 ms: 1.11x slower                                                         |
| deltablue                  | 3.25 ms                                                    | 3.68 ms: 1.13x slower                                                        |
| sqlglot_optimize           | 55.5 ms                                                    | 63.7 ms: 1.15x slower                                                        |
| genshi_xml                 | 51.6 ms                                                    | 61.0 ms: 1.18x slower                                                        |
| pylint                     | 317 ms                                                     | 382 ms: 1.21x slower                                                         |
| generators                 | 29.6 ms                                                    | 36.2 ms: 1.22x slower                                                        |
| hexiom                     | 6.30 ms                                                    | 7.89 ms: 1.25x slower                                                        |
| sympy_integrate            | 20.5 ms                                                    | 26.5 ms: 1.29x slower                                                        |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                                 |

Benchmark hidden because not significant (4): typing_runtime_protocols, pprint_pformat, unpickle_pure_python, pickle_pure_python
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240919-3.14.0a0-14c70a7-JIT/bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7.json: unpack_sequence

# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
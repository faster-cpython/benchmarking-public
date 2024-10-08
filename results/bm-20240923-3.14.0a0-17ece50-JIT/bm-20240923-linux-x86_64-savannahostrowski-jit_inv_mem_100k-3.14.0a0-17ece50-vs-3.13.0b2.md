# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: jit_inv_mem_100k
- machine: linux-x86_64
- commit hash: 17ece50
- commit date: 2024-09-23
- overall geometric mean: 1.04x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 280 ms: 1.02x slower                                                         |
| docutils       | 2.83 sec                                                   | 2.93 sec: 1.04x slower                                                       |
| html5lib       | 67.2 ms                                                    | 65.8 ms: 1.02x faster                                                        |
| tornado_http   | 94.6 ms                                                    | 94.9 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 318 ms: 1.19x faster                                                         |
| async_tree_memoization_tg  | 444 ms                                                     | 391 ms: 1.14x faster                                                         |
| async_tree_memoization     | 463 ms                                                     | 409 ms: 1.13x faster                                                         |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.08x faster                                                         |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 574 ms: 1.07x faster                                                         |
| async_tree_io_tg           | 936 ms                                                     | 880 ms: 1.06x faster                                                         |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 552 ms: 1.06x faster                                                         |
| async_tree_io              | 939 ms                                                     | 886 ms: 1.06x faster                                                         |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.1 ms: 1.11x faster                                                        |
| nbody          | 88.3 ms                                                    | 80.6 ms: 1.10x faster                                                        |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                      | 1.08x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.65 ms: 1.01x faster                                                        |
| regex_dna      | 221 ms                                                     | 221 ms: 1.00x faster                                                         |
| regex_v8       | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                                        |
| regex_compile  | 137 ms                                                     | 144 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|---------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate  | 87.4 ms                                                    | 78.2 ms: 1.12x faster                                                        |
| tomli_loads         | 2.12 sec                                                   | 1.92 sec: 1.10x faster                                                       |
| xml_etree_process   | 61.2 ms                                                    | 55.6 ms: 1.10x faster                                                        |
| xml_etree_parse     | 162 ms                                                     | 148 ms: 1.09x faster                                                         |
| xml_etree_iterparse | 107 ms                                                     | 98.8 ms: 1.09x faster                                                        |
| json_dumps          | 10.7 ms                                                    | 10.0 ms: 1.07x faster                                                        |
| json_loads          | 28.9 us                                                    | 27.2 us: 1.06x faster                                                        |
| unpickle_list       | 5.34 us                                                    | 5.15 us: 1.04x faster                                                        |
| pickle_dict         | 34.8 us                                                    | 34.9 us: 1.00x slower                                                        |
| pickle_list         | 5.11 us                                                    | 5.15 us: 1.01x slower                                                        |
| pickle_pure_python  | 305 us                                                     | 308 us: 1.01x slower                                                         |
| pickle              | 11.5 us                                                    | 11.9 us: 1.04x slower                                                        |
| Geometric mean      | (ref)                                                      | 1.04x faster                                                                 |

Benchmark hidden because not significant (2): unpickle, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                        |
| python_startup_no_site | 7.11 ms                                                    | 7.07 ms: 1.01x faster                                                        |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.75 ms: 1.15x faster                                                        |
| django_template | 34.8 ms                                                    | 36.3 ms: 1.04x slower                                                        |
| genshi_text     | 23.7 ms                                                    | 25.4 ms: 1.07x slower                                                        |
| genshi_xml      | 51.6 ms                                                    | 59.2 ms: 1.15x slower                                                        |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.1 us: 1.47x faster                                                        |
| deepcopy                   | 367 us                                                     | 265 us: 1.39x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                    | 2.64 us: 1.27x faster                                                        |
| richards_super             | 57.4 ms                                                    | 46.0 ms: 1.25x faster                                                        |
| richards                   | 50.9 ms                                                    | 40.9 ms: 1.24x faster                                                        |
| scimark_fft                | 392 ms                                                     | 317 ms: 1.24x faster                                                         |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.38 ms: 1.20x faster                                                        |
| async_tree_none            | 378 ms                                                     | 318 ms: 1.19x faster                                                         |
| crypto_pyaes               | 77.5 ms                                                    | 66.7 ms: 1.16x faster                                                        |
| mako                       | 11.2 ms                                                    | 9.75 ms: 1.15x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 391 ms: 1.14x faster                                                         |
| async_tree_memoization     | 463 ms                                                     | 409 ms: 1.13x faster                                                         |
| xml_etree_generate         | 87.4 ms                                                    | 78.2 ms: 1.12x faster                                                        |
| spectral_norm              | 116 ms                                                     | 104 ms: 1.12x faster                                                         |
| bpe_tokeniser              | 5.02 sec                                                   | 4.50 sec: 1.12x faster                                                       |
| float                      | 78.9 ms                                                    | 71.1 ms: 1.11x faster                                                        |
| tomli_loads                | 2.12 sec                                                   | 1.92 sec: 1.10x faster                                                       |
| xml_etree_process          | 61.2 ms                                                    | 55.6 ms: 1.10x faster                                                        |
| scimark_monte_carlo        | 69.2 ms                                                    | 63.0 ms: 1.10x faster                                                        |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                                       |
| go                         | 145 ms                                                     | 132 ms: 1.10x faster                                                         |
| nbody                      | 88.3 ms                                                    | 80.6 ms: 1.10x faster                                                        |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.09x faster                                                         |
| scimark_lu                 | 122 ms                                                     | 111 ms: 1.09x faster                                                         |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                        |
| scimark_sor                | 127 ms                                                     | 117 ms: 1.09x faster                                                         |
| sqlite_synth               | 2.99 us                                                    | 2.75 us: 1.09x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                     | 98.8 ms: 1.09x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.08x faster                                                         |
| gc_traversal               | 3.98 ms                                                    | 3.68 ms: 1.08x faster                                                        |
| json_dumps                 | 10.7 ms                                                    | 10.0 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 574 ms: 1.07x faster                                                         |
| async_tree_io_tg           | 936 ms                                                     | 880 ms: 1.06x faster                                                         |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 552 ms: 1.06x faster                                                         |
| fannkuch                   | 402 ms                                                     | 378 ms: 1.06x faster                                                         |
| json_loads                 | 28.9 us                                                    | 27.2 us: 1.06x faster                                                        |
| async_tree_io              | 939 ms                                                     | 886 ms: 1.06x faster                                                         |
| create_gc_cycles           | 1.82 ms                                                    | 1.72 ms: 1.06x faster                                                        |
| pyflate                    | 484 ms                                                     | 459 ms: 1.06x faster                                                         |
| telco                      | 8.41 ms                                                    | 7.98 ms: 1.05x faster                                                        |
| thrift                     | 823 us                                                     | 786 us: 1.05x faster                                                         |
| coverage                   | 93.1 ms                                                    | 89.3 ms: 1.04x faster                                                        |
| logging_format             | 6.47 us                                                    | 6.22 us: 1.04x faster                                                        |
| json                       | 5.31 ms                                                    | 5.10 ms: 1.04x faster                                                        |
| unpickle_list              | 5.34 us                                                    | 5.15 us: 1.04x faster                                                        |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                         |
| chaos                      | 61.3 ms                                                    | 59.6 ms: 1.03x faster                                                        |
| asyncio_tcp                | 508 ms                                                     | 495 ms: 1.03x faster                                                         |
| html5lib                   | 67.2 ms                                                    | 65.8 ms: 1.02x faster                                                        |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                        |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                                         |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                       |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.01x faster                                                         |
| logging_simple             | 5.74 us                                                    | 5.69 us: 1.01x faster                                                        |
| deltablue                  | 3.25 ms                                                    | 3.22 ms: 1.01x faster                                                        |
| regex_effbot               | 3.67 ms                                                    | 3.65 ms: 1.01x faster                                                        |
| python_startup_no_site     | 7.11 ms                                                    | 7.07 ms: 1.01x faster                                                        |
| regex_dna                  | 221 ms                                                     | 221 ms: 1.00x faster                                                         |
| tornado_http               | 94.6 ms                                                    | 94.9 ms: 1.00x slower                                                        |
| pickle_dict                | 34.8 us                                                    | 34.9 us: 1.00x slower                                                        |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                        |
| bench_thread_pool          | 834 us                                                     | 839 us: 1.01x slower                                                         |
| pickle_list                | 5.11 us                                                    | 5.15 us: 1.01x slower                                                        |
| pickle_pure_python         | 305 us                                                     | 308 us: 1.01x slower                                                         |
| regex_v8                   | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                                        |
| comprehensions             | 16.6 us                                                    | 16.9 us: 1.02x slower                                                        |
| dulwich_log                | 67.2 ms                                                    | 68.5 ms: 1.02x slower                                                        |
| sqlglot_parse              | 1.32 ms                                                    | 1.35 ms: 1.02x slower                                                        |
| 2to3                       | 274 ms                                                     | 280 ms: 1.02x slower                                                         |
| async_generators           | 442 ms                                                     | 457 ms: 1.03x slower                                                         |
| sqlglot_normalize          | 110 ms                                                     | 114 ms: 1.04x slower                                                         |
| docutils                   | 2.83 sec                                                   | 2.93 sec: 1.04x slower                                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.69 ms: 1.04x slower                                                        |
| pickle                     | 11.5 us                                                    | 11.9 us: 1.04x slower                                                        |
| django_template            | 34.8 ms                                                    | 36.3 ms: 1.04x slower                                                        |
| pycparser                  | 1.16 sec                                                   | 1.22 sec: 1.05x slower                                                       |
| raytrace                   | 267 ms                                                     | 281 ms: 1.05x slower                                                         |
| regex_compile              | 137 ms                                                     | 144 ms: 1.06x slower                                                         |
| nqueens                    | 81.4 ms                                                    | 87.1 ms: 1.07x slower                                                        |
| sympy_expand               | 473 ms                                                     | 507 ms: 1.07x slower                                                         |
| genshi_text                | 23.7 ms                                                    | 25.4 ms: 1.07x slower                                                        |
| sympy_str                  | 282 ms                                                     | 305 ms: 1.08x slower                                                         |
| sqlglot_optimize           | 55.5 ms                                                    | 60.7 ms: 1.09x slower                                                        |
| hexiom                     | 6.30 ms                                                    | 7.02 ms: 1.12x slower                                                        |
| sympy_sum                  | 156 ms                                                     | 176 ms: 1.13x slower                                                         |
| sympy_integrate            | 20.5 ms                                                    | 23.1 ms: 1.13x slower                                                        |
| genshi_xml                 | 51.6 ms                                                    | 59.2 ms: 1.15x slower                                                        |
| generators                 | 29.6 ms                                                    | 35.2 ms: 1.19x slower                                                        |
| pylint                     | 317 ms                                                     | 378 ms: 1.19x slower                                                         |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                                 |

Benchmark hidden because not significant (7): unpickle, pprint_safe_repr, logging_silent, typing_runtime_protocols, coroutines, pprint_pformat, unpickle_pure_python
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240923-3.14.0a0-17ece50-JIT/bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50.json: unpack_sequence

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x
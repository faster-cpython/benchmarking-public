# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: jit_inv_mem_1m
- machine: linux-x86_64
- commit hash: 563a4d7
- commit date: 2024-09-19
- overall geometric mean: 1.04x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 277 ms: 1.01x slower                                                       |
| docutils       | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                                     |
| html5lib       | 67.2 ms                                                    | 65.1 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 317 ms: 1.19x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 394 ms: 1.18x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.14x faster                                                       |
| async_tree_io              | 939 ms                                                     | 858 ms: 1.09x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 308 ms: 1.09x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 547 ms: 1.07x faster                                                       |
| async_tree_io_tg           | 936 ms                                                     | 873 ms: 1.07x faster                                                       |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.7 ms: 1.13x faster                                                      |
| nbody          | 88.3 ms                                                    | 81.3 ms: 1.09x faster                                                      |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                      | 1.08x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                                      |
| regex_dna      | 221 ms                                                     | 218 ms: 1.02x faster                                                       |
| regex_effbot   | 3.67 ms                                                    | 3.76 ms: 1.02x slower                                                      |
| regex_compile  | 137 ms                                                     | 144 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                      | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 144 ms: 1.12x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 54.5 ms: 1.12x faster                                                      |
| xml_etree_generate   | 87.4 ms                                                    | 78.0 ms: 1.12x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                     | 98.8 ms: 1.09x faster                                                      |
| tomli_loads          | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                     |
| json_dumps           | 10.7 ms                                                    | 9.88 ms: 1.09x faster                                                      |
| json_loads           | 28.9 us                                                    | 26.9 us: 1.08x faster                                                      |
| unpickle             | 15.1 us                                                    | 14.9 us: 1.02x faster                                                      |
| unpickle_list        | 5.34 us                                                    | 5.31 us: 1.01x faster                                                      |
| pickle_list          | 5.11 us                                                    | 5.07 us: 1.01x faster                                                      |
| unpickle_pure_python | 218 us                                                     | 217 us: 1.00x faster                                                       |
| pickle_dict          | 34.8 us                                                    | 34.9 us: 1.00x slower                                                      |
| pickle               | 11.5 us                                                    | 11.6 us: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                               |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                      |
| python_startup_no_site | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                                      |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.79 ms: 1.15x faster                                                      |
| django_template | 34.8 ms                                                    | 36.1 ms: 1.04x slower                                                      |
| genshi_text     | 23.7 ms                                                    | 25.8 ms: 1.09x slower                                                      |
| genshi_xml      | 51.6 ms                                                    | 61.2 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                      | 1.04x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.5 us: 1.45x faster                                                      |
| deepcopy                   | 367 us                                                     | 269 us: 1.37x faster                                                       |
| scimark_fft                | 392 ms                                                     | 309 ms: 1.27x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                    | 2.74 us: 1.22x faster                                                      |
| richards                   | 50.9 ms                                                    | 41.9 ms: 1.21x faster                                                      |
| richards_super             | 57.4 ms                                                    | 47.7 ms: 1.20x faster                                                      |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.39 ms: 1.20x faster                                                      |
| async_tree_none            | 378 ms                                                     | 317 ms: 1.19x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 394 ms: 1.18x faster                                                       |
| crypto_pyaes               | 77.5 ms                                                    | 66.3 ms: 1.17x faster                                                      |
| mako                       | 11.2 ms                                                    | 9.79 ms: 1.15x faster                                                      |
| spectral_norm              | 116 ms                                                     | 101 ms: 1.15x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.14x faster                                                       |
| float                      | 78.9 ms                                                    | 69.7 ms: 1.13x faster                                                      |
| xml_etree_parse            | 162 ms                                                     | 144 ms: 1.12x faster                                                       |
| xml_etree_process          | 61.2 ms                                                    | 54.5 ms: 1.12x faster                                                      |
| xml_etree_generate         | 87.4 ms                                                    | 78.0 ms: 1.12x faster                                                      |
| bpe_tokeniser              | 5.02 sec                                                   | 4.49 sec: 1.12x faster                                                     |
| sqlite_synth               | 2.99 us                                                    | 2.73 us: 1.09x faster                                                      |
| async_tree_io              | 939 ms                                                     | 858 ms: 1.09x faster                                                       |
| scimark_lu                 | 122 ms                                                     | 111 ms: 1.09x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 308 ms: 1.09x faster                                                       |
| scimark_monte_carlo        | 69.2 ms                                                    | 63.4 ms: 1.09x faster                                                      |
| go                         | 145 ms                                                     | 133 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                     | 98.8 ms: 1.09x faster                                                      |
| tomli_loads                | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                     |
| scimark_sor                | 127 ms                                                     | 117 ms: 1.09x faster                                                       |
| nbody                      | 88.3 ms                                                    | 81.3 ms: 1.09x faster                                                      |
| json_dumps                 | 10.7 ms                                                    | 9.88 ms: 1.09x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                                       |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                                      |
| json_loads                 | 28.9 us                                                    | 26.9 us: 1.08x faster                                                      |
| fannkuch                   | 402 ms                                                     | 374 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 547 ms: 1.07x faster                                                       |
| async_tree_io_tg           | 936 ms                                                     | 873 ms: 1.07x faster                                                       |
| gc_traversal               | 3.98 ms                                                    | 3.74 ms: 1.06x faster                                                      |
| coverage                   | 93.1 ms                                                    | 88.0 ms: 1.06x faster                                                      |
| json                       | 5.31 ms                                                    | 5.03 ms: 1.06x faster                                                      |
| telco                      | 8.41 ms                                                    | 7.98 ms: 1.05x faster                                                      |
| chaos                      | 61.3 ms                                                    | 58.6 ms: 1.05x faster                                                      |
| logging_format             | 6.47 us                                                    | 6.18 us: 1.05x faster                                                      |
| thrift                     | 823 us                                                     | 788 us: 1.04x faster                                                       |
| asyncio_tcp                | 508 ms                                                     | 487 ms: 1.04x faster                                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.04x faster                                                      |
| html5lib                   | 67.2 ms                                                    | 65.1 ms: 1.03x faster                                                      |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                       |
| pyflate                    | 484 ms                                                     | 470 ms: 1.03x faster                                                       |
| mdp                        | 2.79 sec                                                   | 2.71 sec: 1.03x faster                                                     |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                     |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                                       |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                      |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                       |
| regex_v8                   | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                                      |
| pprint_safe_repr           | 758 ms                                                     | 745 ms: 1.02x faster                                                       |
| unpickle                   | 15.1 us                                                    | 14.9 us: 1.02x faster                                                      |
| regex_dna                  | 221 ms                                                     | 218 ms: 1.02x faster                                                       |
| logging_simple             | 5.74 us                                                    | 5.67 us: 1.01x faster                                                      |
| python_startup_no_site     | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                                      |
| unpickle_list              | 5.34 us                                                    | 5.31 us: 1.01x faster                                                      |
| pickle_list                | 5.11 us                                                    | 5.07 us: 1.01x faster                                                      |
| unpickle_pure_python       | 218 us                                                     | 217 us: 1.00x faster                                                       |
| pickle_dict                | 34.8 us                                                    | 34.9 us: 1.00x slower                                                      |
| bench_thread_pool          | 834 us                                                     | 840 us: 1.01x slower                                                       |
| pickle                     | 11.5 us                                                    | 11.6 us: 1.01x slower                                                      |
| coroutines                 | 23.2 ms                                                    | 23.4 ms: 1.01x slower                                                      |
| 2to3                       | 274 ms                                                     | 277 ms: 1.01x slower                                                       |
| typing_runtime_protocols   | 165 us                                                     | 167 us: 1.01x slower                                                       |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                                       |
| dulwich_log                | 67.2 ms                                                    | 68.5 ms: 1.02x slower                                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.35 ms: 1.02x slower                                                      |
| regex_effbot               | 3.67 ms                                                    | 3.76 ms: 1.02x slower                                                      |
| async_generators           | 442 ms                                                     | 453 ms: 1.03x slower                                                       |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.03x slower                                                     |
| comprehensions             | 16.6 us                                                    | 17.1 us: 1.03x slower                                                      |
| django_template            | 34.8 ms                                                    | 36.1 ms: 1.04x slower                                                      |
| sqlglot_transpile          | 1.63 ms                                                    | 1.70 ms: 1.04x slower                                                      |
| raytrace                   | 267 ms                                                     | 279 ms: 1.04x slower                                                       |
| docutils                   | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                                     |
| sqlglot_optimize           | 55.5 ms                                                    | 58.4 ms: 1.05x slower                                                      |
| regex_compile              | 137 ms                                                     | 144 ms: 1.05x slower                                                       |
| sympy_str                  | 282 ms                                                     | 305 ms: 1.08x slower                                                       |
| sympy_expand               | 473 ms                                                     | 513 ms: 1.08x slower                                                       |
| genshi_text                | 23.7 ms                                                    | 25.8 ms: 1.09x slower                                                      |
| nqueens                    | 81.4 ms                                                    | 88.8 ms: 1.09x slower                                                      |
| sympy_sum                  | 156 ms                                                     | 174 ms: 1.12x slower                                                       |
| hexiom                     | 6.30 ms                                                    | 7.07 ms: 1.12x slower                                                      |
| sympy_integrate            | 20.5 ms                                                    | 23.1 ms: 1.12x slower                                                      |
| genshi_xml                 | 51.6 ms                                                    | 61.2 ms: 1.18x slower                                                      |
| pylint                     | 317 ms                                                     | 377 ms: 1.19x slower                                                       |
| generators                 | 29.6 ms                                                    | 36.2 ms: 1.22x slower                                                      |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                               |

Benchmark hidden because not significant (6): deltablue, pickle_pure_python, tornado_http, pprint_pformat, logging_silent, bench_mp_pool
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240919-3.14.0a0-563a4d7-JIT/bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7.json: unpack_sequence

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x
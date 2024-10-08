# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: jit_mem_2
- machine: linux-x86_64
- commit hash: 8dab2c9
- commit date: 2024-08-13
- overall geometric mean: 1.04x faster
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 284 ms: 1.04x slower                                                  |
| docutils       | 2.83 sec                                                   | 2.98 sec: 1.05x slower                                                |
| tornado_http   | 94.6 ms                                                    | 94.1 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 331 ms: 1.14x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 395 ms: 1.12x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 306 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 535 ms: 1.10x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 869 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 568 ms: 1.08x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 431 ms: 1.07x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                          |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 80.0 ms: 1.10x faster                                                 |
| float          | 78.9 ms                                                    | 73.9 ms: 1.07x faster                                                 |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                      | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.0 ms: 1.05x faster                                                 |
| regex_dna      | 221 ms                                                     | 215 ms: 1.03x faster                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.59 ms: 1.02x faster                                                 |
| regex_compile  | 137 ms                                                     | 142 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.90 sec: 1.12x faster                                                |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.06x faster                                                  |
| xml_etree_parse      | 162 ms                                                     | 153 ms: 1.06x faster                                                  |
| xml_etree_process    | 61.2 ms                                                    | 58.8 ms: 1.04x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 84.9 ms: 1.03x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                                  |
| json_loads           | 28.9 us                                                    | 28.4 us: 1.02x faster                                                 |
| Geometric mean       | (ref)                                                      | 1.04x faster                                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.87 ms: 1.14x faster                                                 |
| django_template | 34.8 ms                                                    | 37.0 ms: 1.06x slower                                                 |
| genshi_text     | 23.7 ms                                                    | 25.2 ms: 1.07x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 56.6 ms: 1.10x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.3 us: 1.45x faster                                                 |
| deepcopy                   | 367 us                                                     | 269 us: 1.37x faster                                                  |
| scimark_fft                | 392 ms                                                     | 306 ms: 1.28x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                    | 2.65 us: 1.26x faster                                                 |
| richards_super             | 57.4 ms                                                    | 45.6 ms: 1.26x faster                                                 |
| richards                   | 50.9 ms                                                    | 40.5 ms: 1.26x faster                                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.23 ms: 1.25x faster                                                 |
| crypto_pyaes               | 77.5 ms                                                    | 67.3 ms: 1.15x faster                                                 |
| spectral_norm              | 116 ms                                                     | 101 ms: 1.14x faster                                                  |
| async_tree_none            | 378 ms                                                     | 331 ms: 1.14x faster                                                  |
| gc_traversal               | 3.98 ms                                                    | 3.48 ms: 1.14x faster                                                 |
| mako                       | 11.2 ms                                                    | 9.87 ms: 1.14x faster                                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 395 ms: 1.12x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 1.90 sec: 1.12x faster                                                |
| pyflate                    | 484 ms                                                     | 434 ms: 1.12x faster                                                  |
| scimark_lu                 | 122 ms                                                     | 110 ms: 1.11x faster                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.6 ms: 1.11x faster                                                 |
| scimark_sor                | 127 ms                                                     | 115 ms: 1.10x faster                                                  |
| nbody                      | 88.3 ms                                                    | 80.0 ms: 1.10x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 306 ms: 1.10x faster                                                  |
| coverage                   | 93.1 ms                                                    | 84.8 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 535 ms: 1.10x faster                                                  |
| fannkuch                   | 402 ms                                                     | 369 ms: 1.09x faster                                                  |
| mdp                        | 2.79 sec                                                   | 2.56 sec: 1.09x faster                                                |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 869 ms: 1.08x faster                                                  |
| telco                      | 8.41 ms                                                    | 7.82 ms: 1.08x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 568 ms: 1.08x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 431 ms: 1.07x faster                                                  |
| float                      | 78.9 ms                                                    | 73.9 ms: 1.07x faster                                                 |
| logging_format             | 6.47 us                                                    | 6.10 us: 1.06x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 101 ms: 1.06x faster                                                  |
| xml_etree_parse            | 162 ms                                                     | 153 ms: 1.06x faster                                                  |
| chaos                      | 61.3 ms                                                    | 58.1 ms: 1.06x faster                                                 |
| meteor_contest             | 110 ms                                                     | 104 ms: 1.05x faster                                                  |
| regex_v8                   | 25.1 ms                                                    | 24.0 ms: 1.05x faster                                                 |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                                 |
| xml_etree_process          | 61.2 ms                                                    | 58.8 ms: 1.04x faster                                                 |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| deltablue                  | 3.25 ms                                                    | 3.13 ms: 1.04x faster                                                 |
| logging_simple             | 5.74 us                                                    | 5.54 us: 1.04x faster                                                 |
| thrift                     | 823 us                                                     | 795 us: 1.04x faster                                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.86 sec: 1.03x faster                                                |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                  |
| xml_etree_generate         | 87.4 ms                                                    | 84.9 ms: 1.03x faster                                                 |
| regex_dna                  | 221 ms                                                     | 215 ms: 1.03x faster                                                  |
| python_startup             | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| regex_effbot               | 3.67 ms                                                    | 3.59 ms: 1.02x faster                                                 |
| logging_silent             | 105 ns                                                     | 103 ns: 1.02x faster                                                  |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                                  |
| unpickle_pure_python       | 218 us                                                     | 214 us: 1.02x faster                                                  |
| json_loads                 | 28.9 us                                                    | 28.4 us: 1.02x faster                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                |
| pprint_safe_repr           | 758 ms                                                     | 745 ms: 1.02x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 821 us: 1.02x faster                                                  |
| asyncio_tcp                | 508 ms                                                     | 503 ms: 1.01x faster                                                  |
| tornado_http               | 94.6 ms                                                    | 94.1 ms: 1.01x faster                                                 |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.00x faster                                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.33 ms: 1.01x slower                                                 |
| async_generators           | 442 ms                                                     | 447 ms: 1.01x slower                                                  |
| raytrace                   | 267 ms                                                     | 270 ms: 1.01x slower                                                  |
| go                         | 145 ms                                                     | 148 ms: 1.03x slower                                                  |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.03x slower                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.69 ms: 1.03x slower                                                 |
| json                       | 5.31 ms                                                    | 5.50 ms: 1.04x slower                                                 |
| 2to3                       | 274 ms                                                     | 284 ms: 1.04x slower                                                  |
| regex_compile              | 137 ms                                                     | 142 ms: 1.04x slower                                                  |
| typing_runtime_protocols   | 165 us                                                     | 172 us: 1.04x slower                                                  |
| sympy_str                  | 282 ms                                                     | 296 ms: 1.05x slower                                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 58.3 ms: 1.05x slower                                                 |
| docutils                   | 2.83 sec                                                   | 2.98 sec: 1.05x slower                                                |
| django_template            | 34.8 ms                                                    | 37.0 ms: 1.06x slower                                                 |
| genshi_text                | 23.7 ms                                                    | 25.2 ms: 1.07x slower                                                 |
| sympy_expand               | 473 ms                                                     | 505 ms: 1.07x slower                                                  |
| nqueens                    | 81.4 ms                                                    | 87.8 ms: 1.08x slower                                                 |
| hexiom                     | 6.30 ms                                                    | 6.80 ms: 1.08x slower                                                 |
| sympy_sum                  | 156 ms                                                     | 170 ms: 1.09x slower                                                  |
| genshi_xml                 | 51.6 ms                                                    | 56.6 ms: 1.10x slower                                                 |
| sympy_integrate            | 20.5 ms                                                    | 22.8 ms: 1.11x slower                                                 |
| pylint                     | 317 ms                                                     | 366 ms: 1.15x slower                                                  |
| generators                 | 29.6 ms                                                    | 35.4 ms: 1.20x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                          |

Benchmark hidden because not significant (5): async_tree_io, pickle_pure_python, pprint_pformat, html5lib, pycparser
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.87% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x
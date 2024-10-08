# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: jit_mem_gc_old
- machine: linux-x86_64
- commit hash: 1268c80
- commit date: 2024-08-19
- overall geometric mean: 1.05x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 281 ms: 1.02x slower                                                       |
| docutils       | 2.83 sec                                                   | 3.00 sec: 1.06x slower                                                     |
| html5lib       | 67.2 ms                                                    | 64.2 ms: 1.05x faster                                                      |
| tornado_http   | 94.6 ms                                                    | 93.3 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                      | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 329 ms: 1.15x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 394 ms: 1.13x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 533 ms: 1.10x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 426 ms: 1.09x faster                                                       |
| async_tree_io_tg           | 936 ms                                                     | 860 ms: 1.09x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                                       |
| async_tree_io              | 939 ms                                                     | 898 ms: 1.05x faster                                                       |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.8 ms: 1.11x faster                                                      |
| nbody          | 88.3 ms                                                    | 83.4 ms: 1.06x faster                                                      |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                      | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 212 ms: 1.05x faster                                                       |
| regex_v8       | 25.1 ms                                                    | 24.3 ms: 1.03x faster                                                      |
| regex_effbot   | 3.67 ms                                                    | 3.59 ms: 1.02x faster                                                      |
| regex_compile  | 137 ms                                                     | 142 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                      | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.90 sec: 1.12x faster                                                     |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                     | 98.2 ms: 1.09x faster                                                      |
| xml_etree_process    | 61.2 ms                                                    | 57.1 ms: 1.07x faster                                                      |
| xml_etree_generate   | 87.4 ms                                                    | 81.7 ms: 1.07x faster                                                      |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                                      |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.01x faster                                                       |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                               |

Benchmark hidden because not significant (2): pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                      |
| python_startup_no_site | 7.11 ms                                                    | 7.12 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.0 ms: 1.12x faster                                                      |
| django_template | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                      |
| genshi_text     | 23.7 ms                                                    | 25.9 ms: 1.09x slower                                                      |
| genshi_xml      | 51.6 ms                                                    | 61.2 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                      | 1.04x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.7 us: 1.49x faster                                                      |
| deepcopy                   | 367 us                                                     | 268 us: 1.37x faster                                                       |
| richards                   | 50.9 ms                                                    | 39.0 ms: 1.31x faster                                                      |
| scimark_fft                | 392 ms                                                     | 303 ms: 1.29x faster                                                       |
| richards_super             | 57.4 ms                                                    | 44.8 ms: 1.28x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                    | 2.69 us: 1.25x faster                                                      |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.40 ms: 1.20x faster                                                      |
| crypto_pyaes               | 77.5 ms                                                    | 65.8 ms: 1.18x faster                                                      |
| spectral_norm              | 116 ms                                                     | 99.3 ms: 1.17x faster                                                      |
| async_tree_none            | 378 ms                                                     | 329 ms: 1.15x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 394 ms: 1.13x faster                                                       |
| mako                       | 11.2 ms                                                    | 10.0 ms: 1.12x faster                                                      |
| scimark_lu                 | 122 ms                                                     | 108 ms: 1.12x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                       |
| scimark_monte_carlo        | 69.2 ms                                                    | 61.9 ms: 1.12x faster                                                      |
| tomli_loads                | 2.12 sec                                                   | 1.90 sec: 1.12x faster                                                     |
| float                      | 78.9 ms                                                    | 70.8 ms: 1.11x faster                                                      |
| scimark_sor                | 127 ms                                                     | 115 ms: 1.11x faster                                                       |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                       |
| bpe_tokeniser              | 5.02 sec                                                   | 4.55 sec: 1.10x faster                                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 533 ms: 1.10x faster                                                       |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                     | 98.2 ms: 1.09x faster                                                      |
| coverage                   | 93.1 ms                                                    | 85.4 ms: 1.09x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 426 ms: 1.09x faster                                                       |
| async_tree_io_tg           | 936 ms                                                     | 860 ms: 1.09x faster                                                       |
| fannkuch                   | 402 ms                                                     | 370 ms: 1.09x faster                                                       |
| pyflate                    | 484 ms                                                     | 447 ms: 1.08x faster                                                       |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                      |
| telco                      | 8.41 ms                                                    | 7.82 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                                       |
| logging_format             | 6.47 us                                                    | 6.03 us: 1.07x faster                                                      |
| xml_etree_process          | 61.2 ms                                                    | 57.1 ms: 1.07x faster                                                      |
| xml_etree_generate         | 87.4 ms                                                    | 81.7 ms: 1.07x faster                                                      |
| gc_traversal               | 3.98 ms                                                    | 3.72 ms: 1.07x faster                                                      |
| nbody                      | 88.3 ms                                                    | 83.4 ms: 1.06x faster                                                      |
| thrift                     | 823 us                                                     | 782 us: 1.05x faster                                                       |
| chaos                      | 61.3 ms                                                    | 58.4 ms: 1.05x faster                                                      |
| html5lib                   | 67.2 ms                                                    | 64.2 ms: 1.05x faster                                                      |
| async_tree_io              | 939 ms                                                     | 898 ms: 1.05x faster                                                       |
| regex_dna                  | 221 ms                                                     | 212 ms: 1.05x faster                                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.04x faster                                                      |
| logging_silent             | 105 ns                                                     | 101 ns: 1.04x faster                                                       |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                       |
| logging_simple             | 5.74 us                                                    | 5.53 us: 1.04x faster                                                      |
| pprint_safe_repr           | 758 ms                                                     | 732 ms: 1.04x faster                                                       |
| regex_v8                   | 25.1 ms                                                    | 24.3 ms: 1.03x faster                                                      |
| deltablue                  | 3.25 ms                                                    | 3.15 ms: 1.03x faster                                                      |
| asyncio_tcp                | 508 ms                                                     | 493 ms: 1.03x faster                                                       |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.03x faster                                                     |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                                      |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                      |
| regex_effbot               | 3.67 ms                                                    | 3.59 ms: 1.02x faster                                                      |
| pprint_pformat             | 1.56 sec                                                   | 1.53 sec: 1.02x faster                                                     |
| bench_thread_pool          | 834 us                                                     | 819 us: 1.02x faster                                                       |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                       |
| tornado_http               | 94.6 ms                                                    | 93.3 ms: 1.01x faster                                                      |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.01x faster                                                       |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                      |
| raytrace                   | 267 ms                                                     | 266 ms: 1.00x faster                                                       |
| python_startup_no_site     | 7.11 ms                                                    | 7.12 ms: 1.00x slower                                                      |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                      |
| json                       | 5.31 ms                                                    | 5.35 ms: 1.01x slower                                                      |
| go                         | 145 ms                                                     | 146 ms: 1.01x slower                                                       |
| 2to3                       | 274 ms                                                     | 281 ms: 1.02x slower                                                       |
| django_template            | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                      |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.03x slower                                                     |
| sqlglot_transpile          | 1.63 ms                                                    | 1.69 ms: 1.03x slower                                                      |
| async_generators           | 442 ms                                                     | 457 ms: 1.03x slower                                                       |
| sqlglot_normalize          | 110 ms                                                     | 114 ms: 1.04x slower                                                       |
| regex_compile              | 137 ms                                                     | 142 ms: 1.04x slower                                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 57.9 ms: 1.04x slower                                                      |
| typing_runtime_protocols   | 165 us                                                     | 172 us: 1.04x slower                                                       |
| docutils                   | 2.83 sec                                                   | 3.00 sec: 1.06x slower                                                     |
| sympy_str                  | 282 ms                                                     | 303 ms: 1.07x slower                                                       |
| sympy_expand               | 473 ms                                                     | 508 ms: 1.07x slower                                                       |
| nqueens                    | 81.4 ms                                                    | 87.7 ms: 1.08x slower                                                      |
| hexiom                     | 6.30 ms                                                    | 6.87 ms: 1.09x slower                                                      |
| genshi_text                | 23.7 ms                                                    | 25.9 ms: 1.09x slower                                                      |
| sympy_integrate            | 20.5 ms                                                    | 23.1 ms: 1.13x slower                                                      |
| generators                 | 29.6 ms                                                    | 33.5 ms: 1.13x slower                                                      |
| sympy_sum                  | 156 ms                                                     | 177 ms: 1.14x slower                                                       |
| pylint                     | 317 ms                                                     | 369 ms: 1.16x slower                                                       |
| genshi_xml                 | 51.6 ms                                                    | 61.2 ms: 1.19x slower                                                      |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                               |

Benchmark hidden because not significant (4): coroutines, pickle_pure_python, sqlglot_parse, json_loads
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x
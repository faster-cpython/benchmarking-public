# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: jump_backward_0
- machine: linux-x86_64
- commit hash: 81f8369
- commit date: 2024-08-09
- overall geometric mean: 1.03x faster
- HPT reliability: 98.52%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 283 ms: 1.03x slower                                                   |
| docutils       | 2.83 sec                                                   | 3.08 sec: 1.09x slower                                                 |
| html5lib       | 67.2 ms                                                    | 64.2 ms: 1.05x faster                                                  |
| tornado_http   | 94.6 ms                                                    | 107 ms: 1.14x slower                                                   |
| Geometric mean | (ref)                                                      | 1.05x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 333 ms: 1.14x faster                                                   |
| async_tree_memoization_tg  | 444 ms                                                     | 400 ms: 1.11x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 539 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 571 ms: 1.07x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 434 ms: 1.07x faster                                                   |
| async_tree_io_tg           | 936 ms                                                     | 881 ms: 1.06x faster                                                   |
| Geometric mean             | (ref)                                                      | 1.08x faster                                                           |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.0 ms: 1.14x faster                                                  |
| nbody          | 88.3 ms                                                    | 79.6 ms: 1.11x faster                                                  |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                      | 1.09x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 212 ms: 1.04x faster                                                   |
| regex_v8       | 25.1 ms                                                    | 24.2 ms: 1.04x faster                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.60 ms: 1.02x faster                                                  |
| regex_compile  | 137 ms                                                     | 138 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                      | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|---------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_process   | 61.2 ms                                                    | 54.7 ms: 1.12x faster                                                  |
| xml_etree_parse     | 162 ms                                                     | 146 ms: 1.11x faster                                                   |
| tomli_loads         | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                                 |
| xml_etree_generate  | 87.4 ms                                                    | 80.0 ms: 1.09x faster                                                  |
| xml_etree_iterparse | 107 ms                                                     | 99.2 ms: 1.08x faster                                                  |
| json_loads          | 28.9 us                                                    | 27.2 us: 1.06x faster                                                  |
| pickle_pure_python  | 305 us                                                     | 293 us: 1.04x faster                                                   |
| json_dumps          | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                  |
| Geometric mean      | (ref)                                                      | 1.07x faster                                                           |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                  |
| python_startup_no_site | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.84 ms: 1.14x faster                                                  |
| genshi_text     | 23.7 ms                                                    | 23.9 ms: 1.01x slower                                                  |
| genshi_xml      | 51.6 ms                                                    | 55.1 ms: 1.07x slower                                                  |
| django_template | 34.8 ms                                                    | 39.3 ms: 1.13x slower                                                  |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.8 us: 1.38x faster                                                  |
| deepcopy                   | 367 us                                                     | 270 us: 1.36x faster                                                   |
| scimark_fft                | 392 ms                                                     | 313 ms: 1.25x faster                                                   |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.30 ms: 1.23x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                    | 2.80 us: 1.19x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 66.6 ms: 1.16x faster                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 59.8 ms: 1.16x faster                                                  |
| float                      | 78.9 ms                                                    | 69.0 ms: 1.14x faster                                                  |
| mako                       | 11.2 ms                                                    | 9.84 ms: 1.14x faster                                                  |
| async_tree_none            | 378 ms                                                     | 333 ms: 1.14x faster                                                   |
| spectral_norm              | 116 ms                                                     | 103 ms: 1.13x faster                                                   |
| scimark_sor                | 127 ms                                                     | 113 ms: 1.12x faster                                                   |
| xml_etree_process          | 61.2 ms                                                    | 54.7 ms: 1.12x faster                                                  |
| scimark_lu                 | 122 ms                                                     | 109 ms: 1.11x faster                                                   |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                   |
| async_tree_memoization_tg  | 444 ms                                                     | 400 ms: 1.11x faster                                                   |
| nbody                      | 88.3 ms                                                    | 79.6 ms: 1.11x faster                                                  |
| richards_super             | 57.4 ms                                                    | 51.7 ms: 1.11x faster                                                  |
| richards                   | 50.9 ms                                                    | 46.0 ms: 1.11x faster                                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.54 sec: 1.11x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.09x faster                                                   |
| tomli_loads                | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 80.0 ms: 1.09x faster                                                  |
| pyflate                    | 484 ms                                                     | 444 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 539 ms: 1.09x faster                                                   |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                  |
| telco                      | 8.41 ms                                                    | 7.75 ms: 1.09x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 99.2 ms: 1.08x faster                                                  |
| fannkuch                   | 402 ms                                                     | 372 ms: 1.08x faster                                                   |
| gc_traversal               | 3.98 ms                                                    | 3.71 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 571 ms: 1.07x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 434 ms: 1.07x faster                                                   |
| logging_silent             | 105 ns                                                     | 98.3 ns: 1.07x faster                                                  |
| chaos                      | 61.3 ms                                                    | 57.7 ms: 1.06x faster                                                  |
| json_loads                 | 28.9 us                                                    | 27.2 us: 1.06x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 881 ms: 1.06x faster                                                   |
| logging_format             | 6.47 us                                                    | 6.12 us: 1.06x faster                                                  |
| json                       | 5.31 ms                                                    | 5.03 ms: 1.05x faster                                                  |
| html5lib                   | 67.2 ms                                                    | 64.2 ms: 1.05x faster                                                  |
| regex_dna                  | 221 ms                                                     | 212 ms: 1.04x faster                                                   |
| mdp                        | 2.79 sec                                                   | 2.67 sec: 1.04x faster                                                 |
| pickle_pure_python         | 305 us                                                     | 293 us: 1.04x faster                                                   |
| pprint_safe_repr           | 758 ms                                                     | 728 ms: 1.04x faster                                                   |
| regex_v8                   | 25.1 ms                                                    | 24.2 ms: 1.04x faster                                                  |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                  |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                   |
| comprehensions             | 16.6 us                                                    | 16.1 us: 1.03x faster                                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.52 sec: 1.02x faster                                                 |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                                   |
| regex_effbot               | 3.67 ms                                                    | 3.60 ms: 1.02x faster                                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.79 ms: 1.02x faster                                                  |
| logging_simple             | 5.74 us                                                    | 5.66 us: 1.02x faster                                                  |
| asyncio_websockets         | 567 ms                                                     | 559 ms: 1.01x faster                                                   |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.83 sec: 1.01x faster                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                                  |
| regex_compile              | 137 ms                                                     | 138 ms: 1.01x slower                                                   |
| genshi_text                | 23.7 ms                                                    | 23.9 ms: 1.01x slower                                                  |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.03x slower                                                 |
| typing_runtime_protocols   | 165 us                                                     | 170 us: 1.03x slower                                                   |
| 2to3                       | 274 ms                                                     | 283 ms: 1.03x slower                                                   |
| async_generators           | 442 ms                                                     | 457 ms: 1.03x slower                                                   |
| go                         | 145 ms                                                     | 150 ms: 1.04x slower                                                   |
| raytrace                   | 267 ms                                                     | 277 ms: 1.04x slower                                                   |
| sqlglot_parse              | 1.32 ms                                                    | 1.37 ms: 1.04x slower                                                  |
| asyncio_tcp                | 508 ms                                                     | 530 ms: 1.04x slower                                                   |
| sqlglot_normalize          | 110 ms                                                     | 115 ms: 1.04x slower                                                   |
| sqlglot_optimize           | 55.5 ms                                                    | 58.1 ms: 1.05x slower                                                  |
| nqueens                    | 81.4 ms                                                    | 85.4 ms: 1.05x slower                                                  |
| bench_thread_pool          | 834 us                                                     | 883 us: 1.06x slower                                                   |
| sqlglot_transpile          | 1.63 ms                                                    | 1.73 ms: 1.06x slower                                                  |
| genshi_xml                 | 51.6 ms                                                    | 55.1 ms: 1.07x slower                                                  |
| hexiom                     | 6.30 ms                                                    | 6.83 ms: 1.08x slower                                                  |
| docutils                   | 2.83 sec                                                   | 3.08 sec: 1.09x slower                                                 |
| coroutines                 | 23.2 ms                                                    | 25.2 ms: 1.09x slower                                                  |
| sympy_expand               | 473 ms                                                     | 530 ms: 1.12x slower                                                   |
| django_template            | 34.8 ms                                                    | 39.3 ms: 1.13x slower                                                  |
| sympy_str                  | 282 ms                                                     | 320 ms: 1.13x slower                                                   |
| tornado_http               | 94.6 ms                                                    | 107 ms: 1.14x slower                                                   |
| generators                 | 29.6 ms                                                    | 35.1 ms: 1.19x slower                                                  |
| sympy_integrate            | 20.5 ms                                                    | 25.0 ms: 1.22x slower                                                  |
| sympy_sum                  | 156 ms                                                     | 197 ms: 1.26x slower                                                   |
| pylint                     | 317 ms                                                     | 401 ms: 1.26x slower                                                   |
| deltablue                  | 3.25 ms                                                    | 4.24 ms: 1.30x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                           |

Benchmark hidden because not significant (4): async_tree_io, unpickle_pure_python, coverage, thrift
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 98.52% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.14x
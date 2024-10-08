# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: experimental_gc_fix
- machine: linux-x86_64
- commit hash: 9d28e99
- commit date: 2024-09-27
- overall geometric mean: 1.01x faster
- HPT reliability: 99.28%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 272 ms: 1.01x faster                                                           |
| docutils       | 2.83 sec                                                   | 2.77 sec: 1.02x faster                                                         |
| html5lib       | 67.2 ms                                                    | 68.1 ms: 1.01x slower                                                          |
| tornado_http   | 94.6 ms                                                    | 91.5 ms: 1.03x faster                                                          |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 611 ms                                                     | 638 ms: 1.04x slower                                                           |
| async_tree_memoization     | 463 ms                                                     | 489 ms: 1.06x slower                                                           |
| async_tree_io              | 939 ms                                                     | 995 ms: 1.06x slower                                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 635 ms: 1.08x slower                                                           |
| async_tree_none            | 378 ms                                                     | 424 ms: 1.12x slower                                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 498 ms: 1.12x slower                                                           |
| async_tree_none_tg         | 336 ms                                                     | 390 ms: 1.16x slower                                                           |
| Geometric mean             | (ref)                                                      | 1.08x slower                                                                   |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                           |
| nbody          | 88.3 ms                                                    | 87.7 ms: 1.01x faster                                                          |
| float          | 78.9 ms                                                    | 97.0 ms: 1.23x slower                                                          |
| Geometric mean | (ref)                                                      | 1.06x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 128 ms: 1.07x faster                                                           |
| regex_v8       | 25.1 ms                                                    | 24.5 ms: 1.02x faster                                                          |
| regex_dna      | 221 ms                                                     | 223 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 27.1 us: 1.07x faster                                                          |
| unpickle             | 15.1 us                                                    | 14.5 us: 1.04x faster                                                          |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                          |
| unpickle_list        | 5.34 us                                                    | 5.22 us: 1.02x faster                                                          |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.01x faster                                                           |
| tomli_loads          | 2.12 sec                                                   | 2.09 sec: 1.01x faster                                                         |
| pickle_dict          | 34.8 us                                                    | 34.8 us: 1.00x slower                                                          |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                                          |
| pickle_list          | 5.11 us                                                    | 5.36 us: 1.05x slower                                                          |
| xml_etree_generate   | 87.4 ms                                                    | 93.0 ms: 1.06x slower                                                          |
| xml_etree_process    | 61.2 ms                                                    | 65.1 ms: 1.06x slower                                                          |
| xml_etree_parse      | 162 ms                                                     | 184 ms: 1.14x slower                                                           |
| xml_etree_iterparse  | 107 ms                                                     | 150 ms: 1.39x slower                                                           |
| Geometric mean       | (ref)                                                      | 1.03x slower                                                                   |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                    | 7.00 ms: 1.01x faster                                                          |
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                          |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.3 ms: 1.06x faster                                                          |
| mako            | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                                          |
| django_template | 34.8 ms                                                    | 35.2 ms: 1.01x slower                                                          |
| genshi_xml      | 51.6 ms                                                    | 54.4 ms: 1.05x slower                                                          |
| Geometric mean  | (ref)                                                      | 1.00x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 261 us: 1.41x faster                                                           |
| deepcopy_memo              | 39.7 us                                                    | 30.6 us: 1.30x faster                                                          |
| deepcopy_reduce            | 3.35 us                                                    | 2.71 us: 1.24x faster                                                          |
| go                         | 145 ms                                                     | 119 ms: 1.22x faster                                                           |
| pylint                     | 317 ms                                                     | 266 ms: 1.19x faster                                                           |
| richards                   | 50.9 ms                                                    | 46.4 ms: 1.10x faster                                                          |
| richards_super             | 57.4 ms                                                    | 52.4 ms: 1.10x faster                                                          |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.88 ms: 1.08x faster                                                          |
| create_gc_cycles           | 1.82 ms                                                    | 1.68 ms: 1.08x faster                                                          |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                          |
| coverage                   | 93.1 ms                                                    | 86.6 ms: 1.08x faster                                                          |
| scimark_fft                | 392 ms                                                     | 368 ms: 1.07x faster                                                           |
| json_loads                 | 28.9 us                                                    | 27.1 us: 1.07x faster                                                          |
| regex_compile              | 137 ms                                                     | 128 ms: 1.07x faster                                                           |
| genshi_text                | 23.7 ms                                                    | 22.3 ms: 1.06x faster                                                          |
| thrift                     | 823 us                                                     | 776 us: 1.06x faster                                                           |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                                         |
| sqlite_synth               | 2.99 us                                                    | 2.82 us: 1.06x faster                                                          |
| asyncio_tcp                | 508 ms                                                     | 480 ms: 1.06x faster                                                           |
| pprint_safe_repr           | 758 ms                                                     | 717 ms: 1.06x faster                                                           |
| sympy_sum                  | 156 ms                                                     | 147 ms: 1.06x faster                                                           |
| bench_thread_pool          | 834 us                                                     | 790 us: 1.06x faster                                                           |
| gc_traversal               | 3.98 ms                                                    | 3.77 ms: 1.06x faster                                                          |
| crypto_pyaes               | 77.5 ms                                                    | 73.4 ms: 1.05x faster                                                          |
| scimark_lu                 | 122 ms                                                     | 116 ms: 1.05x faster                                                           |
| typing_runtime_protocols   | 165 us                                                     | 157 us: 1.05x faster                                                           |
| sympy_str                  | 282 ms                                                     | 269 ms: 1.05x faster                                                           |
| generators                 | 29.6 ms                                                    | 28.3 ms: 1.05x faster                                                          |
| sympy_integrate            | 20.5 ms                                                    | 19.6 ms: 1.04x faster                                                          |
| spectral_norm              | 116 ms                                                     | 112 ms: 1.04x faster                                                           |
| unpickle                   | 15.1 us                                                    | 14.5 us: 1.04x faster                                                          |
| dulwich_log                | 67.2 ms                                                    | 64.8 ms: 1.04x faster                                                          |
| chaos                      | 61.3 ms                                                    | 59.2 ms: 1.04x faster                                                          |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.78 sec: 1.03x faster                                                         |
| tornado_http               | 94.6 ms                                                    | 91.5 ms: 1.03x faster                                                          |
| json                       | 5.31 ms                                                    | 5.13 ms: 1.03x faster                                                          |
| sympy_expand               | 473 ms                                                     | 458 ms: 1.03x faster                                                           |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                                           |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                          |
| regex_v8                   | 25.1 ms                                                    | 24.5 ms: 1.02x faster                                                          |
| unpickle_list              | 5.34 us                                                    | 5.22 us: 1.02x faster                                                          |
| asyncio_websockets         | 567 ms                                                     | 554 ms: 1.02x faster                                                           |
| nqueens                    | 81.4 ms                                                    | 79.6 ms: 1.02x faster                                                          |
| sqlglot_optimize           | 55.5 ms                                                    | 54.3 ms: 1.02x faster                                                          |
| mdp                        | 2.79 sec                                                   | 2.73 sec: 1.02x faster                                                         |
| scimark_sor                | 127 ms                                                     | 125 ms: 1.02x faster                                                           |
| pyflate                    | 484 ms                                                     | 474 ms: 1.02x faster                                                           |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                           |
| logging_format             | 6.47 us                                                    | 6.34 us: 1.02x faster                                                          |
| docutils                   | 2.83 sec                                                   | 2.77 sec: 1.02x faster                                                         |
| scimark_monte_carlo        | 69.2 ms                                                    | 68.0 ms: 1.02x faster                                                          |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                                           |
| python_startup_no_site     | 7.11 ms                                                    | 7.00 ms: 1.01x faster                                                          |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.01x faster                                                           |
| tomli_loads                | 2.12 sec                                                   | 2.09 sec: 1.01x faster                                                         |
| logging_simple             | 5.74 us                                                    | 5.68 us: 1.01x faster                                                          |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                          |
| raytrace                   | 267 ms                                                     | 264 ms: 1.01x faster                                                           |
| 2to3                       | 274 ms                                                     | 272 ms: 1.01x faster                                                           |
| nbody                      | 88.3 ms                                                    | 87.7 ms: 1.01x faster                                                          |
| comprehensions             | 16.6 us                                                    | 16.6 us: 1.00x faster                                                          |
| pickle_dict                | 34.8 us                                                    | 34.8 us: 1.00x slower                                                          |
| hexiom                     | 6.30 ms                                                    | 6.31 ms: 1.00x slower                                                          |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                                          |
| mako                       | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                                          |
| regex_dna                  | 221 ms                                                     | 223 ms: 1.01x slower                                                           |
| fannkuch                   | 402 ms                                                     | 405 ms: 1.01x slower                                                           |
| django_template            | 34.8 ms                                                    | 35.2 ms: 1.01x slower                                                          |
| html5lib                   | 67.2 ms                                                    | 68.1 ms: 1.01x slower                                                          |
| coroutines                 | 23.2 ms                                                    | 23.6 ms: 1.02x slower                                                          |
| pickle                     | 11.5 us                                                    | 11.7 us: 1.02x slower                                                          |
| sqlglot_transpile          | 1.63 ms                                                    | 1.67 ms: 1.02x slower                                                          |
| async_generators           | 442 ms                                                     | 459 ms: 1.04x slower                                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 638 ms: 1.04x slower                                                           |
| pickle_list                | 5.11 us                                                    | 5.36 us: 1.05x slower                                                          |
| pycparser                  | 1.16 sec                                                   | 1.22 sec: 1.05x slower                                                         |
| genshi_xml                 | 51.6 ms                                                    | 54.4 ms: 1.05x slower                                                          |
| async_tree_memoization     | 463 ms                                                     | 489 ms: 1.06x slower                                                           |
| async_tree_io              | 939 ms                                                     | 995 ms: 1.06x slower                                                           |
| xml_etree_generate         | 87.4 ms                                                    | 93.0 ms: 1.06x slower                                                          |
| xml_etree_process          | 61.2 ms                                                    | 65.1 ms: 1.06x slower                                                          |
| sqlglot_parse              | 1.32 ms                                                    | 1.41 ms: 1.07x slower                                                          |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 635 ms: 1.08x slower                                                           |
| deltablue                  | 3.25 ms                                                    | 3.55 ms: 1.09x slower                                                          |
| async_tree_none            | 378 ms                                                     | 424 ms: 1.12x slower                                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 498 ms: 1.12x slower                                                           |
| bpe_tokeniser              | 5.02 sec                                                   | 5.67 sec: 1.13x slower                                                         |
| xml_etree_parse            | 162 ms                                                     | 184 ms: 1.14x slower                                                           |
| async_tree_none_tg         | 336 ms                                                     | 390 ms: 1.16x slower                                                           |
| float                      | 78.9 ms                                                    | 97.0 ms: 1.23x slower                                                          |
| xml_etree_iterparse        | 107 ms                                                     | 150 ms: 1.39x slower                                                           |
| Geometric mean             | (ref)                                                      | 1.01x faster                                                                   |

Benchmark hidden because not significant (5): pickle_pure_python, regex_effbot, telco, logging_silent, async_tree_io_tg
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240927-3.14.0a0-9d28e99/bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99.json: unpack_sequence

# HPT report

- Reliability score: 99.28% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x
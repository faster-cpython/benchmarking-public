# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: experimental_gc_fix
- machine: linux-x86_64
- commit hash: 615a96e
- commit date: 2024-09-27
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 267 ms: 1.03x faster                                                           |
| docutils       | 2.83 sec                                                   | 2.58 sec: 1.09x faster                                                         |
| html5lib       | 67.2 ms                                                    | 67.9 ms: 1.01x slower                                                          |
| tornado_http   | 94.6 ms                                                    | 91.0 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                      | 1.04x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io              | 939 ms                                                     | 654 ms: 1.44x faster                                                           |
| async_tree_io_tg           | 936 ms                                                     | 653 ms: 1.43x faster                                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 349 ms: 1.27x faster                                                           |
| async_tree_none            | 378 ms                                                     | 301 ms: 1.26x faster                                                           |
| async_tree_memoization     | 463 ms                                                     | 370 ms: 1.25x faster                                                           |
| async_tree_none_tg         | 336 ms                                                     | 284 ms: 1.18x faster                                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 512 ms: 1.15x faster                                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 536 ms: 1.14x faster                                                           |
| Geometric mean             | (ref)                                                      | 1.26x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                           |
| float          | 78.9 ms                                                    | 92.7 ms: 1.18x slower                                                          |
| Geometric mean | (ref)                                                      | 1.05x slower                                                                   |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 128 ms: 1.07x faster                                                           |
| regex_v8       | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                                          |
| regex_dna      | 221 ms                                                     | 224 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 26.9 us: 1.07x faster                                                          |
| unpickle_list        | 5.34 us                                                    | 5.14 us: 1.04x faster                                                          |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                          |
| tomli_loads          | 2.12 sec                                                   | 2.08 sec: 1.02x faster                                                         |
| pickle_list          | 5.11 us                                                    | 5.06 us: 1.01x faster                                                          |
| pickle_dict          | 34.8 us                                                    | 34.6 us: 1.01x faster                                                          |
| unpickle_pure_python | 218 us                                                     | 217 us: 1.00x faster                                                           |
| xml_etree_process    | 61.2 ms                                                    | 61.5 ms: 1.01x slower                                                          |
| xml_etree_generate   | 87.4 ms                                                    | 88.1 ms: 1.01x slower                                                          |
| pickle               | 11.5 us                                                    | 11.6 us: 1.01x slower                                                          |
| pickle_pure_python   | 305 us                                                     | 308 us: 1.01x slower                                                           |
| xml_etree_iterparse  | 107 ms                                                     | 129 ms: 1.20x slower                                                           |
| Geometric mean       | (ref)                                                      | 1.00x slower                                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                    | 6.99 ms: 1.02x faster                                                          |
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                          |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.5 ms: 1.05x faster                                                          |
| django_template | 34.8 ms                                                    | 34.6 ms: 1.01x faster                                                          |
| genshi_xml      | 51.6 ms                                                    | 52.2 ms: 1.01x slower                                                          |
| mako            | 11.2 ms                                                    | 11.4 ms: 1.01x slower                                                          |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io              | 939 ms                                                     | 654 ms: 1.44x faster                                                           |
| async_tree_io_tg           | 936 ms                                                     | 653 ms: 1.43x faster                                                           |
| deepcopy                   | 367 us                                                     | 262 us: 1.40x faster                                                           |
| deepcopy_memo              | 39.7 us                                                    | 30.4 us: 1.31x faster                                                          |
| async_tree_memoization_tg  | 444 ms                                                     | 349 ms: 1.27x faster                                                           |
| async_tree_none            | 378 ms                                                     | 301 ms: 1.26x faster                                                           |
| async_tree_memoization     | 463 ms                                                     | 370 ms: 1.25x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.70 us: 1.24x faster                                                          |
| go                         | 145 ms                                                     | 120 ms: 1.20x faster                                                           |
| async_tree_none_tg         | 336 ms                                                     | 284 ms: 1.18x faster                                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 512 ms: 1.15x faster                                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 536 ms: 1.14x faster                                                           |
| pylint                     | 317 ms                                                     | 279 ms: 1.14x faster                                                           |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.65 ms: 1.13x faster                                                          |
| richards                   | 50.9 ms                                                    | 46.1 ms: 1.10x faster                                                          |
| scimark_fft                | 392 ms                                                     | 356 ms: 1.10x faster                                                           |
| richards_super             | 57.4 ms                                                    | 52.4 ms: 1.10x faster                                                          |
| coverage                   | 93.1 ms                                                    | 85.1 ms: 1.09x faster                                                          |
| docutils                   | 2.83 sec                                                   | 2.58 sec: 1.09x faster                                                         |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.08x faster                                                           |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                          |
| crypto_pyaes               | 77.5 ms                                                    | 72.0 ms: 1.08x faster                                                          |
| json                       | 5.31 ms                                                    | 4.93 ms: 1.08x faster                                                          |
| json_loads                 | 28.9 us                                                    | 26.9 us: 1.07x faster                                                          |
| regex_compile              | 137 ms                                                     | 128 ms: 1.07x faster                                                           |
| generators                 | 29.6 ms                                                    | 27.7 ms: 1.07x faster                                                          |
| create_gc_cycles           | 1.82 ms                                                    | 1.70 ms: 1.07x faster                                                          |
| thrift                     | 823 us                                                     | 773 us: 1.06x faster                                                           |
| asyncio_tcp                | 508 ms                                                     | 478 ms: 1.06x faster                                                           |
| sympy_sum                  | 156 ms                                                     | 147 ms: 1.06x faster                                                           |
| sqlite_synth               | 2.99 us                                                    | 2.83 us: 1.06x faster                                                          |
| genshi_text                | 23.7 ms                                                    | 22.5 ms: 1.05x faster                                                          |
| sympy_str                  | 282 ms                                                     | 268 ms: 1.05x faster                                                           |
| sympy_integrate            | 20.5 ms                                                    | 19.5 ms: 1.05x faster                                                          |
| meteor_contest             | 110 ms                                                     | 104 ms: 1.05x faster                                                           |
| pprint_safe_repr           | 758 ms                                                     | 723 ms: 1.05x faster                                                           |
| pprint_pformat             | 1.56 sec                                                   | 1.49 sec: 1.05x faster                                                         |
| bench_thread_pool          | 834 us                                                     | 797 us: 1.05x faster                                                           |
| pyflate                    | 484 ms                                                     | 463 ms: 1.05x faster                                                           |
| typing_runtime_protocols   | 165 us                                                     | 158 us: 1.04x faster                                                           |
| chaos                      | 61.3 ms                                                    | 59.0 ms: 1.04x faster                                                          |
| unpickle_list              | 5.34 us                                                    | 5.14 us: 1.04x faster                                                          |
| tornado_http               | 94.6 ms                                                    | 91.0 ms: 1.04x faster                                                          |
| sqlglot_normalize          | 110 ms                                                     | 106 ms: 1.04x faster                                                           |
| spectral_norm              | 116 ms                                                     | 112 ms: 1.03x faster                                                           |
| sqlglot_optimize           | 55.5 ms                                                    | 53.9 ms: 1.03x faster                                                          |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                         |
| sympy_expand               | 473 ms                                                     | 459 ms: 1.03x faster                                                           |
| dulwich_log                | 67.2 ms                                                    | 65.2 ms: 1.03x faster                                                          |
| logging_format             | 6.47 us                                                    | 6.29 us: 1.03x faster                                                          |
| 2to3                       | 274 ms                                                     | 267 ms: 1.03x faster                                                           |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                          |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                           |
| gc_traversal               | 3.98 ms                                                    | 3.89 ms: 1.02x faster                                                          |
| tomli_loads                | 2.12 sec                                                   | 2.08 sec: 1.02x faster                                                         |
| sqlglot_parse              | 1.32 ms                                                    | 1.30 ms: 1.02x faster                                                          |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                                           |
| sqlglot_transpile          | 1.63 ms                                                    | 1.61 ms: 1.02x faster                                                          |
| python_startup_no_site     | 7.11 ms                                                    | 6.99 ms: 1.02x faster                                                          |
| regex_v8                   | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                                          |
| nqueens                    | 81.4 ms                                                    | 80.1 ms: 1.02x faster                                                          |
| mdp                        | 2.79 sec                                                   | 2.75 sec: 1.01x faster                                                         |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                          |
| scimark_sor                | 127 ms                                                     | 126 ms: 1.01x faster                                                           |
| logging_simple             | 5.74 us                                                    | 5.68 us: 1.01x faster                                                          |
| raytrace                   | 267 ms                                                     | 264 ms: 1.01x faster                                                           |
| hexiom                     | 6.30 ms                                                    | 6.24 ms: 1.01x faster                                                          |
| fannkuch                   | 402 ms                                                     | 398 ms: 1.01x faster                                                           |
| scimark_monte_carlo        | 69.2 ms                                                    | 68.6 ms: 1.01x faster                                                          |
| pickle_list                | 5.11 us                                                    | 5.06 us: 1.01x faster                                                          |
| pickle_dict                | 34.8 us                                                    | 34.6 us: 1.01x faster                                                          |
| django_template            | 34.8 ms                                                    | 34.6 ms: 1.01x faster                                                          |
| unpickle_pure_python       | 218 us                                                     | 217 us: 1.00x faster                                                           |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                          |
| xml_etree_process          | 61.2 ms                                                    | 61.5 ms: 1.01x slower                                                          |
| xml_etree_generate         | 87.4 ms                                                    | 88.1 ms: 1.01x slower                                                          |
| pickle                     | 11.5 us                                                    | 11.6 us: 1.01x slower                                                          |
| pickle_pure_python         | 305 us                                                     | 308 us: 1.01x slower                                                           |
| comprehensions             | 16.6 us                                                    | 16.8 us: 1.01x slower                                                          |
| html5lib                   | 67.2 ms                                                    | 67.9 ms: 1.01x slower                                                          |
| regex_dna                  | 221 ms                                                     | 224 ms: 1.01x slower                                                           |
| genshi_xml                 | 51.6 ms                                                    | 52.2 ms: 1.01x slower                                                          |
| mako                       | 11.2 ms                                                    | 11.4 ms: 1.01x slower                                                          |
| deltablue                  | 3.25 ms                                                    | 3.30 ms: 1.02x slower                                                          |
| async_generators           | 442 ms                                                     | 457 ms: 1.03x slower                                                           |
| bpe_tokeniser              | 5.02 sec                                                   | 5.29 sec: 1.05x slower                                                         |
| pycparser                  | 1.16 sec                                                   | 1.22 sec: 1.06x slower                                                         |
| float                      | 78.9 ms                                                    | 92.7 ms: 1.18x slower                                                          |
| xml_etree_iterparse        | 107 ms                                                     | 129 ms: 1.20x slower                                                           |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                   |

Benchmark hidden because not significant (7): telco, logging_silent, coroutines, nbody, regex_effbot, xml_etree_parse, unpickle
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240927-3.14.0a0-615a96e/bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.99x
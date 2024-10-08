# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: experimental_gc_fix_
- machine: linux-x86_64
- commit hash: ea7b940
- commit date: 2024-09-27
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 268 ms: 1.02x faster                                                            |
| docutils       | 2.83 sec                                                   | 2.61 sec: 1.08x faster                                                          |
| html5lib       | 67.2 ms                                                    | 68.0 ms: 1.01x slower                                                           |
| tornado_http   | 94.6 ms                                                    | 91.1 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                      | 1.03x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 939 ms                                                     | 650 ms: 1.44x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 656 ms: 1.43x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 342 ms: 1.30x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 365 ms: 1.27x faster                                                            |
| async_tree_none            | 378 ms                                                     | 300 ms: 1.26x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 278 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 498 ms: 1.18x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 521 ms: 1.17x faster                                                            |
| Geometric mean             | (ref)                                                      | 1.28x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                            |
| nbody          | 88.3 ms                                                    | 89.6 ms: 1.02x slower                                                           |
| float          | 78.9 ms                                                    | 94.2 ms: 1.19x slower                                                           |
| Geometric mean | (ref)                                                      | 1.06x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 130 ms: 1.05x faster                                                            |
| regex_v8       | 25.1 ms                                                    | 24.3 ms: 1.03x faster                                                           |
| regex_effbot   | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                                           |
| regex_dna      | 221 ms                                                     | 229 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 26.9 us: 1.07x faster                                                           |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                           |
| pickle_dict          | 34.8 us                                                    | 33.6 us: 1.03x faster                                                           |
| pickle_list          | 5.11 us                                                    | 5.06 us: 1.01x faster                                                           |
| pickle               | 11.5 us                                                    | 11.4 us: 1.01x faster                                                           |
| pickle_pure_python   | 305 us                                                     | 307 us: 1.00x slower                                                            |
| xml_etree_generate   | 87.4 ms                                                    | 87.9 ms: 1.01x slower                                                           |
| unpickle_list        | 5.34 us                                                    | 5.41 us: 1.01x slower                                                           |
| xml_etree_process    | 61.2 ms                                                    | 61.9 ms: 1.01x slower                                                           |
| unpickle_pure_python | 218 us                                                     | 221 us: 1.01x slower                                                            |
| xml_etree_iterparse  | 107 ms                                                     | 134 ms: 1.24x slower                                                            |
| Geometric mean       | (ref)                                                      | 1.01x slower                                                                    |

Benchmark hidden because not significant (3): unpickle, tomli_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                    | 7.02 ms: 1.01x faster                                                           |
| python_startup         | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.3 ms: 1.06x faster                                                           |
| django_template | 34.8 ms                                                    | 34.2 ms: 1.02x faster                                                           |
| mako            | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                                           |
| genshi_xml      | 51.6 ms                                                    | 52.6 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 939 ms                                                     | 650 ms: 1.44x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 656 ms: 1.43x faster                                                            |
| deepcopy                   | 367 us                                                     | 262 us: 1.40x faster                                                            |
| deepcopy_memo              | 39.7 us                                                    | 30.6 us: 1.30x faster                                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 342 ms: 1.30x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 365 ms: 1.27x faster                                                            |
| async_tree_none            | 378 ms                                                     | 300 ms: 1.26x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                    | 2.66 us: 1.26x faster                                                           |
| async_tree_none_tg         | 336 ms                                                     | 278 ms: 1.21x faster                                                            |
| go                         | 145 ms                                                     | 121 ms: 1.19x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 498 ms: 1.18x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 521 ms: 1.17x faster                                                            |
| pylint                     | 317 ms                                                     | 279 ms: 1.14x faster                                                            |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.65 ms: 1.13x faster                                                           |
| scimark_fft                | 392 ms                                                     | 357 ms: 1.10x faster                                                            |
| richards                   | 50.9 ms                                                    | 46.5 ms: 1.09x faster                                                           |
| richards_super             | 57.4 ms                                                    | 52.7 ms: 1.09x faster                                                           |
| coverage                   | 93.1 ms                                                    | 85.8 ms: 1.08x faster                                                           |
| scimark_lu                 | 122 ms                                                     | 112 ms: 1.08x faster                                                            |
| crypto_pyaes               | 77.5 ms                                                    | 71.6 ms: 1.08x faster                                                           |
| docutils                   | 2.83 sec                                                   | 2.61 sec: 1.08x faster                                                          |
| json_loads                 | 28.9 us                                                    | 26.9 us: 1.07x faster                                                           |
| generators                 | 29.6 ms                                                    | 27.6 ms: 1.07x faster                                                           |
| thrift                     | 823 us                                                     | 769 us: 1.07x faster                                                            |
| json                       | 5.31 ms                                                    | 4.96 ms: 1.07x faster                                                           |
| pathlib                    | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                                           |
| create_gc_cycles           | 1.82 ms                                                    | 1.70 ms: 1.07x faster                                                           |
| sqlite_synth               | 2.99 us                                                    | 2.81 us: 1.06x faster                                                           |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                                          |
| asyncio_tcp                | 508 ms                                                     | 479 ms: 1.06x faster                                                            |
| genshi_text                | 23.7 ms                                                    | 22.3 ms: 1.06x faster                                                           |
| sympy_str                  | 282 ms                                                     | 267 ms: 1.06x faster                                                            |
| pprint_safe_repr           | 758 ms                                                     | 718 ms: 1.06x faster                                                            |
| sympy_sum                  | 156 ms                                                     | 148 ms: 1.06x faster                                                            |
| regex_compile              | 137 ms                                                     | 130 ms: 1.05x faster                                                            |
| bench_thread_pool          | 834 us                                                     | 793 us: 1.05x faster                                                            |
| sympy_integrate            | 20.5 ms                                                    | 19.6 ms: 1.05x faster                                                           |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                           |
| dulwich_log                | 67.2 ms                                                    | 64.6 ms: 1.04x faster                                                           |
| sympy_expand               | 473 ms                                                     | 455 ms: 1.04x faster                                                            |
| tornado_http               | 94.6 ms                                                    | 91.1 ms: 1.04x faster                                                           |
| pickle_dict                | 34.8 us                                                    | 33.6 us: 1.03x faster                                                           |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                                            |
| sqlglot_optimize           | 55.5 ms                                                    | 53.8 ms: 1.03x faster                                                           |
| regex_v8                   | 25.1 ms                                                    | 24.3 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                          |
| scimark_sor                | 127 ms                                                     | 124 ms: 1.03x faster                                                            |
| mdp                        | 2.79 sec                                                   | 2.71 sec: 1.03x faster                                                          |
| logging_format             | 6.47 us                                                    | 6.32 us: 1.02x faster                                                           |
| 2to3                       | 274 ms                                                     | 268 ms: 1.02x faster                                                            |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                            |
| gc_traversal               | 3.98 ms                                                    | 3.89 ms: 1.02x faster                                                           |
| spectral_norm              | 116 ms                                                     | 114 ms: 1.02x faster                                                            |
| chaos                      | 61.3 ms                                                    | 60.0 ms: 1.02x faster                                                           |
| typing_runtime_protocols   | 165 us                                                     | 161 us: 1.02x faster                                                            |
| nqueens                    | 81.4 ms                                                    | 79.8 ms: 1.02x faster                                                           |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.9 ms: 1.02x faster                                                           |
| django_template            | 34.8 ms                                                    | 34.2 ms: 1.02x faster                                                           |
| logging_simple             | 5.74 us                                                    | 5.66 us: 1.01x faster                                                           |
| python_startup_no_site     | 7.11 ms                                                    | 7.02 ms: 1.01x faster                                                           |
| sqlglot_parse              | 1.32 ms                                                    | 1.30 ms: 1.01x faster                                                           |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.01x faster                                                            |
| asyncio_websockets         | 567 ms                                                     | 560 ms: 1.01x faster                                                            |
| telco                      | 8.41 ms                                                    | 8.33 ms: 1.01x faster                                                           |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                                           |
| pickle_list                | 5.11 us                                                    | 5.06 us: 1.01x faster                                                           |
| python_startup             | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                                           |
| sqlglot_transpile          | 1.63 ms                                                    | 1.62 ms: 1.01x faster                                                           |
| pyflate                    | 484 ms                                                     | 480 ms: 1.01x faster                                                            |
| pickle                     | 11.5 us                                                    | 11.4 us: 1.01x faster                                                           |
| hexiom                     | 6.30 ms                                                    | 6.25 ms: 1.01x faster                                                           |
| logging_silent             | 105 ns                                                     | 104 ns: 1.00x faster                                                            |
| raytrace                   | 267 ms                                                     | 266 ms: 1.00x faster                                                            |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                                           |
| pickle_pure_python         | 305 us                                                     | 307 us: 1.00x slower                                                            |
| xml_etree_generate         | 87.4 ms                                                    | 87.9 ms: 1.01x slower                                                           |
| mako                       | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                                           |
| comprehensions             | 16.6 us                                                    | 16.8 us: 1.01x slower                                                           |
| html5lib                   | 67.2 ms                                                    | 68.0 ms: 1.01x slower                                                           |
| unpickle_list              | 5.34 us                                                    | 5.41 us: 1.01x slower                                                           |
| xml_etree_process          | 61.2 ms                                                    | 61.9 ms: 1.01x slower                                                           |
| unpickle_pure_python       | 218 us                                                     | 221 us: 1.01x slower                                                            |
| nbody                      | 88.3 ms                                                    | 89.6 ms: 1.02x slower                                                           |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                                          |
| genshi_xml                 | 51.6 ms                                                    | 52.6 ms: 1.02x slower                                                           |
| deltablue                  | 3.25 ms                                                    | 3.32 ms: 1.02x slower                                                           |
| regex_effbot               | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                                           |
| async_generators           | 442 ms                                                     | 455 ms: 1.03x slower                                                            |
| regex_dna                  | 221 ms                                                     | 229 ms: 1.03x slower                                                            |
| bpe_tokeniser              | 5.02 sec                                                   | 5.29 sec: 1.05x slower                                                          |
| float                      | 78.9 ms                                                    | 94.2 ms: 1.19x slower                                                           |
| xml_etree_iterparse        | 107 ms                                                     | 134 ms: 1.24x slower                                                            |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                    |

Benchmark hidden because not significant (4): unpickle, tomli_loads, fannkuch, xml_etree_parse
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240927-3.14.0a0-ea7b940/bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.99x
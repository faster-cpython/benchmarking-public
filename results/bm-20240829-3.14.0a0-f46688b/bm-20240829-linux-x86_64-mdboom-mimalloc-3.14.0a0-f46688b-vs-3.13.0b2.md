# Results vs. 3.13.0b2

- fork: mdboom
- ref: mimalloc
- machine: linux-x86_64
- commit hash: f46688b
- commit date: 2024-08-29
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 251 ms: 1.09x faster                                      |
| docutils       | 2.83 sec                                                   | 2.67 sec: 1.06x faster                                    |
| html5lib       | 67.2 ms                                                    | 61.9 ms: 1.09x faster                                     |
| tornado_http   | 94.6 ms                                                    | 86.9 ms: 1.09x faster                                     |
| Geometric mean | (ref)                                                      | 1.08x faster                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                      |
| async_tree_memoization     | 463 ms                                                     | 415 ms: 1.12x faster                                      |
| async_tree_none_tg         | 336 ms                                                     | 304 ms: 1.11x faster                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 534 ms: 1.10x faster                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 407 ms: 1.09x faster                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                      |
| async_tree_io              | 939 ms                                                     | 1.00 sec: 1.07x slower                                    |
| Geometric mean             | (ref)                                                      | 1.07x faster                                              |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------:|
| float          | 78.9 ms                                                    | 75.7 ms: 1.04x faster                                     |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                      |
| nbody          | 88.3 ms                                                    | 89.7 ms: 1.02x slower                                     |
| Geometric mean | (ref)                                                      | 1.02x faster                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.34 ms: 1.10x faster                                     |
| regex_compile  | 137 ms                                                     | 126 ms: 1.08x faster                                      |
| regex_v8       | 25.1 ms                                                    | 23.3 ms: 1.08x faster                                     |
| regex_dna      | 221 ms                                                     | 208 ms: 1.06x faster                                      |
| Geometric mean | (ref)                                                      | 1.08x faster                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------:|
| json_dumps           | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                     |
| xml_etree_parse      | 162 ms                                                     | 153 ms: 1.06x faster                                      |
| tomli_loads          | 2.12 sec                                                   | 2.01 sec: 1.05x faster                                    |
| json_loads           | 28.9 us                                                    | 27.5 us: 1.05x faster                                     |
| xml_etree_iterparse  | 107 ms                                                     | 103 ms: 1.04x faster                                      |
| xml_etree_process    | 61.2 ms                                                    | 58.9 ms: 1.04x faster                                     |
| pickle_pure_python   | 305 us                                                     | 296 us: 1.03x faster                                      |
| xml_etree_generate   | 87.4 ms                                                    | 84.7 ms: 1.03x faster                                     |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                      |
| Geometric mean       | (ref)                                                      | 1.04x faster                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                     |
| python_startup_no_site | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                     |
| Geometric mean         | (ref)                                                      | 1.02x faster                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.4 ms: 1.08x faster                                     |
| genshi_xml      | 51.6 ms                                                    | 49.1 ms: 1.05x faster                                     |
| django_template | 34.8 ms                                                    | 33.2 ms: 1.05x faster                                     |
| genshi_text     | 23.7 ms                                                    | 22.8 ms: 1.04x faster                                     |
| Geometric mean  | (ref)                                                      | 1.06x faster                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 253 us: 1.45x faster                                      |
| deepcopy_memo              | 39.7 us                                                    | 29.3 us: 1.35x faster                                     |
| deepcopy_reduce            | 3.35 us                                                    | 2.61 us: 1.28x faster                                     |
| go                         | 145 ms                                                     | 116 ms: 1.25x faster                                      |
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                      |
| pathlib                    | 17.3 ms                                                    | 15.2 ms: 1.14x faster                                     |
| scimark_fft                | 392 ms                                                     | 350 ms: 1.12x faster                                      |
| async_tree_memoization     | 463 ms                                                     | 415 ms: 1.12x faster                                      |
| crypto_pyaes               | 77.5 ms                                                    | 69.9 ms: 1.11x faster                                     |
| async_tree_none_tg         | 336 ms                                                     | 304 ms: 1.11x faster                                      |
| mdp                        | 2.79 sec                                                   | 2.52 sec: 1.11x faster                                    |
| thrift                     | 823 us                                                     | 747 us: 1.10x faster                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 534 ms: 1.10x faster                                      |
| regex_effbot               | 3.67 ms                                                    | 3.34 ms: 1.10x faster                                     |
| gc_traversal               | 3.98 ms                                                    | 3.62 ms: 1.10x faster                                     |
| scimark_lu                 | 122 ms                                                     | 111 ms: 1.10x faster                                      |
| pyflate                    | 484 ms                                                     | 442 ms: 1.10x faster                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 407 ms: 1.09x faster                                      |
| 2to3                       | 274 ms                                                     | 251 ms: 1.09x faster                                      |
| tornado_http               | 94.6 ms                                                    | 86.9 ms: 1.09x faster                                     |
| pprint_safe_repr           | 758 ms                                                     | 697 ms: 1.09x faster                                      |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.84 ms: 1.09x faster                                     |
| html5lib                   | 67.2 ms                                                    | 61.9 ms: 1.09x faster                                     |
| richards                   | 50.9 ms                                                    | 47.0 ms: 1.08x faster                                     |
| mako                       | 11.2 ms                                                    | 10.4 ms: 1.08x faster                                     |
| regex_compile              | 137 ms                                                     | 126 ms: 1.08x faster                                      |
| pprint_pformat             | 1.56 sec                                                   | 1.44 sec: 1.08x faster                                    |
| regex_v8                   | 25.1 ms                                                    | 23.3 ms: 1.08x faster                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                      |
| spectral_norm              | 116 ms                                                     | 108 ms: 1.07x faster                                      |
| sympy_str                  | 282 ms                                                     | 263 ms: 1.07x faster                                      |
| pycparser                  | 1.16 sec                                                   | 1.08 sec: 1.07x faster                                    |
| richards_super             | 57.4 ms                                                    | 53.5 ms: 1.07x faster                                     |
| sympy_sum                  | 156 ms                                                     | 146 ms: 1.07x faster                                      |
| json                       | 5.31 ms                                                    | 4.97 ms: 1.07x faster                                     |
| sqlglot_optimize           | 55.5 ms                                                    | 52.1 ms: 1.07x faster                                     |
| sqlglot_normalize          | 110 ms                                                     | 104 ms: 1.06x faster                                      |
| logging_silent             | 105 ns                                                     | 98.5 ns: 1.06x faster                                     |
| regex_dna                  | 221 ms                                                     | 208 ms: 1.06x faster                                      |
| json_dumps                 | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                     |
| docutils                   | 2.83 sec                                                   | 2.67 sec: 1.06x faster                                    |
| sympy_expand               | 473 ms                                                     | 447 ms: 1.06x faster                                      |
| logging_format             | 6.47 us                                                    | 6.13 us: 1.06x faster                                     |
| xml_etree_parse            | 162 ms                                                     | 153 ms: 1.06x faster                                      |
| sympy_integrate            | 20.5 ms                                                    | 19.5 ms: 1.05x faster                                     |
| tomli_loads                | 2.12 sec                                                   | 2.01 sec: 1.05x faster                                    |
| generators                 | 29.6 ms                                                    | 28.2 ms: 1.05x faster                                     |
| typing_runtime_protocols   | 165 us                                                     | 157 us: 1.05x faster                                      |
| json_loads                 | 28.9 us                                                    | 27.5 us: 1.05x faster                                     |
| genshi_xml                 | 51.6 ms                                                    | 49.1 ms: 1.05x faster                                     |
| chaos                      | 61.3 ms                                                    | 58.5 ms: 1.05x faster                                     |
| django_template            | 34.8 ms                                                    | 33.2 ms: 1.05x faster                                     |
| scimark_monte_carlo        | 69.2 ms                                                    | 66.1 ms: 1.05x faster                                     |
| scimark_sor                | 127 ms                                                     | 122 ms: 1.05x faster                                      |
| nqueens                    | 81.4 ms                                                    | 77.9 ms: 1.05x faster                                     |
| asyncio_websockets         | 567 ms                                                     | 542 ms: 1.05x faster                                      |
| xml_etree_iterparse        | 107 ms                                                     | 103 ms: 1.04x faster                                      |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.04x faster                                     |
| sqlglot_parse              | 1.32 ms                                                    | 1.26 ms: 1.04x faster                                     |
| sqlglot_transpile          | 1.63 ms                                                    | 1.57 ms: 1.04x faster                                     |
| float                      | 78.9 ms                                                    | 75.7 ms: 1.04x faster                                     |
| coverage                   | 93.1 ms                                                    | 89.3 ms: 1.04x faster                                     |
| genshi_text                | 23.7 ms                                                    | 22.8 ms: 1.04x faster                                     |
| xml_etree_process          | 61.2 ms                                                    | 58.9 ms: 1.04x faster                                     |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                      |
| pickle_pure_python         | 305 us                                                     | 296 us: 1.03x faster                                      |
| xml_etree_generate         | 87.4 ms                                                    | 84.7 ms: 1.03x faster                                     |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                      |
| python_startup             | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                     |
| asyncio_tcp                | 508 ms                                                     | 496 ms: 1.03x faster                                      |
| unpickle_pure_python       | 218 us                                                     | 214 us: 1.02x faster                                      |
| deltablue                  | 3.25 ms                                                    | 3.19 ms: 1.02x faster                                     |
| hexiom                     | 6.30 ms                                                    | 6.19 ms: 1.02x faster                                     |
| bpe_tokeniser              | 5.02 sec                                                   | 4.96 sec: 1.01x faster                                    |
| raytrace                   | 267 ms                                                     | 264 ms: 1.01x faster                                      |
| async_generators           | 442 ms                                                     | 437 ms: 1.01x faster                                      |
| python_startup_no_site     | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                     |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                     |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.83 sec: 1.01x faster                                    |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                     |
| nbody                      | 88.3 ms                                                    | 89.7 ms: 1.02x slower                                     |
| async_tree_io              | 939 ms                                                     | 1.00 sec: 1.07x slower                                    |
| bench_thread_pool          | 834 us                                                     | 1.24 ms: 1.49x slower                                     |
| Geometric mean             | (ref)                                                      | 1.06x faster                                              |

Benchmark hidden because not significant (6): logging_simple, comprehensions, fannkuch, telco, pylint, async_tree_io_tg
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x
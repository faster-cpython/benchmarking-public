# Results vs. 3.13.0b2

- fork: mdboom
- ref: cmq_mdboom
- machine: linux-x86_64
- commit hash: 8ca892b
- commit date: 2024-09-26
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 253 ms: 1.08x faster                                        |
| docutils       | 2.83 sec                                                   | 2.66 sec: 1.06x faster                                      |
| html5lib       | 67.2 ms                                                    | 63.9 ms: 1.05x faster                                       |
| tornado_http   | 94.6 ms                                                    | 90.4 ms: 1.05x faster                                       |
| Geometric mean | (ref)                                                      | 1.06x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 315 ms: 1.20x faster                                        |
| async_tree_memoization     | 463 ms                                                     | 392 ms: 1.18x faster                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 389 ms: 1.14x faster                                        |
| async_tree_none_tg         | 336 ms                                                     | 304 ms: 1.11x faster                                        |
| async_tree_io              | 939 ms                                                     | 855 ms: 1.10x faster                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 560 ms: 1.09x faster                                        |
| async_tree_io_tg           | 936 ms                                                     | 869 ms: 1.08x faster                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 548 ms: 1.07x faster                                        |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 78.9 ms                                                    | 76.0 ms: 1.04x faster                                       |
| pidigits       | 191 ms                                                     | 187 ms: 1.03x faster                                        |
| nbody          | 88.3 ms                                                    | 88.0 ms: 1.00x faster                                       |
| Geometric mean | (ref)                                                      | 1.02x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 127 ms: 1.07x faster                                        |
| regex_v8       | 25.1 ms                                                    | 24.2 ms: 1.04x faster                                       |
| regex_effbot   | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                       |
| regex_dna      | 221 ms                                                     | 229 ms: 1.04x slower                                        |
| Geometric mean | (ref)                                                      | 1.02x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 26.8 us: 1.08x faster                                       |
| xml_etree_process    | 61.2 ms                                                    | 58.4 ms: 1.05x faster                                       |
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                        |
| unpickle             | 15.1 us                                                    | 14.6 us: 1.04x faster                                       |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                       |
| xml_etree_generate   | 87.4 ms                                                    | 84.8 ms: 1.03x faster                                       |
| xml_etree_iterparse  | 107 ms                                                     | 104 ms: 1.03x faster                                        |
| pickle_dict          | 34.8 us                                                    | 33.9 us: 1.03x faster                                       |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                        |
| unpickle_list        | 5.34 us                                                    | 5.24 us: 1.02x faster                                       |
| tomli_loads          | 2.12 sec                                                   | 2.09 sec: 1.02x faster                                      |
| pickle_pure_python   | 305 us                                                     | 307 us: 1.00x slower                                        |
| pickle               | 11.5 us                                                    | 11.8 us: 1.03x slower                                       |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                       |
| python_startup_no_site | 7.11 ms                                                    | 6.98 ms: 1.02x faster                                       |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 21.8 ms: 1.09x faster                                       |
| genshi_xml      | 51.6 ms                                                    | 49.2 ms: 1.05x faster                                       |
| django_template | 34.8 ms                                                    | 34.0 ms: 1.02x faster                                       |
| Geometric mean  | (ref)                                                      | 1.04x faster                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 258 us: 1.42x faster                                        |
| deepcopy_memo              | 39.7 us                                                    | 29.7 us: 1.34x faster                                       |
| deepcopy_reduce            | 3.35 us                                                    | 2.69 us: 1.24x faster                                       |
| go                         | 145 ms                                                     | 117 ms: 1.24x faster                                        |
| async_tree_none            | 378 ms                                                     | 315 ms: 1.20x faster                                        |
| async_tree_memoization     | 463 ms                                                     | 392 ms: 1.18x faster                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 389 ms: 1.14x faster                                        |
| async_tree_none_tg         | 336 ms                                                     | 304 ms: 1.11x faster                                        |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.79 ms: 1.10x faster                                       |
| richards                   | 50.9 ms                                                    | 46.2 ms: 1.10x faster                                       |
| richards_super             | 57.4 ms                                                    | 52.2 ms: 1.10x faster                                       |
| async_tree_io              | 939 ms                                                     | 855 ms: 1.10x faster                                        |
| scimark_fft                | 392 ms                                                     | 358 ms: 1.10x faster                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 560 ms: 1.09x faster                                        |
| genshi_text                | 23.7 ms                                                    | 21.8 ms: 1.09x faster                                       |
| scimark_lu                 | 122 ms                                                     | 112 ms: 1.08x faster                                        |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                       |
| mdp                        | 2.79 sec                                                   | 2.57 sec: 1.08x faster                                      |
| 2to3                       | 274 ms                                                     | 253 ms: 1.08x faster                                        |
| json                       | 5.31 ms                                                    | 4.90 ms: 1.08x faster                                       |
| json_loads                 | 28.9 us                                                    | 26.8 us: 1.08x faster                                       |
| async_tree_io_tg           | 936 ms                                                     | 869 ms: 1.08x faster                                        |
| regex_compile              | 137 ms                                                     | 127 ms: 1.07x faster                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 548 ms: 1.07x faster                                        |
| generators                 | 29.6 ms                                                    | 27.8 ms: 1.07x faster                                       |
| crypto_pyaes               | 77.5 ms                                                    | 72.7 ms: 1.06x faster                                       |
| thrift                     | 823 us                                                     | 774 us: 1.06x faster                                        |
| sqlite_synth               | 2.99 us                                                    | 2.81 us: 1.06x faster                                       |
| chaos                      | 61.3 ms                                                    | 57.7 ms: 1.06x faster                                       |
| docutils                   | 2.83 sec                                                   | 2.66 sec: 1.06x faster                                      |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                      |
| sympy_sum                  | 156 ms                                                     | 147 ms: 1.06x faster                                        |
| create_gc_cycles           | 1.82 ms                                                    | 1.71 ms: 1.06x faster                                       |
| sympy_str                  | 282 ms                                                     | 267 ms: 1.06x faster                                        |
| asyncio_tcp                | 508 ms                                                     | 481 ms: 1.06x faster                                        |
| bench_thread_pool          | 834 us                                                     | 789 us: 1.06x faster                                        |
| html5lib                   | 67.2 ms                                                    | 63.9 ms: 1.05x faster                                       |
| pprint_safe_repr           | 758 ms                                                     | 721 ms: 1.05x faster                                        |
| bpe_tokeniser              | 5.02 sec                                                   | 4.77 sec: 1.05x faster                                      |
| genshi_xml                 | 51.6 ms                                                    | 49.2 ms: 1.05x faster                                       |
| sympy_integrate            | 20.5 ms                                                    | 19.5 ms: 1.05x faster                                       |
| logging_format             | 6.47 us                                                    | 6.17 us: 1.05x faster                                       |
| xml_etree_process          | 61.2 ms                                                    | 58.4 ms: 1.05x faster                                       |
| tornado_http               | 94.6 ms                                                    | 90.4 ms: 1.05x faster                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 53.0 ms: 1.05x faster                                       |
| dulwich_log                | 67.2 ms                                                    | 64.3 ms: 1.05x faster                                       |
| sympy_expand               | 473 ms                                                     | 453 ms: 1.04x faster                                        |
| sqlglot_normalize          | 110 ms                                                     | 106 ms: 1.04x faster                                        |
| typing_runtime_protocols   | 165 us                                                     | 159 us: 1.04x faster                                        |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                        |
| float                      | 78.9 ms                                                    | 76.0 ms: 1.04x faster                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.57 ms: 1.04x faster                                       |
| coverage                   | 93.1 ms                                                    | 89.8 ms: 1.04x faster                                       |
| unpickle                   | 15.1 us                                                    | 14.6 us: 1.04x faster                                       |
| regex_v8                   | 25.1 ms                                                    | 24.2 ms: 1.04x faster                                       |
| logging_simple             | 5.74 us                                                    | 5.55 us: 1.03x faster                                       |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                       |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                        |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                       |
| scimark_sor                | 127 ms                                                     | 124 ms: 1.03x faster                                        |
| xml_etree_generate         | 87.4 ms                                                    | 84.8 ms: 1.03x faster                                       |
| pycparser                  | 1.16 sec                                                   | 1.12 sec: 1.03x faster                                      |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.2 ms: 1.03x faster                                       |
| xml_etree_iterparse        | 107 ms                                                     | 104 ms: 1.03x faster                                        |
| pickle_dict                | 34.8 us                                                    | 33.9 us: 1.03x faster                                       |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                       |
| pidigits                   | 191 ms                                                     | 187 ms: 1.03x faster                                        |
| django_template            | 34.8 ms                                                    | 34.0 ms: 1.02x faster                                       |
| spectral_norm              | 116 ms                                                     | 114 ms: 1.02x faster                                        |
| unpickle_pure_python       | 218 us                                                     | 214 us: 1.02x faster                                        |
| unpickle_list              | 5.34 us                                                    | 5.24 us: 1.02x faster                                       |
| python_startup_no_site     | 7.11 ms                                                    | 6.98 ms: 1.02x faster                                       |
| async_generators           | 442 ms                                                     | 434 ms: 1.02x faster                                        |
| pyflate                    | 484 ms                                                     | 476 ms: 1.02x faster                                        |
| raytrace                   | 267 ms                                                     | 262 ms: 1.02x faster                                        |
| tomli_loads                | 2.12 sec                                                   | 2.09 sec: 1.02x faster                                      |
| hexiom                     | 6.30 ms                                                    | 6.20 ms: 1.02x faster                                       |
| gc_traversal               | 3.98 ms                                                    | 3.92 ms: 1.01x faster                                       |
| nqueens                    | 81.4 ms                                                    | 80.4 ms: 1.01x faster                                       |
| asyncio_websockets         | 567 ms                                                     | 560 ms: 1.01x faster                                        |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                       |
| nbody                      | 88.3 ms                                                    | 88.0 ms: 1.00x faster                                       |
| pickle_pure_python         | 305 us                                                     | 307 us: 1.00x slower                                        |
| logging_silent             | 105 ns                                                     | 105 ns: 1.00x slower                                        |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                       |
| regex_effbot               | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                       |
| coroutines                 | 23.2 ms                                                    | 23.4 ms: 1.01x slower                                       |
| fannkuch                   | 402 ms                                                     | 405 ms: 1.01x slower                                        |
| pickle                     | 11.5 us                                                    | 11.8 us: 1.03x slower                                       |
| regex_dna                  | 221 ms                                                     | 229 ms: 1.04x slower                                        |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                |

Benchmark hidden because not significant (5): telco, deltablue, pickle_list, mako, pylint
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240926-3.14.0a0-8ca892b/bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.01x
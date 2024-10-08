# Results vs. 3.13.0b2

- fork: mdboom
- ref: remove_redundant_typ
- machine: linux-x86_64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 255 ms: 1.08x faster                                                  |
| docutils       | 2.83 sec                                                   | 2.63 sec: 1.07x faster                                                |
| html5lib       | 67.2 ms                                                    | 61.5 ms: 1.09x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 90.4 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                      | 1.07x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 315 ms: 1.20x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 392 ms: 1.18x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 389 ms: 1.14x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 560 ms: 1.09x faster                                                  |
| async_tree_io              | 939 ms                                                     | 867 ms: 1.08x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 874 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 549 ms: 1.07x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 75.6 ms: 1.04x faster                                                 |
| pidigits       | 191 ms                                                     | 187 ms: 1.03x faster                                                  |
| nbody          | 88.3 ms                                                    | 86.7 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 128 ms: 1.07x faster                                                  |
| regex_dna      | 221 ms                                                     | 225 ms: 1.02x slower                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.89 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 26.7 us: 1.08x faster                                                 |
| pickle_dict          | 34.8 us                                                    | 32.7 us: 1.06x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 58.6 ms: 1.04x faster                                                 |
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 103 ms: 1.04x faster                                                  |
| unpickle_list        | 5.34 us                                                    | 5.15 us: 1.04x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 84.8 ms: 1.03x faster                                                 |
| tomli_loads          | 2.12 sec                                                   | 2.06 sec: 1.03x faster                                                |
| pickle_list          | 5.11 us                                                    | 4.98 us: 1.03x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                  |
| pickle               | 11.5 us                                                    | 11.8 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                          |

Benchmark hidden because not significant (2): pickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.00 ms: 1.02x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.1 ms: 1.07x faster                                                 |
| genshi_xml      | 51.6 ms                                                    | 48.6 ms: 1.06x faster                                                 |
| django_template | 34.8 ms                                                    | 34.2 ms: 1.02x faster                                                 |
| mako            | 11.2 ms                                                    | 11.1 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                      | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 255 us: 1.44x faster                                                  |
| deepcopy_memo              | 39.7 us                                                    | 29.9 us: 1.33x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.64 us: 1.27x faster                                                 |
| go                         | 145 ms                                                     | 119 ms: 1.21x faster                                                  |
| async_tree_none            | 378 ms                                                     | 315 ms: 1.20x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 392 ms: 1.18x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 389 ms: 1.14x faster                                                  |
| richards                   | 50.9 ms                                                    | 45.4 ms: 1.12x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                  |
| coverage                   | 93.1 ms                                                    | 83.7 ms: 1.11x faster                                                 |
| richards_super             | 57.4 ms                                                    | 51.6 ms: 1.11x faster                                                 |
| html5lib                   | 67.2 ms                                                    | 61.5 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 560 ms: 1.09x faster                                                  |
| scimark_lu                 | 122 ms                                                     | 112 ms: 1.08x faster                                                  |
| json_loads                 | 28.9 us                                                    | 26.7 us: 1.08x faster                                                 |
| async_tree_io              | 939 ms                                                     | 867 ms: 1.08x faster                                                  |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                                 |
| 2to3                       | 274 ms                                                     | 255 ms: 1.08x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 72.0 ms: 1.08x faster                                                 |
| json                       | 5.31 ms                                                    | 4.94 ms: 1.07x faster                                                 |
| docutils                   | 2.83 sec                                                   | 2.63 sec: 1.07x faster                                                |
| genshi_text                | 23.7 ms                                                    | 22.1 ms: 1.07x faster                                                 |
| pprint_safe_repr           | 758 ms                                                     | 708 ms: 1.07x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 874 ms: 1.07x faster                                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.45 sec: 1.07x faster                                                |
| regex_compile              | 137 ms                                                     | 128 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 549 ms: 1.07x faster                                                  |
| sympy_sum                  | 156 ms                                                     | 146 ms: 1.07x faster                                                  |
| asyncio_tcp                | 508 ms                                                     | 477 ms: 1.07x faster                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.95 ms: 1.06x faster                                                 |
| pickle_dict                | 34.8 us                                                    | 32.7 us: 1.06x faster                                                 |
| genshi_xml                 | 51.6 ms                                                    | 48.6 ms: 1.06x faster                                                 |
| scimark_fft                | 392 ms                                                     | 370 ms: 1.06x faster                                                  |
| thrift                     | 823 us                                                     | 777 us: 1.06x faster                                                  |
| sympy_str                  | 282 ms                                                     | 267 ms: 1.06x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 789 us: 1.06x faster                                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.72 ms: 1.05x faster                                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.77 sec: 1.05x faster                                                |
| generators                 | 29.6 ms                                                    | 28.2 ms: 1.05x faster                                                 |
| sympy_integrate            | 20.5 ms                                                    | 19.6 ms: 1.05x faster                                                 |
| tornado_http               | 94.6 ms                                                    | 90.4 ms: 1.05x faster                                                 |
| chaos                      | 61.3 ms                                                    | 58.6 ms: 1.05x faster                                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 53.1 ms: 1.05x faster                                                 |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| logging_format             | 6.47 us                                                    | 6.20 us: 1.04x faster                                                 |
| sympy_expand               | 473 ms                                                     | 453 ms: 1.04x faster                                                  |
| xml_etree_process          | 61.2 ms                                                    | 58.6 ms: 1.04x faster                                                 |
| float                      | 78.9 ms                                                    | 75.6 ms: 1.04x faster                                                 |
| sqlite_synth               | 2.99 us                                                    | 2.87 us: 1.04x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                                  |
| sqlglot_normalize          | 110 ms                                                     | 106 ms: 1.04x faster                                                  |
| gc_traversal               | 3.98 ms                                                    | 3.83 ms: 1.04x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 103 ms: 1.04x faster                                                  |
| unpickle_list              | 5.34 us                                                    | 5.15 us: 1.04x faster                                                 |
| mdp                        | 2.79 sec                                                   | 2.69 sec: 1.04x faster                                                |
| dulwich_log                | 67.2 ms                                                    | 64.8 ms: 1.04x faster                                                 |
| typing_runtime_protocols   | 165 us                                                     | 159 us: 1.04x faster                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.03x faster                                                 |
| spectral_norm              | 116 ms                                                     | 112 ms: 1.03x faster                                                  |
| scimark_sor                | 127 ms                                                     | 123 ms: 1.03x faster                                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.78 sec: 1.03x faster                                                |
| xml_etree_generate         | 87.4 ms                                                    | 84.8 ms: 1.03x faster                                                 |
| tomli_loads                | 2.12 sec                                                   | 2.06 sec: 1.03x faster                                                |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                                 |
| async_generators           | 442 ms                                                     | 430 ms: 1.03x faster                                                  |
| pidigits                   | 191 ms                                                     | 187 ms: 1.03x faster                                                  |
| pickle_list                | 5.11 us                                                    | 4.98 us: 1.03x faster                                                 |
| nqueens                    | 81.4 ms                                                    | 79.4 ms: 1.02x faster                                                 |
| comprehensions             | 16.6 us                                                    | 16.2 us: 1.02x faster                                                 |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                                  |
| logging_simple             | 5.74 us                                                    | 5.62 us: 1.02x faster                                                 |
| pyflate                    | 484 ms                                                     | 473 ms: 1.02x faster                                                  |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| nbody                      | 88.3 ms                                                    | 86.7 ms: 1.02x faster                                                 |
| django_template            | 34.8 ms                                                    | 34.2 ms: 1.02x faster                                                 |
| coroutines                 | 23.2 ms                                                    | 22.8 ms: 1.02x faster                                                 |
| hexiom                     | 6.30 ms                                                    | 6.19 ms: 1.02x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.00 ms: 1.02x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 68.2 ms: 1.01x faster                                                 |
| mako                       | 11.2 ms                                                    | 11.1 ms: 1.01x faster                                                 |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                                  |
| raytrace                   | 267 ms                                                     | 264 ms: 1.01x faster                                                  |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                                 |
| fannkuch                   | 402 ms                                                     | 404 ms: 1.01x slower                                                  |
| pycparser                  | 1.16 sec                                                   | 1.17 sec: 1.01x slower                                                |
| regex_dna                  | 221 ms                                                     | 225 ms: 1.02x slower                                                  |
| pickle                     | 11.5 us                                                    | 11.8 us: 1.03x slower                                                 |
| regex_effbot               | 3.67 ms                                                    | 3.89 ms: 1.06x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (7): regex_v8, pickle_pure_python, deltablue, telco, pylint, logging_silent, unpickle
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.00x
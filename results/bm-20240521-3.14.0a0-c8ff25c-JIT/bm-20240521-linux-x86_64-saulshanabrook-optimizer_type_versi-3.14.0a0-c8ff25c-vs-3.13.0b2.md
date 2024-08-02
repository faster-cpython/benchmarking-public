# Results vs. 3.13.0b2

- fork: saulshanabrook
- ref: optimizer_type_versi
- machine: linux-x86_64
- commit hash: c8ff25c
- commit date: 2024-05-21
- overall geometric mean: 1.01x faster
- HPT reliability: 75.74%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 278 ms: 1.02x slower                                                          |
| chameleon      | 7.22 ms                                                    | 7.04 ms: 1.02x faster                                                         |
| docutils       | 2.83 sec                                                   | 2.93 sec: 1.04x slower                                                        |
| html5lib       | 67.2 ms                                                    | 66.3 ms: 1.01x faster                                                         |
| tornado_http   | 94.6 ms                                                    | 97.0 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none_tg         | 336 ms                                                     | 330 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 578 ms: 1.02x faster                                                          |
| Geometric mean             | (ref)                                                      | 1.01x faster                                                                  |

Benchmark hidden because not significant (6): async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_io, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 72.6 ms: 1.09x faster                                                         |
| nbody          | 88.3 ms                                                    | 81.6 ms: 1.08x faster                                                         |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                      | 1.06x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.5 ms: 1.03x faster                                                         |
| regex_compile  | 137 ms                                                     | 138 ms: 1.01x slower                                                          |
| regex_effbot   | 3.67 ms                                                    | 3.71 ms: 1.01x slower                                                         |
| regex_dna      | 221 ms                                                     | 231 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                        |
| xml_etree_parse      | 162 ms                                                     | 152 ms: 1.07x faster                                                          |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.06x faster                                                          |
| xml_etree_generate   | 87.4 ms                                                    | 82.4 ms: 1.06x faster                                                         |
| xml_etree_process    | 61.2 ms                                                    | 58.3 ms: 1.05x faster                                                         |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                         |
| pickle_pure_python   | 305 us                                                     | 302 us: 1.01x faster                                                          |
| json_loads           | 28.9 us                                                    | 28.6 us: 1.01x faster                                                         |
| unpickle_list        | 5.34 us                                                    | 5.37 us: 1.00x slower                                                         |
| unpickle             | 15.1 us                                                    | 15.4 us: 1.02x slower                                                         |
| unpickle_pure_python | 218 us                                                     | 222 us: 1.02x slower                                                          |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                                         |
| pickle_dict          | 34.8 us                                                    | 36.3 us: 1.04x slower                                                         |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                                  |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.9 ms: 1.01x slower                                                         |
| python_startup_no_site | 7.11 ms                                                    | 7.59 ms: 1.07x slower                                                         |
| Geometric mean         | (ref)                                                      | 1.04x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.1 ms: 1.11x faster                                                         |
| django_template | 34.8 ms                                                    | 36.2 ms: 1.04x slower                                                         |
| genshi_text     | 23.7 ms                                                    | 24.9 ms: 1.05x slower                                                         |
| genshi_xml      | 51.6 ms                                                    | 58.0 ms: 1.12x slower                                                         |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| scimark_fft                | 392 ms                                                     | 313 ms: 1.25x faster                                                          |
| richards                   | 50.9 ms                                                    | 41.8 ms: 1.22x faster                                                         |
| richards_super             | 57.4 ms                                                    | 48.0 ms: 1.19x faster                                                         |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.45 ms: 1.18x faster                                                         |
| spectral_norm              | 116 ms                                                     | 100.0 ms: 1.16x faster                                                        |
| crypto_pyaes               | 77.5 ms                                                    | 67.8 ms: 1.14x faster                                                         |
| fannkuch                   | 402 ms                                                     | 356 ms: 1.13x faster                                                          |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.1 ms: 1.11x faster                                                         |
| mako                       | 11.2 ms                                                    | 10.1 ms: 1.11x faster                                                         |
| tomli_loads                | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                        |
| float                      | 78.9 ms                                                    | 72.6 ms: 1.09x faster                                                         |
| nbody                      | 88.3 ms                                                    | 81.6 ms: 1.08x faster                                                         |
| pprint_safe_repr           | 758 ms                                                     | 702 ms: 1.08x faster                                                          |
| pprint_pformat             | 1.56 sec                                                   | 1.44 sec: 1.08x faster                                                        |
| pyflate                    | 484 ms                                                     | 453 ms: 1.07x faster                                                          |
| xml_etree_parse            | 162 ms                                                     | 152 ms: 1.07x faster                                                          |
| gc_traversal               | 3.98 ms                                                    | 3.74 ms: 1.06x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                     | 101 ms: 1.06x faster                                                          |
| xml_etree_generate         | 87.4 ms                                                    | 82.4 ms: 1.06x faster                                                         |
| sqlite_synth               | 2.99 us                                                    | 2.83 us: 1.06x faster                                                         |
| deepcopy_memo              | 39.7 us                                                    | 37.7 us: 1.05x faster                                                         |
| pathlib                    | 17.3 ms                                                    | 16.5 ms: 1.05x faster                                                         |
| xml_etree_process          | 61.2 ms                                                    | 58.3 ms: 1.05x faster                                                         |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                         |
| regex_v8                   | 25.1 ms                                                    | 24.5 ms: 1.03x faster                                                         |
| chameleon                  | 7.22 ms                                                    | 7.04 ms: 1.02x faster                                                         |
| telco                      | 8.41 ms                                                    | 8.22 ms: 1.02x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                    | 3.29 us: 1.02x faster                                                         |
| json                       | 5.31 ms                                                    | 5.21 ms: 1.02x faster                                                         |
| async_tree_none_tg         | 336 ms                                                     | 330 ms: 1.02x faster                                                          |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 578 ms: 1.02x faster                                                          |
| chaos                      | 61.3 ms                                                    | 60.5 ms: 1.01x faster                                                         |
| html5lib                   | 67.2 ms                                                    | 66.3 ms: 1.01x faster                                                         |
| create_gc_cycles           | 1.82 ms                                                    | 1.79 ms: 1.01x faster                                                         |
| sqlglot_parse              | 1.32 ms                                                    | 1.30 ms: 1.01x faster                                                         |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                                          |
| coroutines                 | 23.2 ms                                                    | 22.9 ms: 1.01x faster                                                         |
| logging_format             | 6.47 us                                                    | 6.40 us: 1.01x faster                                                         |
| json_loads                 | 28.9 us                                                    | 28.6 us: 1.01x faster                                                         |
| thrift                     | 823 us                                                     | 816 us: 1.01x faster                                                          |
| logging_simple             | 5.74 us                                                    | 5.70 us: 1.01x faster                                                         |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.00x slower                                                         |
| unpickle_list              | 5.34 us                                                    | 5.37 us: 1.00x slower                                                         |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.85 sec: 1.01x slower                                                        |
| meteor_contest             | 110 ms                                                     | 111 ms: 1.01x slower                                                          |
| regex_compile              | 137 ms                                                     | 138 ms: 1.01x slower                                                          |
| python_startup             | 10.8 ms                                                    | 10.9 ms: 1.01x slower                                                         |
| regex_effbot               | 3.67 ms                                                    | 3.71 ms: 1.01x slower                                                         |
| scimark_lu                 | 122 ms                                                     | 123 ms: 1.01x slower                                                          |
| unpickle                   | 15.1 us                                                    | 15.4 us: 1.02x slower                                                         |
| 2to3                       | 274 ms                                                     | 278 ms: 1.02x slower                                                          |
| dask                       | 369 ms                                                     | 375 ms: 1.02x slower                                                          |
| sqlglot_optimize           | 55.5 ms                                                    | 56.6 ms: 1.02x slower                                                         |
| unpickle_pure_python       | 218 us                                                     | 222 us: 1.02x slower                                                          |
| logging_silent             | 105 ns                                                     | 107 ns: 1.02x slower                                                          |
| pickle                     | 11.5 us                                                    | 11.7 us: 1.02x slower                                                         |
| deepcopy                   | 367 us                                                     | 375 us: 1.02x slower                                                          |
| asyncio_tcp                | 508 ms                                                     | 520 ms: 1.02x slower                                                          |
| flaskblogging              | 9.01 ms                                                    | 9.23 ms: 1.02x slower                                                         |
| tornado_http               | 94.6 ms                                                    | 97.0 ms: 1.02x slower                                                         |
| go                         | 145 ms                                                     | 149 ms: 1.03x slower                                                          |
| dulwich_log                | 67.2 ms                                                    | 69.3 ms: 1.03x slower                                                         |
| sqlglot_normalize          | 110 ms                                                     | 114 ms: 1.03x slower                                                          |
| docutils                   | 2.83 sec                                                   | 2.93 sec: 1.04x slower                                                        |
| bench_thread_pool          | 834 us                                                     | 866 us: 1.04x slower                                                          |
| django_template            | 34.8 ms                                                    | 36.2 ms: 1.04x slower                                                         |
| typing_runtime_protocols   | 165 us                                                     | 172 us: 1.04x slower                                                          |
| pickle_dict                | 34.8 us                                                    | 36.3 us: 1.04x slower                                                         |
| regex_dna                  | 221 ms                                                     | 231 ms: 1.04x slower                                                          |
| async_generators           | 442 ms                                                     | 463 ms: 1.05x slower                                                          |
| raytrace                   | 267 ms                                                     | 280 ms: 1.05x slower                                                          |
| genshi_text                | 23.7 ms                                                    | 24.9 ms: 1.05x slower                                                         |
| nqueens                    | 81.4 ms                                                    | 85.5 ms: 1.05x slower                                                         |
| sympy_str                  | 282 ms                                                     | 302 ms: 1.07x slower                                                          |
| python_startup_no_site     | 7.11 ms                                                    | 7.59 ms: 1.07x slower                                                         |
| sympy_expand               | 473 ms                                                     | 509 ms: 1.08x slower                                                          |
| scimark_sor                | 127 ms                                                     | 138 ms: 1.08x slower                                                          |
| sympy_integrate            | 20.5 ms                                                    | 22.5 ms: 1.10x slower                                                         |
| sympy_sum                  | 156 ms                                                     | 171 ms: 1.10x slower                                                          |
| pylint                     | 317 ms                                                     | 354 ms: 1.11x slower                                                          |
| genshi_xml                 | 51.6 ms                                                    | 58.0 ms: 1.12x slower                                                         |
| deltablue                  | 3.25 ms                                                    | 3.75 ms: 1.15x slower                                                         |
| generators                 | 29.6 ms                                                    | 36.3 ms: 1.23x slower                                                         |
| Geometric mean             | (ref)                                                      | 1.01x faster                                                                  |

Benchmark hidden because not significant (12): async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_io, coverage, pickle_list, async_tree_none, asyncio_websockets, sqlglot_transpile, pycparser, bench_mp_pool
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, djangocms, gunicorn, hexiom, mdp, mypy2

# HPT report

- Reliability score: 75.74% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x
# Results vs. 3.13.0b2

- fork: saulshanabrook
- ref: optimizer_type_versi
- machine: linux-x86_64
- commit hash: 1eabca9
- commit date: 2024-05-22
- overall geometric mean: 1.01x faster
- HPT reliability: 51.77%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 278 ms: 1.02x slower                                                          |
| chameleon      | 7.22 ms                                                    | 7.00 ms: 1.03x faster                                                         |
| docutils       | 2.83 sec                                                   | 2.95 sec: 1.04x slower                                                        |
| tornado_http   | 94.6 ms                                                    | 96.7 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_none, async_tree_memoization_tg, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 81.1 ms: 1.09x faster                                                         |
| float          | 78.9 ms                                                    | 72.5 ms: 1.09x faster                                                         |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                      | 1.06x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.58 ms: 1.03x faster                                                         |
| regex_v8       | 25.1 ms                                                    | 25.0 ms: 1.00x faster                                                         |
| regex_compile  | 137 ms                                                     | 138 ms: 1.01x slower                                                          |
| regex_dna      | 221 ms                                                     | 228 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                      | 1.00x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                                        |
| xml_etree_parse      | 162 ms                                                     | 150 ms: 1.08x faster                                                          |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.07x faster                                                          |
| xml_etree_generate   | 87.4 ms                                                    | 83.1 ms: 1.05x faster                                                         |
| json_dumps           | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                         |
| xml_etree_process    | 61.2 ms                                                    | 58.6 ms: 1.04x faster                                                         |
| unpickle_list        | 5.34 us                                                    | 5.17 us: 1.03x faster                                                         |
| pickle_pure_python   | 305 us                                                     | 296 us: 1.03x faster                                                          |
| json_loads           | 28.9 us                                                    | 28.6 us: 1.01x faster                                                         |
| unpickle_pure_python | 218 us                                                     | 221 us: 1.02x slower                                                          |
| unpickle             | 15.1 us                                                    | 15.4 us: 1.02x slower                                                         |
| pickle_list          | 5.11 us                                                    | 5.36 us: 1.05x slower                                                         |
| pickle_dict          | 34.8 us                                                    | 36.8 us: 1.06x slower                                                         |
| pickle               | 11.5 us                                                    | 12.2 us: 1.07x slower                                                         |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.9 ms: 1.01x slower                                                         |
| python_startup_no_site | 7.11 ms                                                    | 7.62 ms: 1.07x slower                                                         |
| Geometric mean         | (ref)                                                      | 1.04x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.99 ms: 1.12x faster                                                         |
| genshi_text     | 23.7 ms                                                    | 24.4 ms: 1.03x slower                                                         |
| django_template | 34.8 ms                                                    | 36.4 ms: 1.05x slower                                                         |
| genshi_xml      | 51.6 ms                                                    | 56.9 ms: 1.10x slower                                                         |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9 |
|--------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| scimark_fft              | 392 ms                                                     | 311 ms: 1.26x faster                                                          |
| richards                 | 50.9 ms                                                    | 41.7 ms: 1.22x faster                                                         |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.33 ms: 1.22x faster                                                         |
| richards_super           | 57.4 ms                                                    | 48.2 ms: 1.19x faster                                                         |
| crypto_pyaes             | 77.5 ms                                                    | 66.9 ms: 1.16x faster                                                         |
| spectral_norm            | 116 ms                                                     | 101 ms: 1.15x faster                                                          |
| fannkuch                 | 402 ms                                                     | 354 ms: 1.14x faster                                                          |
| mako                     | 11.2 ms                                                    | 9.99 ms: 1.12x faster                                                         |
| scimark_monte_carlo      | 69.2 ms                                                    | 61.9 ms: 1.12x faster                                                         |
| pyflate                  | 484 ms                                                     | 439 ms: 1.10x faster                                                          |
| pprint_safe_repr         | 758 ms                                                     | 694 ms: 1.09x faster                                                          |
| nbody                    | 88.3 ms                                                    | 81.1 ms: 1.09x faster                                                         |
| float                    | 78.9 ms                                                    | 72.5 ms: 1.09x faster                                                         |
| tomli_loads              | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                                        |
| xml_etree_parse          | 162 ms                                                     | 150 ms: 1.08x faster                                                          |
| xml_etree_iterparse      | 107 ms                                                     | 101 ms: 1.07x faster                                                          |
| pprint_pformat           | 1.56 sec                                                   | 1.46 sec: 1.07x faster                                                        |
| deepcopy_memo            | 39.7 us                                                    | 37.3 us: 1.06x faster                                                         |
| xml_etree_generate       | 87.4 ms                                                    | 83.1 ms: 1.05x faster                                                         |
| json_dumps               | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                         |
| pathlib                  | 17.3 ms                                                    | 16.5 ms: 1.05x faster                                                         |
| gc_traversal             | 3.98 ms                                                    | 3.80 ms: 1.05x faster                                                         |
| xml_etree_process        | 61.2 ms                                                    | 58.6 ms: 1.04x faster                                                         |
| sqlite_synth             | 2.99 us                                                    | 2.87 us: 1.04x faster                                                         |
| unpickle_list            | 5.34 us                                                    | 5.17 us: 1.03x faster                                                         |
| pickle_pure_python       | 305 us                                                     | 296 us: 1.03x faster                                                          |
| chameleon                | 7.22 ms                                                    | 7.00 ms: 1.03x faster                                                         |
| chaos                    | 61.3 ms                                                    | 59.6 ms: 1.03x faster                                                         |
| telco                    | 8.41 ms                                                    | 8.19 ms: 1.03x faster                                                         |
| regex_effbot             | 3.67 ms                                                    | 3.58 ms: 1.03x faster                                                         |
| sqlglot_parse            | 1.32 ms                                                    | 1.30 ms: 1.02x faster                                                         |
| pidigits                 | 191 ms                                                     | 188 ms: 1.02x faster                                                          |
| json                     | 5.31 ms                                                    | 5.23 ms: 1.02x faster                                                         |
| pycparser                | 1.16 sec                                                   | 1.14 sec: 1.01x faster                                                        |
| logging_format           | 6.47 us                                                    | 6.39 us: 1.01x faster                                                         |
| json_loads               | 28.9 us                                                    | 28.6 us: 1.01x faster                                                         |
| create_gc_cycles         | 1.82 ms                                                    | 1.80 ms: 1.01x faster                                                         |
| coverage                 | 93.1 ms                                                    | 92.5 ms: 1.01x faster                                                         |
| sqlglot_transpile        | 1.63 ms                                                    | 1.63 ms: 1.01x faster                                                         |
| regex_v8                 | 25.1 ms                                                    | 25.0 ms: 1.00x faster                                                         |
| meteor_contest           | 110 ms                                                     | 109 ms: 1.00x faster                                                          |
| comprehensions           | 16.6 us                                                    | 16.6 us: 1.00x faster                                                         |
| regex_compile            | 137 ms                                                     | 138 ms: 1.01x slower                                                          |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                                        |
| thrift                   | 823 us                                                     | 833 us: 1.01x slower                                                          |
| logging_silent           | 105 ns                                                     | 106 ns: 1.01x slower                                                          |
| python_startup           | 10.8 ms                                                    | 10.9 ms: 1.01x slower                                                         |
| coroutines               | 23.2 ms                                                    | 23.5 ms: 1.01x slower                                                         |
| unpickle_pure_python     | 218 us                                                     | 221 us: 1.02x slower                                                          |
| 2to3                     | 274 ms                                                     | 278 ms: 1.02x slower                                                          |
| unpickle                 | 15.1 us                                                    | 15.4 us: 1.02x slower                                                         |
| go                       | 145 ms                                                     | 147 ms: 1.02x slower                                                          |
| flaskblogging            | 9.01 ms                                                    | 9.18 ms: 1.02x slower                                                         |
| scimark_lu               | 122 ms                                                     | 124 ms: 1.02x slower                                                          |
| dask                     | 369 ms                                                     | 378 ms: 1.02x slower                                                          |
| tornado_http             | 94.6 ms                                                    | 96.7 ms: 1.02x slower                                                         |
| sqlglot_optimize         | 55.5 ms                                                    | 56.8 ms: 1.02x slower                                                         |
| asyncio_tcp              | 508 ms                                                     | 521 ms: 1.03x slower                                                          |
| dulwich_log              | 67.2 ms                                                    | 69.0 ms: 1.03x slower                                                         |
| generators               | 29.6 ms                                                    | 30.5 ms: 1.03x slower                                                         |
| genshi_text              | 23.7 ms                                                    | 24.4 ms: 1.03x slower                                                         |
| regex_dna                | 221 ms                                                     | 228 ms: 1.03x slower                                                          |
| sqlglot_normalize        | 110 ms                                                     | 114 ms: 1.03x slower                                                          |
| bench_thread_pool        | 834 us                                                     | 862 us: 1.03x slower                                                          |
| raytrace                 | 267 ms                                                     | 277 ms: 1.04x slower                                                          |
| async_generators         | 442 ms                                                     | 460 ms: 1.04x slower                                                          |
| docutils                 | 2.83 sec                                                   | 2.95 sec: 1.04x slower                                                        |
| django_template          | 34.8 ms                                                    | 36.4 ms: 1.05x slower                                                         |
| typing_runtime_protocols | 165 us                                                     | 173 us: 1.05x slower                                                          |
| pickle_list              | 5.11 us                                                    | 5.36 us: 1.05x slower                                                         |
| hexiom                   | 6.30 ms                                                    | 6.62 ms: 1.05x slower                                                         |
| pickle_dict              | 34.8 us                                                    | 36.8 us: 1.06x slower                                                         |
| pickle                   | 11.5 us                                                    | 12.2 us: 1.07x slower                                                         |
| sympy_str                | 282 ms                                                     | 301 ms: 1.07x slower                                                          |
| nqueens                  | 81.4 ms                                                    | 86.9 ms: 1.07x slower                                                         |
| python_startup_no_site   | 7.11 ms                                                    | 7.62 ms: 1.07x slower                                                         |
| sympy_expand             | 473 ms                                                     | 511 ms: 1.08x slower                                                          |
| scimark_sor              | 127 ms                                                     | 138 ms: 1.08x slower                                                          |
| sympy_integrate          | 20.5 ms                                                    | 22.5 ms: 1.10x slower                                                         |
| genshi_xml               | 51.6 ms                                                    | 56.9 ms: 1.10x slower                                                         |
| sympy_sum                | 156 ms                                                     | 172 ms: 1.10x slower                                                          |
| pylint                   | 317 ms                                                     | 353 ms: 1.11x slower                                                          |
| deltablue                | 3.25 ms                                                    | 3.69 ms: 1.14x slower                                                         |
| Geometric mean           | (ref)                                                      | 1.01x faster                                                                  |

Benchmark hidden because not significant (15): async_tree_memoization, async_tree_cpu_io_mixed_tg, deepcopy_reduce, html5lib, async_tree_cpu_io_mixed, async_tree_none_tg, deepcopy, asyncio_websockets, mdp, async_tree_none, async_tree_memoization_tg, logging_simple, async_tree_io, bench_mp_pool, async_tree_io_tg
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2

# HPT report

- Reliability score: 51.77% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x
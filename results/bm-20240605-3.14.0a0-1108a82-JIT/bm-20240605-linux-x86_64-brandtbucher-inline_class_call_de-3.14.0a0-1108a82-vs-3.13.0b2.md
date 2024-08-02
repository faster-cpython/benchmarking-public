# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: inline_class_call_de
- machine: linux-x86_64
- commit hash: 1108a82
- commit date: 2024-06-05
- overall geometric mean: 1.00x faster
- HPT reliability: 93.89%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 280 ms: 1.02x slower                                                        |
| docutils       | 2.83 sec                                                   | 2.95 sec: 1.04x slower                                                      |
| html5lib       | 67.2 ms                                                    | 69.3 ms: 1.03x slower                                                       |
| tornado_http   | 94.6 ms                                                    | 97.2 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                      | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 599 ms: 1.02x slower                                                        |
| async_tree_none_tg         | 336 ms                                                     | 343 ms: 1.02x slower                                                        |
| async_tree_io              | 939 ms                                                     | 980 ms: 1.04x slower                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 638 ms: 1.04x slower                                                        |
| Geometric mean             | (ref)                                                      | 1.02x slower                                                                |

Benchmark hidden because not significant (4): async_tree_none, async_tree_io_tg, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 81.4 ms: 1.09x faster                                                       |
| float          | 78.9 ms                                                    | 72.7 ms: 1.09x faster                                                       |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                      | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 137 ms: 1.00x slower                                                        |
| regex_dna      | 221 ms                                                     | 231 ms: 1.04x slower                                                        |
| regex_effbot   | 3.67 ms                                                    | 3.86 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                      | 1.02x slower                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                      |
| xml_etree_parse      | 162 ms                                                     | 150 ms: 1.08x faster                                                        |
| xml_etree_generate   | 87.4 ms                                                    | 82.7 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                     | 102 ms: 1.06x faster                                                        |
| xml_etree_process    | 61.2 ms                                                    | 58.5 ms: 1.05x faster                                                       |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                       |
| pickle_pure_python   | 305 us                                                     | 300 us: 1.02x faster                                                        |
| pickle_dict          | 34.8 us                                                    | 35.1 us: 1.01x slower                                                       |
| unpickle_list        | 5.34 us                                                    | 5.40 us: 1.01x slower                                                       |
| unpickle_pure_python | 218 us                                                     | 222 us: 1.02x slower                                                        |
| json_loads           | 28.9 us                                                    | 29.4 us: 1.02x slower                                                       |
| pickle_list          | 5.11 us                                                    | 5.34 us: 1.05x slower                                                       |
| pickle               | 11.5 us                                                    | 12.2 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.2 ms: 1.04x slower                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.63 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                      | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.1 ms: 1.11x faster                                                       |
| django_template | 34.8 ms                                                    | 36.6 ms: 1.05x slower                                                       |
| genshi_text     | 23.7 ms                                                    | 25.1 ms: 1.06x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 58.9 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| scimark_fft                | 392 ms                                                     | 314 ms: 1.25x faster                                                        |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.33 ms: 1.22x faster                                                       |
| richards                   | 50.9 ms                                                    | 42.2 ms: 1.21x faster                                                       |
| richards_super             | 57.4 ms                                                    | 48.5 ms: 1.18x faster                                                       |
| crypto_pyaes               | 77.5 ms                                                    | 67.4 ms: 1.15x faster                                                       |
| fannkuch                   | 402 ms                                                     | 355 ms: 1.13x faster                                                        |
| spectral_norm              | 116 ms                                                     | 104 ms: 1.12x faster                                                        |
| mako                       | 11.2 ms                                                    | 10.1 ms: 1.11x faster                                                       |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.6 ms: 1.10x faster                                                       |
| tomli_loads                | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                      |
| nbody                      | 88.3 ms                                                    | 81.4 ms: 1.09x faster                                                       |
| float                      | 78.9 ms                                                    | 72.7 ms: 1.09x faster                                                       |
| pprint_safe_repr           | 758 ms                                                     | 701 ms: 1.08x faster                                                        |
| mdp                        | 2.79 sec                                                   | 2.58 sec: 1.08x faster                                                      |
| xml_etree_parse            | 162 ms                                                     | 150 ms: 1.08x faster                                                        |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                                      |
| xml_etree_generate         | 87.4 ms                                                    | 82.7 ms: 1.06x faster                                                       |
| gc_traversal               | 3.98 ms                                                    | 3.76 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                     | 102 ms: 1.06x faster                                                        |
| sqlite_synth               | 2.99 us                                                    | 2.84 us: 1.05x faster                                                       |
| pyflate                    | 484 ms                                                     | 460 ms: 1.05x faster                                                        |
| xml_etree_process          | 61.2 ms                                                    | 58.5 ms: 1.05x faster                                                       |
| telco                      | 8.41 ms                                                    | 8.05 ms: 1.05x faster                                                       |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                       |
| deepcopy_memo              | 39.7 us                                                    | 38.1 us: 1.04x faster                                                       |
| pathlib                    | 17.3 ms                                                    | 16.7 ms: 1.04x faster                                                       |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                                       |
| pickle_pure_python         | 305 us                                                     | 300 us: 1.02x faster                                                        |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                                        |
| chaos                      | 61.3 ms                                                    | 60.3 ms: 1.02x faster                                                       |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                                        |
| thrift                     | 823 us                                                     | 813 us: 1.01x faster                                                        |
| sqlglot_parse              | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.80 ms: 1.01x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                    | 3.32 us: 1.01x faster                                                       |
| regex_compile              | 137 ms                                                     | 137 ms: 1.00x slower                                                        |
| json                       | 5.31 ms                                                    | 5.34 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.65 ms: 1.01x slower                                                       |
| pickle_dict                | 34.8 us                                                    | 35.1 us: 1.01x slower                                                       |
| unpickle_list              | 5.34 us                                                    | 5.40 us: 1.01x slower                                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                                      |
| unpickle_pure_python       | 218 us                                                     | 222 us: 1.02x slower                                                        |
| json_loads                 | 28.9 us                                                    | 29.4 us: 1.02x slower                                                       |
| dulwich_log                | 67.2 ms                                                    | 68.5 ms: 1.02x slower                                                       |
| 2to3                       | 274 ms                                                     | 280 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 599 ms: 1.02x slower                                                        |
| async_tree_none_tg         | 336 ms                                                     | 343 ms: 1.02x slower                                                        |
| asyncio_tcp                | 508 ms                                                     | 519 ms: 1.02x slower                                                        |
| logging_silent             | 105 ns                                                     | 107 ns: 1.02x slower                                                        |
| dask                       | 369 ms                                                     | 379 ms: 1.03x slower                                                        |
| sqlglot_optimize           | 55.5 ms                                                    | 57.0 ms: 1.03x slower                                                       |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.03x slower                                                        |
| tornado_http               | 94.6 ms                                                    | 97.2 ms: 1.03x slower                                                       |
| go                         | 145 ms                                                     | 149 ms: 1.03x slower                                                        |
| html5lib                   | 67.2 ms                                                    | 69.3 ms: 1.03x slower                                                       |
| deepcopy                   | 367 us                                                     | 379 us: 1.03x slower                                                        |
| generators                 | 29.6 ms                                                    | 30.6 ms: 1.03x slower                                                       |
| scimark_sor                | 127 ms                                                     | 133 ms: 1.04x slower                                                        |
| pycparser                  | 1.16 sec                                                   | 1.21 sec: 1.04x slower                                                      |
| scimark_lu                 | 122 ms                                                     | 127 ms: 1.04x slower                                                        |
| python_startup             | 10.8 ms                                                    | 11.2 ms: 1.04x slower                                                       |
| docutils                   | 2.83 sec                                                   | 2.95 sec: 1.04x slower                                                      |
| async_tree_io              | 939 ms                                                     | 980 ms: 1.04x slower                                                        |
| regex_dna                  | 221 ms                                                     | 231 ms: 1.04x slower                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 638 ms: 1.04x slower                                                        |
| pickle_list                | 5.11 us                                                    | 5.34 us: 1.05x slower                                                       |
| bench_thread_pool          | 834 us                                                     | 875 us: 1.05x slower                                                        |
| regex_effbot               | 3.67 ms                                                    | 3.86 ms: 1.05x slower                                                       |
| django_template            | 34.8 ms                                                    | 36.6 ms: 1.05x slower                                                       |
| async_generators           | 442 ms                                                     | 466 ms: 1.05x slower                                                        |
| typing_runtime_protocols   | 165 us                                                     | 174 us: 1.06x slower                                                        |
| genshi_text                | 23.7 ms                                                    | 25.1 ms: 1.06x slower                                                       |
| pickle                     | 11.5 us                                                    | 12.2 us: 1.06x slower                                                       |
| raytrace                   | 267 ms                                                     | 283 ms: 1.06x slower                                                        |
| hexiom                     | 6.30 ms                                                    | 6.70 ms: 1.06x slower                                                       |
| sympy_str                  | 282 ms                                                     | 302 ms: 1.07x slower                                                        |
| python_startup_no_site     | 7.11 ms                                                    | 7.63 ms: 1.07x slower                                                       |
| sympy_expand               | 473 ms                                                     | 510 ms: 1.08x slower                                                        |
| nqueens                    | 81.4 ms                                                    | 88.1 ms: 1.08x slower                                                       |
| sympy_integrate            | 20.5 ms                                                    | 22.5 ms: 1.10x slower                                                       |
| sympy_sum                  | 156 ms                                                     | 172 ms: 1.10x slower                                                        |
| pylint                     | 317 ms                                                     | 352 ms: 1.11x slower                                                        |
| genshi_xml                 | 51.6 ms                                                    | 58.9 ms: 1.14x slower                                                       |
| deltablue                  | 3.25 ms                                                    | 3.75 ms: 1.15x slower                                                       |
| Geometric mean             | (ref)                                                      | 1.00x faster                                                                |

Benchmark hidden because not significant (12): logging_format, regex_v8, logging_simple, comprehensions, asyncio_websockets, coverage, bench_mp_pool, async_tree_none, unpickle, async_tree_io_tg, async_tree_memoization_tg, async_tree_memoization
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 93.89% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x
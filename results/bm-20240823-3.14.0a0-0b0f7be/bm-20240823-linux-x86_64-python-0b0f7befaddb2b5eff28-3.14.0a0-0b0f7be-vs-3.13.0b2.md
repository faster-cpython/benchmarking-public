# Results vs. 3.13.0b2

- fork: python
- ref: 0b0f7befaddb2b5eff28
- machine: linux-x86_64
- commit hash: 0b0f7be
- commit date: 2024-08-23
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 254 ms: 1.08x faster                                                  |
| docutils       | 2.83 sec                                                   | 2.70 sec: 1.05x faster                                                |
| html5lib       | 67.2 ms                                                    | 65.6 ms: 1.03x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 90.4 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                      | 1.05x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 391 ms: 1.18x faster                                                  |
| async_tree_none            | 378 ms                                                     | 322 ms: 1.18x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 402 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 555 ms: 1.10x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 537 ms: 1.09x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 895 ms: 1.05x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                          |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| float          | 78.9 ms                                                    | 77.3 ms: 1.02x faster                                                 |
| nbody          | 88.3 ms                                                    | 86.9 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 128 ms: 1.07x faster                                                  |
| regex_v8       | 25.1 ms                                                    | 24.5 ms: 1.02x faster                                                 |
| regex_effbot   | 3.67 ms                                                    | 3.63 ms: 1.01x faster                                                 |
| regex_dna      | 221 ms                                                     | 220 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 61.2 ms                                                    | 58.4 ms: 1.05x faster                                                 |
| xml_etree_parse      | 162 ms                                                     | 155 ms: 1.05x faster                                                  |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 84.5 ms: 1.04x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 212 us: 1.03x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.03x faster                                                  |
| tomli_loads          | 2.12 sec                                                   | 2.07 sec: 1.02x faster                                                |
| json_loads           | 28.9 us                                                    | 28.3 us: 1.02x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 302 us: 1.01x faster                                                  |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.07 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.6 ms: 1.05x faster                                                 |
| genshi_xml      | 51.6 ms                                                    | 49.8 ms: 1.04x faster                                                 |
| django_template | 34.8 ms                                                    | 34.1 ms: 1.02x faster                                                 |
| mako            | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.02x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 259 us: 1.42x faster                                                  |
| deepcopy_memo              | 39.7 us                                                    | 29.6 us: 1.34x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.67 us: 1.25x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 391 ms: 1.18x faster                                                  |
| async_tree_none            | 378 ms                                                     | 322 ms: 1.18x faster                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.72 ms: 1.12x faster                                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 402 ms: 1.10x faster                                                  |
| richards                   | 50.9 ms                                                    | 46.1 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 555 ms: 1.10x faster                                                  |
| richards_super             | 57.4 ms                                                    | 52.1 ms: 1.10x faster                                                 |
| scimark_fft                | 392 ms                                                     | 358 ms: 1.10x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.09x faster                                                  |
| coverage                   | 93.1 ms                                                    | 85.1 ms: 1.09x faster                                                 |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 537 ms: 1.09x faster                                                  |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.08x faster                                                  |
| mdp                        | 2.79 sec                                                   | 2.58 sec: 1.08x faster                                                |
| 2to3                       | 274 ms                                                     | 254 ms: 1.08x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 71.9 ms: 1.08x faster                                                 |
| gc_traversal               | 3.98 ms                                                    | 3.72 ms: 1.07x faster                                                 |
| regex_compile              | 137 ms                                                     | 128 ms: 1.07x faster                                                  |
| sympy_sum                  | 156 ms                                                     | 147 ms: 1.06x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 785 us: 1.06x faster                                                  |
| sympy_str                  | 282 ms                                                     | 266 ms: 1.06x faster                                                  |
| generators                 | 29.6 ms                                                    | 27.9 ms: 1.06x faster                                                 |
| thrift                     | 823 us                                                     | 777 us: 1.06x faster                                                  |
| asyncio_tcp                | 508 ms                                                     | 482 ms: 1.05x faster                                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                                |
| spectral_norm              | 116 ms                                                     | 110 ms: 1.05x faster                                                  |
| pprint_safe_repr           | 758 ms                                                     | 722 ms: 1.05x faster                                                  |
| sympy_integrate            | 20.5 ms                                                    | 19.5 ms: 1.05x faster                                                 |
| logging_format             | 6.47 us                                                    | 6.17 us: 1.05x faster                                                 |
| docutils                   | 2.83 sec                                                   | 2.70 sec: 1.05x faster                                                |
| xml_etree_process          | 61.2 ms                                                    | 58.4 ms: 1.05x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 155 ms: 1.05x faster                                                  |
| tornado_http               | 94.6 ms                                                    | 90.4 ms: 1.05x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 895 ms: 1.05x faster                                                  |
| genshi_text                | 23.7 ms                                                    | 22.6 ms: 1.05x faster                                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.81 sec: 1.05x faster                                                |
| chaos                      | 61.3 ms                                                    | 58.8 ms: 1.04x faster                                                 |
| logging_simple             | 5.74 us                                                    | 5.51 us: 1.04x faster                                                 |
| typing_runtime_protocols   | 165 us                                                     | 158 us: 1.04x faster                                                  |
| logging_silent             | 105 ns                                                     | 101 ns: 1.04x faster                                                  |
| sympy_expand               | 473 ms                                                     | 454 ms: 1.04x faster                                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 53.4 ms: 1.04x faster                                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 1.57 ms: 1.04x faster                                                 |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| genshi_xml                 | 51.6 ms                                                    | 49.8 ms: 1.04x faster                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 84.5 ms: 1.04x faster                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                                 |
| nqueens                    | 81.4 ms                                                    | 78.8 ms: 1.03x faster                                                 |
| telco                      | 8.41 ms                                                    | 8.15 ms: 1.03x faster                                                 |
| pyflate                    | 484 ms                                                     | 470 ms: 1.03x faster                                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                |
| unpickle_pure_python       | 218 us                                                     | 212 us: 1.03x faster                                                  |
| hexiom                     | 6.30 ms                                                    | 6.13 ms: 1.03x faster                                                 |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.03x faster                                                  |
| raytrace                   | 267 ms                                                     | 260 ms: 1.03x faster                                                  |
| html5lib                   | 67.2 ms                                                    | 65.6 ms: 1.03x faster                                                 |
| regex_v8                   | 25.1 ms                                                    | 24.5 ms: 1.02x faster                                                 |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                                  |
| sqlglot_normalize          | 110 ms                                                     | 108 ms: 1.02x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 2.07 sec: 1.02x faster                                                |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.6 ms: 1.02x faster                                                 |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| deltablue                  | 3.25 ms                                                    | 3.18 ms: 1.02x faster                                                 |
| async_generators           | 442 ms                                                     | 433 ms: 1.02x faster                                                  |
| django_template            | 34.8 ms                                                    | 34.1 ms: 1.02x faster                                                 |
| float                      | 78.9 ms                                                    | 77.3 ms: 1.02x faster                                                 |
| json_loads                 | 28.9 us                                                    | 28.3 us: 1.02x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                                  |
| nbody                      | 88.3 ms                                                    | 86.9 ms: 1.02x faster                                                 |
| comprehensions             | 16.6 us                                                    | 16.3 us: 1.02x faster                                                 |
| coroutines                 | 23.2 ms                                                    | 22.8 ms: 1.02x faster                                                 |
| regex_effbot               | 3.67 ms                                                    | 3.63 ms: 1.01x faster                                                 |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                                  |
| scimark_sor                | 127 ms                                                     | 126 ms: 1.01x faster                                                  |
| fannkuch                   | 402 ms                                                     | 398 ms: 1.01x faster                                                  |
| regex_dna                  | 221 ms                                                     | 220 ms: 1.01x faster                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.07 ms: 1.00x faster                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| mako                       | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                                 |
| go                         | 145 ms                                                     | 161 ms: 1.11x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (4): pycparser, async_tree_io, json, pylint
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.01x
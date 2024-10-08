# Results vs. 3.13.0b2

- fork: python
- ref: a4fd7aa4a6420cef1c22
- machine: linux-x86_64
- commit hash: a4fd7aa
- commit date: 2024-08-21
- overall geometric mean: 1.04x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 264 ms: 1.04x faster                                                  |
| docutils       | 2.83 sec                                                   | 2.70 sec: 1.05x faster                                                |
| html5lib       | 67.2 ms                                                    | 63.6 ms: 1.06x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 90.5 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                      | 1.05x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 394 ms: 1.17x faster                                                  |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 404 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 311 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 548 ms: 1.07x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 905 ms: 1.03x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                          |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| nbody          | 88.3 ms                                                    | 86.7 ms: 1.02x faster                                                 |
| float          | 78.9 ms                                                    | 78.1 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 129 ms: 1.06x faster                                                  |
| regex_dna      | 221 ms                                                     | 223 ms: 1.01x slower                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                                 |
| regex_v8       | 25.1 ms                                                    | 26.2 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 155 ms: 1.04x faster                                                  |
| xml_etree_process    | 61.2 ms                                                    | 58.9 ms: 1.04x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 85.0 ms: 1.03x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                                 |
| tomli_loads          | 2.12 sec                                                   | 2.08 sec: 1.02x faster                                                |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                                  |
| json_loads           | 28.9 us                                                    | 28.4 us: 1.02x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 106 ms: 1.02x faster                                                  |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.5 ms: 1.05x faster                                                 |
| genshi_xml      | 51.6 ms                                                    | 49.9 ms: 1.03x faster                                                 |
| django_template | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                                 |
| Geometric mean  | (ref)                                                      | 1.03x faster                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 262 us: 1.40x faster                                                  |
| deepcopy_memo              | 39.7 us                                                    | 29.8 us: 1.33x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.66 us: 1.26x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 394 ms: 1.17x faster                                                  |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                  |
| mdp                        | 2.79 sec                                                   | 2.53 sec: 1.10x faster                                                |
| async_tree_memoization_tg  | 444 ms                                                     | 404 ms: 1.10x faster                                                  |
| coverage                   | 93.1 ms                                                    | 85.7 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 311 ms: 1.08x faster                                                  |
| richards_super             | 57.4 ms                                                    | 53.3 ms: 1.08x faster                                                 |
| richards                   | 50.9 ms                                                    | 47.4 ms: 1.07x faster                                                 |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.07x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 548 ms: 1.07x faster                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.92 ms: 1.07x faster                                                 |
| asyncio_tcp                | 508 ms                                                     | 474 ms: 1.07x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 72.5 ms: 1.07x faster                                                 |
| scimark_lu                 | 122 ms                                                     | 114 ms: 1.07x faster                                                  |
| scimark_fft                | 392 ms                                                     | 368 ms: 1.07x faster                                                  |
| regex_compile              | 137 ms                                                     | 129 ms: 1.06x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 789 us: 1.06x faster                                                  |
| html5lib                   | 67.2 ms                                                    | 63.6 ms: 1.06x faster                                                 |
| thrift                     | 823 us                                                     | 779 us: 1.06x faster                                                  |
| logging_format             | 6.47 us                                                    | 6.13 us: 1.06x faster                                                 |
| generators                 | 29.6 ms                                                    | 28.1 ms: 1.05x faster                                                 |
| sympy_str                  | 282 ms                                                     | 268 ms: 1.05x faster                                                  |
| sympy_sum                  | 156 ms                                                     | 148 ms: 1.05x faster                                                  |
| logging_simple             | 5.74 us                                                    | 5.47 us: 1.05x faster                                                 |
| genshi_text                | 23.7 ms                                                    | 22.5 ms: 1.05x faster                                                 |
| docutils                   | 2.83 sec                                                   | 2.70 sec: 1.05x faster                                                |
| tornado_http               | 94.6 ms                                                    | 90.5 ms: 1.05x faster                                                 |
| sympy_integrate            | 20.5 ms                                                    | 19.7 ms: 1.04x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 155 ms: 1.04x faster                                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 53.4 ms: 1.04x faster                                                 |
| xml_etree_process          | 61.2 ms                                                    | 58.9 ms: 1.04x faster                                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.84 sec: 1.04x faster                                                |
| 2to3                       | 274 ms                                                     | 264 ms: 1.04x faster                                                  |
| pyflate                    | 484 ms                                                     | 466 ms: 1.04x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 905 ms: 1.03x faster                                                  |
| sympy_expand               | 473 ms                                                     | 457 ms: 1.03x faster                                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.78 sec: 1.03x faster                                                |
| genshi_xml                 | 51.6 ms                                                    | 49.9 ms: 1.03x faster                                                 |
| telco                      | 8.41 ms                                                    | 8.16 ms: 1.03x faster                                                 |
| gc_traversal               | 3.98 ms                                                    | 3.86 ms: 1.03x faster                                                 |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                 |
| chaos                      | 61.3 ms                                                    | 59.6 ms: 1.03x faster                                                 |
| django_template            | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                                 |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                                |
| xml_etree_generate         | 87.4 ms                                                    | 85.0 ms: 1.03x faster                                                 |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                                  |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                                 |
| async_generators           | 442 ms                                                     | 432 ms: 1.02x faster                                                  |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| nqueens                    | 81.4 ms                                                    | 79.7 ms: 1.02x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.60 ms: 1.02x faster                                                 |
| pprint_safe_repr           | 758 ms                                                     | 743 ms: 1.02x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 2.08 sec: 1.02x faster                                                |
| unpickle_pure_python       | 218 us                                                     | 214 us: 1.02x faster                                                  |
| nbody                      | 88.3 ms                                                    | 86.7 ms: 1.02x faster                                                 |
| json_loads                 | 28.9 us                                                    | 28.4 us: 1.02x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 106 ms: 1.02x faster                                                  |
| go                         | 145 ms                                                     | 142 ms: 1.02x faster                                                  |
| spectral_norm              | 116 ms                                                     | 114 ms: 1.01x faster                                                  |
| typing_runtime_protocols   | 165 us                                                     | 162 us: 1.01x faster                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 68.3 ms: 1.01x faster                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.30 ms: 1.01x faster                                                 |
| raytrace                   | 267 ms                                                     | 264 ms: 1.01x faster                                                  |
| scimark_sor                | 127 ms                                                     | 126 ms: 1.01x faster                                                  |
| float                      | 78.9 ms                                                    | 78.1 ms: 1.01x faster                                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                                 |
| regex_dna                  | 221 ms                                                     | 223 ms: 1.01x slower                                                  |
| fannkuch                   | 402 ms                                                     | 407 ms: 1.01x slower                                                  |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.03x slower                                                |
| regex_effbot               | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                                 |
| regex_v8                   | 25.1 ms                                                    | 26.2 ms: 1.04x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                          |

Benchmark hidden because not significant (11): meteor_contest, async_tree_io, coroutines, mako, logging_silent, comprehensions, hexiom, deltablue, json, pickle_pure_python, pylint
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x
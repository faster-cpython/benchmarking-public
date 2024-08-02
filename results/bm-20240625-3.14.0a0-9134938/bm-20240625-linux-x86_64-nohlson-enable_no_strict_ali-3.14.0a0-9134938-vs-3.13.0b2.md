# Results vs. 3.13.0b2

- fork: nohlson
- ref: enable_no_strict_ali
- machine: linux-x86_64
- commit hash: 9134938
- commit date: 2024-06-25
- overall geometric mean: 1.04x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 264 ms: 1.04x faster                                                   |
| docutils       | 2.83 sec                                                   | 2.72 sec: 1.04x faster                                                 |
| html5lib       | 67.2 ms                                                    | 65.9 ms: 1.02x faster                                                  |
| tornado_http   | 94.6 ms                                                    | 90.0 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                      | 1.04x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 377 ms: 1.18x faster                                                   |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 411 ms: 1.13x faster                                                   |
| async_tree_io_tg           | 936 ms                                                     | 845 ms: 1.11x faster                                                   |
| async_tree_io              | 939 ms                                                     | 859 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 543 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 571 ms: 1.07x faster                                                   |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                   |
| float          | 78.9 ms                                                    | 78.5 ms: 1.00x faster                                                  |
| nbody          | 88.3 ms                                                    | 92.0 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 133 ms: 1.03x faster                                                   |
| regex_dna      | 221 ms                                                     | 222 ms: 1.00x slower                                                   |
| regex_v8       | 25.1 ms                                                    | 25.2 ms: 1.00x slower                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                      | 1.00x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                     | 104 ms: 1.03x faster                                                   |
| xml_etree_parse      | 162 ms                                                     | 157 ms: 1.03x faster                                                   |
| json_loads           | 28.9 us                                                    | 28.2 us: 1.02x faster                                                  |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.02x faster                                                   |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                  |
| xml_etree_process    | 61.2 ms                                                    | 60.3 ms: 1.01x faster                                                  |
| xml_etree_generate   | 87.4 ms                                                    | 86.4 ms: 1.01x faster                                                  |
| unpickle_list        | 5.34 us                                                    | 5.28 us: 1.01x faster                                                  |
| tomli_loads          | 2.12 sec                                                   | 2.11 sec: 1.00x faster                                                 |
| pickle_dict          | 34.8 us                                                    | 35.3 us: 1.01x slower                                                  |
| pickle_list          | 5.11 us                                                    | 5.19 us: 1.02x slower                                                  |
| pickle               | 11.5 us                                                    | 11.8 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                           |

Benchmark hidden because not significant (2): unpickle, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                  |
| python_startup_no_site | 7.11 ms                                                    | 7.04 ms: 1.01x faster                                                  |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.8 ms                                                    | 33.9 ms: 1.03x faster                                                  |
| mako            | 11.2 ms                                                    | 11.4 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 265 us: 1.38x faster                                                   |
| deepcopy_memo              | 39.7 us                                                    | 30.5 us: 1.30x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                    | 2.74 us: 1.22x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 377 ms: 1.18x faster                                                   |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 411 ms: 1.13x faster                                                   |
| mdp                        | 2.79 sec                                                   | 2.49 sec: 1.12x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 845 ms: 1.11x faster                                                   |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.09x faster                                                  |
| async_tree_io              | 939 ms                                                     | 859 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 543 ms: 1.08x faster                                                   |
| logging_format             | 6.47 us                                                    | 6.02 us: 1.07x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 571 ms: 1.07x faster                                                   |
| asyncio_tcp                | 508 ms                                                     | 475 ms: 1.07x faster                                                   |
| gc_traversal               | 3.98 ms                                                    | 3.72 ms: 1.07x faster                                                  |
| richards                   | 50.9 ms                                                    | 47.7 ms: 1.07x faster                                                  |
| richards_super             | 57.4 ms                                                    | 53.9 ms: 1.06x faster                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.96 ms: 1.06x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 788 us: 1.06x faster                                                   |
| crypto_pyaes               | 77.5 ms                                                    | 73.3 ms: 1.06x faster                                                  |
| tornado_http               | 94.6 ms                                                    | 90.0 ms: 1.05x faster                                                  |
| scimark_lu                 | 122 ms                                                     | 116 ms: 1.05x faster                                                   |
| scimark_fft                | 392 ms                                                     | 374 ms: 1.05x faster                                                   |
| spectral_norm              | 116 ms                                                     | 111 ms: 1.05x faster                                                   |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.05x faster                                                  |
| logging_simple             | 5.74 us                                                    | 5.50 us: 1.04x faster                                                  |
| dulwich_log                | 67.2 ms                                                    | 64.4 ms: 1.04x faster                                                  |
| pyflate                    | 484 ms                                                     | 465 ms: 1.04x faster                                                   |
| thrift                     | 823 us                                                     | 791 us: 1.04x faster                                                   |
| chaos                      | 61.3 ms                                                    | 59.0 ms: 1.04x faster                                                  |
| docutils                   | 2.83 sec                                                   | 2.72 sec: 1.04x faster                                                 |
| 2to3                       | 274 ms                                                     | 264 ms: 1.04x faster                                                   |
| dask                       | 369 ms                                                     | 356 ms: 1.04x faster                                                   |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.78 sec: 1.03x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 104 ms: 1.03x faster                                                   |
| xml_etree_parse            | 162 ms                                                     | 157 ms: 1.03x faster                                                   |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.1 ms: 1.03x faster                                                  |
| scimark_sor                | 127 ms                                                     | 124 ms: 1.03x faster                                                   |
| async_generators           | 442 ms                                                     | 429 ms: 1.03x faster                                                   |
| regex_compile              | 137 ms                                                     | 133 ms: 1.03x faster                                                   |
| django_template            | 34.8 ms                                                    | 33.9 ms: 1.03x faster                                                  |
| sympy_str                  | 282 ms                                                     | 275 ms: 1.03x faster                                                   |
| sqlite_synth               | 2.99 us                                                    | 2.91 us: 1.03x faster                                                  |
| sympy_sum                  | 156 ms                                                     | 152 ms: 1.03x faster                                                   |
| logging_silent             | 105 ns                                                     | 102 ns: 1.03x faster                                                   |
| sympy_integrate            | 20.5 ms                                                    | 20.0 ms: 1.03x faster                                                  |
| nqueens                    | 81.4 ms                                                    | 79.4 ms: 1.03x faster                                                  |
| json_loads                 | 28.9 us                                                    | 28.2 us: 1.02x faster                                                  |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.02x faster                                                   |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.60 ms: 1.02x faster                                                  |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                                   |
| html5lib                   | 67.2 ms                                                    | 65.9 ms: 1.02x faster                                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 54.5 ms: 1.02x faster                                                  |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                                   |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                                   |
| sqlglot_parse              | 1.32 ms                                                    | 1.30 ms: 1.02x faster                                                  |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.95 sec: 1.01x faster                                                 |
| xml_etree_process          | 61.2 ms                                                    | 60.3 ms: 1.01x faster                                                  |
| xml_etree_generate         | 87.4 ms                                                    | 86.4 ms: 1.01x faster                                                  |
| unpickle_list              | 5.34 us                                                    | 5.28 us: 1.01x faster                                                  |
| sqlglot_normalize          | 110 ms                                                     | 109 ms: 1.01x faster                                                   |
| json                       | 5.31 ms                                                    | 5.25 ms: 1.01x faster                                                  |
| telco                      | 8.41 ms                                                    | 8.33 ms: 1.01x faster                                                  |
| go                         | 145 ms                                                     | 143 ms: 1.01x faster                                                   |
| fannkuch                   | 402 ms                                                     | 398 ms: 1.01x faster                                                   |
| python_startup_no_site     | 7.11 ms                                                    | 7.04 ms: 1.01x faster                                                  |
| generators                 | 29.6 ms                                                    | 29.4 ms: 1.01x faster                                                  |
| hexiom                     | 6.30 ms                                                    | 6.26 ms: 1.01x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 2.11 sec: 1.00x faster                                                 |
| float                      | 78.9 ms                                                    | 78.5 ms: 1.00x faster                                                  |
| regex_dna                  | 221 ms                                                     | 222 ms: 1.00x slower                                                   |
| pprint_safe_repr           | 758 ms                                                     | 761 ms: 1.00x slower                                                   |
| regex_v8                   | 25.1 ms                                                    | 25.2 ms: 1.00x slower                                                  |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                  |
| raytrace                   | 267 ms                                                     | 268 ms: 1.01x slower                                                   |
| deltablue                  | 3.25 ms                                                    | 3.27 ms: 1.01x slower                                                  |
| regex_effbot               | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                                  |
| pickle_dict                | 34.8 us                                                    | 35.3 us: 1.01x slower                                                  |
| pickle_list                | 5.11 us                                                    | 5.19 us: 1.02x slower                                                  |
| mako                       | 11.2 ms                                                    | 11.4 ms: 1.02x slower                                                  |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                                 |
| pickle                     | 11.5 us                                                    | 11.8 us: 1.03x slower                                                  |
| nbody                      | 88.3 ms                                                    | 92.0 ms: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                           |

Benchmark hidden because not significant (11): pylint, typing_runtime_protocols, genshi_xml, sympy_expand, unpickle, coverage, pickle_pure_python, genshi_text, comprehensions, pprint_pformat, coroutines
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.00x
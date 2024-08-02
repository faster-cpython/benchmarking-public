# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: call_list_append
- machine: linux-x86_64
- commit hash: d7c7f4c
- commit date: 2024-06-06
- overall geometric mean: 1.00x faster
- HPT reliability: 82.24%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 281 ms: 1.02x slower                                                    |
| docutils       | 2.83 sec                                                   | 2.95 sec: 1.04x slower                                                  |
| html5lib       | 67.2 ms                                                    | 68.4 ms: 1.02x slower                                                   |
| tornado_http   | 94.6 ms                                                    | 97.1 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                      | 1.03x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 336 ms                                                     | 343 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 602 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 640 ms: 1.05x slower                                                    |
| async_tree_io              | 939 ms                                                     | 999 ms: 1.06x slower                                                    |
| Geometric mean             | (ref)                                                      | 1.02x slower                                                            |

Benchmark hidden because not significant (4): async_tree_io_tg, async_tree_memoization_tg, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 72.6 ms: 1.09x faster                                                   |
| nbody          | 88.3 ms                                                    | 82.5 ms: 1.07x faster                                                   |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                      | 1.06x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.56 ms: 1.03x faster                                                   |
| regex_v8       | 25.1 ms                                                    | 25.0 ms: 1.01x faster                                                   |
| regex_dna      | 221 ms                                                     | 222 ms: 1.00x slower                                                    |
| regex_compile  | 137 ms                                                     | 138 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                      | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                                  |
| xml_etree_parse      | 162 ms                                                     | 150 ms: 1.08x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.07x faster                                                    |
| xml_etree_generate   | 87.4 ms                                                    | 82.0 ms: 1.07x faster                                                   |
| xml_etree_process    | 61.2 ms                                                    | 57.7 ms: 1.06x faster                                                   |
| json_dumps           | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                   |
| pickle_dict          | 34.8 us                                                    | 34.7 us: 1.00x faster                                                   |
| unpickle_list        | 5.34 us                                                    | 5.37 us: 1.00x slower                                                   |
| pickle_list          | 5.11 us                                                    | 5.14 us: 1.01x slower                                                   |
| unpickle_pure_python | 218 us                                                     | 225 us: 1.03x slower                                                    |
| unpickle             | 15.1 us                                                    | 15.6 us: 1.03x slower                                                   |
| pickle               | 11.5 us                                                    | 12.0 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                            |

Benchmark hidden because not significant (2): json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.1 ms: 1.04x slower                                                   |
| python_startup_no_site | 7.11 ms                                                    | 7.60 ms: 1.07x slower                                                   |
| Geometric mean         | (ref)                                                      | 1.05x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.1 ms: 1.12x faster                                                   |
| genshi_text     | 23.7 ms                                                    | 25.0 ms: 1.05x slower                                                   |
| django_template | 34.8 ms                                                    | 37.3 ms: 1.07x slower                                                   |
| genshi_xml      | 51.6 ms                                                    | 58.9 ms: 1.14x slower                                                   |
| Geometric mean  | (ref)                                                      | 1.04x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| richards                   | 50.9 ms                                                    | 41.8 ms: 1.22x faster                                                   |
| scimark_fft                | 392 ms                                                     | 324 ms: 1.21x faster                                                    |
| richards_super             | 57.4 ms                                                    | 48.4 ms: 1.18x faster                                                   |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.64 ms: 1.13x faster                                                   |
| fannkuch                   | 402 ms                                                     | 356 ms: 1.13x faster                                                    |
| mako                       | 11.2 ms                                                    | 10.1 ms: 1.12x faster                                                   |
| crypto_pyaes               | 77.5 ms                                                    | 70.2 ms: 1.10x faster                                                   |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.8 ms: 1.10x faster                                                   |
| spectral_norm              | 116 ms                                                     | 106 ms: 1.10x faster                                                    |
| float                      | 78.9 ms                                                    | 72.6 ms: 1.09x faster                                                   |
| pyflate                    | 484 ms                                                     | 446 ms: 1.09x faster                                                    |
| tomli_loads                | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                                  |
| mdp                        | 2.79 sec                                                   | 2.58 sec: 1.08x faster                                                  |
| xml_etree_parse            | 162 ms                                                     | 150 ms: 1.08x faster                                                    |
| pprint_pformat             | 1.56 sec                                                   | 1.45 sec: 1.08x faster                                                  |
| nbody                      | 88.3 ms                                                    | 82.5 ms: 1.07x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                     | 101 ms: 1.07x faster                                                    |
| xml_etree_generate         | 87.4 ms                                                    | 82.0 ms: 1.07x faster                                                   |
| pprint_safe_repr           | 758 ms                                                     | 712 ms: 1.07x faster                                                    |
| xml_etree_process          | 61.2 ms                                                    | 57.7 ms: 1.06x faster                                                   |
| pathlib                    | 17.3 ms                                                    | 16.5 ms: 1.05x faster                                                   |
| json_dumps                 | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                   |
| telco                      | 8.41 ms                                                    | 8.06 ms: 1.04x faster                                                   |
| sqlite_synth               | 2.99 us                                                    | 2.87 us: 1.04x faster                                                   |
| deepcopy_memo              | 39.7 us                                                    | 38.4 us: 1.03x faster                                                   |
| regex_effbot               | 3.67 ms                                                    | 3.56 ms: 1.03x faster                                                   |
| gc_traversal               | 3.98 ms                                                    | 3.87 ms: 1.03x faster                                                   |
| coroutines                 | 23.2 ms                                                    | 22.6 ms: 1.02x faster                                                   |
| chaos                      | 61.3 ms                                                    | 60.3 ms: 1.02x faster                                                   |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                                    |
| pycparser                  | 1.16 sec                                                   | 1.14 sec: 1.01x faster                                                  |
| sqlglot_parse              | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                                   |
| meteor_contest             | 110 ms                                                     | 109 ms: 1.01x faster                                                    |
| create_gc_cycles           | 1.82 ms                                                    | 1.80 ms: 1.01x faster                                                   |
| logging_format             | 6.47 us                                                    | 6.42 us: 1.01x faster                                                   |
| logging_simple             | 5.74 us                                                    | 5.71 us: 1.01x faster                                                   |
| regex_v8                   | 25.1 ms                                                    | 25.0 ms: 1.01x faster                                                   |
| pickle_dict                | 34.8 us                                                    | 34.7 us: 1.00x faster                                                   |
| regex_dna                  | 221 ms                                                     | 222 ms: 1.00x slower                                                    |
| unpickle_list              | 5.34 us                                                    | 5.37 us: 1.00x slower                                                   |
| sqlglot_transpile          | 1.63 ms                                                    | 1.65 ms: 1.01x slower                                                   |
| pickle_list                | 5.11 us                                                    | 5.14 us: 1.01x slower                                                   |
| regex_compile              | 137 ms                                                     | 138 ms: 1.01x slower                                                    |
| scimark_sor                | 127 ms                                                     | 129 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.87 sec: 1.01x slower                                                  |
| comprehensions             | 16.6 us                                                    | 16.9 us: 1.02x slower                                                   |
| html5lib                   | 67.2 ms                                                    | 68.4 ms: 1.02x slower                                                   |
| asyncio_tcp                | 508 ms                                                     | 518 ms: 1.02x slower                                                    |
| async_tree_none_tg         | 336 ms                                                     | 343 ms: 1.02x slower                                                    |
| logging_silent             | 105 ns                                                     | 107 ns: 1.02x slower                                                    |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.02x slower                                                    |
| 2to3                       | 274 ms                                                     | 281 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 602 ms: 1.02x slower                                                    |
| dulwich_log                | 67.2 ms                                                    | 68.9 ms: 1.03x slower                                                   |
| tornado_http               | 94.6 ms                                                    | 97.1 ms: 1.03x slower                                                   |
| sqlglot_optimize           | 55.5 ms                                                    | 57.0 ms: 1.03x slower                                                   |
| unpickle_pure_python       | 218 us                                                     | 225 us: 1.03x slower                                                    |
| deepcopy                   | 367 us                                                     | 378 us: 1.03x slower                                                    |
| go                         | 145 ms                                                     | 149 ms: 1.03x slower                                                    |
| dask                       | 369 ms                                                     | 381 ms: 1.03x slower                                                    |
| scimark_lu                 | 122 ms                                                     | 126 ms: 1.03x slower                                                    |
| unpickle                   | 15.1 us                                                    | 15.6 us: 1.03x slower                                                   |
| python_startup             | 10.8 ms                                                    | 11.1 ms: 1.04x slower                                                   |
| generators                 | 29.6 ms                                                    | 30.9 ms: 1.04x slower                                                   |
| docutils                   | 2.83 sec                                                   | 2.95 sec: 1.04x slower                                                  |
| nqueens                    | 81.4 ms                                                    | 85.0 ms: 1.04x slower                                                   |
| raytrace                   | 267 ms                                                     | 279 ms: 1.04x slower                                                    |
| pickle                     | 11.5 us                                                    | 12.0 us: 1.05x slower                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 640 ms: 1.05x slower                                                    |
| genshi_text                | 23.7 ms                                                    | 25.0 ms: 1.05x slower                                                   |
| bench_thread_pool          | 834 us                                                     | 881 us: 1.06x slower                                                    |
| typing_runtime_protocols   | 165 us                                                     | 174 us: 1.06x slower                                                    |
| hexiom                     | 6.30 ms                                                    | 6.66 ms: 1.06x slower                                                   |
| async_generators           | 442 ms                                                     | 469 ms: 1.06x slower                                                    |
| async_tree_io              | 939 ms                                                     | 999 ms: 1.06x slower                                                    |
| sympy_str                  | 282 ms                                                     | 301 ms: 1.07x slower                                                    |
| python_startup_no_site     | 7.11 ms                                                    | 7.60 ms: 1.07x slower                                                   |
| django_template            | 34.8 ms                                                    | 37.3 ms: 1.07x slower                                                   |
| sympy_expand               | 473 ms                                                     | 512 ms: 1.08x slower                                                    |
| sympy_integrate            | 20.5 ms                                                    | 22.5 ms: 1.10x slower                                                   |
| sympy_sum                  | 156 ms                                                     | 171 ms: 1.10x slower                                                    |
| pylint                     | 317 ms                                                     | 352 ms: 1.11x slower                                                    |
| genshi_xml                 | 51.6 ms                                                    | 58.9 ms: 1.14x slower                                                   |
| deltablue                  | 3.25 ms                                                    | 3.77 ms: 1.16x slower                                                   |
| Geometric mean             | (ref)                                                      | 1.00x faster                                                            |

Benchmark hidden because not significant (12): async_tree_io_tg, deepcopy_reduce, json_loads, asyncio_websockets, json, pickle_pure_python, thrift, coverage, async_tree_memoization_tg, bench_mp_pool, async_tree_none, async_tree_memoization
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 82.24% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x
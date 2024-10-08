# Results vs. 3.13.0b2

- fork: python
- ref: 91b7f2e7f6593acefda4
- machine: linux-x86_64
- commit hash: 91b7f2e
- commit date: 2024-09-01
- overall geometric mean: 1.05x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 276 ms: 1.01x slower                                                  |
| docutils       | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                                |
| html5lib       | 67.2 ms                                                    | 64.7 ms: 1.04x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 94.4 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 401 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 554 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 537 ms: 1.09x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 406 ms: 1.09x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.08x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 899 ms: 1.04x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                          |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.1 ms: 1.13x faster                                                 |
| nbody          | 88.3 ms                                                    | 79.8 ms: 1.11x faster                                                 |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                      | 1.09x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.0 ms: 1.05x faster                                                 |
| regex_effbot   | 3.67 ms                                                    | 3.52 ms: 1.04x faster                                                 |
| regex_dna      | 221 ms                                                     | 217 ms: 1.02x faster                                                  |
| regex_compile  | 137 ms                                                     | 141 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.6 ms: 1.13x faster                                                 |
| xml_etree_parse      | 162 ms                                                     | 145 ms: 1.11x faster                                                  |
| tomli_loads          | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                |
| xml_etree_process    | 61.2 ms                                                    | 55.1 ms: 1.11x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 98.3 ms: 1.09x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.01x faster                                                  |
| json_loads           | 28.9 us                                                    | 28.6 us: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.97 ms: 1.13x faster                                                 |
| django_template | 34.8 ms                                                    | 36.3 ms: 1.04x slower                                                 |
| genshi_text     | 23.7 ms                                                    | 24.9 ms: 1.05x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 58.3 ms: 1.13x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.7 us: 1.49x faster                                                 |
| deepcopy                   | 367 us                                                     | 267 us: 1.37x faster                                                  |
| richards                   | 50.9 ms                                                    | 39.3 ms: 1.30x faster                                                 |
| scimark_fft                | 392 ms                                                     | 309 ms: 1.27x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                    | 2.65 us: 1.26x faster                                                 |
| richards_super             | 57.4 ms                                                    | 45.4 ms: 1.26x faster                                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.34 ms: 1.21x faster                                                 |
| crypto_pyaes               | 77.5 ms                                                    | 65.7 ms: 1.18x faster                                                 |
| spectral_norm              | 116 ms                                                     | 99.9 ms: 1.16x faster                                                 |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 401 ms: 1.15x faster                                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.43 sec: 1.13x faster                                                |
| xml_etree_generate         | 87.4 ms                                                    | 77.6 ms: 1.13x faster                                                 |
| mako                       | 11.2 ms                                                    | 9.97 ms: 1.13x faster                                                 |
| float                      | 78.9 ms                                                    | 70.1 ms: 1.13x faster                                                 |
| gc_traversal               | 3.98 ms                                                    | 3.56 ms: 1.12x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 145 ms: 1.11x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                |
| xml_etree_process          | 61.2 ms                                                    | 55.1 ms: 1.11x faster                                                 |
| nbody                      | 88.3 ms                                                    | 79.8 ms: 1.11x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 554 ms: 1.10x faster                                                  |
| scimark_sor                | 127 ms                                                     | 116 ms: 1.10x faster                                                  |
| go                         | 145 ms                                                     | 131 ms: 1.10x faster                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.9 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 537 ms: 1.09x faster                                                  |
| mdp                        | 2.79 sec                                                   | 2.55 sec: 1.09x faster                                                |
| async_tree_memoization_tg  | 444 ms                                                     | 406 ms: 1.09x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 98.3 ms: 1.09x faster                                                 |
| scimark_lu                 | 122 ms                                                     | 111 ms: 1.09x faster                                                  |
| coverage                   | 93.1 ms                                                    | 85.4 ms: 1.09x faster                                                 |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.09x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.08x faster                                                  |
| fannkuch                   | 402 ms                                                     | 372 ms: 1.08x faster                                                  |
| pyflate                    | 484 ms                                                     | 449 ms: 1.08x faster                                                  |
| logging_format             | 6.47 us                                                    | 6.07 us: 1.07x faster                                                 |
| telco                      | 8.41 ms                                                    | 7.93 ms: 1.06x faster                                                 |
| pprint_safe_repr           | 758 ms                                                     | 718 ms: 1.06x faster                                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                                |
| chaos                      | 61.3 ms                                                    | 58.5 ms: 1.05x faster                                                 |
| regex_v8                   | 25.1 ms                                                    | 24.0 ms: 1.05x faster                                                 |
| thrift                     | 823 us                                                     | 786 us: 1.05x faster                                                  |
| logging_simple             | 5.74 us                                                    | 5.51 us: 1.04x faster                                                 |
| regex_effbot               | 3.67 ms                                                    | 3.52 ms: 1.04x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 899 ms: 1.04x faster                                                  |
| html5lib                   | 67.2 ms                                                    | 64.7 ms: 1.04x faster                                                 |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                 |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                                  |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                  |
| logging_silent             | 105 ns                                                     | 102 ns: 1.03x faster                                                  |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| asyncio_tcp                | 508 ms                                                     | 495 ms: 1.03x faster                                                  |
| asyncio_websockets         | 567 ms                                                     | 554 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                |
| regex_dna                  | 221 ms                                                     | 217 ms: 1.02x faster                                                  |
| deltablue                  | 3.25 ms                                                    | 3.19 ms: 1.02x faster                                                 |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                                 |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.01x faster                                                  |
| json_loads                 | 28.9 us                                                    | 28.6 us: 1.01x faster                                                 |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                 |
| tornado_http               | 94.6 ms                                                    | 94.4 ms: 1.00x faster                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                                 |
| 2to3                       | 274 ms                                                     | 276 ms: 1.01x slower                                                  |
| json                       | 5.31 ms                                                    | 5.36 ms: 1.01x slower                                                 |
| dulwich_log                | 67.2 ms                                                    | 68.2 ms: 1.02x slower                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.34 ms: 1.02x slower                                                 |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                                |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.03x slower                                                  |
| async_generators           | 442 ms                                                     | 455 ms: 1.03x slower                                                  |
| raytrace                   | 267 ms                                                     | 275 ms: 1.03x slower                                                  |
| regex_compile              | 137 ms                                                     | 141 ms: 1.03x slower                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.69 ms: 1.03x slower                                                 |
| django_template            | 34.8 ms                                                    | 36.3 ms: 1.04x slower                                                 |
| nqueens                    | 81.4 ms                                                    | 85.1 ms: 1.05x slower                                                 |
| docutils                   | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                                |
| genshi_text                | 23.7 ms                                                    | 24.9 ms: 1.05x slower                                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 58.4 ms: 1.05x slower                                                 |
| sympy_str                  | 282 ms                                                     | 301 ms: 1.06x slower                                                  |
| sympy_expand               | 473 ms                                                     | 507 ms: 1.07x slower                                                  |
| hexiom                     | 6.30 ms                                                    | 6.86 ms: 1.09x slower                                                 |
| sympy_sum                  | 156 ms                                                     | 173 ms: 1.11x slower                                                  |
| sympy_integrate            | 20.5 ms                                                    | 22.8 ms: 1.11x slower                                                 |
| generators                 | 29.6 ms                                                    | 33.1 ms: 1.12x slower                                                 |
| genshi_xml                 | 51.6 ms                                                    | 58.3 ms: 1.13x slower                                                 |
| pylint                     | 317 ms                                                     | 372 ms: 1.17x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (4): async_tree_io, pickle_pure_python, typing_runtime_protocols, bench_thread_pool
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.09x
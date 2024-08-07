# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: underflow_static
- machine: linux-x86_64
- commit hash: f6b4125
- commit date: 2024-07-10
- overall geometric mean: 1.05x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 275 ms: 1.00x slower                                                    |
| docutils       | 2.83 sec                                                   | 2.90 sec: 1.03x slower                                                  |
| html5lib       | 67.2 ms                                                    | 63.1 ms: 1.07x faster                                                   |
| tornado_http   | 94.6 ms                                                    | 92.6 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                      | 1.01x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 377 ms: 1.18x faster                                                    |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                    |
| async_tree_memoization     | 463 ms                                                     | 409 ms: 1.13x faster                                                    |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 848 ms: 1.10x faster                                                    |
| async_tree_io              | 939 ms                                                     | 856 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 542 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                                    |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.9 ms: 1.13x faster                                                   |
| nbody          | 88.3 ms                                                    | 80.0 ms: 1.10x faster                                                   |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                      | 1.09x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 25.7 ms: 1.02x slower                                                   |
| regex_dna      | 221 ms                                                     | 229 ms: 1.03x slower                                                    |
| regex_effbot   | 3.67 ms                                                    | 4.02 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                      | 1.04x slower                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                  |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                     | 99.4 ms: 1.08x faster                                                   |
| xml_etree_generate   | 87.4 ms                                                    | 81.6 ms: 1.07x faster                                                   |
| xml_etree_process    | 61.2 ms                                                    | 57.1 ms: 1.07x faster                                                   |
| unpickle_pure_python | 218 us                                                     | 207 us: 1.05x faster                                                    |
| pickle_pure_python   | 305 us                                                     | 292 us: 1.05x faster                                                    |
| json_loads           | 28.9 us                                                    | 27.8 us: 1.04x faster                                                   |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                   |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                      | 1.01x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.91 ms: 1.13x faster                                                   |
| django_template | 34.8 ms                                                    | 36.0 ms: 1.03x slower                                                   |
| genshi_text     | 23.7 ms                                                    | 25.2 ms: 1.07x slower                                                   |
| genshi_xml      | 51.6 ms                                                    | 58.7 ms: 1.14x slower                                                   |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.4 us: 1.45x faster                                                   |
| deepcopy                   | 367 us                                                     | 271 us: 1.35x faster                                                    |
| richards                   | 50.9 ms                                                    | 40.9 ms: 1.25x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                    | 2.69 us: 1.24x faster                                                   |
| scimark_fft                | 392 ms                                                     | 320 ms: 1.23x faster                                                    |
| richards_super             | 57.4 ms                                                    | 48.0 ms: 1.20x faster                                                   |
| scimark_monte_carlo        | 69.2 ms                                                    | 58.5 ms: 1.18x faster                                                   |
| async_tree_memoization_tg  | 444 ms                                                     | 377 ms: 1.18x faster                                                    |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                    |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.53 ms: 1.16x faster                                                   |
| crypto_pyaes               | 77.5 ms                                                    | 67.0 ms: 1.16x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 409 ms: 1.13x faster                                                    |
| mako                       | 11.2 ms                                                    | 9.91 ms: 1.13x faster                                                   |
| float                      | 78.9 ms                                                    | 69.9 ms: 1.13x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                    |
| fannkuch                   | 402 ms                                                     | 362 ms: 1.11x faster                                                    |
| tomli_loads                | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                  |
| spectral_norm              | 116 ms                                                     | 105 ms: 1.11x faster                                                    |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 848 ms: 1.10x faster                                                    |
| nbody                      | 88.3 ms                                                    | 80.0 ms: 1.10x faster                                                   |
| pyflate                    | 484 ms                                                     | 439 ms: 1.10x faster                                                    |
| mdp                        | 2.79 sec                                                   | 2.53 sec: 1.10x faster                                                  |
| async_tree_io              | 939 ms                                                     | 856 ms: 1.10x faster                                                    |
| pprint_safe_repr           | 758 ms                                                     | 697 ms: 1.09x faster                                                    |
| pprint_pformat             | 1.56 sec                                                   | 1.43 sec: 1.09x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 542 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                     | 99.4 ms: 1.08x faster                                                   |
| logging_format             | 6.47 us                                                    | 6.02 us: 1.07x faster                                                   |
| xml_etree_generate         | 87.4 ms                                                    | 81.6 ms: 1.07x faster                                                   |
| xml_etree_process          | 61.2 ms                                                    | 57.1 ms: 1.07x faster                                                   |
| logging_silent             | 105 ns                                                     | 98.0 ns: 1.07x faster                                                   |
| pathlib                    | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                                   |
| html5lib                   | 67.2 ms                                                    | 63.1 ms: 1.07x faster                                                   |
| unpickle_pure_python       | 218 us                                                     | 207 us: 1.05x faster                                                    |
| telco                      | 8.41 ms                                                    | 8.00 ms: 1.05x faster                                                   |
| gc_traversal               | 3.98 ms                                                    | 3.78 ms: 1.05x faster                                                   |
| logging_simple             | 5.74 us                                                    | 5.49 us: 1.05x faster                                                   |
| pickle_pure_python         | 305 us                                                     | 292 us: 1.05x faster                                                    |
| bpe_tokeniser              | 5.02 sec                                                   | 4.81 sec: 1.05x faster                                                  |
| sqlglot_parse              | 1.32 ms                                                    | 1.27 ms: 1.04x faster                                                   |
| json_loads                 | 28.9 us                                                    | 27.8 us: 1.04x faster                                                   |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                   |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                    |
| thrift                     | 823 us                                                     | 801 us: 1.03x faster                                                    |
| json                       | 5.31 ms                                                    | 5.17 ms: 1.03x faster                                                   |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                   |
| sqlglot_transpile          | 1.63 ms                                                    | 1.60 ms: 1.02x faster                                                   |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                                    |
| create_gc_cycles           | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                   |
| tornado_http               | 94.6 ms                                                    | 92.6 ms: 1.02x faster                                                   |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                  |
| dask                       | 369 ms                                                     | 363 ms: 1.02x faster                                                    |
| asyncio_tcp                | 508 ms                                                     | 500 ms: 1.02x faster                                                    |
| coverage                   | 93.1 ms                                                    | 92.4 ms: 1.01x faster                                                   |
| bench_thread_pool          | 834 us                                                     | 829 us: 1.01x faster                                                    |
| sqlglot_optimize           | 55.5 ms                                                    | 55.3 ms: 1.00x faster                                                   |
| 2to3                       | 274 ms                                                     | 275 ms: 1.00x slower                                                    |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                   |
| chaos                      | 61.3 ms                                                    | 61.7 ms: 1.01x slower                                                   |
| generators                 | 29.6 ms                                                    | 29.9 ms: 1.01x slower                                                   |
| sqlglot_normalize          | 110 ms                                                     | 111 ms: 1.01x slower                                                    |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.01x slower                                                   |
| go                         | 145 ms                                                     | 146 ms: 1.01x slower                                                    |
| coroutines                 | 23.2 ms                                                    | 23.5 ms: 1.01x slower                                                   |
| typing_runtime_protocols   | 165 us                                                     | 169 us: 1.02x slower                                                    |
| regex_v8                   | 25.1 ms                                                    | 25.7 ms: 1.02x slower                                                   |
| scimark_sor                | 127 ms                                                     | 131 ms: 1.02x slower                                                    |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.03x slower                                                  |
| docutils                   | 2.83 sec                                                   | 2.90 sec: 1.03x slower                                                  |
| regex_dna                  | 221 ms                                                     | 229 ms: 1.03x slower                                                    |
| django_template            | 34.8 ms                                                    | 36.0 ms: 1.03x slower                                                   |
| async_generators           | 442 ms                                                     | 458 ms: 1.04x slower                                                    |
| scimark_lu                 | 122 ms                                                     | 126 ms: 1.04x slower                                                    |
| sympy_str                  | 282 ms                                                     | 295 ms: 1.04x slower                                                    |
| nqueens                    | 81.4 ms                                                    | 85.1 ms: 1.04x slower                                                   |
| sympy_expand               | 473 ms                                                     | 496 ms: 1.05x slower                                                    |
| sympy_sum                  | 156 ms                                                     | 164 ms: 1.06x slower                                                    |
| hexiom                     | 6.30 ms                                                    | 6.65 ms: 1.06x slower                                                   |
| genshi_text                | 23.7 ms                                                    | 25.2 ms: 1.07x slower                                                   |
| sympy_integrate            | 20.5 ms                                                    | 22.0 ms: 1.07x slower                                                   |
| pylint                     | 317 ms                                                     | 344 ms: 1.08x slower                                                    |
| regex_effbot               | 3.67 ms                                                    | 4.02 ms: 1.09x slower                                                   |
| deltablue                  | 3.25 ms                                                    | 3.60 ms: 1.11x slower                                                   |
| genshi_xml                 | 51.6 ms                                                    | 58.7 ms: 1.14x slower                                                   |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                            |

Benchmark hidden because not significant (4): regex_compile, dulwich_log, python_startup_no_site, raytrace
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x
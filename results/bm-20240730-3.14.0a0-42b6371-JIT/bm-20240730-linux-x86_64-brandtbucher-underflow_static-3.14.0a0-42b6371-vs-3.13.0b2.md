# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: underflow_static
- machine: linux-x86_64
- commit hash: 42b6371
- commit date: 2024-07-30
- overall geometric mean: 1.04x faster
- HPT reliability: 99.78%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 277 ms: 1.01x slower                                                    |
| docutils       | 2.83 sec                                                   | 2.97 sec: 1.05x slower                                                  |
| html5lib       | 67.2 ms                                                    | 62.7 ms: 1.07x faster                                                   |
| tornado_http   | 94.6 ms                                                    | 94.0 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                      | 1.00x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                    |
| async_tree_memoization     | 463 ms                                                     | 400 ms: 1.16x faster                                                    |
| async_tree_memoization_tg  | 444 ms                                                     | 390 ms: 1.14x faster                                                    |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 531 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 868 ms: 1.08x faster                                                    |
| async_tree_io              | 939 ms                                                     | 913 ms: 1.03x faster                                                    |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 79.2 ms: 1.12x faster                                                   |
| float          | 78.9 ms                                                    | 70.9 ms: 1.11x faster                                                   |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                      | 1.09x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.5 ms: 1.03x faster                                                   |
| regex_compile  | 137 ms                                                     | 137 ms: 1.00x slower                                                    |
| regex_effbot   | 3.67 ms                                                    | 3.79 ms: 1.03x slower                                                   |
| regex_dna      | 221 ms                                                     | 231 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                      | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 79.1 ms: 1.11x faster                                                   |
| xml_etree_parse      | 162 ms                                                     | 147 ms: 1.10x faster                                                    |
| xml_etree_process    | 61.2 ms                                                    | 55.9 ms: 1.09x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                     | 99.5 ms: 1.08x faster                                                   |
| tomli_loads          | 2.12 sec                                                   | 1.98 sec: 1.07x faster                                                  |
| unpickle_pure_python | 218 us                                                     | 207 us: 1.05x faster                                                    |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.05x faster                                                   |
| json_loads           | 28.9 us                                                    | 28.0 us: 1.03x faster                                                   |
| pickle_pure_python   | 305 us                                                     | 315 us: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                   |
| python_startup_no_site | 7.11 ms                                                    | 7.14 ms: 1.00x slower                                                   |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.91 ms: 1.13x faster                                                   |
| django_template | 34.8 ms                                                    | 36.6 ms: 1.05x slower                                                   |
| genshi_text     | 23.7 ms                                                    | 25.7 ms: 1.09x slower                                                   |
| genshi_xml      | 51.6 ms                                                    | 57.2 ms: 1.11x slower                                                   |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.8 us: 1.48x faster                                                   |
| deepcopy                   | 367 us                                                     | 277 us: 1.32x faster                                                    |
| scimark_fft                | 392 ms                                                     | 303 ms: 1.29x faster                                                    |
| richards                   | 50.9 ms                                                    | 39.3 ms: 1.29x faster                                                   |
| richards_super             | 57.4 ms                                                    | 44.9 ms: 1.28x faster                                                   |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.27 ms: 1.23x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                    | 2.81 us: 1.19x faster                                                   |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                    |
| scimark_monte_carlo        | 69.2 ms                                                    | 59.6 ms: 1.16x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 400 ms: 1.16x faster                                                    |
| crypto_pyaes               | 77.5 ms                                                    | 67.8 ms: 1.14x faster                                                   |
| async_tree_memoization_tg  | 444 ms                                                     | 390 ms: 1.14x faster                                                    |
| spectral_norm              | 116 ms                                                     | 102 ms: 1.14x faster                                                    |
| mako                       | 11.2 ms                                                    | 9.91 ms: 1.13x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                    |
| gc_traversal               | 3.98 ms                                                    | 3.55 ms: 1.12x faster                                                   |
| nbody                      | 88.3 ms                                                    | 79.2 ms: 1.12x faster                                                   |
| float                      | 78.9 ms                                                    | 70.9 ms: 1.11x faster                                                   |
| bpe_tokeniser              | 5.02 sec                                                   | 4.52 sec: 1.11x faster                                                  |
| pyflate                    | 484 ms                                                     | 436 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 531 ms: 1.11x faster                                                    |
| xml_etree_generate         | 87.4 ms                                                    | 79.1 ms: 1.11x faster                                                   |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                                    |
| xml_etree_process          | 61.2 ms                                                    | 55.9 ms: 1.09x faster                                                   |
| fannkuch                   | 402 ms                                                     | 368 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.09x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                     | 99.5 ms: 1.08x faster                                                   |
| async_tree_io_tg           | 936 ms                                                     | 868 ms: 1.08x faster                                                    |
| telco                      | 8.41 ms                                                    | 7.82 ms: 1.08x faster                                                   |
| tomli_loads                | 2.12 sec                                                   | 1.98 sec: 1.07x faster                                                  |
| html5lib                   | 67.2 ms                                                    | 62.7 ms: 1.07x faster                                                   |
| pathlib                    | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                                   |
| unpickle_pure_python       | 218 us                                                     | 207 us: 1.05x faster                                                    |
| thrift                     | 823 us                                                     | 787 us: 1.05x faster                                                    |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.05x faster                                                   |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.04x faster                                                   |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.04x faster                                                    |
| pprint_pformat             | 1.56 sec                                                   | 1.50 sec: 1.04x faster                                                  |
| json                       | 5.31 ms                                                    | 5.13 ms: 1.03x faster                                                   |
| json_loads                 | 28.9 us                                                    | 28.0 us: 1.03x faster                                                   |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                    |
| logging_format             | 6.47 us                                                    | 6.28 us: 1.03x faster                                                   |
| pprint_safe_repr           | 758 ms                                                     | 737 ms: 1.03x faster                                                    |
| async_tree_io              | 939 ms                                                     | 913 ms: 1.03x faster                                                    |
| regex_v8                   | 25.1 ms                                                    | 24.5 ms: 1.03x faster                                                   |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.03x faster                                                  |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                                   |
| coverage                   | 93.1 ms                                                    | 91.2 ms: 1.02x faster                                                   |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                   |
| logging_silent             | 105 ns                                                     | 103 ns: 1.02x faster                                                    |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                    |
| pycparser                  | 1.16 sec                                                   | 1.14 sec: 1.02x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 822 us: 1.01x faster                                                    |
| dask                       | 369 ms                                                     | 365 ms: 1.01x faster                                                    |
| comprehensions             | 16.6 us                                                    | 16.4 us: 1.01x faster                                                   |
| tornado_http               | 94.6 ms                                                    | 94.0 ms: 1.01x faster                                                   |
| regex_compile              | 137 ms                                                     | 137 ms: 1.00x slower                                                    |
| python_startup_no_site     | 7.11 ms                                                    | 7.14 ms: 1.00x slower                                                   |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                   |
| sqlglot_transpile          | 1.63 ms                                                    | 1.65 ms: 1.01x slower                                                   |
| 2to3                       | 274 ms                                                     | 277 ms: 1.01x slower                                                    |
| chaos                      | 61.3 ms                                                    | 62.4 ms: 1.02x slower                                                   |
| scimark_sor                | 127 ms                                                     | 130 ms: 1.02x slower                                                    |
| scimark_lu                 | 122 ms                                                     | 124 ms: 1.02x slower                                                    |
| go                         | 145 ms                                                     | 148 ms: 1.02x slower                                                    |
| raytrace                   | 267 ms                                                     | 275 ms: 1.03x slower                                                    |
| regex_effbot               | 3.67 ms                                                    | 3.79 ms: 1.03x slower                                                   |
| pickle_pure_python         | 305 us                                                     | 315 us: 1.03x slower                                                    |
| sqlglot_normalize          | 110 ms                                                     | 114 ms: 1.03x slower                                                    |
| nqueens                    | 81.4 ms                                                    | 84.1 ms: 1.03x slower                                                   |
| sqlglot_optimize           | 55.5 ms                                                    | 57.4 ms: 1.03x slower                                                   |
| regex_dna                  | 221 ms                                                     | 231 ms: 1.04x slower                                                    |
| typing_runtime_protocols   | 165 us                                                     | 172 us: 1.05x slower                                                    |
| docutils                   | 2.83 sec                                                   | 2.97 sec: 1.05x slower                                                  |
| async_generators           | 442 ms                                                     | 465 ms: 1.05x slower                                                    |
| django_template            | 34.8 ms                                                    | 36.6 ms: 1.05x slower                                                   |
| sympy_str                  | 282 ms                                                     | 304 ms: 1.08x slower                                                    |
| hexiom                     | 6.30 ms                                                    | 6.82 ms: 1.08x slower                                                   |
| genshi_text                | 23.7 ms                                                    | 25.7 ms: 1.09x slower                                                   |
| sympy_expand               | 473 ms                                                     | 515 ms: 1.09x slower                                                    |
| genshi_xml                 | 51.6 ms                                                    | 57.2 ms: 1.11x slower                                                   |
| sympy_sum                  | 156 ms                                                     | 173 ms: 1.11x slower                                                    |
| sympy_integrate            | 20.5 ms                                                    | 22.8 ms: 1.11x slower                                                   |
| generators                 | 29.6 ms                                                    | 33.8 ms: 1.14x slower                                                   |
| pylint                     | 317 ms                                                     | 365 ms: 1.15x slower                                                    |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                            |

Benchmark hidden because not significant (5): logging_simple, asyncio_tcp, mdp, deltablue, sqlglot_parse
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.78% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x
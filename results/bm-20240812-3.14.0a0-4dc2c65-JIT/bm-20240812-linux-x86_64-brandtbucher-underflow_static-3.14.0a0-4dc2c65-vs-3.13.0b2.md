# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: underflow_static
- machine: linux-x86_64
- commit hash: 4dc2c65
- commit date: 2024-08-12
- overall geometric mean: 1.03x faster
- HPT reliability: 97.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 282 ms: 1.03x slower                                                    |
| docutils       | 2.83 sec                                                   | 3.30 sec: 1.17x slower                                                  |
| html5lib       | 67.2 ms                                                    | 69.6 ms: 1.04x slower                                                   |
| tornado_http   | 94.6 ms                                                    | 95.3 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                      | 1.06x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                    |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                                    |
| async_tree_none_tg         | 336 ms                                                     | 302 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 530 ms: 1.11x faster                                                    |
| async_tree_memoization     | 463 ms                                                     | 421 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 866 ms: 1.08x faster                                                    |
| async_tree_io              | 939 ms                                                     | 903 ms: 1.04x faster                                                    |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.5 ms: 1.12x faster                                                   |
| nbody          | 88.3 ms                                                    | 80.3 ms: 1.10x faster                                                   |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                      | 1.08x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 218 ms: 1.02x faster                                                    |
| regex_effbot   | 3.67 ms                                                    | 3.75 ms: 1.02x slower                                                   |
| regex_v8       | 25.1 ms                                                    | 26.0 ms: 1.03x slower                                                   |
| regex_compile  | 137 ms                                                     | 146 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                      | 1.03x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.09x faster                                                    |
| xml_etree_generate   | 87.4 ms                                                    | 80.5 ms: 1.09x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                     | 99.1 ms: 1.08x faster                                                   |
| xml_etree_process    | 61.2 ms                                                    | 56.6 ms: 1.08x faster                                                   |
| tomli_loads          | 2.12 sec                                                   | 1.97 sec: 1.08x faster                                                  |
| unpickle_pure_python | 218 us                                                     | 203 us: 1.08x faster                                                    |
| json_loads           | 28.9 us                                                    | 27.8 us: 1.04x faster                                                   |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                   |
| pickle_pure_python   | 305 us                                                     | 303 us: 1.01x faster                                                    |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                   |
| python_startup_no_site | 7.11 ms                                                    | 7.18 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.91 ms: 1.13x faster                                                   |
| django_template | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                   |
| genshi_text     | 23.7 ms                                                    | 24.9 ms: 1.05x slower                                                   |
| genshi_xml      | 51.6 ms                                                    | 56.8 ms: 1.10x slower                                                   |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.0 us: 1.53x faster                                                   |
| richards                   | 50.9 ms                                                    | 35.2 ms: 1.45x faster                                                   |
| richards_super             | 57.4 ms                                                    | 40.2 ms: 1.43x faster                                                   |
| deepcopy                   | 367 us                                                     | 268 us: 1.37x faster                                                    |
| scimark_fft                | 392 ms                                                     | 310 ms: 1.26x faster                                                    |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.30 ms: 1.23x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                    | 2.75 us: 1.22x faster                                                   |
| crypto_pyaes               | 77.5 ms                                                    | 65.5 ms: 1.18x faster                                                   |
| spectral_norm              | 116 ms                                                     | 100 ms: 1.16x faster                                                    |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                    |
| mako                       | 11.2 ms                                                    | 9.91 ms: 1.13x faster                                                   |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                                    |
| float                      | 78.9 ms                                                    | 70.5 ms: 1.12x faster                                                   |
| scimark_sor                | 127 ms                                                     | 114 ms: 1.12x faster                                                    |
| async_tree_none_tg         | 336 ms                                                     | 302 ms: 1.11x faster                                                    |
| bpe_tokeniser              | 5.02 sec                                                   | 4.53 sec: 1.11x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 530 ms: 1.11x faster                                                    |
| telco                      | 8.41 ms                                                    | 7.62 ms: 1.10x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 421 ms: 1.10x faster                                                    |
| fannkuch                   | 402 ms                                                     | 365 ms: 1.10x faster                                                    |
| nbody                      | 88.3 ms                                                    | 80.3 ms: 1.10x faster                                                   |
| scimark_lu                 | 122 ms                                                     | 111 ms: 1.09x faster                                                    |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.09x faster                                                    |
| xml_etree_generate         | 87.4 ms                                                    | 80.5 ms: 1.09x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                     | 99.1 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 866 ms: 1.08x faster                                                    |
| xml_etree_process          | 61.2 ms                                                    | 56.6 ms: 1.08x faster                                                   |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                   |
| tomli_loads                | 2.12 sec                                                   | 1.97 sec: 1.08x faster                                                  |
| unpickle_pure_python       | 218 us                                                     | 203 us: 1.08x faster                                                    |
| scimark_monte_carlo        | 69.2 ms                                                    | 64.6 ms: 1.07x faster                                                   |
| pyflate                    | 484 ms                                                     | 453 ms: 1.07x faster                                                    |
| logging_format             | 6.47 us                                                    | 6.11 us: 1.06x faster                                                   |
| logging_silent             | 105 ns                                                     | 99.3 ns: 1.05x faster                                                   |
| json                       | 5.31 ms                                                    | 5.04 ms: 1.05x faster                                                   |
| gc_traversal               | 3.98 ms                                                    | 3.78 ms: 1.05x faster                                                   |
| thrift                     | 823 us                                                     | 787 us: 1.05x faster                                                    |
| mdp                        | 2.79 sec                                                   | 2.67 sec: 1.04x faster                                                  |
| logging_simple             | 5.74 us                                                    | 5.52 us: 1.04x faster                                                   |
| json_loads                 | 28.9 us                                                    | 27.8 us: 1.04x faster                                                   |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                   |
| async_tree_io              | 939 ms                                                     | 903 ms: 1.04x faster                                                    |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                    |
| deltablue                  | 3.25 ms                                                    | 3.15 ms: 1.03x faster                                                   |
| coroutines                 | 23.2 ms                                                    | 22.6 ms: 1.03x faster                                                   |
| create_gc_cycles           | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                   |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                  |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                                    |
| bench_thread_pool          | 834 us                                                     | 820 us: 1.02x faster                                                    |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                   |
| regex_dna                  | 221 ms                                                     | 218 ms: 1.02x faster                                                    |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                    |
| comprehensions             | 16.6 us                                                    | 16.4 us: 1.01x faster                                                   |
| pickle_pure_python         | 305 us                                                     | 303 us: 1.01x faster                                                    |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                                   |
| tornado_http               | 94.6 ms                                                    | 95.3 ms: 1.01x slower                                                   |
| python_startup_no_site     | 7.11 ms                                                    | 7.18 ms: 1.01x slower                                                   |
| asyncio_tcp                | 508 ms                                                     | 515 ms: 1.01x slower                                                    |
| raytrace                   | 267 ms                                                     | 271 ms: 1.02x slower                                                    |
| regex_effbot               | 3.67 ms                                                    | 3.75 ms: 1.02x slower                                                   |
| typing_runtime_protocols   | 165 us                                                     | 169 us: 1.02x slower                                                    |
| nqueens                    | 81.4 ms                                                    | 83.6 ms: 1.03x slower                                                   |
| async_generators           | 442 ms                                                     | 454 ms: 1.03x slower                                                    |
| 2to3                       | 274 ms                                                     | 282 ms: 1.03x slower                                                    |
| django_template            | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                   |
| go                         | 145 ms                                                     | 149 ms: 1.03x slower                                                    |
| regex_v8                   | 25.1 ms                                                    | 26.0 ms: 1.03x slower                                                   |
| html5lib                   | 67.2 ms                                                    | 69.6 ms: 1.04x slower                                                   |
| genshi_text                | 23.7 ms                                                    | 24.9 ms: 1.05x slower                                                   |
| pycparser                  | 1.16 sec                                                   | 1.22 sec: 1.06x slower                                                  |
| chaos                      | 61.3 ms                                                    | 65.3 ms: 1.06x slower                                                   |
| regex_compile              | 137 ms                                                     | 146 ms: 1.07x slower                                                    |
| sqlglot_optimize           | 55.5 ms                                                    | 60.3 ms: 1.09x slower                                                   |
| sqlglot_normalize          | 110 ms                                                     | 120 ms: 1.09x slower                                                    |
| hexiom                     | 6.30 ms                                                    | 6.88 ms: 1.09x slower                                                   |
| sympy_expand               | 473 ms                                                     | 519 ms: 1.10x slower                                                    |
| genshi_xml                 | 51.6 ms                                                    | 56.8 ms: 1.10x slower                                                   |
| sqlglot_parse              | 1.32 ms                                                    | 1.46 ms: 1.10x slower                                                   |
| sqlglot_transpile          | 1.63 ms                                                    | 1.84 ms: 1.12x slower                                                   |
| sympy_str                  | 282 ms                                                     | 323 ms: 1.15x slower                                                    |
| docutils                   | 2.83 sec                                                   | 3.30 sec: 1.17x slower                                                  |
| sympy_integrate            | 20.5 ms                                                    | 24.4 ms: 1.19x slower                                                   |
| sympy_sum                  | 156 ms                                                     | 191 ms: 1.23x slower                                                    |
| pylint                     | 317 ms                                                     | 404 ms: 1.27x slower                                                    |
| generators                 | 29.6 ms                                                    | 41.3 ms: 1.39x slower                                                   |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                            |

Benchmark hidden because not significant (3): coverage, pprint_safe_repr, pprint_pformat
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 97.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x
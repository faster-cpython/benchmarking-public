# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow_static
- machine: linux-x86_64
- commit hash: 42b6371
- commit date: 2024-07-30
- overall geometric mean: 1.01x faster
- HPT reliability: 52.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 277 ms: 1.04x slower                                                    |
| docutils       | 2.58 sec                                               | 2.97 sec: 1.15x slower                                                  |
| html5lib       | 64.5 ms                                                | 62.7 ms: 1.03x faster                                                   |
| tornado_http   | 91.5 ms                                                | 94.0 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 390 ms: 1.19x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 400 ms: 1.11x faster                                                    |
| async_tree_none            | 354 ms                                                 | 325 ms: 1.09x faster                                                    |
| async_tree_none_tg         | 320 ms                                                 | 298 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 531 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 563 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                  |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                    |
| asyncio_tcp                | 488 ms                                                 | 507 ms: 1.04x slower                                                    |
| async_tree_io_tg           | 825 ms                                                 | 868 ms: 1.05x slower                                                    |
| async_generators           | 433 ms                                                 | 465 ms: 1.07x slower                                                    |
| async_tree_io              | 843 ms                                                 | 913 ms: 1.08x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.9 ms: 1.11x faster                                                   |
| nbody          | 85.7 ms                                                | 79.2 ms: 1.08x faster                                                   |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                  | 1.06x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 24.5 ms: 1.03x faster                                                   |
| regex_effbot   | 3.88 ms                                                | 3.79 ms: 1.03x faster                                                   |
| regex_compile  | 131 ms                                                 | 137 ms: 1.05x slower                                                    |
| regex_dna      | 220 ms                                                 | 231 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 79.1 ms: 1.10x faster                                                   |
| xml_etree_process    | 60.4 ms                                                | 55.9 ms: 1.08x faster                                                   |
| tomli_loads          | 2.11 sec                                               | 1.98 sec: 1.07x faster                                                  |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                    |
| unpickle_pure_python | 213 us                                                 | 207 us: 1.03x faster                                                    |
| xml_etree_iterparse  | 102 ms                                                 | 99.5 ms: 1.03x faster                                                   |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                   |
| json_loads           | 27.0 us                                                | 28.0 us: 1.04x slower                                                   |
| pickle_pure_python   | 300 us                                                 | 315 us: 1.05x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                   |
| python_startup_no_site | 6.99 ms                                                | 7.14 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.91 ms: 1.12x faster                                                   |
| django_template | 34.4 ms                                                | 36.6 ms: 1.06x slower                                                   |
| genshi_text     | 22.9 ms                                                | 25.7 ms: 1.12x slower                                                   |
| genshi_xml      | 50.3 ms                                                | 57.2 ms: 1.14x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.8 us: 1.42x faster                                                   |
| deepcopy                   | 352 us                                                 | 277 us: 1.27x faster                                                    |
| richards                   | 48.1 ms                                                | 39.3 ms: 1.22x faster                                                   |
| scimark_fft                | 369 ms                                                 | 303 ms: 1.22x faster                                                    |
| richards_super             | 54.4 ms                                                | 44.9 ms: 1.21x faster                                                   |
| async_tree_memoization_tg  | 465 ms                                                 | 390 ms: 1.19x faster                                                    |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.27 ms: 1.18x faster                                                   |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                    |
| deepcopy_reduce            | 3.17 us                                                | 2.81 us: 1.13x faster                                                   |
| mako                       | 11.1 ms                                                | 9.91 ms: 1.12x faster                                                   |
| scimark_monte_carlo        | 66.3 ms                                                | 59.6 ms: 1.11x faster                                                   |
| float                      | 78.5 ms                                                | 70.9 ms: 1.11x faster                                                   |
| async_tree_memoization     | 442 ms                                                 | 400 ms: 1.11x faster                                                    |
| xml_etree_generate         | 87.0 ms                                                | 79.1 ms: 1.10x faster                                                   |
| async_tree_none            | 354 ms                                                 | 325 ms: 1.09x faster                                                    |
| nbody                      | 85.7 ms                                                | 79.2 ms: 1.08x faster                                                   |
| telco                      | 8.45 ms                                                | 7.82 ms: 1.08x faster                                                   |
| xml_etree_process          | 60.4 ms                                                | 55.9 ms: 1.08x faster                                                   |
| crypto_pyaes               | 73.0 ms                                                | 67.8 ms: 1.08x faster                                                   |
| async_tree_none_tg         | 320 ms                                                 | 298 ms: 1.07x faster                                                    |
| gc_traversal               | 3.81 ms                                                | 3.55 ms: 1.07x faster                                                   |
| tomli_loads                | 2.11 sec                                               | 1.98 sec: 1.07x faster                                                  |
| xml_etree_parse            | 156 ms                                                 | 147 ms: 1.06x faster                                                    |
| pathlib                    | 17.1 ms                                                | 16.2 ms: 1.06x faster                                                   |
| pyflate                    | 460 ms                                                 | 436 ms: 1.05x faster                                                    |
| pycparser                  | 1.19 sec                                               | 1.14 sec: 1.05x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.52 sec: 1.04x faster                                                  |
| fannkuch                   | 381 ms                                                 | 368 ms: 1.04x faster                                                    |
| regex_v8                   | 25.3 ms                                                | 24.5 ms: 1.03x faster                                                   |
| html5lib                   | 64.5 ms                                                | 62.7 ms: 1.03x faster                                                   |
| unpickle_pure_python       | 213 us                                                 | 207 us: 1.03x faster                                                    |
| regex_effbot               | 3.88 ms                                                | 3.79 ms: 1.03x faster                                                   |
| xml_etree_iterparse        | 102 ms                                                 | 99.5 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 531 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 563 ms: 1.02x faster                                                    |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.02x faster                                                    |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                   |
| json                       | 5.20 ms                                                | 5.13 ms: 1.01x faster                                                   |
| thrift                     | 796 us                                                 | 787 us: 1.01x faster                                                    |
| pprint_safe_repr           | 744 ms                                                 | 737 ms: 1.01x faster                                                    |
| pprint_pformat             | 1.51 sec                                               | 1.50 sec: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 185 ms: 1.00x faster                                                    |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                  |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                    |
| bench_thread_pool          | 815 us                                                 | 822 us: 1.01x slower                                                    |
| logging_silent             | 102 ns                                                 | 103 ns: 1.01x slower                                                    |
| mdp                        | 2.74 sec                                               | 2.78 sec: 1.02x slower                                                  |
| python_startup_no_site     | 6.99 ms                                                | 7.14 ms: 1.02x slower                                                   |
| tornado_http               | 91.5 ms                                                | 94.0 ms: 1.03x slower                                                   |
| deltablue                  | 3.15 ms                                                | 3.26 ms: 1.04x slower                                                   |
| json_loads                 | 27.0 us                                                | 28.0 us: 1.04x slower                                                   |
| asyncio_tcp                | 488 ms                                                 | 507 ms: 1.04x slower                                                    |
| nqueens                    | 80.6 ms                                                | 84.1 ms: 1.04x slower                                                   |
| 2to3                       | 265 ms                                                 | 277 ms: 1.04x slower                                                    |
| sqlglot_transpile          | 1.57 ms                                                | 1.65 ms: 1.05x slower                                                   |
| go                         | 142 ms                                                 | 148 ms: 1.05x slower                                                    |
| regex_compile              | 131 ms                                                 | 137 ms: 1.05x slower                                                    |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.05x slower                                                   |
| pickle_pure_python         | 300 us                                                 | 315 us: 1.05x slower                                                    |
| raytrace                   | 262 ms                                                 | 275 ms: 1.05x slower                                                    |
| regex_dna                  | 220 ms                                                 | 231 ms: 1.05x slower                                                    |
| async_tree_io_tg           | 825 ms                                                 | 868 ms: 1.05x slower                                                    |
| sqlglot_normalize          | 107 ms                                                 | 114 ms: 1.06x slower                                                    |
| scimark_sor                | 122 ms                                                 | 130 ms: 1.06x slower                                                    |
| django_template            | 34.4 ms                                                | 36.6 ms: 1.06x slower                                                   |
| sqlglot_optimize           | 53.9 ms                                                | 57.4 ms: 1.06x slower                                                   |
| chaos                      | 58.4 ms                                                | 62.4 ms: 1.07x slower                                                   |
| async_generators           | 433 ms                                                 | 465 ms: 1.07x slower                                                    |
| dask                       | 338 ms                                                 | 365 ms: 1.08x slower                                                    |
| scimark_lu                 | 115 ms                                                 | 124 ms: 1.08x slower                                                    |
| typing_runtime_protocols   | 159 us                                                 | 172 us: 1.08x slower                                                    |
| async_tree_io              | 843 ms                                                 | 913 ms: 1.08x slower                                                    |
| create_gc_cycles           | 1.61 ms                                                | 1.74 ms: 1.08x slower                                                   |
| coverage                   | 83.7 ms                                                | 91.2 ms: 1.09x slower                                                   |
| sympy_str                  | 274 ms                                                 | 304 ms: 1.11x slower                                                    |
| hexiom                     | 6.13 ms                                                | 6.82 ms: 1.11x slower                                                   |
| sympy_expand               | 462 ms                                                 | 515 ms: 1.12x slower                                                    |
| genshi_text                | 22.9 ms                                                | 25.7 ms: 1.12x slower                                                   |
| genshi_xml                 | 50.3 ms                                                | 57.2 ms: 1.14x slower                                                   |
| sympy_integrate            | 19.9 ms                                                | 22.8 ms: 1.15x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.97 sec: 1.15x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 173 ms: 1.16x slower                                                    |
| pylint                     | 313 ms                                                 | 365 ms: 1.17x slower                                                    |
| generators                 | 28.8 ms                                                | 33.8 ms: 1.17x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (5): bench_mp_pool, comprehensions, logging_format, coroutines, logging_simple
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 52.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x
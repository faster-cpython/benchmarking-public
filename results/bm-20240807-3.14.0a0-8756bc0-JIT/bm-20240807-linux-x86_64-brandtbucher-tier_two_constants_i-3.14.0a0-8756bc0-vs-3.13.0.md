# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_constants_i
- machine: linux-x86_64
- commit hash: 8756bc0
- commit date: 2024-08-07
- overall geometric mean: 1.02x faster
- HPT reliability: 87.56%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 274 ms: 1.03x slower                                                        |
| docutils       | 2.58 sec                                               | 2.90 sec: 1.12x slower                                                      |
| html5lib       | 64.5 ms                                                | 65.9 ms: 1.02x slower                                                       |
| tornado_http   | 91.5 ms                                                | 92.6 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 392 ms: 1.18x faster                                                        |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                        |
| async_tree_none_tg         | 320 ms                                                 | 301 ms: 1.06x faster                                                        |
| async_tree_memoization     | 442 ms                                                 | 418 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 528 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 562 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| asyncio_tcp                | 488 ms                                                 | 499 ms: 1.02x slower                                                        |
| coroutines                 | 22.5 ms                                                | 23.1 ms: 1.03x slower                                                       |
| async_tree_io_tg           | 825 ms                                                 | 867 ms: 1.05x slower                                                        |
| async_generators           | 433 ms                                                 | 456 ms: 1.05x slower                                                        |
| async_tree_io              | 843 ms                                                 | 904 ms: 1.07x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.6 ms: 1.11x faster                                                       |
| nbody          | 85.7 ms                                                | 79.0 ms: 1.09x faster                                                       |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.58 ms: 1.09x faster                                                       |
| regex_v8       | 25.3 ms                                                | 24.5 ms: 1.03x faster                                                       |
| regex_dna      | 220 ms                                                 | 224 ms: 1.02x slower                                                        |
| regex_compile  | 131 ms                                                 | 134 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                      |
| xml_etree_generate   | 87.0 ms                                                | 79.7 ms: 1.09x faster                                                       |
| xml_etree_process    | 60.4 ms                                                | 56.3 ms: 1.07x faster                                                       |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                        |
| xml_etree_iterparse  | 102 ms                                                 | 99.0 ms: 1.03x faster                                                       |
| pickle_pure_python   | 300 us                                                 | 295 us: 1.02x faster                                                        |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                       |
| unpickle_pure_python | 213 us                                                 | 214 us: 1.00x slower                                                        |
| json_loads           | 27.0 us                                                | 28.8 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                       |
| python_startup_no_site | 6.99 ms                                                | 7.15 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.71 ms: 1.14x faster                                                       |
| django_template | 34.4 ms                                                | 35.9 ms: 1.04x slower                                                       |
| genshi_text     | 22.9 ms                                                | 24.0 ms: 1.05x slower                                                       |
| genshi_xml      | 50.3 ms                                                | 53.2 ms: 1.06x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 28.8 us: 1.32x faster                                                       |
| deepcopy                   | 352 us                                                 | 271 us: 1.30x faster                                                        |
| scimark_fft                | 369 ms                                                 | 310 ms: 1.19x faster                                                        |
| async_tree_memoization_tg  | 465 ms                                                 | 392 ms: 1.18x faster                                                        |
| richards                   | 48.1 ms                                                | 41.2 ms: 1.17x faster                                                       |
| richards_super             | 54.4 ms                                                | 47.2 ms: 1.15x faster                                                       |
| deepcopy_reduce            | 3.17 us                                                | 2.76 us: 1.15x faster                                                       |
| mako                       | 11.1 ms                                                | 9.71 ms: 1.14x faster                                                       |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                        |
| float                      | 78.5 ms                                                | 70.6 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.54 ms: 1.11x faster                                                       |
| crypto_pyaes               | 73.0 ms                                                | 66.2 ms: 1.10x faster                                                       |
| tomli_loads                | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                      |
| xml_etree_generate         | 87.0 ms                                                | 79.7 ms: 1.09x faster                                                       |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                        |
| regex_effbot               | 3.88 ms                                                | 3.58 ms: 1.09x faster                                                       |
| nbody                      | 85.7 ms                                                | 79.0 ms: 1.09x faster                                                       |
| telco                      | 8.45 ms                                                | 7.80 ms: 1.08x faster                                                       |
| scimark_monte_carlo        | 66.3 ms                                                | 61.4 ms: 1.08x faster                                                       |
| xml_etree_process          | 60.4 ms                                                | 56.3 ms: 1.07x faster                                                       |
| mdp                        | 2.74 sec                                               | 2.56 sec: 1.07x faster                                                      |
| scimark_sor                | 122 ms                                                 | 115 ms: 1.07x faster                                                        |
| pathlib                    | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                       |
| async_tree_none_tg         | 320 ms                                                 | 301 ms: 1.06x faster                                                        |
| scimark_lu                 | 115 ms                                                 | 108 ms: 1.06x faster                                                        |
| xml_etree_parse            | 156 ms                                                 | 147 ms: 1.06x faster                                                        |
| async_tree_memoization     | 442 ms                                                 | 418 ms: 1.06x faster                                                        |
| pycparser                  | 1.19 sec                                               | 1.13 sec: 1.06x faster                                                      |
| pyflate                    | 460 ms                                                 | 435 ms: 1.06x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.45 sec: 1.05x faster                                                      |
| gc_traversal               | 3.81 ms                                                | 3.67 ms: 1.04x faster                                                       |
| regex_v8                   | 25.3 ms                                                | 24.5 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 102 ms                                                 | 99.0 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 528 ms: 1.03x faster                                                        |
| fannkuch                   | 381 ms                                                 | 371 ms: 1.03x faster                                                        |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 562 ms: 1.02x faster                                                        |
| logging_simple             | 5.66 us                                                | 5.55 us: 1.02x faster                                                       |
| pprint_safe_repr           | 744 ms                                                 | 729 ms: 1.02x faster                                                        |
| logging_format             | 6.25 us                                                | 6.13 us: 1.02x faster                                                       |
| pickle_pure_python         | 300 us                                                 | 295 us: 1.02x faster                                                        |
| json                       | 5.20 ms                                                | 5.12 ms: 1.02x faster                                                       |
| thrift                     | 796 us                                                 | 787 us: 1.01x faster                                                        |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                       |
| comprehensions             | 16.4 us                                                | 16.2 us: 1.01x faster                                                       |
| chaos                      | 58.4 ms                                                | 58.1 ms: 1.01x faster                                                       |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                       |
| unpickle_pure_python       | 213 us                                                 | 214 us: 1.00x slower                                                        |
| bench_thread_pool          | 815 us                                                 | 819 us: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| tornado_http               | 91.5 ms                                                | 92.6 ms: 1.01x slower                                                       |
| regex_dna                  | 220 ms                                                 | 224 ms: 1.02x slower                                                        |
| html5lib                   | 64.5 ms                                                | 65.9 ms: 1.02x slower                                                       |
| regex_compile              | 131 ms                                                 | 134 ms: 1.02x slower                                                        |
| asyncio_tcp                | 488 ms                                                 | 499 ms: 1.02x slower                                                        |
| python_startup_no_site     | 6.99 ms                                                | 7.15 ms: 1.02x slower                                                       |
| raytrace                   | 262 ms                                                 | 268 ms: 1.03x slower                                                        |
| coroutines                 | 22.5 ms                                                | 23.1 ms: 1.03x slower                                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.30 ms: 1.03x slower                                                       |
| sqlglot_transpile          | 1.57 ms                                                | 1.62 ms: 1.03x slower                                                       |
| sqlglot_optimize           | 53.9 ms                                                | 55.6 ms: 1.03x slower                                                       |
| 2to3                       | 265 ms                                                 | 274 ms: 1.03x slower                                                        |
| go                         | 142 ms                                                 | 146 ms: 1.03x slower                                                        |
| nqueens                    | 80.6 ms                                                | 83.9 ms: 1.04x slower                                                       |
| django_template            | 34.4 ms                                                | 35.9 ms: 1.04x slower                                                       |
| genshi_text                | 22.9 ms                                                | 24.0 ms: 1.05x slower                                                       |
| async_tree_io_tg           | 825 ms                                                 | 867 ms: 1.05x slower                                                        |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.05x slower                                                        |
| async_generators           | 433 ms                                                 | 456 ms: 1.05x slower                                                        |
| genshi_xml                 | 50.3 ms                                                | 53.2 ms: 1.06x slower                                                       |
| typing_runtime_protocols   | 159 us                                                 | 170 us: 1.07x slower                                                        |
| json_loads                 | 27.0 us                                                | 28.8 us: 1.07x slower                                                       |
| async_tree_io              | 843 ms                                                 | 904 ms: 1.07x slower                                                        |
| hexiom                     | 6.13 ms                                                | 6.66 ms: 1.09x slower                                                       |
| create_gc_cycles           | 1.61 ms                                                | 1.76 ms: 1.09x slower                                                       |
| sympy_str                  | 274 ms                                                 | 299 ms: 1.09x slower                                                        |
| coverage                   | 83.7 ms                                                | 92.0 ms: 1.10x slower                                                       |
| sympy_expand               | 462 ms                                                 | 510 ms: 1.11x slower                                                        |
| docutils                   | 2.58 sec                                               | 2.90 sec: 1.12x slower                                                      |
| deltablue                  | 3.15 ms                                                | 3.54 ms: 1.13x slower                                                       |
| sympy_integrate            | 19.9 ms                                                | 22.5 ms: 1.13x slower                                                       |
| generators                 | 28.8 ms                                                | 32.6 ms: 1.13x slower                                                       |
| pylint                     | 313 ms                                                 | 355 ms: 1.14x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 170 ms: 1.14x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                |

Benchmark hidden because not significant (4): asyncio_websockets, bench_mp_pool, pprint_pformat, logging_silent
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 87.56% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x
# Results vs. 3.13.0

- fork: brandtbucher
- ref: replicate_more
- machine: linux-x86_64
- commit hash: 3a2f40c
- commit date: 2024-08-06
- overall geometric mean: 1.01x faster
- HPT reliability: 77.17%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 274 ms: 1.03x slower                                                  |
| docutils       | 2.58 sec                                               | 2.91 sec: 1.13x slower                                                |
| html5lib       | 64.5 ms                                                | 64.3 ms: 1.00x faster                                                 |
| tornado_http   | 91.5 ms                                                | 92.9 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 395 ms: 1.18x faster                                                  |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                  |
| async_tree_none_tg         | 320 ms                                                 | 302 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 532 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 563 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                |
| asyncio_tcp                | 488 ms                                                 | 497 ms: 1.02x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 872 ms: 1.06x slower                                                  |
| async_generators           | 433 ms                                                 | 461 ms: 1.06x slower                                                  |
| async_tree_io              | 843 ms                                                 | 909 ms: 1.08x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (3): async_tree_memoization, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 72.9 ms: 1.08x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 25.1 ms: 1.00x faster                                                 |
| regex_effbot   | 3.88 ms                                                | 3.90 ms: 1.00x slower                                                 |
| regex_compile  | 131 ms                                                 | 133 ms: 1.01x slower                                                  |
| regex_dna      | 220 ms                                                 | 229 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                |
| xml_etree_generate   | 87.0 ms                                                | 79.8 ms: 1.09x faster                                                 |
| xml_etree_process    | 60.4 ms                                                | 56.2 ms: 1.08x faster                                                 |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.06x faster                                                  |
| xml_etree_iterparse  | 102 ms                                                 | 99.5 ms: 1.03x faster                                                 |
| pickle_pure_python   | 300 us                                                 | 293 us: 1.02x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 214 us: 1.00x slower                                                  |
| json_loads           | 27.0 us                                                | 28.3 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.15 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.79 ms: 1.13x faster                                                 |
| genshi_xml      | 50.3 ms                                                | 52.9 ms: 1.05x slower                                                 |
| django_template | 34.4 ms                                                | 36.2 ms: 1.05x slower                                                 |
| genshi_text     | 22.9 ms                                                | 24.2 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 28.7 us: 1.32x faster                                                 |
| deepcopy                   | 352 us                                                 | 271 us: 1.30x faster                                                  |
| scimark_fft                | 369 ms                                                 | 302 ms: 1.22x faster                                                  |
| async_tree_memoization_tg  | 465 ms                                                 | 395 ms: 1.18x faster                                                  |
| richards                   | 48.1 ms                                                | 41.0 ms: 1.17x faster                                                 |
| deepcopy_reduce            | 3.17 us                                                | 2.70 us: 1.17x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.33 ms: 1.16x faster                                                 |
| richards_super             | 54.4 ms                                                | 47.2 ms: 1.15x faster                                                 |
| mako                       | 11.1 ms                                                | 9.79 ms: 1.13x faster                                                 |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                  |
| tomli_loads                | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                |
| scimark_monte_carlo        | 66.3 ms                                                | 60.7 ms: 1.09x faster                                                 |
| xml_etree_generate         | 87.0 ms                                                | 79.8 ms: 1.09x faster                                                 |
| crypto_pyaes               | 73.0 ms                                                | 67.1 ms: 1.09x faster                                                 |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                  |
| telco                      | 8.45 ms                                                | 7.81 ms: 1.08x faster                                                 |
| float                      | 78.5 ms                                                | 72.9 ms: 1.08x faster                                                 |
| xml_etree_process          | 60.4 ms                                                | 56.2 ms: 1.08x faster                                                 |
| mdp                        | 2.74 sec                                               | 2.57 sec: 1.07x faster                                                |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.06x faster                                                  |
| scimark_lu                 | 115 ms                                                 | 108 ms: 1.06x faster                                                  |
| scimark_sor                | 122 ms                                                 | 115 ms: 1.06x faster                                                  |
| async_tree_none_tg         | 320 ms                                                 | 302 ms: 1.06x faster                                                  |
| pathlib                    | 17.1 ms                                                | 16.3 ms: 1.05x faster                                                 |
| pyflate                    | 460 ms                                                 | 439 ms: 1.05x faster                                                  |
| pprint_safe_repr           | 744 ms                                                 | 711 ms: 1.05x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.50 sec: 1.04x faster                                                |
| fannkuch                   | 381 ms                                                 | 366 ms: 1.04x faster                                                  |
| pprint_pformat             | 1.51 sec                                               | 1.45 sec: 1.04x faster                                                |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 102 ms                                                 | 99.5 ms: 1.03x faster                                                 |
| pickle_pure_python         | 300 us                                                 | 293 us: 1.02x faster                                                  |
| logging_format             | 6.25 us                                                | 6.11 us: 1.02x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 532 ms: 1.02x faster                                                  |
| logging_simple             | 5.66 us                                                | 5.54 us: 1.02x faster                                                 |
| json                       | 5.20 ms                                                | 5.09 ms: 1.02x faster                                                 |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 563 ms: 1.02x faster                                                  |
| gc_traversal               | 3.81 ms                                                | 3.77 ms: 1.01x faster                                                 |
| regex_v8                   | 25.3 ms                                                | 25.1 ms: 1.00x faster                                                 |
| html5lib                   | 64.5 ms                                                | 64.3 ms: 1.00x faster                                                 |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                 |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                                  |
| regex_effbot               | 3.88 ms                                                | 3.90 ms: 1.00x slower                                                 |
| bench_thread_pool          | 815 us                                                 | 819 us: 1.00x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 214 us: 1.00x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                |
| regex_compile              | 131 ms                                                 | 133 ms: 1.01x slower                                                  |
| tornado_http               | 91.5 ms                                                | 92.9 ms: 1.01x slower                                                 |
| asyncio_tcp                | 488 ms                                                 | 497 ms: 1.02x slower                                                  |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                  |
| raytrace                   | 262 ms                                                 | 267 ms: 1.02x slower                                                  |
| python_startup_no_site     | 6.99 ms                                                | 7.15 ms: 1.02x slower                                                 |
| go                         | 142 ms                                                 | 145 ms: 1.03x slower                                                  |
| sqlglot_parse              | 1.27 ms                                                | 1.30 ms: 1.03x slower                                                 |
| 2to3                       | 265 ms                                                 | 274 ms: 1.03x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.63 ms: 1.03x slower                                                 |
| sqlglot_optimize           | 53.9 ms                                                | 55.8 ms: 1.03x slower                                                 |
| regex_dna                  | 220 ms                                                 | 229 ms: 1.04x slower                                                  |
| sqlglot_normalize          | 107 ms                                                 | 112 ms: 1.04x slower                                                  |
| json_loads                 | 27.0 us                                                | 28.3 us: 1.05x slower                                                 |
| genshi_xml                 | 50.3 ms                                                | 52.9 ms: 1.05x slower                                                 |
| django_template            | 34.4 ms                                                | 36.2 ms: 1.05x slower                                                 |
| nqueens                    | 80.6 ms                                                | 85.1 ms: 1.06x slower                                                 |
| genshi_text                | 22.9 ms                                                | 24.2 ms: 1.06x slower                                                 |
| async_tree_io_tg           | 825 ms                                                 | 872 ms: 1.06x slower                                                  |
| typing_runtime_protocols   | 159 us                                                 | 169 us: 1.06x slower                                                  |
| async_generators           | 433 ms                                                 | 461 ms: 1.06x slower                                                  |
| async_tree_io              | 843 ms                                                 | 909 ms: 1.08x slower                                                  |
| sympy_str                  | 274 ms                                                 | 298 ms: 1.09x slower                                                  |
| coverage                   | 83.7 ms                                                | 91.4 ms: 1.09x slower                                                 |
| hexiom                     | 6.13 ms                                                | 6.72 ms: 1.10x slower                                                 |
| sympy_expand               | 462 ms                                                 | 507 ms: 1.10x slower                                                  |
| create_gc_cycles           | 1.61 ms                                                | 1.77 ms: 1.10x slower                                                 |
| deltablue                  | 3.15 ms                                                | 3.52 ms: 1.12x slower                                                 |
| sympy_integrate            | 19.9 ms                                                | 22.4 ms: 1.12x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.91 sec: 1.13x slower                                                |
| sympy_sum                  | 150 ms                                                 | 170 ms: 1.13x slower                                                  |
| generators                 | 28.8 ms                                                | 32.8 ms: 1.14x slower                                                 |
| pylint                     | 313 ms                                                 | 356 ms: 1.14x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (9): async_tree_memoization, json_dumps, chaos, nbody, asyncio_websockets, thrift, bench_mp_pool, comprehensions, coroutines
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 77.17% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x
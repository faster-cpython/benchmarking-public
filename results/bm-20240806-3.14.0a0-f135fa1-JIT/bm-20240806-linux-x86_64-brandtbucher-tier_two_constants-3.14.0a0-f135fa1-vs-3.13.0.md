# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: f135fa1
- commit date: 2024-08-06
- overall geometric mean: 1.01x faster
- HPT reliability: 83.55%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 274 ms: 1.04x slower                                                      |
| docutils       | 2.58 sec                                               | 2.92 sec: 1.13x slower                                                    |
| html5lib       | 64.5 ms                                                | 65.8 ms: 1.02x slower                                                     |
| tornado_http   | 91.5 ms                                                | 92.7 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 396 ms: 1.17x faster                                                      |
| async_tree_none            | 354 ms                                                 | 328 ms: 1.08x faster                                                      |
| async_tree_none_tg         | 320 ms                                                 | 302 ms: 1.06x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 428 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 531 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 564 ms: 1.02x faster                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                     |
| asyncio_tcp                | 488 ms                                                 | 500 ms: 1.03x slower                                                      |
| async_tree_io_tg           | 825 ms                                                 | 875 ms: 1.06x slower                                                      |
| async_generators           | 433 ms                                                 | 469 ms: 1.08x slower                                                      |
| async_tree_io              | 843 ms                                                 | 917 ms: 1.09x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.6 ms: 1.10x faster                                                     |
| nbody          | 85.7 ms                                                | 79.2 ms: 1.08x faster                                                     |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.57 ms: 1.09x faster                                                     |
| regex_v8       | 25.3 ms                                                | 23.7 ms: 1.06x faster                                                     |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                                      |
| regex_compile  | 131 ms                                                 | 135 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.93 sec: 1.09x faster                                                    |
| xml_etree_generate   | 87.0 ms                                                | 79.9 ms: 1.09x faster                                                     |
| xml_etree_process    | 60.4 ms                                                | 56.6 ms: 1.07x faster                                                     |
| xml_etree_parse      | 156 ms                                                 | 149 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 102 ms                                                 | 99.4 ms: 1.03x faster                                                     |
| pickle_pure_python   | 300 us                                                 | 297 us: 1.01x faster                                                      |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                      |
| json_loads           | 27.0 us                                                | 28.6 us: 1.06x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                     |
| python_startup_no_site | 6.99 ms                                                | 7.20 ms: 1.03x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.87 ms: 1.12x faster                                                     |
| genshi_text     | 22.9 ms                                                | 24.0 ms: 1.05x slower                                                     |
| django_template | 34.4 ms                                                | 36.2 ms: 1.05x slower                                                     |
| genshi_xml      | 50.3 ms                                                | 53.6 ms: 1.06x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 29.2 us: 1.30x faster                                                     |
| deepcopy                   | 352 us                                                 | 275 us: 1.28x faster                                                      |
| scimark_fft                | 369 ms                                                 | 304 ms: 1.21x faster                                                      |
| async_tree_memoization_tg  | 465 ms                                                 | 396 ms: 1.17x faster                                                      |
| richards                   | 48.1 ms                                                | 41.7 ms: 1.15x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.36 ms: 1.15x faster                                                     |
| richards_super             | 54.4 ms                                                | 47.4 ms: 1.15x faster                                                     |
| deepcopy_reduce            | 3.17 us                                                | 2.80 us: 1.13x faster                                                     |
| mako                       | 11.1 ms                                                | 9.87 ms: 1.12x faster                                                     |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                      |
| scimark_monte_carlo        | 66.3 ms                                                | 60.4 ms: 1.10x faster                                                     |
| float                      | 78.5 ms                                                | 71.6 ms: 1.10x faster                                                     |
| tomli_loads                | 2.11 sec                                               | 1.93 sec: 1.09x faster                                                    |
| xml_etree_generate         | 87.0 ms                                                | 79.9 ms: 1.09x faster                                                     |
| regex_effbot               | 3.88 ms                                                | 3.57 ms: 1.09x faster                                                     |
| nbody                      | 85.7 ms                                                | 79.2 ms: 1.08x faster                                                     |
| async_tree_none            | 354 ms                                                 | 328 ms: 1.08x faster                                                      |
| crypto_pyaes               | 73.0 ms                                                | 68.0 ms: 1.07x faster                                                     |
| telco                      | 8.45 ms                                                | 7.91 ms: 1.07x faster                                                     |
| mdp                        | 2.74 sec                                               | 2.57 sec: 1.07x faster                                                    |
| xml_etree_process          | 60.4 ms                                                | 56.6 ms: 1.07x faster                                                     |
| regex_v8                   | 25.3 ms                                                | 23.7 ms: 1.06x faster                                                     |
| pycparser                  | 1.19 sec                                               | 1.12 sec: 1.06x faster                                                    |
| scimark_lu                 | 115 ms                                                 | 108 ms: 1.06x faster                                                      |
| async_tree_none_tg         | 320 ms                                                 | 302 ms: 1.06x faster                                                      |
| pyflate                    | 460 ms                                                 | 435 ms: 1.06x faster                                                      |
| scimark_sor                | 122 ms                                                 | 116 ms: 1.06x faster                                                      |
| gc_traversal               | 3.81 ms                                                | 3.61 ms: 1.05x faster                                                     |
| pathlib                    | 17.1 ms                                                | 16.3 ms: 1.05x faster                                                     |
| xml_etree_parse            | 156 ms                                                 | 149 ms: 1.05x faster                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.49 sec: 1.04x faster                                                    |
| fannkuch                   | 381 ms                                                 | 365 ms: 1.04x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 428 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 102 ms                                                 | 99.4 ms: 1.03x faster                                                     |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.02x faster                                                      |
| logging_format             | 6.25 us                                                | 6.11 us: 1.02x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 531 ms: 1.02x faster                                                      |
| regex_dna                  | 220 ms                                                 | 215 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 564 ms: 1.02x faster                                                      |
| logging_simple             | 5.66 us                                                | 5.57 us: 1.02x faster                                                     |
| pickle_pure_python         | 300 us                                                 | 297 us: 1.01x faster                                                      |
| pidigits                   | 186 ms                                                 | 185 ms: 1.00x faster                                                      |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                     |
| thrift                     | 796 us                                                 | 803 us: 1.01x slower                                                      |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                                      |
| bench_thread_pool          | 815 us                                                 | 823 us: 1.01x slower                                                      |
| tornado_http               | 91.5 ms                                                | 92.7 ms: 1.01x slower                                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                     |
| html5lib                   | 64.5 ms                                                | 65.8 ms: 1.02x slower                                                     |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                      |
| go                         | 142 ms                                                 | 145 ms: 1.02x slower                                                      |
| asyncio_tcp                | 488 ms                                                 | 500 ms: 1.03x slower                                                      |
| regex_compile              | 131 ms                                                 | 135 ms: 1.03x slower                                                      |
| python_startup_no_site     | 6.99 ms                                                | 7.20 ms: 1.03x slower                                                     |
| sqlglot_parse              | 1.27 ms                                                | 1.31 ms: 1.03x slower                                                     |
| sqlglot_transpile          | 1.57 ms                                                | 1.63 ms: 1.03x slower                                                     |
| 2to3                       | 265 ms                                                 | 274 ms: 1.04x slower                                                      |
| raytrace                   | 262 ms                                                 | 273 ms: 1.04x slower                                                      |
| sqlglot_optimize           | 53.9 ms                                                | 56.4 ms: 1.05x slower                                                     |
| genshi_text                | 22.9 ms                                                | 24.0 ms: 1.05x slower                                                     |
| django_template            | 34.4 ms                                                | 36.2 ms: 1.05x slower                                                     |
| nqueens                    | 80.6 ms                                                | 84.9 ms: 1.05x slower                                                     |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.06x slower                                                      |
| json_loads                 | 27.0 us                                                | 28.6 us: 1.06x slower                                                     |
| async_tree_io_tg           | 825 ms                                                 | 875 ms: 1.06x slower                                                      |
| genshi_xml                 | 50.3 ms                                                | 53.6 ms: 1.06x slower                                                     |
| async_generators           | 433 ms                                                 | 469 ms: 1.08x slower                                                      |
| typing_runtime_protocols   | 159 us                                                 | 173 us: 1.09x slower                                                      |
| async_tree_io              | 843 ms                                                 | 917 ms: 1.09x slower                                                      |
| coverage                   | 83.7 ms                                                | 91.6 ms: 1.09x slower                                                     |
| hexiom                     | 6.13 ms                                                | 6.71 ms: 1.10x slower                                                     |
| sympy_str                  | 274 ms                                                 | 302 ms: 1.11x slower                                                      |
| create_gc_cycles           | 1.61 ms                                                | 1.78 ms: 1.11x slower                                                     |
| sympy_expand               | 462 ms                                                 | 515 ms: 1.11x slower                                                      |
| docutils                   | 2.58 sec                                               | 2.92 sec: 1.13x slower                                                    |
| sympy_integrate            | 19.9 ms                                                | 22.7 ms: 1.14x slower                                                     |
| pylint                     | 313 ms                                                 | 357 ms: 1.14x slower                                                      |
| generators                 | 28.8 ms                                                | 32.9 ms: 1.14x slower                                                     |
| deltablue                  | 3.15 ms                                                | 3.60 ms: 1.14x slower                                                     |
| sympy_sum                  | 150 ms                                                 | 171 ms: 1.15x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (8): pprint_safe_repr, json, pprint_pformat, comprehensions, bench_mp_pool, asyncio_websockets, chaos, json_dumps
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 83.55% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x
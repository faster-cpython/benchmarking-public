# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: c5de9e3
- commit date: 2024-09-05
- overall geometric mean: 1.01x faster
- HPT reliability: 87.04%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 274 ms: 1.03x slower                                                      |
| docutils       | 2.58 sec                                               | 3.02 sec: 1.17x slower                                                    |
| tornado_http   | 91.5 ms                                                | 95.5 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.06x slower                                                              |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 402 ms: 1.16x faster                                                      |
| async_tree_memoization    | 442 ms                                                 | 401 ms: 1.10x faster                                                      |
| async_tree_none           | 354 ms                                                 | 327 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 556 ms: 1.03x faster                                                      |
| async_tree_none_tg        | 320 ms                                                 | 311 ms: 1.03x faster                                                      |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                    |
| async_generators          | 433 ms                                                 | 453 ms: 1.05x slower                                                      |
| async_tree_io             | 843 ms                                                 | 932 ms: 1.11x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 919 ms: 1.11x slower                                                      |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, asyncio_tcp, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.4 ms: 1.10x faster                                                     |
| nbody          | 85.7 ms                                                | 80.7 ms: 1.06x faster                                                     |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.64 ms: 1.07x faster                                                     |
| regex_v8       | 25.3 ms                                                | 24.4 ms: 1.04x faster                                                     |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                                      |
| regex_compile  | 131 ms                                                 | 140 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.6 ms: 1.12x faster                                                     |
| xml_etree_process    | 60.4 ms                                                | 54.7 ms: 1.10x faster                                                     |
| tomli_loads          | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                    |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 102 ms                                                 | 98.6 ms: 1.04x faster                                                     |
| unpickle_pure_python | 213 us                                                 | 211 us: 1.01x faster                                                      |
| pickle_pure_python   | 300 us                                                 | 298 us: 1.01x faster                                                      |
| json_loads           | 27.0 us                                                | 28.6 us: 1.06x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                     |
| python_startup_no_site | 6.99 ms                                                | 7.18 ms: 1.03x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.86 ms: 1.13x faster                                                     |
| django_template | 34.4 ms                                                | 35.5 ms: 1.03x slower                                                     |
| genshi_text     | 22.9 ms                                                | 24.9 ms: 1.09x slower                                                     |
| genshi_xml      | 50.3 ms                                                | 59.4 ms: 1.18x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                              |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 26.6 us: 1.43x faster                                                     |
| deepcopy                  | 352 us                                                 | 266 us: 1.33x faster                                                      |
| richards                  | 48.1 ms                                                | 39.1 ms: 1.23x faster                                                     |
| richards_super            | 54.4 ms                                                | 44.9 ms: 1.21x faster                                                     |
| scimark_fft               | 369 ms                                                 | 307 ms: 1.20x faster                                                      |
| deepcopy_reduce           | 3.17 us                                                | 2.65 us: 1.19x faster                                                     |
| spectral_norm             | 115 ms                                                 | 99.1 ms: 1.16x faster                                                     |
| async_tree_memoization_tg | 465 ms                                                 | 402 ms: 1.16x faster                                                      |
| mako                      | 11.1 ms                                                | 9.86 ms: 1.13x faster                                                     |
| xml_etree_generate        | 87.0 ms                                                | 77.6 ms: 1.12x faster                                                     |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.55 ms: 1.10x faster                                                     |
| async_tree_memoization    | 442 ms                                                 | 401 ms: 1.10x faster                                                      |
| xml_etree_process         | 60.4 ms                                                | 54.7 ms: 1.10x faster                                                     |
| crypto_pyaes              | 73.0 ms                                                | 66.2 ms: 1.10x faster                                                     |
| tomli_loads               | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                    |
| float                     | 78.5 ms                                                | 71.4 ms: 1.10x faster                                                     |
| go                        | 142 ms                                                 | 130 ms: 1.09x faster                                                      |
| mdp                       | 2.74 sec                                               | 2.53 sec: 1.08x faster                                                    |
| async_tree_none           | 354 ms                                                 | 327 ms: 1.08x faster                                                      |
| telco                     | 8.45 ms                                                | 7.89 ms: 1.07x faster                                                     |
| pathlib                   | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                     |
| regex_effbot              | 3.88 ms                                                | 3.64 ms: 1.07x faster                                                     |
| bpe_tokeniser             | 4.69 sec                                               | 4.41 sec: 1.06x faster                                                    |
| nbody                     | 85.7 ms                                                | 80.7 ms: 1.06x faster                                                     |
| scimark_monte_carlo       | 66.3 ms                                                | 62.5 ms: 1.06x faster                                                     |
| xml_etree_parse           | 156 ms                                                 | 148 ms: 1.06x faster                                                      |
| scimark_sor               | 122 ms                                                 | 116 ms: 1.06x faster                                                      |
| gc_traversal              | 3.81 ms                                                | 3.62 ms: 1.05x faster                                                     |
| pprint_safe_repr          | 744 ms                                                 | 713 ms: 1.04x faster                                                      |
| regex_v8                  | 25.3 ms                                                | 24.4 ms: 1.04x faster                                                     |
| xml_etree_iterparse       | 102 ms                                                 | 98.6 ms: 1.04x faster                                                     |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 556 ms: 1.03x faster                                                      |
| async_tree_none_tg        | 320 ms                                                 | 311 ms: 1.03x faster                                                      |
| thrift                    | 796 us                                                 | 776 us: 1.03x faster                                                      |
| logging_silent            | 102 ns                                                 | 99.5 ns: 1.03x faster                                                     |
| fannkuch                  | 381 ms                                                 | 372 ms: 1.02x faster                                                      |
| regex_dna                 | 220 ms                                                 | 215 ms: 1.02x faster                                                      |
| pyflate                   | 460 ms                                                 | 451 ms: 1.02x faster                                                      |
| pprint_pformat            | 1.51 sec                                               | 1.49 sec: 1.02x faster                                                    |
| scimark_lu                | 115 ms                                                 | 113 ms: 1.02x faster                                                      |
| pycparser                 | 1.19 sec                                               | 1.18 sec: 1.01x faster                                                    |
| unpickle_pure_python      | 213 us                                                 | 211 us: 1.01x faster                                                      |
| pickle_pure_python        | 300 us                                                 | 298 us: 1.01x faster                                                      |
| meteor_contest            | 108 ms                                                 | 107 ms: 1.01x faster                                                      |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                     |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                    |
| pidigits                  | 186 ms                                                 | 187 ms: 1.01x slower                                                      |
| deltablue                 | 3.15 ms                                                | 3.19 ms: 1.01x slower                                                     |
| comprehensions            | 16.4 us                                                | 16.7 us: 1.02x slower                                                     |
| typing_runtime_protocols  | 159 us                                                 | 162 us: 1.02x slower                                                      |
| bench_thread_pool         | 815 us                                                 | 833 us: 1.02x slower                                                      |
| json                      | 5.20 ms                                                | 5.32 ms: 1.02x slower                                                     |
| python_startup_no_site    | 6.99 ms                                                | 7.18 ms: 1.03x slower                                                     |
| django_template           | 34.4 ms                                                | 35.5 ms: 1.03x slower                                                     |
| 2to3                      | 265 ms                                                 | 274 ms: 1.03x slower                                                      |
| tornado_http              | 91.5 ms                                                | 95.5 ms: 1.04x slower                                                     |
| sqlglot_normalize         | 107 ms                                                 | 112 ms: 1.04x slower                                                      |
| async_generators          | 433 ms                                                 | 453 ms: 1.05x slower                                                      |
| sqlglot_parse             | 1.27 ms                                                | 1.33 ms: 1.05x slower                                                     |
| raytrace                  | 262 ms                                                 | 276 ms: 1.06x slower                                                      |
| nqueens                   | 80.6 ms                                                | 85.2 ms: 1.06x slower                                                     |
| json_loads                | 27.0 us                                                | 28.6 us: 1.06x slower                                                     |
| regex_compile             | 131 ms                                                 | 140 ms: 1.07x slower                                                      |
| sqlglot_transpile         | 1.57 ms                                                | 1.68 ms: 1.07x slower                                                     |
| sqlglot_optimize          | 53.9 ms                                                | 58.3 ms: 1.08x slower                                                     |
| dulwich_log               | 63.0 ms                                                | 68.1 ms: 1.08x slower                                                     |
| genshi_text               | 22.9 ms                                                | 24.9 ms: 1.09x slower                                                     |
| sympy_str                 | 274 ms                                                 | 300 ms: 1.10x slower                                                      |
| sympy_expand              | 462 ms                                                 | 507 ms: 1.10x slower                                                      |
| create_gc_cycles          | 1.61 ms                                                | 1.78 ms: 1.11x slower                                                     |
| async_tree_io             | 843 ms                                                 | 932 ms: 1.11x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 919 ms: 1.11x slower                                                      |
| hexiom                    | 6.13 ms                                                | 6.85 ms: 1.12x slower                                                     |
| coverage                  | 83.7 ms                                                | 94.0 ms: 1.12x slower                                                     |
| sympy_integrate           | 19.9 ms                                                | 22.8 ms: 1.15x slower                                                     |
| generators                | 28.8 ms                                                | 33.1 ms: 1.15x slower                                                     |
| sympy_sum                 | 150 ms                                                 | 173 ms: 1.16x slower                                                      |
| docutils                  | 2.58 sec                                               | 3.02 sec: 1.17x slower                                                    |
| genshi_xml                | 50.3 ms                                                | 59.4 ms: 1.18x slower                                                     |
| pylint                    | 313 ms                                                 | 372 ms: 1.19x slower                                                      |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed_tg, json_dumps, html5lib, logging_simple, logging_format, chaos, asyncio_tcp, asyncio_websockets, bench_mp_pool, coroutines
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 87.04% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x
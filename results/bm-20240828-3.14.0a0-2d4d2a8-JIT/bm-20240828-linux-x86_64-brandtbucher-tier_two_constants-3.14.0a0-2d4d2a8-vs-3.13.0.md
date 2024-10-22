# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: 2d4d2a8
- commit date: 2024-08-28
- overall geometric mean: 1.01x faster
- HPT reliability: 70.08%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 277 ms: 1.05x slower                                                      |
| docutils       | 2.58 sec                                               | 3.04 sec: 1.18x slower                                                    |
| html5lib       | 64.5 ms                                                | 64.2 ms: 1.01x faster                                                     |
| tornado_http   | 91.5 ms                                                | 94.4 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.06x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 404 ms: 1.15x faster                                                      |
| async_tree_none           | 354 ms                                                 | 328 ms: 1.08x faster                                                      |
| async_tree_memoization    | 442 ms                                                 | 417 ms: 1.06x faster                                                      |
| async_tree_none_tg        | 320 ms                                                 | 310 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 560 ms: 1.03x faster                                                      |
| asyncio_tcp               | 488 ms                                                 | 492 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| coroutines                | 22.5 ms                                                | 23.6 ms: 1.05x slower                                                     |
| async_generators          | 433 ms                                                 | 459 ms: 1.06x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 902 ms: 1.09x slower                                                      |
| async_tree_io             | 843 ms                                                 | 938 ms: 1.11x slower                                                      |
| Geometric mean            | (ref)                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.8 ms: 1.11x faster                                                     |
| nbody          | 85.7 ms                                                | 79.6 ms: 1.08x faster                                                     |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.56 ms: 1.09x faster                                                     |
| regex_v8       | 25.3 ms                                                | 24.3 ms: 1.04x faster                                                     |
| regex_dna      | 220 ms                                                 | 213 ms: 1.03x faster                                                      |
| regex_compile  | 131 ms                                                 | 141 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.6 ms: 1.12x faster                                                     |
| xml_etree_process    | 60.4 ms                                                | 54.5 ms: 1.11x faster                                                     |
| tomli_loads          | 2.11 sec                                               | 1.93 sec: 1.10x faster                                                    |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.06x faster                                                      |
| json_dumps           | 10.4 ms                                                | 9.96 ms: 1.04x faster                                                     |
| xml_etree_iterparse  | 102 ms                                                 | 98.6 ms: 1.03x faster                                                     |
| pickle_pure_python   | 300 us                                                 | 302 us: 1.01x slower                                                      |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                      |
| json_loads           | 27.0 us                                                | 28.8 us: 1.07x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                     |
| python_startup_no_site | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.67 ms: 1.15x faster                                                     |
| genshi_text     | 22.9 ms                                                | 24.1 ms: 1.05x slower                                                     |
| django_template | 34.4 ms                                                | 36.7 ms: 1.07x slower                                                     |
| genshi_xml      | 50.3 ms                                                | 56.7 ms: 1.13x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                              |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 26.9 us: 1.41x faster                                                     |
| deepcopy                  | 352 us                                                 | 261 us: 1.35x faster                                                      |
| richards                  | 48.1 ms                                                | 39.3 ms: 1.23x faster                                                     |
| richards_super            | 54.4 ms                                                | 45.0 ms: 1.21x faster                                                     |
| deepcopy_reduce           | 3.17 us                                                | 2.63 us: 1.20x faster                                                     |
| scimark_fft               | 369 ms                                                 | 307 ms: 1.20x faster                                                      |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.30 ms: 1.17x faster                                                     |
| spectral_norm             | 115 ms                                                 | 98.5 ms: 1.17x faster                                                     |
| async_tree_memoization_tg | 465 ms                                                 | 404 ms: 1.15x faster                                                      |
| mako                      | 11.1 ms                                                | 9.67 ms: 1.15x faster                                                     |
| xml_etree_generate        | 87.0 ms                                                | 77.6 ms: 1.12x faster                                                     |
| crypto_pyaes              | 73.0 ms                                                | 65.6 ms: 1.11x faster                                                     |
| telco                     | 8.45 ms                                                | 7.62 ms: 1.11x faster                                                     |
| float                     | 78.5 ms                                                | 70.8 ms: 1.11x faster                                                     |
| xml_etree_process         | 60.4 ms                                                | 54.5 ms: 1.11x faster                                                     |
| tomli_loads               | 2.11 sec                                               | 1.93 sec: 1.10x faster                                                    |
| regex_effbot              | 3.88 ms                                                | 3.56 ms: 1.09x faster                                                     |
| pathlib                   | 17.1 ms                                                | 15.8 ms: 1.08x faster                                                     |
| async_tree_none           | 354 ms                                                 | 328 ms: 1.08x faster                                                      |
| nbody                     | 85.7 ms                                                | 79.6 ms: 1.08x faster                                                     |
| mdp                       | 2.74 sec                                               | 2.56 sec: 1.07x faster                                                    |
| bpe_tokeniser             | 4.69 sec                                               | 4.40 sec: 1.07x faster                                                    |
| async_tree_memoization    | 442 ms                                                 | 417 ms: 1.06x faster                                                      |
| xml_etree_parse           | 156 ms                                                 | 148 ms: 1.06x faster                                                      |
| pyflate                   | 460 ms                                                 | 435 ms: 1.06x faster                                                      |
| scimark_monte_carlo       | 66.3 ms                                                | 63.2 ms: 1.05x faster                                                     |
| json_dumps                | 10.4 ms                                                | 9.96 ms: 1.04x faster                                                     |
| regex_v8                  | 25.3 ms                                                | 24.3 ms: 1.04x faster                                                     |
| scimark_lu                | 115 ms                                                 | 110 ms: 1.04x faster                                                      |
| scimark_sor               | 122 ms                                                 | 118 ms: 1.04x faster                                                      |
| gc_traversal              | 3.81 ms                                                | 3.67 ms: 1.04x faster                                                     |
| xml_etree_iterparse       | 102 ms                                                 | 98.6 ms: 1.03x faster                                                     |
| async_tree_none_tg        | 320 ms                                                 | 310 ms: 1.03x faster                                                      |
| regex_dna                 | 220 ms                                                 | 213 ms: 1.03x faster                                                      |
| fannkuch                  | 381 ms                                                 | 370 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 560 ms: 1.03x faster                                                      |
| pprint_safe_repr          | 744 ms                                                 | 730 ms: 1.02x faster                                                      |
| logging_simple            | 5.66 us                                                | 5.61 us: 1.01x faster                                                     |
| meteor_contest            | 108 ms                                                 | 107 ms: 1.01x faster                                                      |
| logging_format            | 6.25 us                                                | 6.21 us: 1.01x faster                                                     |
| html5lib                  | 64.5 ms                                                | 64.2 ms: 1.01x faster                                                     |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                     |
| bench_thread_pool         | 815 us                                                 | 816 us: 1.00x slower                                                      |
| pickle_pure_python        | 300 us                                                 | 302 us: 1.01x slower                                                      |
| asyncio_tcp               | 488 ms                                                 | 492 ms: 1.01x slower                                                      |
| pycparser                 | 1.19 sec                                               | 1.20 sec: 1.01x slower                                                    |
| thrift                    | 796 us                                                 | 803 us: 1.01x slower                                                      |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| unpickle_pure_python      | 213 us                                                 | 216 us: 1.01x slower                                                      |
| comprehensions            | 16.4 us                                                | 16.6 us: 1.01x slower                                                     |
| logging_silent            | 102 ns                                                 | 104 ns: 1.02x slower                                                      |
| deltablue                 | 3.15 ms                                                | 3.22 ms: 1.02x slower                                                     |
| python_startup_no_site    | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                     |
| typing_runtime_protocols  | 159 us                                                 | 164 us: 1.03x slower                                                      |
| tornado_http              | 91.5 ms                                                | 94.4 ms: 1.03x slower                                                     |
| json                      | 5.20 ms                                                | 5.38 ms: 1.03x slower                                                     |
| coverage                  | 83.7 ms                                                | 87.1 ms: 1.04x slower                                                     |
| sqlglot_normalize         | 107 ms                                                 | 112 ms: 1.04x slower                                                      |
| nqueens                   | 80.6 ms                                                | 84.3 ms: 1.05x slower                                                     |
| 2to3                      | 265 ms                                                 | 277 ms: 1.05x slower                                                      |
| coroutines                | 22.5 ms                                                | 23.6 ms: 1.05x slower                                                     |
| genshi_text               | 22.9 ms                                                | 24.1 ms: 1.05x slower                                                     |
| async_generators          | 433 ms                                                 | 459 ms: 1.06x slower                                                      |
| raytrace                  | 262 ms                                                 | 277 ms: 1.06x slower                                                      |
| django_template           | 34.4 ms                                                | 36.7 ms: 1.07x slower                                                     |
| json_loads                | 27.0 us                                                | 28.8 us: 1.07x slower                                                     |
| sqlglot_parse             | 1.27 ms                                                | 1.35 ms: 1.07x slower                                                     |
| sqlglot_transpile         | 1.57 ms                                                | 1.69 ms: 1.07x slower                                                     |
| regex_compile             | 131 ms                                                 | 141 ms: 1.08x slower                                                      |
| sqlglot_optimize          | 53.9 ms                                                | 58.1 ms: 1.08x slower                                                     |
| sympy_str                 | 274 ms                                                 | 299 ms: 1.09x slower                                                      |
| sympy_expand              | 462 ms                                                 | 504 ms: 1.09x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 902 ms: 1.09x slower                                                      |
| async_tree_io             | 843 ms                                                 | 938 ms: 1.11x slower                                                      |
| create_gc_cycles          | 1.61 ms                                                | 1.79 ms: 1.11x slower                                                     |
| hexiom                    | 6.13 ms                                                | 6.86 ms: 1.12x slower                                                     |
| genshi_xml                | 50.3 ms                                                | 56.7 ms: 1.13x slower                                                     |
| generators                | 28.8 ms                                                | 32.6 ms: 1.13x slower                                                     |
| sympy_sum                 | 150 ms                                                 | 171 ms: 1.15x slower                                                      |
| sympy_integrate           | 19.9 ms                                                | 22.8 ms: 1.15x slower                                                     |
| docutils                  | 2.58 sec                                               | 3.04 sec: 1.18x slower                                                    |
| pylint                    | 313 ms                                                 | 372 ms: 1.19x slower                                                      |
| go                        | 142 ms                                                 | 170 ms: 1.20x slower                                                      |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed_tg, bench_mp_pool, asyncio_websockets, chaos, pprint_pformat
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 70.08% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x
# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: 85c5a08
- commit date: 2024-08-21
- overall geometric mean: 1.01x faster
- HPT reliability: 53.44%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 283 ms: 1.07x slower                                                      |
| docutils       | 2.58 sec                                               | 3.06 sec: 1.18x slower                                                    |
| html5lib       | 64.5 ms                                                | 66.4 ms: 1.03x slower                                                     |
| tornado_http   | 91.5 ms                                                | 94.1 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.08x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 398 ms: 1.17x faster                                                      |
| async_tree_none           | 354 ms                                                 | 329 ms: 1.08x faster                                                      |
| async_tree_none_tg        | 320 ms                                                 | 305 ms: 1.05x faster                                                      |
| async_tree_memoization    | 442 ms                                                 | 429 ms: 1.03x faster                                                      |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                    |
| coroutines                | 22.5 ms                                                | 22.7 ms: 1.01x slower                                                     |
| asyncio_tcp               | 488 ms                                                 | 496 ms: 1.02x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 868 ms: 1.05x slower                                                      |
| async_generators          | 433 ms                                                 | 461 ms: 1.07x slower                                                      |
| async_tree_io             | 843 ms                                                 | 903 ms: 1.07x slower                                                      |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.1 ms: 1.10x faster                                                     |
| nbody          | 85.7 ms                                                | 82.2 ms: 1.04x faster                                                     |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.55 ms: 1.10x faster                                                     |
| regex_v8       | 25.3 ms                                                | 23.8 ms: 1.06x faster                                                     |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                                      |
| regex_compile  | 131 ms                                                 | 143 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate  | 87.0 ms                                                | 78.1 ms: 1.11x faster                                                     |
| tomli_loads         | 2.11 sec                                               | 1.93 sec: 1.09x faster                                                    |
| xml_etree_process   | 60.4 ms                                                | 55.9 ms: 1.08x faster                                                     |
| xml_etree_parse     | 156 ms                                                 | 148 ms: 1.06x faster                                                      |
| xml_etree_iterparse | 102 ms                                                 | 98.9 ms: 1.03x faster                                                     |
| json_dumps          | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                     |
| pickle_pure_python  | 300 us                                                 | 306 us: 1.02x slower                                                      |
| json_loads          | 27.0 us                                                | 28.3 us: 1.05x slower                                                     |
| Geometric mean      | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                     |
| python_startup_no_site | 6.99 ms                                                | 7.12 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.74 ms: 1.14x faster                                                     |
| django_template | 34.4 ms                                                | 36.8 ms: 1.07x slower                                                     |
| genshi_text     | 22.9 ms                                                | 25.6 ms: 1.12x slower                                                     |
| genshi_xml      | 50.3 ms                                                | 60.0 ms: 1.19x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                              |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 27.3 us: 1.40x faster                                                     |
| deepcopy                  | 352 us                                                 | 266 us: 1.32x faster                                                      |
| richards                  | 48.1 ms                                                | 39.4 ms: 1.22x faster                                                     |
| richards_super            | 54.4 ms                                                | 44.7 ms: 1.22x faster                                                     |
| deepcopy_reduce           | 3.17 us                                                | 2.64 us: 1.20x faster                                                     |
| scimark_fft               | 369 ms                                                 | 308 ms: 1.20x faster                                                      |
| async_tree_memoization_tg | 465 ms                                                 | 398 ms: 1.17x faster                                                      |
| spectral_norm             | 115 ms                                                 | 99.6 ms: 1.15x faster                                                     |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.37 ms: 1.15x faster                                                     |
| mako                      | 11.1 ms                                                | 9.74 ms: 1.14x faster                                                     |
| crypto_pyaes              | 73.0 ms                                                | 65.3 ms: 1.12x faster                                                     |
| xml_etree_generate        | 87.0 ms                                                | 78.1 ms: 1.11x faster                                                     |
| float                     | 78.5 ms                                                | 71.1 ms: 1.10x faster                                                     |
| telco                     | 8.45 ms                                                | 7.69 ms: 1.10x faster                                                     |
| regex_effbot              | 3.88 ms                                                | 3.55 ms: 1.10x faster                                                     |
| tomli_loads               | 2.11 sec                                               | 1.93 sec: 1.09x faster                                                    |
| xml_etree_process         | 60.4 ms                                                | 55.9 ms: 1.08x faster                                                     |
| async_tree_none           | 354 ms                                                 | 329 ms: 1.08x faster                                                      |
| gc_traversal              | 3.81 ms                                                | 3.56 ms: 1.07x faster                                                     |
| mdp                       | 2.74 sec                                               | 2.57 sec: 1.07x faster                                                    |
| regex_v8                  | 25.3 ms                                                | 23.8 ms: 1.06x faster                                                     |
| pathlib                   | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                     |
| scimark_sor               | 122 ms                                                 | 116 ms: 1.06x faster                                                      |
| scimark_monte_carlo       | 66.3 ms                                                | 62.6 ms: 1.06x faster                                                     |
| xml_etree_parse           | 156 ms                                                 | 148 ms: 1.06x faster                                                      |
| async_tree_none_tg        | 320 ms                                                 | 305 ms: 1.05x faster                                                      |
| pyflate                   | 460 ms                                                 | 438 ms: 1.05x faster                                                      |
| bpe_tokeniser             | 4.69 sec                                               | 4.49 sec: 1.04x faster                                                    |
| nbody                     | 85.7 ms                                                | 82.2 ms: 1.04x faster                                                     |
| logging_format            | 6.25 us                                                | 6.00 us: 1.04x faster                                                     |
| async_tree_memoization    | 442 ms                                                 | 429 ms: 1.03x faster                                                      |
| scimark_lu                | 115 ms                                                 | 111 ms: 1.03x faster                                                      |
| xml_etree_iterparse       | 102 ms                                                 | 98.9 ms: 1.03x faster                                                     |
| logging_simple            | 5.66 us                                                | 5.51 us: 1.03x faster                                                     |
| regex_dna                 | 220 ms                                                 | 215 ms: 1.02x faster                                                      |
| fannkuch                  | 381 ms                                                 | 373 ms: 1.02x faster                                                      |
| json_dumps                | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                     |
| pycparser                 | 1.19 sec                                               | 1.18 sec: 1.01x faster                                                    |
| meteor_contest            | 108 ms                                                 | 106 ms: 1.01x faster                                                      |
| thrift                    | 796 us                                                 | 787 us: 1.01x faster                                                      |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                     |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                    |
| logging_silent            | 102 ns                                                 | 103 ns: 1.01x slower                                                      |
| chaos                     | 58.4 ms                                                | 58.9 ms: 1.01x slower                                                     |
| bench_thread_pool         | 815 us                                                 | 822 us: 1.01x slower                                                      |
| coroutines                | 22.5 ms                                                | 22.7 ms: 1.01x slower                                                     |
| pprint_safe_repr          | 744 ms                                                 | 755 ms: 1.01x slower                                                      |
| comprehensions            | 16.4 us                                                | 16.6 us: 1.02x slower                                                     |
| asyncio_tcp               | 488 ms                                                 | 496 ms: 1.02x slower                                                      |
| coverage                  | 83.7 ms                                                | 85.1 ms: 1.02x slower                                                     |
| pickle_pure_python        | 300 us                                                 | 306 us: 1.02x slower                                                      |
| python_startup_no_site    | 6.99 ms                                                | 7.12 ms: 1.02x slower                                                     |
| json                      | 5.20 ms                                                | 5.34 ms: 1.03x slower                                                     |
| pprint_pformat            | 1.51 sec                                               | 1.55 sec: 1.03x slower                                                    |
| tornado_http              | 91.5 ms                                                | 94.1 ms: 1.03x slower                                                     |
| html5lib                  | 64.5 ms                                                | 66.4 ms: 1.03x slower                                                     |
| go                        | 142 ms                                                 | 148 ms: 1.04x slower                                                      |
| sqlglot_parse             | 1.27 ms                                                | 1.32 ms: 1.05x slower                                                     |
| raytrace                  | 262 ms                                                 | 274 ms: 1.05x slower                                                      |
| json_loads                | 27.0 us                                                | 28.3 us: 1.05x slower                                                     |
| async_tree_io_tg          | 825 ms                                                 | 868 ms: 1.05x slower                                                      |
| async_generators          | 433 ms                                                 | 461 ms: 1.07x slower                                                      |
| sqlglot_normalize         | 107 ms                                                 | 115 ms: 1.07x slower                                                      |
| typing_runtime_protocols  | 159 us                                                 | 170 us: 1.07x slower                                                      |
| 2to3                      | 265 ms                                                 | 283 ms: 1.07x slower                                                      |
| nqueens                   | 80.6 ms                                                | 86.1 ms: 1.07x slower                                                     |
| django_template           | 34.4 ms                                                | 36.8 ms: 1.07x slower                                                     |
| async_tree_io             | 843 ms                                                 | 903 ms: 1.07x slower                                                      |
| sqlglot_transpile         | 1.57 ms                                                | 1.70 ms: 1.08x slower                                                     |
| sqlglot_optimize          | 53.9 ms                                                | 58.2 ms: 1.08x slower                                                     |
| create_gc_cycles          | 1.61 ms                                                | 1.74 ms: 1.08x slower                                                     |
| regex_compile             | 131 ms                                                 | 143 ms: 1.09x slower                                                      |
| sympy_expand              | 462 ms                                                 | 514 ms: 1.11x slower                                                      |
| sympy_str                 | 274 ms                                                 | 306 ms: 1.12x slower                                                      |
| genshi_text               | 22.9 ms                                                | 25.6 ms: 1.12x slower                                                     |
| hexiom                    | 6.13 ms                                                | 6.87 ms: 1.12x slower                                                     |
| generators                | 28.8 ms                                                | 32.6 ms: 1.13x slower                                                     |
| sympy_integrate           | 19.9 ms                                                | 23.3 ms: 1.17x slower                                                     |
| docutils                  | 2.58 sec                                               | 3.06 sec: 1.18x slower                                                    |
| sympy_sum                 | 150 ms                                                 | 178 ms: 1.19x slower                                                      |
| genshi_xml                | 50.3 ms                                                | 60.0 ms: 1.19x slower                                                     |
| pylint                    | 313 ms                                                 | 373 ms: 1.19x slower                                                      |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, deltablue, asyncio_websockets, bench_mp_pool, unpickle_pure_python
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 53.44% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x
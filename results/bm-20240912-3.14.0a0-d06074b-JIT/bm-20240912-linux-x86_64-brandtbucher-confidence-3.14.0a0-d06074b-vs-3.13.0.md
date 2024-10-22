# Results vs. 3.13.0

- fork: brandtbucher
- ref: confidence
- machine: linux-x86_64
- commit hash: d06074b
- commit date: 2024-09-12
- overall geometric mean: 1.01x faster
- HPT reliability: 90.59%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 273 ms: 1.03x slower                                              |
| docutils       | 2.58 sec                                               | 2.96 sec: 1.15x slower                                            |
| tornado_http   | 91.5 ms                                                | 94.9 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                  | 1.05x slower                                                      |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 384 ms: 1.21x faster                                              |
| async_tree_memoization     | 442 ms                                                 | 393 ms: 1.13x faster                                              |
| async_tree_none            | 354 ms                                                 | 315 ms: 1.12x faster                                              |
| async_tree_none_tg         | 320 ms                                                 | 303 ms: 1.06x faster                                              |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                            |
| asyncio_tcp                | 488 ms                                                 | 494 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 552 ms: 1.02x slower                                              |
| async_generators           | 433 ms                                                 | 455 ms: 1.05x slower                                              |
| async_tree_io_tg           | 825 ms                                                 | 873 ms: 1.06x slower                                              |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                      |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, asyncio_websockets, coroutines, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.9 ms: 1.12x faster                                             |
| nbody          | 85.7 ms                                                | 79.9 ms: 1.07x faster                                             |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                  | 1.07x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 24.4 ms: 1.03x faster                                             |
| regex_effbot   | 3.88 ms                                                | 3.82 ms: 1.02x faster                                             |
| regex_dna      | 220 ms                                                 | 221 ms: 1.01x slower                                              |
| regex_compile  | 131 ms                                                 | 140 ms: 1.07x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 76.9 ms: 1.13x faster                                             |
| xml_etree_process    | 60.4 ms                                                | 54.6 ms: 1.11x faster                                             |
| tomli_loads          | 2.11 sec                                               | 1.94 sec: 1.09x faster                                            |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.07x faster                                              |
| xml_etree_iterparse  | 102 ms                                                 | 98.3 ms: 1.04x faster                                             |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                             |
| unpickle             | 14.9 us                                                | 14.4 us: 1.03x faster                                             |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                             |
| pickle_pure_python   | 300 us                                                 | 304 us: 1.01x slower                                              |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                              |
| unpickle_list        | 4.96 us                                                | 5.07 us: 1.02x slower                                             |
| pickle_list          | 5.01 us                                                | 5.24 us: 1.05x slower                                             |
| pickle_dict          | 33.2 us                                                | 34.9 us: 1.05x slower                                             |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                      |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                             |
| python_startup_no_site | 6.99 ms                                                | 7.04 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.85 ms: 1.13x faster                                             |
| django_template | 34.4 ms                                                | 35.9 ms: 1.04x slower                                             |
| genshi_text     | 22.9 ms                                                | 24.8 ms: 1.08x slower                                             |
| genshi_xml      | 50.3 ms                                                | 56.4 ms: 1.12x slower                                             |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 27.0 us: 1.41x faster                                             |
| deepcopy                   | 352 us                                                 | 259 us: 1.36x faster                                              |
| richards_super             | 54.4 ms                                                | 43.3 ms: 1.26x faster                                             |
| richards                   | 48.1 ms                                                | 39.3 ms: 1.22x faster                                             |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.11 ms: 1.22x faster                                             |
| async_tree_memoization_tg  | 465 ms                                                 | 384 ms: 1.21x faster                                              |
| deepcopy_reduce            | 3.17 us                                                | 2.64 us: 1.20x faster                                             |
| scimark_fft                | 369 ms                                                 | 308 ms: 1.20x faster                                              |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                              |
| xml_etree_generate         | 87.0 ms                                                | 76.9 ms: 1.13x faster                                             |
| mako                       | 11.1 ms                                                | 9.85 ms: 1.13x faster                                             |
| async_tree_memoization     | 442 ms                                                 | 393 ms: 1.13x faster                                              |
| async_tree_none            | 354 ms                                                 | 315 ms: 1.12x faster                                              |
| float                      | 78.5 ms                                                | 69.9 ms: 1.12x faster                                             |
| crypto_pyaes               | 73.0 ms                                                | 66.0 ms: 1.11x faster                                             |
| xml_etree_process          | 60.4 ms                                                | 54.6 ms: 1.11x faster                                             |
| tomli_loads                | 2.11 sec                                               | 1.94 sec: 1.09x faster                                            |
| go                         | 142 ms                                                 | 131 ms: 1.08x faster                                              |
| nbody                      | 85.7 ms                                                | 79.9 ms: 1.07x faster                                             |
| xml_etree_parse            | 156 ms                                                 | 145 ms: 1.07x faster                                              |
| pathlib                    | 17.1 ms                                                | 15.9 ms: 1.07x faster                                             |
| pyflate                    | 460 ms                                                 | 430 ms: 1.07x faster                                              |
| scimark_monte_carlo        | 66.3 ms                                                | 62.3 ms: 1.06x faster                                             |
| bpe_tokeniser              | 4.69 sec                                               | 4.43 sec: 1.06x faster                                            |
| telco                      | 8.45 ms                                                | 8.00 ms: 1.06x faster                                             |
| async_tree_none_tg         | 320 ms                                                 | 303 ms: 1.06x faster                                              |
| scimark_sor                | 122 ms                                                 | 116 ms: 1.05x faster                                              |
| pprint_safe_repr           | 744 ms                                                 | 710 ms: 1.05x faster                                              |
| scimark_lu                 | 115 ms                                                 | 111 ms: 1.04x faster                                              |
| xml_etree_iterparse        | 102 ms                                                 | 98.3 ms: 1.04x faster                                             |
| json                       | 5.20 ms                                                | 5.01 ms: 1.04x faster                                             |
| regex_v8                   | 25.3 ms                                                | 24.4 ms: 1.03x faster                                             |
| mdp                        | 2.74 sec                                               | 2.66 sec: 1.03x faster                                            |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                             |
| unpickle                   | 14.9 us                                                | 14.4 us: 1.03x faster                                             |
| pprint_pformat             | 1.51 sec                                               | 1.47 sec: 1.03x faster                                            |
| sqlite_synth               | 2.85 us                                                | 2.78 us: 1.03x faster                                             |
| pycparser                  | 1.19 sec                                               | 1.16 sec: 1.03x faster                                            |
| logging_format             | 6.25 us                                                | 6.11 us: 1.02x faster                                             |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                              |
| fannkuch                   | 381 ms                                                 | 375 ms: 1.02x faster                                              |
| regex_effbot               | 3.88 ms                                                | 3.82 ms: 1.02x faster                                             |
| thrift                     | 796 us                                                 | 789 us: 1.01x faster                                              |
| logging_simple             | 5.66 us                                                | 5.61 us: 1.01x faster                                             |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                             |
| pidigits                   | 186 ms                                                 | 185 ms: 1.00x faster                                              |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                            |
| regex_dna                  | 220 ms                                                 | 221 ms: 1.01x slower                                              |
| python_startup_no_site     | 6.99 ms                                                | 7.04 ms: 1.01x slower                                             |
| coverage                   | 83.7 ms                                                | 84.4 ms: 1.01x slower                                             |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                             |
| asyncio_tcp                | 488 ms                                                 | 494 ms: 1.01x slower                                              |
| chaos                      | 58.4 ms                                                | 59.2 ms: 1.01x slower                                             |
| pickle_pure_python         | 300 us                                                 | 304 us: 1.01x slower                                              |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 552 ms: 1.02x slower                                              |
| comprehensions             | 16.4 us                                                | 16.7 us: 1.02x slower                                             |
| typing_runtime_protocols   | 159 us                                                 | 162 us: 1.02x slower                                              |
| unpickle_list              | 4.96 us                                                | 5.07 us: 1.02x slower                                             |
| logging_silent             | 102 ns                                                 | 105 ns: 1.02x slower                                              |
| bench_thread_pool          | 815 us                                                 | 838 us: 1.03x slower                                              |
| deltablue                  | 3.15 ms                                                | 3.24 ms: 1.03x slower                                             |
| 2to3                       | 265 ms                                                 | 273 ms: 1.03x slower                                              |
| tornado_http               | 91.5 ms                                                | 94.9 ms: 1.04x slower                                             |
| django_template            | 34.4 ms                                                | 35.9 ms: 1.04x slower                                             |
| nqueens                    | 80.6 ms                                                | 84.1 ms: 1.04x slower                                             |
| pickle_list                | 5.01 us                                                | 5.24 us: 1.05x slower                                             |
| gc_traversal               | 3.81 ms                                                | 3.98 ms: 1.05x slower                                             |
| async_generators           | 433 ms                                                 | 455 ms: 1.05x slower                                              |
| pickle_dict                | 33.2 us                                                | 34.9 us: 1.05x slower                                             |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.05x slower                                              |
| raytrace                   | 262 ms                                                 | 276 ms: 1.06x slower                                              |
| async_tree_io_tg           | 825 ms                                                 | 873 ms: 1.06x slower                                              |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.06x slower                                             |
| regex_compile              | 131 ms                                                 | 140 ms: 1.07x slower                                              |
| dulwich_log                | 63.0 ms                                                | 67.3 ms: 1.07x slower                                             |
| sqlglot_transpile          | 1.57 ms                                                | 1.68 ms: 1.07x slower                                             |
| sqlglot_optimize           | 53.9 ms                                                | 58.2 ms: 1.08x slower                                             |
| genshi_text                | 22.9 ms                                                | 24.8 ms: 1.08x slower                                             |
| sympy_expand               | 462 ms                                                 | 500 ms: 1.08x slower                                              |
| create_gc_cycles           | 1.61 ms                                                | 1.75 ms: 1.08x slower                                             |
| sympy_str                  | 274 ms                                                 | 298 ms: 1.09x slower                                              |
| genshi_xml                 | 50.3 ms                                                | 56.4 ms: 1.12x slower                                             |
| hexiom                     | 6.13 ms                                                | 6.88 ms: 1.12x slower                                             |
| generators                 | 28.8 ms                                                | 32.9 ms: 1.14x slower                                             |
| sympy_integrate            | 19.9 ms                                                | 22.8 ms: 1.15x slower                                             |
| docutils                   | 2.58 sec                                               | 2.96 sec: 1.15x slower                                            |
| sympy_sum                  | 150 ms                                                 | 172 ms: 1.15x slower                                              |
| pylint                     | 313 ms                                                 | 375 ms: 1.20x slower                                              |
| unpack_sequence            | 42.4 ns                                                | 111 ns: 2.62x slower                                              |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, asyncio_websockets, bench_mp_pool, html5lib, json_loads, coroutines, async_tree_io
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 90.59% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x
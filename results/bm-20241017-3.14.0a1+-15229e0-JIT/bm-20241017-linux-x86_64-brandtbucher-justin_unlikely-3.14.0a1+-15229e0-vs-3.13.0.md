# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_unlikely
- machine: linux-x86_64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.03x slower
- HPT reliability: 55.50%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 278 ms: 1.05x slower                                                    |
| docutils       | 2.58 sec                                               | 2.92 sec: 1.13x slower                                                  |
| html5lib       | 64.5 ms                                                | 63.4 ms: 1.02x faster                                                   |
| tornado_http   | 91.5 ms                                                | 95.4 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 374 ms: 1.24x faster                                                    |
| async_tree_none            | 354 ms                                                 | 328 ms: 1.08x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 414 ms: 1.07x faster                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                  |
| coroutines                 | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                   |
| asyncio_tcp                | 488 ms                                                 | 500 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 559 ms: 1.03x slower                                                    |
| async_generators           | 433 ms                                                 | 461 ms: 1.06x slower                                                    |
| async_tree_io_tg           | 825 ms                                                 | 974 ms: 1.18x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 85.7 ms                                                | 80.9 ms: 1.06x faster                                                   |
| float          | 78.5 ms                                                | 75.3 ms: 1.04x faster                                                   |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 24.5 ms: 1.03x faster                                                   |
| regex_effbot   | 3.88 ms                                                | 3.78 ms: 1.03x faster                                                   |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                    |
| regex_compile  | 131 ms                                                 | 141 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                  | 1.00x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 78.5 ms: 1.11x faster                                                   |
| tomli_loads          | 2.11 sec                                               | 1.91 sec: 1.10x faster                                                  |
| xml_etree_process    | 60.4 ms                                                | 55.0 ms: 1.10x faster                                                   |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                    |
| xml_etree_iterparse  | 102 ms                                                 | 99.1 ms: 1.03x faster                                                   |
| json_loads           | 27.0 us                                                | 26.6 us: 1.01x faster                                                   |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                    |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                                   |
| pickle_pure_python   | 300 us                                                 | 309 us: 1.03x slower                                                    |
| pickle_list          | 5.01 us                                                | 5.16 us: 1.03x slower                                                   |
| json_dumps           | 10.4 ms                                                | 10.9 ms: 1.05x slower                                                   |
| unpickle_list        | 4.96 us                                                | 5.30 us: 1.07x slower                                                   |
| pickle_dict          | 33.2 us                                                | 35.8 us: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 7.09 ms: 1.02x slower                                                   |
| python_startup         | 10.6 ms                                                | 11.9 ms: 1.13x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.93 ms: 1.12x faster                                                   |
| django_template | 34.4 ms                                                | 36.9 ms: 1.07x slower                                                   |
| genshi_text     | 22.9 ms                                                | 25.5 ms: 1.11x slower                                                   |
| genshi_xml      | 50.3 ms                                                | 59.7 ms: 1.19x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 270 us: 1.30x faster                                                    |
| deepcopy_memo              | 38.0 us                                                | 29.3 us: 1.30x faster                                                   |
| async_tree_memoization_tg  | 465 ms                                                 | 374 ms: 1.24x faster                                                    |
| richards                   | 48.1 ms                                                | 41.1 ms: 1.17x faster                                                   |
| deepcopy_reduce            | 3.17 us                                                | 2.71 us: 1.17x faster                                                   |
| scimark_fft                | 369 ms                                                 | 317 ms: 1.16x faster                                                    |
| richards_super             | 54.4 ms                                                | 47.0 ms: 1.16x faster                                                   |
| mako                       | 11.1 ms                                                | 9.93 ms: 1.12x faster                                                   |
| xml_etree_generate         | 87.0 ms                                                | 78.5 ms: 1.11x faster                                                   |
| tomli_loads                | 2.11 sec                                               | 1.91 sec: 1.10x faster                                                  |
| crypto_pyaes               | 73.0 ms                                                | 66.4 ms: 1.10x faster                                                   |
| xml_etree_process          | 60.4 ms                                                | 55.0 ms: 1.10x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.62 ms: 1.09x faster                                                   |
| telco                      | 8.45 ms                                                | 7.79 ms: 1.09x faster                                                   |
| mdp                        | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                  |
| async_tree_none            | 354 ms                                                 | 328 ms: 1.08x faster                                                    |
| go                         | 142 ms                                                 | 132 ms: 1.07x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 414 ms: 1.07x faster                                                    |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                    |
| nbody                      | 85.7 ms                                                | 80.9 ms: 1.06x faster                                                   |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                   |
| json                       | 5.20 ms                                                | 4.92 ms: 1.06x faster                                                   |
| bpe_tokeniser              | 4.69 sec                                               | 4.45 sec: 1.05x faster                                                  |
| float                      | 78.5 ms                                                | 75.3 ms: 1.04x faster                                                   |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                                    |
| pprint_safe_repr           | 744 ms                                                 | 719 ms: 1.03x faster                                                    |
| scimark_monte_carlo        | 66.3 ms                                                | 64.1 ms: 1.03x faster                                                   |
| regex_v8                   | 25.3 ms                                                | 24.5 ms: 1.03x faster                                                   |
| xml_etree_iterparse        | 102 ms                                                 | 99.1 ms: 1.03x faster                                                   |
| regex_effbot               | 3.88 ms                                                | 3.78 ms: 1.03x faster                                                   |
| logging_format             | 6.25 us                                                | 6.12 us: 1.02x faster                                                   |
| logging_silent             | 102 ns                                                 | 100 ns: 1.02x faster                                                    |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                                    |
| html5lib                   | 64.5 ms                                                | 63.4 ms: 1.02x faster                                                   |
| thrift                     | 796 us                                                 | 783 us: 1.02x faster                                                    |
| pyflate                    | 460 ms                                                 | 452 ms: 1.02x faster                                                    |
| pycparser                  | 1.19 sec                                               | 1.18 sec: 1.02x faster                                                  |
| scimark_lu                 | 115 ms                                                 | 113 ms: 1.01x faster                                                    |
| json_loads                 | 27.0 us                                                | 26.6 us: 1.01x faster                                                   |
| logging_simple             | 5.66 us                                                | 5.59 us: 1.01x faster                                                   |
| chaos                      | 58.4 ms                                                | 57.9 ms: 1.01x faster                                                   |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                  |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                    |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                                    |
| coroutines                 | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                   |
| python_startup_no_site     | 6.99 ms                                                | 7.09 ms: 1.02x slower                                                   |
| spectral_norm              | 115 ms                                                 | 117 ms: 1.02x slower                                                    |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                                   |
| asyncio_tcp                | 488 ms                                                 | 500 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 559 ms: 1.03x slower                                                    |
| pickle_pure_python         | 300 us                                                 | 309 us: 1.03x slower                                                    |
| comprehensions             | 16.4 us                                                | 16.9 us: 1.03x slower                                                   |
| pickle_list                | 5.01 us                                                | 5.16 us: 1.03x slower                                                   |
| deltablue                  | 3.15 ms                                                | 3.26 ms: 1.03x slower                                                   |
| fannkuch                   | 381 ms                                                 | 395 ms: 1.04x slower                                                    |
| typing_runtime_protocols   | 159 us                                                 | 166 us: 1.04x slower                                                    |
| tornado_http               | 91.5 ms                                                | 95.4 ms: 1.04x slower                                                   |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.05x slower                                                   |
| 2to3                       | 265 ms                                                 | 278 ms: 1.05x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 10.9 ms: 1.05x slower                                                   |
| raytrace                   | 262 ms                                                 | 276 ms: 1.06x slower                                                    |
| dulwich_log                | 63.0 ms                                                | 67.0 ms: 1.06x slower                                                   |
| async_generators           | 433 ms                                                 | 461 ms: 1.06x slower                                                    |
| sqlglot_transpile          | 1.57 ms                                                | 1.68 ms: 1.07x slower                                                   |
| unpickle_list              | 4.96 us                                                | 5.30 us: 1.07x slower                                                   |
| sqlglot_normalize          | 107 ms                                                 | 115 ms: 1.07x slower                                                    |
| django_template            | 34.4 ms                                                | 36.9 ms: 1.07x slower                                                   |
| bench_thread_pool          | 815 us                                                 | 878 us: 1.08x slower                                                    |
| pickle_dict                | 33.2 us                                                | 35.8 us: 1.08x slower                                                   |
| regex_compile              | 131 ms                                                 | 141 ms: 1.08x slower                                                    |
| sympy_expand               | 462 ms                                                 | 499 ms: 1.08x slower                                                    |
| nqueens                    | 80.6 ms                                                | 88.4 ms: 1.10x slower                                                   |
| sympy_str                  | 274 ms                                                 | 301 ms: 1.10x slower                                                    |
| sqlglot_optimize           | 53.9 ms                                                | 59.9 ms: 1.11x slower                                                   |
| genshi_text                | 22.9 ms                                                | 25.5 ms: 1.11x slower                                                   |
| python_startup             | 10.6 ms                                                | 11.9 ms: 1.13x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.92 sec: 1.13x slower                                                  |
| hexiom                     | 6.13 ms                                                | 6.98 ms: 1.14x slower                                                   |
| gc_traversal               | 3.81 ms                                                | 4.45 ms: 1.17x slower                                                   |
| async_tree_io_tg           | 825 ms                                                 | 974 ms: 1.18x slower                                                    |
| sympy_sum                  | 150 ms                                                 | 177 ms: 1.18x slower                                                    |
| sympy_integrate            | 19.9 ms                                                | 23.5 ms: 1.18x slower                                                   |
| genshi_xml                 | 50.3 ms                                                | 59.7 ms: 1.19x slower                                                   |
| pylint                     | 313 ms                                                 | 376 ms: 1.20x slower                                                    |
| generators                 | 28.8 ms                                                | 35.3 ms: 1.22x slower                                                   |
| create_gc_cycles           | 1.61 ms                                                | 2.67 ms: 1.66x slower                                                   |
| unpack_sequence            | 42.4 ns                                                | 106 ns: 2.50x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 84.2 ms: 3.51x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.03x slower                                                            |

Benchmark hidden because not significant (8): async_tree_none_tg, sqlite_synth, pprint_pformat, async_tree_cpu_io_mixed, asyncio_websockets, coverage, unpickle, async_tree_io
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: sphinx

# HPT report

- Reliability score: 55.50% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.19x
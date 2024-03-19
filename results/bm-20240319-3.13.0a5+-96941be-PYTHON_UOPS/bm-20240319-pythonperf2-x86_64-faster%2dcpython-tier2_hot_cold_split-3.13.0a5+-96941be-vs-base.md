# Results vs. base

- fork: faster-cpython
- ref: tier2_hot_cold_split
- machine: linux-x86_64
- commit hash: 96941be
- commit date: 2024-03-19
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240319-pythonperf2-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 315 ms                                                                       | 333 ms: 1.06x slower                                                                   |
| chameleon      | 7.52 ms                                                                      | 7.56 ms: 1.01x slower                                                                  |
| docutils       | 3.04 sec                                                                     | 3.11 sec: 1.02x slower                                                                 |
| html5lib       | 78.0 ms                                                                      | 79.8 ms: 1.02x slower                                                                  |
| tornado_http   | 128 ms                                                                       | 131 ms: 1.02x slower                                                                   |
| Geometric mean | (ref)                                                                        | 1.03x slower                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240319-pythonperf2-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 711 ms                                                                       | 719 ms: 1.01x slower                                                                   |
| async_tree_cpu_io_mixed    | 710 ms                                                                       | 720 ms: 1.01x slower                                                                   |
| async_tree_none            | 444 ms                                                                       | 452 ms: 1.02x slower                                                                   |
| async_tree_io_tg           | 1.09 sec                                                                     | 1.11 sec: 1.02x slower                                                                 |
| async_tree_io              | 1.09 sec                                                                     | 1.12 sec: 1.02x slower                                                                 |
| async_tree_none_tg         | 440 ms                                                                       | 449 ms: 1.02x slower                                                                   |
| async_tree_memoization     | 556 ms                                                                       | 571 ms: 1.03x slower                                                                   |
| Geometric mean             | (ref)                                                                        | 1.01x slower                                                                           |

Benchmark hidden because not significant (1): async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240319-pythonperf2-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pidigits       | 264 ms                                                                       | 264 ms: 1.00x faster                                                                   |
| float          | 95.8 ms                                                                      | 102 ms: 1.07x slower                                                                   |
| nbody          | 118 ms                                                                       | 143 ms: 1.21x slower                                                                   |
| Geometric mean | (ref)                                                                        | 1.09x slower                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240319-pythonperf2-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_dna      | 250 ms                                                                       | 244 ms: 1.03x faster                                                                   |
| regex_v8       | 25.9 ms                                                                      | 26.2 ms: 1.01x slower                                                                  |
| regex_compile  | 193 ms                                                                       | 215 ms: 1.11x slower                                                                   |
| Geometric mean | (ref)                                                                        | 1.02x slower                                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240319-pythonperf2-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpickle             | 14.9 us                                                                      | 14.8 us: 1.00x faster                                                                  |
| json_loads           | 24.9 us                                                                      | 25.0 us: 1.01x slower                                                                  |
| pickle_dict          | 32.6 us                                                                      | 33.0 us: 1.01x slower                                                                  |
| xml_etree_parse      | 146 ms                                                                       | 148 ms: 1.02x slower                                                                   |
| xml_etree_generate   | 90.0 ms                                                                      | 92.3 ms: 1.03x slower                                                                  |
| xml_etree_process    | 61.9 ms                                                                      | 63.7 ms: 1.03x slower                                                                  |
| pickle_list          | 4.37 us                                                                      | 4.50 us: 1.03x slower                                                                  |
| json_dumps           | 10.6 ms                                                                      | 10.9 ms: 1.03x slower                                                                  |
| pickle_pure_python   | 315 us                                                                       | 326 us: 1.04x slower                                                                   |
| xml_etree_iterparse  | 109 ms                                                                       | 114 ms: 1.04x slower                                                                   |
| unpickle_list        | 4.51 us                                                                      | 4.74 us: 1.05x slower                                                                  |
| pickle               | 10.5 us                                                                      | 11.1 us: 1.06x slower                                                                  |
| unpickle_pure_python | 284 us                                                                       | 305 us: 1.07x slower                                                                   |
| tomli_loads          | 2.71 sec                                                                     | 2.97 sec: 1.10x slower                                                                 |
| Geometric mean       | (ref)                                                                        | 1.04x slower                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240319-pythonperf2-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup | 12.8 ms                                                                      | 12.8 ms: 1.00x faster                                                                  |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240319-pythonperf2-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|-----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_text     | 28.4 ms                                                                      | 28.2 ms: 1.01x faster                                                                  |
| django_template | 39.2 ms                                                                      | 40.3 ms: 1.03x slower                                                                  |
| genshi_xml      | 61.4 ms                                                                      | 64.3 ms: 1.05x slower                                                                  |
| mako            | 12.7 ms                                                                      | 13.9 ms: 1.09x slower                                                                  |
| Geometric mean  | (ref)                                                                        | 1.04x slower                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20240319-pythonperf2-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| gc_traversal               | 4.02 ms                                                                      | 3.54 ms: 1.14x faster                                                                  |
| regex_dna                  | 250 ms                                                                       | 244 ms: 1.03x faster                                                                   |
| scimark_sparse_mat_mult    | 6.11 ms                                                                      | 5.98 ms: 1.02x faster                                                                  |
| logging_silent             | 102 ns                                                                       | 100 ns: 1.02x faster                                                                   |
| gunicorn                   | 1.10 ms                                                                      | 1.09 ms: 1.01x faster                                                                  |
| scimark_lu                 | 134 ms                                                                       | 132 ms: 1.01x faster                                                                   |
| genshi_text                | 28.4 ms                                                                      | 28.2 ms: 1.01x faster                                                                  |
| unpickle                   | 14.9 us                                                                      | 14.8 us: 1.00x faster                                                                  |
| pidigits                   | 264 ms                                                                       | 264 ms: 1.00x faster                                                                   |
| python_startup             | 12.8 ms                                                                      | 12.8 ms: 1.00x faster                                                                  |
| asyncio_tcp_ssl            | 1.59 sec                                                                     | 1.60 sec: 1.00x slower                                                                 |
| sqlite_synth               | 2.79 us                                                                      | 2.81 us: 1.00x slower                                                                  |
| json_loads                 | 24.9 us                                                                      | 25.0 us: 1.01x slower                                                                  |
| chameleon                  | 7.52 ms                                                                      | 7.56 ms: 1.01x slower                                                                  |
| meteor_contest             | 139 ms                                                                       | 139 ms: 1.01x slower                                                                   |
| asyncio_websockets         | 386 ms                                                                       | 389 ms: 1.01x slower                                                                   |
| asyncio_tcp                | 377 ms                                                                       | 380 ms: 1.01x slower                                                                   |
| pathlib                    | 20.0 ms                                                                      | 20.2 ms: 1.01x slower                                                                  |
| scimark_sor                | 157 ms                                                                       | 159 ms: 1.01x slower                                                                   |
| async_tree_cpu_io_mixed_tg | 711 ms                                                                       | 719 ms: 1.01x slower                                                                   |
| thrift                     | 871 us                                                                       | 880 us: 1.01x slower                                                                   |
| logging_format             | 7.40 us                                                                      | 7.48 us: 1.01x slower                                                                  |
| generators                 | 33.5 ms                                                                      | 33.9 ms: 1.01x slower                                                                  |
| regex_v8                   | 25.9 ms                                                                      | 26.2 ms: 1.01x slower                                                                  |
| crypto_pyaes               | 84.2 ms                                                                      | 85.4 ms: 1.01x slower                                                                  |
| async_tree_cpu_io_mixed    | 710 ms                                                                       | 720 ms: 1.01x slower                                                                   |
| pickle_dict                | 32.6 us                                                                      | 33.0 us: 1.01x slower                                                                  |
| async_tree_none            | 444 ms                                                                       | 452 ms: 1.02x slower                                                                   |
| xml_etree_parse            | 146 ms                                                                       | 148 ms: 1.02x slower                                                                   |
| async_tree_io_tg           | 1.09 sec                                                                     | 1.11 sec: 1.02x slower                                                                 |
| sqlglot_normalize          | 122 ms                                                                       | 125 ms: 1.02x slower                                                                   |
| async_tree_io              | 1.09 sec                                                                     | 1.12 sec: 1.02x slower                                                                 |
| tornado_http               | 128 ms                                                                       | 131 ms: 1.02x slower                                                                   |
| docutils                   | 3.04 sec                                                                     | 3.11 sec: 1.02x slower                                                                 |
| coroutines                 | 22.2 ms                                                                      | 22.6 ms: 1.02x slower                                                                  |
| async_tree_none_tg         | 440 ms                                                                       | 449 ms: 1.02x slower                                                                   |
| async_generators           | 388 ms                                                                       | 398 ms: 1.02x slower                                                                   |
| html5lib                   | 78.0 ms                                                                      | 79.8 ms: 1.02x slower                                                                  |
| sympy_integrate            | 25.0 ms                                                                      | 25.6 ms: 1.02x slower                                                                  |
| dask                       | 406 ms                                                                       | 416 ms: 1.03x slower                                                                   |
| sympy_sum                  | 171 ms                                                                       | 176 ms: 1.03x slower                                                                   |
| xml_etree_generate         | 90.0 ms                                                                      | 92.3 ms: 1.03x slower                                                                  |
| async_tree_memoization     | 556 ms                                                                       | 571 ms: 1.03x slower                                                                   |
| mdp                        | 2.63 sec                                                                     | 2.70 sec: 1.03x slower                                                                 |
| xml_etree_process          | 61.9 ms                                                                      | 63.7 ms: 1.03x slower                                                                  |
| django_template            | 39.2 ms                                                                      | 40.3 ms: 1.03x slower                                                                  |
| pickle_list                | 4.37 us                                                                      | 4.50 us: 1.03x slower                                                                  |
| json_dumps                 | 10.6 ms                                                                      | 10.9 ms: 1.03x slower                                                                  |
| pylint                     | 362 ms                                                                       | 374 ms: 1.03x slower                                                                   |
| dulwich_log                | 75.8 ms                                                                      | 78.4 ms: 1.03x slower                                                                  |
| pickle_pure_python         | 315 us                                                                       | 326 us: 1.04x slower                                                                   |
| sympy_str                  | 329 ms                                                                       | 342 ms: 1.04x slower                                                                   |
| sympy_expand               | 562 ms                                                                       | 585 ms: 1.04x slower                                                                   |
| xml_etree_iterparse        | 109 ms                                                                       | 114 ms: 1.04x slower                                                                   |
| deepcopy_reduce            | 3.40 us                                                                      | 3.54 us: 1.04x slower                                                                  |
| sqlglot_transpile          | 1.97 ms                                                                      | 2.06 ms: 1.04x slower                                                                  |
| telco                      | 8.29 ms                                                                      | 8.67 ms: 1.05x slower                                                                  |
| genshi_xml                 | 61.4 ms                                                                      | 64.3 ms: 1.05x slower                                                                  |
| spectral_norm              | 140 ms                                                                       | 147 ms: 1.05x slower                                                                   |
| unpickle_list              | 4.51 us                                                                      | 4.74 us: 1.05x slower                                                                  |
| pprint_safe_repr           | 932 ms                                                                       | 981 ms: 1.05x slower                                                                   |
| scimark_monte_carlo        | 91.0 ms                                                                      | 95.8 ms: 1.05x slower                                                                  |
| sqlglot_optimize           | 66.0 ms                                                                      | 69.5 ms: 1.05x slower                                                                  |
| sqlglot_parse              | 1.54 ms                                                                      | 1.62 ms: 1.05x slower                                                                  |
| nqueens                    | 109 ms                                                                       | 115 ms: 1.05x slower                                                                   |
| raytrace                   | 331 ms                                                                       | 349 ms: 1.06x slower                                                                   |
| 2to3                       | 315 ms                                                                       | 333 ms: 1.06x slower                                                                   |
| pickle                     | 10.5 us                                                                      | 11.1 us: 1.06x slower                                                                  |
| pprint_pformat             | 1.91 sec                                                                     | 2.02 sec: 1.06x slower                                                                 |
| go                         | 195 ms                                                                       | 208 ms: 1.07x slower                                                                   |
| deltablue                  | 3.88 ms                                                                      | 4.14 ms: 1.07x slower                                                                  |
| float                      | 95.8 ms                                                                      | 102 ms: 1.07x slower                                                                   |
| deepcopy                   | 377 us                                                                       | 404 us: 1.07x slower                                                                   |
| pyflate                    | 616 ms                                                                       | 660 ms: 1.07x slower                                                                   |
| comprehensions             | 22.8 us                                                                      | 24.5 us: 1.07x slower                                                                  |
| pycparser                  | 1.41 sec                                                                     | 1.51 sec: 1.07x slower                                                                 |
| unpickle_pure_python       | 284 us                                                                       | 305 us: 1.07x slower                                                                   |
| scimark_fft                | 402 ms                                                                       | 432 ms: 1.07x slower                                                                   |
| chaos                      | 71.9 ms                                                                      | 77.5 ms: 1.08x slower                                                                  |
| typing_runtime_protocols   | 121 us                                                                       | 131 us: 1.08x slower                                                                   |
| mako                       | 12.7 ms                                                                      | 13.9 ms: 1.09x slower                                                                  |
| fannkuch                   | 474 ms                                                                       | 519 ms: 1.10x slower                                                                   |
| deepcopy_memo              | 40.9 us                                                                      | 44.9 us: 1.10x slower                                                                  |
| tomli_loads                | 2.71 sec                                                                     | 2.97 sec: 1.10x slower                                                                 |
| richards_super             | 60.9 ms                                                                      | 67.5 ms: 1.11x slower                                                                  |
| regex_compile              | 193 ms                                                                       | 215 ms: 1.11x slower                                                                   |
| bench_mp_pool              | 4.59 ms                                                                      | 5.12 ms: 1.12x slower                                                                  |
| richards                   | 54.6 ms                                                                      | 61.2 ms: 1.12x slower                                                                  |
| unpack_sequence            | 60.1 ns                                                                      | 68.0 ns: 1.13x slower                                                                  |
| hexiom                     | 9.34 ms                                                                      | 10.7 ms: 1.14x slower                                                                  |
| coverage                   | 77.4 ms                                                                      | 89.3 ms: 1.15x slower                                                                  |
| nbody                      | 118 ms                                                                       | 143 ms: 1.21x slower                                                                   |
| bench_thread_pool          | 941 us                                                                       | 1.15 ms: 1.22x slower                                                                  |
| Geometric mean             | (ref)                                                                        | 1.04x slower                                                                           |

Benchmark hidden because not significant (8): async_tree_memoization_tg, regex_effbot, create_gc_cycles, python_startup_no_site, json, logging_simple, aiohttp, mypy2


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x


# Memory

- memory change: 1.00x
# Results vs. base

- fork: python
- ref: v3.13.0a5
- machine: linux-x86_64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.43x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240312-3.13.0a5-076d169/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json | results/bm-20240312-3.13.0a5-076d169-NOGIL/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| 2to3           | 270 ms                                                                                               | 377 ms: 1.40x slower                                                                                       |
| chameleon      | 6.83 ms                                                                                              | 12.3 ms: 1.80x slower                                                                                      |
| docutils       | 2.66 sec                                                                                             | 3.28 sec: 1.23x slower                                                                                     |
| html5lib       | 67.4 ms                                                                                              | 91.5 ms: 1.36x slower                                                                                      |
| tornado_http   | 98.6 ms                                                                                              | 137 ms: 1.39x slower                                                                                       |
| Geometric mean | (ref)                                                                                                | 1.42x slower                                                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240312-3.13.0a5-076d169/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json | results/bm-20240312-3.13.0a5-076d169-NOGIL/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json |
|----------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.24 sec                                                                                             | 839 ms: 1.47x faster                                                                                       |
| async_tree_io              | 1.22 sec                                                                                             | 877 ms: 1.39x faster                                                                                       |
| async_tree_memoization_tg  | 595 ms                                                                                               | 472 ms: 1.26x faster                                                                                       |
| async_tree_none_tg         | 463 ms                                                                                               | 369 ms: 1.25x faster                                                                                       |
| async_tree_cpu_io_mixed_tg | 745 ms                                                                                               | 623 ms: 1.20x faster                                                                                       |
| async_tree_memoization     | 581 ms                                                                                               | 518 ms: 1.12x faster                                                                                       |
| async_tree_none            | 449 ms                                                                                               | 412 ms: 1.09x faster                                                                                       |
| async_tree_cpu_io_mixed    | 729 ms                                                                                               | 668 ms: 1.09x faster                                                                                       |
| Geometric mean             | (ref)                                                                                                | 1.23x faster                                                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240312-3.13.0a5-076d169/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json | results/bm-20240312-3.13.0a5-076d169-NOGIL/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                                               | 192 ms: 1.01x slower                                                                                       |
| float          | 82.6 ms                                                                                              | 127 ms: 1.53x slower                                                                                       |
| nbody          | 93.6 ms                                                                                              | 215 ms: 2.30x slower                                                                                       |
| Geometric mean | (ref)                                                                                                | 1.53x slower                                                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240312-3.13.0a5-076d169/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json | results/bm-20240312-3.13.0a5-076d169-NOGIL/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.54 ms                                                                                              | 3.56 ms: 1.01x slower                                                                                      |
| regex_dna      | 216 ms                                                                                               | 230 ms: 1.06x slower                                                                                       |
| regex_v8       | 24.7 ms                                                                                              | 26.9 ms: 1.09x slower                                                                                      |
| regex_compile  | 133 ms                                                                                               | 204 ms: 1.54x slower                                                                                       |
| Geometric mean | (ref)                                                                                                | 1.16x slower                                                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240312-3.13.0a5-076d169/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json | results/bm-20240312-3.13.0a5-076d169-NOGIL/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json |
|----------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                                                               | 156 ms: 1.02x faster                                                                                       |
| pickle_list          | 5.01 us                                                                                              | 4.97 us: 1.01x faster                                                                                      |
| pickle               | 11.7 us                                                                                              | 12.1 us: 1.04x slower                                                                                      |
| xml_etree_iterparse  | 106 ms                                                                                               | 117 ms: 1.10x slower                                                                                       |
| unpickle_list        | 5.05 us                                                                                              | 5.75 us: 1.14x slower                                                                                      |
| pickle_dict          | 35.7 us                                                                                              | 41.4 us: 1.16x slower                                                                                      |
| unpickle             | 15.1 us                                                                                              | 18.1 us: 1.20x slower                                                                                      |
| xml_etree_generate   | 87.3 ms                                                                                              | 108 ms: 1.23x slower                                                                                       |
| json_loads           | 27.7 us                                                                                              | 34.8 us: 1.25x slower                                                                                      |
| json_dumps           | 10.8 ms                                                                                              | 13.7 ms: 1.27x slower                                                                                      |
| tomli_loads          | 2.16 sec                                                                                             | 3.11 sec: 1.44x slower                                                                                     |
| xml_etree_process    | 59.8 ms                                                                                              | 86.4 ms: 1.45x slower                                                                                      |
| unpickle_pure_python | 217 us                                                                                               | 367 us: 1.69x slower                                                                                       |
| pickle_pure_python   | 302 us                                                                                               | 528 us: 1.75x slower                                                                                       |
| Geometric mean       | (ref)                                                                                                | 1.24x slower                                                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240312-3.13.0a5-076d169/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json | results/bm-20240312-3.13.0a5-076d169-NOGIL/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json |
|------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.99 ms                                                                                              | 11.6 ms: 1.29x slower                                                                                      |
| python_startup         | 10.4 ms                                                                                              | 13.6 ms: 1.31x slower                                                                                      |
| Geometric mean         | (ref)                                                                                                | 1.30x slower                                                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240312-3.13.0a5-076d169/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json | results/bm-20240312-3.13.0a5-076d169-NOGIL/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json |
|-----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 52.0 ms                                                                                              | 78.4 ms: 1.51x slower                                                                                      |
| genshi_text     | 23.0 ms                                                                                              | 38.9 ms: 1.69x slower                                                                                      |
| django_template | 33.8 ms                                                                                              | 57.7 ms: 1.71x slower                                                                                      |
| mako            | 11.3 ms                                                                                              | 21.0 ms: 1.86x slower                                                                                      |
| Geometric mean  | (ref)                                                                                                | 1.69x slower                                                                                               |

All benchmarks:
===============

| Benchmark                  | results/bm-20240312-3.13.0a5-076d169/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json | results/bm-20240312-3.13.0a5-076d169-NOGIL/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json |
|----------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.24 sec                                                                                             | 839 ms: 1.47x faster                                                                                       |
| gc_traversal               | 3.78 ms                                                                                              | 2.57 ms: 1.47x faster                                                                                      |
| create_gc_cycles           | 1.52 ms                                                                                              | 1.08 ms: 1.40x faster                                                                                      |
| async_tree_io              | 1.22 sec                                                                                             | 877 ms: 1.39x faster                                                                                       |
| async_tree_memoization_tg  | 595 ms                                                                                               | 472 ms: 1.26x faster                                                                                       |
| async_tree_none_tg         | 463 ms                                                                                               | 369 ms: 1.25x faster                                                                                       |
| async_tree_cpu_io_mixed_tg | 745 ms                                                                                               | 623 ms: 1.20x faster                                                                                       |
| async_tree_memoization     | 581 ms                                                                                               | 518 ms: 1.12x faster                                                                                       |
| async_tree_none            | 449 ms                                                                                               | 412 ms: 1.09x faster                                                                                       |
| async_tree_cpu_io_mixed    | 729 ms                                                                                               | 668 ms: 1.09x faster                                                                                       |
| xml_etree_parse            | 159 ms                                                                                               | 156 ms: 1.02x faster                                                                                       |
| pickle_list                | 5.01 us                                                                                              | 4.97 us: 1.01x faster                                                                                      |
| asyncio_websockets         | 563 ms                                                                                               | 567 ms: 1.01x slower                                                                                       |
| regex_effbot               | 3.54 ms                                                                                              | 3.56 ms: 1.01x slower                                                                                      |
| pidigits                   | 189 ms                                                                                               | 192 ms: 1.01x slower                                                                                       |
| pickle                     | 11.7 us                                                                                              | 12.1 us: 1.04x slower                                                                                      |
| regex_dna                  | 216 ms                                                                                               | 230 ms: 1.06x slower                                                                                       |
| asyncio_tcp_ssl            | 1.85 sec                                                                                             | 1.99 sec: 1.08x slower                                                                                     |
| regex_v8                   | 24.7 ms                                                                                              | 26.9 ms: 1.09x slower                                                                                      |
| xml_etree_iterparse        | 106 ms                                                                                               | 117 ms: 1.10x slower                                                                                       |
| async_generators           | 449 ms                                                                                               | 511 ms: 1.14x slower                                                                                       |
| unpickle_list              | 5.05 us                                                                                              | 5.75 us: 1.14x slower                                                                                      |
| asyncio_tcp                | 504 ms                                                                                               | 584 ms: 1.16x slower                                                                                       |
| pickle_dict                | 35.7 us                                                                                              | 41.4 us: 1.16x slower                                                                                      |
| unpickle                   | 15.1 us                                                                                              | 18.1 us: 1.20x slower                                                                                      |
| json                       | 5.15 ms                                                                                              | 6.24 ms: 1.21x slower                                                                                      |
| generators                 | 29.5 ms                                                                                              | 36.2 ms: 1.23x slower                                                                                      |
| docutils                   | 2.66 sec                                                                                             | 3.28 sec: 1.23x slower                                                                                     |
| mypy2                      | 871 ms                                                                                               | 1.07 sec: 1.23x slower                                                                                     |
| xml_etree_generate         | 87.3 ms                                                                                              | 108 ms: 1.23x slower                                                                                       |
| meteor_contest             | 109 ms                                                                                               | 136 ms: 1.24x slower                                                                                       |
| pylint                     | 312 ms                                                                                               | 390 ms: 1.25x slower                                                                                       |
| json_loads                 | 27.7 us                                                                                              | 34.8 us: 1.25x slower                                                                                      |
| json_dumps                 | 10.8 ms                                                                                              | 13.7 ms: 1.27x slower                                                                                      |
| python_startup_no_site     | 8.99 ms                                                                                              | 11.6 ms: 1.29x slower                                                                                      |
| mdp                        | 2.53 sec                                                                                             | 3.30 sec: 1.30x slower                                                                                     |
| python_startup             | 10.4 ms                                                                                              | 13.6 ms: 1.31x slower                                                                                      |
| dulwich_log                | 67.3 ms                                                                                              | 89.2 ms: 1.32x slower                                                                                      |
| gunicorn                   | 1.29 ms                                                                                              | 1.71 ms: 1.33x slower                                                                                      |
| scimark_fft                | 362 ms                                                                                               | 481 ms: 1.33x slower                                                                                       |
| coroutines                 | 22.0 ms                                                                                              | 29.3 ms: 1.33x slower                                                                                      |
| pycparser                  | 1.18 sec                                                                                             | 1.57 sec: 1.33x slower                                                                                     |
| sqlite_synth               | 2.89 us                                                                                              | 3.84 us: 1.33x slower                                                                                      |
| aiohttp                    | 1.19 ms                                                                                              | 1.59 ms: 1.34x slower                                                                                      |
| html5lib                   | 67.4 ms                                                                                              | 91.5 ms: 1.36x slower                                                                                      |
| telco                      | 8.60 ms                                                                                              | 11.7 ms: 1.36x slower                                                                                      |
| nqueens                    | 80.7 ms                                                                                              | 111 ms: 1.38x slower                                                                                       |
| tornado_http               | 98.6 ms                                                                                              | 137 ms: 1.39x slower                                                                                       |
| fannkuch                   | 400 ms                                                                                               | 559 ms: 1.40x slower                                                                                       |
| pathlib                    | 18.5 ms                                                                                              | 25.9 ms: 1.40x slower                                                                                      |
| 2to3                       | 270 ms                                                                                               | 377 ms: 1.40x slower                                                                                       |
| sympy_integrate            | 20.0 ms                                                                                              | 28.4 ms: 1.42x slower                                                                                      |
| tomli_loads                | 2.16 sec                                                                                             | 3.11 sec: 1.44x slower                                                                                     |
| xml_etree_process          | 59.8 ms                                                                                              | 86.4 ms: 1.45x slower                                                                                      |
| crypto_pyaes               | 73.0 ms                                                                                              | 108 ms: 1.48x slower                                                                                       |
| richards                   | 45.9 ms                                                                                              | 68.0 ms: 1.48x slower                                                                                      |
| typing_runtime_protocols   | 112 us                                                                                               | 167 us: 1.49x slower                                                                                       |
| genshi_xml                 | 52.0 ms                                                                                              | 78.4 ms: 1.51x slower                                                                                      |
| deepcopy                   | 346 us                                                                                               | 527 us: 1.52x slower                                                                                       |
| sympy_str                  | 275 ms                                                                                               | 421 ms: 1.53x slower                                                                                       |
| float                      | 82.6 ms                                                                                              | 127 ms: 1.53x slower                                                                                       |
| regex_compile              | 133 ms                                                                                               | 204 ms: 1.54x slower                                                                                       |
| pyflate                    | 469 ms                                                                                               | 728 ms: 1.55x slower                                                                                       |
| scimark_sparse_mat_mult    | 4.68 ms                                                                                              | 7.26 ms: 1.55x slower                                                                                      |
| deepcopy_reduce            | 3.04 us                                                                                              | 4.74 us: 1.56x slower                                                                                      |
| comprehensions             | 16.4 us                                                                                              | 25.7 us: 1.56x slower                                                                                      |
| richards_super             | 51.9 ms                                                                                              | 82.3 ms: 1.58x slower                                                                                      |
| pprint_safe_repr           | 757 ms                                                                                               | 1.20 sec: 1.59x slower                                                                                     |
| sympy_expand               | 466 ms                                                                                               | 740 ms: 1.59x slower                                                                                       |
| deepcopy_memo              | 38.1 us                                                                                              | 60.8 us: 1.59x slower                                                                                      |
| pprint_pformat             | 1.55 sec                                                                                             | 2.49 sec: 1.60x slower                                                                                     |
| flaskblogging              | 8.82 ms                                                                                              | 14.3 ms: 1.62x slower                                                                                      |
| sqlglot_optimize           | 53.9 ms                                                                                              | 88.8 ms: 1.65x slower                                                                                      |
| sympy_sum                  | 153 ms                                                                                               | 254 ms: 1.66x slower                                                                                       |
| sqlglot_normalize          | 107 ms                                                                                               | 177 ms: 1.66x slower                                                                                       |
| spectral_norm              | 108 ms                                                                                               | 181 ms: 1.67x slower                                                                                       |
| unpickle_pure_python       | 217 us                                                                                               | 367 us: 1.69x slower                                                                                       |
| genshi_text                | 23.0 ms                                                                                              | 38.9 ms: 1.69x slower                                                                                      |
| django_template            | 33.8 ms                                                                                              | 57.7 ms: 1.71x slower                                                                                      |
| logging_format             | 6.53 us                                                                                              | 11.2 us: 1.72x slower                                                                                      |
| logging_simple             | 5.85 us                                                                                              | 10.2 us: 1.73x slower                                                                                      |
| pickle_pure_python         | 302 us                                                                                               | 528 us: 1.75x slower                                                                                       |
| scimark_monte_carlo        | 67.9 ms                                                                                              | 119 ms: 1.76x slower                                                                                       |
| logging_silent             | 99.5 ns                                                                                              | 176 ns: 1.77x slower                                                                                       |
| sqlglot_transpile          | 1.59 ms                                                                                              | 2.84 ms: 1.78x slower                                                                                      |
| chameleon                  | 6.83 ms                                                                                              | 12.3 ms: 1.80x slower                                                                                      |
| hexiom                     | 6.13 ms                                                                                              | 11.0 ms: 1.80x slower                                                                                      |
| mako                       | 11.3 ms                                                                                              | 21.0 ms: 1.86x slower                                                                                      |
| sqlglot_parse              | 1.27 ms                                                                                              | 2.37 ms: 1.87x slower                                                                                      |
| chaos                      | 60.9 ms                                                                                              | 115 ms: 1.89x slower                                                                                       |
| scimark_sor                | 123 ms                                                                                               | 241 ms: 1.96x slower                                                                                       |
| raytrace                   | 263 ms                                                                                               | 518 ms: 1.97x slower                                                                                       |
| go                         | 139 ms                                                                                               | 273 ms: 1.97x slower                                                                                       |
| scimark_lu                 | 113 ms                                                                                               | 250 ms: 2.21x slower                                                                                       |
| nbody                      | 93.6 ms                                                                                              | 215 ms: 2.30x slower                                                                                       |
| deltablue                  | 3.23 ms                                                                                              | 7.43 ms: 2.30x slower                                                                                      |
| bench_thread_pool          | 842 us                                                                                               | 3.01 ms: 3.58x slower                                                                                      |
| coverage                   | 95.6 ms                                                                                              | 891 ms: 9.32x slower                                                                                       |
| thrift                     | 790 us                                                                                               | 12.4 ms: 15.68x slower                                                                                     |
| Geometric mean             | (ref)                                                                                                | 1.43x slower                                                                                               |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of results/bm-20240312-3.13.0a5-076d169/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json: dask, djangocms

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.33x
- 95% likely to have a slowdown of 1.32x
- 99% likely to have a slowdown of 1.29x

# Memory
- memory change: 1.13x
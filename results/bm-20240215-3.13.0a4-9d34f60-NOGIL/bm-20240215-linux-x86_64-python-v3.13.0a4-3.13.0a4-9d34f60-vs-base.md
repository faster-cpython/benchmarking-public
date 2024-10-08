# Results vs. base

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.12x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-NOGIL/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| 2to3           | 269 ms                                                                                               | 296 ms: 1.10x slower                                                                                       |
| chameleon      | 6.85 ms                                                                                              | 8.24 ms: 1.20x slower                                                                                      |
| docutils       | 2.65 sec                                                                                             | 3.07 sec: 1.16x slower                                                                                     |
| tornado_http   | 97.1 ms                                                                                              | 98.6 ms: 1.02x slower                                                                                      |
| Geometric mean | (ref)                                                                                                | 1.09x slower                                                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-NOGIL/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| async_tree_io              | 1.20 sec                                                                                             | 796 ms: 1.51x faster                                                                                       |
| async_tree_io_tg           | 1.22 sec                                                                                             | 828 ms: 1.48x faster                                                                                       |
| async_tree_memoization_tg  | 585 ms                                                                                               | 458 ms: 1.28x faster                                                                                       |
| async_tree_none_tg         | 455 ms                                                                                               | 377 ms: 1.21x faster                                                                                       |
| async_tree_memoization     | 571 ms                                                                                               | 476 ms: 1.20x faster                                                                                       |
| async_tree_cpu_io_mixed_tg | 733 ms                                                                                               | 612 ms: 1.20x faster                                                                                       |
| async_tree_none            | 444 ms                                                                                               | 377 ms: 1.18x faster                                                                                       |
| async_tree_cpu_io_mixed    | 718 ms                                                                                               | 646 ms: 1.11x faster                                                                                       |
| Geometric mean             | (ref)                                                                                                | 1.26x faster                                                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-NOGIL/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| float          | 83.1 ms                                                                                              | 74.2 ms: 1.12x faster                                                                                      |
| pidigits       | 189 ms                                                                                               | 194 ms: 1.03x slower                                                                                       |
| nbody          | 92.1 ms                                                                                              | 104 ms: 1.13x slower                                                                                       |
| Geometric mean | (ref)                                                                                                | 1.01x slower                                                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-NOGIL/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.66 ms                                                                                              | 3.60 ms: 1.02x faster                                                                                      |
| regex_v8       | 24.4 ms                                                                                              | 25.1 ms: 1.03x slower                                                                                      |
| regex_dna      | 224 ms                                                                                               | 232 ms: 1.04x slower                                                                                       |
| regex_compile  | 132 ms                                                                                               | 141 ms: 1.07x slower                                                                                       |
| Geometric mean | (ref)                                                                                                | 1.03x slower                                                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-NOGIL/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| pickle_list          | 5.28 us                                                                                              | 4.88 us: 1.08x faster                                                                                      |
| xml_etree_parse      | 160 ms                                                                                               | 151 ms: 1.06x faster                                                                                       |
| tomli_loads          | 2.20 sec                                                                                             | 2.23 sec: 1.02x slower                                                                                     |
| unpickle_list        | 5.09 us                                                                                              | 5.21 us: 1.02x slower                                                                                      |
| xml_etree_generate   | 86.9 ms                                                                                              | 90.5 ms: 1.04x slower                                                                                      |
| unpickle_pure_python | 217 us                                                                                               | 237 us: 1.09x slower                                                                                       |
| pickle_pure_python   | 302 us                                                                                               | 333 us: 1.10x slower                                                                                       |
| json_dumps           | 10.5 ms                                                                                              | 11.6 ms: 1.11x slower                                                                                      |
| json_loads           | 27.9 us                                                                                              | 32.2 us: 1.15x slower                                                                                      |
| unpickle             | 15.4 us                                                                                              | 18.0 us: 1.17x slower                                                                                      |
| pickle_dict          | 34.7 us                                                                                              | 41.2 us: 1.19x slower                                                                                      |
| xml_etree_process    | 59.3 ms                                                                                              | 71.1 ms: 1.20x slower                                                                                      |
| xml_etree_iterparse  | 107 ms                                                                                               | 166 ms: 1.55x slower                                                                                       |
| Geometric mean       | (ref)                                                                                                | 1.10x slower                                                                                               |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-NOGIL/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.87 ms                                                                                              | 10.0 ms: 1.13x slower                                                                                      |
| python_startup         | 10.3 ms                                                                                              | 12.0 ms: 1.16x slower                                                                                      |
| Geometric mean         | (ref)                                                                                                | 1.15x slower                                                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-NOGIL/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|-----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 52.8 ms                                                                                              | 54.7 ms: 1.04x slower                                                                                      |
| django_template | 34.7 ms                                                                                              | 39.1 ms: 1.13x slower                                                                                      |
| genshi_text     | 23.0 ms                                                                                              | 26.1 ms: 1.14x slower                                                                                      |
| mako            | 11.2 ms                                                                                              | 16.3 ms: 1.45x slower                                                                                      |
| Geometric mean  | (ref)                                                                                                | 1.18x slower                                                                                               |

All benchmarks:
===============

| Benchmark                  | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-NOGIL/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| async_tree_io              | 1.20 sec                                                                                             | 796 ms: 1.51x faster                                                                                       |
| async_tree_io_tg           | 1.22 sec                                                                                             | 828 ms: 1.48x faster                                                                                       |
| create_gc_cycles           | 1.51 ms                                                                                              | 1.03 ms: 1.47x faster                                                                                      |
| gc_traversal               | 3.55 ms                                                                                              | 2.57 ms: 1.38x faster                                                                                      |
| async_tree_memoization_tg  | 585 ms                                                                                               | 458 ms: 1.28x faster                                                                                       |
| mypy2                      | 865 ms                                                                                               | 696 ms: 1.24x faster                                                                                       |
| async_tree_none_tg         | 455 ms                                                                                               | 377 ms: 1.21x faster                                                                                       |
| async_tree_memoization     | 571 ms                                                                                               | 476 ms: 1.20x faster                                                                                       |
| async_tree_cpu_io_mixed_tg | 733 ms                                                                                               | 612 ms: 1.20x faster                                                                                       |
| async_tree_none            | 444 ms                                                                                               | 377 ms: 1.18x faster                                                                                       |
| float                      | 83.1 ms                                                                                              | 74.2 ms: 1.12x faster                                                                                      |
| async_tree_cpu_io_mixed    | 718 ms                                                                                               | 646 ms: 1.11x faster                                                                                       |
| pickle_list                | 5.28 us                                                                                              | 4.88 us: 1.08x faster                                                                                      |
| xml_etree_parse            | 160 ms                                                                                               | 151 ms: 1.06x faster                                                                                       |
| pylint                     | 310 ms                                                                                               | 296 ms: 1.05x faster                                                                                       |
| pycparser                  | 1.23 sec                                                                                             | 1.19 sec: 1.03x faster                                                                                     |
| bench_mp_pool              | 23.8 ms                                                                                              | 23.4 ms: 1.02x faster                                                                                      |
| regex_effbot               | 3.66 ms                                                                                              | 3.60 ms: 1.02x faster                                                                                      |
| asyncio_websockets         | 563 ms                                                                                               | 557 ms: 1.01x faster                                                                                       |
| scimark_sor                | 129 ms                                                                                               | 129 ms: 1.01x slower                                                                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                                                             | 1.85 sec: 1.01x slower                                                                                     |
| async_generators           | 459 ms                                                                                               | 463 ms: 1.01x slower                                                                                       |
| asyncio_tcp                | 501 ms                                                                                               | 508 ms: 1.01x slower                                                                                       |
| pathlib                    | 18.7 ms                                                                                              | 19.0 ms: 1.01x slower                                                                                      |
| tornado_http               | 97.1 ms                                                                                              | 98.6 ms: 1.02x slower                                                                                      |
| tomli_loads                | 2.20 sec                                                                                             | 2.23 sec: 1.02x slower                                                                                     |
| unpickle_list              | 5.09 us                                                                                              | 5.21 us: 1.02x slower                                                                                      |
| richards                   | 48.1 ms                                                                                              | 49.2 ms: 1.02x slower                                                                                      |
| pidigits                   | 189 ms                                                                                               | 194 ms: 1.03x slower                                                                                       |
| regex_v8                   | 24.4 ms                                                                                              | 25.1 ms: 1.03x slower                                                                                      |
| dulwich_log                | 67.0 ms                                                                                              | 69.0 ms: 1.03x slower                                                                                      |
| generators                 | 30.3 ms                                                                                              | 31.2 ms: 1.03x slower                                                                                      |
| regex_dna                  | 224 ms                                                                                               | 232 ms: 1.04x slower                                                                                       |
| genshi_xml                 | 52.8 ms                                                                                              | 54.7 ms: 1.04x slower                                                                                      |
| richards_super             | 54.1 ms                                                                                              | 56.3 ms: 1.04x slower                                                                                      |
| xml_etree_generate         | 86.9 ms                                                                                              | 90.5 ms: 1.04x slower                                                                                      |
| nqueens                    | 81.0 ms                                                                                              | 84.7 ms: 1.05x slower                                                                                      |
| crypto_pyaes               | 72.0 ms                                                                                              | 75.5 ms: 1.05x slower                                                                                      |
| scimark_fft                | 359 ms                                                                                               | 380 ms: 1.06x slower                                                                                       |
| spectral_norm              | 111 ms                                                                                               | 118 ms: 1.06x slower                                                                                       |
| meteor_contest             | 108 ms                                                                                               | 115 ms: 1.07x slower                                                                                       |
| hexiom                     | 6.20 ms                                                                                              | 6.62 ms: 1.07x slower                                                                                      |
| fannkuch                   | 401 ms                                                                                               | 428 ms: 1.07x slower                                                                                       |
| regex_compile              | 132 ms                                                                                               | 141 ms: 1.07x slower                                                                                       |
| scimark_lu                 | 113 ms                                                                                               | 121 ms: 1.07x slower                                                                                       |
| sqlglot_normalize          | 108 ms                                                                                               | 116 ms: 1.07x slower                                                                                       |
| gunicorn                   | 1.27 ms                                                                                              | 1.37 ms: 1.08x slower                                                                                      |
| aiohttp                    | 1.17 ms                                                                                              | 1.27 ms: 1.08x slower                                                                                      |
| telco                      | 8.41 ms                                                                                              | 9.09 ms: 1.08x slower                                                                                      |
| chaos                      | 61.2 ms                                                                                              | 66.2 ms: 1.08x slower                                                                                      |
| pprint_safe_repr           | 734 ms                                                                                               | 797 ms: 1.09x slower                                                                                       |
| pprint_pformat             | 1.51 sec                                                                                             | 1.64 sec: 1.09x slower                                                                                     |
| typing_runtime_protocols   | 112 us                                                                                               | 122 us: 1.09x slower                                                                                       |
| sqlglot_optimize           | 54.2 ms                                                                                              | 59.3 ms: 1.09x slower                                                                                      |
| unpickle_pure_python       | 217 us                                                                                               | 237 us: 1.09x slower                                                                                       |
| logging_format             | 6.53 us                                                                                              | 7.18 us: 1.10x slower                                                                                      |
| 2to3                       | 269 ms                                                                                               | 296 ms: 1.10x slower                                                                                       |
| scimark_monte_carlo        | 67.2 ms                                                                                              | 74.0 ms: 1.10x slower                                                                                      |
| logging_simple             | 5.83 us                                                                                              | 6.43 us: 1.10x slower                                                                                      |
| pickle_pure_python         | 302 us                                                                                               | 333 us: 1.10x slower                                                                                       |
| sqlite_synth               | 2.87 us                                                                                              | 3.17 us: 1.10x slower                                                                                      |
| go                         | 139 ms                                                                                               | 154 ms: 1.11x slower                                                                                       |
| json_dumps                 | 10.5 ms                                                                                              | 11.6 ms: 1.11x slower                                                                                      |
| json                       | 5.19 ms                                                                                              | 5.81 ms: 1.12x slower                                                                                      |
| deepcopy                   | 347 us                                                                                               | 390 us: 1.12x slower                                                                                       |
| raytrace                   | 265 ms                                                                                               | 298 ms: 1.12x slower                                                                                       |
| django_template            | 34.7 ms                                                                                              | 39.1 ms: 1.13x slower                                                                                      |
| sqlglot_transpile          | 1.58 ms                                                                                              | 1.78 ms: 1.13x slower                                                                                      |
| scimark_sparse_mat_mult    | 4.64 ms                                                                                              | 5.25 ms: 1.13x slower                                                                                      |
| nbody                      | 92.1 ms                                                                                              | 104 ms: 1.13x slower                                                                                       |
| deepcopy_reduce            | 3.06 us                                                                                              | 3.46 us: 1.13x slower                                                                                      |
| python_startup_no_site     | 8.87 ms                                                                                              | 10.0 ms: 1.13x slower                                                                                      |
| genshi_text                | 23.0 ms                                                                                              | 26.1 ms: 1.14x slower                                                                                      |
| comprehensions             | 16.2 us                                                                                              | 18.5 us: 1.14x slower                                                                                      |
| sqlglot_parse              | 1.26 ms                                                                                              | 1.44 ms: 1.14x slower                                                                                      |
| json_loads                 | 27.9 us                                                                                              | 32.2 us: 1.15x slower                                                                                      |
| docutils                   | 2.65 sec                                                                                             | 3.07 sec: 1.16x slower                                                                                     |
| python_startup             | 10.3 ms                                                                                              | 12.0 ms: 1.16x slower                                                                                      |
| logging_silent             | 97.7 ns                                                                                              | 114 ns: 1.17x slower                                                                                       |
| unpickle                   | 15.4 us                                                                                              | 18.0 us: 1.17x slower                                                                                      |
| pickle_dict                | 34.7 us                                                                                              | 41.2 us: 1.19x slower                                                                                      |
| sympy_integrate            | 19.9 ms                                                                                              | 23.8 ms: 1.20x slower                                                                                      |
| xml_etree_process          | 59.3 ms                                                                                              | 71.1 ms: 1.20x slower                                                                                      |
| deepcopy_memo              | 37.9 us                                                                                              | 45.6 us: 1.20x slower                                                                                      |
| chameleon                  | 6.85 ms                                                                                              | 8.24 ms: 1.20x slower                                                                                      |
| deltablue                  | 3.24 ms                                                                                              | 4.16 ms: 1.29x slower                                                                                      |
| sympy_str                  | 274 ms                                                                                               | 354 ms: 1.29x slower                                                                                       |
| sympy_expand               | 462 ms                                                                                               | 623 ms: 1.35x slower                                                                                       |
| mdp                        | 2.61 sec                                                                                             | 3.64 sec: 1.39x slower                                                                                     |
| sympy_sum                  | 150 ms                                                                                               | 211 ms: 1.40x slower                                                                                       |
| mako                       | 11.2 ms                                                                                              | 16.3 ms: 1.45x slower                                                                                      |
| xml_etree_iterparse        | 107 ms                                                                                               | 166 ms: 1.55x slower                                                                                       |
| flaskblogging              | 8.75 ms                                                                                              | 18.7 ms: 2.14x slower                                                                                      |
| bench_thread_pool          | 838 us                                                                                               | 2.42 ms: 2.89x slower                                                                                      |
| coverage                   | 96.3 ms                                                                                              | 712 ms: 7.40x slower                                                                                       |
| thrift                     | 807 us                                                                                               | 9.43 ms: 11.68x slower                                                                                     |
| Geometric mean             | (ref)                                                                                                | 1.12x slower                                                                                               |

Benchmark hidden because not significant (4): coroutines, pickle, pyflate, html5lib
Ignored benchmarks (1) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: djangocms

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.11x
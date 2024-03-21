# Results vs. 3.11.0

- fork: faster-cpython
- ref: fix_gc_counting
- machine: linux-x86_64
- commit hash: d0672a4
- commit date: 2024-03-21
- overall geometric mean: 1.07x faster
- HPT reliability: 99.61%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                 | 268 ms: 1.01x slower                                                        |
| chameleon      | 6.70 ms                                                | 6.95 ms: 1.04x slower                                                       |
| docutils       | 2.66 sec                                               | 2.74 sec: 1.03x slower                                                      |
| tornado_http   | 98.1 ms                                                | 94.8 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 626 ms                                                 | 442 ms: 1.42x faster                                                        |
| async_tree_io_tg           | 1.29 sec                                               | 917 ms: 1.41x faster                                                        |
| async_tree_none            | 528 ms                                                 | 374 ms: 1.41x faster                                                        |
| async_tree_none_tg         | 491 ms                                                 | 350 ms: 1.40x faster                                                        |
| async_tree_io              | 1.29 sec                                               | 917 ms: 1.40x faster                                                        |
| async_tree_memoization     | 639 ms                                                 | 461 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 590 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 606 ms: 1.26x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 96.0 ms                                                | 89.9 ms: 1.07x faster                                                       |
| pidigits       | 194 ms                                                 | 190 ms: 1.02x faster                                                        |
| float          | 78.9 ms                                                | 78.5 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 141 ms                                                 | 135 ms: 1.05x faster                                                        |
| regex_effbot   | 3.51 ms                                                | 3.61 ms: 1.03x slower                                                       |
| regex_dna      | 205 ms                                                 | 218 ms: 1.07x slower                                                        |
| regex_v8       | 22.9 ms                                                | 24.8 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                | 10.4 ms: 1.28x faster                                                       |
| unpickle_pure_python | 242 us                                                 | 220 us: 1.10x faster                                                        |
| pickle_pure_python   | 320 us                                                 | 302 us: 1.06x faster                                                        |
| tomli_loads          | 2.30 sec                                               | 2.19 sec: 1.05x faster                                                      |
| json_loads           | 29.2 us                                                | 28.6 us: 1.02x faster                                                       |
| xml_etree_parse      | 164 ms                                                 | 162 ms: 1.01x faster                                                        |
| xml_etree_iterparse  | 108 ms                                                 | 107 ms: 1.01x faster                                                        |
| unpickle_list        | 5.21 us                                                | 5.24 us: 1.01x slower                                                       |
| pickle_dict          | 34.6 us                                                | 35.3 us: 1.02x slower                                                       |
| xml_etree_process    | 56.9 ms                                                | 59.8 ms: 1.05x slower                                                       |
| unpickle             | 13.8 us                                                | 14.6 us: 1.05x slower                                                       |
| xml_etree_generate   | 81.1 ms                                                | 85.5 ms: 1.06x slower                                                       |
| pickle               | 11.0 us                                                | 11.8 us: 1.07x slower                                                       |
| pickle_list          | 4.59 us                                                | 5.36 us: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.56 ms                                                | 10.4 ms: 1.22x slower                                                       |
| python_startup_no_site | 6.01 ms                                                | 8.83 ms: 1.47x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.34x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 53.4 ms                                                | 52.1 ms: 1.03x faster                                                       |
| django_template | 33.5 ms                                                | 34.0 ms: 1.01x slower                                                       |
| genshi_text     | 22.5 ms                                                | 23.1 ms: 1.03x slower                                                       |
| mako            | 10.7 ms                                                | 11.5 ms: 1.08x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols   | 520 us                                                 | 113 us: 4.60x faster                                                        |
| generators                 | 74.9 ms                                                | 30.1 ms: 2.49x faster                                                       |
| asyncio_tcp                | 875 ms                                                 | 503 ms: 1.74x faster                                                        |
| asyncio_tcp_ssl            | 3.11 sec                                               | 1.84 sec: 1.69x faster                                                      |
| pylint                     | 476 ms                                                 | 317 ms: 1.50x faster                                                        |
| comprehensions             | 23.6 us                                                | 16.4 us: 1.44x faster                                                       |
| async_tree_memoization_tg  | 626 ms                                                 | 442 ms: 1.42x faster                                                        |
| async_tree_io_tg           | 1.29 sec                                               | 917 ms: 1.41x faster                                                        |
| async_tree_none            | 528 ms                                                 | 374 ms: 1.41x faster                                                        |
| async_tree_none_tg         | 491 ms                                                 | 350 ms: 1.40x faster                                                        |
| async_tree_io              | 1.29 sec                                               | 917 ms: 1.40x faster                                                        |
| async_tree_memoization     | 639 ms                                                 | 461 ms: 1.39x faster                                                        |
| json_dumps                 | 13.3 ms                                                | 10.4 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 590 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 606 ms: 1.26x faster                                                        |
| deltablue                  | 3.92 ms                                                | 3.28 ms: 1.20x faster                                                       |
| richards_super             | 61.9 ms                                                | 53.1 ms: 1.17x faster                                                       |
| chaos                      | 71.9 ms                                                | 61.7 ms: 1.16x faster                                                       |
| coroutines                 | 27.0 ms                                                | 23.2 ms: 1.16x faster                                                       |
| raytrace                   | 309 ms                                                 | 268 ms: 1.15x faster                                                        |
| sqlglot_parse              | 1.43 ms                                                | 1.28 ms: 1.12x faster                                                       |
| logging_silent             | 111 ns                                                 | 99.8 ns: 1.11x faster                                                       |
| sqlglot_transpile          | 1.75 ms                                                | 1.58 ms: 1.11x faster                                                       |
| unpickle_pure_python       | 242 us                                                 | 220 us: 1.10x faster                                                        |
| gc_traversal               | 4.01 ms                                                | 3.65 ms: 1.10x faster                                                       |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.10x faster                                                        |
| hexiom                     | 6.89 ms                                                | 6.34 ms: 1.09x faster                                                       |
| richards                   | 49.8 ms                                                | 46.1 ms: 1.08x faster                                                       |
| nqueens                    | 87.9 ms                                                | 81.8 ms: 1.07x faster                                                       |
| sympy_str                  | 297 ms                                                 | 277 ms: 1.07x faster                                                        |
| sympy_integrate            | 21.5 ms                                                | 20.0 ms: 1.07x faster                                                       |
| djangocms                  | 33.5 us                                                | 31.3 us: 1.07x faster                                                       |
| nbody                      | 96.0 ms                                                | 89.9 ms: 1.07x faster                                                       |
| logging_simple             | 6.22 us                                                | 5.84 us: 1.06x faster                                                       |
| pickle_pure_python         | 320 us                                                 | 302 us: 1.06x faster                                                        |
| deepcopy_memo              | 40.2 us                                                | 38.1 us: 1.05x faster                                                       |
| crypto_pyaes               | 76.7 ms                                                | 72.9 ms: 1.05x faster                                                       |
| tomli_loads                | 2.30 sec                                               | 2.19 sec: 1.05x faster                                                      |
| logging_format             | 6.81 us                                                | 6.49 us: 1.05x faster                                                       |
| go                         | 149 ms                                                 | 142 ms: 1.05x faster                                                        |
| sympy_expand               | 484 ms                                                 | 463 ms: 1.05x faster                                                        |
| sqlglot_normalize          | 113 ms                                                 | 108 ms: 1.05x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.81 ms: 1.05x faster                                                       |
| regex_compile              | 141 ms                                                 | 135 ms: 1.05x faster                                                        |
| tornado_http               | 98.1 ms                                                | 94.8 ms: 1.03x faster                                                       |
| deepcopy                   | 365 us                                                 | 353 us: 1.03x faster                                                        |
| scimark_lu                 | 116 ms                                                 | 113 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.55 sec                                               | 1.51 sec: 1.03x faster                                                      |
| genshi_xml                 | 53.4 ms                                                | 52.1 ms: 1.03x faster                                                       |
| mdp                        | 2.77 sec                                               | 2.71 sec: 1.02x faster                                                      |
| pidigits                   | 194 ms                                                 | 190 ms: 1.02x faster                                                        |
| json_loads                 | 29.2 us                                                | 28.6 us: 1.02x faster                                                       |
| deepcopy_reduce            | 3.22 us                                                | 3.16 us: 1.02x faster                                                       |
| scimark_monte_carlo        | 70.7 ms                                                | 69.6 ms: 1.02x faster                                                       |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.01x faster                                                      |
| xml_etree_parse            | 164 ms                                                 | 162 ms: 1.01x faster                                                        |
| sqlglot_optimize           | 55.3 ms                                                | 54.8 ms: 1.01x faster                                                       |
| pprint_safe_repr           | 747 ms                                                 | 741 ms: 1.01x faster                                                        |
| pathlib                    | 18.5 ms                                                | 18.4 ms: 1.01x faster                                                       |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.01x faster                                                       |
| xml_etree_iterparse        | 108 ms                                                 | 107 ms: 1.01x faster                                                        |
| float                      | 78.9 ms                                                | 78.5 ms: 1.01x faster                                                       |
| bench_thread_pool          | 834 us                                                 | 831 us: 1.00x faster                                                        |
| unpickle_list              | 5.21 us                                                | 5.24 us: 1.01x slower                                                       |
| create_gc_cycles           | 1.43 ms                                                | 1.44 ms: 1.01x slower                                                       |
| meteor_contest             | 109 ms                                                 | 110 ms: 1.01x slower                                                        |
| json                       | 5.24 ms                                                | 5.31 ms: 1.01x slower                                                       |
| django_template            | 33.5 ms                                                | 34.0 ms: 1.01x slower                                                       |
| 2to3                       | 264 ms                                                 | 268 ms: 1.01x slower                                                        |
| unpack_sequence            | 43.5 ns                                                | 44.2 ns: 1.02x slower                                                       |
| pickle_dict                | 34.6 us                                                | 35.3 us: 1.02x slower                                                       |
| asyncio_websockets         | 550 ms                                                 | 563 ms: 1.02x slower                                                        |
| genshi_text                | 22.5 ms                                                | 23.1 ms: 1.03x slower                                                       |
| thrift                     | 784 us                                                 | 805 us: 1.03x slower                                                        |
| docutils                   | 2.66 sec                                               | 2.74 sec: 1.03x slower                                                      |
| regex_effbot               | 3.51 ms                                                | 3.61 ms: 1.03x slower                                                       |
| chameleon                  | 6.70 ms                                                | 6.95 ms: 1.04x slower                                                       |
| scimark_fft                | 345 ms                                                 | 360 ms: 1.04x slower                                                        |
| xml_etree_process          | 56.9 ms                                                | 59.8 ms: 1.05x slower                                                       |
| dulwich_log                | 64.6 ms                                                | 67.9 ms: 1.05x slower                                                       |
| aiohttp                    | 1.12 ms                                                | 1.17 ms: 1.05x slower                                                       |
| unpickle                   | 13.8 us                                                | 14.6 us: 1.05x slower                                                       |
| xml_etree_generate         | 81.1 ms                                                | 85.5 ms: 1.06x slower                                                       |
| spectral_norm              | 108 ms                                                 | 114 ms: 1.06x slower                                                        |
| gunicorn                   | 1.20 ms                                                | 1.27 ms: 1.06x slower                                                       |
| regex_dna                  | 205 ms                                                 | 218 ms: 1.07x slower                                                        |
| pickle                     | 11.0 us                                                | 11.8 us: 1.07x slower                                                       |
| mypy2                      | 686 ms                                                 | 738 ms: 1.08x slower                                                        |
| scimark_sor                | 121 ms                                                 | 131 ms: 1.08x slower                                                        |
| mako                       | 10.7 ms                                                | 11.5 ms: 1.08x slower                                                       |
| regex_v8                   | 22.9 ms                                                | 24.8 ms: 1.08x slower                                                       |
| pyflate                    | 434 ms                                                 | 483 ms: 1.11x slower                                                        |
| sqlite_synth               | 2.57 us                                                | 2.89 us: 1.12x slower                                                       |
| pickle_list                | 4.59 us                                                | 5.36 us: 1.17x slower                                                       |
| async_generators           | 374 ms                                                 | 440 ms: 1.18x slower                                                        |
| python_startup             | 8.56 ms                                                | 10.4 ms: 1.22x slower                                                       |
| coverage                   | 78.8 ms                                                | 96.1 ms: 1.22x slower                                                       |
| telco                      | 6.86 ms                                                | 8.41 ms: 1.23x slower                                                       |
| python_startup_no_site     | 6.01 ms                                                | 8.83 ms: 1.47x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                                |

Benchmark hidden because not significant (3): fannkuch, html5lib, dask
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 99.61% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.01x
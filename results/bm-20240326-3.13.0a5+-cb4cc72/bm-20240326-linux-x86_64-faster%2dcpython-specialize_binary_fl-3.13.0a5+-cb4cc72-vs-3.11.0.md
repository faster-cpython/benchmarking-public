# Results vs. 3.11.0

- fork: faster-cpython
- ref: specialize_binary_fl
- machine: linux-x86_64
- commit hash: cb4cc72
- commit date: 2024-03-26
- overall geometric mean: 1.07x faster
- HPT reliability: 99.34%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                 | 269 ms: 1.02x slower                                                             |
| chameleon      | 6.70 ms                                                | 6.94 ms: 1.04x slower                                                            |
| docutils       | 2.66 sec                                               | 2.77 sec: 1.04x slower                                                           |
| html5lib       | 64.8 ms                                                | 66.0 ms: 1.02x slower                                                            |
| tornado_http   | 98.1 ms                                                | 95.3 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 626 ms                                                 | 446 ms: 1.41x faster                                                             |
| async_tree_io_tg           | 1.29 sec                                               | 922 ms: 1.40x faster                                                             |
| async_tree_none            | 528 ms                                                 | 376 ms: 1.40x faster                                                             |
| async_tree_io              | 1.29 sec                                               | 920 ms: 1.40x faster                                                             |
| async_tree_none_tg         | 491 ms                                                 | 352 ms: 1.39x faster                                                             |
| async_tree_memoization     | 639 ms                                                 | 464 ms: 1.38x faster                                                             |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 599 ms: 1.25x faster                                                             |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 613 ms: 1.24x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 96.0 ms                                                | 91.2 ms: 1.05x faster                                                            |
| pidigits       | 194 ms                                                 | 189 ms: 1.03x faster                                                             |
| float          | 78.9 ms                                                | 77.2 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 141 ms                                                 | 134 ms: 1.05x faster                                                             |
| regex_effbot   | 3.51 ms                                                | 3.69 ms: 1.05x slower                                                            |
| regex_dna      | 205 ms                                                 | 226 ms: 1.10x slower                                                             |
| regex_v8       | 22.9 ms                                                | 25.6 ms: 1.12x slower                                                            |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                | 10.7 ms: 1.25x faster                                                            |
| unpickle_pure_python | 242 us                                                 | 221 us: 1.09x faster                                                             |
| pickle_pure_python   | 320 us                                                 | 302 us: 1.06x faster                                                             |
| tomli_loads          | 2.30 sec                                               | 2.21 sec: 1.04x faster                                                           |
| xml_etree_parse      | 164 ms                                                 | 160 ms: 1.02x faster                                                             |
| json_loads           | 29.2 us                                                | 28.5 us: 1.02x faster                                                            |
| pickle_dict          | 34.6 us                                                | 35.2 us: 1.02x slower                                                            |
| xml_etree_process    | 56.9 ms                                                | 60.0 ms: 1.05x slower                                                            |
| unpickle_list        | 5.21 us                                                | 5.50 us: 1.06x slower                                                            |
| xml_etree_generate   | 81.1 ms                                                | 85.7 ms: 1.06x slower                                                            |
| pickle               | 11.0 us                                                | 11.7 us: 1.07x slower                                                            |
| pickle_list          | 4.59 us                                                | 5.16 us: 1.13x slower                                                            |
| unpickle             | 13.8 us                                                | 16.0 us: 1.15x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.56 ms                                                | 10.6 ms: 1.24x slower                                                            |
| python_startup_no_site | 6.01 ms                                                | 8.95 ms: 1.49x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.36x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 53.4 ms                                                | 50.8 ms: 1.05x faster                                                            |
| django_template | 33.5 ms                                                | 34.6 ms: 1.03x slower                                                            |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                            |
| genshi_text     | 22.5 ms                                                | 24.2 ms: 1.07x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 520 us                                                 | 109 us: 4.78x faster                                                             |
| generators                 | 74.9 ms                                                | 29.9 ms: 2.50x faster                                                            |
| asyncio_tcp                | 875 ms                                                 | 505 ms: 1.73x faster                                                             |
| asyncio_tcp_ssl            | 3.11 sec                                               | 1.83 sec: 1.70x faster                                                           |
| pylint                     | 476 ms                                                 | 320 ms: 1.49x faster                                                             |
| comprehensions             | 23.6 us                                                | 16.5 us: 1.43x faster                                                            |
| async_tree_memoization_tg  | 626 ms                                                 | 446 ms: 1.41x faster                                                             |
| async_tree_io_tg           | 1.29 sec                                               | 922 ms: 1.40x faster                                                             |
| async_tree_none            | 528 ms                                                 | 376 ms: 1.40x faster                                                             |
| async_tree_io              | 1.29 sec                                               | 920 ms: 1.40x faster                                                             |
| async_tree_none_tg         | 491 ms                                                 | 352 ms: 1.39x faster                                                             |
| async_tree_memoization     | 639 ms                                                 | 464 ms: 1.38x faster                                                             |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 599 ms: 1.25x faster                                                             |
| json_dumps                 | 13.3 ms                                                | 10.7 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 613 ms: 1.24x faster                                                             |
| deltablue                  | 3.92 ms                                                | 3.25 ms: 1.21x faster                                                            |
| richards_super             | 61.9 ms                                                | 51.8 ms: 1.20x faster                                                            |
| chaos                      | 71.9 ms                                                | 60.4 ms: 1.19x faster                                                            |
| coroutines                 | 27.0 ms                                                | 23.0 ms: 1.18x faster                                                            |
| raytrace                   | 309 ms                                                 | 267 ms: 1.16x faster                                                             |
| sqlglot_parse              | 1.43 ms                                                | 1.27 ms: 1.12x faster                                                            |
| gc_traversal               | 4.01 ms                                                | 3.58 ms: 1.12x faster                                                            |
| sqlglot_transpile          | 1.75 ms                                                | 1.58 ms: 1.11x faster                                                            |
| logging_silent             | 111 ns                                                 | 101 ns: 1.10x faster                                                             |
| sympy_sum                  | 169 ms                                                 | 153 ms: 1.10x faster                                                             |
| unpickle_pure_python       | 242 us                                                 | 221 us: 1.09x faster                                                             |
| hexiom                     | 6.89 ms                                                | 6.33 ms: 1.09x faster                                                            |
| nqueens                    | 87.9 ms                                                | 80.7 ms: 1.09x faster                                                            |
| richards                   | 49.8 ms                                                | 46.0 ms: 1.08x faster                                                            |
| sympy_str                  | 297 ms                                                 | 276 ms: 1.08x faster                                                             |
| djangocms                  | 33.5 us                                                | 31.2 us: 1.07x faster                                                            |
| sympy_integrate            | 21.5 ms                                                | 20.1 ms: 1.07x faster                                                            |
| go                         | 149 ms                                                 | 140 ms: 1.06x faster                                                             |
| pickle_pure_python         | 320 us                                                 | 302 us: 1.06x faster                                                             |
| crypto_pyaes               | 76.7 ms                                                | 72.8 ms: 1.05x faster                                                            |
| nbody                      | 96.0 ms                                                | 91.2 ms: 1.05x faster                                                            |
| logging_simple             | 6.22 us                                                | 5.91 us: 1.05x faster                                                            |
| genshi_xml                 | 53.4 ms                                                | 50.8 ms: 1.05x faster                                                            |
| regex_compile              | 141 ms                                                 | 134 ms: 1.05x faster                                                             |
| scimark_monte_carlo        | 70.7 ms                                                | 67.4 ms: 1.05x faster                                                            |
| sympy_expand               | 484 ms                                                 | 463 ms: 1.05x faster                                                             |
| tomli_loads                | 2.30 sec                                               | 2.21 sec: 1.04x faster                                                           |
| logging_format             | 6.81 us                                                | 6.56 us: 1.04x faster                                                            |
| sqlglot_normalize          | 113 ms                                                 | 109 ms: 1.04x faster                                                             |
| scimark_lu                 | 116 ms                                                 | 113 ms: 1.03x faster                                                             |
| pprint_pformat             | 1.55 sec                                               | 1.51 sec: 1.03x faster                                                           |
| tornado_http               | 98.1 ms                                                | 95.3 ms: 1.03x faster                                                            |
| unpack_sequence            | 43.5 ns                                                | 42.3 ns: 1.03x faster                                                            |
| deepcopy                   | 365 us                                                 | 356 us: 1.03x faster                                                             |
| deepcopy_memo              | 40.2 us                                                | 39.2 us: 1.03x faster                                                            |
| pidigits                   | 194 ms                                                 | 189 ms: 1.03x faster                                                             |
| xml_etree_parse            | 164 ms                                                 | 160 ms: 1.02x faster                                                             |
| json_loads                 | 29.2 us                                                | 28.5 us: 1.02x faster                                                            |
| float                      | 78.9 ms                                                | 77.2 ms: 1.02x faster                                                            |
| pprint_safe_repr           | 747 ms                                                 | 731 ms: 1.02x faster                                                             |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.93 ms: 1.02x faster                                                            |
| deepcopy_reduce            | 3.22 us                                                | 3.19 us: 1.01x faster                                                            |
| fannkuch                   | 405 ms                                                 | 403 ms: 1.01x faster                                                             |
| sqlglot_optimize           | 55.3 ms                                                | 55.0 ms: 1.00x faster                                                            |
| bench_thread_pool          | 834 us                                                 | 833 us: 1.00x faster                                                             |
| mdp                        | 2.77 sec                                               | 2.78 sec: 1.00x slower                                                           |
| meteor_contest             | 109 ms                                                 | 109 ms: 1.00x slower                                                             |
| pathlib                    | 18.5 ms                                                | 18.7 ms: 1.01x slower                                                            |
| scimark_sor                | 121 ms                                                 | 123 ms: 1.01x slower                                                             |
| json                       | 5.24 ms                                                | 5.32 ms: 1.02x slower                                                            |
| 2to3                       | 264 ms                                                 | 269 ms: 1.02x slower                                                             |
| html5lib                   | 64.8 ms                                                | 66.0 ms: 1.02x slower                                                            |
| pickle_dict                | 34.6 us                                                | 35.2 us: 1.02x slower                                                            |
| create_gc_cycles           | 1.43 ms                                                | 1.46 ms: 1.02x slower                                                            |
| asyncio_websockets         | 550 ms                                                 | 565 ms: 1.03x slower                                                             |
| thrift                     | 784 us                                                 | 808 us: 1.03x slower                                                             |
| django_template            | 33.5 ms                                                | 34.6 ms: 1.03x slower                                                            |
| chameleon                  | 6.70 ms                                                | 6.94 ms: 1.04x slower                                                            |
| docutils                   | 2.66 sec                                               | 2.77 sec: 1.04x slower                                                           |
| spectral_norm              | 108 ms                                                 | 113 ms: 1.05x slower                                                             |
| dulwich_log                | 64.6 ms                                                | 68.0 ms: 1.05x slower                                                            |
| regex_effbot               | 3.51 ms                                                | 3.69 ms: 1.05x slower                                                            |
| xml_etree_process          | 56.9 ms                                                | 60.0 ms: 1.05x slower                                                            |
| unpickle_list              | 5.21 us                                                | 5.50 us: 1.06x slower                                                            |
| xml_etree_generate         | 81.1 ms                                                | 85.7 ms: 1.06x slower                                                            |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                            |
| aiohttp                    | 1.12 ms                                                | 1.19 ms: 1.06x slower                                                            |
| scimark_fft                | 345 ms                                                 | 367 ms: 1.06x slower                                                             |
| pickle                     | 11.0 us                                                | 11.7 us: 1.07x slower                                                            |
| gunicorn                   | 1.20 ms                                                | 1.28 ms: 1.07x slower                                                            |
| genshi_text                | 22.5 ms                                                | 24.2 ms: 1.07x slower                                                            |
| mypy2                      | 686 ms                                                 | 741 ms: 1.08x slower                                                             |
| pyflate                    | 434 ms                                                 | 478 ms: 1.10x slower                                                             |
| regex_dna                  | 205 ms                                                 | 226 ms: 1.10x slower                                                             |
| regex_v8                   | 22.9 ms                                                | 25.6 ms: 1.12x slower                                                            |
| pickle_list                | 4.59 us                                                | 5.16 us: 1.13x slower                                                            |
| sqlite_synth               | 2.57 us                                                | 2.92 us: 1.14x slower                                                            |
| unpickle                   | 13.8 us                                                | 16.0 us: 1.15x slower                                                            |
| async_generators           | 374 ms                                                 | 443 ms: 1.19x slower                                                             |
| coverage                   | 78.8 ms                                                | 96.4 ms: 1.22x slower                                                            |
| python_startup             | 8.56 ms                                                | 10.6 ms: 1.24x slower                                                            |
| telco                      | 6.86 ms                                                | 8.55 ms: 1.25x slower                                                            |
| python_startup_no_site     | 6.01 ms                                                | 8.95 ms: 1.49x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                                     |

Benchmark hidden because not significant (4): xml_etree_iterparse, bench_mp_pool, pycparser, dask
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 99.34% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.01x
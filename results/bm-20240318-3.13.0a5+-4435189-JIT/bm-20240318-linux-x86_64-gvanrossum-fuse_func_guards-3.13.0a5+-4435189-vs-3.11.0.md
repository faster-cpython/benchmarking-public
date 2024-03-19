# Results vs. 3.11.0

- fork: gvanrossum
- ref: fuse_func_guards
- machine: linux-x86_64
- commit hash: 4435189
- commit date: 2024-03-18
- overall geometric mean: 1.02x faster
- HPT reliability: 52.46%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 264 ms                                                 | 283 ms: 1.07x slower                                                   |
| chameleon      | 6.70 ms                                                | 6.98 ms: 1.04x slower                                                  |
| docutils       | 2.66 sec                                               | 2.77 sec: 1.04x slower                                                 |
| html5lib       | 64.8 ms                                                | 65.9 ms: 1.02x slower                                                  |
| tornado_http   | 98.1 ms                                                | 99.0 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none            | 528 ms                                                 | 445 ms: 1.19x faster                                                   |
| async_tree_memoization     | 639 ms                                                 | 574 ms: 1.11x faster                                                   |
| async_tree_none_tg         | 491 ms                                                 | 457 ms: 1.07x faster                                                   |
| async_tree_memoization_tg  | 626 ms                                                 | 584 ms: 1.07x faster                                                   |
| async_tree_io              | 1.29 sec                                               | 1.21 sec: 1.06x faster                                                 |
| async_tree_io_tg           | 1.29 sec                                               | 1.23 sec: 1.05x faster                                                 |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 727 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 739 ms: 1.03x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 96.0 ms                                                | 93.2 ms: 1.03x faster                                                  |
| pidigits       | 194 ms                                                 | 189 ms: 1.03x faster                                                   |
| float          | 78.9 ms                                                | 80.3 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 141 ms                                                 | 143 ms: 1.01x slower                                                   |
| regex_effbot   | 3.51 ms                                                | 3.78 ms: 1.08x slower                                                  |
| regex_dna      | 205 ms                                                 | 224 ms: 1.09x slower                                                   |
| regex_v8       | 22.9 ms                                                | 25.7 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                | 10.6 ms: 1.26x faster                                                  |
| tomli_loads          | 2.30 sec                                               | 2.09 sec: 1.10x faster                                                 |
| json_loads           | 29.2 us                                                | 27.9 us: 1.04x faster                                                  |
| pickle_pure_python   | 320 us                                                 | 306 us: 1.04x faster                                                   |
| unpickle_list        | 5.21 us                                                | 5.07 us: 1.03x faster                                                  |
| pickle_dict          | 34.6 us                                                | 33.7 us: 1.03x faster                                                  |
| xml_etree_parse      | 164 ms                                                 | 160 ms: 1.02x faster                                                   |
| unpickle_pure_python | 242 us                                                 | 239 us: 1.01x faster                                                   |
| xml_etree_iterparse  | 108 ms                                                 | 109 ms: 1.01x slower                                                   |
| pickle               | 11.0 us                                                | 11.6 us: 1.05x slower                                                  |
| xml_etree_process    | 56.9 ms                                                | 60.4 ms: 1.06x slower                                                  |
| xml_etree_generate   | 81.1 ms                                                | 87.9 ms: 1.08x slower                                                  |
| pickle_list          | 4.59 us                                                | 5.01 us: 1.09x slower                                                  |
| unpickle             | 13.8 us                                                | 15.5 us: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.56 ms                                                | 12.6 ms: 1.47x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 11.2 ms: 1.86x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.66x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 33.5 ms                                                | 34.5 ms: 1.03x slower                                                  |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                  |
| genshi_xml      | 53.4 ms                                                | 56.5 ms: 1.06x slower                                                  |
| genshi_text     | 22.5 ms                                                | 25.0 ms: 1.11x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols   | 520 us                                                 | 112 us: 4.65x faster                                                   |
| generators                 | 74.9 ms                                                | 29.6 ms: 2.53x faster                                                  |
| asyncio_tcp                | 875 ms                                                 | 504 ms: 1.74x faster                                                   |
| asyncio_tcp_ssl            | 3.11 sec                                               | 1.85 sec: 1.68x faster                                                 |
| pylint                     | 476 ms                                                 | 324 ms: 1.47x faster                                                   |
| comprehensions             | 23.6 us                                                | 17.5 us: 1.35x faster                                                  |
| json_dumps                 | 13.3 ms                                                | 10.6 ms: 1.26x faster                                                  |
| async_tree_none            | 528 ms                                                 | 445 ms: 1.19x faster                                                   |
| coroutines                 | 27.0 ms                                                | 22.9 ms: 1.18x faster                                                  |
| richards_super             | 61.9 ms                                                | 52.6 ms: 1.18x faster                                                  |
| deltablue                  | 3.92 ms                                                | 3.45 ms: 1.14x faster                                                  |
| chaos                      | 71.9 ms                                                | 64.2 ms: 1.12x faster                                                  |
| async_tree_memoization     | 639 ms                                                 | 574 ms: 1.11x faster                                                   |
| logging_silent             | 111 ns                                                 | 100 ns: 1.11x faster                                                   |
| tomli_loads                | 2.30 sec                                               | 2.09 sec: 1.10x faster                                                 |
| sqlglot_parse              | 1.43 ms                                                | 1.32 ms: 1.08x faster                                                  |
| async_tree_none_tg         | 491 ms                                                 | 457 ms: 1.07x faster                                                   |
| async_tree_memoization_tg  | 626 ms                                                 | 584 ms: 1.07x faster                                                   |
| richards                   | 49.8 ms                                                | 46.5 ms: 1.07x faster                                                  |
| djangocms                  | 33.5 us                                                | 31.4 us: 1.07x faster                                                  |
| async_tree_io              | 1.29 sec                                               | 1.21 sec: 1.06x faster                                                 |
| logging_simple             | 6.22 us                                                | 5.89 us: 1.06x faster                                                  |
| raytrace                   | 309 ms                                                 | 293 ms: 1.05x faster                                                   |
| sqlglot_transpile          | 1.75 ms                                                | 1.66 ms: 1.05x faster                                                  |
| async_tree_io_tg           | 1.29 sec                                               | 1.23 sec: 1.05x faster                                                 |
| deepcopy                   | 365 us                                                 | 348 us: 1.05x faster                                                   |
| mdp                        | 2.77 sec                                               | 2.65 sec: 1.05x faster                                                 |
| logging_format             | 6.81 us                                                | 6.50 us: 1.05x faster                                                  |
| deepcopy_reduce            | 3.22 us                                                | 3.08 us: 1.05x faster                                                  |
| json_loads                 | 29.2 us                                                | 27.9 us: 1.04x faster                                                  |
| pickle_pure_python         | 320 us                                                 | 306 us: 1.04x faster                                                   |
| sqlglot_normalize          | 113 ms                                                 | 108 ms: 1.04x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 162 ms: 1.04x faster                                                   |
| sympy_str                  | 297 ms                                                 | 287 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 727 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 739 ms: 1.03x faster                                                   |
| nbody                      | 96.0 ms                                                | 93.2 ms: 1.03x faster                                                  |
| deepcopy_memo              | 40.2 us                                                | 39.0 us: 1.03x faster                                                  |
| unpickle_list              | 5.21 us                                                | 5.07 us: 1.03x faster                                                  |
| pickle_dict                | 34.6 us                                                | 33.7 us: 1.03x faster                                                  |
| pidigits                   | 194 ms                                                 | 189 ms: 1.03x faster                                                   |
| json                       | 5.24 ms                                                | 5.12 ms: 1.02x faster                                                  |
| xml_etree_parse            | 164 ms                                                 | 160 ms: 1.02x faster                                                   |
| gc_traversal               | 4.01 ms                                                | 3.92 ms: 1.02x faster                                                  |
| fannkuch                   | 405 ms                                                 | 397 ms: 1.02x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.96 ms: 1.01x faster                                                  |
| unpickle_pure_python       | 242 us                                                 | 239 us: 1.01x faster                                                   |
| crypto_pyaes               | 76.7 ms                                                | 75.9 ms: 1.01x faster                                                  |
| sympy_integrate            | 21.5 ms                                                | 21.2 ms: 1.01x faster                                                  |
| sympy_expand               | 484 ms                                                 | 487 ms: 1.01x slower                                                   |
| tornado_http               | 98.1 ms                                                | 99.0 ms: 1.01x slower                                                  |
| xml_etree_iterparse        | 108 ms                                                 | 109 ms: 1.01x slower                                                   |
| regex_compile              | 141 ms                                                 | 143 ms: 1.01x slower                                                   |
| pprint_safe_repr           | 747 ms                                                 | 758 ms: 1.01x slower                                                   |
| meteor_contest             | 109 ms                                                 | 111 ms: 1.02x slower                                                   |
| pycparser                  | 1.19 sec                                               | 1.20 sec: 1.02x slower                                                 |
| html5lib                   | 64.8 ms                                                | 65.9 ms: 1.02x slower                                                  |
| float                      | 78.9 ms                                                | 80.3 ms: 1.02x slower                                                  |
| dask                       | 365 ms                                                 | 373 ms: 1.02x slower                                                   |
| hexiom                     | 6.89 ms                                                | 7.04 ms: 1.02x slower                                                  |
| thrift                     | 784 us                                                 | 802 us: 1.02x slower                                                   |
| asyncio_websockets         | 550 ms                                                 | 564 ms: 1.02x slower                                                   |
| bench_thread_pool          | 834 us                                                 | 855 us: 1.02x slower                                                   |
| nqueens                    | 87.9 ms                                                | 90.2 ms: 1.03x slower                                                  |
| django_template            | 33.5 ms                                                | 34.5 ms: 1.03x slower                                                  |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                  |
| pathlib                    | 18.5 ms                                                | 19.1 ms: 1.03x slower                                                  |
| sqlglot_optimize           | 55.3 ms                                                | 57.1 ms: 1.03x slower                                                  |
| docutils                   | 2.66 sec                                               | 2.77 sec: 1.04x slower                                                 |
| chameleon                  | 6.70 ms                                                | 6.98 ms: 1.04x slower                                                  |
| pickle                     | 11.0 us                                                | 11.6 us: 1.05x slower                                                  |
| spectral_norm              | 108 ms                                                 | 114 ms: 1.05x slower                                                   |
| create_gc_cycles           | 1.43 ms                                                | 1.51 ms: 1.05x slower                                                  |
| genshi_xml                 | 53.4 ms                                                | 56.5 ms: 1.06x slower                                                  |
| go                         | 149 ms                                                 | 158 ms: 1.06x slower                                                   |
| xml_etree_process          | 56.9 ms                                                | 60.4 ms: 1.06x slower                                                  |
| 2to3                       | 264 ms                                                 | 283 ms: 1.07x slower                                                   |
| aiohttp                    | 1.12 ms                                                | 1.20 ms: 1.07x slower                                                  |
| scimark_sor                | 121 ms                                                 | 131 ms: 1.08x slower                                                   |
| dulwich_log                | 64.6 ms                                                | 69.7 ms: 1.08x slower                                                  |
| regex_effbot               | 3.51 ms                                                | 3.78 ms: 1.08x slower                                                  |
| gunicorn                   | 1.20 ms                                                | 1.30 ms: 1.08x slower                                                  |
| xml_etree_generate         | 81.1 ms                                                | 87.9 ms: 1.08x slower                                                  |
| pickle_list                | 4.59 us                                                | 5.01 us: 1.09x slower                                                  |
| regex_dna                  | 205 ms                                                 | 224 ms: 1.09x slower                                                   |
| sqlite_synth               | 2.57 us                                                | 2.83 us: 1.10x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 26.4 ms: 1.10x slower                                                  |
| genshi_text                | 22.5 ms                                                | 25.0 ms: 1.11x slower                                                  |
| pyflate                    | 434 ms                                                 | 481 ms: 1.11x slower                                                   |
| unpickle                   | 13.8 us                                                | 15.5 us: 1.12x slower                                                  |
| regex_v8                   | 22.9 ms                                                | 25.7 ms: 1.12x slower                                                  |
| scimark_lu                 | 116 ms                                                 | 132 ms: 1.14x slower                                                   |
| telco                      | 6.86 ms                                                | 8.44 ms: 1.23x slower                                                  |
| async_generators           | 374 ms                                                 | 468 ms: 1.25x slower                                                   |
| coverage                   | 78.8 ms                                                | 98.6 ms: 1.25x slower                                                  |
| mypy2                      | 686 ms                                                 | 905 ms: 1.32x slower                                                   |
| python_startup             | 8.56 ms                                                | 12.6 ms: 1.47x slower                                                  |
| python_startup_no_site     | 6.01 ms                                                | 11.2 ms: 1.86x slower                                                  |
| unpack_sequence            | 43.5 ns                                                | 86.8 ns: 2.00x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (3): scimark_monte_carlo, pprint_pformat, scimark_fft
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 52.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.24x
# Results vs. 3.11.0

- fork: python
- ref: 48c0b05cf0dd2db275bd
- machine: linux-x86_64
- commit hash: 48c0b05
- commit date: 2024-03-26
- overall geometric mean: 1.04x faster
- HPT reliability: 60.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 264 ms                                                 | 276 ms: 1.05x slower                                                   |
| chameleon      | 6.70 ms                                                | 6.88 ms: 1.03x slower                                                  |
| docutils       | 2.66 sec                                               | 2.90 sec: 1.09x slower                                                 |
| html5lib       | 64.8 ms                                                | 67.8 ms: 1.05x slower                                                  |
| tornado_http   | 98.1 ms                                                | 96.8 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none            | 528 ms                                                 | 354 ms: 1.49x faster                                                   |
| async_tree_io_tg           | 1.29 sec                                               | 914 ms: 1.42x faster                                                   |
| async_tree_memoization     | 639 ms                                                 | 452 ms: 1.41x faster                                                   |
| async_tree_none_tg         | 491 ms                                                 | 350 ms: 1.40x faster                                                   |
| async_tree_memoization_tg  | 626 ms                                                 | 450 ms: 1.39x faster                                                   |
| async_tree_io              | 1.29 sec                                               | 927 ms: 1.39x faster                                                   |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 602 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 615 ms: 1.22x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 96.0 ms                                                | 92.7 ms: 1.04x faster                                                  |
| float          | 78.9 ms                                                | 76.7 ms: 1.03x faster                                                  |
| pidigits       | 194 ms                                                 | 189 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 141 ms                                                 | 147 ms: 1.04x slower                                                   |
| regex_dna      | 205 ms                                                 | 217 ms: 1.06x slower                                                   |
| regex_effbot   | 3.51 ms                                                | 3.75 ms: 1.07x slower                                                  |
| regex_v8       | 22.9 ms                                                | 25.3 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                | 10.5 ms: 1.28x faster                                                  |
| tomli_loads          | 2.30 sec                                               | 2.09 sec: 1.10x faster                                                 |
| pickle_pure_python   | 320 us                                                 | 306 us: 1.05x faster                                                   |
| json_loads           | 29.2 us                                                | 28.6 us: 1.02x faster                                                  |
| xml_etree_parse      | 164 ms                                                 | 161 ms: 1.02x faster                                                   |
| pickle_dict          | 34.6 us                                                | 34.3 us: 1.01x faster                                                  |
| xml_etree_iterparse  | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| unpickle_pure_python | 242 us                                                 | 241 us: 1.00x faster                                                   |
| unpickle_list        | 5.21 us                                                | 5.29 us: 1.01x slower                                                  |
| xml_etree_process    | 56.9 ms                                                | 60.0 ms: 1.05x slower                                                  |
| pickle               | 11.0 us                                                | 11.6 us: 1.06x slower                                                  |
| xml_etree_generate   | 81.1 ms                                                | 87.0 ms: 1.07x slower                                                  |
| pickle_list          | 4.59 us                                                | 4.94 us: 1.08x slower                                                  |
| unpickle             | 13.8 us                                                | 15.2 us: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.56 ms                                                | 11.0 ms: 1.29x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 9.48 ms: 1.58x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.43x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 53.4 ms                                                | 54.3 ms: 1.02x slower                                                  |
| mako            | 10.7 ms                                                | 10.8 ms: 1.02x slower                                                  |
| django_template | 33.5 ms                                                | 36.1 ms: 1.07x slower                                                  |
| genshi_text     | 22.5 ms                                                | 24.3 ms: 1.08x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols   | 520 us                                                 | 111 us: 4.67x faster                                                   |
| generators                 | 74.9 ms                                                | 29.5 ms: 2.54x faster                                                  |
| asyncio_tcp                | 875 ms                                                 | 510 ms: 1.72x faster                                                   |
| asyncio_tcp_ssl            | 3.11 sec                                               | 1.86 sec: 1.67x faster                                                 |
| async_tree_none            | 528 ms                                                 | 354 ms: 1.49x faster                                                   |
| pylint                     | 476 ms                                                 | 335 ms: 1.42x faster                                                   |
| async_tree_io_tg           | 1.29 sec                                               | 914 ms: 1.42x faster                                                   |
| async_tree_memoization     | 639 ms                                                 | 452 ms: 1.41x faster                                                   |
| async_tree_none_tg         | 491 ms                                                 | 350 ms: 1.40x faster                                                   |
| async_tree_memoization_tg  | 626 ms                                                 | 450 ms: 1.39x faster                                                   |
| async_tree_io              | 1.29 sec                                               | 927 ms: 1.39x faster                                                   |
| comprehensions             | 23.6 us                                                | 18.4 us: 1.28x faster                                                  |
| json_dumps                 | 13.3 ms                                                | 10.5 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 602 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 615 ms: 1.22x faster                                                   |
| richards_super             | 61.9 ms                                                | 52.6 ms: 1.18x faster                                                  |
| coroutines                 | 27.0 ms                                                | 23.0 ms: 1.18x faster                                                  |
| deltablue                  | 3.92 ms                                                | 3.44 ms: 1.14x faster                                                  |
| chaos                      | 71.9 ms                                                | 63.1 ms: 1.14x faster                                                  |
| tomli_loads                | 2.30 sec                                               | 2.09 sec: 1.10x faster                                                 |
| gc_traversal               | 4.01 ms                                                | 3.69 ms: 1.09x faster                                                  |
| sqlglot_parse              | 1.43 ms                                                | 1.32 ms: 1.08x faster                                                  |
| logging_silent             | 111 ns                                                 | 104 ns: 1.07x faster                                                   |
| raytrace                   | 309 ms                                                 | 289 ms: 1.07x faster                                                   |
| richards                   | 49.8 ms                                                | 46.7 ms: 1.07x faster                                                  |
| sqlglot_transpile          | 1.75 ms                                                | 1.64 ms: 1.06x faster                                                  |
| pickle_pure_python         | 320 us                                                 | 306 us: 1.05x faster                                                   |
| mdp                        | 2.77 sec                                               | 2.65 sec: 1.05x faster                                                 |
| logging_simple             | 6.22 us                                                | 5.96 us: 1.04x faster                                                  |
| logging_format             | 6.81 us                                                | 6.57 us: 1.04x faster                                                  |
| nbody                      | 96.0 ms                                                | 92.7 ms: 1.04x faster                                                  |
| djangocms                  | 33.5 us                                                | 32.4 us: 1.03x faster                                                  |
| float                      | 78.9 ms                                                | 76.7 ms: 1.03x faster                                                  |
| pprint_pformat             | 1.55 sec                                               | 1.51 sec: 1.03x faster                                                 |
| pidigits                   | 194 ms                                                 | 189 ms: 1.03x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 165 ms: 1.03x faster                                                   |
| crypto_pyaes               | 76.7 ms                                                | 75.0 ms: 1.02x faster                                                  |
| sympy_str                  | 297 ms                                                 | 291 ms: 1.02x faster                                                   |
| fannkuch                   | 405 ms                                                 | 396 ms: 1.02x faster                                                   |
| json_loads                 | 29.2 us                                                | 28.6 us: 1.02x faster                                                  |
| xml_etree_parse            | 164 ms                                                 | 161 ms: 1.02x faster                                                   |
| deepcopy_memo              | 40.2 us                                                | 39.5 us: 1.02x faster                                                  |
| deepcopy_reduce            | 3.22 us                                                | 3.17 us: 1.02x faster                                                  |
| deepcopy                   | 365 us                                                 | 360 us: 1.02x faster                                                   |
| tornado_http               | 98.1 ms                                                | 96.8 ms: 1.01x faster                                                  |
| pickle_dict                | 34.6 us                                                | 34.3 us: 1.01x faster                                                  |
| xml_etree_iterparse        | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| unpickle_pure_python       | 242 us                                                 | 241 us: 1.00x faster                                                   |
| sympy_expand               | 484 ms                                                 | 491 ms: 1.01x slower                                                   |
| unpickle_list              | 5.21 us                                                | 5.29 us: 1.01x slower                                                  |
| sympy_integrate            | 21.5 ms                                                | 21.8 ms: 1.01x slower                                                  |
| scimark_fft                | 345 ms                                                 | 351 ms: 1.02x slower                                                   |
| genshi_xml                 | 53.4 ms                                                | 54.3 ms: 1.02x slower                                                  |
| mako                       | 10.7 ms                                                | 10.8 ms: 1.02x slower                                                  |
| bench_thread_pool          | 834 us                                                 | 852 us: 1.02x slower                                                   |
| meteor_contest             | 109 ms                                                 | 111 ms: 1.02x slower                                                   |
| pathlib                    | 18.5 ms                                                | 19.0 ms: 1.02x slower                                                  |
| json                       | 5.24 ms                                                | 5.37 ms: 1.03x slower                                                  |
| nqueens                    | 87.9 ms                                                | 90.1 ms: 1.03x slower                                                  |
| chameleon                  | 6.70 ms                                                | 6.88 ms: 1.03x slower                                                  |
| dask                       | 365 ms                                                 | 377 ms: 1.03x slower                                                   |
| thrift                     | 784 us                                                 | 810 us: 1.03x slower                                                   |
| asyncio_websockets         | 550 ms                                                 | 569 ms: 1.03x slower                                                   |
| regex_compile              | 141 ms                                                 | 147 ms: 1.04x slower                                                   |
| 2to3                       | 264 ms                                                 | 276 ms: 1.05x slower                                                   |
| go                         | 149 ms                                                 | 155 ms: 1.05x slower                                                   |
| html5lib                   | 64.8 ms                                                | 67.8 ms: 1.05x slower                                                  |
| hexiom                     | 6.89 ms                                                | 7.23 ms: 1.05x slower                                                  |
| spectral_norm              | 108 ms                                                 | 114 ms: 1.05x slower                                                   |
| sqlglot_optimize           | 55.3 ms                                                | 58.1 ms: 1.05x slower                                                  |
| xml_etree_process          | 56.9 ms                                                | 60.0 ms: 1.05x slower                                                  |
| pickle                     | 11.0 us                                                | 11.6 us: 1.06x slower                                                  |
| regex_dna                  | 205 ms                                                 | 217 ms: 1.06x slower                                                   |
| regex_effbot               | 3.51 ms                                                | 3.75 ms: 1.07x slower                                                  |
| xml_etree_generate         | 81.1 ms                                                | 87.0 ms: 1.07x slower                                                  |
| django_template            | 33.5 ms                                                | 36.1 ms: 1.07x slower                                                  |
| pickle_list                | 4.59 us                                                | 4.94 us: 1.08x slower                                                  |
| scimark_sor                | 121 ms                                                 | 131 ms: 1.08x slower                                                   |
| genshi_text                | 22.5 ms                                                | 24.3 ms: 1.08x slower                                                  |
| aiohttp                    | 1.12 ms                                                | 1.21 ms: 1.08x slower                                                  |
| docutils                   | 2.66 sec                                               | 2.90 sec: 1.09x slower                                                 |
| gunicorn                   | 1.20 ms                                                | 1.31 ms: 1.09x slower                                                  |
| unpickle                   | 13.8 us                                                | 15.2 us: 1.09x slower                                                  |
| dulwich_log                | 64.6 ms                                                | 70.9 ms: 1.10x slower                                                  |
| regex_v8                   | 22.9 ms                                                | 25.3 ms: 1.11x slower                                                  |
| sqlite_synth               | 2.57 us                                                | 2.88 us: 1.12x slower                                                  |
| pyflate                    | 434 ms                                                 | 493 ms: 1.14x slower                                                   |
| scimark_lu                 | 116 ms                                                 | 134 ms: 1.15x slower                                                   |
| mypy2                      | 686 ms                                                 | 789 ms: 1.15x slower                                                   |
| create_gc_cycles           | 1.43 ms                                                | 1.67 ms: 1.16x slower                                                  |
| coverage                   | 78.8 ms                                                | 96.4 ms: 1.22x slower                                                  |
| async_generators           | 374 ms                                                 | 463 ms: 1.24x slower                                                   |
| telco                      | 6.86 ms                                                | 8.69 ms: 1.27x slower                                                  |
| python_startup             | 8.56 ms                                                | 11.0 ms: 1.29x slower                                                  |
| python_startup_no_site     | 6.01 ms                                                | 9.48 ms: 1.58x slower                                                  |
| unpack_sequence            | 43.5 ns                                                | 86.5 ns: 1.99x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (6): pycparser, scimark_sparse_mat_mult, bench_mp_pool, sqlglot_normalize, scimark_monte_carlo, pprint_safe_repr
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 60.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.10x
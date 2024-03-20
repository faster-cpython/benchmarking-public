# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin_plt
- machine: linux-x86_64
- commit hash: 9242976
- commit date: 2024-03-15
- overall geometric mean: 1.00x faster
- HPT reliability: 93.33%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 264 ms                                                 | 285 ms: 1.08x slower                                               |
| chameleon      | 6.70 ms                                                | 6.86 ms: 1.02x slower                                              |
| docutils       | 2.66 sec                                               | 2.79 sec: 1.05x slower                                             |
| html5lib       | 64.8 ms                                                | 66.0 ms: 1.02x slower                                              |
| tornado_http   | 98.1 ms                                                | 99.3 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                  | 1.04x slower                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none            | 528 ms                                                 | 450 ms: 1.17x faster                                               |
| async_tree_memoization     | 639 ms                                                 | 580 ms: 1.10x faster                                               |
| async_tree_none_tg         | 491 ms                                                 | 456 ms: 1.08x faster                                               |
| async_tree_io              | 1.29 sec                                               | 1.22 sec: 1.06x faster                                             |
| async_tree_memoization_tg  | 626 ms                                                 | 599 ms: 1.05x faster                                               |
| async_tree_io_tg           | 1.29 sec                                               | 1.24 sec: 1.05x faster                                             |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 724 ms: 1.04x faster                                               |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 737 ms: 1.03x faster                                               |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 194 ms                                                 | 190 ms: 1.02x faster                                               |
| nbody          | 96.0 ms                                                | 97.9 ms: 1.02x slower                                              |
| float          | 78.9 ms                                                | 81.5 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 141 ms                                                 | 155 ms: 1.09x slower                                               |
| regex_dna      | 205 ms                                                 | 224 ms: 1.09x slower                                               |
| regex_effbot   | 3.51 ms                                                | 3.92 ms: 1.12x slower                                              |
| regex_v8       | 22.9 ms                                                | 25.7 ms: 1.12x slower                                              |
| Geometric mean | (ref)                                                  | 1.11x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                | 10.5 ms: 1.27x faster                                              |
| pickle_pure_python   | 320 us                                                 | 300 us: 1.07x faster                                               |
| tomli_loads          | 2.30 sec                                               | 2.17 sec: 1.06x faster                                             |
| json_loads           | 29.2 us                                                | 28.1 us: 1.04x faster                                              |
| xml_etree_parse      | 164 ms                                                 | 160 ms: 1.03x faster                                               |
| unpickle_list        | 5.21 us                                                | 5.09 us: 1.02x faster                                              |
| pickle_dict          | 34.6 us                                                | 34.5 us: 1.00x faster                                              |
| xml_etree_iterparse  | 108 ms                                                 | 109 ms: 1.01x slower                                               |
| unpickle_pure_python | 242 us                                                 | 246 us: 1.02x slower                                               |
| xml_etree_process    | 56.9 ms                                                | 60.1 ms: 1.06x slower                                              |
| unpickle             | 13.8 us                                                | 14.8 us: 1.07x slower                                              |
| pickle               | 11.0 us                                                | 11.8 us: 1.07x slower                                              |
| xml_etree_generate   | 81.1 ms                                                | 88.4 ms: 1.09x slower                                              |
| pickle_list          | 4.59 us                                                | 5.19 us: 1.13x slower                                              |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 8.56 ms                                                | 11.5 ms: 1.34x slower                                              |
| python_startup_no_site | 6.01 ms                                                | 10.1 ms: 1.68x slower                                              |
| Geometric mean         | (ref)                                                  | 1.50x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 33.5 ms                                                | 34.6 ms: 1.03x slower                                              |
| genshi_xml      | 53.4 ms                                                | 55.9 ms: 1.05x slower                                              |
| mako            | 10.7 ms                                                | 11.4 ms: 1.07x slower                                              |
| genshi_text     | 22.5 ms                                                | 24.6 ms: 1.09x slower                                              |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols   | 520 us                                                 | 109 us: 4.75x faster                                               |
| generators                 | 74.9 ms                                                | 29.8 ms: 2.51x faster                                              |
| asyncio_tcp                | 875 ms                                                 | 501 ms: 1.75x faster                                               |
| asyncio_tcp_ssl            | 3.11 sec                                               | 1.85 sec: 1.68x faster                                             |
| pylint                     | 476 ms                                                 | 325 ms: 1.46x faster                                               |
| comprehensions             | 23.6 us                                                | 18.3 us: 1.29x faster                                              |
| json_dumps                 | 13.3 ms                                                | 10.5 ms: 1.27x faster                                              |
| coroutines                 | 27.0 ms                                                | 23.0 ms: 1.18x faster                                              |
| async_tree_none            | 528 ms                                                 | 450 ms: 1.17x faster                                               |
| richards_super             | 61.9 ms                                                | 53.3 ms: 1.16x faster                                              |
| deltablue                  | 3.92 ms                                                | 3.48 ms: 1.13x faster                                              |
| logging_silent             | 111 ns                                                 | 100 ns: 1.11x faster                                               |
| async_tree_memoization     | 639 ms                                                 | 580 ms: 1.10x faster                                               |
| sqlglot_parse              | 1.43 ms                                                | 1.33 ms: 1.08x faster                                              |
| async_tree_none_tg         | 491 ms                                                 | 456 ms: 1.08x faster                                               |
| chaos                      | 71.9 ms                                                | 66.9 ms: 1.07x faster                                              |
| pickle_pure_python         | 320 us                                                 | 300 us: 1.07x faster                                               |
| logging_simple             | 6.22 us                                                | 5.83 us: 1.07x faster                                              |
| tomli_loads                | 2.30 sec                                               | 2.17 sec: 1.06x faster                                             |
| async_tree_io              | 1.29 sec                                               | 1.22 sec: 1.06x faster                                             |
| logging_format             | 6.81 us                                                | 6.46 us: 1.05x faster                                              |
| djangocms                  | 33.5 us                                                | 31.8 us: 1.05x faster                                              |
| richards                   | 49.8 ms                                                | 47.5 ms: 1.05x faster                                              |
| async_tree_memoization_tg  | 626 ms                                                 | 599 ms: 1.05x faster                                               |
| async_tree_io_tg           | 1.29 sec                                               | 1.24 sec: 1.05x faster                                             |
| deepcopy_reduce            | 3.22 us                                                | 3.08 us: 1.04x faster                                              |
| sqlglot_transpile          | 1.75 ms                                                | 1.68 ms: 1.04x faster                                              |
| json_loads                 | 29.2 us                                                | 28.1 us: 1.04x faster                                              |
| deepcopy                   | 365 us                                                 | 351 us: 1.04x faster                                               |
| sqlglot_normalize          | 113 ms                                                 | 109 ms: 1.04x faster                                               |
| sympy_sum                  | 169 ms                                                 | 163 ms: 1.04x faster                                               |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 724 ms: 1.04x faster                                               |
| deepcopy_memo              | 40.2 us                                                | 38.9 us: 1.03x faster                                              |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 737 ms: 1.03x faster                                               |
| xml_etree_parse            | 164 ms                                                 | 160 ms: 1.03x faster                                               |
| sympy_str                  | 297 ms                                                 | 290 ms: 1.03x faster                                               |
| unpickle_list              | 5.21 us                                                | 5.09 us: 1.02x faster                                              |
| pidigits                   | 194 ms                                                 | 190 ms: 1.02x faster                                               |
| raytrace                   | 309 ms                                                 | 303 ms: 1.02x faster                                               |
| sympy_integrate            | 21.5 ms                                                | 21.4 ms: 1.00x faster                                              |
| pickle_dict                | 34.6 us                                                | 34.5 us: 1.00x faster                                              |
| xml_etree_iterparse        | 108 ms                                                 | 109 ms: 1.01x slower                                               |
| tornado_http               | 98.1 ms                                                | 99.3 ms: 1.01x slower                                              |
| pathlib                    | 18.5 ms                                                | 18.8 ms: 1.01x slower                                              |
| json                       | 5.24 ms                                                | 5.32 ms: 1.01x slower                                              |
| crypto_pyaes               | 76.7 ms                                                | 77.9 ms: 1.02x slower                                              |
| sympy_expand               | 484 ms                                                 | 492 ms: 1.02x slower                                               |
| unpickle_pure_python       | 242 us                                                 | 246 us: 1.02x slower                                               |
| html5lib                   | 64.8 ms                                                | 66.0 ms: 1.02x slower                                              |
| gc_traversal               | 4.01 ms                                                | 4.09 ms: 1.02x slower                                              |
| nbody                      | 96.0 ms                                                | 97.9 ms: 1.02x slower                                              |
| thrift                     | 784 us                                                 | 801 us: 1.02x slower                                               |
| dask                       | 365 ms                                                 | 373 ms: 1.02x slower                                               |
| chameleon                  | 6.70 ms                                                | 6.86 ms: 1.02x slower                                              |
| asyncio_websockets         | 550 ms                                                 | 564 ms: 1.02x slower                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.16 ms: 1.03x slower                                              |
| meteor_contest             | 109 ms                                                 | 112 ms: 1.03x slower                                               |
| django_template            | 33.5 ms                                                | 34.6 ms: 1.03x slower                                              |
| float                      | 78.9 ms                                                | 81.5 ms: 1.03x slower                                              |
| bench_thread_pool          | 834 us                                                 | 862 us: 1.03x slower                                               |
| pycparser                  | 1.19 sec                                               | 1.23 sec: 1.04x slower                                             |
| sqlglot_optimize           | 55.3 ms                                                | 57.6 ms: 1.04x slower                                              |
| genshi_xml                 | 53.4 ms                                                | 55.9 ms: 1.05x slower                                              |
| docutils                   | 2.66 sec                                               | 2.79 sec: 1.05x slower                                             |
| scimark_fft                | 345 ms                                                 | 363 ms: 1.05x slower                                               |
| create_gc_cycles           | 1.43 ms                                                | 1.51 ms: 1.05x slower                                              |
| xml_etree_process          | 56.9 ms                                                | 60.1 ms: 1.06x slower                                              |
| fannkuch                   | 405 ms                                                 | 429 ms: 1.06x slower                                               |
| nqueens                    | 87.9 ms                                                | 93.2 ms: 1.06x slower                                              |
| pprint_safe_repr           | 747 ms                                                 | 792 ms: 1.06x slower                                               |
| scimark_monte_carlo        | 70.7 ms                                                | 75.1 ms: 1.06x slower                                              |
| unpickle                   | 13.8 us                                                | 14.8 us: 1.07x slower                                              |
| mako                       | 10.7 ms                                                | 11.4 ms: 1.07x slower                                              |
| pickle                     | 11.0 us                                                | 11.8 us: 1.07x slower                                              |
| go                         | 149 ms                                                 | 159 ms: 1.07x slower                                               |
| scimark_sor                | 121 ms                                                 | 130 ms: 1.07x slower                                               |
| 2to3                       | 264 ms                                                 | 285 ms: 1.08x slower                                               |
| aiohttp                    | 1.12 ms                                                | 1.21 ms: 1.08x slower                                              |
| pprint_pformat             | 1.55 sec                                               | 1.69 sec: 1.09x slower                                             |
| gunicorn                   | 1.20 ms                                                | 1.30 ms: 1.09x slower                                              |
| xml_etree_generate         | 81.1 ms                                                | 88.4 ms: 1.09x slower                                              |
| genshi_text                | 22.5 ms                                                | 24.6 ms: 1.09x slower                                              |
| regex_compile              | 141 ms                                                 | 155 ms: 1.09x slower                                               |
| regex_dna                  | 205 ms                                                 | 224 ms: 1.09x slower                                               |
| hexiom                     | 6.89 ms                                                | 7.60 ms: 1.10x slower                                              |
| dulwich_log                | 64.6 ms                                                | 71.8 ms: 1.11x slower                                              |
| regex_effbot               | 3.51 ms                                                | 3.92 ms: 1.12x slower                                              |
| sqlite_synth               | 2.57 us                                                | 2.89 us: 1.12x slower                                              |
| regex_v8                   | 22.9 ms                                                | 25.7 ms: 1.12x slower                                              |
| pickle_list                | 4.59 us                                                | 5.19 us: 1.13x slower                                              |
| scimark_lu                 | 116 ms                                                 | 133 ms: 1.15x slower                                               |
| spectral_norm              | 108 ms                                                 | 125 ms: 1.15x slower                                               |
| pyflate                    | 434 ms                                                 | 513 ms: 1.18x slower                                               |
| telco                      | 6.86 ms                                                | 8.55 ms: 1.25x slower                                              |
| coverage                   | 78.8 ms                                                | 98.8 ms: 1.25x slower                                              |
| async_generators           | 374 ms                                                 | 469 ms: 1.26x slower                                               |
| mypy2                      | 686 ms                                                 | 905 ms: 1.32x slower                                               |
| python_startup             | 8.56 ms                                                | 11.5 ms: 1.34x slower                                              |
| python_startup_no_site     | 6.01 ms                                                | 10.1 ms: 1.68x slower                                              |
| unpack_sequence            | 43.5 ns                                                | 122 ns: 2.81x slower                                               |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (2): mdp, bench_mp_pool
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 93.33% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.13x
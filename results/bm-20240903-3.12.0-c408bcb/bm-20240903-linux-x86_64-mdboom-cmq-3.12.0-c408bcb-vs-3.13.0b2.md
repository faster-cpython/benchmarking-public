# Results vs. 3.13.0b2

- fork: mdboom
- ref: cmq
- machine: linux-x86_64
- commit hash: c408bcb
- commit date: 2024-09-03
- overall geometric mean: 1.02x slower
- HPT reliability: 96.35%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.59x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------:|
| 2to3           | 274 ms                                                     | 276 ms: 1.01x slower                               |
| chameleon      | 7.22 ms                                                    | 7.26 ms: 1.01x slower                              |
| docutils       | 2.83 sec                                                   | 2.76 sec: 1.02x faster                             |
| html5lib       | 67.2 ms                                                    | 66.3 ms: 1.01x faster                              |
| tornado_http   | 94.6 ms                                                    | 103 ms: 1.09x slower                               |
| Geometric mean | (ref)                                                      | 1.01x slower                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------:|
| async_tree_cpu_io_mixed    | 611 ms                                                     | 720 ms: 1.18x slower                               |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 719 ms: 1.22x slower                               |
| async_tree_io              | 939 ms                                                     | 1.16 sec: 1.23x slower                             |
| async_tree_none            | 378 ms                                                     | 472 ms: 1.25x slower                               |
| async_tree_memoization     | 463 ms                                                     | 580 ms: 1.25x slower                               |
| async_tree_io_tg           | 936 ms                                                     | 1.19 sec: 1.27x slower                             |
| async_tree_memoization_tg  | 444 ms                                                     | 572 ms: 1.29x slower                               |
| async_tree_none_tg         | 336 ms                                                     | 445 ms: 1.32x slower                               |
| Geometric mean             | (ref)                                                      | 1.25x slower                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------:|
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                               |
| nbody          | 88.3 ms                                                    | 92.0 ms: 1.04x slower                              |
| float          | 78.9 ms                                                    | 83.1 ms: 1.05x slower                              |
| Geometric mean | (ref)                                                      | 1.02x slower                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 209 ms: 1.06x faster                               |
| regex_v8       | 25.1 ms                                                    | 24.0 ms: 1.05x faster                              |
| regex_effbot   | 3.67 ms                                                    | 3.64 ms: 1.01x faster                              |
| regex_compile  | 137 ms                                                     | 149 ms: 1.09x slower                               |
| Geometric mean | (ref)                                                      | 1.01x faster                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------:|
| pickle_dict          | 34.8 us                                                    | 33.3 us: 1.04x faster                              |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.04x faster                              |
| pickle_list          | 5.11 us                                                    | 4.94 us: 1.03x faster                              |
| json_loads           | 28.9 us                                                    | 28.0 us: 1.03x faster                              |
| xml_etree_iterparse  | 107 ms                                                     | 106 ms: 1.01x faster                               |
| xml_etree_process    | 61.2 ms                                                    | 61.4 ms: 1.00x slower                              |
| xml_etree_generate   | 87.4 ms                                                    | 88.1 ms: 1.01x slower                              |
| unpickle_list        | 5.34 us                                                    | 5.41 us: 1.01x slower                              |
| unpickle_pure_python | 218 us                                                     | 230 us: 1.05x slower                               |
| tomli_loads          | 2.12 sec                                                   | 2.26 sec: 1.06x slower                             |
| pickle_pure_python   | 305 us                                                     | 326 us: 1.07x slower                               |
| unpickle             | 15.1 us                                                    | 16.1 us: 1.07x slower                              |
| Geometric mean       | (ref)                                                      | 1.01x slower                                       |

Benchmark hidden because not significant (2): xml_etree_parse, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 9.60 ms: 1.12x faster                              |
| python_startup_no_site | 7.11 ms                                                    | 6.94 ms: 1.02x faster                              |
| Geometric mean         | (ref)                                                      | 1.07x faster                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 23.2 ms: 1.02x faster                              |
| django_template | 34.8 ms                                                    | 34.5 ms: 1.01x faster                              |
| genshi_xml      | 51.6 ms                                                    | 52.0 ms: 1.01x slower                              |
| mako            | 11.2 ms                                                    | 11.4 ms: 1.02x slower                              |
| Geometric mean  | (ref)                                                      | 1.00x faster                                       |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------:|
| coverage                   | 93.1 ms                                                    | 73.9 ms: 1.26x faster                              |
| create_gc_cycles           | 1.82 ms                                                    | 1.46 ms: 1.24x faster                              |
| flaskblogging              | 9.01 ms                                                    | 7.46 ms: 1.21x faster                              |
| telco                      | 8.41 ms                                                    | 7.06 ms: 1.19x faster                              |
| python_startup             | 10.8 ms                                                    | 9.60 ms: 1.12x faster                              |
| richards_super             | 57.4 ms                                                    | 52.4 ms: 1.09x faster                              |
| richards                   | 50.9 ms                                                    | 46.6 ms: 1.09x faster                              |
| mdp                        | 2.79 sec                                                   | 2.59 sec: 1.07x faster                             |
| sqlite_synth               | 2.99 us                                                    | 2.80 us: 1.07x faster                              |
| regex_dna                  | 221 ms                                                     | 209 ms: 1.06x faster                               |
| spectral_norm              | 116 ms                                                     | 110 ms: 1.06x faster                               |
| typing_runtime_protocols   | 165 us                                                     | 157 us: 1.05x faster                               |
| regex_v8                   | 25.1 ms                                                    | 24.0 ms: 1.05x faster                              |
| pickle_dict                | 34.8 us                                                    | 33.3 us: 1.04x faster                              |
| gc_traversal               | 3.98 ms                                                    | 3.81 ms: 1.04x faster                              |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.04x faster                              |
| pickle_list                | 5.11 us                                                    | 4.94 us: 1.03x faster                              |
| go                         | 145 ms                                                     | 140 ms: 1.03x faster                               |
| json_loads                 | 28.9 us                                                    | 28.0 us: 1.03x faster                              |
| asyncio_websockets         | 567 ms                                                     | 551 ms: 1.03x faster                               |
| scimark_lu                 | 122 ms                                                     | 119 ms: 1.03x faster                               |
| gunicorn                   | 1.28 ms                                                    | 1.24 ms: 1.03x faster                              |
| scimark_fft                | 392 ms                                                     | 383 ms: 1.03x faster                               |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.03x faster                             |
| docutils                   | 2.83 sec                                                   | 2.76 sec: 1.02x faster                             |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                               |
| python_startup_no_site     | 7.11 ms                                                    | 6.94 ms: 1.02x faster                              |
| aiohttp                    | 1.18 ms                                                    | 1.16 ms: 1.02x faster                              |
| genshi_text                | 23.7 ms                                                    | 23.2 ms: 1.02x faster                              |
| deepcopy_reduce            | 3.35 us                                                    | 3.29 us: 1.02x faster                              |
| html5lib                   | 67.2 ms                                                    | 66.3 ms: 1.01x faster                              |
| xml_etree_iterparse        | 107 ms                                                     | 106 ms: 1.01x faster                               |
| json                       | 5.31 ms                                                    | 5.24 ms: 1.01x faster                              |
| thrift                     | 823 us                                                     | 813 us: 1.01x faster                               |
| pyflate                    | 484 ms                                                     | 478 ms: 1.01x faster                               |
| coroutines                 | 23.2 ms                                                    | 22.9 ms: 1.01x faster                              |
| sqlglot_optimize           | 55.5 ms                                                    | 54.9 ms: 1.01x faster                              |
| django_template            | 34.8 ms                                                    | 34.5 ms: 1.01x faster                              |
| regex_effbot               | 3.67 ms                                                    | 3.64 ms: 1.01x faster                              |
| xml_etree_process          | 61.2 ms                                                    | 61.4 ms: 1.00x slower                              |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                              |
| 2to3                       | 274 ms                                                     | 276 ms: 1.01x slower                               |
| chameleon                  | 7.22 ms                                                    | 7.26 ms: 1.01x slower                              |
| pprint_safe_repr           | 758 ms                                                     | 763 ms: 1.01x slower                               |
| meteor_contest             | 110 ms                                                     | 111 ms: 1.01x slower                               |
| genshi_xml                 | 51.6 ms                                                    | 52.0 ms: 1.01x slower                              |
| xml_etree_generate         | 87.4 ms                                                    | 88.1 ms: 1.01x slower                              |
| asyncio_tcp                | 508 ms                                                     | 514 ms: 1.01x slower                               |
| pycparser                  | 1.16 sec                                                   | 1.17 sec: 1.01x slower                             |
| unpickle_list              | 5.34 us                                                    | 5.41 us: 1.01x slower                              |
| sympy_expand               | 473 ms                                                     | 478 ms: 1.01x slower                               |
| deepcopy_memo              | 39.7 us                                                    | 40.2 us: 1.01x slower                              |
| logging_silent             | 105 ns                                                     | 106 ns: 1.01x slower                               |
| mako                       | 11.2 ms                                                    | 11.4 ms: 1.02x slower                              |
| bench_thread_pool          | 834 us                                                     | 851 us: 1.02x slower                               |
| dulwich_log                | 67.2 ms                                                    | 68.7 ms: 1.02x slower                              |
| sqlglot_parse              | 1.32 ms                                                    | 1.36 ms: 1.03x slower                              |
| sqlglot_transpile          | 1.63 ms                                                    | 1.68 ms: 1.03x slower                              |
| scimark_sor                | 127 ms                                                     | 132 ms: 1.03x slower                               |
| async_generators           | 442 ms                                                     | 459 ms: 1.04x slower                               |
| sympy_integrate            | 20.5 ms                                                    | 21.3 ms: 1.04x slower                              |
| hexiom                     | 6.30 ms                                                    | 6.55 ms: 1.04x slower                              |
| nbody                      | 88.3 ms                                                    | 92.0 ms: 1.04x slower                              |
| nqueens                    | 81.4 ms                                                    | 84.9 ms: 1.04x slower                              |
| djangocms                  | 31.5 us                                                    | 32.9 us: 1.04x slower                              |
| fannkuch                   | 402 ms                                                     | 420 ms: 1.04x slower                               |
| float                      | 78.9 ms                                                    | 83.1 ms: 1.05x slower                              |
| unpickle_pure_python       | 218 us                                                     | 230 us: 1.05x slower                               |
| sympy_str                  | 282 ms                                                     | 300 ms: 1.06x slower                               |
| tomli_loads                | 2.12 sec                                                   | 2.26 sec: 1.06x slower                             |
| pickle_pure_python         | 305 us                                                     | 326 us: 1.07x slower                               |
| unpickle                   | 15.1 us                                                    | 16.1 us: 1.07x slower                              |
| sympy_sum                  | 156 ms                                                     | 167 ms: 1.07x slower                               |
| crypto_pyaes               | 77.5 ms                                                    | 83.5 ms: 1.08x slower                              |
| tornado_http               | 94.6 ms                                                    | 103 ms: 1.09x slower                               |
| regex_compile              | 137 ms                                                     | 149 ms: 1.09x slower                               |
| scimark_monte_carlo        | 69.2 ms                                                    | 75.6 ms: 1.09x slower                              |
| chaos                      | 61.3 ms                                                    | 67.5 ms: 1.10x slower                              |
| logging_format             | 6.47 us                                                    | 7.23 us: 1.12x slower                              |
| logging_simple             | 5.74 us                                                    | 6.50 us: 1.13x slower                              |
| generators                 | 29.6 ms                                                    | 33.6 ms: 1.13x slower                              |
| pathlib                    | 17.3 ms                                                    | 19.7 ms: 1.14x slower                              |
| deltablue                  | 3.25 ms                                                    | 3.74 ms: 1.15x slower                              |
| raytrace                   | 267 ms                                                     | 309 ms: 1.16x slower                               |
| mypy2                      | 742 ms                                                     | 863 ms: 1.16x slower                               |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 720 ms: 1.18x slower                               |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 719 ms: 1.22x slower                               |
| async_tree_io              | 939 ms                                                     | 1.16 sec: 1.23x slower                             |
| async_tree_none            | 378 ms                                                     | 472 ms: 1.25x slower                               |
| async_tree_memoization     | 463 ms                                                     | 580 ms: 1.25x slower                               |
| async_tree_io_tg           | 936 ms                                                     | 1.19 sec: 1.27x slower                             |
| async_tree_memoization_tg  | 444 ms                                                     | 572 ms: 1.29x slower                               |
| comprehensions             | 16.6 us                                                    | 21.6 us: 1.30x slower                              |
| async_tree_none_tg         | 336 ms                                                     | 445 ms: 1.32x slower                               |
| Geometric mean             | (ref)                                                      | 1.02x slower                                       |

Benchmark hidden because not significant (9): xml_etree_parse, scimark_sparse_mat_mult, pickle, deepcopy, pprint_pformat, sqlglot_normalize, bpe_tokeniser, dask, pylint
Ignored benchmarks (3) of results/bm-20240903-3.12.0-c408bcb/bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence

# HPT report

- Reliability score: 96.35% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.59x
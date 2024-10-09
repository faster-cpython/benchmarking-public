# Results vs. 3.13.0b2

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: aa18ec3
- commit date: 2024-10-07
- overall geometric mean: 1.03x faster
- HPT reliability: 99.86%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 278 ms: 1.02x slower                                           |
| docutils       | 2.83 sec                                                   | 2.94 sec: 1.04x slower                                         |
| html5lib       | 67.2 ms                                                    | 65.0 ms: 1.03x faster                                          |
| tornado_http   | 94.6 ms                                                    | 95.6 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                      | 1.01x slower                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 319 ms: 1.19x faster                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 386 ms: 1.15x faster                                           |
| async_tree_memoization     | 463 ms                                                     | 406 ms: 1.14x faster                                           |
| async_tree_none_tg         | 336 ms                                                     | 309 ms: 1.09x faster                                           |
| async_tree_io_tg           | 936 ms                                                     | 872 ms: 1.07x faster                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 551 ms: 1.07x faster                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 575 ms: 1.06x faster                                           |
| async_tree_io              | 939 ms                                                     | 886 ms: 1.06x faster                                           |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 80.1 ms: 1.10x faster                                          |
| float          | 78.9 ms                                                    | 71.9 ms: 1.10x faster                                          |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                           |
| Geometric mean | (ref)                                                      | 1.08x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 227 ms: 1.03x slower                                           |
| regex_compile  | 137 ms                                                     | 143 ms: 1.04x slower                                           |
| regex_v8       | 25.1 ms                                                    | 26.4 ms: 1.05x slower                                          |
| Geometric mean | (ref)                                                      | 1.03x slower                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.6 ms: 1.13x faster                                          |
| xml_etree_process    | 61.2 ms                                                    | 54.7 ms: 1.12x faster                                          |
| xml_etree_parse      | 162 ms                                                     | 145 ms: 1.11x faster                                           |
| tomli_loads          | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                         |
| xml_etree_iterparse  | 107 ms                                                     | 98.2 ms: 1.09x faster                                          |
| json_loads           | 28.9 us                                                    | 27.0 us: 1.07x faster                                          |
| json_dumps           | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                          |
| unpickle             | 15.1 us                                                    | 14.7 us: 1.03x faster                                          |
| unpickle_list        | 5.34 us                                                    | 5.29 us: 1.01x faster                                          |
| pickle_pure_python   | 305 us                                                     | 302 us: 1.01x faster                                           |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                           |
| pickle_list          | 5.11 us                                                    | 5.13 us: 1.01x slower                                          |
| pickle_dict          | 34.8 us                                                    | 35.5 us: 1.02x slower                                          |
| pickle               | 11.5 us                                                    | 11.8 us: 1.03x slower                                          |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                          |
| python_startup_no_site | 7.11 ms                                                    | 7.10 ms: 1.00x faster                                          |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.94 ms: 1.13x faster                                          |
| django_template | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                          |
| genshi_text     | 23.7 ms                                                    | 25.4 ms: 1.07x slower                                          |
| genshi_xml      | 51.6 ms                                                    | 58.2 ms: 1.13x slower                                          |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.1 us: 1.46x faster                                          |
| deepcopy                   | 367 us                                                     | 263 us: 1.40x faster                                           |
| scimark_fft                | 392 ms                                                     | 305 ms: 1.29x faster                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.66 us: 1.26x faster                                          |
| richards_super             | 57.4 ms                                                    | 45.8 ms: 1.25x faster                                          |
| richards                   | 50.9 ms                                                    | 41.0 ms: 1.24x faster                                          |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.37 ms: 1.20x faster                                          |
| async_tree_none            | 378 ms                                                     | 319 ms: 1.19x faster                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 386 ms: 1.15x faster                                           |
| crypto_pyaes               | 77.5 ms                                                    | 67.4 ms: 1.15x faster                                          |
| spectral_norm              | 116 ms                                                     | 102 ms: 1.14x faster                                           |
| async_tree_memoization     | 463 ms                                                     | 406 ms: 1.14x faster                                           |
| mako                       | 11.2 ms                                                    | 9.94 ms: 1.13x faster                                          |
| xml_etree_generate         | 87.4 ms                                                    | 77.6 ms: 1.13x faster                                          |
| bpe_tokeniser              | 5.02 sec                                                   | 4.47 sec: 1.12x faster                                         |
| xml_etree_process          | 61.2 ms                                                    | 54.7 ms: 1.12x faster                                          |
| xml_etree_parse            | 162 ms                                                     | 145 ms: 1.11x faster                                           |
| scimark_lu                 | 122 ms                                                     | 110 ms: 1.11x faster                                           |
| telco                      | 8.41 ms                                                    | 7.62 ms: 1.10x faster                                          |
| nbody                      | 88.3 ms                                                    | 80.1 ms: 1.10x faster                                          |
| tomli_loads                | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                         |
| float                      | 78.9 ms                                                    | 71.9 ms: 1.10x faster                                          |
| sqlite_synth               | 2.99 us                                                    | 2.73 us: 1.09x faster                                          |
| xml_etree_iterparse        | 107 ms                                                     | 98.2 ms: 1.09x faster                                          |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                          |
| pprint_safe_repr           | 758 ms                                                     | 698 ms: 1.09x faster                                           |
| async_tree_none_tg         | 336 ms                                                     | 309 ms: 1.09x faster                                           |
| coverage                   | 93.1 ms                                                    | 85.8 ms: 1.09x faster                                          |
| go                         | 145 ms                                                     | 134 ms: 1.08x faster                                           |
| scimark_monte_carlo        | 69.2 ms                                                    | 64.0 ms: 1.08x faster                                          |
| scimark_sor                | 127 ms                                                     | 118 ms: 1.08x faster                                           |
| fannkuch                   | 402 ms                                                     | 374 ms: 1.07x faster                                           |
| pprint_pformat             | 1.56 sec                                                   | 1.45 sec: 1.07x faster                                         |
| async_tree_io_tg           | 936 ms                                                     | 872 ms: 1.07x faster                                           |
| json                       | 5.31 ms                                                    | 4.96 ms: 1.07x faster                                          |
| json_loads                 | 28.9 us                                                    | 27.0 us: 1.07x faster                                          |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 551 ms: 1.07x faster                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 575 ms: 1.06x faster                                           |
| gc_traversal               | 3.98 ms                                                    | 3.75 ms: 1.06x faster                                          |
| async_tree_io              | 939 ms                                                     | 886 ms: 1.06x faster                                           |
| pyflate                    | 484 ms                                                     | 457 ms: 1.06x faster                                           |
| json_dumps                 | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                          |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                          |
| logging_silent             | 105 ns                                                     | 100.0 ns: 1.05x faster                                         |
| logging_format             | 6.47 us                                                    | 6.19 us: 1.05x faster                                          |
| thrift                     | 823 us                                                     | 790 us: 1.04x faster                                           |
| html5lib                   | 67.2 ms                                                    | 65.0 ms: 1.03x faster                                          |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                           |
| asyncio_tcp                | 508 ms                                                     | 493 ms: 1.03x faster                                           |
| unpickle                   | 15.1 us                                                    | 14.7 us: 1.03x faster                                          |
| mdp                        | 2.79 sec                                                   | 2.71 sec: 1.03x faster                                         |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                         |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                           |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                           |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                          |
| logging_simple             | 5.74 us                                                    | 5.67 us: 1.01x faster                                          |
| deltablue                  | 3.25 ms                                                    | 3.21 ms: 1.01x faster                                          |
| chaos                      | 61.3 ms                                                    | 60.7 ms: 1.01x faster                                          |
| unpickle_list              | 5.34 us                                                    | 5.29 us: 1.01x faster                                          |
| typing_runtime_protocols   | 165 us                                                     | 163 us: 1.01x faster                                           |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                           |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                           |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                          |
| python_startup_no_site     | 7.11 ms                                                    | 7.10 ms: 1.00x faster                                          |
| pickle_list                | 5.11 us                                                    | 5.13 us: 1.01x slower                                          |
| tornado_http               | 94.6 ms                                                    | 95.6 ms: 1.01x slower                                          |
| 2to3                       | 274 ms                                                     | 278 ms: 1.02x slower                                           |
| sqlglot_parse              | 1.32 ms                                                    | 1.34 ms: 1.02x slower                                          |
| dulwich_log                | 67.2 ms                                                    | 68.5 ms: 1.02x slower                                          |
| pickle_dict                | 34.8 us                                                    | 35.5 us: 1.02x slower                                          |
| comprehensions             | 16.6 us                                                    | 17.0 us: 1.03x slower                                          |
| regex_dna                  | 221 ms                                                     | 227 ms: 1.03x slower                                           |
| pickle                     | 11.5 us                                                    | 11.8 us: 1.03x slower                                          |
| django_template            | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                          |
| sqlglot_transpile          | 1.63 ms                                                    | 1.69 ms: 1.03x slower                                          |
| raytrace                   | 267 ms                                                     | 276 ms: 1.03x slower                                           |
| async_generators           | 442 ms                                                     | 457 ms: 1.03x slower                                           |
| docutils                   | 2.83 sec                                                   | 2.94 sec: 1.04x slower                                         |
| regex_compile              | 137 ms                                                     | 143 ms: 1.04x slower                                           |
| sqlglot_normalize          | 110 ms                                                     | 115 ms: 1.04x slower                                           |
| pycparser                  | 1.16 sec                                                   | 1.21 sec: 1.05x slower                                         |
| regex_v8                   | 25.1 ms                                                    | 26.4 ms: 1.05x slower                                          |
| nqueens                    | 81.4 ms                                                    | 85.8 ms: 1.05x slower                                          |
| sympy_expand               | 473 ms                                                     | 499 ms: 1.05x slower                                           |
| sympy_str                  | 282 ms                                                     | 300 ms: 1.06x slower                                           |
| genshi_text                | 23.7 ms                                                    | 25.4 ms: 1.07x slower                                          |
| bench_thread_pool          | 834 us                                                     | 897 us: 1.08x slower                                           |
| sqlglot_optimize           | 55.5 ms                                                    | 59.9 ms: 1.08x slower                                          |
| hexiom                     | 6.30 ms                                                    | 6.99 ms: 1.11x slower                                          |
| genshi_xml                 | 51.6 ms                                                    | 58.2 ms: 1.13x slower                                          |
| sympy_sum                  | 156 ms                                                     | 177 ms: 1.14x slower                                           |
| sympy_integrate            | 20.5 ms                                                    | 23.4 ms: 1.14x slower                                          |
| pylint                     | 317 ms                                                     | 373 ms: 1.17x slower                                           |
| generators                 | 29.6 ms                                                    | 35.1 ms: 1.18x slower                                          |
| bench_mp_pool              | 23.9 ms                                                    | 61.3 ms: 2.57x slower                                          |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                   |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241007-3.14.0a0-aa18ec3-JIT/bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3.json: unpack_sequence

# HPT report

- Reliability score: 99.86% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x
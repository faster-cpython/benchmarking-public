# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: decref_escapes
- machine: linux-x86_64
- commit hash: 87cbfd7
- commit date: 2024-09-23
- overall geometric mean: 1.04x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 278 ms: 1.01x slower                                                  |
| docutils       | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                                |
| html5lib       | 67.2 ms                                                    | 62.7 ms: 1.07x faster                                                 |
| Geometric mean | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 317 ms: 1.19x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 395 ms: 1.17x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.14x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 308 ms: 1.09x faster                                                  |
| async_tree_io              | 939 ms                                                     | 862 ms: 1.09x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 874 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 574 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 557 ms: 1.05x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.6 ms: 1.12x faster                                                 |
| nbody          | 88.3 ms                                                    | 81.4 ms: 1.08x faster                                                 |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                      | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.1 ms: 1.04x faster                                                 |
| regex_dna      | 221 ms                                                     | 215 ms: 1.03x faster                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.61 ms: 1.02x faster                                                 |
| regex_compile  | 137 ms                                                     | 142 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 78.2 ms: 1.12x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 55.0 ms: 1.11x faster                                                 |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                  |
| tomli_loads          | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                |
| xml_etree_iterparse  | 107 ms                                                     | 99.3 ms: 1.08x faster                                                 |
| json_loads           | 28.9 us                                                    | 26.7 us: 1.08x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                                 |
| pickle_dict          | 34.8 us                                                    | 33.2 us: 1.05x faster                                                 |
| pickle_list          | 5.11 us                                                    | 5.04 us: 1.01x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                  |
| unpickle_list        | 5.34 us                                                    | 5.31 us: 1.01x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 308 us: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.77 ms: 1.15x faster                                                 |
| django_template | 34.8 ms                                                    | 36.4 ms: 1.05x slower                                                 |
| genshi_text     | 23.7 ms                                                    | 24.9 ms: 1.05x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 60.0 ms: 1.16x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.0 us: 1.47x faster                                                 |
| deepcopy                   | 367 us                                                     | 260 us: 1.41x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                    | 2.62 us: 1.28x faster                                                 |
| scimark_fft                | 392 ms                                                     | 315 ms: 1.25x faster                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.32 ms: 1.22x faster                                                 |
| richards_super             | 57.4 ms                                                    | 47.2 ms: 1.22x faster                                                 |
| async_tree_none            | 378 ms                                                     | 317 ms: 1.19x faster                                                  |
| richards                   | 50.9 ms                                                    | 42.7 ms: 1.19x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 395 ms: 1.17x faster                                                  |
| mako                       | 11.2 ms                                                    | 9.77 ms: 1.15x faster                                                 |
| crypto_pyaes               | 77.5 ms                                                    | 67.6 ms: 1.15x faster                                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.14x faster                                                  |
| spectral_norm              | 116 ms                                                     | 103 ms: 1.13x faster                                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.47 sec: 1.12x faster                                                |
| xml_etree_generate         | 87.4 ms                                                    | 78.2 ms: 1.12x faster                                                 |
| float                      | 78.9 ms                                                    | 70.6 ms: 1.12x faster                                                 |
| xml_etree_process          | 61.2 ms                                                    | 55.0 ms: 1.11x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                  |
| mdp                        | 2.79 sec                                                   | 2.52 sec: 1.10x faster                                                |
| coverage                   | 93.1 ms                                                    | 84.4 ms: 1.10x faster                                                 |
| sqlite_synth               | 2.99 us                                                    | 2.73 us: 1.10x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 63.1 ms: 1.10x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 308 ms: 1.09x faster                                                  |
| pyflate                    | 484 ms                                                     | 443 ms: 1.09x faster                                                  |
| go                         | 145 ms                                                     | 133 ms: 1.09x faster                                                  |
| async_tree_io              | 939 ms                                                     | 862 ms: 1.09x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                |
| nbody                      | 88.3 ms                                                    | 81.4 ms: 1.08x faster                                                 |
| scimark_lu                 | 122 ms                                                     | 112 ms: 1.08x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 99.3 ms: 1.08x faster                                                 |
| json_loads                 | 28.9 us                                                    | 26.7 us: 1.08x faster                                                 |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                 |
| scimark_sor                | 127 ms                                                     | 119 ms: 1.07x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 874 ms: 1.07x faster                                                  |
| html5lib                   | 67.2 ms                                                    | 62.7 ms: 1.07x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 574 ms: 1.06x faster                                                  |
| json_dumps                 | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                                 |
| fannkuch                   | 402 ms                                                     | 380 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 557 ms: 1.05x faster                                                  |
| json                       | 5.31 ms                                                    | 5.04 ms: 1.05x faster                                                 |
| pickle_dict                | 34.8 us                                                    | 33.2 us: 1.05x faster                                                 |
| thrift                     | 823 us                                                     | 786 us: 1.05x faster                                                  |
| pprint_safe_repr           | 758 ms                                                     | 726 ms: 1.05x faster                                                  |
| telco                      | 8.41 ms                                                    | 8.06 ms: 1.04x faster                                                 |
| regex_v8                   | 25.1 ms                                                    | 24.1 ms: 1.04x faster                                                 |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                  |
| chaos                      | 61.3 ms                                                    | 59.4 ms: 1.03x faster                                                 |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                 |
| logging_format             | 6.47 us                                                    | 6.28 us: 1.03x faster                                                 |
| asyncio_tcp                | 508 ms                                                     | 494 ms: 1.03x faster                                                  |
| regex_dna                  | 221 ms                                                     | 215 ms: 1.03x faster                                                  |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| coroutines                 | 23.2 ms                                                    | 22.6 ms: 1.02x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                  |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                |
| gc_traversal               | 3.98 ms                                                    | 3.91 ms: 1.02x faster                                                 |
| typing_runtime_protocols   | 165 us                                                     | 162 us: 1.02x faster                                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.53 sec: 1.02x faster                                                |
| regex_effbot               | 3.67 ms                                                    | 3.61 ms: 1.02x faster                                                 |
| logging_silent             | 105 ns                                                     | 103 ns: 1.01x faster                                                  |
| pickle_list                | 5.11 us                                                    | 5.04 us: 1.01x faster                                                 |
| logging_simple             | 5.74 us                                                    | 5.69 us: 1.01x faster                                                 |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                                  |
| unpickle_list              | 5.34 us                                                    | 5.31 us: 1.01x faster                                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| bench_thread_pool          | 834 us                                                     | 839 us: 1.01x slower                                                  |
| pickle_pure_python         | 305 us                                                     | 308 us: 1.01x slower                                                  |
| comprehensions             | 16.6 us                                                    | 16.8 us: 1.01x slower                                                 |
| 2to3                       | 274 ms                                                     | 278 ms: 1.01x slower                                                  |
| dulwich_log                | 67.2 ms                                                    | 68.5 ms: 1.02x slower                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.35 ms: 1.02x slower                                                 |
| sqlglot_normalize          | 110 ms                                                     | 114 ms: 1.03x slower                                                  |
| async_generators           | 442 ms                                                     | 457 ms: 1.03x slower                                                  |
| regex_compile              | 137 ms                                                     | 142 ms: 1.04x slower                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.71 ms: 1.04x slower                                                 |
| raytrace                   | 267 ms                                                     | 279 ms: 1.04x slower                                                  |
| django_template            | 34.8 ms                                                    | 36.4 ms: 1.05x slower                                                 |
| docutils                   | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                                |
| sqlglot_optimize           | 55.5 ms                                                    | 58.2 ms: 1.05x slower                                                 |
| genshi_text                | 23.7 ms                                                    | 24.9 ms: 1.05x slower                                                 |
| nqueens                    | 81.4 ms                                                    | 86.1 ms: 1.06x slower                                                 |
| sympy_str                  | 282 ms                                                     | 299 ms: 1.06x slower                                                  |
| sympy_expand               | 473 ms                                                     | 505 ms: 1.07x slower                                                  |
| sympy_sum                  | 156 ms                                                     | 172 ms: 1.10x slower                                                  |
| sympy_integrate            | 20.5 ms                                                    | 22.7 ms: 1.11x slower                                                 |
| hexiom                     | 6.30 ms                                                    | 7.00 ms: 1.11x slower                                                 |
| generators                 | 29.6 ms                                                    | 33.0 ms: 1.11x slower                                                 |
| genshi_xml                 | 51.6 ms                                                    | 60.0 ms: 1.16x slower                                                 |
| pylint                     | 317 ms                                                     | 374 ms: 1.18x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                          |

Benchmark hidden because not significant (5): unpickle, pickle, tornado_http, deltablue, pycparser
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240923-3.14.0a0-87cbfd7-JIT/bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7.json: unpack_sequence

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.08x
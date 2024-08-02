# Results vs. 3.13.0b2

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: d57f8a9
- commit date: 2024-08-02
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 274 ms                                                     | 319 ms: 1.16x slower                                  |
| docutils       | 2.83 sec                                                   | 3.17 sec: 1.12x slower                                |
| html5lib       | 67.2 ms                                                    | 73.9 ms: 1.10x slower                                 |
| tornado_http   | 94.6 ms                                                    | 97.6 ms: 1.03x slower                                 |
| Geometric mean | (ref)                                                      | 1.10x slower                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 345 ms: 1.10x faster                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 408 ms: 1.09x faster                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 545 ms: 1.08x faster                                  |
| async_tree_none_tg         | 336 ms                                                     | 314 ms: 1.07x faster                                  |
| async_tree_io_tg           | 936 ms                                                     | 886 ms: 1.06x faster                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 579 ms: 1.06x faster                                  |
| Geometric mean             | (ref)                                                      | 1.06x faster                                          |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                  |
| float          | 78.9 ms                                                    | 86.2 ms: 1.09x slower                                 |
| nbody          | 88.3 ms                                                    | 122 ms: 1.38x slower                                  |
| Geometric mean | (ref)                                                      | 1.14x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                 |
| regex_effbot   | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                 |
| regex_dna      | 221 ms                                                     | 224 ms: 1.01x slower                                  |
| regex_compile  | 137 ms                                                     | 184 ms: 1.35x slower                                  |
| Geometric mean | (ref)                                                      | 1.08x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 149 ms: 1.08x faster                                  |
| json_loads           | 28.9 us                                                    | 28.3 us: 1.02x faster                                 |
| json_dumps           | 10.7 ms                                                    | 10.8 ms: 1.01x slower                                 |
| xml_etree_iterparse  | 107 ms                                                     | 109 ms: 1.02x slower                                  |
| xml_etree_process    | 61.2 ms                                                    | 65.0 ms: 1.06x slower                                 |
| xml_etree_generate   | 87.4 ms                                                    | 93.7 ms: 1.07x slower                                 |
| tomli_loads          | 2.12 sec                                                   | 2.57 sec: 1.21x slower                                |
| unpickle_pure_python | 218 us                                                     | 272 us: 1.25x slower                                  |
| pickle_pure_python   | 305 us                                                     | 404 us: 1.32x slower                                  |
| Geometric mean       | (ref)                                                      | 1.09x slower                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 28.0 ms: 1.18x slower                                 |
| django_template | 34.8 ms                                                    | 41.4 ms: 1.19x slower                                 |
| mako            | 11.2 ms                                                    | 13.9 ms: 1.23x slower                                 |
| genshi_xml      | 51.6 ms                                                    | 64.1 ms: 1.24x slower                                 |
| Geometric mean  | (ref)                                                      | 1.21x slower                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| coverage                   | 93.1 ms                                                    | 83.6 ms: 1.11x faster                                 |
| deepcopy                   | 367 us                                                     | 333 us: 1.10x faster                                  |
| async_tree_none            | 378 ms                                                     | 345 ms: 1.10x faster                                  |
| gc_traversal               | 3.98 ms                                                    | 3.65 ms: 1.09x faster                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 408 ms: 1.09x faster                                  |
| xml_etree_parse            | 162 ms                                                     | 149 ms: 1.08x faster                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 545 ms: 1.08x faster                                  |
| async_tree_none_tg         | 336 ms                                                     | 314 ms: 1.07x faster                                  |
| async_tree_io_tg           | 936 ms                                                     | 886 ms: 1.06x faster                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 579 ms: 1.06x faster                                  |
| pathlib                    | 17.3 ms                                                    | 16.6 ms: 1.05x faster                                 |
| deepcopy_reduce            | 3.35 us                                                    | 3.24 us: 1.03x faster                                 |
| create_gc_cycles           | 1.82 ms                                                    | 1.77 ms: 1.02x faster                                 |
| thrift                     | 823 us                                                     | 805 us: 1.02x faster                                  |
| json_loads                 | 28.9 us                                                    | 28.3 us: 1.02x faster                                 |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                  |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                 |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                  |
| regex_v8                   | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                 |
| json                       | 5.31 ms                                                    | 5.25 ms: 1.01x faster                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.82 sec: 1.01x faster                                |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                 |
| regex_effbot               | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                 |
| json_dumps                 | 10.7 ms                                                    | 10.8 ms: 1.01x slower                                 |
| regex_dna                  | 221 ms                                                     | 224 ms: 1.01x slower                                  |
| xml_etree_iterparse        | 107 ms                                                     | 109 ms: 1.02x slower                                  |
| dask                       | 369 ms                                                     | 377 ms: 1.02x slower                                  |
| tornado_http               | 94.6 ms                                                    | 97.6 ms: 1.03x slower                                 |
| deepcopy_memo              | 39.7 us                                                    | 41.0 us: 1.03x slower                                 |
| bench_thread_pool          | 834 us                                                     | 862 us: 1.03x slower                                  |
| async_generators           | 442 ms                                                     | 459 ms: 1.04x slower                                  |
| telco                      | 8.41 ms                                                    | 8.79 ms: 1.04x slower                                 |
| xml_etree_process          | 61.2 ms                                                    | 65.0 ms: 1.06x slower                                 |
| mdp                        | 2.79 sec                                                   | 2.97 sec: 1.07x slower                                |
| xml_etree_generate         | 87.4 ms                                                    | 93.7 ms: 1.07x slower                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.71 ms: 1.08x slower                                 |
| float                      | 78.9 ms                                                    | 86.2 ms: 1.09x slower                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 5.52 sec: 1.10x slower                                |
| html5lib                   | 67.2 ms                                                    | 73.9 ms: 1.10x slower                                 |
| logging_simple             | 5.74 us                                                    | 6.33 us: 1.10x slower                                 |
| scimark_fft                | 392 ms                                                     | 436 ms: 1.11x slower                                  |
| richards_super             | 57.4 ms                                                    | 64.0 ms: 1.12x slower                                 |
| meteor_contest             | 110 ms                                                     | 123 ms: 1.12x slower                                  |
| richards                   | 50.9 ms                                                    | 56.9 ms: 1.12x slower                                 |
| docutils                   | 2.83 sec                                                   | 3.17 sec: 1.12x slower                                |
| logging_format             | 6.47 us                                                    | 7.27 us: 1.12x slower                                 |
| scimark_lu                 | 122 ms                                                     | 138 ms: 1.13x slower                                  |
| typing_runtime_protocols   | 165 us                                                     | 187 us: 1.14x slower                                  |
| pylint                     | 317 ms                                                     | 362 ms: 1.14x slower                                  |
| sympy_sum                  | 156 ms                                                     | 180 ms: 1.15x slower                                  |
| crypto_pyaes               | 77.5 ms                                                    | 90.0 ms: 1.16x slower                                 |
| 2to3                       | 274 ms                                                     | 319 ms: 1.16x slower                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 65.5 ms: 1.18x slower                                 |
| sympy_str                  | 282 ms                                                     | 333 ms: 1.18x slower                                  |
| genshi_text                | 23.7 ms                                                    | 28.0 ms: 1.18x slower                                 |
| sympy_integrate            | 20.5 ms                                                    | 24.3 ms: 1.18x slower                                 |
| pyflate                    | 484 ms                                                     | 574 ms: 1.19x slower                                  |
| django_template            | 34.8 ms                                                    | 41.4 ms: 1.19x slower                                 |
| raytrace                   | 267 ms                                                     | 318 ms: 1.19x slower                                  |
| sympy_expand               | 473 ms                                                     | 564 ms: 1.19x slower                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.96 ms: 1.20x slower                                 |
| tomli_loads                | 2.12 sec                                                   | 2.57 sec: 1.21x slower                                |
| sqlglot_parse              | 1.32 ms                                                    | 1.60 ms: 1.21x slower                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 84.4 ms: 1.22x slower                                 |
| go                         | 145 ms                                                     | 177 ms: 1.22x slower                                  |
| sqlglot_normalize          | 110 ms                                                     | 136 ms: 1.23x slower                                  |
| mako                       | 11.2 ms                                                    | 13.9 ms: 1.23x slower                                 |
| pycparser                  | 1.16 sec                                                   | 1.43 sec: 1.23x slower                                |
| fannkuch                   | 402 ms                                                     | 498 ms: 1.24x slower                                  |
| scimark_sor                | 127 ms                                                     | 158 ms: 1.24x slower                                  |
| spectral_norm              | 116 ms                                                     | 144 ms: 1.24x slower                                  |
| genshi_xml                 | 51.6 ms                                                    | 64.1 ms: 1.24x slower                                 |
| deltablue                  | 3.25 ms                                                    | 4.04 ms: 1.24x slower                                 |
| unpickle_pure_python       | 218 us                                                     | 272 us: 1.25x slower                                  |
| pprint_safe_repr           | 758 ms                                                     | 951 ms: 1.25x slower                                  |
| nqueens                    | 81.4 ms                                                    | 103 ms: 1.27x slower                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.98 sec: 1.27x slower                                |
| chaos                      | 61.3 ms                                                    | 79.5 ms: 1.30x slower                                 |
| pickle_pure_python         | 305 us                                                     | 404 us: 1.32x slower                                  |
| regex_compile              | 137 ms                                                     | 184 ms: 1.35x slower                                  |
| nbody                      | 88.3 ms                                                    | 122 ms: 1.38x slower                                  |
| logging_silent             | 105 ns                                                     | 146 ns: 1.40x slower                                  |
| comprehensions             | 16.6 us                                                    | 23.8 us: 1.43x slower                                 |
| generators                 | 29.6 ms                                                    | 43.4 ms: 1.46x slower                                 |
| hexiom                     | 6.30 ms                                                    | 9.64 ms: 1.53x slower                                 |
| Geometric mean             | (ref)                                                      | 1.10x slower                                          |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_io, asyncio_tcp, coroutines
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.02x
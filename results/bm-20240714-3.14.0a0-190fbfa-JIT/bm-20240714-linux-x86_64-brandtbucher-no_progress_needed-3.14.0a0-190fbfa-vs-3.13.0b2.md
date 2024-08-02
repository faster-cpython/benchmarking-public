# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 190fbfa
- commit date: 2024-07-14
- overall geometric mean: 1.03x faster
- HPT reliability: 99.67%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 273 ms: 1.00x faster                                                      |
| docutils       | 2.83 sec                                                   | 2.98 sec: 1.05x slower                                                    |
| html5lib       | 67.2 ms                                                    | 71.6 ms: 1.07x slower                                                     |
| tornado_http   | 94.6 ms                                                    | 98.3 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                      | 1.04x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 383 ms: 1.16x faster                                                      |
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 412 ms: 1.12x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 305 ms: 1.10x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 867 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 545 ms: 1.08x faster                                                      |
| async_tree_io              | 939 ms                                                     | 910 ms: 1.03x faster                                                      |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 77.0 ms: 1.15x faster                                                     |
| float          | 78.9 ms                                                    | 70.4 ms: 1.12x faster                                                     |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                      | 1.09x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 23.7 ms: 1.06x faster                                                     |
| regex_compile  | 137 ms                                                     | 132 ms: 1.04x faster                                                      |
| regex_effbot   | 3.67 ms                                                    | 3.61 ms: 1.02x faster                                                     |
| regex_dna      | 221 ms                                                     | 219 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                      | 1.03x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                    |
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.09x faster                                                      |
| json_loads           | 28.9 us                                                    | 27.5 us: 1.05x faster                                                     |
| xml_etree_process    | 61.2 ms                                                    | 58.6 ms: 1.04x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                     | 103 ms: 1.04x faster                                                      |
| xml_etree_generate   | 87.4 ms                                                    | 84.3 ms: 1.04x faster                                                     |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                     |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.01x faster                                                      |
| pickle_pure_python   | 305 us                                                     | 304 us: 1.01x faster                                                      |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                     |
| python_startup_no_site | 7.11 ms                                                    | 7.13 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.96 ms: 1.13x faster                                                     |
| django_template | 34.8 ms                                                    | 40.4 ms: 1.16x slower                                                     |
| genshi_text     | 23.7 ms                                                    | 27.7 ms: 1.17x slower                                                     |
| genshi_xml      | 51.6 ms                                                    | 63.3 ms: 1.23x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.10x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.6 us: 1.49x faster                                                     |
| deepcopy                   | 367 us                                                     | 258 us: 1.42x faster                                                      |
| richards                   | 50.9 ms                                                    | 39.1 ms: 1.30x faster                                                     |
| richards_super             | 57.4 ms                                                    | 45.3 ms: 1.27x faster                                                     |
| scimark_fft                | 392 ms                                                     | 313 ms: 1.25x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                    | 2.68 us: 1.25x faster                                                     |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.36 ms: 1.21x faster                                                     |
| crypto_pyaes               | 77.5 ms                                                    | 66.7 ms: 1.16x faster                                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 383 ms: 1.16x faster                                                      |
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                      |
| spectral_norm              | 116 ms                                                     | 101 ms: 1.15x faster                                                      |
| nbody                      | 88.3 ms                                                    | 77.0 ms: 1.15x faster                                                     |
| mako                       | 11.2 ms                                                    | 9.96 ms: 1.13x faster                                                     |
| async_tree_memoization     | 463 ms                                                     | 412 ms: 1.12x faster                                                      |
| float                      | 78.9 ms                                                    | 70.4 ms: 1.12x faster                                                     |
| async_tree_none_tg         | 336 ms                                                     | 305 ms: 1.10x faster                                                      |
| tomli_loads                | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                    |
| fannkuch                   | 402 ms                                                     | 366 ms: 1.10x faster                                                      |
| chaos                      | 61.3 ms                                                    | 56.0 ms: 1.10x faster                                                     |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.09x faster                                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 63.4 ms: 1.09x faster                                                     |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                     |
| async_tree_io_tg           | 936 ms                                                     | 867 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                      |
| pyflate                    | 484 ms                                                     | 449 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 545 ms: 1.08x faster                                                      |
| gc_traversal               | 3.98 ms                                                    | 3.73 ms: 1.07x faster                                                     |
| logging_format             | 6.47 us                                                    | 6.09 us: 1.06x faster                                                     |
| pprint_pformat             | 1.56 sec                                                   | 1.46 sec: 1.06x faster                                                    |
| bpe_tokeniser              | 5.02 sec                                                   | 4.73 sec: 1.06x faster                                                    |
| pprint_safe_repr           | 758 ms                                                     | 715 ms: 1.06x faster                                                      |
| regex_v8                   | 25.1 ms                                                    | 23.7 ms: 1.06x faster                                                     |
| telco                      | 8.41 ms                                                    | 8.00 ms: 1.05x faster                                                     |
| json_loads                 | 28.9 us                                                    | 27.5 us: 1.05x faster                                                     |
| xml_etree_process          | 61.2 ms                                                    | 58.6 ms: 1.04x faster                                                     |
| json                       | 5.31 ms                                                    | 5.10 ms: 1.04x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                     | 103 ms: 1.04x faster                                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.27 ms: 1.04x faster                                                     |
| xml_etree_generate         | 87.4 ms                                                    | 84.3 ms: 1.04x faster                                                     |
| logging_simple             | 5.74 us                                                    | 5.54 us: 1.04x faster                                                     |
| regex_compile              | 137 ms                                                     | 132 ms: 1.04x faster                                                      |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                     |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                                      |
| async_tree_io              | 939 ms                                                     | 910 ms: 1.03x faster                                                      |
| go                         | 145 ms                                                     | 140 ms: 1.03x faster                                                      |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                     |
| pycparser                  | 1.16 sec                                                   | 1.13 sec: 1.03x faster                                                    |
| logging_silent             | 105 ns                                                     | 102 ns: 1.02x faster                                                      |
| scimark_lu                 | 122 ms                                                     | 119 ms: 1.02x faster                                                      |
| thrift                     | 823 us                                                     | 807 us: 1.02x faster                                                      |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                                      |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                                      |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                     |
| regex_effbot               | 3.67 ms                                                    | 3.61 ms: 1.02x faster                                                     |
| mdp                        | 2.79 sec                                                   | 2.74 sec: 1.02x faster                                                    |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.01x faster                                                      |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.82 sec: 1.01x faster                                                    |
| sqlglot_transpile          | 1.63 ms                                                    | 1.62 ms: 1.01x faster                                                     |
| regex_dna                  | 221 ms                                                     | 219 ms: 1.01x faster                                                      |
| dulwich_log                | 67.2 ms                                                    | 66.7 ms: 1.01x faster                                                     |
| coverage                   | 93.1 ms                                                    | 92.4 ms: 1.01x faster                                                     |
| scimark_sor                | 127 ms                                                     | 127 ms: 1.01x faster                                                      |
| pickle_pure_python         | 305 us                                                     | 304 us: 1.01x faster                                                      |
| 2to3                       | 274 ms                                                     | 273 ms: 1.00x faster                                                      |
| python_startup_no_site     | 7.11 ms                                                    | 7.13 ms: 1.00x slower                                                     |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                     |
| raytrace                   | 267 ms                                                     | 269 ms: 1.01x slower                                                      |
| asyncio_tcp                | 508 ms                                                     | 518 ms: 1.02x slower                                                      |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.02x slower                                                      |
| bench_thread_pool          | 834 us                                                     | 857 us: 1.03x slower                                                      |
| sqlglot_optimize           | 55.5 ms                                                    | 57.3 ms: 1.03x slower                                                     |
| sympy_expand               | 473 ms                                                     | 489 ms: 1.03x slower                                                      |
| hexiom                     | 6.30 ms                                                    | 6.52 ms: 1.03x slower                                                     |
| typing_runtime_protocols   | 165 us                                                     | 171 us: 1.04x slower                                                      |
| tornado_http               | 94.6 ms                                                    | 98.3 ms: 1.04x slower                                                     |
| dask                       | 369 ms                                                     | 384 ms: 1.04x slower                                                      |
| deltablue                  | 3.25 ms                                                    | 3.42 ms: 1.05x slower                                                     |
| docutils                   | 2.83 sec                                                   | 2.98 sec: 1.05x slower                                                    |
| sympy_str                  | 282 ms                                                     | 300 ms: 1.06x slower                                                      |
| html5lib                   | 67.2 ms                                                    | 71.6 ms: 1.07x slower                                                     |
| sympy_sum                  | 156 ms                                                     | 168 ms: 1.08x slower                                                      |
| pylint                     | 317 ms                                                     | 368 ms: 1.16x slower                                                      |
| django_template            | 34.8 ms                                                    | 40.4 ms: 1.16x slower                                                     |
| async_generators           | 442 ms                                                     | 514 ms: 1.16x slower                                                      |
| genshi_text                | 23.7 ms                                                    | 27.7 ms: 1.17x slower                                                     |
| coroutines                 | 23.2 ms                                                    | 27.6 ms: 1.19x slower                                                     |
| nqueens                    | 81.4 ms                                                    | 97.5 ms: 1.20x slower                                                     |
| genshi_xml                 | 51.6 ms                                                    | 63.3 ms: 1.23x slower                                                     |
| sympy_integrate            | 20.5 ms                                                    | 25.3 ms: 1.23x slower                                                     |
| generators                 | 29.6 ms                                                    | 56.1 ms: 1.89x slower                                                     |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                              |

Benchmark hidden because not significant (1): comprehensions
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.67% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x
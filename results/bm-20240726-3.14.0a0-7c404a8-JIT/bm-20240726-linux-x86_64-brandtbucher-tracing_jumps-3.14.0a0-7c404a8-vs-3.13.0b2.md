# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: tracing_jumps
- machine: linux-x86_64
- commit hash: 7c404a8
- commit date: 2024-07-26
- overall geometric mean: 1.04x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 275 ms: 1.00x slower                                                 |
| docutils       | 2.83 sec                                                   | 2.90 sec: 1.02x slower                                               |
| html5lib       | 67.2 ms                                                    | 65.2 ms: 1.03x faster                                                |
| tornado_http   | 94.6 ms                                                    | 92.5 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                      | 1.01x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 394 ms: 1.18x faster                                                 |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 390 ms: 1.14x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 532 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 564 ms: 1.08x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 871 ms: 1.07x faster                                                 |
| async_tree_io              | 939 ms                                                     | 902 ms: 1.04x faster                                                 |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.3 ms: 1.12x faster                                                |
| nbody          | 88.3 ms                                                    | 80.2 ms: 1.10x faster                                                |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                      | 1.08x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 134 ms: 1.02x faster                                                 |
| regex_dna      | 221 ms                                                     | 221 ms: 1.00x faster                                                 |
| regex_v8       | 25.1 ms                                                    | 25.9 ms: 1.03x slower                                                |
| regex_effbot   | 3.67 ms                                                    | 3.79 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                      | 1.01x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.10x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 56.1 ms: 1.09x faster                                                |
| xml_etree_generate   | 87.4 ms                                                    | 80.6 ms: 1.08x faster                                                |
| xml_etree_iterparse  | 107 ms                                                     | 99.1 ms: 1.08x faster                                                |
| tomli_loads          | 2.12 sec                                                   | 1.97 sec: 1.07x faster                                               |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                |
| pickle_pure_python   | 305 us                                                     | 298 us: 1.03x faster                                                 |
| json_loads           | 28.9 us                                                    | 28.3 us: 1.02x faster                                                |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                |
| python_startup_no_site | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.65 ms: 1.16x faster                                                |
| genshi_text     | 23.7 ms                                                    | 24.2 ms: 1.02x slower                                                |
| genshi_xml      | 51.6 ms                                                    | 53.1 ms: 1.03x slower                                                |
| django_template | 34.8 ms                                                    | 36.0 ms: 1.04x slower                                                |
| Geometric mean  | (ref)                                                      | 1.02x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.5 us: 1.39x faster                                                |
| deepcopy                   | 367 us                                                     | 269 us: 1.36x faster                                                 |
| scimark_fft                | 392 ms                                                     | 309 ms: 1.27x faster                                                 |
| richards                   | 50.9 ms                                                    | 41.4 ms: 1.23x faster                                                |
| richards_super             | 57.4 ms                                                    | 47.1 ms: 1.22x faster                                                |
| deepcopy_reduce            | 3.35 us                                                    | 2.77 us: 1.21x faster                                                |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.45 ms: 1.18x faster                                                |
| async_tree_memoization     | 463 ms                                                     | 394 ms: 1.18x faster                                                 |
| mako                       | 11.2 ms                                                    | 9.65 ms: 1.16x faster                                                |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                 |
| crypto_pyaes               | 77.5 ms                                                    | 67.5 ms: 1.15x faster                                                |
| async_tree_memoization_tg  | 444 ms                                                     | 390 ms: 1.14x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.9 ms: 1.14x faster                                                |
| spectral_norm              | 116 ms                                                     | 103 ms: 1.13x faster                                                 |
| float                      | 78.9 ms                                                    | 70.3 ms: 1.12x faster                                                |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                 |
| pyflate                    | 484 ms                                                     | 435 ms: 1.11x faster                                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.51 sec: 1.11x faster                                               |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 532 ms: 1.10x faster                                                 |
| nbody                      | 88.3 ms                                                    | 80.2 ms: 1.10x faster                                                |
| fannkuch                   | 402 ms                                                     | 366 ms: 1.10x faster                                                 |
| xml_etree_process          | 61.2 ms                                                    | 56.1 ms: 1.09x faster                                                |
| xml_etree_generate         | 87.4 ms                                                    | 80.6 ms: 1.08x faster                                                |
| xml_etree_iterparse        | 107 ms                                                     | 99.1 ms: 1.08x faster                                                |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 564 ms: 1.08x faster                                                 |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.07x faster                                                |
| async_tree_io_tg           | 936 ms                                                     | 871 ms: 1.07x faster                                                 |
| tomli_loads                | 2.12 sec                                                   | 1.97 sec: 1.07x faster                                               |
| pprint_safe_repr           | 758 ms                                                     | 707 ms: 1.07x faster                                                 |
| pprint_pformat             | 1.56 sec                                                   | 1.46 sec: 1.06x faster                                               |
| logging_format             | 6.47 us                                                    | 6.09 us: 1.06x faster                                                |
| chaos                      | 61.3 ms                                                    | 57.7 ms: 1.06x faster                                                |
| telco                      | 8.41 ms                                                    | 7.96 ms: 1.06x faster                                                |
| meteor_contest             | 110 ms                                                     | 104 ms: 1.06x faster                                                 |
| gc_traversal               | 3.98 ms                                                    | 3.77 ms: 1.05x faster                                                |
| thrift                     | 823 us                                                     | 789 us: 1.04x faster                                                 |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                |
| async_tree_io              | 939 ms                                                     | 902 ms: 1.04x faster                                                 |
| logging_simple             | 5.74 us                                                    | 5.53 us: 1.04x faster                                                |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                 |
| html5lib                   | 67.2 ms                                                    | 65.2 ms: 1.03x faster                                                |
| json                       | 5.31 ms                                                    | 5.16 ms: 1.03x faster                                                |
| pickle_pure_python         | 305 us                                                     | 298 us: 1.03x faster                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.03x faster                                                |
| mdp                        | 2.79 sec                                                   | 2.72 sec: 1.02x faster                                               |
| coroutines                 | 23.2 ms                                                    | 22.6 ms: 1.02x faster                                                |
| tornado_http               | 94.6 ms                                                    | 92.5 ms: 1.02x faster                                                |
| comprehensions             | 16.6 us                                                    | 16.2 us: 1.02x faster                                                |
| bench_thread_pool          | 834 us                                                     | 816 us: 1.02x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                 |
| json_loads                 | 28.9 us                                                    | 28.3 us: 1.02x faster                                                |
| asyncio_tcp                | 508 ms                                                     | 498 ms: 1.02x faster                                                 |
| regex_compile              | 137 ms                                                     | 134 ms: 1.02x faster                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                               |
| dask                       | 369 ms                                                     | 364 ms: 1.02x faster                                                 |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 1.62 ms: 1.01x faster                                                |
| regex_dna                  | 221 ms                                                     | 221 ms: 1.00x faster                                                 |
| 2to3                       | 274 ms                                                     | 275 ms: 1.00x slower                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                |
| scimark_sor                | 127 ms                                                     | 129 ms: 1.01x slower                                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                |
| raytrace                   | 267 ms                                                     | 270 ms: 1.01x slower                                                 |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                                 |
| genshi_text                | 23.7 ms                                                    | 24.2 ms: 1.02x slower                                                |
| scimark_lu                 | 122 ms                                                     | 124 ms: 1.02x slower                                                 |
| go                         | 145 ms                                                     | 148 ms: 1.02x slower                                                 |
| docutils                   | 2.83 sec                                                   | 2.90 sec: 1.02x slower                                               |
| genshi_xml                 | 51.6 ms                                                    | 53.1 ms: 1.03x slower                                                |
| async_generators           | 442 ms                                                     | 455 ms: 1.03x slower                                                 |
| regex_v8                   | 25.1 ms                                                    | 25.9 ms: 1.03x slower                                                |
| regex_effbot               | 3.67 ms                                                    | 3.79 ms: 1.03x slower                                                |
| dulwich_log                | 67.2 ms                                                    | 69.4 ms: 1.03x slower                                                |
| django_template            | 34.8 ms                                                    | 36.0 ms: 1.04x slower                                                |
| nqueens                    | 81.4 ms                                                    | 84.4 ms: 1.04x slower                                                |
| typing_runtime_protocols   | 165 us                                                     | 173 us: 1.05x slower                                                 |
| sympy_str                  | 282 ms                                                     | 296 ms: 1.05x slower                                                 |
| hexiom                     | 6.30 ms                                                    | 6.63 ms: 1.05x slower                                                |
| sympy_expand               | 473 ms                                                     | 505 ms: 1.07x slower                                                 |
| sympy_sum                  | 156 ms                                                     | 168 ms: 1.08x slower                                                 |
| sympy_integrate            | 20.5 ms                                                    | 22.3 ms: 1.09x slower                                                |
| deltablue                  | 3.25 ms                                                    | 3.57 ms: 1.10x slower                                                |
| generators                 | 29.6 ms                                                    | 33.1 ms: 1.12x slower                                                |
| pylint                     | 317 ms                                                     | 355 ms: 1.12x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                         |

Benchmark hidden because not significant (4): coverage, sqlglot_optimize, pycparser, logging_silent
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x
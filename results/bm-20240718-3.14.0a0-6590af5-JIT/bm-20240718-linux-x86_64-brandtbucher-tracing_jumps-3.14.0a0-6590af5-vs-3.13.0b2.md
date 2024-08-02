# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: tracing_jumps
- machine: linux-x86_64
- commit hash: 6590af5
- commit date: 2024-07-18
- overall geometric mean: 1.05x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 275 ms: 1.00x slower                                                 |
| docutils       | 2.83 sec                                                   | 2.88 sec: 1.02x slower                                               |
| html5lib       | 67.2 ms                                                    | 65.9 ms: 1.02x faster                                                |
| tornado_http   | 94.6 ms                                                    | 92.5 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                      | 1.01x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 377 ms: 1.18x faster                                                 |
| async_tree_none            | 378 ms                                                     | 330 ms: 1.15x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 413 ms: 1.12x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 844 ms: 1.11x faster                                                 |
| async_tree_io              | 939 ms                                                     | 861 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 539 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                                 |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.8 ms: 1.10x faster                                                |
| nbody          | 88.3 ms                                                    | 82.4 ms: 1.07x faster                                                |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                      | 1.07x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 132 ms: 1.03x faster                                                 |
| regex_v8       | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                                |
| regex_dna      | 221 ms                                                     | 228 ms: 1.03x slower                                                 |
| regex_effbot   | 3.67 ms                                                    | 3.87 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                      | 1.02x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                               |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 79.9 ms: 1.09x faster                                                |
| xml_etree_iterparse  | 107 ms                                                     | 98.9 ms: 1.09x faster                                                |
| xml_etree_process    | 61.2 ms                                                    | 56.8 ms: 1.08x faster                                                |
| json_loads           | 28.9 us                                                    | 27.4 us: 1.05x faster                                                |
| pickle_pure_python   | 305 us                                                     | 295 us: 1.03x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.02x faster                                                 |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                |
| python_startup_no_site | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.65 ms: 1.16x faster                                                |
| genshi_text     | 23.7 ms                                                    | 24.0 ms: 1.01x slower                                                |
| django_template | 34.8 ms                                                    | 36.0 ms: 1.03x slower                                                |
| genshi_xml      | 51.6 ms                                                    | 53.5 ms: 1.04x slower                                                |
| Geometric mean  | (ref)                                                      | 1.02x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 29.2 us: 1.36x faster                                                |
| deepcopy                   | 367 us                                                     | 276 us: 1.33x faster                                                 |
| richards                   | 50.9 ms                                                    | 40.8 ms: 1.25x faster                                                |
| scimark_fft                | 392 ms                                                     | 316 ms: 1.24x faster                                                 |
| richards_super             | 57.4 ms                                                    | 46.5 ms: 1.23x faster                                                |
| deepcopy_reduce            | 3.35 us                                                    | 2.74 us: 1.22x faster                                                |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.35 ms: 1.21x faster                                                |
| async_tree_memoization_tg  | 444 ms                                                     | 377 ms: 1.18x faster                                                 |
| mako                       | 11.2 ms                                                    | 9.65 ms: 1.16x faster                                                |
| crypto_pyaes               | 77.5 ms                                                    | 66.7 ms: 1.16x faster                                                |
| pyflate                    | 484 ms                                                     | 421 ms: 1.15x faster                                                 |
| async_tree_none            | 378 ms                                                     | 330 ms: 1.15x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.4 ms: 1.15x faster                                                |
| spectral_norm              | 116 ms                                                     | 102 ms: 1.13x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                 |
| fannkuch                   | 402 ms                                                     | 358 ms: 1.12x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 413 ms: 1.12x faster                                                 |
| tomli_loads                | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                               |
| async_tree_io_tg           | 936 ms                                                     | 844 ms: 1.11x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.57 sec: 1.10x faster                                               |
| float                      | 78.9 ms                                                    | 71.8 ms: 1.10x faster                                                |
| xml_etree_generate         | 87.4 ms                                                    | 79.9 ms: 1.09x faster                                                |
| async_tree_io              | 939 ms                                                     | 861 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 539 ms: 1.09x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 98.9 ms: 1.09x faster                                                |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                                |
| xml_etree_process          | 61.2 ms                                                    | 56.8 ms: 1.08x faster                                                |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                                 |
| logging_format             | 6.47 us                                                    | 6.03 us: 1.07x faster                                                |
| gc_traversal               | 3.98 ms                                                    | 3.71 ms: 1.07x faster                                                |
| nbody                      | 88.3 ms                                                    | 82.4 ms: 1.07x faster                                                |
| mdp                        | 2.79 sec                                                   | 2.61 sec: 1.07x faster                                               |
| chaos                      | 61.3 ms                                                    | 58.0 ms: 1.06x faster                                                |
| meteor_contest             | 110 ms                                                     | 104 ms: 1.06x faster                                                 |
| json_loads                 | 28.9 us                                                    | 27.4 us: 1.05x faster                                                |
| logging_simple             | 5.74 us                                                    | 5.48 us: 1.05x faster                                                |
| pprint_safe_repr           | 758 ms                                                     | 724 ms: 1.05x faster                                                 |
| pprint_pformat             | 1.56 sec                                                   | 1.49 sec: 1.04x faster                                               |
| telco                      | 8.41 ms                                                    | 8.08 ms: 1.04x faster                                                |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                |
| regex_compile              | 137 ms                                                     | 132 ms: 1.03x faster                                                 |
| pickle_pure_python         | 305 us                                                     | 295 us: 1.03x faster                                                 |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                 |
| thrift                     | 823 us                                                     | 803 us: 1.02x faster                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                                |
| coroutines                 | 23.2 ms                                                    | 22.6 ms: 1.02x faster                                                |
| coverage                   | 93.1 ms                                                    | 90.9 ms: 1.02x faster                                                |
| tornado_http               | 94.6 ms                                                    | 92.5 ms: 1.02x faster                                                |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                               |
| asyncio_tcp                | 508 ms                                                     | 498 ms: 1.02x faster                                                 |
| html5lib                   | 67.2 ms                                                    | 65.9 ms: 1.02x faster                                                |
| dask                       | 369 ms                                                     | 363 ms: 1.02x faster                                                 |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.02x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                 |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                |
| comprehensions             | 16.6 us                                                    | 16.4 us: 1.02x faster                                                |
| json                       | 5.31 ms                                                    | 5.23 ms: 1.01x faster                                                |
| bench_thread_pool          | 834 us                                                     | 826 us: 1.01x faster                                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 1.62 ms: 1.01x faster                                                |
| sqlglot_optimize           | 55.5 ms                                                    | 55.3 ms: 1.00x faster                                                |
| 2to3                       | 274 ms                                                     | 275 ms: 1.00x slower                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                |
| raytrace                   | 267 ms                                                     | 269 ms: 1.01x slower                                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                |
| scimark_sor                | 127 ms                                                     | 129 ms: 1.01x slower                                                 |
| dulwich_log                | 67.2 ms                                                    | 67.8 ms: 1.01x slower                                                |
| regex_v8                   | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                                |
| genshi_text                | 23.7 ms                                                    | 24.0 ms: 1.01x slower                                                |
| logging_silent             | 105 ns                                                     | 106 ns: 1.02x slower                                                 |
| docutils                   | 2.83 sec                                                   | 2.88 sec: 1.02x slower                                               |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                                 |
| async_generators           | 442 ms                                                     | 451 ms: 1.02x slower                                                 |
| scimark_lu                 | 122 ms                                                     | 125 ms: 1.03x slower                                                 |
| nqueens                    | 81.4 ms                                                    | 83.8 ms: 1.03x slower                                                |
| regex_dna                  | 221 ms                                                     | 228 ms: 1.03x slower                                                 |
| django_template            | 34.8 ms                                                    | 36.0 ms: 1.03x slower                                                |
| genshi_xml                 | 51.6 ms                                                    | 53.5 ms: 1.04x slower                                                |
| typing_runtime_protocols   | 165 us                                                     | 171 us: 1.04x slower                                                 |
| sympy_str                  | 282 ms                                                     | 297 ms: 1.05x slower                                                 |
| regex_effbot               | 3.67 ms                                                    | 3.87 ms: 1.05x slower                                                |
| hexiom                     | 6.30 ms                                                    | 6.67 ms: 1.06x slower                                                |
| sympy_expand               | 473 ms                                                     | 501 ms: 1.06x slower                                                 |
| pylint                     | 317 ms                                                     | 339 ms: 1.07x slower                                                 |
| sympy_sum                  | 156 ms                                                     | 169 ms: 1.09x slower                                                 |
| sympy_integrate            | 20.5 ms                                                    | 22.4 ms: 1.09x slower                                                |
| deltablue                  | 3.25 ms                                                    | 3.57 ms: 1.10x slower                                                |
| generators                 | 29.6 ms                                                    | 33.0 ms: 1.11x slower                                                |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                         |

Benchmark hidden because not significant (2): go, pycparser
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x
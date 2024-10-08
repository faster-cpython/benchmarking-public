# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_progress_needed_8
- machine: linux-x86_64
- commit hash: 95535e9
- commit date: 2024-07-13
- overall geometric mean: 1.05x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 277 ms: 1.01x slower                                                        |
| docutils       | 2.83 sec                                                   | 3.02 sec: 1.07x slower                                                      |
| html5lib       | 67.2 ms                                                    | 64.9 ms: 1.04x faster                                                       |
| tornado_http   | 94.6 ms                                                    | 93.6 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 382 ms: 1.16x faster                                                        |
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 410 ms: 1.13x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 834 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                        |
| async_tree_io              | 939 ms                                                     | 858 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 544 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                                        |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.0 ms: 1.13x faster                                                       |
| nbody          | 88.3 ms                                                    | 79.7 ms: 1.11x faster                                                       |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                      | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 138 ms: 1.01x slower                                                        |
| regex_v8       | 25.1 ms                                                    | 25.7 ms: 1.02x slower                                                       |
| regex_dna      | 221 ms                                                     | 227 ms: 1.03x slower                                                        |
| regex_effbot   | 3.67 ms                                                    | 3.88 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                      | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.89 sec: 1.12x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                     | 98.7 ms: 1.09x faster                                                       |
| xml_etree_parse      | 162 ms                                                     | 149 ms: 1.09x faster                                                        |
| xml_etree_generate   | 87.4 ms                                                    | 81.4 ms: 1.07x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 57.8 ms: 1.06x faster                                                       |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                       |
| json_loads           | 28.9 us                                                    | 27.9 us: 1.04x faster                                                       |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.02x faster                                                        |
| pickle_pure_python   | 305 us                                                     | 303 us: 1.01x faster                                                        |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako           | 11.2 ms                                                    | 9.85 ms: 1.14x faster                                                       |
| genshi_text    | 23.7 ms                                                    | 25.0 ms: 1.06x slower                                                       |
| genshi_xml     | 51.6 ms                                                    | 56.6 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                      | 1.00x slower                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.3 us: 1.46x faster                                                       |
| richards                   | 50.9 ms                                                    | 36.3 ms: 1.40x faster                                                       |
| richards_super             | 57.4 ms                                                    | 41.1 ms: 1.40x faster                                                       |
| deepcopy                   | 367 us                                                     | 264 us: 1.39x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                    | 2.66 us: 1.26x faster                                                       |
| scimark_fft                | 392 ms                                                     | 316 ms: 1.24x faster                                                        |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.33 ms: 1.22x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 382 ms: 1.16x faster                                                        |
| crypto_pyaes               | 77.5 ms                                                    | 66.9 ms: 1.16x faster                                                       |
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                        |
| mako                       | 11.2 ms                                                    | 9.85 ms: 1.14x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 410 ms: 1.13x faster                                                        |
| spectral_norm              | 116 ms                                                     | 103 ms: 1.13x faster                                                        |
| float                      | 78.9 ms                                                    | 70.0 ms: 1.13x faster                                                       |
| async_tree_io_tg           | 936 ms                                                     | 834 ms: 1.12x faster                                                        |
| tomli_loads                | 2.12 sec                                                   | 1.89 sec: 1.12x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                        |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.0 ms: 1.12x faster                                                       |
| fannkuch                   | 402 ms                                                     | 361 ms: 1.11x faster                                                        |
| gc_traversal               | 3.98 ms                                                    | 3.58 ms: 1.11x faster                                                       |
| nbody                      | 88.3 ms                                                    | 79.7 ms: 1.11x faster                                                       |
| async_tree_io              | 939 ms                                                     | 858 ms: 1.09x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                     | 98.7 ms: 1.09x faster                                                       |
| xml_etree_parse            | 162 ms                                                     | 149 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 544 ms: 1.08x faster                                                        |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                       |
| pyflate                    | 484 ms                                                     | 449 ms: 1.08x faster                                                        |
| chaos                      | 61.3 ms                                                    | 57.1 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                                        |
| xml_etree_generate         | 87.4 ms                                                    | 81.4 ms: 1.07x faster                                                       |
| logging_format             | 6.47 us                                                    | 6.06 us: 1.07x faster                                                       |
| bpe_tokeniser              | 5.02 sec                                                   | 4.73 sec: 1.06x faster                                                      |
| xml_etree_process          | 61.2 ms                                                    | 57.8 ms: 1.06x faster                                                       |
| telco                      | 8.41 ms                                                    | 8.01 ms: 1.05x faster                                                       |
| logging_simple             | 5.74 us                                                    | 5.47 us: 1.05x faster                                                       |
| scimark_lu                 | 122 ms                                                     | 117 ms: 1.04x faster                                                        |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                       |
| json_loads                 | 28.9 us                                                    | 27.9 us: 1.04x faster                                                       |
| html5lib                   | 67.2 ms                                                    | 64.9 ms: 1.04x faster                                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                       |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                                        |
| logging_silent             | 105 ns                                                     | 101 ns: 1.03x faster                                                        |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                                      |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                        |
| dask                       | 369 ms                                                     | 361 ms: 1.02x faster                                                        |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                      |
| mdp                        | 2.79 sec                                                   | 2.72 sec: 1.02x faster                                                      |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                       |
| pprint_safe_repr           | 758 ms                                                     | 742 ms: 1.02x faster                                                        |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.02x faster                                                        |
| json                       | 5.31 ms                                                    | 5.20 ms: 1.02x faster                                                       |
| thrift                     | 823 us                                                     | 807 us: 1.02x faster                                                        |
| asyncio_tcp                | 508 ms                                                     | 499 ms: 1.02x faster                                                        |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                        |
| tornado_http               | 94.6 ms                                                    | 93.6 ms: 1.01x faster                                                       |
| scimark_sor                | 127 ms                                                     | 126 ms: 1.01x faster                                                        |
| coverage                   | 93.1 ms                                                    | 92.2 ms: 1.01x faster                                                       |
| bench_thread_pool          | 834 us                                                     | 826 us: 1.01x faster                                                        |
| dulwich_log                | 67.2 ms                                                    | 66.6 ms: 1.01x faster                                                       |
| pickle_pure_python         | 305 us                                                     | 303 us: 1.01x faster                                                        |
| raytrace                   | 267 ms                                                     | 268 ms: 1.00x slower                                                        |
| regex_compile              | 137 ms                                                     | 138 ms: 1.01x slower                                                        |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                       |
| typing_runtime_protocols   | 165 us                                                     | 167 us: 1.01x slower                                                        |
| sqlglot_normalize          | 110 ms                                                     | 111 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.63 ms                                                    | 1.65 ms: 1.01x slower                                                       |
| 2to3                       | 274 ms                                                     | 277 ms: 1.01x slower                                                        |
| coroutines                 | 23.2 ms                                                    | 23.5 ms: 1.02x slower                                                       |
| async_generators           | 442 ms                                                     | 449 ms: 1.02x slower                                                        |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                                      |
| regex_v8                   | 25.1 ms                                                    | 25.7 ms: 1.02x slower                                                       |
| regex_dna                  | 221 ms                                                     | 227 ms: 1.03x slower                                                        |
| sympy_str                  | 282 ms                                                     | 290 ms: 1.03x slower                                                        |
| sqlglot_optimize           | 55.5 ms                                                    | 57.4 ms: 1.03x slower                                                       |
| generators                 | 29.6 ms                                                    | 30.8 ms: 1.04x slower                                                       |
| sympy_expand               | 473 ms                                                     | 493 ms: 1.04x slower                                                        |
| hexiom                     | 6.30 ms                                                    | 6.58 ms: 1.05x slower                                                       |
| deltablue                  | 3.25 ms                                                    | 3.43 ms: 1.06x slower                                                       |
| regex_effbot               | 3.67 ms                                                    | 3.88 ms: 1.06x slower                                                       |
| genshi_text                | 23.7 ms                                                    | 25.0 ms: 1.06x slower                                                       |
| nqueens                    | 81.4 ms                                                    | 86.6 ms: 1.06x slower                                                       |
| docutils                   | 2.83 sec                                                   | 3.02 sec: 1.07x slower                                                      |
| sympy_integrate            | 20.5 ms                                                    | 21.9 ms: 1.07x slower                                                       |
| sympy_sum                  | 156 ms                                                     | 168 ms: 1.08x slower                                                        |
| genshi_xml                 | 51.6 ms                                                    | 56.6 ms: 1.10x slower                                                       |
| pylint                     | 317 ms                                                     | 373 ms: 1.18x slower                                                        |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                |

Benchmark hidden because not significant (4): go, python_startup_no_site, django_template, comprehensions
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x
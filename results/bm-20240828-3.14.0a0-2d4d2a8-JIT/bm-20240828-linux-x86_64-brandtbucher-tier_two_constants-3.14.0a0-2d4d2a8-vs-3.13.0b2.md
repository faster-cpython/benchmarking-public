# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: 2d4d2a8
- commit date: 2024-08-28
- overall geometric mean: 1.05x faster
- HPT reliability: 99.82%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 277 ms: 1.01x slower                                                      |
| docutils       | 2.83 sec                                                   | 3.04 sec: 1.08x slower                                                    |
| html5lib       | 67.2 ms                                                    | 64.2 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                      | 1.01x slower                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 417 ms: 1.11x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 404 ms: 1.10x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 537 ms: 1.09x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 560 ms: 1.09x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.08x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 902 ms: 1.04x faster                                                      |
| Geometric mean             | (ref)                                                      | 1.08x faster                                                              |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.8 ms: 1.11x faster                                                     |
| nbody          | 88.3 ms                                                    | 79.6 ms: 1.11x faster                                                     |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                      | 1.08x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 213 ms: 1.04x faster                                                      |
| regex_v8       | 25.1 ms                                                    | 24.3 ms: 1.03x faster                                                     |
| regex_effbot   | 3.67 ms                                                    | 3.56 ms: 1.03x faster                                                     |
| regex_compile  | 137 ms                                                     | 141 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                      | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.6 ms: 1.13x faster                                                     |
| xml_etree_process    | 61.2 ms                                                    | 54.5 ms: 1.12x faster                                                     |
| tomli_loads          | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                    |
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                     | 98.6 ms: 1.09x faster                                                     |
| json_dumps           | 10.7 ms                                                    | 9.96 ms: 1.08x faster                                                     |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                      |
| pickle_pure_python   | 305 us                                                     | 302 us: 1.01x faster                                                      |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                              |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                     |
| python_startup_no_site | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.67 ms: 1.16x faster                                                     |
| genshi_text     | 23.7 ms                                                    | 24.1 ms: 1.02x slower                                                     |
| django_template | 34.8 ms                                                    | 36.7 ms: 1.05x slower                                                     |
| genshi_xml      | 51.6 ms                                                    | 56.7 ms: 1.10x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.00x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.9 us: 1.48x faster                                                     |
| deepcopy                   | 367 us                                                     | 261 us: 1.41x faster                                                      |
| richards                   | 50.9 ms                                                    | 39.3 ms: 1.30x faster                                                     |
| scimark_fft                | 392 ms                                                     | 307 ms: 1.28x faster                                                      |
| richards_super             | 57.4 ms                                                    | 45.0 ms: 1.27x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                    | 2.63 us: 1.27x faster                                                     |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.30 ms: 1.23x faster                                                     |
| crypto_pyaes               | 77.5 ms                                                    | 65.6 ms: 1.18x faster                                                     |
| spectral_norm              | 116 ms                                                     | 98.5 ms: 1.18x faster                                                     |
| mako                       | 11.2 ms                                                    | 9.67 ms: 1.16x faster                                                     |
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                      |
| bpe_tokeniser              | 5.02 sec                                                   | 4.40 sec: 1.14x faster                                                    |
| xml_etree_generate         | 87.4 ms                                                    | 77.6 ms: 1.13x faster                                                     |
| xml_etree_process          | 61.2 ms                                                    | 54.5 ms: 1.12x faster                                                     |
| float                      | 78.9 ms                                                    | 70.8 ms: 1.11x faster                                                     |
| pyflate                    | 484 ms                                                     | 435 ms: 1.11x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 417 ms: 1.11x faster                                                      |
| nbody                      | 88.3 ms                                                    | 79.6 ms: 1.11x faster                                                     |
| telco                      | 8.41 ms                                                    | 7.62 ms: 1.10x faster                                                     |
| tomli_loads                | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                    |
| scimark_lu                 | 122 ms                                                     | 110 ms: 1.10x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 404 ms: 1.10x faster                                                      |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.10x faster                                                      |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.10x faster                                                     |
| scimark_monte_carlo        | 69.2 ms                                                    | 63.2 ms: 1.09x faster                                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 537 ms: 1.09x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 560 ms: 1.09x faster                                                      |
| mdp                        | 2.79 sec                                                   | 2.56 sec: 1.09x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                     | 98.6 ms: 1.09x faster                                                     |
| fannkuch                   | 402 ms                                                     | 370 ms: 1.09x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.08x faster                                                      |
| gc_traversal               | 3.98 ms                                                    | 3.67 ms: 1.08x faster                                                     |
| scimark_sor                | 127 ms                                                     | 118 ms: 1.08x faster                                                      |
| json_dumps                 | 10.7 ms                                                    | 9.96 ms: 1.08x faster                                                     |
| coverage                   | 93.1 ms                                                    | 87.1 ms: 1.07x faster                                                     |
| chaos                      | 61.3 ms                                                    | 58.5 ms: 1.05x faster                                                     |
| html5lib                   | 67.2 ms                                                    | 64.2 ms: 1.05x faster                                                     |
| logging_format             | 6.47 us                                                    | 6.21 us: 1.04x faster                                                     |
| pprint_safe_repr           | 758 ms                                                     | 730 ms: 1.04x faster                                                      |
| regex_dna                  | 221 ms                                                     | 213 ms: 1.04x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 902 ms: 1.04x faster                                                      |
| regex_v8                   | 25.1 ms                                                    | 24.3 ms: 1.03x faster                                                     |
| asyncio_tcp                | 508 ms                                                     | 492 ms: 1.03x faster                                                      |
| regex_effbot               | 3.67 ms                                                    | 3.56 ms: 1.03x faster                                                     |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                      |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                      |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                                    |
| thrift                     | 823 us                                                     | 803 us: 1.02x faster                                                      |
| logging_simple             | 5.74 us                                                    | 5.61 us: 1.02x faster                                                     |
| bench_thread_pool          | 834 us                                                     | 816 us: 1.02x faster                                                      |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                      |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                    |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                     |
| create_gc_cycles           | 1.82 ms                                                    | 1.79 ms: 1.01x faster                                                     |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                                      |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                                      |
| deltablue                  | 3.25 ms                                                    | 3.22 ms: 1.01x faster                                                     |
| logging_silent             | 105 ns                                                     | 104 ns: 1.01x faster                                                      |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                     |
| python_startup_no_site     | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                     |
| 2to3                       | 274 ms                                                     | 277 ms: 1.01x slower                                                      |
| json                       | 5.31 ms                                                    | 5.38 ms: 1.01x slower                                                     |
| coroutines                 | 23.2 ms                                                    | 23.6 ms: 1.02x slower                                                     |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                                      |
| genshi_text                | 23.7 ms                                                    | 24.1 ms: 1.02x slower                                                     |
| sqlglot_parse              | 1.32 ms                                                    | 1.35 ms: 1.02x slower                                                     |
| regex_compile              | 137 ms                                                     | 141 ms: 1.03x slower                                                      |
| sqlglot_transpile          | 1.63 ms                                                    | 1.69 ms: 1.03x slower                                                     |
| nqueens                    | 81.4 ms                                                    | 84.3 ms: 1.04x slower                                                     |
| async_generators           | 442 ms                                                     | 459 ms: 1.04x slower                                                      |
| pycparser                  | 1.16 sec                                                   | 1.20 sec: 1.04x slower                                                    |
| raytrace                   | 267 ms                                                     | 277 ms: 1.04x slower                                                      |
| sqlglot_optimize           | 55.5 ms                                                    | 58.1 ms: 1.05x slower                                                     |
| django_template            | 34.8 ms                                                    | 36.7 ms: 1.05x slower                                                     |
| sympy_str                  | 282 ms                                                     | 299 ms: 1.06x slower                                                      |
| sympy_expand               | 473 ms                                                     | 504 ms: 1.07x slower                                                      |
| docutils                   | 2.83 sec                                                   | 3.04 sec: 1.08x slower                                                    |
| hexiom                     | 6.30 ms                                                    | 6.86 ms: 1.09x slower                                                     |
| genshi_xml                 | 51.6 ms                                                    | 56.7 ms: 1.10x slower                                                     |
| sympy_sum                  | 156 ms                                                     | 171 ms: 1.10x slower                                                      |
| generators                 | 29.6 ms                                                    | 32.6 ms: 1.10x slower                                                     |
| sympy_integrate            | 20.5 ms                                                    | 22.8 ms: 1.11x slower                                                     |
| pylint                     | 317 ms                                                     | 372 ms: 1.17x slower                                                      |
| go                         | 145 ms                                                     | 170 ms: 1.18x slower                                                      |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                              |

Benchmark hidden because not significant (5): typing_runtime_protocols, json_loads, tornado_http, comprehensions, async_tree_io
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.82% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x
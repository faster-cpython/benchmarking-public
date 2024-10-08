# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: tier_two_immortals
- machine: linux-x86_64
- commit hash: 8ef2e8f
- commit date: 2024-10-03
- overall geometric mean: 1.03x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 279 ms: 1.02x slower                                                      |
| docutils       | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                    |
| html5lib       | 67.2 ms                                                    | 64.7 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                      | 1.00x slower                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 317 ms: 1.20x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 387 ms: 1.15x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 408 ms: 1.14x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.10x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 872 ms: 1.07x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 547 ms: 1.07x faster                                                      |
| async_tree_io              | 939 ms                                                     | 885 ms: 1.06x faster                                                      |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.8 ms: 1.10x faster                                                     |
| nbody          | 88.3 ms                                                    | 82.3 ms: 1.07x faster                                                     |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                      | 1.07x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.69 ms: 1.01x slower                                                     |
| regex_v8       | 25.1 ms                                                    | 25.5 ms: 1.02x slower                                                     |
| regex_compile  | 137 ms                                                     | 143 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                      | 1.02x slower                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 76.8 ms: 1.14x faster                                                     |
| xml_etree_process    | 61.2 ms                                                    | 54.4 ms: 1.12x faster                                                     |
| xml_etree_parse      | 162 ms                                                     | 145 ms: 1.12x faster                                                      |
| tomli_loads          | 2.12 sec                                                   | 1.90 sec: 1.11x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                     | 98.1 ms: 1.09x faster                                                     |
| json_loads           | 28.9 us                                                    | 26.9 us: 1.07x faster                                                     |
| json_dumps           | 10.7 ms                                                    | 10.2 ms: 1.06x faster                                                     |
| pickle_list          | 5.11 us                                                    | 4.91 us: 1.04x faster                                                     |
| unpickle_list        | 5.34 us                                                    | 5.16 us: 1.04x faster                                                     |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.03x faster                                                      |
| pickle_dict          | 34.8 us                                                    | 34.4 us: 1.01x faster                                                     |
| pickle               | 11.5 us                                                    | 11.4 us: 1.01x faster                                                     |
| pickle_pure_python   | 305 us                                                     | 309 us: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                              |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                     |
| python_startup_no_site | 7.11 ms                                                    | 7.03 ms: 1.01x faster                                                     |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.90 ms: 1.14x faster                                                     |
| django_template | 34.8 ms                                                    | 36.9 ms: 1.06x slower                                                     |
| genshi_text     | 23.7 ms                                                    | 25.5 ms: 1.08x slower                                                     |
| genshi_xml      | 51.6 ms                                                    | 57.9 ms: 1.12x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.1 us: 1.47x faster                                                     |
| deepcopy                   | 367 us                                                     | 271 us: 1.36x faster                                                      |
| richards                   | 50.9 ms                                                    | 39.5 ms: 1.29x faster                                                     |
| richards_super             | 57.4 ms                                                    | 44.7 ms: 1.28x faster                                                     |
| scimark_fft                | 392 ms                                                     | 307 ms: 1.28x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                    | 2.65 us: 1.26x faster                                                     |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.36 ms: 1.21x faster                                                     |
| async_tree_none            | 378 ms                                                     | 317 ms: 1.20x faster                                                      |
| crypto_pyaes               | 77.5 ms                                                    | 65.4 ms: 1.18x faster                                                     |
| spectral_norm              | 116 ms                                                     | 100 ms: 1.16x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 387 ms: 1.15x faster                                                      |
| xml_etree_generate         | 87.4 ms                                                    | 76.8 ms: 1.14x faster                                                     |
| async_tree_memoization     | 463 ms                                                     | 408 ms: 1.14x faster                                                      |
| mako                       | 11.2 ms                                                    | 9.90 ms: 1.14x faster                                                     |
| bpe_tokeniser              | 5.02 sec                                                   | 4.43 sec: 1.13x faster                                                    |
| xml_etree_process          | 61.2 ms                                                    | 54.4 ms: 1.12x faster                                                     |
| telco                      | 8.41 ms                                                    | 7.49 ms: 1.12x faster                                                     |
| xml_etree_parse            | 162 ms                                                     | 145 ms: 1.12x faster                                                      |
| tomli_loads                | 2.12 sec                                                   | 1.90 sec: 1.11x faster                                                    |
| pyflate                    | 484 ms                                                     | 435 ms: 1.11x faster                                                      |
| pathlib                    | 17.3 ms                                                    | 15.6 ms: 1.11x faster                                                     |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.5 ms: 1.11x faster                                                     |
| scimark_lu                 | 122 ms                                                     | 110 ms: 1.10x faster                                                      |
| float                      | 78.9 ms                                                    | 71.8 ms: 1.10x faster                                                     |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                                    |
| go                         | 145 ms                                                     | 132 ms: 1.10x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.10x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                     | 98.1 ms: 1.09x faster                                                     |
| coverage                   | 93.1 ms                                                    | 85.8 ms: 1.09x faster                                                     |
| scimark_sor                | 127 ms                                                     | 118 ms: 1.08x faster                                                      |
| sqlite_synth               | 2.99 us                                                    | 2.76 us: 1.08x faster                                                     |
| fannkuch                   | 402 ms                                                     | 372 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                                      |
| json_loads                 | 28.9 us                                                    | 26.9 us: 1.07x faster                                                     |
| async_tree_io_tg           | 936 ms                                                     | 872 ms: 1.07x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 547 ms: 1.07x faster                                                      |
| nbody                      | 88.3 ms                                                    | 82.3 ms: 1.07x faster                                                     |
| async_tree_io              | 939 ms                                                     | 885 ms: 1.06x faster                                                      |
| json_dumps                 | 10.7 ms                                                    | 10.2 ms: 1.06x faster                                                     |
| json                       | 5.31 ms                                                    | 5.06 ms: 1.05x faster                                                     |
| asyncio_tcp                | 508 ms                                                     | 484 ms: 1.05x faster                                                      |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                                     |
| pickle_list                | 5.11 us                                                    | 4.91 us: 1.04x faster                                                     |
| html5lib                   | 67.2 ms                                                    | 64.7 ms: 1.04x faster                                                     |
| unpickle_list              | 5.34 us                                                    | 5.16 us: 1.04x faster                                                     |
| coroutines                 | 23.2 ms                                                    | 22.4 ms: 1.03x faster                                                     |
| gc_traversal               | 3.98 ms                                                    | 3.85 ms: 1.03x faster                                                     |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                      |
| thrift                     | 823 us                                                     | 797 us: 1.03x faster                                                      |
| logging_format             | 6.47 us                                                    | 6.28 us: 1.03x faster                                                     |
| chaos                      | 61.3 ms                                                    | 59.7 ms: 1.03x faster                                                     |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                    |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                     |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                      |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.03x faster                                                      |
| pprint_safe_repr           | 758 ms                                                     | 740 ms: 1.02x faster                                                      |
| deltablue                  | 3.25 ms                                                    | 3.19 ms: 1.02x faster                                                     |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                      |
| logging_simple             | 5.74 us                                                    | 5.67 us: 1.01x faster                                                     |
| pickle_dict                | 34.8 us                                                    | 34.4 us: 1.01x faster                                                     |
| python_startup_no_site     | 7.11 ms                                                    | 7.03 ms: 1.01x faster                                                     |
| pickle                     | 11.5 us                                                    | 11.4 us: 1.01x faster                                                     |
| logging_silent             | 105 ns                                                     | 104 ns: 1.01x faster                                                      |
| regex_effbot               | 3.67 ms                                                    | 3.69 ms: 1.01x slower                                                     |
| comprehensions             | 16.6 us                                                    | 16.8 us: 1.01x slower                                                     |
| pickle_pure_python         | 305 us                                                     | 309 us: 1.01x slower                                                      |
| dulwich_log                | 67.2 ms                                                    | 68.2 ms: 1.01x slower                                                     |
| regex_v8                   | 25.1 ms                                                    | 25.5 ms: 1.02x slower                                                     |
| 2to3                       | 274 ms                                                     | 279 ms: 1.02x slower                                                      |
| async_generators           | 442 ms                                                     | 452 ms: 1.02x slower                                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.35 ms: 1.02x slower                                                     |
| sqlglot_transpile          | 1.63 ms                                                    | 1.68 ms: 1.03x slower                                                     |
| docutils                   | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                    |
| sqlglot_normalize          | 110 ms                                                     | 114 ms: 1.04x slower                                                      |
| pycparser                  | 1.16 sec                                                   | 1.20 sec: 1.04x slower                                                    |
| regex_compile              | 137 ms                                                     | 143 ms: 1.04x slower                                                      |
| raytrace                   | 267 ms                                                     | 278 ms: 1.04x slower                                                      |
| nqueens                    | 81.4 ms                                                    | 85.9 ms: 1.06x slower                                                     |
| django_template            | 34.8 ms                                                    | 36.9 ms: 1.06x slower                                                     |
| sympy_expand               | 473 ms                                                     | 505 ms: 1.07x slower                                                      |
| sympy_str                  | 282 ms                                                     | 303 ms: 1.07x slower                                                      |
| bench_thread_pool          | 834 us                                                     | 896 us: 1.07x slower                                                      |
| genshi_text                | 23.7 ms                                                    | 25.5 ms: 1.08x slower                                                     |
| sqlglot_optimize           | 55.5 ms                                                    | 60.3 ms: 1.09x slower                                                     |
| hexiom                     | 6.30 ms                                                    | 6.95 ms: 1.10x slower                                                     |
| sympy_sum                  | 156 ms                                                     | 175 ms: 1.12x slower                                                      |
| genshi_xml                 | 51.6 ms                                                    | 57.9 ms: 1.12x slower                                                     |
| sympy_integrate            | 20.5 ms                                                    | 23.4 ms: 1.14x slower                                                     |
| generators                 | 29.6 ms                                                    | 34.5 ms: 1.16x slower                                                     |
| pylint                     | 317 ms                                                     | 374 ms: 1.18x slower                                                      |
| bench_mp_pool              | 23.9 ms                                                    | 60.2 ms: 2.52x slower                                                     |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                              |

Benchmark hidden because not significant (5): unpickle, pprint_pformat, regex_dna, tornado_http, typing_runtime_protocols
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241003-3.14.0a0-8ef2e8f-JIT/bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f.json: unpack_sequence

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x
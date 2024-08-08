# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: c232e47
- commit date: 2024-08-07
- overall geometric mean: 1.00x slower
- HPT reliability: 99.74%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 282 ms: 1.03x slower                                                      |
| docutils       | 2.83 sec                                                   | 6.89 sec: 2.44x slower                                                    |
| tornado_http   | 94.6 ms                                                    | 93.1 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                      | 1.25x slower                                                              |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 331 ms: 1.14x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 398 ms: 1.11x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 305 ms: 1.10x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 536 ms: 1.10x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 432 ms: 1.07x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 571 ms: 1.07x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 880 ms: 1.06x faster                                                      |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                              |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 79.4 ms: 1.11x faster                                                     |
| float          | 78.9 ms                                                    | 71.0 ms: 1.11x faster                                                     |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                      | 1.08x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                                     |
| regex_compile  | 137 ms                                                     | 136 ms: 1.01x faster                                                      |
| regex_dna      | 221 ms                                                     | 224 ms: 1.01x slower                                                      |
| regex_effbot   | 3.67 ms                                                    | 3.82 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                      | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.89 sec: 1.12x faster                                                    |
| xml_etree_parse      | 162 ms                                                     | 147 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                     | 99.6 ms: 1.08x faster                                                     |
| xml_etree_process    | 61.2 ms                                                    | 57.8 ms: 1.06x faster                                                     |
| json_dumps           | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                     |
| xml_etree_generate   | 87.4 ms                                                    | 84.1 ms: 1.04x faster                                                     |
| unpickle_pure_python | 218 us                                                     | 211 us: 1.03x faster                                                      |
| json_loads           | 28.9 us                                                    | 28.0 us: 1.03x faster                                                     |
| pickle_pure_python   | 305 us                                                     | 316 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                     |
| python_startup_no_site | 7.11 ms                                                    | 7.20 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                      | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.71 ms: 1.16x faster                                                     |
| django_template | 34.8 ms                                                    | 35.3 ms: 1.02x slower                                                     |
| genshi_text     | 23.7 ms                                                    | 25.5 ms: 1.08x slower                                                     |
| genshi_xml      | 51.6 ms                                                    | 57.1 ms: 1.11x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.5 us: 1.44x faster                                                     |
| deepcopy                   | 367 us                                                     | 260 us: 1.41x faster                                                      |
| scimark_fft                | 392 ms                                                     | 304 ms: 1.29x faster                                                      |
| richards                   | 50.9 ms                                                    | 39.7 ms: 1.28x faster                                                     |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.15 ms: 1.27x faster                                                     |
| richards_super             | 57.4 ms                                                    | 45.4 ms: 1.26x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                    | 2.68 us: 1.25x faster                                                     |
| crypto_pyaes               | 77.5 ms                                                    | 66.1 ms: 1.17x faster                                                     |
| spectral_norm              | 116 ms                                                     | 99.5 ms: 1.17x faster                                                     |
| mako                       | 11.2 ms                                                    | 9.71 ms: 1.16x faster                                                     |
| async_tree_none            | 378 ms                                                     | 331 ms: 1.14x faster                                                      |
| scimark_lu                 | 122 ms                                                     | 107 ms: 1.13x faster                                                      |
| tomli_loads                | 2.12 sec                                                   | 1.89 sec: 1.12x faster                                                    |
| async_tree_memoization_tg  | 444 ms                                                     | 398 ms: 1.11x faster                                                      |
| nbody                      | 88.3 ms                                                    | 79.4 ms: 1.11x faster                                                     |
| float                      | 78.9 ms                                                    | 71.0 ms: 1.11x faster                                                     |
| bpe_tokeniser              | 5.02 sec                                                   | 4.52 sec: 1.11x faster                                                    |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.8 ms: 1.10x faster                                                     |
| scimark_sor                | 127 ms                                                     | 116 ms: 1.10x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 305 ms: 1.10x faster                                                      |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 536 ms: 1.10x faster                                                      |
| pyflate                    | 484 ms                                                     | 445 ms: 1.09x faster                                                      |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.09x faster                                                     |
| fannkuch                   | 402 ms                                                     | 372 ms: 1.08x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                     | 99.6 ms: 1.08x faster                                                     |
| logging_format             | 6.47 us                                                    | 6.01 us: 1.08x faster                                                     |
| telco                      | 8.41 ms                                                    | 7.83 ms: 1.07x faster                                                     |
| async_tree_memoization     | 463 ms                                                     | 432 ms: 1.07x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 571 ms: 1.07x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 880 ms: 1.06x faster                                                      |
| deltablue                  | 3.25 ms                                                    | 3.06 ms: 1.06x faster                                                     |
| gc_traversal               | 3.98 ms                                                    | 3.75 ms: 1.06x faster                                                     |
| xml_etree_process          | 61.2 ms                                                    | 57.8 ms: 1.06x faster                                                     |
| chaos                      | 61.3 ms                                                    | 58.1 ms: 1.06x faster                                                     |
| logging_simple             | 5.74 us                                                    | 5.47 us: 1.05x faster                                                     |
| logging_silent             | 105 ns                                                     | 99.8 ns: 1.05x faster                                                     |
| json_dumps                 | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                     |
| json                       | 5.31 ms                                                    | 5.08 ms: 1.04x faster                                                     |
| xml_etree_generate         | 87.4 ms                                                    | 84.1 ms: 1.04x faster                                                     |
| pprint_safe_repr           | 758 ms                                                     | 733 ms: 1.04x faster                                                      |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                                      |
| unpickle_pure_python       | 218 us                                                     | 211 us: 1.03x faster                                                      |
| mdp                        | 2.79 sec                                                   | 2.70 sec: 1.03x faster                                                    |
| json_loads                 | 28.9 us                                                    | 28.0 us: 1.03x faster                                                     |
| thrift                     | 823 us                                                     | 798 us: 1.03x faster                                                      |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                      |
| coroutines                 | 23.2 ms                                                    | 22.6 ms: 1.02x faster                                                     |
| bench_thread_pool          | 834 us                                                     | 817 us: 1.02x faster                                                      |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                                      |
| create_gc_cycles           | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                     |
| regex_v8                   | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                                     |
| coverage                   | 93.1 ms                                                    | 91.4 ms: 1.02x faster                                                     |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                    |
| tornado_http               | 94.6 ms                                                    | 93.1 ms: 1.02x faster                                                     |
| comprehensions             | 16.6 us                                                    | 16.4 us: 1.02x faster                                                     |
| asyncio_tcp                | 508 ms                                                     | 502 ms: 1.01x faster                                                      |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                     |
| regex_compile              | 137 ms                                                     | 136 ms: 1.01x faster                                                      |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                     |
| regex_dna                  | 221 ms                                                     | 224 ms: 1.01x slower                                                      |
| python_startup_no_site     | 7.11 ms                                                    | 7.20 ms: 1.01x slower                                                     |
| django_template            | 34.8 ms                                                    | 35.3 ms: 1.02x slower                                                     |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.02x slower                                                      |
| async_generators           | 442 ms                                                     | 454 ms: 1.03x slower                                                      |
| 2to3                       | 274 ms                                                     | 282 ms: 1.03x slower                                                      |
| pickle_pure_python         | 305 us                                                     | 316 us: 1.03x slower                                                      |
| typing_runtime_protocols   | 165 us                                                     | 170 us: 1.03x slower                                                      |
| regex_effbot               | 3.67 ms                                                    | 3.82 ms: 1.04x slower                                                     |
| sympy_expand               | 473 ms                                                     | 496 ms: 1.05x slower                                                      |
| sympy_str                  | 282 ms                                                     | 296 ms: 1.05x slower                                                      |
| sqlglot_transpile          | 1.63 ms                                                    | 1.73 ms: 1.06x slower                                                     |
| nqueens                    | 81.4 ms                                                    | 86.3 ms: 1.06x slower                                                     |
| sqlglot_parse              | 1.32 ms                                                    | 1.40 ms: 1.06x slower                                                     |
| hexiom                     | 6.30 ms                                                    | 6.71 ms: 1.07x slower                                                     |
| genshi_text                | 23.7 ms                                                    | 25.5 ms: 1.08x slower                                                     |
| sqlglot_optimize           | 55.5 ms                                                    | 60.6 ms: 1.09x slower                                                     |
| sympy_sum                  | 156 ms                                                     | 171 ms: 1.10x slower                                                      |
| generators                 | 29.6 ms                                                    | 32.8 ms: 1.11x slower                                                     |
| genshi_xml                 | 51.6 ms                                                    | 57.1 ms: 1.11x slower                                                     |
| sympy_integrate            | 20.5 ms                                                    | 22.8 ms: 1.11x slower                                                     |
| pylint                     | 317 ms                                                     | 443 ms: 1.40x slower                                                      |
| pycparser                  | 1.16 sec                                                   | 1.64 sec: 1.42x slower                                                    |
| docutils                   | 2.83 sec                                                   | 6.89 sec: 2.44x slower                                                    |
| raytrace                   | 267 ms                                                     | 5.00 sec: 18.77x slower                                                   |
| Geometric mean             | (ref)                                                      | 1.00x slower                                                              |

Benchmark hidden because not significant (4): async_tree_io, pprint_pformat, go, html5lib
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.74% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x
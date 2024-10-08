# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 1e7db3e
- commit date: 2024-07-29
- overall geometric mean: 1.02x faster
- HPT reliability: 95.11%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 289 ms: 1.05x slower                                                      |
| docutils       | 2.83 sec                                                   | 3.09 sec: 1.09x slower                                                    |
| html5lib       | 67.2 ms                                                    | 67.5 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                      | 1.04x slower                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 329 ms: 1.15x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 394 ms: 1.13x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 532 ms: 1.10x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.09x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 429 ms: 1.08x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 874 ms: 1.07x faster                                                      |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                              |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 80.1 ms: 1.10x faster                                                     |
| float          | 78.9 ms                                                    | 71.6 ms: 1.10x faster                                                     |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                      | 1.08x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.2 ms: 1.04x faster                                                     |
| regex_effbot   | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                                     |
| regex_dna      | 221 ms                                                     | 225 ms: 1.02x slower                                                      |
| regex_compile  | 137 ms                                                     | 151 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                      | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 147 ms: 1.10x faster                                                      |
| tomli_loads          | 2.12 sec                                                   | 1.98 sec: 1.07x faster                                                    |
| xml_etree_generate   | 87.4 ms                                                    | 82.0 ms: 1.07x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.07x faster                                                      |
| xml_etree_process    | 61.2 ms                                                    | 57.9 ms: 1.06x faster                                                     |
| json_dumps           | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                     |
| json_loads           | 28.9 us                                                    | 27.9 us: 1.04x faster                                                     |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                      |
| pickle_pure_python   | 305 us                                                     | 304 us: 1.00x faster                                                      |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                     |
| python_startup_no_site | 7.11 ms                                                    | 7.13 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.63 ms: 1.17x faster                                                     |
| genshi_text     | 23.7 ms                                                    | 24.6 ms: 1.04x slower                                                     |
| genshi_xml      | 51.6 ms                                                    | 56.2 ms: 1.09x slower                                                     |
| django_template | 34.8 ms                                                    | 38.0 ms: 1.09x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-1e7db3e |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.9 us: 1.42x faster                                                     |
| deepcopy                   | 367 us                                                     | 271 us: 1.35x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                    | 2.66 us: 1.26x faster                                                     |
| scimark_fft                | 392 ms                                                     | 313 ms: 1.25x faster                                                      |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.42 ms: 1.19x faster                                                     |
| mako                       | 11.2 ms                                                    | 9.63 ms: 1.17x faster                                                     |
| crypto_pyaes               | 77.5 ms                                                    | 67.0 ms: 1.16x faster                                                     |
| async_tree_none            | 378 ms                                                     | 329 ms: 1.15x faster                                                      |
| richards                   | 50.9 ms                                                    | 44.7 ms: 1.14x faster                                                     |
| spectral_norm              | 116 ms                                                     | 102 ms: 1.14x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 394 ms: 1.13x faster                                                      |
| richards_super             | 57.4 ms                                                    | 51.3 ms: 1.12x faster                                                     |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 532 ms: 1.10x faster                                                      |
| nbody                      | 88.3 ms                                                    | 80.1 ms: 1.10x faster                                                     |
| float                      | 78.9 ms                                                    | 71.6 ms: 1.10x faster                                                     |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                                      |
| bpe_tokeniser              | 5.02 sec                                                   | 4.60 sec: 1.09x faster                                                    |
| scimark_monte_carlo        | 69.2 ms                                                    | 63.7 ms: 1.09x faster                                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.09x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 429 ms: 1.08x faster                                                      |
| pyflate                    | 484 ms                                                     | 450 ms: 1.08x faster                                                      |
| tomli_loads                | 2.12 sec                                                   | 1.98 sec: 1.07x faster                                                    |
| fannkuch                   | 402 ms                                                     | 375 ms: 1.07x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 874 ms: 1.07x faster                                                      |
| xml_etree_generate         | 87.4 ms                                                    | 82.0 ms: 1.07x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                     | 101 ms: 1.07x faster                                                      |
| mdp                        | 2.79 sec                                                   | 2.62 sec: 1.06x faster                                                    |
| logging_format             | 6.47 us                                                    | 6.12 us: 1.06x faster                                                     |
| xml_etree_process          | 61.2 ms                                                    | 57.9 ms: 1.06x faster                                                     |
| deltablue                  | 3.25 ms                                                    | 3.08 ms: 1.06x faster                                                     |
| pathlib                    | 17.3 ms                                                    | 16.4 ms: 1.06x faster                                                     |
| telco                      | 8.41 ms                                                    | 7.98 ms: 1.05x faster                                                     |
| json_dumps                 | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                     |
| gc_traversal               | 3.98 ms                                                    | 3.81 ms: 1.04x faster                                                     |
| logging_silent             | 105 ns                                                     | 101 ns: 1.04x faster                                                      |
| thrift                     | 823 us                                                     | 792 us: 1.04x faster                                                      |
| regex_v8                   | 25.1 ms                                                    | 24.2 ms: 1.04x faster                                                     |
| json_loads                 | 28.9 us                                                    | 27.9 us: 1.04x faster                                                     |
| coroutines                 | 23.2 ms                                                    | 22.4 ms: 1.03x faster                                                     |
| logging_simple             | 5.74 us                                                    | 5.57 us: 1.03x faster                                                     |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                     |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                      |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                      |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                     |
| chaos                      | 61.3 ms                                                    | 60.0 ms: 1.02x faster                                                     |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                      |
| json                       | 5.31 ms                                                    | 5.20 ms: 1.02x faster                                                     |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                    |
| coverage                   | 93.1 ms                                                    | 91.6 ms: 1.02x faster                                                     |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                                      |
| pickle_pure_python         | 305 us                                                     | 304 us: 1.00x faster                                                      |
| asyncio_tcp                | 508 ms                                                     | 507 ms: 1.00x faster                                                      |
| python_startup_no_site     | 7.11 ms                                                    | 7.13 ms: 1.00x slower                                                     |
| html5lib                   | 67.2 ms                                                    | 67.5 ms: 1.00x slower                                                     |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                     |
| bench_thread_pool          | 834 us                                                     | 839 us: 1.01x slower                                                      |
| regex_effbot               | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                                     |
| sqlglot_parse              | 1.32 ms                                                    | 1.34 ms: 1.02x slower                                                     |
| regex_dna                  | 221 ms                                                     | 225 ms: 1.02x slower                                                      |
| comprehensions             | 16.6 us                                                    | 17.0 us: 1.02x slower                                                     |
| pycparser                  | 1.16 sec                                                   | 1.20 sec: 1.04x slower                                                    |
| genshi_text                | 23.7 ms                                                    | 24.6 ms: 1.04x slower                                                     |
| sqlglot_transpile          | 1.63 ms                                                    | 1.71 ms: 1.05x slower                                                     |
| scimark_sor                | 127 ms                                                     | 134 ms: 1.05x slower                                                      |
| go                         | 145 ms                                                     | 152 ms: 1.05x slower                                                      |
| 2to3                       | 274 ms                                                     | 289 ms: 1.05x slower                                                      |
| raytrace                   | 267 ms                                                     | 281 ms: 1.05x slower                                                      |
| async_generators           | 442 ms                                                     | 473 ms: 1.07x slower                                                      |
| typing_runtime_protocols   | 165 us                                                     | 176 us: 1.07x slower                                                      |
| sqlglot_normalize          | 110 ms                                                     | 119 ms: 1.08x slower                                                      |
| scimark_lu                 | 122 ms                                                     | 132 ms: 1.08x slower                                                      |
| sqlglot_optimize           | 55.5 ms                                                    | 60.4 ms: 1.09x slower                                                     |
| genshi_xml                 | 51.6 ms                                                    | 56.2 ms: 1.09x slower                                                     |
| docutils                   | 2.83 sec                                                   | 3.09 sec: 1.09x slower                                                    |
| django_template            | 34.8 ms                                                    | 38.0 ms: 1.09x slower                                                     |
| regex_compile              | 137 ms                                                     | 151 ms: 1.10x slower                                                      |
| sympy_str                  | 282 ms                                                     | 322 ms: 1.14x slower                                                      |
| generators                 | 29.6 ms                                                    | 34.1 ms: 1.15x slower                                                     |
| sympy_expand               | 473 ms                                                     | 545 ms: 1.15x slower                                                      |
| nqueens                    | 81.4 ms                                                    | 94.6 ms: 1.16x slower                                                     |
| sympy_sum                  | 156 ms                                                     | 186 ms: 1.19x slower                                                      |
| sympy_integrate            | 20.5 ms                                                    | 24.8 ms: 1.21x slower                                                     |
| pylint                     | 317 ms                                                     | 394 ms: 1.24x slower                                                      |
| hexiom                     | 6.30 ms                                                    | 8.07 ms: 1.28x slower                                                     |
| Geometric mean             | (ref)                                                      | 1.02x faster                                                              |

Benchmark hidden because not significant (5): async_tree_io, dask, pprint_safe_repr, tornado_http, pprint_pformat
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 95.11% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x
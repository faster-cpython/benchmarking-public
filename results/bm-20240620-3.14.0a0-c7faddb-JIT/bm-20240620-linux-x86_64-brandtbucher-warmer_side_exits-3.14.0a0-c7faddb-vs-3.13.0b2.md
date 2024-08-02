# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: warmer_side_exits
- machine: linux-x86_64
- commit hash: c7faddb
- commit date: 2024-06-20
- overall geometric mean: 1.03x faster
- HPT reliability: 99.51%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 276 ms: 1.01x slower                                                     |
| docutils       | 2.83 sec                                                   | 2.89 sec: 1.02x slower                                                   |
| html5lib       | 67.2 ms                                                    | 67.8 ms: 1.01x slower                                                    |
| tornado_http   | 94.6 ms                                                    | 94.0 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                      | 1.01x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 936 ms                                                     | 882 ms: 1.06x faster                                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 422 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 563 ms: 1.04x faster                                                     |
| async_tree_io              | 939 ms                                                     | 904 ms: 1.04x faster                                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 594 ms: 1.03x faster                                                     |
| async_tree_none            | 378 ms                                                     | 368 ms: 1.03x faster                                                     |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                             |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.2 ms: 1.12x faster                                                    |
| nbody          | 88.3 ms                                                    | 81.2 ms: 1.09x faster                                                    |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                      | 1.08x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 136 ms: 1.01x faster                                                     |
| regex_v8       | 25.1 ms                                                    | 26.3 ms: 1.05x slower                                                    |
| regex_dna      | 221 ms                                                     | 233 ms: 1.05x slower                                                     |
| regex_effbot   | 3.67 ms                                                    | 3.95 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                      | 1.04x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.90 sec: 1.11x faster                                                   |
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.10x faster                                                     |
| xml_etree_generate   | 87.4 ms                                                    | 81.0 ms: 1.08x faster                                                    |
| unpickle_pure_python | 218 us                                                     | 202 us: 1.08x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                     | 100 ms: 1.07x faster                                                     |
| xml_etree_process    | 61.2 ms                                                    | 57.3 ms: 1.07x faster                                                    |
| pickle_pure_python   | 305 us                                                     | 296 us: 1.03x faster                                                     |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                    |
| unpickle_list        | 5.34 us                                                    | 5.20 us: 1.03x faster                                                    |
| unpickle             | 15.1 us                                                    | 14.7 us: 1.03x faster                                                    |
| pickle_list          | 5.11 us                                                    | 5.01 us: 1.02x faster                                                    |
| json_loads           | 28.9 us                                                    | 28.3 us: 1.02x faster                                                    |
| pickle_dict          | 34.8 us                                                    | 34.5 us: 1.01x faster                                                    |
| pickle               | 11.5 us                                                    | 11.9 us: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                      | 1.04x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.8 ms: 1.01x slower                                                    |
| python_startup_no_site | 7.11 ms                                                    | 7.41 ms: 1.04x slower                                                    |
| Geometric mean         | (ref)                                                      | 1.02x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.80 ms: 1.15x faster                                                    |
| django_template | 34.8 ms                                                    | 36.5 ms: 1.05x slower                                                    |
| genshi_text     | 23.7 ms                                                    | 25.8 ms: 1.09x slower                                                    |
| genshi_xml      | 51.6 ms                                                    | 59.4 ms: 1.15x slower                                                    |
| Geometric mean  | (ref)                                                      | 1.04x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.5 us: 1.39x faster                                                    |
| deepcopy                   | 367 us                                                     | 278 us: 1.32x faster                                                     |
| scimark_fft                | 392 ms                                                     | 313 ms: 1.25x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                    | 2.76 us: 1.21x faster                                                    |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.36 ms: 1.21x faster                                                    |
| fannkuch                   | 402 ms                                                     | 345 ms: 1.17x faster                                                     |
| crypto_pyaes               | 77.5 ms                                                    | 66.8 ms: 1.16x faster                                                    |
| mako                       | 11.2 ms                                                    | 9.80 ms: 1.15x faster                                                    |
| richards                   | 50.9 ms                                                    | 44.6 ms: 1.14x faster                                                    |
| pyflate                    | 484 ms                                                     | 425 ms: 1.14x faster                                                     |
| richards_super             | 57.4 ms                                                    | 50.5 ms: 1.14x faster                                                    |
| scimark_monte_carlo        | 69.2 ms                                                    | 61.4 ms: 1.13x faster                                                    |
| float                      | 78.9 ms                                                    | 70.2 ms: 1.12x faster                                                    |
| spectral_norm              | 116 ms                                                     | 104 ms: 1.12x faster                                                     |
| tomli_loads                | 2.12 sec                                                   | 1.90 sec: 1.11x faster                                                   |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.10x faster                                                     |
| nbody                      | 88.3 ms                                                    | 81.2 ms: 1.09x faster                                                    |
| pprint_pformat             | 1.56 sec                                                   | 1.44 sec: 1.08x faster                                                   |
| xml_etree_generate         | 87.4 ms                                                    | 81.0 ms: 1.08x faster                                                    |
| unpickle_pure_python       | 218 us                                                     | 202 us: 1.08x faster                                                     |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                     | 100 ms: 1.07x faster                                                     |
| xml_etree_process          | 61.2 ms                                                    | 57.3 ms: 1.07x faster                                                    |
| telco                      | 8.41 ms                                                    | 7.89 ms: 1.07x faster                                                    |
| pprint_safe_repr           | 758 ms                                                     | 712 ms: 1.06x faster                                                     |
| logging_format             | 6.47 us                                                    | 6.08 us: 1.06x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 882 ms: 1.06x faster                                                     |
| sqlite_synth               | 2.99 us                                                    | 2.83 us: 1.06x faster                                                    |
| async_tree_memoization_tg  | 444 ms                                                     | 422 ms: 1.05x faster                                                     |
| logging_simple             | 5.74 us                                                    | 5.50 us: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 563 ms: 1.04x faster                                                     |
| bpe_tokeniser              | 5.02 sec                                                   | 4.82 sec: 1.04x faster                                                   |
| async_tree_io              | 939 ms                                                     | 904 ms: 1.04x faster                                                     |
| asyncio_tcp                | 508 ms                                                     | 489 ms: 1.04x faster                                                     |
| chaos                      | 61.3 ms                                                    | 59.2 ms: 1.04x faster                                                    |
| mdp                        | 2.79 sec                                                   | 2.69 sec: 1.03x faster                                                   |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                    |
| pickle_pure_python         | 305 us                                                     | 296 us: 1.03x faster                                                     |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                     |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 594 ms: 1.03x faster                                                     |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                    |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                     |
| async_tree_none            | 378 ms                                                     | 368 ms: 1.03x faster                                                     |
| unpickle_list              | 5.34 us                                                    | 5.20 us: 1.03x faster                                                    |
| unpickle                   | 15.1 us                                                    | 14.7 us: 1.03x faster                                                    |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                     |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                                    |
| pickle_list                | 5.11 us                                                    | 5.01 us: 1.02x faster                                                    |
| json_loads                 | 28.9 us                                                    | 28.3 us: 1.02x faster                                                    |
| sqlglot_transpile          | 1.63 ms                                                    | 1.61 ms: 1.02x faster                                                    |
| comprehensions             | 16.6 us                                                    | 16.4 us: 1.02x faster                                                    |
| thrift                     | 823 us                                                     | 812 us: 1.01x faster                                                     |
| coroutines                 | 23.2 ms                                                    | 22.9 ms: 1.01x faster                                                    |
| json                       | 5.31 ms                                                    | 5.27 ms: 1.01x faster                                                    |
| pickle_dict                | 34.8 us                                                    | 34.5 us: 1.01x faster                                                    |
| regex_compile              | 137 ms                                                     | 136 ms: 1.01x faster                                                     |
| tornado_http               | 94.6 ms                                                    | 94.0 ms: 1.01x faster                                                    |
| bench_thread_pool          | 834 us                                                     | 830 us: 1.00x faster                                                     |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                    |
| 2to3                       | 274 ms                                                     | 276 ms: 1.01x slower                                                     |
| python_startup             | 10.8 ms                                                    | 10.8 ms: 1.01x slower                                                    |
| gc_traversal               | 3.98 ms                                                    | 4.01 ms: 1.01x slower                                                    |
| html5lib                   | 67.2 ms                                                    | 67.8 ms: 1.01x slower                                                    |
| logging_silent             | 105 ns                                                     | 106 ns: 1.01x slower                                                     |
| dulwich_log                | 67.2 ms                                                    | 67.9 ms: 1.01x slower                                                    |
| coverage                   | 93.1 ms                                                    | 94.2 ms: 1.01x slower                                                    |
| go                         | 145 ms                                                     | 147 ms: 1.02x slower                                                     |
| generators                 | 29.6 ms                                                    | 30.2 ms: 1.02x slower                                                    |
| typing_runtime_protocols   | 165 us                                                     | 168 us: 1.02x slower                                                     |
| docutils                   | 2.83 sec                                                   | 2.89 sec: 1.02x slower                                                   |
| nqueens                    | 81.4 ms                                                    | 84.2 ms: 1.03x slower                                                    |
| pickle                     | 11.5 us                                                    | 11.9 us: 1.03x slower                                                    |
| scimark_lu                 | 122 ms                                                     | 126 ms: 1.04x slower                                                     |
| sqlglot_optimize           | 55.5 ms                                                    | 57.7 ms: 1.04x slower                                                    |
| raytrace                   | 267 ms                                                     | 277 ms: 1.04x slower                                                     |
| python_startup_no_site     | 7.11 ms                                                    | 7.41 ms: 1.04x slower                                                    |
| sqlglot_normalize          | 110 ms                                                     | 115 ms: 1.04x slower                                                     |
| async_generators           | 442 ms                                                     | 461 ms: 1.04x slower                                                     |
| hexiom                     | 6.30 ms                                                    | 6.57 ms: 1.04x slower                                                    |
| regex_v8                   | 25.1 ms                                                    | 26.3 ms: 1.05x slower                                                    |
| scimark_sor                | 127 ms                                                     | 134 ms: 1.05x slower                                                     |
| django_template            | 34.8 ms                                                    | 36.5 ms: 1.05x slower                                                    |
| regex_dna                  | 221 ms                                                     | 233 ms: 1.05x slower                                                     |
| sympy_str                  | 282 ms                                                     | 297 ms: 1.05x slower                                                     |
| sympy_expand               | 473 ms                                                     | 507 ms: 1.07x slower                                                     |
| regex_effbot               | 3.67 ms                                                    | 3.95 ms: 1.08x slower                                                    |
| sympy_sum                  | 156 ms                                                     | 168 ms: 1.08x slower                                                     |
| sympy_integrate            | 20.5 ms                                                    | 22.3 ms: 1.09x slower                                                    |
| genshi_text                | 23.7 ms                                                    | 25.8 ms: 1.09x slower                                                    |
| pylint                     | 317 ms                                                     | 349 ms: 1.10x slower                                                     |
| genshi_xml                 | 51.6 ms                                                    | 59.4 ms: 1.15x slower                                                    |
| deltablue                  | 3.25 ms                                                    | 3.85 ms: 1.18x slower                                                    |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                             |

Benchmark hidden because not significant (4): async_tree_memoization, dask, async_tree_none_tg, pycparser
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.51% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.11x
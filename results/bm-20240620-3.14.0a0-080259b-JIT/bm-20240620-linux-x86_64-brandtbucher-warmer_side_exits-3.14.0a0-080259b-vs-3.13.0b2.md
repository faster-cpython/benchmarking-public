# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: warmer_side_exits
- machine: linux-x86_64
- commit hash: 080259b
- commit date: 2024-06-20
- overall geometric mean: 1.03x faster
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 276 ms: 1.01x slower                                                     |
| docutils       | 2.83 sec                                                   | 2.88 sec: 1.02x slower                                                   |
| html5lib       | 67.2 ms                                                    | 65.5 ms: 1.03x faster                                                    |
| tornado_http   | 94.6 ms                                                    | 94.1 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                      | 1.00x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 424 ms: 1.05x faster                                                     |
| async_tree_io_tg           | 936 ms                                                     | 902 ms: 1.04x faster                                                     |
| async_tree_io              | 939 ms                                                     | 911 ms: 1.03x faster                                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 570 ms: 1.03x faster                                                     |
| async_tree_none            | 378 ms                                                     | 369 ms: 1.03x faster                                                     |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                             |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.6 ms: 1.12x faster                                                    |
| nbody          | 88.3 ms                                                    | 83.0 ms: 1.06x faster                                                    |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                      | 1.07x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.0 ms: 1.05x faster                                                    |
| regex_compile  | 137 ms                                                     | 134 ms: 1.02x faster                                                     |
| regex_effbot   | 3.67 ms                                                    | 3.72 ms: 1.01x slower                                                    |
| regex_dna      | 221 ms                                                     | 228 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                      | 1.01x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.90 sec: 1.11x faster                                                   |
| xml_etree_parse      | 162 ms                                                     | 149 ms: 1.09x faster                                                     |
| xml_etree_generate   | 87.4 ms                                                    | 80.6 ms: 1.08x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                     | 99.3 ms: 1.08x faster                                                    |
| unpickle_pure_python | 218 us                                                     | 204 us: 1.07x faster                                                     |
| xml_etree_process    | 61.2 ms                                                    | 57.8 ms: 1.06x faster                                                    |
| unpickle_list        | 5.34 us                                                    | 5.13 us: 1.04x faster                                                    |
| pickle_pure_python   | 305 us                                                     | 294 us: 1.04x faster                                                     |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                    |
| json_loads           | 28.9 us                                                    | 28.5 us: 1.01x faster                                                    |
| pickle_list          | 5.11 us                                                    | 5.19 us: 1.02x slower                                                    |
| pickle               | 11.5 us                                                    | 11.8 us: 1.03x slower                                                    |
| pickle_dict          | 34.8 us                                                    | 35.9 us: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                      | 1.04x faster                                                             |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.8 ms: 1.01x slower                                                    |
| python_startup_no_site | 7.11 ms                                                    | 7.39 ms: 1.04x slower                                                    |
| Geometric mean         | (ref)                                                      | 1.02x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.58 ms: 1.17x faster                                                    |
| django_template | 34.8 ms                                                    | 35.5 ms: 1.02x slower                                                    |
| genshi_text     | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                    |
| genshi_xml      | 51.6 ms                                                    | 55.9 ms: 1.08x slower                                                    |
| Geometric mean  | (ref)                                                      | 1.00x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 29.1 us: 1.37x faster                                                    |
| deepcopy                   | 367 us                                                     | 279 us: 1.32x faster                                                     |
| scimark_fft                | 392 ms                                                     | 313 ms: 1.26x faster                                                     |
| richards                   | 50.9 ms                                                    | 40.5 ms: 1.26x faster                                                    |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.22 ms: 1.25x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                    | 2.76 us: 1.21x faster                                                    |
| richards_super             | 57.4 ms                                                    | 47.6 ms: 1.20x faster                                                    |
| mako                       | 11.2 ms                                                    | 9.58 ms: 1.17x faster                                                    |
| fannkuch                   | 402 ms                                                     | 345 ms: 1.17x faster                                                     |
| crypto_pyaes               | 77.5 ms                                                    | 66.8 ms: 1.16x faster                                                    |
| scimark_monte_carlo        | 69.2 ms                                                    | 61.9 ms: 1.12x faster                                                    |
| float                      | 78.9 ms                                                    | 70.6 ms: 1.12x faster                                                    |
| pyflate                    | 484 ms                                                     | 434 ms: 1.12x faster                                                     |
| gc_traversal               | 3.98 ms                                                    | 3.57 ms: 1.11x faster                                                    |
| tomli_loads                | 2.12 sec                                                   | 1.90 sec: 1.11x faster                                                   |
| spectral_norm              | 116 ms                                                     | 105 ms: 1.11x faster                                                     |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                    |
| xml_etree_parse            | 162 ms                                                     | 149 ms: 1.09x faster                                                     |
| xml_etree_generate         | 87.4 ms                                                    | 80.6 ms: 1.08x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                     | 99.3 ms: 1.08x faster                                                    |
| logging_format             | 6.47 us                                                    | 6.03 us: 1.07x faster                                                    |
| unpickle_pure_python       | 218 us                                                     | 204 us: 1.07x faster                                                     |
| pprint_pformat             | 1.56 sec                                                   | 1.46 sec: 1.07x faster                                                   |
| pprint_safe_repr           | 758 ms                                                     | 712 ms: 1.07x faster                                                     |
| nbody                      | 88.3 ms                                                    | 83.0 ms: 1.06x faster                                                    |
| xml_etree_process          | 61.2 ms                                                    | 57.8 ms: 1.06x faster                                                    |
| sqlite_synth               | 2.99 us                                                    | 2.83 us: 1.06x faster                                                    |
| telco                      | 8.41 ms                                                    | 7.97 ms: 1.06x faster                                                    |
| logging_simple             | 5.74 us                                                    | 5.46 us: 1.05x faster                                                    |
| chaos                      | 61.3 ms                                                    | 58.3 ms: 1.05x faster                                                    |
| async_tree_memoization_tg  | 444 ms                                                     | 424 ms: 1.05x faster                                                     |
| regex_v8                   | 25.1 ms                                                    | 24.0 ms: 1.05x faster                                                    |
| bpe_tokeniser              | 5.02 sec                                                   | 4.81 sec: 1.04x faster                                                   |
| unpickle_list              | 5.34 us                                                    | 5.13 us: 1.04x faster                                                    |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 902 ms: 1.04x faster                                                     |
| pickle_pure_python         | 305 us                                                     | 294 us: 1.04x faster                                                     |
| asyncio_tcp                | 508 ms                                                     | 491 ms: 1.04x faster                                                     |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                     |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                                     |
| async_tree_io              | 939 ms                                                     | 911 ms: 1.03x faster                                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 570 ms: 1.03x faster                                                     |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                                    |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                   |
| async_tree_none            | 378 ms                                                     | 369 ms: 1.03x faster                                                     |
| html5lib                   | 67.2 ms                                                    | 65.5 ms: 1.03x faster                                                    |
| sqlglot_transpile          | 1.63 ms                                                    | 1.59 ms: 1.03x faster                                                    |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                    |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                                     |
| regex_compile              | 137 ms                                                     | 134 ms: 1.02x faster                                                     |
| json_loads                 | 28.9 us                                                    | 28.5 us: 1.01x faster                                                    |
| comprehensions             | 16.6 us                                                    | 16.4 us: 1.01x faster                                                    |
| mdp                        | 2.79 sec                                                   | 2.75 sec: 1.01x faster                                                   |
| bench_thread_pool          | 834 us                                                     | 827 us: 1.01x faster                                                     |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                                    |
| thrift                     | 823 us                                                     | 817 us: 1.01x faster                                                     |
| tornado_http               | 94.6 ms                                                    | 94.1 ms: 1.01x faster                                                    |
| 2to3                       | 274 ms                                                     | 276 ms: 1.01x slower                                                     |
| python_startup             | 10.8 ms                                                    | 10.8 ms: 1.01x slower                                                    |
| logging_silent             | 105 ns                                                     | 106 ns: 1.01x slower                                                     |
| dulwich_log                | 67.2 ms                                                    | 67.7 ms: 1.01x slower                                                    |
| regex_effbot               | 3.67 ms                                                    | 3.72 ms: 1.01x slower                                                    |
| sqlglot_optimize           | 55.5 ms                                                    | 56.3 ms: 1.01x slower                                                    |
| go                         | 145 ms                                                     | 147 ms: 1.02x slower                                                     |
| pickle_list                | 5.11 us                                                    | 5.19 us: 1.02x slower                                                    |
| docutils                   | 2.83 sec                                                   | 2.88 sec: 1.02x slower                                                   |
| scimark_lu                 | 122 ms                                                     | 124 ms: 1.02x slower                                                     |
| django_template            | 34.8 ms                                                    | 35.5 ms: 1.02x slower                                                    |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.02x slower                                                   |
| typing_runtime_protocols   | 165 us                                                     | 169 us: 1.03x slower                                                     |
| regex_dna                  | 221 ms                                                     | 228 ms: 1.03x slower                                                     |
| pickle                     | 11.5 us                                                    | 11.8 us: 1.03x slower                                                    |
| pickle_dict                | 34.8 us                                                    | 35.9 us: 1.03x slower                                                    |
| async_generators           | 442 ms                                                     | 457 ms: 1.03x slower                                                     |
| sqlglot_normalize          | 110 ms                                                     | 114 ms: 1.03x slower                                                     |
| raytrace                   | 267 ms                                                     | 277 ms: 1.04x slower                                                     |
| hexiom                     | 6.30 ms                                                    | 6.54 ms: 1.04x slower                                                    |
| python_startup_no_site     | 7.11 ms                                                    | 7.39 ms: 1.04x slower                                                    |
| nqueens                    | 81.4 ms                                                    | 84.7 ms: 1.04x slower                                                    |
| genshi_text                | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                    |
| sympy_str                  | 282 ms                                                     | 300 ms: 1.06x slower                                                     |
| scimark_sor                | 127 ms                                                     | 136 ms: 1.07x slower                                                     |
| sympy_expand               | 473 ms                                                     | 505 ms: 1.07x slower                                                     |
| sympy_sum                  | 156 ms                                                     | 169 ms: 1.08x slower                                                     |
| genshi_xml                 | 51.6 ms                                                    | 55.9 ms: 1.08x slower                                                    |
| sympy_integrate            | 20.5 ms                                                    | 22.3 ms: 1.09x slower                                                    |
| pylint                     | 317 ms                                                     | 347 ms: 1.10x slower                                                     |
| deltablue                  | 3.25 ms                                                    | 3.84 ms: 1.18x slower                                                    |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                             |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed, async_tree_memoization, dask, json, coverage, generators, bench_mp_pool, async_tree_none_tg, unpickle
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.83% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x
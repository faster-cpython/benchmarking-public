# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: warmer_side_exits
- machine: linux-x86_64
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.83 sec                                                   | 2.86 sec: 1.01x slower                                                   |
| html5lib       | 67.2 ms                                                    | 65.7 ms: 1.02x faster                                                    |
| tornado_http   | 94.6 ms                                                    | 92.2 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                      | 1.01x faster                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 312 ms: 1.21x faster                                                     |
| async_tree_memoization     | 463 ms                                                     | 403 ms: 1.15x faster                                                     |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                     |
| async_tree_io_tg           | 936 ms                                                     | 830 ms: 1.13x faster                                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 397 ms: 1.12x faster                                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 555 ms: 1.10x faster                                                     |
| async_tree_io              | 939 ms                                                     | 867 ms: 1.08x faster                                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 543 ms: 1.08x faster                                                     |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.7 ms: 1.12x faster                                                    |
| nbody          | 88.3 ms                                                    | 79.7 ms: 1.11x faster                                                    |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                      | 1.08x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 134 ms: 1.02x faster                                                     |
| regex_v8       | 25.1 ms                                                    | 24.9 ms: 1.01x faster                                                    |
| regex_effbot   | 3.67 ms                                                    | 3.68 ms: 1.00x slower                                                    |
| regex_dna      | 221 ms                                                     | 226 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                      | 1.00x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                   |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                     |
| unpickle_pure_python | 218 us                                                     | 201 us: 1.09x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                     | 99.1 ms: 1.08x faster                                                    |
| xml_etree_generate   | 87.4 ms                                                    | 81.1 ms: 1.08x faster                                                    |
| xml_etree_process    | 61.2 ms                                                    | 57.1 ms: 1.07x faster                                                    |
| json_loads           | 28.9 us                                                    | 27.6 us: 1.05x faster                                                    |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                    |
| pickle_pure_python   | 305 us                                                     | 299 us: 1.02x faster                                                     |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                                    |
| python_startup_no_site | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                                    |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.53 ms: 1.18x faster                                                    |
| django_template | 34.8 ms                                                    | 35.3 ms: 1.02x slower                                                    |
| genshi_text     | 23.7 ms                                                    | 25.0 ms: 1.06x slower                                                    |
| genshi_xml      | 51.6 ms                                                    | 58.1 ms: 1.13x slower                                                    |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 29.0 us: 1.37x faster                                                    |
| deepcopy                   | 367 us                                                     | 271 us: 1.36x faster                                                     |
| scimark_fft                | 392 ms                                                     | 313 ms: 1.25x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                    | 2.73 us: 1.23x faster                                                    |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.30 ms: 1.23x faster                                                    |
| async_tree_none            | 378 ms                                                     | 312 ms: 1.21x faster                                                     |
| mako                       | 11.2 ms                                                    | 9.53 ms: 1.18x faster                                                    |
| richards                   | 50.9 ms                                                    | 43.6 ms: 1.17x faster                                                    |
| richards_super             | 57.4 ms                                                    | 49.3 ms: 1.16x faster                                                    |
| crypto_pyaes               | 77.5 ms                                                    | 67.0 ms: 1.16x faster                                                    |
| async_tree_memoization     | 463 ms                                                     | 403 ms: 1.15x faster                                                     |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.7 ms: 1.14x faster                                                    |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                     |
| async_tree_io_tg           | 936 ms                                                     | 830 ms: 1.13x faster                                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 397 ms: 1.12x faster                                                     |
| fannkuch                   | 402 ms                                                     | 359 ms: 1.12x faster                                                     |
| float                      | 78.9 ms                                                    | 70.7 ms: 1.12x faster                                                    |
| pyflate                    | 484 ms                                                     | 434 ms: 1.11x faster                                                     |
| spectral_norm              | 116 ms                                                     | 105 ms: 1.11x faster                                                     |
| tomli_loads                | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                   |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                     |
| nbody                      | 88.3 ms                                                    | 79.7 ms: 1.11x faster                                                    |
| mdp                        | 2.79 sec                                                   | 2.53 sec: 1.10x faster                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 555 ms: 1.10x faster                                                     |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.10x faster                                                    |
| unpickle_pure_python       | 218 us                                                     | 201 us: 1.09x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                     | 99.1 ms: 1.08x faster                                                    |
| async_tree_io              | 939 ms                                                     | 867 ms: 1.08x faster                                                     |
| gc_traversal               | 3.98 ms                                                    | 3.68 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 543 ms: 1.08x faster                                                     |
| logging_format             | 6.47 us                                                    | 6.00 us: 1.08x faster                                                    |
| xml_etree_generate         | 87.4 ms                                                    | 81.1 ms: 1.08x faster                                                    |
| xml_etree_process          | 61.2 ms                                                    | 57.1 ms: 1.07x faster                                                    |
| telco                      | 8.41 ms                                                    | 7.90 ms: 1.06x faster                                                    |
| chaos                      | 61.3 ms                                                    | 57.9 ms: 1.06x faster                                                    |
| pprint_pformat             | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                                   |
| json_loads                 | 28.9 us                                                    | 27.6 us: 1.05x faster                                                    |
| bpe_tokeniser              | 5.02 sec                                                   | 4.81 sec: 1.04x faster                                                   |
| pprint_safe_repr           | 758 ms                                                     | 726 ms: 1.04x faster                                                     |
| logging_simple             | 5.74 us                                                    | 5.52 us: 1.04x faster                                                    |
| json                       | 5.31 ms                                                    | 5.10 ms: 1.04x faster                                                    |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                    |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                    |
| thrift                     | 823 us                                                     | 798 us: 1.03x faster                                                     |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                                     |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                     |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                                    |
| python_startup             | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                                    |
| tornado_http               | 94.6 ms                                                    | 92.2 ms: 1.03x faster                                                    |
| sqlglot_transpile          | 1.63 ms                                                    | 1.59 ms: 1.02x faster                                                    |
| html5lib                   | 67.2 ms                                                    | 65.7 ms: 1.02x faster                                                    |
| pickle_pure_python         | 305 us                                                     | 299 us: 1.02x faster                                                     |
| regex_compile              | 137 ms                                                     | 134 ms: 1.02x faster                                                     |
| dask                       | 369 ms                                                     | 363 ms: 1.02x faster                                                     |
| asyncio_tcp                | 508 ms                                                     | 499 ms: 1.02x faster                                                     |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                   |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                     |
| pycparser                  | 1.16 sec                                                   | 1.14 sec: 1.01x faster                                                   |
| regex_v8                   | 25.1 ms                                                    | 24.9 ms: 1.01x faster                                                    |
| go                         | 145 ms                                                     | 143 ms: 1.01x faster                                                     |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                    |
| python_startup_no_site     | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                                    |
| regex_effbot               | 3.67 ms                                                    | 3.68 ms: 1.00x slower                                                    |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                    |
| coroutines                 | 23.2 ms                                                    | 23.3 ms: 1.01x slower                                                    |
| docutils                   | 2.83 sec                                                   | 2.86 sec: 1.01x slower                                                   |
| sqlglot_optimize           | 55.5 ms                                                    | 56.3 ms: 1.01x slower                                                    |
| django_template            | 34.8 ms                                                    | 35.3 ms: 1.02x slower                                                    |
| generators                 | 29.6 ms                                                    | 30.1 ms: 1.02x slower                                                    |
| raytrace                   | 267 ms                                                     | 271 ms: 1.02x slower                                                     |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                                     |
| logging_silent             | 105 ns                                                     | 107 ns: 1.02x slower                                                     |
| regex_dna                  | 221 ms                                                     | 226 ms: 1.02x slower                                                     |
| scimark_lu                 | 122 ms                                                     | 125 ms: 1.02x slower                                                     |
| async_generators           | 442 ms                                                     | 454 ms: 1.03x slower                                                     |
| scimark_sor                | 127 ms                                                     | 131 ms: 1.03x slower                                                     |
| typing_runtime_protocols   | 165 us                                                     | 170 us: 1.03x slower                                                     |
| hexiom                     | 6.30 ms                                                    | 6.57 ms: 1.04x slower                                                    |
| sympy_str                  | 282 ms                                                     | 295 ms: 1.05x slower                                                     |
| genshi_text                | 23.7 ms                                                    | 25.0 ms: 1.06x slower                                                    |
| sympy_expand               | 473 ms                                                     | 499 ms: 1.06x slower                                                     |
| sympy_sum                  | 156 ms                                                     | 167 ms: 1.07x slower                                                     |
| nqueens                    | 81.4 ms                                                    | 87.5 ms: 1.08x slower                                                    |
| sympy_integrate            | 20.5 ms                                                    | 22.1 ms: 1.08x slower                                                    |
| pylint                     | 317 ms                                                     | 346 ms: 1.09x slower                                                     |
| genshi_xml                 | 51.6 ms                                                    | 58.1 ms: 1.13x slower                                                    |
| deltablue                  | 3.25 ms                                                    | 3.81 ms: 1.17x slower                                                    |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                             |

Benchmark hidden because not significant (4): bench_thread_pool, dulwich_log, 2to3, coverage
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x
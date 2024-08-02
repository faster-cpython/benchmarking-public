# Results vs. 3.13.0b2

- fork: python
- ref: c15f94d6fbc960790db3
- machine: linux-aarch64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.13x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 353 ms: 1.16x slower                                                     |
| chameleon      | 8.95 ms                                                      | 10.0 ms: 1.12x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.50 sec: 1.13x slower                                                   |
| html5lib       | 66.1 ms                                                      | 72.1 ms: 1.09x slower                                                    |
| tornado_http   | 128 ms                                                       | 134 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                        | 1.11x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.24 sec: 1.03x faster                                                   |
| async_tree_io              | 1.22 sec                                                     | 1.26 sec: 1.03x slower                                                   |
| async_tree_none_tg         | 476 ms                                                       | 491 ms: 1.03x slower                                                     |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 793 ms: 1.04x slower                                                     |
| async_tree_memoization_tg  | 604 ms                                                       | 629 ms: 1.04x slower                                                     |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 828 ms: 1.05x slower                                                     |
| async_tree_none            | 492 ms                                                       | 519 ms: 1.05x slower                                                     |
| async_tree_memoization     | 645 ms                                                       | 684 ms: 1.06x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 113 ms: 1.23x slower                                                     |
| nbody          | 114 ms                                                       | 141 ms: 1.24x slower                                                     |
| Geometric mean | (ref)                                                        | 1.15x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 249 ms: 1.04x faster                                                     |
| regex_effbot   | 4.98 ms                                                      | 4.87 ms: 1.02x faster                                                    |
| regex_compile  | 128 ms                                                       | 166 ms: 1.29x slower                                                     |
| Geometric mean | (ref)                                                        | 1.05x slower                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_list        | 6.52 us                                                      | 6.62 us: 1.02x slower                                                    |
| pickle_list          | 5.27 us                                                      | 5.37 us: 1.02x slower                                                    |
| json_dumps           | 13.1 ms                                                      | 13.7 ms: 1.04x slower                                                    |
| xml_etree_process    | 80.8 ms                                                      | 87.0 ms: 1.08x slower                                                    |
| xml_etree_generate   | 114 ms                                                       | 124 ms: 1.09x slower                                                     |
| xml_etree_iterparse  | 147 ms                                                       | 162 ms: 1.10x slower                                                     |
| tomli_loads          | 2.57 sec                                                     | 3.11 sec: 1.21x slower                                                   |
| pickle_pure_python   | 359 us                                                       | 448 us: 1.25x slower                                                     |
| unpickle_pure_python | 251 us                                                       | 348 us: 1.38x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.08x slower                                                             |

Benchmark hidden because not significant (5): xml_etree_parse, pickle_dict, pickle, json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.2 ms: 1.02x slower                                                    |
| python_startup_no_site | 8.60 ms                                                      | 8.77 ms: 1.02x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 48.9 ms: 1.16x slower                                                    |
| mako            | 13.2 ms                                                      | 16.4 ms: 1.25x slower                                                    |
| genshi_xml      | 60.4 ms                                                      | 76.1 ms: 1.26x slower                                                    |
| genshi_text     | 27.4 ms                                                      | 36.2 ms: 1.32x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.24x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna                  | 259 ms                                                       | 249 ms: 1.04x faster                                                     |
| async_tree_io_tg           | 1.27 sec                                                     | 1.24 sec: 1.03x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.87 ms: 1.02x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 5.10 ms: 1.02x faster                                                    |
| unpickle_list              | 6.52 us                                                      | 6.62 us: 1.02x slower                                                    |
| logging_simple             | 7.21 us                                                      | 7.32 us: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.25 sec: 1.02x slower                                                   |
| python_startup             | 13.0 ms                                                      | 13.2 ms: 1.02x slower                                                    |
| pickle_list                | 5.27 us                                                      | 5.37 us: 1.02x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 8.77 ms: 1.02x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 596 ms: 1.02x slower                                                     |
| coverage                   | 98.4 ms                                                      | 101 ms: 1.02x slower                                                     |
| sqlite_synth               | 3.90 us                                                      | 3.99 us: 1.02x slower                                                    |
| logging_format             | 7.82 us                                                      | 8.02 us: 1.02x slower                                                    |
| pathlib                    | 22.8 ms                                                      | 23.4 ms: 1.03x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.26 sec: 1.03x slower                                                   |
| async_tree_none_tg         | 476 ms                                                       | 491 ms: 1.03x slower                                                     |
| json                       | 5.64 ms                                                      | 5.84 ms: 1.03x slower                                                    |
| create_gc_cycles           | 2.33 ms                                                      | 2.41 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 793 ms: 1.04x slower                                                     |
| async_tree_memoization_tg  | 604 ms                                                       | 629 ms: 1.04x slower                                                     |
| json_dumps                 | 13.1 ms                                                      | 13.7 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 828 ms: 1.05x slower                                                     |
| coroutines                 | 29.0 ms                                                      | 30.4 ms: 1.05x slower                                                    |
| tornado_http               | 128 ms                                                       | 134 ms: 1.05x slower                                                     |
| dask                       | 370 ms                                                       | 389 ms: 1.05x slower                                                     |
| async_tree_none            | 492 ms                                                       | 519 ms: 1.05x slower                                                     |
| async_tree_memoization     | 645 ms                                                       | 684 ms: 1.06x slower                                                     |
| bench_thread_pool          | 1.26 ms                                                      | 1.34 ms: 1.07x slower                                                    |
| mdp                        | 3.33 sec                                                     | 3.56 sec: 1.07x slower                                                   |
| flaskblogging              | 4.70 ms                                                      | 5.03 ms: 1.07x slower                                                    |
| xml_etree_process          | 80.8 ms                                                      | 87.0 ms: 1.08x slower                                                    |
| telco                      | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                    |
| generators                 | 37.1 ms                                                      | 40.2 ms: 1.08x slower                                                    |
| aiohttp                    | 1.18 ms                                                      | 1.28 ms: 1.08x slower                                                    |
| xml_etree_generate         | 114 ms                                                       | 124 ms: 1.09x slower                                                     |
| html5lib                   | 66.1 ms                                                      | 72.1 ms: 1.09x slower                                                    |
| async_generators           | 488 ms                                                       | 538 ms: 1.10x slower                                                     |
| xml_etree_iterparse        | 147 ms                                                       | 162 ms: 1.10x slower                                                     |
| pycparser                  | 1.22 sec                                                     | 1.36 sec: 1.12x slower                                                   |
| chameleon                  | 8.95 ms                                                      | 10.0 ms: 1.12x slower                                                    |
| dulwich_log                | 58.5 ms                                                      | 65.9 ms: 1.13x slower                                                    |
| mypy2                      | 767 ms                                                       | 866 ms: 1.13x slower                                                     |
| docutils                   | 3.10 sec                                                     | 3.50 sec: 1.13x slower                                                   |
| sympy_expand               | 457 ms                                                       | 521 ms: 1.14x slower                                                     |
| gunicorn                   | 1.19 ms                                                      | 1.35 ms: 1.14x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 222 us: 1.15x slower                                                     |
| raytrace                   | 297 ms                                                       | 340 ms: 1.15x slower                                                     |
| bench_mp_pool              | 7.03 ms                                                      | 8.06 ms: 1.15x slower                                                    |
| django_template            | 42.3 ms                                                      | 48.9 ms: 1.16x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 150 ms: 1.16x slower                                                     |
| 2to3                       | 305 ms                                                       | 353 ms: 1.16x slower                                                     |
| sqlglot_optimize           | 62.6 ms                                                      | 72.7 ms: 1.16x slower                                                    |
| pylint                     | 337 ms                                                       | 393 ms: 1.17x slower                                                     |
| meteor_contest             | 113 ms                                                       | 133 ms: 1.17x slower                                                     |
| richards_super             | 62.3 ms                                                      | 73.6 ms: 1.18x slower                                                    |
| sympy_str                  | 265 ms                                                       | 314 ms: 1.18x slower                                                     |
| deepcopy_reduce            | 4.04 us                                                      | 4.78 us: 1.18x slower                                                    |
| richards                   | 55.9 ms                                                      | 66.4 ms: 1.19x slower                                                    |
| sqlglot_parse              | 1.42 ms                                                      | 1.70 ms: 1.20x slower                                                    |
| deepcopy                   | 448 us                                                       | 539 us: 1.20x slower                                                     |
| sympy_sum                  | 144 ms                                                       | 173 ms: 1.21x slower                                                     |
| tomli_loads                | 2.57 sec                                                     | 3.11 sec: 1.21x slower                                                   |
| fannkuch                   | 451 ms                                                       | 547 ms: 1.21x slower                                                     |
| scimark_fft                | 445 ms                                                       | 543 ms: 1.22x slower                                                     |
| go                         | 161 ms                                                       | 196 ms: 1.22x slower                                                     |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 8.05 ms: 1.23x slower                                                    |
| pprint_pformat             | 1.93 sec                                                     | 2.38 sec: 1.23x slower                                                   |
| float                      | 91.4 ms                                                      | 113 ms: 1.23x slower                                                     |
| crypto_pyaes               | 82.0 ms                                                      | 101 ms: 1.24x slower                                                     |
| nbody                      | 114 ms                                                       | 141 ms: 1.24x slower                                                     |
| sympy_integrate            | 20.9 ms                                                      | 26.0 ms: 1.24x slower                                                    |
| pprint_safe_repr           | 933 ms                                                       | 1.16 sec: 1.25x slower                                                   |
| scimark_sor                | 159 ms                                                       | 199 ms: 1.25x slower                                                     |
| chaos                      | 68.3 ms                                                      | 85.2 ms: 1.25x slower                                                    |
| mako                       | 13.2 ms                                                      | 16.4 ms: 1.25x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 448 us: 1.25x slower                                                     |
| sqlglot_transpile          | 1.71 ms                                                      | 2.15 ms: 1.26x slower                                                    |
| genshi_xml                 | 60.4 ms                                                      | 76.1 ms: 1.26x slower                                                    |
| pyflate                    | 557 ms                                                       | 706 ms: 1.27x slower                                                     |
| regex_compile              | 128 ms                                                       | 166 ms: 1.29x slower                                                     |
| spectral_norm              | 141 ms                                                       | 183 ms: 1.30x slower                                                     |
| nqueens                    | 98.9 ms                                                      | 128 ms: 1.30x slower                                                     |
| genshi_text                | 27.4 ms                                                      | 36.2 ms: 1.32x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 5.13 ms: 1.32x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 348 us: 1.38x slower                                                     |
| scimark_monte_carlo        | 82.3 ms                                                      | 116 ms: 1.41x slower                                                     |
| logging_silent             | 133 ns                                                       | 188 ns: 1.41x slower                                                     |
| deepcopy_memo              | 50.8 us                                                      | 72.0 us: 1.42x slower                                                    |
| comprehensions             | 20.5 us                                                      | 29.6 us: 1.44x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 10.5 ms: 1.48x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 211 ms: 1.50x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.13x slower                                                             |

Benchmark hidden because not significant (9): xml_etree_parse, regex_v8, pickle_dict, pickle, asyncio_websockets, json_loads, unpickle, pidigits, thrift
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.01x
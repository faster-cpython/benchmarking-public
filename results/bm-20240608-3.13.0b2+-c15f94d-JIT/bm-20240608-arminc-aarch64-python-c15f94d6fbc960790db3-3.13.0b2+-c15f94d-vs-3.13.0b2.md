# Results vs. 3.13.0b2

- fork: python
- ref: c15f94d6fbc960790db3
- machine: linux-aarch64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 362 ms: 1.19x slower                                                     |
| chameleon      | 8.95 ms                                                      | 9.09 ms: 1.02x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.54 sec: 1.14x slower                                                   |
| html5lib       | 66.1 ms                                                      | 72.6 ms: 1.10x slower                                                    |
| tornado_http   | 128 ms                                                       | 142 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                        | 1.11x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.22 sec: 1.04x faster                                                   |
| async_tree_none            | 492 ms                                                       | 507 ms: 1.03x slower                                                     |
| async_tree_memoization     | 645 ms                                                       | 668 ms: 1.04x slower                                                     |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 827 ms: 1.05x slower                                                     |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 798 ms: 1.05x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                             |

Benchmark hidden because not significant (3): async_tree_io, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 90.0 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                        | 1.00x faster                                                             |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.2 ms: 1.03x faster                                                    |
| regex_compile  | 128 ms                                                       | 178 ms: 1.39x slower                                                     |
| Geometric mean | (ref)                                                        | 1.08x slower                                                             |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 13.1 ms                                                      | 13.0 ms: 1.00x faster                                                    |
| tomli_loads          | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                   |
| unpickle_pure_python | 251 us                                                       | 277 us: 1.10x slower                                                     |
| pickle_pure_python   | 359 us                                                       | 398 us: 1.11x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                             |

Benchmark hidden because not significant (10): xml_etree_parse, xml_etree_process, unpickle, xml_etree_generate, pickle_dict, pickle, pickle_list, json_loads, unpickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 15.5 ms: 1.20x slower                                                    |
| python_startup_no_site | 8.60 ms                                                      | 11.1 ms: 1.29x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.24x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 13.0 ms: 1.01x faster                                                    |
| django_template | 42.3 ms                                                      | 50.5 ms: 1.19x slower                                                    |
| genshi_text     | 27.4 ms                                                      | 33.9 ms: 1.23x slower                                                    |
| genshi_xml      | 60.4 ms                                                      | 82.6 ms: 1.37x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.19x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.22 sec: 1.04x faster                                                   |
| deepcopy_memo              | 50.8 us                                                      | 49.2 us: 1.03x faster                                                    |
| regex_v8                   | 31.1 ms                                                      | 30.2 ms: 1.03x faster                                                    |
| sqlite_synth               | 3.90 us                                                      | 3.81 us: 1.02x faster                                                    |
| float                      | 91.4 ms                                                      | 90.0 ms: 1.02x faster                                                    |
| mako                       | 13.2 ms                                                      | 13.0 ms: 1.01x faster                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.0 ms: 1.00x faster                                                    |
| coverage                   | 98.4 ms                                                      | 99.5 ms: 1.01x slower                                                    |
| asyncio_websockets         | 657 ms                                                       | 666 ms: 1.01x slower                                                     |
| chameleon                  | 8.95 ms                                                      | 9.09 ms: 1.02x slower                                                    |
| pathlib                    | 22.8 ms                                                      | 23.2 ms: 1.02x slower                                                    |
| logging_format             | 7.82 us                                                      | 7.98 us: 1.02x slower                                                    |
| logging_simple             | 7.21 us                                                      | 7.35 us: 1.02x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                   |
| fannkuch                   | 451 ms                                                       | 462 ms: 1.02x slower                                                     |
| create_gc_cycles           | 2.33 ms                                                      | 2.39 ms: 1.02x slower                                                    |
| meteor_contest             | 113 ms                                                       | 117 ms: 1.03x slower                                                     |
| async_tree_none            | 492 ms                                                       | 507 ms: 1.03x slower                                                     |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.28 sec: 1.03x slower                                                   |
| scimark_fft                | 445 ms                                                       | 460 ms: 1.03x slower                                                     |
| async_tree_memoization     | 645 ms                                                       | 668 ms: 1.04x slower                                                     |
| mdp                        | 3.33 sec                                                     | 3.45 sec: 1.04x slower                                                   |
| logging_silent             | 133 ns                                                       | 139 ns: 1.04x slower                                                     |
| spectral_norm              | 141 ms                                                       | 147 ms: 1.05x slower                                                     |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 827 ms: 1.05x slower                                                     |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 798 ms: 1.05x slower                                                     |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.89 ms: 1.05x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.33 ms: 1.06x slower                                                    |
| dask                       | 370 ms                                                       | 392 ms: 1.06x slower                                                     |
| generators                 | 37.1 ms                                                      | 39.7 ms: 1.07x slower                                                    |
| async_generators           | 488 ms                                                       | 522 ms: 1.07x slower                                                     |
| pyflate                    | 557 ms                                                       | 596 ms: 1.07x slower                                                     |
| asyncio_tcp                | 584 ms                                                       | 630 ms: 1.08x slower                                                     |
| typing_runtime_protocols   | 193 us                                                       | 209 us: 1.08x slower                                                     |
| crypto_pyaes               | 82.0 ms                                                      | 88.8 ms: 1.08x slower                                                    |
| raytrace                   | 297 ms                                                       | 322 ms: 1.09x slower                                                     |
| flaskblogging              | 4.70 ms                                                      | 5.14 ms: 1.09x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 90.0 ms: 1.09x slower                                                    |
| scimark_sor                | 159 ms                                                       | 175 ms: 1.10x slower                                                     |
| html5lib                   | 66.1 ms                                                      | 72.6 ms: 1.10x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 142 ms: 1.10x slower                                                     |
| unpickle_pure_python       | 251 us                                                       | 277 us: 1.10x slower                                                     |
| deepcopy                   | 448 us                                                       | 495 us: 1.10x slower                                                     |
| sqlglot_optimize           | 62.6 ms                                                      | 69.3 ms: 1.11x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 398 us: 1.11x slower                                                     |
| tornado_http               | 128 ms                                                       | 142 ms: 1.11x slower                                                     |
| sqlglot_parse              | 1.42 ms                                                      | 1.58 ms: 1.11x slower                                                    |
| go                         | 161 ms                                                       | 179 ms: 1.11x slower                                                     |
| aiohttp                    | 1.18 ms                                                      | 1.32 ms: 1.12x slower                                                    |
| pycparser                  | 1.22 sec                                                     | 1.38 sec: 1.13x slower                                                   |
| comprehensions             | 20.5 us                                                      | 23.1 us: 1.13x slower                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 4.60 us: 1.14x slower                                                    |
| docutils                   | 3.10 sec                                                     | 3.54 sec: 1.14x slower                                                   |
| gunicorn                   | 1.19 ms                                                      | 1.36 ms: 1.15x slower                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 8.22 ms: 1.17x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 2.01 ms: 1.17x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 4.55 ms: 1.17x slower                                                    |
| nqueens                    | 98.9 ms                                                      | 117 ms: 1.18x slower                                                     |
| 2to3                       | 305 ms                                                       | 362 ms: 1.19x slower                                                     |
| pprint_safe_repr           | 933 ms                                                       | 1.11 sec: 1.19x slower                                                   |
| django_template            | 42.3 ms                                                      | 50.5 ms: 1.19x slower                                                    |
| sympy_expand               | 457 ms                                                       | 547 ms: 1.20x slower                                                     |
| python_startup             | 13.0 ms                                                      | 15.5 ms: 1.20x slower                                                    |
| pprint_pformat             | 1.93 sec                                                     | 2.32 sec: 1.20x slower                                                   |
| sympy_str                  | 265 ms                                                       | 323 ms: 1.22x slower                                                     |
| dulwich_log                | 58.5 ms                                                      | 71.8 ms: 1.23x slower                                                    |
| sympy_integrate            | 20.9 ms                                                      | 25.6 ms: 1.23x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 33.9 ms: 1.23x slower                                                    |
| mypy2                      | 767 ms                                                       | 948 ms: 1.24x slower                                                     |
| pylint                     | 337 ms                                                       | 421 ms: 1.25x slower                                                     |
| hexiom                     | 7.08 ms                                                      | 9.05 ms: 1.28x slower                                                    |
| sympy_sum                  | 144 ms                                                       | 185 ms: 1.29x slower                                                     |
| chaos                      | 68.3 ms                                                      | 88.0 ms: 1.29x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 11.1 ms: 1.29x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 184 ms: 1.30x slower                                                     |
| genshi_xml                 | 60.4 ms                                                      | 82.6 ms: 1.37x slower                                                    |
| regex_compile              | 128 ms                                                       | 178 ms: 1.39x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                             |

Benchmark hidden because not significant (24): xml_etree_parse, xml_etree_process, unpickle, richards, gc_traversal, regex_effbot, coroutines, xml_etree_generate, pidigits, nbody, pickle_dict, async_tree_io, pickle, pickle_list, json_loads, regex_dna, richards_super, async_tree_none_tg, unpickle_list, telco, json, thrift, xml_etree_iterparse, async_tree_memoization_tg
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.09x
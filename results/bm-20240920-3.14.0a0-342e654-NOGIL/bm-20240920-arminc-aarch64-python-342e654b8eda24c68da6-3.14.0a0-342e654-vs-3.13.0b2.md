# Results vs. 3.13.0b2

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-aarch64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.50x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 508 ms: 1.67x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.93 sec: 1.27x slower                                                  |
| html5lib       | 66.1 ms                                                      | 118 ms: 1.79x slower                                                    |
| tornado_http   | 128 ms                                                       | 203 ms: 1.59x slower                                                    |
| Geometric mean | (ref)                                                        | 1.56x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.34 sec: 1.05x slower                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.37 sec: 1.12x slower                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 862 ms: 1.13x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 897 ms: 1.13x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 689 ms: 1.14x slower                                                    |
| async_tree_memoization     | 645 ms                                                       | 735 ms: 1.14x slower                                                    |
| async_tree_none_tg         | 476 ms                                                       | 565 ms: 1.19x slower                                                    |
| async_tree_none            | 492 ms                                                       | 604 ms: 1.23x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.14x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 205 ms: 2.24x slower                                                    |
| nbody          | 114 ms                                                       | 279 ms: 2.44x slower                                                    |
| Geometric mean | (ref)                                                        | 1.76x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.98 ms                                                      | 4.42 ms: 1.13x faster                                                   |
| regex_dna      | 259 ms                                                       | 254 ms: 1.02x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 32.5 ms: 1.05x slower                                                   |
| regex_compile  | 128 ms                                                       | 248 ms: 1.94x slower                                                    |
| Geometric mean | (ref)                                                        | 1.15x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 191 ms                                                       | 182 ms: 1.05x faster                                                    |
| pickle               | 13.4 us                                                      | 13.1 us: 1.02x faster                                                   |
| pickle_list          | 5.27 us                                                      | 5.41 us: 1.03x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 152 ms: 1.04x slower                                                    |
| pickle_dict          | 37.6 us                                                      | 39.4 us: 1.05x slower                                                   |
| unpickle             | 19.8 us                                                      | 21.3 us: 1.08x slower                                                   |
| unpickle_list        | 6.52 us                                                      | 7.12 us: 1.09x slower                                                   |
| json_loads           | 32.1 us                                                      | 37.9 us: 1.18x slower                                                   |
| json_dumps           | 13.1 ms                                                      | 17.8 ms: 1.36x slower                                                   |
| xml_etree_generate   | 114 ms                                                       | 155 ms: 1.36x slower                                                    |
| xml_etree_process    | 80.8 ms                                                      | 125 ms: 1.55x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 4.11 sec: 1.60x slower                                                  |
| unpickle_pure_python | 251 us                                                       | 526 us: 2.09x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 754 us: 2.10x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.27x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 18.1 ms: 1.40x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 12.1 ms: 1.41x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.40x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.4 ms                                                      | 101 ms: 1.67x slower                                                    |
| django_template | 42.3 ms                                                      | 79.0 ms: 1.87x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 52.1 ms: 1.90x slower                                                   |
| mako            | 13.2 ms                                                      | 28.4 ms: 2.16x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.89x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 5.17 ms                                                      | 3.44 ms: 1.51x faster                                                   |
| create_gc_cycles           | 2.33 ms                                                      | 1.61 ms: 1.44x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.42 ms: 1.13x faster                                                   |
| xml_etree_parse            | 191 ms                                                       | 182 ms: 1.05x faster                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 6.69 ms: 1.05x faster                                                   |
| pickle                     | 13.4 us                                                      | 13.1 us: 1.02x faster                                                   |
| regex_dna                  | 259 ms                                                       | 254 ms: 1.02x faster                                                    |
| pickle_list                | 5.27 us                                                      | 5.41 us: 1.03x slower                                                   |
| asyncio_websockets         | 657 ms                                                       | 676 ms: 1.03x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                       | 152 ms: 1.04x slower                                                    |
| pickle_dict                | 37.6 us                                                      | 39.4 us: 1.05x slower                                                   |
| sqlite_synth               | 3.90 us                                                      | 4.08 us: 1.05x slower                                                   |
| regex_v8                   | 31.1 ms                                                      | 32.5 ms: 1.05x slower                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.34 sec: 1.05x slower                                                  |
| unpickle                   | 19.8 us                                                      | 21.3 us: 1.08x slower                                                   |
| unpickle_list              | 6.52 us                                                      | 7.12 us: 1.09x slower                                                   |
| async_tree_io              | 1.22 sec                                                     | 1.37 sec: 1.12x slower                                                  |
| pathlib                    | 22.8 ms                                                      | 25.7 ms: 1.13x slower                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 862 ms: 1.13x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 897 ms: 1.13x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 689 ms: 1.14x slower                                                    |
| async_tree_memoization     | 645 ms                                                       | 735 ms: 1.14x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 668 ms: 1.14x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.59 sec: 1.17x slower                                                  |
| json_loads                 | 32.1 us                                                      | 37.9 us: 1.18x slower                                                   |
| deepcopy                   | 448 us                                                       | 531 us: 1.18x slower                                                    |
| async_tree_none_tg         | 476 ms                                                       | 565 ms: 1.19x slower                                                    |
| json                       | 5.64 ms                                                      | 6.77 ms: 1.20x slower                                                   |
| async_tree_none            | 492 ms                                                       | 604 ms: 1.23x slower                                                    |
| docutils                   | 3.10 sec                                                     | 3.93 sec: 1.27x slower                                                  |
| telco                      | 10.0 ms                                                      | 12.9 ms: 1.28x slower                                                   |
| mdp                        | 3.33 sec                                                     | 4.28 sec: 1.29x slower                                                  |
| scimark_fft                | 445 ms                                                       | 574 ms: 1.29x slower                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 8.66 ms: 1.32x slower                                                   |
| deepcopy_memo              | 50.8 us                                                      | 67.9 us: 1.34x slower                                                   |
| async_generators           | 488 ms                                                       | 653 ms: 1.34x slower                                                    |
| coverage                   | 98.4 ms                                                      | 133 ms: 1.36x slower                                                    |
| coroutines                 | 29.0 ms                                                      | 39.3 ms: 1.36x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 17.8 ms: 1.36x slower                                                   |
| xml_etree_generate         | 114 ms                                                       | 155 ms: 1.36x slower                                                    |
| python_startup             | 13.0 ms                                                      | 18.1 ms: 1.40x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 12.1 ms: 1.41x slower                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 5.76 us: 1.43x slower                                                   |
| meteor_contest             | 113 ms                                                       | 166 ms: 1.46x slower                                                    |
| pylint                     | 337 ms                                                       | 499 ms: 1.48x slower                                                    |
| nqueens                    | 98.9 ms                                                      | 149 ms: 1.51x slower                                                    |
| xml_etree_process          | 80.8 ms                                                      | 125 ms: 1.55x slower                                                    |
| generators                 | 37.1 ms                                                      | 57.8 ms: 1.56x slower                                                   |
| tornado_http               | 128 ms                                                       | 203 ms: 1.59x slower                                                    |
| bpe_tokeniser              | 5.83 sec                                                     | 9.28 sec: 1.59x slower                                                  |
| spectral_norm              | 141 ms                                                       | 225 ms: 1.59x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 4.11 sec: 1.60x slower                                                  |
| dulwich_log                | 58.5 ms                                                      | 93.6 ms: 1.60x slower                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 2.01 ms: 1.60x slower                                                   |
| pycparser                  | 1.22 sec                                                     | 2.00 sec: 1.64x slower                                                  |
| sympy_integrate            | 20.9 ms                                                      | 34.6 ms: 1.66x slower                                                   |
| 2to3                       | 305 ms                                                       | 508 ms: 1.67x slower                                                    |
| fannkuch                   | 451 ms                                                       | 753 ms: 1.67x slower                                                    |
| genshi_xml                 | 60.4 ms                                                      | 101 ms: 1.67x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 324 us: 1.68x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 217 ms: 1.68x slower                                                    |
| thrift                     | 962 us                                                       | 1.62 ms: 1.69x slower                                                   |
| crypto_pyaes               | 82.0 ms                                                      | 139 ms: 1.69x slower                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 110 ms: 1.76x slower                                                    |
| pprint_pformat             | 1.93 sec                                                     | 3.43 sec: 1.78x slower                                                  |
| pprint_safe_repr           | 933 ms                                                       | 1.67 sec: 1.79x slower                                                  |
| html5lib                   | 66.1 ms                                                      | 118 ms: 1.79x slower                                                    |
| pyflate                    | 557 ms                                                       | 1.00 sec: 1.80x slower                                                  |
| django_template            | 42.3 ms                                                      | 79.0 ms: 1.87x slower                                                   |
| genshi_text                | 27.4 ms                                                      | 52.1 ms: 1.90x slower                                                   |
| sympy_str                  | 265 ms                                                       | 504 ms: 1.90x slower                                                    |
| regex_compile              | 128 ms                                                       | 248 ms: 1.94x slower                                                    |
| logging_simple             | 7.21 us                                                      | 14.1 us: 1.95x slower                                                   |
| comprehensions             | 20.5 us                                                      | 40.2 us: 1.96x slower                                                   |
| logging_format             | 7.82 us                                                      | 15.4 us: 1.97x slower                                                   |
| sympy_expand               | 457 ms                                                       | 936 ms: 2.05x slower                                                    |
| richards                   | 55.9 ms                                                      | 115 ms: 2.06x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 526 us: 2.09x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 754 us: 2.10x slower                                                    |
| scimark_sor                | 159 ms                                                       | 337 ms: 2.12x slower                                                    |
| logging_silent             | 133 ns                                                       | 284 ns: 2.13x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 176 ms: 2.14x slower                                                    |
| sympy_sum                  | 144 ms                                                       | 310 ms: 2.16x slower                                                    |
| mako                       | 13.2 ms                                                      | 28.4 ms: 2.16x slower                                                   |
| richards_super             | 62.3 ms                                                      | 135 ms: 2.17x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 15.4 ms: 2.17x slower                                                   |
| float                      | 91.4 ms                                                      | 205 ms: 2.24x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 330 ms: 2.34x slower                                                    |
| chaos                      | 68.3 ms                                                      | 161 ms: 2.36x slower                                                    |
| go                         | 161 ms                                                       | 384 ms: 2.39x slower                                                    |
| nbody                      | 114 ms                                                       | 279 ms: 2.44x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 4.28 ms: 2.50x slower                                                   |
| sqlglot_parse              | 1.42 ms                                                      | 3.72 ms: 2.61x slower                                                   |
| raytrace                   | 297 ms                                                       | 821 ms: 2.77x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 12.4 ms: 3.19x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.50x slower                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240920-3.14.0a0-342e654-NOGIL/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.41x
- 95% likely to have a slowdown of 1.37x
- 99% likely to have a slowdown of 1.33x

# Memory
- memory change: 1.16x
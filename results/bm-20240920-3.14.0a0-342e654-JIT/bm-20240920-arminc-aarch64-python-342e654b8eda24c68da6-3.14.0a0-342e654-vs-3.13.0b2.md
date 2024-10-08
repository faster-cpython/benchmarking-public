# Results vs. 3.13.0b2

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-aarch64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 382 ms: 1.25x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.94 sec: 1.27x slower                                                  |
| html5lib       | 66.1 ms                                                      | 71.9 ms: 1.09x slower                                                   |
| tornado_http   | 128 ms                                                       | 150 ms: 1.17x slower                                                    |
| Geometric mean | (ref)                                                        | 1.19x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 426 ms: 1.12x faster                                                    |
| async_tree_none            | 492 ms                                                       | 442 ms: 1.11x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 589 ms: 1.10x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.09x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 556 ms: 1.09x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.06x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 748 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 735 ms: 1.04x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.08x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 87.5 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 252 ms: 1.03x faster                                                    |
| regex_compile  | 128 ms                                                       | 196 ms: 1.53x slower                                                    |
| Geometric mean | (ref)                                                        | 1.10x slower                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle             | 19.8 us                                                      | 19.3 us: 1.03x faster                                                   |
| xml_etree_generate   | 114 ms                                                       | 111 ms: 1.02x faster                                                    |
| json_loads           | 32.1 us                                                      | 31.4 us: 1.02x faster                                                   |
| unpickle_list        | 6.52 us                                                      | 6.42 us: 1.02x faster                                                   |
| pickle_list          | 5.27 us                                                      | 5.20 us: 1.01x faster                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 148 ms: 1.01x slower                                                    |
| pickle_dict          | 37.6 us                                                      | 38.3 us: 1.02x slower                                                   |
| pickle               | 13.4 us                                                      | 13.7 us: 1.02x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| json_dumps           | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| unpickle_pure_python | 251 us                                                       | 267 us: 1.06x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 392 us: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 8.79 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                                   |
| django_template | 42.3 ms                                                      | 51.4 ms: 1.21x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 35.0 ms: 1.28x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 80.8 ms: 1.34x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.19x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 37.6 us: 1.35x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 426 ms: 1.12x faster                                                    |
| deepcopy                   | 448 us                                                       | 401 us: 1.12x faster                                                    |
| async_tree_none            | 492 ms                                                       | 442 ms: 1.11x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 589 ms: 1.10x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.09x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 556 ms: 1.09x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.06x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 748 ms: 1.06x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.83 us: 1.05x faster                                                   |
| pathlib                    | 22.8 ms                                                      | 21.7 ms: 1.05x faster                                                   |
| scimark_sor                | 159 ms                                                       | 152 ms: 1.05x faster                                                    |
| float                      | 91.4 ms                                                      | 87.5 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 735 ms: 1.04x faster                                                    |
| regex_dna                  | 259 ms                                                       | 252 ms: 1.03x faster                                                    |
| unpickle                   | 19.8 us                                                      | 19.3 us: 1.03x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 111 ms: 1.02x faster                                                    |
| json_loads                 | 32.1 us                                                      | 31.4 us: 1.02x faster                                                   |
| mako                       | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                                   |
| coroutines                 | 29.0 ms                                                      | 28.5 ms: 1.02x faster                                                   |
| sqlite_synth               | 3.90 us                                                      | 3.84 us: 1.02x faster                                                   |
| unpickle_list              | 6.52 us                                                      | 6.42 us: 1.02x faster                                                   |
| pickle_list                | 5.27 us                                                      | 5.20 us: 1.01x faster                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 148 ms: 1.01x slower                                                    |
| python_startup             | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| pickle_dict                | 37.6 us                                                      | 38.3 us: 1.02x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 8.79 ms: 1.02x slower                                                   |
| pickle                     | 13.4 us                                                      | 13.7 us: 1.02x slower                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.27 sec: 1.02x slower                                                  |
| bpe_tokeniser              | 5.83 sec                                                     | 5.98 sec: 1.03x slower                                                  |
| tomli_loads                | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| logging_silent             | 133 ns                                                       | 137 ns: 1.03x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| scimark_fft                | 445 ms                                                       | 459 ms: 1.03x slower                                                    |
| spectral_norm              | 141 ms                                                       | 146 ms: 1.03x slower                                                    |
| logging_simple             | 7.21 us                                                      | 7.46 us: 1.04x slower                                                   |
| coverage                   | 98.4 ms                                                      | 102 ms: 1.04x slower                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.85 ms: 1.05x slower                                                   |
| logging_format             | 7.82 us                                                      | 8.20 us: 1.05x slower                                                   |
| async_generators           | 488 ms                                                       | 512 ms: 1.05x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 148 ms: 1.05x slower                                                    |
| telco                      | 10.0 ms                                                      | 10.6 ms: 1.06x slower                                                   |
| mdp                        | 3.33 sec                                                     | 3.52 sec: 1.06x slower                                                  |
| unpickle_pure_python       | 251 us                                                       | 267 us: 1.06x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.35 ms: 1.07x slower                                                   |
| asyncio_tcp                | 584 ms                                                       | 629 ms: 1.08x slower                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 7.57 ms: 1.08x slower                                                   |
| html5lib                   | 66.1 ms                                                      | 71.9 ms: 1.09x slower                                                   |
| pickle_pure_python         | 359 us                                                       | 392 us: 1.09x slower                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 89.7 ms: 1.09x slower                                                   |
| meteor_contest             | 113 ms                                                       | 124 ms: 1.10x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 213 us: 1.10x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 92.6 ms: 1.13x slower                                                   |
| fannkuch                   | 451 ms                                                       | 508 ms: 1.13x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 4.39 ms: 1.13x slower                                                   |
| sqlglot_normalize          | 129 ms                                                       | 150 ms: 1.16x slower                                                    |
| tornado_http               | 128 ms                                                       | 150 ms: 1.17x slower                                                    |
| raytrace                   | 297 ms                                                       | 348 ms: 1.17x slower                                                    |
| pyflate                    | 557 ms                                                       | 657 ms: 1.18x slower                                                    |
| go                         | 161 ms                                                       | 190 ms: 1.18x slower                                                    |
| richards                   | 55.9 ms                                                      | 66.3 ms: 1.19x slower                                                   |
| comprehensions             | 20.5 us                                                      | 24.5 us: 1.19x slower                                                   |
| django_template            | 42.3 ms                                                      | 51.4 ms: 1.21x slower                                                   |
| richards_super             | 62.3 ms                                                      | 75.9 ms: 1.22x slower                                                   |
| sqlglot_parse              | 1.42 ms                                                      | 1.76 ms: 1.24x slower                                                   |
| pycparser                  | 1.22 sec                                                     | 1.53 sec: 1.25x slower                                                  |
| 2to3                       | 305 ms                                                       | 382 ms: 1.25x slower                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 78.5 ms: 1.25x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 126 ms: 1.27x slower                                                    |
| docutils                   | 3.10 sec                                                     | 3.94 sec: 1.27x slower                                                  |
| genshi_text                | 27.4 ms                                                      | 35.0 ms: 1.28x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 2.23 ms: 1.30x slower                                                   |
| pprint_safe_repr           | 933 ms                                                       | 1.25 sec: 1.33x slower                                                  |
| genshi_xml                 | 60.4 ms                                                      | 80.8 ms: 1.34x slower                                                   |
| sympy_expand               | 457 ms                                                       | 613 ms: 1.34x slower                                                    |
| chaos                      | 68.3 ms                                                      | 92.2 ms: 1.35x slower                                                   |
| pprint_pformat             | 1.93 sec                                                     | 2.61 sec: 1.35x slower                                                  |
| sympy_integrate            | 20.9 ms                                                      | 28.5 ms: 1.37x slower                                                   |
| sympy_str                  | 265 ms                                                       | 369 ms: 1.39x slower                                                    |
| dulwich_log                | 58.5 ms                                                      | 82.0 ms: 1.40x slower                                                   |
| pylint                     | 337 ms                                                       | 479 ms: 1.42x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 10.3 ms: 1.46x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 211 ms: 1.47x slower                                                    |
| regex_compile              | 128 ms                                                       | 196 ms: 1.53x slower                                                    |
| generators                 | 37.1 ms                                                      | 57.6 ms: 1.55x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                            |

Benchmark hidden because not significant (11): xml_etree_parse, gc_traversal, create_gc_cycles, regex_effbot, xml_etree_process, pidigits, nbody, regex_v8, json, thrift, asyncio_websockets
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.09x
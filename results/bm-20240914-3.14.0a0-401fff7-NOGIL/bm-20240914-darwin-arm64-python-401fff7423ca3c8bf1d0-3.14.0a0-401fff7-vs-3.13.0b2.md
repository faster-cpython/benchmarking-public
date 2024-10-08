# Results vs. 3.13.0b2

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: darwin-arm64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.40x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x slower
- Memory change: 0.55x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 249 ms: 1.55x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.78 sec: 1.24x slower                                                |
| html5lib       | 31.2 ms                                                    | 51.8 ms: 1.66x slower                                                 |
| tornado_http   | 66.7 ms                                                    | 103 ms: 1.54x slower                                                  |
| Geometric mean | (ref)                                                      | 1.49x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io_tg           | 768 ms                                                     | 477 ms: 1.61x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 498 ms: 1.54x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 515 ms: 1.10x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 541 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 467 ms: 1.04x slower                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 494 ms: 1.06x slower                                                  |
| async_tree_none_tg               | 198 ms                                                     | 213 ms: 1.08x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 399 ms: 1.12x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 370 ms: 1.12x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 271 ms: 1.13x slower                                                  |
| async_tree_memoization           | 260 ms                                                     | 296 ms: 1.14x slower                                                  |
| async_tree_none                  | 209 ms                                                     | 239 ms: 1.14x slower                                                  |
| async_tree_eager_memoization     | 152 ms                                                     | 188 ms: 1.23x slower                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 162 ms: 1.29x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 107 ms: 1.78x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 76.3 ms: 1.85x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.09x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| float          | 48.6 ms                                                    | 97.7 ms: 2.01x slower                                                 |
| nbody          | 59.6 ms                                                    | 157 ms: 2.64x slower                                                  |
| Geometric mean | (ref)                                                      | 1.74x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 149 ms                                                     | 139 ms: 1.08x faster                                                  |
| regex_effbot   | 2.58 ms                                                    | 2.45 ms: 1.06x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 17.2 ms: 1.00x faster                                                 |
| regex_compile  | 68.5 ms                                                    | 121 ms: 1.77x slower                                                  |
| Geometric mean | (ref)                                                      | 1.12x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle               | 7.48 us                                                    | 7.01 us: 1.07x faster                                                 |
| pickle_list          | 2.96 us                                                    | 2.89 us: 1.02x faster                                                 |
| xml_etree_parse      | 106 ms                                                     | 105 ms: 1.01x faster                                                  |
| pickle_dict          | 18.3 us                                                    | 18.4 us: 1.01x slower                                                 |
| xml_etree_iterparse  | 71.5 ms                                                    | 77.1 ms: 1.08x slower                                                 |
| unpickle             | 9.12 us                                                    | 9.84 us: 1.08x slower                                                 |
| unpickle_list        | 2.88 us                                                    | 3.22 us: 1.12x slower                                                 |
| json_loads           | 16.8 us                                                    | 19.2 us: 1.14x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 7.92 ms: 1.27x slower                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 70.1 ms: 1.33x slower                                                 |
| tomli_loads          | 1.47 sec                                                   | 2.03 sec: 1.39x slower                                                |
| xml_etree_process    | 37.1 ms                                                    | 58.3 ms: 1.57x slower                                                 |
| unpickle_pure_python | 141 us                                                     | 265 us: 1.89x slower                                                  |
| pickle_pure_python   | 179 us                                                     | 348 us: 1.95x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.23x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 15.6 ms: 1.26x slower                                                 |
| python_startup         | 15.2 ms                                                    | 19.2 ms: 1.26x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.26x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 29.9 ms                                                    | 50.2 ms: 1.68x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 25.3 ms: 1.82x slower                                                 |
| django_template | 19.4 ms                                                    | 35.9 ms: 1.85x slower                                                 |
| mako            | 6.99 ms                                                    | 13.5 ms: 1.93x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.82x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io_tg           | 768 ms                                                     | 477 ms: 1.61x faster                                                  |
| sqlglot_normalize                | 166 ms                                                     | 105 ms: 1.58x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 498 ms: 1.54x faster                                                  |
| create_gc_cycles                 | 897 us                                                     | 699 us: 1.28x faster                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.06 ms: 1.19x faster                                                 |
| asyncio_tcp                      | 402 ms                                                     | 353 ms: 1.14x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 515 ms: 1.10x faster                                                  |
| regex_dna                        | 149 ms                                                     | 139 ms: 1.08x faster                                                  |
| pickle                           | 7.48 us                                                    | 7.01 us: 1.07x faster                                                 |
| regex_effbot                     | 2.58 ms                                                    | 2.45 ms: 1.06x faster                                                 |
| async_tree_io                    | 563 ms                                                     | 541 ms: 1.04x faster                                                  |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.24 sec: 1.04x faster                                                |
| pickle_list                      | 2.96 us                                                    | 2.89 us: 1.02x faster                                                 |
| asyncio_websockets               | 409 ms                                                     | 405 ms: 1.01x faster                                                  |
| xml_etree_parse                  | 106 ms                                                     | 105 ms: 1.01x faster                                                  |
| sqlite_synth                     | 1.55 us                                                    | 1.54 us: 1.01x faster                                                 |
| pidigits                         | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| regex_v8                         | 17.3 ms                                                    | 17.2 ms: 1.00x faster                                                 |
| pickle_dict                      | 18.3 us                                                    | 18.4 us: 1.01x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 467 ms: 1.04x slower                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 494 ms: 1.06x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 77.1 ms: 1.08x slower                                                 |
| unpickle                         | 9.12 us                                                    | 9.84 us: 1.08x slower                                                 |
| async_tree_none_tg               | 198 ms                                                     | 213 ms: 1.08x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 399 ms: 1.12x slower                                                  |
| unpickle_list                    | 2.88 us                                                    | 3.22 us: 1.12x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 370 ms: 1.12x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 271 ms: 1.13x slower                                                  |
| async_tree_memoization           | 260 ms                                                     | 296 ms: 1.14x slower                                                  |
| json_loads                       | 16.8 us                                                    | 19.2 us: 1.14x slower                                                 |
| async_tree_none                  | 209 ms                                                     | 239 ms: 1.14x slower                                                  |
| pathlib                          | 23.3 ms                                                    | 26.7 ms: 1.15x slower                                                 |
| json                             | 2.93 ms                                                    | 3.41 ms: 1.16x slower                                                 |
| async_generators                 | 281 ms                                                     | 332 ms: 1.18x slower                                                  |
| mdp                              | 1.53 sec                                                   | 1.84 sec: 1.20x slower                                                |
| bench_mp_pool                    | 47.2 ms                                                    | 56.8 ms: 1.20x slower                                                 |
| deepcopy                         | 204 us                                                     | 249 us: 1.22x slower                                                  |
| async_tree_eager_memoization     | 152 ms                                                     | 188 ms: 1.23x slower                                                  |
| docutils                         | 1.44 sec                                                   | 1.78 sec: 1.24x slower                                                |
| python_startup_no_site           | 12.3 ms                                                    | 15.6 ms: 1.26x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 19.2 ms: 1.26x slower                                                 |
| coverage                         | 45.0 ms                                                    | 56.9 ms: 1.27x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 7.92 ms: 1.27x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 89.5 ms: 1.27x slower                                                 |
| telco                            | 4.60 ms                                                    | 5.90 ms: 1.28x slower                                                 |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 162 ms: 1.29x slower                                                  |
| pylint                           | 170 ms                                                     | 220 ms: 1.30x slower                                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 4.03 sec: 1.32x slower                                                |
| xml_etree_generate               | 52.7 ms                                                    | 70.1 ms: 1.33x slower                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 2.49 us: 1.37x slower                                                 |
| tomli_loads                      | 1.47 sec                                                   | 2.03 sec: 1.39x slower                                                |
| deepcopy_memo                    | 22.6 us                                                    | 31.6 us: 1.40x slower                                                 |
| fannkuch                         | 248 ms                                                     | 358 ms: 1.44x slower                                                  |
| nqueens                          | 52.2 ms                                                    | 76.1 ms: 1.46x slower                                                 |
| pycparser                        | 632 ms                                                     | 935 ms: 1.48x slower                                                  |
| dulwich_log                      | 27.6 ms                                                    | 41.2 ms: 1.50x slower                                                 |
| pyflate                          | 321 ms                                                     | 484 ms: 1.51x slower                                                  |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 4.19 ms: 1.51x slower                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 15.7 ms: 1.52x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 274 ms: 1.52x slower                                                  |
| generators                       | 22.9 ms                                                    | 35.0 ms: 1.53x slower                                                 |
| tornado_http                     | 66.7 ms                                                    | 103 ms: 1.54x slower                                                  |
| 2to3                             | 161 ms                                                     | 249 ms: 1.55x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 77.8 ms: 1.57x slower                                                 |
| xml_etree_process                | 37.1 ms                                                    | 58.3 ms: 1.57x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 25.1 ms: 1.58x slower                                                 |
| thrift                           | 435 us                                                     | 692 us: 1.59x slower                                                  |
| typing_runtime_protocols         | 87.6 us                                                    | 144 us: 1.65x slower                                                  |
| html5lib                         | 31.2 ms                                                    | 51.8 ms: 1.66x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 50.2 ms: 1.68x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 52.4 ms: 1.70x slower                                                 |
| pprint_pformat                   | 947 ms                                                     | 1.66 sec: 1.75x slower                                                |
| pprint_safe_repr                 | 465 ms                                                     | 817 ms: 1.76x slower                                                  |
| scimark_sor                      | 94.9 ms                                                    | 167 ms: 1.76x slower                                                  |
| regex_compile                    | 68.5 ms                                                    | 121 ms: 1.77x slower                                                  |
| sympy_str                        | 131 ms                                                     | 234 ms: 1.78x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 107 ms: 1.78x slower                                                  |
| bench_thread_pool                | 447 us                                                     | 798 us: 1.79x slower                                                  |
| richards                         | 31.8 ms                                                    | 57.0 ms: 1.79x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 120 ms: 1.80x slower                                                  |
| genshi_text                      | 13.9 ms                                                    | 25.3 ms: 1.82x slower                                                 |
| go                               | 101 ms                                                     | 184 ms: 1.83x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 76.3 ms: 1.85x slower                                                 |
| django_template                  | 19.4 ms                                                    | 35.9 ms: 1.85x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 18.9 us: 1.86x slower                                                 |
| richards_super                   | 35.2 ms                                                    | 65.7 ms: 1.87x slower                                                 |
| unpickle_pure_python             | 141 us                                                     | 265 us: 1.89x slower                                                  |
| scimark_monte_carlo              | 42.5 ms                                                    | 81.1 ms: 1.91x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 432 ms: 1.91x slower                                                  |
| hexiom                           | 4.06 ms                                                    | 7.77 ms: 1.91x slower                                                 |
| mako                             | 6.99 ms                                                    | 13.5 ms: 1.93x slower                                                 |
| pickle_pure_python               | 179 us                                                     | 348 us: 1.95x slower                                                  |
| float                            | 48.6 ms                                                    | 97.7 ms: 2.01x slower                                                 |
| sympy_sum                        | 69.2 ms                                                    | 140 ms: 2.02x slower                                                  |
| logging_simple                   | 3.04 us                                                    | 6.17 us: 2.03x slower                                                 |
| logging_format                   | 3.31 us                                                    | 6.73 us: 2.03x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 1.94 ms: 2.17x slower                                                 |
| chaos                            | 34.0 ms                                                    | 76.0 ms: 2.24x slower                                                 |
| scimark_lu                       | 66.9 ms                                                    | 152 ms: 2.28x slower                                                  |
| logging_silent                   | 60.1 ns                                                    | 137 ns: 2.28x slower                                                  |
| sqlglot_parse                    | 732 us                                                     | 1.69 ms: 2.32x slower                                                 |
| raytrace                         | 147 ms                                                     | 381 ms: 2.59x slower                                                  |
| nbody                            | 59.6 ms                                                    | 157 ms: 2.64x slower                                                  |
| deltablue                        | 2.14 ms                                                    | 5.74 ms: 2.68x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.40x slower                                                          |
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240914-3.14.0a0-401fff7-NOGIL/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.28x
- 95% likely to have a slowdown of 1.27x
- 99% likely to have a slowdown of 1.23x

# Memory
- memory change: 0.55x
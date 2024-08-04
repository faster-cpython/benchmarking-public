# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: faster_jit_builds
- machine: darwin-arm64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.01x slower
- HPT reliability: 99.32%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.50x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 176 ms: 1.09x slower                                                     |
| docutils       | 1.44 sec                                                   | 1.57 sec: 1.09x slower                                                   |
| html5lib       | 31.2 ms                                                    | 30.9 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                      | 1.05x slower                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 640 ms: 1.20x faster                                                     |
| async_tree_eager_io_tg           | 768 ms                                                     | 676 ms: 1.14x faster                                                     |
| async_tree_io_tg                 | 565 ms                                                     | 507 ms: 1.11x faster                                                     |
| async_tree_none_tg               | 198 ms                                                     | 182 ms: 1.08x faster                                                     |
| async_tree_memoization           | 260 ms                                                     | 240 ms: 1.08x faster                                                     |
| async_tree_none                  | 209 ms                                                     | 195 ms: 1.08x faster                                                     |
| async_tree_memoization_tg        | 240 ms                                                     | 226 ms: 1.06x faster                                                     |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 453 ms: 1.03x faster                                                     |
| async_tree_io                    | 563 ms                                                     | 547 ms: 1.03x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                     |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                     |
| async_tree_eager                 | 60.3 ms                                                    | 61.8 ms: 1.02x slower                                                    |
| Geometric mean                   | (ref)                                                      | 1.05x faster                                                             |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization, async_tree_eager_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 45.9 ms: 1.06x faster                                                    |
| nbody          | 59.6 ms                                                    | 63.0 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                      | 1.00x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 149 ms                                                     | 150 ms: 1.00x slower                                                     |
| regex_effbot   | 2.58 ms                                                    | 2.73 ms: 1.06x slower                                                    |
| regex_compile  | 68.5 ms                                                    | 73.4 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                      | 1.03x slower                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.24 sec: 1.18x faster                                                   |
| unpickle_pure_python | 141 us                                                     | 133 us: 1.06x faster                                                     |
| xml_etree_process    | 37.1 ms                                                    | 35.4 ms: 1.05x faster                                                    |
| pickle_pure_python   | 179 us                                                     | 173 us: 1.03x faster                                                     |
| xml_etree_generate   | 52.7 ms                                                    | 51.7 ms: 1.02x faster                                                    |
| json_dumps           | 6.23 ms                                                    | 6.19 ms: 1.01x faster                                                    |
| json_loads           | 16.8 us                                                    | 17.0 us: 1.01x slower                                                    |
| xml_etree_iterparse  | 71.5 ms                                                    | 72.7 ms: 1.02x slower                                                    |
| xml_etree_parse      | 106 ms                                                     | 109 ms: 1.04x slower                                                     |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 17.1 ms: 1.13x slower                                                    |
| python_startup_no_site | 12.3 ms                                                    | 14.3 ms: 1.16x slower                                                    |
| Geometric mean         | (ref)                                                      | 1.14x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.43 ms: 1.09x faster                                                    |
| django_template | 19.4 ms                                                    | 21.3 ms: 1.10x slower                                                    |
| genshi_text     | 13.9 ms                                                    | 16.5 ms: 1.19x slower                                                    |
| genshi_xml      | 29.9 ms                                                    | 39.6 ms: 1.32x slower                                                    |
| Geometric mean  | (ref)                                                      | 1.12x slower                                                             |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo                    | 22.6 us                                                    | 16.6 us: 1.36x faster                                                    |
| deepcopy                         | 204 us                                                     | 154 us: 1.33x faster                                                     |
| async_tree_eager_io              | 766 ms                                                     | 640 ms: 1.20x faster                                                     |
| deepcopy_reduce                  | 1.82 us                                                    | 1.54 us: 1.18x faster                                                    |
| tomli_loads                      | 1.47 sec                                                   | 1.24 sec: 1.18x faster                                                   |
| async_tree_eager_io_tg           | 768 ms                                                     | 676 ms: 1.14x faster                                                     |
| async_tree_io_tg                 | 565 ms                                                     | 507 ms: 1.11x faster                                                     |
| mako                             | 6.99 ms                                                    | 6.43 ms: 1.09x faster                                                    |
| async_tree_none_tg               | 198 ms                                                     | 182 ms: 1.08x faster                                                     |
| async_tree_memoization           | 260 ms                                                     | 240 ms: 1.08x faster                                                     |
| async_tree_none                  | 209 ms                                                     | 195 ms: 1.08x faster                                                     |
| mdp                              | 1.53 sec                                                   | 1.44 sec: 1.07x faster                                                   |
| generators                       | 22.9 ms                                                    | 21.6 ms: 1.06x faster                                                    |
| async_tree_memoization_tg        | 240 ms                                                     | 226 ms: 1.06x faster                                                     |
| float                            | 48.6 ms                                                    | 45.9 ms: 1.06x faster                                                    |
| unpickle_pure_python             | 141 us                                                     | 133 us: 1.06x faster                                                     |
| richards                         | 31.8 ms                                                    | 30.4 ms: 1.05x faster                                                    |
| xml_etree_process                | 37.1 ms                                                    | 35.4 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 453 ms: 1.03x faster                                                     |
| pyflate                          | 321 ms                                                     | 311 ms: 1.03x faster                                                     |
| pickle_pure_python               | 179 us                                                     | 173 us: 1.03x faster                                                     |
| async_tree_io                    | 563 ms                                                     | 547 ms: 1.03x faster                                                     |
| telco                            | 4.60 ms                                                    | 4.51 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.27 sec: 1.02x faster                                                   |
| xml_etree_generate               | 52.7 ms                                                    | 51.7 ms: 1.02x faster                                                    |
| richards_super                   | 35.2 ms                                                    | 34.6 ms: 1.02x faster                                                    |
| logging_simple                   | 3.04 us                                                    | 3.00 us: 1.01x faster                                                    |
| json                             | 2.93 ms                                                    | 2.89 ms: 1.01x faster                                                    |
| html5lib                         | 31.2 ms                                                    | 30.9 ms: 1.01x faster                                                    |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.03 sec: 1.01x faster                                                   |
| json_dumps                       | 6.23 ms                                                    | 6.19 ms: 1.01x faster                                                    |
| logging_format                   | 3.31 us                                                    | 3.29 us: 1.00x faster                                                    |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                     |
| regex_dna                        | 149 ms                                                     | 150 ms: 1.00x slower                                                     |
| go                               | 101 ms                                                     | 101 ms: 1.00x slower                                                     |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                    |
| json_loads                       | 16.8 us                                                    | 17.0 us: 1.01x slower                                                    |
| create_gc_cycles                 | 897 us                                                     | 903 us: 1.01x slower                                                     |
| scimark_fft                      | 181 ms                                                     | 182 ms: 1.01x slower                                                     |
| meteor_contest                   | 70.3 ms                                                    | 70.9 ms: 1.01x slower                                                    |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                     |
| thrift                           | 435 us                                                     | 440 us: 1.01x slower                                                     |
| spectral_norm                    | 66.4 ms                                                    | 67.1 ms: 1.01x slower                                                    |
| pathlib                          | 23.3 ms                                                    | 23.6 ms: 1.01x slower                                                    |
| xml_etree_iterparse              | 71.5 ms                                                    | 72.7 ms: 1.02x slower                                                    |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                     |
| logging_silent                   | 60.1 ns                                                    | 61.4 ns: 1.02x slower                                                    |
| coverage                         | 45.0 ms                                                    | 46.0 ms: 1.02x slower                                                    |
| async_tree_eager                 | 60.3 ms                                                    | 61.8 ms: 1.02x slower                                                    |
| async_generators                 | 281 ms                                                     | 289 ms: 1.03x slower                                                     |
| coroutines                       | 15.8 ms                                                    | 16.3 ms: 1.03x slower                                                    |
| dulwich_log                      | 27.6 ms                                                    | 28.5 ms: 1.03x slower                                                    |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.9 ms: 1.03x slower                                                    |
| xml_etree_parse                  | 106 ms                                                     | 109 ms: 1.04x slower                                                     |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.89 ms: 1.04x slower                                                    |
| pprint_safe_repr                 | 465 ms                                                     | 487 ms: 1.05x slower                                                     |
| crypto_pyaes                     | 49.5 ms                                                    | 51.9 ms: 1.05x slower                                                    |
| bench_thread_pool                | 447 us                                                     | 470 us: 1.05x slower                                                     |
| sqlglot_normalize                | 166 ms                                                     | 175 ms: 1.05x slower                                                     |
| dask                             | 221 ms                                                     | 234 ms: 1.05x slower                                                     |
| nbody                            | 59.6 ms                                                    | 63.0 ms: 1.06x slower                                                    |
| regex_effbot                     | 2.58 ms                                                    | 2.73 ms: 1.06x slower                                                    |
| pprint_pformat                   | 947 ms                                                     | 1.00 sec: 1.06x slower                                                   |
| sympy_sum                        | 69.2 ms                                                    | 73.4 ms: 1.06x slower                                                    |
| sympy_str                        | 131 ms                                                     | 140 ms: 1.06x slower                                                     |
| scimark_sor                      | 94.9 ms                                                    | 101 ms: 1.06x slower                                                     |
| sqlglot_optimize                 | 30.9 ms                                                    | 32.8 ms: 1.06x slower                                                    |
| deltablue                        | 2.14 ms                                                    | 2.28 ms: 1.07x slower                                                    |
| sympy_expand                     | 226 ms                                                     | 241 ms: 1.07x slower                                                     |
| regex_compile                    | 68.5 ms                                                    | 73.4 ms: 1.07x slower                                                    |
| typing_runtime_protocols         | 87.6 us                                                    | 93.8 us: 1.07x slower                                                    |
| hexiom                           | 4.06 ms                                                    | 4.36 ms: 1.08x slower                                                    |
| sympy_integrate                  | 10.3 ms                                                    | 11.2 ms: 1.08x slower                                                    |
| bench_mp_pool                    | 47.2 ms                                                    | 51.4 ms: 1.09x slower                                                    |
| raytrace                         | 147 ms                                                     | 160 ms: 1.09x slower                                                     |
| docutils                         | 1.44 sec                                                   | 1.57 sec: 1.09x slower                                                   |
| 2to3                             | 161 ms                                                     | 176 ms: 1.09x slower                                                     |
| nqueens                          | 52.2 ms                                                    | 57.1 ms: 1.09x slower                                                    |
| django_template                  | 19.4 ms                                                    | 21.3 ms: 1.10x slower                                                    |
| pylint                           | 170 ms                                                     | 190 ms: 1.12x slower                                                     |
| pycparser                        | 632 ms                                                     | 708 ms: 1.12x slower                                                     |
| python_startup                   | 15.2 ms                                                    | 17.1 ms: 1.13x slower                                                    |
| sqlglot_transpile                | 891 us                                                     | 1.00 ms: 1.13x slower                                                    |
| chaos                            | 34.0 ms                                                    | 38.5 ms: 1.13x slower                                                    |
| sqlglot_parse                    | 732 us                                                     | 835 us: 1.14x slower                                                     |
| python_startup_no_site           | 12.3 ms                                                    | 14.3 ms: 1.16x slower                                                    |
| genshi_text                      | 13.9 ms                                                    | 16.5 ms: 1.19x slower                                                    |
| scimark_lu                       | 66.9 ms                                                    | 80.2 ms: 1.20x slower                                                    |
| comprehensions                   | 10.2 us                                                    | 12.3 us: 1.21x slower                                                    |
| genshi_xml                       | 29.9 ms                                                    | 39.6 ms: 1.32x slower                                                    |
| Geometric mean                   | (ref)                                                      | 1.01x slower                                                             |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, fannkuch, async_tree_eager_memoization, pidigits, async_tree_eager_tg, regex_v8, asyncio_tcp, tornado_http
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.32% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.50x
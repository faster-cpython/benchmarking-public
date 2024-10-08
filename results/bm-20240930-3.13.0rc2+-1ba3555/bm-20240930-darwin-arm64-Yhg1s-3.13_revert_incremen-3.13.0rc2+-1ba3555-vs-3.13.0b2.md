# Results vs. 3.13.0b2

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: darwin-arm64
- commit hash: 1ba3555
- commit date: 2024-09-30
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 0.47x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 174 ms: 1.08x slower                                                   |
| chameleon      | 4.27 ms                                                    | 4.75 ms: 1.11x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.43 sec: 1.01x faster                                                 |
| html5lib       | 31.2 ms                                                    | 34.7 ms: 1.11x slower                                                  |
| tornado_http   | 66.7 ms                                                    | 82.8 ms: 1.24x slower                                                  |
| Geometric mean | (ref)                                                      | 1.11x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager_io_tg           | 768 ms                                                     | 469 ms: 1.64x faster                                                   |
| async_tree_eager_io              | 766 ms                                                     | 506 ms: 1.51x faster                                                   |
| async_tree_io_tg                 | 565 ms                                                     | 494 ms: 1.14x faster                                                   |
| async_tree_io                    | 563 ms                                                     | 501 ms: 1.12x faster                                                   |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 454 ms: 1.03x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 372 ms: 1.04x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 344 ms: 1.04x slower                                                   |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 135 ms: 1.07x slower                                                   |
| async_tree_eager_memoization     | 152 ms                                                     | 165 ms: 1.08x slower                                                   |
| async_tree_eager_tg              | 41.4 ms                                                    | 45.4 ms: 1.10x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 67.6 ms: 1.12x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 285 ms: 1.19x slower                                                   |
| Geometric mean                   | (ref)                                                      | 1.04x faster                                                           |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 54.6 ms: 1.12x slower                                                  |
| nbody          | 59.6 ms                                                    | 75.1 ms: 1.26x slower                                                  |
| Geometric mean | (ref)                                                      | 1.12x slower                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.58 ms: 1.00x faster                                                  |
| regex_dna      | 149 ms                                                     | 149 ms: 1.00x faster                                                   |
| regex_v8       | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                                  |
| regex_compile  | 68.5 ms                                                    | 76.1 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                      | 1.03x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_list        | 2.88 us                                                    | 2.86 us: 1.01x faster                                                  |
| unpickle             | 9.12 us                                                    | 9.21 us: 1.01x slower                                                  |
| xml_etree_parse      | 106 ms                                                     | 107 ms: 1.02x slower                                                   |
| pickle               | 7.48 us                                                    | 7.60 us: 1.02x slower                                                  |
| pickle_list          | 2.96 us                                                    | 3.03 us: 1.03x slower                                                  |
| xml_etree_iterparse  | 71.5 ms                                                    | 74.0 ms: 1.04x slower                                                  |
| tomli_loads          | 1.47 sec                                                   | 1.52 sec: 1.04x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 6.56 ms: 1.05x slower                                                  |
| xml_etree_generate   | 52.7 ms                                                    | 56.3 ms: 1.07x slower                                                  |
| xml_etree_process    | 37.1 ms                                                    | 40.8 ms: 1.10x slower                                                  |
| unpickle_pure_python | 141 us                                                     | 156 us: 1.11x slower                                                   |
| pickle_pure_python   | 179 us                                                     | 203 us: 1.14x slower                                                   |
| Geometric mean       | (ref)                                                      | 1.04x slower                                                           |

Benchmark hidden because not significant (2): pickle_dict, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 13.2 ms: 1.07x slower                                                  |
| python_startup         | 15.2 ms                                                    | 16.7 ms: 1.10x slower                                                  |
| Geometric mean         | (ref)                                                      | 1.09x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 7.54 ms: 1.08x slower                                                  |
| genshi_xml      | 29.9 ms                                                    | 32.7 ms: 1.09x slower                                                  |
| genshi_text     | 13.9 ms                                                    | 15.7 ms: 1.13x slower                                                  |
| django_template | 19.4 ms                                                    | 22.1 ms: 1.14x slower                                                  |
| Geometric mean  | (ref)                                                      | 1.11x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager_io_tg           | 768 ms                                                     | 469 ms: 1.64x faster                                                   |
| async_tree_eager_io              | 766 ms                                                     | 506 ms: 1.51x faster                                                   |
| async_tree_io_tg                 | 565 ms                                                     | 494 ms: 1.14x faster                                                   |
| async_tree_io                    | 563 ms                                                     | 501 ms: 1.12x faster                                                   |
| create_gc_cycles                 | 897 us                                                     | 808 us: 1.11x faster                                                   |
| mdp                              | 1.53 sec                                                   | 1.47 sec: 1.04x faster                                                 |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 454 ms: 1.03x faster                                                   |
| docutils                         | 1.44 sec                                                   | 1.43 sec: 1.01x faster                                                 |
| unpickle_list                    | 2.88 us                                                    | 2.86 us: 1.01x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.58 ms: 1.00x faster                                                  |
| regex_dna                        | 149 ms                                                     | 149 ms: 1.00x faster                                                   |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                   |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                  |
| regex_v8                         | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                                  |
| unpickle                         | 9.12 us                                                    | 9.21 us: 1.01x slower                                                  |
| sqlite_synth                     | 1.55 us                                                    | 1.57 us: 1.01x slower                                                  |
| xml_etree_parse                  | 106 ms                                                     | 107 ms: 1.02x slower                                                   |
| pickle                           | 7.48 us                                                    | 7.60 us: 1.02x slower                                                  |
| coverage                         | 45.0 ms                                                    | 46.1 ms: 1.03x slower                                                  |
| pickle_list                      | 2.96 us                                                    | 3.03 us: 1.03x slower                                                  |
| json                             | 2.93 ms                                                    | 3.01 ms: 1.03x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 74.0 ms: 1.04x slower                                                  |
| tomli_loads                      | 1.47 sec                                                   | 1.52 sec: 1.04x slower                                                 |
| telco                            | 4.60 ms                                                    | 4.77 ms: 1.04x slower                                                  |
| dulwich_log                      | 27.6 ms                                                    | 28.6 ms: 1.04x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 372 ms: 1.04x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 344 ms: 1.04x slower                                                   |
| dask                             | 221 ms                                                     | 230 ms: 1.04x slower                                                   |
| meteor_contest                   | 70.3 ms                                                    | 73.3 ms: 1.04x slower                                                  |
| thrift                           | 435 us                                                     | 457 us: 1.05x slower                                                   |
| pathlib                          | 23.3 ms                                                    | 24.5 ms: 1.05x slower                                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.21 sec: 1.05x slower                                                 |
| async_generators                 | 281 ms                                                     | 296 ms: 1.05x slower                                                   |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.92 ms: 1.05x slower                                                  |
| json_dumps                       | 6.23 ms                                                    | 6.56 ms: 1.05x slower                                                  |
| pyflate                          | 321 ms                                                     | 341 ms: 1.06x slower                                                   |
| xml_etree_generate               | 52.7 ms                                                    | 56.3 ms: 1.07x slower                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 135 ms: 1.07x slower                                                   |
| python_startup_no_site           | 12.3 ms                                                    | 13.2 ms: 1.07x slower                                                  |
| bench_thread_pool                | 447 us                                                     | 479 us: 1.07x slower                                                   |
| bench_mp_pool                    | 47.2 ms                                                    | 50.7 ms: 1.08x slower                                                  |
| fannkuch                         | 248 ms                                                     | 267 ms: 1.08x slower                                                   |
| mako                             | 6.99 ms                                                    | 7.54 ms: 1.08x slower                                                  |
| async_tree_eager_memoization     | 152 ms                                                     | 165 ms: 1.08x slower                                                   |
| 2to3                             | 161 ms                                                     | 174 ms: 1.08x slower                                                   |
| crypto_pyaes                     | 49.5 ms                                                    | 53.6 ms: 1.08x slower                                                  |
| sympy_integrate                  | 10.3 ms                                                    | 11.2 ms: 1.09x slower                                                  |
| richards                         | 31.8 ms                                                    | 34.6 ms: 1.09x slower                                                  |
| scimark_sor                      | 94.9 ms                                                    | 103 ms: 1.09x slower                                                   |
| richards_super                   | 35.2 ms                                                    | 38.4 ms: 1.09x slower                                                  |
| sympy_sum                        | 69.2 ms                                                    | 75.4 ms: 1.09x slower                                                  |
| scimark_fft                      | 181 ms                                                     | 197 ms: 1.09x slower                                                   |
| spectral_norm                    | 66.4 ms                                                    | 72.5 ms: 1.09x slower                                                  |
| genshi_xml                       | 29.9 ms                                                    | 32.7 ms: 1.09x slower                                                  |
| sympy_expand                     | 226 ms                                                     | 247 ms: 1.10x slower                                                   |
| sympy_str                        | 131 ms                                                     | 144 ms: 1.10x slower                                                   |
| async_tree_eager_tg              | 41.4 ms                                                    | 45.4 ms: 1.10x slower                                                  |
| go                               | 101 ms                                                     | 110 ms: 1.10x slower                                                   |
| flaskblogging                    | 3.61 ms                                                    | 3.97 ms: 1.10x slower                                                  |
| xml_etree_process                | 37.1 ms                                                    | 40.8 ms: 1.10x slower                                                  |
| python_startup                   | 15.2 ms                                                    | 16.7 ms: 1.10x slower                                                  |
| pycparser                        | 632 ms                                                     | 698 ms: 1.10x slower                                                   |
| unpickle_pure_python             | 141 us                                                     | 156 us: 1.11x slower                                                   |
| deepcopy_reduce                  | 1.82 us                                                    | 2.02 us: 1.11x slower                                                  |
| generators                       | 22.9 ms                                                    | 25.4 ms: 1.11x slower                                                  |
| regex_compile                    | 68.5 ms                                                    | 76.1 ms: 1.11x slower                                                  |
| pprint_safe_repr                 | 465 ms                                                     | 516 ms: 1.11x slower                                                   |
| html5lib                         | 31.2 ms                                                    | 34.7 ms: 1.11x slower                                                  |
| pprint_pformat                   | 947 ms                                                     | 1.05 sec: 1.11x slower                                                 |
| chameleon                        | 4.27 ms                                                    | 4.75 ms: 1.11x slower                                                  |
| deepcopy                         | 204 us                                                     | 228 us: 1.12x slower                                                   |
| async_tree_eager                 | 60.3 ms                                                    | 67.6 ms: 1.12x slower                                                  |
| scimark_monte_carlo              | 42.5 ms                                                    | 47.7 ms: 1.12x slower                                                  |
| float                            | 48.6 ms                                                    | 54.6 ms: 1.12x slower                                                  |
| sqlglot_optimize                 | 30.9 ms                                                    | 34.8 ms: 1.13x slower                                                  |
| genshi_text                      | 13.9 ms                                                    | 15.7 ms: 1.13x slower                                                  |
| sqlglot_normalize                | 166 ms                                                     | 188 ms: 1.13x slower                                                   |
| logging_format                   | 3.31 us                                                    | 3.75 us: 1.13x slower                                                  |
| typing_runtime_protocols         | 87.6 us                                                    | 99.2 us: 1.13x slower                                                  |
| asyncio_tcp                      | 402 ms                                                     | 456 ms: 1.13x slower                                                   |
| django_template                  | 19.4 ms                                                    | 22.1 ms: 1.14x slower                                                  |
| pickle_pure_python               | 179 us                                                     | 203 us: 1.14x slower                                                   |
| sqlglot_transpile                | 891 us                                                     | 1.01 ms: 1.14x slower                                                  |
| logging_simple                   | 3.04 us                                                    | 3.47 us: 1.14x slower                                                  |
| nqueens                          | 52.2 ms                                                    | 59.6 ms: 1.14x slower                                                  |
| sqlglot_parse                    | 732 us                                                     | 838 us: 1.15x slower                                                   |
| deepcopy_memo                    | 22.6 us                                                    | 25.9 us: 1.15x slower                                                  |
| deltablue                        | 2.14 ms                                                    | 2.46 ms: 1.15x slower                                                  |
| scimark_lu                       | 66.9 ms                                                    | 76.9 ms: 1.15x slower                                                  |
| logging_silent                   | 60.1 ns                                                    | 69.5 ns: 1.15x slower                                                  |
| hexiom                           | 4.06 ms                                                    | 4.70 ms: 1.16x slower                                                  |
| aiohttp                          | 997 us                                                     | 1.16 ms: 1.16x slower                                                  |
| chaos                            | 34.0 ms                                                    | 39.6 ms: 1.17x slower                                                  |
| coroutines                       | 15.8 ms                                                    | 18.5 ms: 1.17x slower                                                  |
| gunicorn                         | 1.04 ms                                                    | 1.22 ms: 1.17x slower                                                  |
| raytrace                         | 147 ms                                                     | 173 ms: 1.18x slower                                                   |
| comprehensions                   | 10.2 us                                                    | 12.0 us: 1.18x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 285 ms: 1.19x slower                                                   |
| tornado_http                     | 66.7 ms                                                    | 82.8 ms: 1.24x slower                                                  |
| nbody                            | 59.6 ms                                                    | 75.1 ms: 1.26x slower                                                  |
| mypy2                            | 379 ms                                                     | 484 ms: 1.28x slower                                                   |
| Geometric mean                   | (ref)                                                      | 1.07x slower                                                           |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, async_tree_none_tg, asyncio_tcp_ssl, pickle_dict, pidigits, json_loads, async_tree_none, async_tree_memoization, pylint
Ignored benchmarks (1) of results/bm-20240930-3.13.0rc2+-1ba3555/bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 0.47x
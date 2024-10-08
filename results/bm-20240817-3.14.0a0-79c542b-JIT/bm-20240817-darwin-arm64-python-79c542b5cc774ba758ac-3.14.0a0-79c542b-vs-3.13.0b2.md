# Results vs. 3.13.0b2

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: darwin-arm64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.04x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.55x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 179 ms: 1.12x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.62 sec: 1.13x slower                                                |
| html5lib       | 31.2 ms                                                    | 34.5 ms: 1.11x slower                                                 |
| tornado_http   | 66.7 ms                                                    | 81.0 ms: 1.21x slower                                                 |
| Geometric mean | (ref)                                                      | 1.14x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 636 ms: 1.20x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 492 ms: 1.15x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 675 ms: 1.14x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 182 ms: 1.09x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 242 ms: 1.07x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 197 ms: 1.06x faster                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 229 ms: 1.05x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 543 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 456 ms: 1.03x faster                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.9 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 338 ms: 1.02x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 367 ms: 1.03x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 64.8 ms: 1.07x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.04x faster                                                          |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 46.6 ms: 1.04x faster                                                 |
| pidigits       | 282 ms                                                     | 282 ms: 1.00x faster                                                  |
| nbody          | 59.6 ms                                                    | 63.8 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                                 |
| regex_dna      | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| regex_v8       | 17.3 ms                                                    | 16.9 ms: 1.03x faster                                                 |
| regex_compile  | 68.5 ms                                                    | 74.8 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.26 sec: 1.16x faster                                                |
| xml_etree_process    | 37.1 ms                                                    | 34.4 ms: 1.08x faster                                                 |
| unpickle_pure_python | 141 us                                                     | 134 us: 1.05x faster                                                  |
| xml_etree_generate   | 52.7 ms                                                    | 50.3 ms: 1.05x faster                                                 |
| json_loads           | 16.8 us                                                    | 17.2 us: 1.02x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 109 ms: 1.03x slower                                                  |
| json_dumps           | 6.23 ms                                                    | 6.50 ms: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 11.6 ms: 1.06x faster                                                 |
| python_startup         | 15.2 ms                                                    | 14.3 ms: 1.06x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.06x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.50 ms: 1.07x faster                                                 |
| django_template | 19.4 ms                                                    | 23.0 ms: 1.19x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 17.0 ms: 1.22x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 42.1 ms: 1.41x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.17x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 22.6 us                                                    | 16.2 us: 1.40x faster                                                 |
| deepcopy                         | 204 us                                                     | 155 us: 1.32x faster                                                  |
| deepcopy_reduce                  | 1.82 us                                                    | 1.51 us: 1.21x faster                                                 |
| async_tree_eager_io              | 766 ms                                                     | 636 ms: 1.20x faster                                                  |
| tomli_loads                      | 1.47 sec                                                   | 1.26 sec: 1.16x faster                                                |
| async_tree_io_tg                 | 565 ms                                                     | 492 ms: 1.15x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 675 ms: 1.14x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 182 ms: 1.09x faster                                                  |
| scimark_sor                      | 94.9 ms                                                    | 88.0 ms: 1.08x faster                                                 |
| xml_etree_process                | 37.1 ms                                                    | 34.4 ms: 1.08x faster                                                 |
| mako                             | 6.99 ms                                                    | 6.50 ms: 1.07x faster                                                 |
| async_tree_memoization           | 260 ms                                                     | 242 ms: 1.07x faster                                                  |
| python_startup_no_site           | 12.3 ms                                                    | 11.6 ms: 1.06x faster                                                 |
| async_tree_none                  | 209 ms                                                     | 197 ms: 1.06x faster                                                  |
| python_startup                   | 15.2 ms                                                    | 14.3 ms: 1.06x faster                                                 |
| mdp                              | 1.53 sec                                                   | 1.45 sec: 1.06x faster                                                |
| unpickle_pure_python             | 141 us                                                     | 134 us: 1.05x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                                 |
| xml_etree_generate               | 52.7 ms                                                    | 50.3 ms: 1.05x faster                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 229 ms: 1.05x faster                                                  |
| float                            | 48.6 ms                                                    | 46.6 ms: 1.04x faster                                                 |
| async_tree_io                    | 563 ms                                                     | 543 ms: 1.04x faster                                                  |
| regex_dna                        | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 456 ms: 1.03x faster                                                  |
| regex_v8                         | 17.3 ms                                                    | 16.9 ms: 1.03x faster                                                 |
| scimark_lu                       | 66.9 ms                                                    | 65.6 ms: 1.02x faster                                                 |
| coverage                         | 45.0 ms                                                    | 44.6 ms: 1.01x faster                                                 |
| logging_simple                   | 3.04 us                                                    | 3.02 us: 1.01x faster                                                 |
| create_gc_cycles                 | 897 us                                                     | 893 us: 1.00x faster                                                  |
| thrift                           | 435 us                                                     | 434 us: 1.00x faster                                                  |
| pidigits                         | 282 ms                                                     | 282 ms: 1.00x faster                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                 |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.07 sec: 1.00x slower                                                |
| pathlib                          | 23.3 ms                                                    | 23.5 ms: 1.01x slower                                                 |
| logging_format                   | 3.31 us                                                    | 3.33 us: 1.01x slower                                                 |
| telco                            | 4.60 ms                                                    | 4.64 ms: 1.01x slower                                                 |
| go                               | 101 ms                                                     | 102 ms: 1.01x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.9 ms: 1.01x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 16.1 ms: 1.01x slower                                                 |
| pyflate                          | 321 ms                                                     | 327 ms: 1.02x slower                                                  |
| json_loads                       | 16.8 us                                                    | 17.2 us: 1.02x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 338 ms: 1.02x slower                                                  |
| dulwich_log                      | 27.6 ms                                                    | 28.2 ms: 1.02x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 367 ms: 1.03x slower                                                  |
| xml_etree_parse                  | 106 ms                                                     | 109 ms: 1.03x slower                                                  |
| logging_silent                   | 60.1 ns                                                    | 62.1 ns: 1.03x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 49.1 ms: 1.04x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.50 ms: 1.04x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 469 us: 1.05x slower                                                  |
| spectral_norm                    | 66.4 ms                                                    | 69.7 ms: 1.05x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 52.1 ms: 1.05x slower                                                 |
| async_generators                 | 281 ms                                                     | 297 ms: 1.06x slower                                                  |
| meteor_contest                   | 70.3 ms                                                    | 74.6 ms: 1.06x slower                                                 |
| generators                       | 22.9 ms                                                    | 24.5 ms: 1.07x slower                                                 |
| nbody                            | 59.6 ms                                                    | 63.8 ms: 1.07x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 194 ms: 1.07x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 64.8 ms: 1.07x slower                                                 |
| deltablue                        | 2.14 ms                                                    | 2.32 ms: 1.08x slower                                                 |
| fannkuch                         | 248 ms                                                     | 269 ms: 1.09x slower                                                  |
| regex_compile                    | 68.5 ms                                                    | 74.8 ms: 1.09x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 95.8 us: 1.09x slower                                                 |
| pycparser                        | 632 ms                                                     | 695 ms: 1.10x slower                                                  |
| pprint_safe_repr                 | 465 ms                                                     | 512 ms: 1.10x slower                                                  |
| html5lib                         | 31.2 ms                                                    | 34.5 ms: 1.11x slower                                                 |
| pprint_pformat                   | 947 ms                                                     | 1.05 sec: 1.11x slower                                                |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 3.08 ms: 1.11x slower                                                 |
| asyncio_tcp                      | 402 ms                                                     | 448 ms: 1.11x slower                                                  |
| raytrace                         | 147 ms                                                     | 164 ms: 1.11x slower                                                  |
| 2to3                             | 161 ms                                                     | 179 ms: 1.12x slower                                                  |
| sympy_expand                     | 226 ms                                                     | 252 ms: 1.12x slower                                                  |
| sympy_sum                        | 69.2 ms                                                    | 77.3 ms: 1.12x slower                                                 |
| sympy_str                        | 131 ms                                                     | 147 ms: 1.12x slower                                                  |
| sqlglot_normalize                | 166 ms                                                     | 185 ms: 1.12x slower                                                  |
| scimark_monte_carlo              | 42.5 ms                                                    | 48.0 ms: 1.13x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.62 sec: 1.13x slower                                                |
| nqueens                          | 52.2 ms                                                    | 59.2 ms: 1.13x slower                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 11.9 ms: 1.15x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 4.72 ms: 1.16x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 36.0 ms: 1.16x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 856 us: 1.17x slower                                                  |
| chaos                            | 34.0 ms                                                    | 40.1 ms: 1.18x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 1.05 ms: 1.18x slower                                                 |
| django_template                  | 19.4 ms                                                    | 23.0 ms: 1.19x slower                                                 |
| pylint                           | 170 ms                                                     | 205 ms: 1.21x slower                                                  |
| tornado_http                     | 66.7 ms                                                    | 81.0 ms: 1.21x slower                                                 |
| genshi_text                      | 13.9 ms                                                    | 17.0 ms: 1.22x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 12.7 us: 1.25x slower                                                 |
| richards_super                   | 35.2 ms                                                    | 48.1 ms: 1.37x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 42.1 ms: 1.41x slower                                                 |
| richards                         | 31.8 ms                                                    | 45.9 ms: 1.44x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.04x slower                                                          |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, json, asyncio_websockets, pickle_pure_python, async_tree_eager_memoization_tg, xml_etree_iterparse, asyncio_tcp_ssl, async_tree_eager_memoization
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.55x
# Results vs. 3.13.0b2

- fork: python
- ref: c15f94d6fbc960790db3
- machine: darwin-arm64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.12x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 0.59x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 181 ms: 1.12x slower                                                   |
| chameleon      | 4.27 ms                                                    | 4.97 ms: 1.16x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.66 sec: 1.16x slower                                                 |
| html5lib       | 31.2 ms                                                    | 33.3 ms: 1.07x slower                                                  |
| tornado_http   | 66.7 ms                                                    | 69.4 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                      | 1.11x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 335 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 476 ms: 1.02x slower                                                   |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 365 ms: 1.02x slower                                                   |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 129 ms: 1.03x slower                                                   |
| async_tree_none_tg               | 198 ms                                                     | 205 ms: 1.04x slower                                                   |
| async_tree_memoization           | 260 ms                                                     | 269 ms: 1.04x slower                                                   |
| async_tree_none                  | 209 ms                                                     | 221 ms: 1.05x slower                                                   |
| async_tree_eager_tg              | 41.4 ms                                                    | 44.4 ms: 1.07x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 257 ms: 1.07x slower                                                   |
| async_tree_eager                 | 60.3 ms                                                    | 68.7 ms: 1.14x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.03x slower                                                           |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 283 ms: 1.00x slower                                                   |
| float          | 48.6 ms                                                    | 60.7 ms: 1.25x slower                                                  |
| nbody          | 59.6 ms                                                    | 76.8 ms: 1.29x slower                                                  |
| Geometric mean | (ref)                                                      | 1.17x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.58 ms: 1.00x faster                                                  |
| regex_dna      | 149 ms                                                     | 149 ms: 1.00x faster                                                   |
| regex_v8       | 17.3 ms                                                    | 17.6 ms: 1.02x slower                                                  |
| regex_compile  | 68.5 ms                                                    | 96.0 ms: 1.40x slower                                                  |
| Geometric mean | (ref)                                                      | 1.09x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                     | 103 ms: 1.02x faster                                                   |
| pickle_dict          | 18.3 us                                                    | 18.2 us: 1.00x faster                                                  |
| json_loads           | 16.8 us                                                    | 16.9 us: 1.00x slower                                                  |
| pickle               | 7.48 us                                                    | 7.52 us: 1.01x slower                                                  |
| pickle_list          | 2.96 us                                                    | 3.00 us: 1.02x slower                                                  |
| unpickle_list        | 2.88 us                                                    | 2.94 us: 1.02x slower                                                  |
| unpickle             | 9.12 us                                                    | 9.31 us: 1.02x slower                                                  |
| json_dumps           | 6.23 ms                                                    | 6.60 ms: 1.06x slower                                                  |
| xml_etree_iterparse  | 71.5 ms                                                    | 76.0 ms: 1.06x slower                                                  |
| xml_etree_process    | 37.1 ms                                                    | 41.2 ms: 1.11x slower                                                  |
| tomli_loads          | 1.47 sec                                                   | 1.63 sec: 1.11x slower                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 59.0 ms: 1.12x slower                                                  |
| unpickle_pure_python | 141 us                                                     | 175 us: 1.24x slower                                                   |
| pickle_pure_python   | 179 us                                                     | 226 us: 1.27x slower                                                   |
| Geometric mean       | (ref)                                                      | 1.07x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 11.4 ms: 1.08x faster                                                  |
| python_startup         | 15.2 ms                                                    | 14.3 ms: 1.06x faster                                                  |
| Geometric mean         | (ref)                                                      | 1.07x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 29.9 ms                                                    | 35.9 ms: 1.20x slower                                                  |
| django_template | 19.4 ms                                                    | 23.6 ms: 1.22x slower                                                  |
| genshi_text     | 13.9 ms                                                    | 17.3 ms: 1.25x slower                                                  |
| mako            | 6.99 ms                                                    | 8.85 ms: 1.27x slower                                                  |
| Geometric mean  | (ref)                                                      | 1.23x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| flaskblogging                    | 3.61 ms                                                    | 3.28 ms: 1.10x faster                                                  |
| python_startup_no_site           | 12.3 ms                                                    | 11.4 ms: 1.08x faster                                                  |
| python_startup                   | 15.2 ms                                                    | 14.3 ms: 1.06x faster                                                  |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.24 sec: 1.04x faster                                                 |
| pathlib                          | 23.3 ms                                                    | 22.7 ms: 1.03x faster                                                  |
| xml_etree_parse                  | 106 ms                                                     | 103 ms: 1.02x faster                                                   |
| pickle_dict                      | 18.3 us                                                    | 18.2 us: 1.00x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.58 ms: 1.00x faster                                                  |
| regex_dna                        | 149 ms                                                     | 149 ms: 1.00x faster                                                   |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                  |
| json_loads                       | 16.8 us                                                    | 16.9 us: 1.00x slower                                                  |
| pidigits                         | 282 ms                                                     | 283 ms: 1.00x slower                                                   |
| pickle                           | 7.48 us                                                    | 7.52 us: 1.01x slower                                                  |
| create_gc_cycles                 | 897 us                                                     | 903 us: 1.01x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 335 ms: 1.01x slower                                                   |
| thrift                           | 435 us                                                     | 441 us: 1.01x slower                                                   |
| pickle_list                      | 2.96 us                                                    | 3.00 us: 1.02x slower                                                  |
| mdp                              | 1.53 sec                                                   | 1.56 sec: 1.02x slower                                                 |
| regex_v8                         | 17.3 ms                                                    | 17.6 ms: 1.02x slower                                                  |
| unpickle_list                    | 2.88 us                                                    | 2.94 us: 1.02x slower                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 476 ms: 1.02x slower                                                   |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 365 ms: 1.02x slower                                                   |
| unpickle                         | 9.12 us                                                    | 9.31 us: 1.02x slower                                                  |
| generators                       | 22.9 ms                                                    | 23.4 ms: 1.02x slower                                                  |
| coroutines                       | 15.8 ms                                                    | 16.2 ms: 1.02x slower                                                  |
| coverage                         | 45.0 ms                                                    | 46.0 ms: 1.02x slower                                                  |
| dask                             | 221 ms                                                     | 227 ms: 1.03x slower                                                   |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 129 ms: 1.03x slower                                                   |
| json                             | 2.93 ms                                                    | 3.03 ms: 1.04x slower                                                  |
| async_tree_none_tg               | 198 ms                                                     | 205 ms: 1.04x slower                                                   |
| async_tree_memoization           | 260 ms                                                     | 269 ms: 1.04x slower                                                   |
| logging_simple                   | 3.04 us                                                    | 3.16 us: 1.04x slower                                                  |
| tornado_http                     | 66.7 ms                                                    | 69.4 ms: 1.04x slower                                                  |
| sqlite_synth                     | 1.55 us                                                    | 1.62 us: 1.04x slower                                                  |
| logging_format                   | 3.31 us                                                    | 3.46 us: 1.04x slower                                                  |
| async_generators                 | 281 ms                                                     | 294 ms: 1.05x slower                                                   |
| async_tree_none                  | 209 ms                                                     | 221 ms: 1.05x slower                                                   |
| json_dumps                       | 6.23 ms                                                    | 6.60 ms: 1.06x slower                                                  |
| aiohttp                          | 997 us                                                     | 1.06 ms: 1.06x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 76.0 ms: 1.06x slower                                                  |
| dulwich_log                      | 27.6 ms                                                    | 29.5 ms: 1.07x slower                                                  |
| html5lib                         | 31.2 ms                                                    | 33.3 ms: 1.07x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 44.4 ms: 1.07x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 257 ms: 1.07x slower                                                   |
| telco                            | 4.60 ms                                                    | 4.96 ms: 1.08x slower                                                  |
| gunicorn                         | 1.04 ms                                                    | 1.12 ms: 1.08x slower                                                  |
| xml_etree_process                | 37.1 ms                                                    | 41.2 ms: 1.11x slower                                                  |
| tomli_loads                      | 1.47 sec                                                   | 1.63 sec: 1.11x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 78.6 ms: 1.12x slower                                                  |
| pylint                           | 170 ms                                                     | 190 ms: 1.12x slower                                                   |
| xml_etree_generate               | 52.7 ms                                                    | 59.0 ms: 1.12x slower                                                  |
| 2to3                             | 161 ms                                                     | 181 ms: 1.12x slower                                                   |
| scimark_sor                      | 94.9 ms                                                    | 107 ms: 1.13x slower                                                   |
| mypy2                            | 379 ms                                                     | 428 ms: 1.13x slower                                                   |
| async_tree_eager                 | 60.3 ms                                                    | 68.7 ms: 1.14x slower                                                  |
| pycparser                        | 632 ms                                                     | 723 ms: 1.14x slower                                                   |
| docutils                         | 1.44 sec                                                   | 1.66 sec: 1.16x slower                                                 |
| richards_super                   | 35.2 ms                                                    | 40.8 ms: 1.16x slower                                                  |
| chameleon                        | 4.27 ms                                                    | 4.97 ms: 1.16x slower                                                  |
| deepcopy_reduce                  | 1.82 us                                                    | 2.12 us: 1.16x slower                                                  |
| go                               | 101 ms                                                     | 117 ms: 1.17x slower                                                   |
| bench_thread_pool                | 447 us                                                     | 522 us: 1.17x slower                                                   |
| sympy_expand                     | 226 ms                                                     | 264 ms: 1.17x slower                                                   |
| richards                         | 31.8 ms                                                    | 37.4 ms: 1.17x slower                                                  |
| sqlglot_optimize                 | 30.9 ms                                                    | 37.0 ms: 1.20x slower                                                  |
| genshi_xml                       | 29.9 ms                                                    | 35.9 ms: 1.20x slower                                                  |
| sympy_integrate                  | 10.3 ms                                                    | 12.5 ms: 1.21x slower                                                  |
| typing_runtime_protocols         | 87.6 us                                                    | 106 us: 1.21x slower                                                   |
| django_template                  | 19.4 ms                                                    | 23.6 ms: 1.22x slower                                                  |
| sympy_sum                        | 69.2 ms                                                    | 84.9 ms: 1.23x slower                                                  |
| raytrace                         | 147 ms                                                     | 180 ms: 1.23x slower                                                   |
| crypto_pyaes                     | 49.5 ms                                                    | 60.8 ms: 1.23x slower                                                  |
| pyflate                          | 321 ms                                                     | 395 ms: 1.23x slower                                                   |
| deepcopy                         | 204 us                                                     | 251 us: 1.23x slower                                                   |
| scimark_fft                      | 181 ms                                                     | 223 ms: 1.23x slower                                                   |
| fannkuch                         | 248 ms                                                     | 308 ms: 1.24x slower                                                   |
| unpickle_pure_python             | 141 us                                                     | 175 us: 1.24x slower                                                   |
| sympy_str                        | 131 ms                                                     | 164 ms: 1.24x slower                                                   |
| genshi_text                      | 13.9 ms                                                    | 17.3 ms: 1.25x slower                                                  |
| pprint_safe_repr                 | 465 ms                                                     | 579 ms: 1.25x slower                                                   |
| pprint_pformat                   | 947 ms                                                     | 1.18 sec: 1.25x slower                                                 |
| float                            | 48.6 ms                                                    | 60.7 ms: 1.25x slower                                                  |
| mako                             | 6.99 ms                                                    | 8.85 ms: 1.27x slower                                                  |
| pickle_pure_python               | 179 us                                                     | 226 us: 1.27x slower                                                   |
| nbody                            | 59.6 ms                                                    | 76.8 ms: 1.29x slower                                                  |
| nqueens                          | 52.2 ms                                                    | 67.5 ms: 1.29x slower                                                  |
| sqlglot_transpile                | 891 us                                                     | 1.16 ms: 1.30x slower                                                  |
| sqlglot_parse                    | 732 us                                                     | 952 us: 1.30x slower                                                   |
| chaos                            | 34.0 ms                                                    | 46.4 ms: 1.37x slower                                                  |
| deltablue                        | 2.14 ms                                                    | 2.94 ms: 1.38x slower                                                  |
| spectral_norm                    | 66.4 ms                                                    | 92.1 ms: 1.39x slower                                                  |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 3.86 ms: 1.39x slower                                                  |
| regex_compile                    | 68.5 ms                                                    | 96.0 ms: 1.40x slower                                                  |
| scimark_monte_carlo              | 42.5 ms                                                    | 60.8 ms: 1.43x slower                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 32.6 us: 1.44x slower                                                  |
| scimark_lu                       | 66.9 ms                                                    | 97.1 ms: 1.45x slower                                                  |
| hexiom                           | 4.06 ms                                                    | 5.92 ms: 1.46x slower                                                  |
| logging_silent                   | 60.1 ns                                                    | 94.6 ns: 1.57x slower                                                  |
| comprehensions                   | 10.2 us                                                    | 17.3 us: 1.71x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.12x slower                                                           |

Benchmark hidden because not significant (9): async_tree_io_tg, async_tree_eager_io, async_tree_eager_io_tg, asyncio_websockets, bench_mp_pool, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization, asyncio_tcp
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 0.59x
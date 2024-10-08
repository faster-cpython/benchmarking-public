# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a3
- machine: darwin-arm64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 170 ms: 1.06x slower                                       |
| chameleon      | 4.27 ms                                                    | 4.87 ms: 1.14x slower                                      |
| docutils       | 1.44 sec                                                   | 1.46 sec: 1.02x slower                                     |
| html5lib       | 31.2 ms                                                    | 35.9 ms: 1.15x slower                                      |
| tornado_http   | 66.7 ms                                                    | 78.1 ms: 1.17x slower                                      |
| Geometric mean | (ref)                                                      | 1.11x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_eager_io_tg           | 768 ms                                                     | 644 ms: 1.19x faster                                       |
| async_tree_eager_io              | 766 ms                                                     | 670 ms: 1.14x faster                                       |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 370 ms: 1.03x slower                                       |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 342 ms: 1.03x slower                                       |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 521 ms: 1.11x slower                                       |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 140 ms: 1.12x slower                                       |
| async_tree_eager_memoization     | 152 ms                                                     | 173 ms: 1.13x slower                                       |
| async_tree_eager                 | 60.3 ms                                                    | 68.6 ms: 1.14x slower                                      |
| async_tree_eager_tg              | 41.4 ms                                                    | 47.2 ms: 1.14x slower                                      |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 531 ms: 1.18x slower                                       |
| async_tree_io_tg                 | 565 ms                                                     | 672 ms: 1.19x slower                                       |
| async_tree_none                  | 209 ms                                                     | 253 ms: 1.21x slower                                       |
| async_tree_io                    | 563 ms                                                     | 703 ms: 1.25x slower                                       |
| async_tree_memoization           | 260 ms                                                     | 329 ms: 1.27x slower                                       |
| async_tree_none_tg               | 198 ms                                                     | 260 ms: 1.31x slower                                       |
| async_tree_memoization_tg        | 240 ms                                                     | 324 ms: 1.35x slower                                       |
| Geometric mean                   | (ref)                                                      | 1.13x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 282 ms: 1.00x slower                                       |
| float          | 48.6 ms                                                    | 56.9 ms: 1.17x slower                                      |
| nbody          | 59.6 ms                                                    | 75.6 ms: 1.27x slower                                      |
| Geometric mean | (ref)                                                      | 1.14x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 18.0 ms: 1.04x slower                                      |
| regex_dna      | 149 ms                                                     | 157 ms: 1.05x slower                                       |
| regex_effbot   | 2.58 ms                                                    | 2.77 ms: 1.07x slower                                      |
| regex_compile  | 68.5 ms                                                    | 73.8 ms: 1.08x slower                                      |
| Geometric mean | (ref)                                                      | 1.06x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                     | 99.6 ms: 1.06x faster                                      |
| pickle               | 7.48 us                                                    | 7.41 us: 1.01x faster                                      |
| pickle_list          | 2.96 us                                                    | 2.93 us: 1.01x faster                                      |
| pickle_dict          | 18.3 us                                                    | 18.2 us: 1.01x faster                                      |
| xml_etree_iterparse  | 71.5 ms                                                    | 71.9 ms: 1.01x slower                                      |
| json_loads           | 16.8 us                                                    | 17.1 us: 1.01x slower                                      |
| unpickle             | 9.12 us                                                    | 9.29 us: 1.02x slower                                      |
| json_dumps           | 6.23 ms                                                    | 6.52 ms: 1.05x slower                                      |
| tomli_loads          | 1.47 sec                                                   | 1.54 sec: 1.05x slower                                     |
| xml_etree_generate   | 52.7 ms                                                    | 56.3 ms: 1.07x slower                                      |
| xml_etree_process    | 37.1 ms                                                    | 39.9 ms: 1.08x slower                                      |
| unpickle_list        | 2.88 us                                                    | 3.11 us: 1.08x slower                                      |
| unpickle_pure_python | 141 us                                                     | 154 us: 1.09x slower                                       |
| pickle_pure_python   | 179 us                                                     | 198 us: 1.11x slower                                       |
| Geometric mean       | (ref)                                                      | 1.03x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup | 15.2 ms                                                    | 13.9 ms: 1.09x faster                                      |
| Geometric mean | (ref)                                                      | 1.04x faster                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 7.54 ms: 1.08x slower                                      |
| django_template | 19.4 ms                                                    | 21.7 ms: 1.12x slower                                      |
| genshi_xml      | 29.9 ms                                                    | 33.6 ms: 1.12x slower                                      |
| genshi_text     | 13.9 ms                                                    | 15.8 ms: 1.13x slower                                      |
| Geometric mean  | (ref)                                                      | 1.11x slower                                               |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles                 | 897 us                                                     | 706 us: 1.27x faster                                       |
| typing_runtime_protocols         | 87.6 us                                                    | 70.9 us: 1.23x faster                                      |
| async_tree_eager_io_tg           | 768 ms                                                     | 644 ms: 1.19x faster                                       |
| async_tree_eager_io              | 766 ms                                                     | 670 ms: 1.14x faster                                       |
| python_startup                   | 15.2 ms                                                    | 13.9 ms: 1.09x faster                                      |
| xml_etree_parse                  | 106 ms                                                     | 99.6 ms: 1.06x faster                                      |
| bench_mp_pool                    | 47.2 ms                                                    | 45.1 ms: 1.05x faster                                      |
| crypto_pyaes                     | 49.5 ms                                                    | 48.3 ms: 1.02x faster                                      |
| gc_traversal                     | 2.45 ms                                                    | 2.40 ms: 1.02x faster                                      |
| pickle                           | 7.48 us                                                    | 7.41 us: 1.01x faster                                      |
| pickle_list                      | 2.96 us                                                    | 2.93 us: 1.01x faster                                      |
| pickle_dict                      | 18.3 us                                                    | 18.2 us: 1.01x faster                                      |
| pidigits                         | 282 ms                                                     | 282 ms: 1.00x slower                                       |
| xml_etree_iterparse              | 71.5 ms                                                    | 71.9 ms: 1.01x slower                                      |
| telco                            | 4.60 ms                                                    | 4.65 ms: 1.01x slower                                      |
| json_loads                       | 16.8 us                                                    | 17.1 us: 1.01x slower                                      |
| docutils                         | 1.44 sec                                                   | 1.46 sec: 1.02x slower                                     |
| json                             | 2.93 ms                                                    | 2.98 ms: 1.02x slower                                      |
| unpickle                         | 9.12 us                                                    | 9.29 us: 1.02x slower                                      |
| mdp                              | 1.53 sec                                                   | 1.56 sec: 1.02x slower                                     |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.32 sec: 1.03x slower                                     |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 370 ms: 1.03x slower                                       |
| sqlite_synth                     | 1.55 us                                                    | 1.60 us: 1.03x slower                                      |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 342 ms: 1.03x slower                                       |
| meteor_contest                   | 70.3 ms                                                    | 72.7 ms: 1.03x slower                                      |
| sympy_integrate                  | 10.3 ms                                                    | 10.7 ms: 1.04x slower                                      |
| regex_v8                         | 17.3 ms                                                    | 18.0 ms: 1.04x slower                                      |
| json_dumps                       | 6.23 ms                                                    | 6.52 ms: 1.05x slower                                      |
| sympy_sum                        | 69.2 ms                                                    | 72.5 ms: 1.05x slower                                      |
| pathlib                          | 23.3 ms                                                    | 24.5 ms: 1.05x slower                                      |
| coverage                         | 45.0 ms                                                    | 47.2 ms: 1.05x slower                                      |
| go                               | 101 ms                                                     | 106 ms: 1.05x slower                                       |
| regex_dna                        | 149 ms                                                     | 157 ms: 1.05x slower                                       |
| thrift                           | 435 us                                                     | 458 us: 1.05x slower                                       |
| async_generators                 | 281 ms                                                     | 296 ms: 1.05x slower                                       |
| tomli_loads                      | 1.47 sec                                                   | 1.54 sec: 1.05x slower                                     |
| sympy_expand                     | 226 ms                                                     | 238 ms: 1.06x slower                                       |
| pyflate                          | 321 ms                                                     | 339 ms: 1.06x slower                                       |
| 2to3                             | 161 ms                                                     | 170 ms: 1.06x slower                                       |
| richards_super                   | 35.2 ms                                                    | 37.3 ms: 1.06x slower                                      |
| sympy_str                        | 131 ms                                                     | 140 ms: 1.06x slower                                       |
| richards                         | 31.8 ms                                                    | 33.8 ms: 1.06x slower                                      |
| dulwich_log                      | 27.6 ms                                                    | 29.4 ms: 1.07x slower                                      |
| xml_etree_generate               | 52.7 ms                                                    | 56.3 ms: 1.07x slower                                      |
| regex_effbot                     | 2.58 ms                                                    | 2.77 ms: 1.07x slower                                      |
| xml_etree_process                | 37.1 ms                                                    | 39.9 ms: 1.08x slower                                      |
| regex_compile                    | 68.5 ms                                                    | 73.8 ms: 1.08x slower                                      |
| unpickle_list                    | 2.88 us                                                    | 3.11 us: 1.08x slower                                      |
| sqlglot_parse                    | 732 us                                                     | 789 us: 1.08x slower                                       |
| mako                             | 6.99 ms                                                    | 7.54 ms: 1.08x slower                                      |
| sqlglot_transpile                | 891 us                                                     | 965 us: 1.08x slower                                       |
| deepcopy_reduce                  | 1.82 us                                                    | 1.98 us: 1.09x slower                                      |
| flaskblogging                    | 3.61 ms                                                    | 3.94 ms: 1.09x slower                                      |
| unpickle_pure_python             | 141 us                                                     | 154 us: 1.09x slower                                       |
| fannkuch                         | 248 ms                                                     | 273 ms: 1.10x slower                                       |
| sqlglot_optimize                 | 30.9 ms                                                    | 33.9 ms: 1.10x slower                                      |
| sqlglot_normalize                | 166 ms                                                     | 183 ms: 1.10x slower                                       |
| deepcopy                         | 204 us                                                     | 225 us: 1.10x slower                                       |
| pycparser                        | 632 ms                                                     | 700 ms: 1.11x slower                                       |
| pprint_pformat                   | 947 ms                                                     | 1.05 sec: 1.11x slower                                     |
| pickle_pure_python               | 179 us                                                     | 198 us: 1.11x slower                                       |
| scimark_sor                      | 94.9 ms                                                    | 105 ms: 1.11x slower                                       |
| scimark_lu                       | 66.9 ms                                                    | 74.2 ms: 1.11x slower                                      |
| pprint_safe_repr                 | 465 ms                                                     | 516 ms: 1.11x slower                                       |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 521 ms: 1.11x slower                                       |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 140 ms: 1.12x slower                                       |
| django_template                  | 19.4 ms                                                    | 21.7 ms: 1.12x slower                                      |
| bench_thread_pool                | 447 us                                                     | 500 us: 1.12x slower                                       |
| scimark_monte_carlo              | 42.5 ms                                                    | 47.5 ms: 1.12x slower                                      |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 3.11 ms: 1.12x slower                                      |
| genshi_xml                       | 29.9 ms                                                    | 33.6 ms: 1.12x slower                                      |
| hexiom                           | 4.06 ms                                                    | 4.57 ms: 1.13x slower                                      |
| scimark_fft                      | 181 ms                                                     | 204 ms: 1.13x slower                                       |
| genshi_text                      | 13.9 ms                                                    | 15.8 ms: 1.13x slower                                      |
| async_tree_eager_memoization     | 152 ms                                                     | 173 ms: 1.13x slower                                       |
| spectral_norm                    | 66.4 ms                                                    | 75.4 ms: 1.14x slower                                      |
| async_tree_eager                 | 60.3 ms                                                    | 68.6 ms: 1.14x slower                                      |
| deepcopy_memo                    | 22.6 us                                                    | 25.7 us: 1.14x slower                                      |
| deltablue                        | 2.14 ms                                                    | 2.44 ms: 1.14x slower                                      |
| chameleon                        | 4.27 ms                                                    | 4.87 ms: 1.14x slower                                      |
| async_tree_eager_tg              | 41.4 ms                                                    | 47.2 ms: 1.14x slower                                      |
| logging_format                   | 3.31 us                                                    | 3.79 us: 1.15x slower                                      |
| logging_simple                   | 3.04 us                                                    | 3.49 us: 1.15x slower                                      |
| html5lib                         | 31.2 ms                                                    | 35.9 ms: 1.15x slower                                      |
| logging_silent                   | 60.1 ns                                                    | 69.9 ns: 1.16x slower                                      |
| raytrace                         | 147 ms                                                     | 171 ms: 1.16x slower                                       |
| nqueens                          | 52.2 ms                                                    | 60.9 ms: 1.17x slower                                      |
| chaos                            | 34.0 ms                                                    | 39.8 ms: 1.17x slower                                      |
| tornado_http                     | 66.7 ms                                                    | 78.1 ms: 1.17x slower                                      |
| float                            | 48.6 ms                                                    | 56.9 ms: 1.17x slower                                      |
| coroutines                       | 15.8 ms                                                    | 18.7 ms: 1.18x slower                                      |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 531 ms: 1.18x slower                                       |
| async_tree_io_tg                 | 565 ms                                                     | 672 ms: 1.19x slower                                       |
| comprehensions                   | 10.2 us                                                    | 12.1 us: 1.19x slower                                      |
| async_tree_none                  | 209 ms                                                     | 253 ms: 1.21x slower                                       |
| generators                       | 22.9 ms                                                    | 28.4 ms: 1.24x slower                                      |
| async_tree_io                    | 563 ms                                                     | 703 ms: 1.25x slower                                       |
| gunicorn                         | 1.04 ms                                                    | 1.30 ms: 1.25x slower                                      |
| aiohttp                          | 997 us                                                     | 1.25 ms: 1.25x slower                                      |
| nbody                            | 59.6 ms                                                    | 75.6 ms: 1.27x slower                                      |
| async_tree_memoization           | 260 ms                                                     | 329 ms: 1.27x slower                                       |
| async_tree_none_tg               | 198 ms                                                     | 260 ms: 1.31x slower                                       |
| async_tree_memoization_tg        | 240 ms                                                     | 324 ms: 1.35x slower                                       |
| mypy2                            | 379 ms                                                     | 597 ms: 1.57x slower                                       |
| Geometric mean                   | (ref)                                                      | 1.08x slower                                               |

Benchmark hidden because not significant (4): pylint, asyncio_websockets, python_startup_no_site, asyncio_tcp
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, dask

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 0.94x
# Results vs. 3.13.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: darwin-arm64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 161 ms: 1.11x faster                                                  |
| docutils       | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                |
| html5lib       | 36.6 ms                                                | 31.9 ms: 1.15x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.4 ms: 1.21x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 59.3 ms: 1.19x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 41.2 ms: 1.18x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 258 ms: 1.12x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 124 ms: 1.12x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 154 ms: 1.10x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 248 ms: 1.09x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 197 ms: 1.07x faster                                                  |
| async_generators                 | 294 ms                                                 | 274 ms: 1.07x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 185 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 359 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 335 ms: 1.04x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 460 ms: 1.03x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 529 ms: 1.06x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 585 ms: 1.15x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 675 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 700 ms: 1.47x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, asyncio_tcp, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 48.8 ms: 1.15x faster                                                 |
| nbody          | 73.9 ms                                                | 65.7 ms: 1.13x faster                                                 |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 67.8 ms: 1.16x faster                                                 |
| regex_v8       | 16.9 ms                                                | 16.4 ms: 1.04x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.62 ms: 1.00x faster                                                 |
| regex_dna      | 148 ms                                                 | 148 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 182 us: 1.17x faster                                                  |
| unpickle_pure_python | 163 us                                                 | 140 us: 1.17x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 37.4 ms: 1.09x faster                                                 |
| xml_etree_generate   | 56.6 ms                                                | 52.3 ms: 1.08x faster                                                 |
| json_dumps           | 6.56 ms                                                | 6.20 ms: 1.06x faster                                                 |
| tomli_loads          | 1.56 sec                                               | 1.51 sec: 1.03x faster                                                |
| json_loads           | 16.9 us                                                | 16.5 us: 1.03x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 107 ms: 1.01x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 73.1 ms: 1.01x faster                                                 |
| unpickle             | 9.15 us                                                | 9.07 us: 1.01x faster                                                 |
| pickle               | 7.36 us                                                | 7.33 us: 1.00x faster                                                 |
| unpickle_list        | 2.93 us                                                | 3.00 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (2): pickle_dict, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 16.3 ms: 1.04x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 13.3 ms: 1.02x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.6 ms: 1.24x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 29.7 ms: 1.16x faster                                                 |
| django_template | 22.2 ms                                                | 19.7 ms: 1.13x faster                                                 |
| mako            | 7.68 ms                                                | 6.83 ms: 1.12x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.16x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.7 us: 1.63x faster                                                 |
| deepcopy                         | 232 us                                                 | 144 us: 1.62x faster                                                  |
| generators                       | 31.5 ms                                                | 20.6 ms: 1.53x faster                                                 |
| go                               | 115 ms                                                 | 81.6 ms: 1.41x faster                                                 |
| deepcopy_reduce                  | 2.06 us                                                | 1.50 us: 1.37x faster                                                 |
| unpack_sequence                  | 36.1 ns                                                | 28.1 ns: 1.28x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 13.6 ms: 1.24x faster                                                 |
| coroutines                       | 19.8 ms                                                | 16.4 ms: 1.21x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.22 ms: 1.21x faster                                                 |
| nqueens                          | 62.9 ms                                                | 52.2 ms: 1.20x faster                                                 |
| raytrace                         | 182 ms                                                 | 151 ms: 1.20x faster                                                  |
| hexiom                           | 4.85 ms                                                | 4.08 ms: 1.19x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 59.3 ms: 1.19x faster                                                 |
| logging_simple                   | 3.57 us                                                | 3.04 us: 1.18x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 41.2 ms: 1.18x faster                                                 |
| scimark_lu                       | 76.5 ms                                                | 65.2 ms: 1.17x faster                                                 |
| pickle_pure_python               | 213 us                                                 | 182 us: 1.17x faster                                                  |
| unpickle_pure_python             | 163 us                                                 | 140 us: 1.17x faster                                                  |
| sqlglot_parse                    | 856 us                                                 | 736 us: 1.16x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.32 us: 1.16x faster                                                 |
| pprint_safe_repr                 | 531 ms                                                 | 458 ms: 1.16x faster                                                  |
| regex_compile                    | 78.5 ms                                                | 67.8 ms: 1.16x faster                                                 |
| genshi_xml                       | 34.4 ms                                                | 29.7 ms: 1.16x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 43.7 ms: 1.15x faster                                                 |
| pprint_pformat                   | 1.08 sec                                               | 936 ms: 1.15x faster                                                  |
| float                            | 56.2 ms                                                | 48.8 ms: 1.15x faster                                                 |
| html5lib                         | 36.6 ms                                                | 31.9 ms: 1.15x faster                                                 |
| chaos                            | 41.3 ms                                                | 36.0 ms: 1.15x faster                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 899 us: 1.14x faster                                                  |
| logging_silent                   | 69.9 ns                                                | 61.5 ns: 1.14x faster                                                 |
| sqlglot_normalize                | 189 ms                                                 | 166 ms: 1.14x faster                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 30.8 ms: 1.14x faster                                                 |
| django_template                  | 22.2 ms                                                | 19.7 ms: 1.13x faster                                                 |
| nbody                            | 73.9 ms                                                | 65.7 ms: 1.13x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 258 ms: 1.12x faster                                                  |
| mako                             | 7.68 ms                                                | 6.83 ms: 1.12x faster                                                 |
| richards                         | 35.4 ms                                                | 31.6 ms: 1.12x faster                                                 |
| thrift                           | 466 us                                                 | 416 us: 1.12x faster                                                  |
| richards_super                   | 39.1 ms                                                | 35.0 ms: 1.12x faster                                                 |
| pycparser                        | 706 ms                                                 | 632 ms: 1.12x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 124 ms: 1.12x faster                                                  |
| comprehensions                   | 12.2 us                                                | 10.9 us: 1.11x faster                                                 |
| bench_thread_pool                | 506 us                                                 | 455 us: 1.11x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 95.5 ms: 1.11x faster                                                 |
| 2to3                             | 178 ms                                                 | 161 ms: 1.11x faster                                                  |
| sympy_str                        | 145 ms                                                 | 132 ms: 1.10x faster                                                  |
| sympy_sum                        | 75.6 ms                                                | 68.8 ms: 1.10x faster                                                 |
| spectral_norm                    | 77.3 ms                                                | 70.3 ms: 1.10x faster                                                 |
| async_tree_eager_memoization     | 169 ms                                                 | 154 ms: 1.10x faster                                                  |
| sympy_expand                     | 246 ms                                                 | 224 ms: 1.10x faster                                                  |
| xml_etree_process                | 40.9 ms                                                | 37.4 ms: 1.09x faster                                                 |
| async_tree_memoization           | 270 ms                                                 | 248 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.75 ms: 1.09x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 92.8 us: 1.09x faster                                                 |
| xml_etree_generate               | 56.6 ms                                                | 52.3 ms: 1.08x faster                                                 |
| pyflate                          | 351 ms                                                 | 325 ms: 1.08x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 197 ms: 1.07x faster                                                  |
| async_generators                 | 294 ms                                                 | 274 ms: 1.07x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 187 ms: 1.07x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 185 ms: 1.07x faster                                                  |
| fannkuch                         | 282 ms                                                 | 263 ms: 1.07x faster                                                  |
| pathlib                          | 22.8 ms                                                | 21.4 ms: 1.06x faster                                                 |
| json_dumps                       | 6.56 ms                                                | 6.20 ms: 1.06x faster                                                 |
| coverage                         | 46.1 ms                                                | 43.7 ms: 1.05x faster                                                 |
| crypto_pyaes                     | 54.0 ms                                                | 51.3 ms: 1.05x faster                                                 |
| telco                            | 4.80 ms                                                | 4.56 ms: 1.05x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 27.4 ms: 1.05x faster                                                 |
| bench_mp_pool                    | 50.9 ms                                                | 48.6 ms: 1.05x faster                                                 |
| mdp                              | 1.50 sec                                               | 1.44 sec: 1.04x faster                                                |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 359 ms: 1.04x faster                                                  |
| json                             | 2.94 ms                                                | 2.82 ms: 1.04x faster                                                 |
| python_startup                   | 17.0 ms                                                | 16.3 ms: 1.04x faster                                                 |
| sympy_integrate                  | 11.3 ms                                                | 10.9 ms: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 335 ms: 1.04x faster                                                  |
| bpe_tokeniser                    | 3.24 sec                                               | 3.13 sec: 1.04x faster                                                |
| regex_v8                         | 16.9 ms                                                | 16.4 ms: 1.04x faster                                                 |
| docutils                         | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                |
| meteor_contest                   | 73.8 ms                                                | 71.6 ms: 1.03x faster                                                 |
| tomli_loads                      | 1.56 sec                                               | 1.51 sec: 1.03x faster                                                |
| sqlite_synth                     | 1.54 us                                                | 1.50 us: 1.03x faster                                                 |
| json_loads                       | 16.9 us                                                | 16.5 us: 1.03x faster                                                 |
| python_startup_no_site           | 13.7 ms                                                | 13.3 ms: 1.02x faster                                                 |
| xml_etree_parse                  | 109 ms                                                 | 107 ms: 1.01x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 73.1 ms: 1.01x faster                                                 |
| unpickle                         | 9.15 us                                                | 9.07 us: 1.01x faster                                                 |
| gc_traversal                     | 2.48 ms                                                | 2.47 ms: 1.00x faster                                                 |
| pickle                           | 7.36 us                                                | 7.33 us: 1.00x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.62 ms: 1.00x faster                                                 |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                  |
| regex_dna                        | 148 ms                                                 | 148 ms: 1.00x slower                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                |
| unpickle_list                    | 2.93 us                                                | 3.00 us: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 460 ms: 1.03x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 529 ms: 1.06x slower                                                  |
| create_gc_cycles                 | 803 us                                                 | 900 us: 1.12x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 585 ms: 1.15x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 675 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 700 ms: 1.47x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (7): tornado_http, pylint, async_tree_cpu_io_mixed, asyncio_tcp, asyncio_websockets, pickle_dict, pickle_list
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.00x
# Results vs. 3.13.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: darwin-arm64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.03x faster
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 181 ms: 1.02x slower                                                  |
| docutils       | 1.44 sec                                               | 1.60 sec: 1.11x slower                                                |
| html5lib       | 36.6 ms                                                | 34.2 ms: 1.07x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.2 ms: 1.22x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 41.6 ms: 1.16x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 260 ms: 1.12x faster                                                  |
| async_tree_eager                 | 70.5 ms                                                | 63.5 ms: 1.11x faster                                                 |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 126 ms: 1.10x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 251 ms: 1.08x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 158 ms: 1.07x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 187 ms: 1.06x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 201 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 335 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 364 ms: 1.03x faster                                                  |
| async_generators                 | 294 ms                                                 | 291 ms: 1.01x faster                                                  |
| asyncio_websockets               | 241 ms                                                 | 242 ms: 1.00x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 458 ms: 1.02x slower                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.30 sec: 1.03x slower                                                |
| async_tree_io_tg                 | 500 ms                                                 | 573 ms: 1.15x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 583 ms: 1.15x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 677 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 701 ms: 1.47x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (2): asyncio_tcp, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 46.7 ms: 1.20x faster                                                 |
| nbody          | 73.9 ms                                                | 63.6 ms: 1.16x faster                                                 |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 76.0 ms: 1.03x faster                                                 |
| regex_v8       | 16.9 ms                                                | 16.9 ms: 1.00x faster                                                 |
| regex_dna      | 148 ms                                                 | 149 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 163 us                                                 | 130 us: 1.26x faster                                                  |
| tomli_loads          | 1.56 sec                                               | 1.26 sec: 1.24x faster                                                |
| pickle_pure_python   | 213 us                                                 | 176 us: 1.21x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 34.6 ms: 1.18x faster                                                 |
| xml_etree_generate   | 56.6 ms                                                | 50.1 ms: 1.13x faster                                                 |
| json_dumps           | 6.56 ms                                                | 6.14 ms: 1.07x faster                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 70.7 ms: 1.05x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.05x faster                                                  |
| json_loads           | 16.9 us                                                | 16.5 us: 1.02x faster                                                 |
| unpickle             | 9.15 us                                                | 9.01 us: 1.02x faster                                                 |
| pickle_list          | 2.99 us                                                | 2.97 us: 1.01x faster                                                 |
| pickle_dict          | 18.2 us                                                | 18.1 us: 1.00x faster                                                 |
| pickle               | 7.36 us                                                | 7.43 us: 1.01x slower                                                 |
| unpickle_list        | 2.93 us                                                | 2.99 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 18.2 ms: 1.07x slower                                                 |
| python_startup_no_site | 13.7 ms                                                | 15.2 ms: 1.12x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.39 ms: 1.20x faster                                                 |
| genshi_text     | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                 |
| django_template | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                 |
| genshi_xml      | 34.4 ms                                                | 42.7 ms: 1.24x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.5 us: 1.65x faster                                                 |
| deepcopy                         | 232 us                                                 | 157 us: 1.48x faster                                                  |
| deepcopy_reduce                  | 2.06 us                                                | 1.52 us: 1.35x faster                                                 |
| unpickle_pure_python             | 163 us                                                 | 130 us: 1.26x faster                                                  |
| generators                       | 31.5 ms                                                | 25.4 ms: 1.24x faster                                                 |
| tomli_loads                      | 1.56 sec                                               | 1.26 sec: 1.24x faster                                                |
| coroutines                       | 19.8 ms                                                | 16.2 ms: 1.22x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 87.3 ms: 1.21x faster                                                 |
| pickle_pure_python               | 213 us                                                 | 176 us: 1.21x faster                                                  |
| float                            | 56.2 ms                                                | 46.7 ms: 1.20x faster                                                 |
| mako                             | 7.68 ms                                                | 6.39 ms: 1.20x faster                                                 |
| scimark_lu                       | 76.5 ms                                                | 64.0 ms: 1.19x faster                                                 |
| xml_etree_process                | 40.9 ms                                                | 34.6 ms: 1.18x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 41.6 ms: 1.16x faster                                                 |
| nbody                            | 73.9 ms                                                | 63.6 ms: 1.16x faster                                                 |
| logging_simple                   | 3.57 us                                                | 3.08 us: 1.16x faster                                                 |
| spectral_norm                    | 77.3 ms                                                | 67.0 ms: 1.15x faster                                                 |
| logging_silent                   | 69.9 ns                                                | 60.7 ns: 1.15x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.35 us: 1.15x faster                                                 |
| go                               | 115 ms                                                 | 101 ms: 1.14x faster                                                  |
| xml_etree_generate               | 56.6 ms                                                | 50.1 ms: 1.13x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 260 ms: 1.12x faster                                                  |
| thrift                           | 466 us                                                 | 419 us: 1.11x faster                                                  |
| deltablue                        | 2.68 ms                                                | 2.41 ms: 1.11x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 63.5 ms: 1.11x faster                                                 |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 126 ms: 1.10x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 184 ms: 1.09x faster                                                  |
| pyflate                          | 351 ms                                                 | 323 ms: 1.09x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 251 ms: 1.08x faster                                                  |
| html5lib                         | 36.6 ms                                                | 34.2 ms: 1.07x faster                                                 |
| telco                            | 4.80 ms                                                | 4.49 ms: 1.07x faster                                                 |
| async_tree_eager_memoization     | 169 ms                                                 | 158 ms: 1.07x faster                                                  |
| json_dumps                       | 6.56 ms                                                | 6.14 ms: 1.07x faster                                                 |
| nqueens                          | 62.9 ms                                                | 59.0 ms: 1.07x faster                                                 |
| fannkuch                         | 282 ms                                                 | 265 ms: 1.06x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 187 ms: 1.06x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 1.01 sec: 1.06x faster                                                |
| pprint_safe_repr                 | 531 ms                                                 | 501 ms: 1.06x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 95.5 us: 1.06x faster                                                 |
| bpe_tokeniser                    | 3.24 sec                                               | 3.07 sec: 1.06x faster                                                |
| scimark_monte_carlo              | 50.4 ms                                                | 47.8 ms: 1.05x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 201 ms: 1.05x faster                                                  |
| bench_thread_pool                | 506 us                                                 | 482 us: 1.05x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 70.7 ms: 1.05x faster                                                 |
| coverage                         | 46.1 ms                                                | 44.0 ms: 1.05x faster                                                 |
| xml_etree_parse                  | 109 ms                                                 | 104 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 335 ms: 1.04x faster                                                  |
| pycparser                        | 706 ms                                                 | 679 ms: 1.04x faster                                                  |
| crypto_pyaes                     | 54.0 ms                                                | 52.3 ms: 1.03x faster                                                 |
| hexiom                           | 4.85 ms                                                | 4.70 ms: 1.03x faster                                                 |
| regex_compile                    | 78.5 ms                                                | 76.0 ms: 1.03x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 364 ms: 1.03x faster                                                  |
| pathlib                          | 22.8 ms                                                | 22.2 ms: 1.03x faster                                                 |
| raytrace                         | 182 ms                                                 | 177 ms: 1.03x faster                                                  |
| json_loads                       | 16.9 us                                                | 16.5 us: 1.02x faster                                                 |
| json                             | 2.94 ms                                                | 2.88 ms: 1.02x faster                                                 |
| chaos                            | 41.3 ms                                                | 40.5 ms: 1.02x faster                                                 |
| unpickle                         | 9.15 us                                                | 9.01 us: 1.02x faster                                                 |
| mdp                              | 1.50 sec                                               | 1.48 sec: 1.01x faster                                                |
| sqlite_synth                     | 1.54 us                                                | 1.53 us: 1.01x faster                                                 |
| async_generators                 | 294 ms                                                 | 291 ms: 1.01x faster                                                  |
| sqlglot_parse                    | 856 us                                                 | 848 us: 1.01x faster                                                  |
| pickle_list                      | 2.99 us                                                | 2.97 us: 1.01x faster                                                 |
| gc_traversal                     | 2.48 ms                                                | 2.47 ms: 1.01x faster                                                 |
| regex_v8                         | 16.9 ms                                                | 16.9 ms: 1.00x faster                                                 |
| sympy_expand                     | 246 ms                                                 | 246 ms: 1.00x faster                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.99 ms: 1.00x faster                                                 |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                  |
| sqlglot_normalize                | 189 ms                                                 | 188 ms: 1.00x faster                                                  |
| pickle_dict                      | 18.2 us                                                | 18.1 us: 1.00x faster                                                 |
| asyncio_websockets               | 241 ms                                                 | 242 ms: 1.00x slower                                                  |
| pickle                           | 7.36 us                                                | 7.43 us: 1.01x slower                                                 |
| regex_dna                        | 148 ms                                                 | 149 ms: 1.01x slower                                                  |
| dulwich_log                      | 28.7 ms                                                | 29.0 ms: 1.01x slower                                                 |
| 2to3                             | 178 ms                                                 | 181 ms: 1.02x slower                                                  |
| meteor_contest                   | 73.8 ms                                                | 75.1 ms: 1.02x slower                                                 |
| genshi_text                      | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 1.05 ms: 1.02x slower                                                 |
| unpickle_list                    | 2.93 us                                                | 2.99 us: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 458 ms: 1.02x slower                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.30 sec: 1.03x slower                                                |
| sympy_str                        | 145 ms                                                 | 150 ms: 1.03x slower                                                  |
| sympy_sum                        | 75.6 ms                                                | 78.9 ms: 1.04x slower                                                 |
| django_template                  | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                 |
| comprehensions                   | 12.2 us                                                | 12.9 us: 1.06x slower                                                 |
| python_startup                   | 17.0 ms                                                | 18.2 ms: 1.07x slower                                                 |
| sqlglot_optimize                 | 34.9 ms                                                | 37.8 ms: 1.08x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.60 sec: 1.11x slower                                                |
| sympy_integrate                  | 11.3 ms                                                | 12.6 ms: 1.11x slower                                                 |
| python_startup_no_site           | 13.7 ms                                                | 15.2 ms: 1.12x slower                                                 |
| create_gc_cycles                 | 803 us                                                 | 899 us: 1.12x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 573 ms: 1.15x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 583 ms: 1.15x slower                                                  |
| pylint                           | 181 ms                                                 | 214 ms: 1.18x slower                                                  |
| richards_super                   | 39.1 ms                                                | 46.6 ms: 1.19x slower                                                 |
| genshi_xml                       | 34.4 ms                                                | 42.7 ms: 1.24x slower                                                 |
| richards                         | 35.4 ms                                                | 45.2 ms: 1.28x slower                                                 |
| async_tree_eager_io              | 513 ms                                                 | 677 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 701 ms: 1.47x slower                                                  |
| unpack_sequence                  | 36.1 ns                                                | 76.8 ns: 2.13x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (5): tornado_http, asyncio_tcp, async_tree_cpu_io_mixed, regex_effbot, bench_mp_pool
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.87% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x
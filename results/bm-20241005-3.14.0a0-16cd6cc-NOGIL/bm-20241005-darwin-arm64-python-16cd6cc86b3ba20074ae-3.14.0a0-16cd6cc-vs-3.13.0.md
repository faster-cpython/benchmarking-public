# Results vs. 3.13.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: darwin-arm64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.28x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 249 ms: 1.40x slower                                                  |
| docutils       | 1.44 sec                                               | 1.76 sec: 1.22x slower                                                |
| html5lib       | 36.6 ms                                                | 53.2 ms: 1.45x slower                                                 |
| tornado_http   | 77.2 ms                                                | 104 ms: 1.35x slower                                                  |
| Geometric mean | (ref)                                                  | 1.35x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_tcp                      | 457 ms                                                 | 385 ms: 1.19x faster                                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 266 ms: 1.09x faster                                                  |
| async_tree_eager_io              | 513 ms                                                 | 490 ms: 1.05x faster                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 465 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.23 sec: 1.02x faster                                                |
| asyncio_websockets               | 241 ms                                                 | 239 ms: 1.01x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 207 ms: 1.04x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 466 ms: 1.04x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 530 ms: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 370 ms: 1.06x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 398 ms: 1.06x slower                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 490 ms: 1.07x slower                                                  |
| async_tree_memoization           | 270 ms                                                 | 292 ms: 1.08x slower                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 187 ms: 1.11x slower                                                  |
| async_tree_none                  | 212 ms                                                 | 235 ms: 1.11x slower                                                  |
| async_generators                 | 294 ms                                                 | 332 ms: 1.13x slower                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 162 ms: 1.17x slower                                                  |
| coroutines                       | 19.8 ms                                                | 24.7 ms: 1.25x slower                                                 |
| async_tree_eager                 | 70.5 ms                                                | 106 ms: 1.50x slower                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 75.5 ms: 1.56x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.08x slower                                                          |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| float          | 56.2 ms                                                | 93.0 ms: 1.65x slower                                                 |
| nbody          | 73.9 ms                                                | 154 ms: 2.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.51x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.51 ms: 1.05x faster                                                 |
| regex_dna      | 148 ms                                                 | 146 ms: 1.01x faster                                                  |
| regex_v8       | 16.9 ms                                                | 17.4 ms: 1.03x slower                                                 |
| regex_compile  | 78.5 ms                                                | 119 ms: 1.52x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle               | 7.36 us                                                | 7.03 us: 1.05x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.05x faster                                                  |
| pickle_list          | 2.99 us                                                | 2.97 us: 1.01x faster                                                 |
| pickle_dict          | 18.2 us                                                | 18.5 us: 1.02x slower                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 75.9 ms: 1.02x slower                                                 |
| unpickle             | 9.15 us                                                | 9.46 us: 1.03x slower                                                 |
| json_loads           | 16.9 us                                                | 18.5 us: 1.10x slower                                                 |
| unpickle_list        | 2.93 us                                                | 3.26 us: 1.11x slower                                                 |
| xml_etree_generate   | 56.6 ms                                                | 67.9 ms: 1.20x slower                                                 |
| json_dumps           | 6.56 ms                                                | 7.91 ms: 1.20x slower                                                 |
| tomli_loads          | 1.56 sec                                               | 1.99 sec: 1.28x slower                                                |
| xml_etree_process    | 40.9 ms                                                | 56.3 ms: 1.38x slower                                                 |
| unpickle_pure_python | 163 us                                                 | 262 us: 1.61x slower                                                  |
| pickle_pure_python   | 213 us                                                 | 346 us: 1.62x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.16x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 13.9 ms: 1.02x slower                                                 |
| python_startup         | 17.0 ms                                                | 17.4 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 34.4 ms                                                | 49.8 ms: 1.45x slower                                                 |
| genshi_text     | 16.9 ms                                                | 24.7 ms: 1.46x slower                                                 |
| django_template | 22.2 ms                                                | 36.1 ms: 1.63x slower                                                 |
| mako            | 7.68 ms                                                | 13.3 ms: 1.73x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.56x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| sqlglot_normalize                | 189 ms                                                 | 103 ms: 1.83x faster                                                  |
| gc_traversal                     | 2.48 ms                                                | 2.05 ms: 1.21x faster                                                 |
| asyncio_tcp                      | 457 ms                                                 | 385 ms: 1.19x faster                                                  |
| create_gc_cycles                 | 803 us                                                 | 679 us: 1.18x faster                                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 266 ms: 1.09x faster                                                  |
| pickle                           | 7.36 us                                                | 7.03 us: 1.05x faster                                                 |
| async_tree_eager_io              | 513 ms                                                 | 490 ms: 1.05x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.51 ms: 1.05x faster                                                 |
| xml_etree_parse                  | 109 ms                                                 | 104 ms: 1.05x faster                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 465 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.23 sec: 1.02x faster                                                |
| sqlite_synth                     | 1.54 us                                                | 1.52 us: 1.02x faster                                                 |
| regex_dna                        | 148 ms                                                 | 146 ms: 1.01x faster                                                  |
| asyncio_websockets               | 241 ms                                                 | 239 ms: 1.01x faster                                                  |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| pickle_list                      | 2.99 us                                                | 2.97 us: 1.01x faster                                                 |
| pickle_dict                      | 18.2 us                                                | 18.5 us: 1.02x slower                                                 |
| python_startup_no_site           | 13.7 ms                                                | 13.9 ms: 1.02x slower                                                 |
| python_startup                   | 17.0 ms                                                | 17.4 ms: 1.02x slower                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 75.9 ms: 1.02x slower                                                 |
| regex_v8                         | 16.9 ms                                                | 17.4 ms: 1.03x slower                                                 |
| unpickle                         | 9.15 us                                                | 9.46 us: 1.03x slower                                                 |
| async_tree_none_tg               | 198 ms                                                 | 207 ms: 1.04x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 466 ms: 1.04x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 530 ms: 1.05x slower                                                  |
| deepcopy                         | 232 us                                                 | 243 us: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 370 ms: 1.06x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 398 ms: 1.06x slower                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 490 ms: 1.07x slower                                                  |
| async_tree_memoization           | 270 ms                                                 | 292 ms: 1.08x slower                                                  |
| json_loads                       | 16.9 us                                                | 18.5 us: 1.10x slower                                                 |
| pathlib                          | 22.8 ms                                                | 25.1 ms: 1.10x slower                                                 |
| async_tree_eager_memoization     | 169 ms                                                 | 187 ms: 1.11x slower                                                  |
| async_tree_none                  | 212 ms                                                 | 235 ms: 1.11x slower                                                  |
| generators                       | 31.5 ms                                                | 35.0 ms: 1.11x slower                                                 |
| unpickle_list                    | 2.93 us                                                | 3.26 us: 1.11x slower                                                 |
| deepcopy_memo                    | 27.2 us                                                | 30.6 us: 1.12x slower                                                 |
| bench_mp_pool                    | 50.9 ms                                                | 57.2 ms: 1.12x slower                                                 |
| telco                            | 4.80 ms                                                | 5.42 ms: 1.13x slower                                                 |
| async_generators                 | 294 ms                                                 | 332 ms: 1.13x slower                                                  |
| json                             | 2.94 ms                                                | 3.33 ms: 1.13x slower                                                 |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 162 ms: 1.17x slower                                                  |
| coverage                         | 46.1 ms                                                | 54.4 ms: 1.18x slower                                                 |
| deepcopy_reduce                  | 2.06 us                                                | 2.45 us: 1.19x slower                                                 |
| pylint                           | 181 ms                                                 | 217 ms: 1.20x slower                                                  |
| xml_etree_generate               | 56.6 ms                                                | 67.9 ms: 1.20x slower                                                 |
| meteor_contest                   | 73.8 ms                                                | 88.9 ms: 1.20x slower                                                 |
| json_dumps                       | 6.56 ms                                                | 7.91 ms: 1.20x slower                                                 |
| nqueens                          | 62.9 ms                                                | 76.4 ms: 1.22x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.76 sec: 1.22x slower                                                |
| bpe_tokeniser                    | 3.24 sec                                               | 3.97 sec: 1.22x slower                                                |
| coroutines                       | 19.8 ms                                                | 24.7 ms: 1.25x slower                                                 |
| mdp                              | 1.50 sec                                               | 1.88 sec: 1.25x slower                                                |
| fannkuch                         | 282 ms                                                 | 354 ms: 1.26x slower                                                  |
| tomli_loads                      | 1.56 sec                                               | 1.99 sec: 1.28x slower                                                |
| pycparser                        | 706 ms                                                 | 915 ms: 1.30x slower                                                  |
| scimark_fft                      | 201 ms                                                 | 266 ms: 1.33x slower                                                  |
| tornado_http                     | 77.2 ms                                                | 104 ms: 1.35x slower                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 4.07 ms: 1.36x slower                                                 |
| xml_etree_process                | 40.9 ms                                                | 56.3 ms: 1.38x slower                                                 |
| pyflate                          | 351 ms                                                 | 490 ms: 1.39x slower                                                  |
| 2to3                             | 178 ms                                                 | 249 ms: 1.40x slower                                                  |
| typing_runtime_protocols         | 101 us                                                 | 142 us: 1.40x slower                                                  |
| dulwich_log                      | 28.7 ms                                                | 40.9 ms: 1.42x slower                                                 |
| thrift                           | 466 us                                                 | 667 us: 1.43x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 16.3 ms: 1.44x slower                                                 |
| crypto_pyaes                     | 54.0 ms                                                | 77.8 ms: 1.44x slower                                                 |
| genshi_xml                       | 34.4 ms                                                | 49.8 ms: 1.45x slower                                                 |
| html5lib                         | 36.6 ms                                                | 53.2 ms: 1.45x slower                                                 |
| genshi_text                      | 16.9 ms                                                | 24.7 ms: 1.46x slower                                                 |
| sqlglot_optimize                 | 34.9 ms                                                | 51.6 ms: 1.48x slower                                                 |
| async_tree_eager                 | 70.5 ms                                                | 106 ms: 1.50x slower                                                  |
| regex_compile                    | 78.5 ms                                                | 119 ms: 1.52x slower                                                  |
| pprint_safe_repr                 | 531 ms                                                 | 810 ms: 1.53x slower                                                  |
| pprint_pformat                   | 1.08 sec                                               | 1.65 sec: 1.53x slower                                                |
| comprehensions                   | 12.2 us                                                | 18.7 us: 1.54x slower                                                 |
| spectral_norm                    | 77.3 ms                                                | 119 ms: 1.54x slower                                                  |
| scimark_sor                      | 106 ms                                                 | 164 ms: 1.55x slower                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 78.4 ms: 1.55x slower                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 75.5 ms: 1.56x slower                                                 |
| richards                         | 35.4 ms                                                | 55.6 ms: 1.57x slower                                                 |
| bench_thread_pool                | 506 us                                                 | 798 us: 1.58x slower                                                  |
| go                               | 115 ms                                                 | 182 ms: 1.58x slower                                                  |
| hexiom                           | 4.85 ms                                                | 7.74 ms: 1.59x slower                                                 |
| sympy_str                        | 145 ms                                                 | 233 ms: 1.60x slower                                                  |
| unpickle_pure_python             | 163 us                                                 | 262 us: 1.61x slower                                                  |
| pickle_pure_python               | 213 us                                                 | 346 us: 1.62x slower                                                  |
| django_template                  | 22.2 ms                                                | 36.1 ms: 1.63x slower                                                 |
| richards_super                   | 39.1 ms                                                | 64.7 ms: 1.65x slower                                                 |
| float                            | 56.2 ms                                                | 93.0 ms: 1.65x slower                                                 |
| logging_simple                   | 3.57 us                                                | 6.10 us: 1.71x slower                                                 |
| logging_format                   | 3.85 us                                                | 6.64 us: 1.72x slower                                                 |
| mako                             | 7.68 ms                                                | 13.3 ms: 1.73x slower                                                 |
| sympy_expand                     | 246 ms                                                 | 427 ms: 1.73x slower                                                  |
| chaos                            | 41.3 ms                                                | 74.7 ms: 1.81x slower                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 1.90 ms: 1.85x slower                                                 |
| sympy_sum                        | 75.6 ms                                                | 141 ms: 1.86x slower                                                  |
| scimark_lu                       | 76.5 ms                                                | 145 ms: 1.90x slower                                                  |
| sqlglot_parse                    | 856 us                                                 | 1.65 ms: 1.93x slower                                                 |
| logging_silent                   | 69.9 ns                                                | 136 ns: 1.94x slower                                                  |
| raytrace                         | 182 ms                                                 | 373 ms: 2.05x slower                                                  |
| nbody                            | 73.9 ms                                                | 154 ms: 2.09x slower                                                  |
| deltablue                        | 2.68 ms                                                | 5.61 ms: 2.09x slower                                                 |
| unpack_sequence                  | 36.1 ns                                                | 96.0 ns: 2.66x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.28x slower                                                          |

Benchmark hidden because not significant (1): async_tree_io_tg
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.21x
- 95% likely to have a slowdown of 1.20x
- 99% likely to have a slowdown of 1.17x

# Memory
- memory change: 1.00x
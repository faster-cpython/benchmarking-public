# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: darwin-arm64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.28x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 246 ms: 1.39x slower                                                  |
| docutils       | 1.44 sec                                               | 1.75 sec: 1.21x slower                                                |
| html5lib       | 36.6 ms                                                | 51.2 ms: 1.40x slower                                                 |
| tornado_http   | 77.2 ms                                                | 127 ms: 1.65x slower                                                  |
| Geometric mean | (ref)                                                  | 1.40x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_tcp                      | 457 ms                                                 | 335 ms: 1.36x faster                                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 263 ms: 1.10x faster                                                  |
| async_tree_eager_io              | 513 ms                                                 | 484 ms: 1.06x faster                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 464 ms: 1.03x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.24 sec: 1.02x faster                                                |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 460 ms: 1.03x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 525 ms: 1.04x slower                                                  |
| async_tree_none_tg               | 198 ms                                                 | 206 ms: 1.04x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 367 ms: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 395 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 485 ms: 1.06x slower                                                  |
| async_tree_memoization           | 270 ms                                                 | 288 ms: 1.06x slower                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 184 ms: 1.09x slower                                                  |
| async_tree_none                  | 212 ms                                                 | 233 ms: 1.10x slower                                                  |
| async_generators                 | 294 ms                                                 | 331 ms: 1.13x slower                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 159 ms: 1.15x slower                                                  |
| coroutines                       | 19.8 ms                                                | 25.0 ms: 1.26x slower                                                 |
| async_tree_eager                 | 70.5 ms                                                | 106 ms: 1.51x slower                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 74.9 ms: 1.55x slower                                                 |
| asyncio_websockets               | 241 ms                                                 | 405 ms: 1.68x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.09x slower                                                          |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| float          | 56.2 ms                                                | 93.8 ms: 1.67x slower                                                 |
| nbody          | 73.9 ms                                                | 154 ms: 2.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.51x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.44 ms: 1.08x faster                                                 |
| regex_dna      | 148 ms                                                 | 139 ms: 1.06x faster                                                  |
| regex_v8       | 16.9 ms                                                | 17.1 ms: 1.01x slower                                                 |
| regex_compile  | 78.5 ms                                                | 119 ms: 1.52x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle               | 7.36 us                                                | 7.05 us: 1.04x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.04x faster                                                  |
| pickle_list          | 2.99 us                                                | 2.90 us: 1.03x faster                                                 |
| pickle_dict          | 18.2 us                                                | 18.4 us: 1.01x slower                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 75.6 ms: 1.02x slower                                                 |
| unpickle             | 9.15 us                                                | 9.72 us: 1.06x slower                                                 |
| unpickle_list        | 2.93 us                                                | 3.25 us: 1.11x slower                                                 |
| json_loads           | 16.9 us                                                | 18.8 us: 1.11x slower                                                 |
| json_dumps           | 6.56 ms                                                | 7.74 ms: 1.18x slower                                                 |
| xml_etree_generate   | 56.6 ms                                                | 68.1 ms: 1.20x slower                                                 |
| tomli_loads          | 1.56 sec                                               | 1.99 sec: 1.28x slower                                                |
| xml_etree_process    | 40.9 ms                                                | 57.2 ms: 1.40x slower                                                 |
| unpickle_pure_python | 163 us                                                 | 262 us: 1.61x slower                                                  |
| pickle_pure_python   | 213 us                                                 | 346 us: 1.63x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.16x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 13.6 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 34.4 ms                                                | 49.6 ms: 1.44x slower                                                 |
| genshi_text     | 16.9 ms                                                | 24.9 ms: 1.48x slower                                                 |
| django_template | 22.2 ms                                                | 35.3 ms: 1.59x slower                                                 |
| mako            | 7.68 ms                                                | 13.3 ms: 1.73x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.56x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| sqlglot_normalize                | 189 ms                                                 | 102 ms: 1.84x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 335 ms: 1.36x faster                                                  |
| gc_traversal                     | 2.48 ms                                                | 2.05 ms: 1.21x faster                                                 |
| create_gc_cycles                 | 803 us                                                 | 686 us: 1.17x faster                                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 263 ms: 1.10x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.44 ms: 1.08x faster                                                 |
| regex_dna                        | 148 ms                                                 | 139 ms: 1.06x faster                                                  |
| async_tree_eager_io              | 513 ms                                                 | 484 ms: 1.06x faster                                                  |
| pickle                           | 7.36 us                                                | 7.05 us: 1.04x faster                                                 |
| xml_etree_parse                  | 109 ms                                                 | 104 ms: 1.04x faster                                                  |
| pickle_list                      | 2.99 us                                                | 2.90 us: 1.03x faster                                                 |
| async_tree_eager_io_tg           | 477 ms                                                 | 464 ms: 1.03x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.24 sec: 1.02x faster                                                |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| sqlite_synth                     | 1.54 us                                                | 1.53 us: 1.01x faster                                                 |
| python_startup_no_site           | 13.7 ms                                                | 13.6 ms: 1.01x faster                                                 |
| regex_v8                         | 16.9 ms                                                | 17.1 ms: 1.01x slower                                                 |
| pickle_dict                      | 18.2 us                                                | 18.4 us: 1.01x slower                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 75.6 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 460 ms: 1.03x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 525 ms: 1.04x slower                                                  |
| async_tree_none_tg               | 198 ms                                                 | 206 ms: 1.04x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 367 ms: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 395 ms: 1.05x slower                                                  |
| deepcopy                         | 232 us                                                 | 245 us: 1.05x slower                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 485 ms: 1.06x slower                                                  |
| unpickle                         | 9.15 us                                                | 9.72 us: 1.06x slower                                                 |
| async_tree_memoization           | 270 ms                                                 | 288 ms: 1.06x slower                                                  |
| bench_mp_pool                    | 50.9 ms                                                | 54.9 ms: 1.08x slower                                                 |
| async_tree_eager_memoization     | 169 ms                                                 | 184 ms: 1.09x slower                                                  |
| generators                       | 31.5 ms                                                | 34.6 ms: 1.10x slower                                                 |
| async_tree_none                  | 212 ms                                                 | 233 ms: 1.10x slower                                                  |
| unpickle_list                    | 2.93 us                                                | 3.25 us: 1.11x slower                                                 |
| json_loads                       | 16.9 us                                                | 18.8 us: 1.11x slower                                                 |
| pathlib                          | 22.8 ms                                                | 25.6 ms: 1.12x slower                                                 |
| async_generators                 | 294 ms                                                 | 331 ms: 1.13x slower                                                  |
| json                             | 2.94 ms                                                | 3.35 ms: 1.14x slower                                                 |
| deepcopy_memo                    | 27.2 us                                                | 31.2 us: 1.14x slower                                                 |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 159 ms: 1.15x slower                                                  |
| json_dumps                       | 6.56 ms                                                | 7.74 ms: 1.18x slower                                                 |
| telco                            | 4.80 ms                                                | 5.69 ms: 1.19x slower                                                 |
| pylint                           | 181 ms                                                 | 215 ms: 1.19x slower                                                  |
| deepcopy_reduce                  | 2.06 us                                                | 2.46 us: 1.20x slower                                                 |
| nqueens                          | 62.9 ms                                                | 75.5 ms: 1.20x slower                                                 |
| meteor_contest                   | 73.8 ms                                                | 88.7 ms: 1.20x slower                                                 |
| xml_etree_generate               | 56.6 ms                                                | 68.1 ms: 1.20x slower                                                 |
| coverage                         | 46.1 ms                                                | 55.6 ms: 1.21x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.75 sec: 1.21x slower                                                |
| bpe_tokeniser                    | 3.24 sec                                               | 3.95 sec: 1.22x slower                                                |
| mdp                              | 1.50 sec                                               | 1.83 sec: 1.22x slower                                                |
| fannkuch                         | 282 ms                                                 | 352 ms: 1.25x slower                                                  |
| coroutines                       | 19.8 ms                                                | 25.0 ms: 1.26x slower                                                 |
| tomli_loads                      | 1.56 sec                                               | 1.99 sec: 1.28x slower                                                |
| pycparser                        | 706 ms                                                 | 913 ms: 1.29x slower                                                  |
| scimark_fft                      | 201 ms                                                 | 263 ms: 1.31x slower                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 4.06 ms: 1.36x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 15.4 ms: 1.36x slower                                                 |
| pyflate                          | 351 ms                                                 | 479 ms: 1.37x slower                                                  |
| 2to3                             | 178 ms                                                 | 246 ms: 1.39x slower                                                  |
| html5lib                         | 36.6 ms                                                | 51.2 ms: 1.40x slower                                                 |
| xml_etree_process                | 40.9 ms                                                | 57.2 ms: 1.40x slower                                                 |
| typing_runtime_protocols         | 101 us                                                 | 142 us: 1.41x slower                                                  |
| dulwich_log                      | 28.7 ms                                                | 40.7 ms: 1.42x slower                                                 |
| crypto_pyaes                     | 54.0 ms                                                | 77.4 ms: 1.43x slower                                                 |
| genshi_xml                       | 34.4 ms                                                | 49.6 ms: 1.44x slower                                                 |
| sqlglot_optimize                 | 34.9 ms                                                | 50.9 ms: 1.46x slower                                                 |
| thrift                           | 466 us                                                 | 679 us: 1.46x slower                                                  |
| genshi_text                      | 16.9 ms                                                | 24.9 ms: 1.48x slower                                                 |
| async_tree_eager                 | 70.5 ms                                                | 106 ms: 1.51x slower                                                  |
| regex_compile                    | 78.5 ms                                                | 119 ms: 1.52x slower                                                  |
| pprint_safe_repr                 | 531 ms                                                 | 808 ms: 1.52x slower                                                  |
| pprint_pformat                   | 1.08 sec                                               | 1.64 sec: 1.52x slower                                                |
| spectral_norm                    | 77.3 ms                                                | 118 ms: 1.52x slower                                                  |
| comprehensions                   | 12.2 us                                                | 18.7 us: 1.54x slower                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 74.9 ms: 1.55x slower                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 78.1 ms: 1.55x slower                                                 |
| scimark_sor                      | 106 ms                                                 | 165 ms: 1.56x slower                                                  |
| sympy_str                        | 145 ms                                                 | 227 ms: 1.56x slower                                                  |
| bench_thread_pool                | 506 us                                                 | 792 us: 1.57x slower                                                  |
| richards                         | 35.4 ms                                                | 55.6 ms: 1.57x slower                                                 |
| hexiom                           | 4.85 ms                                                | 7.63 ms: 1.57x slower                                                 |
| go                               | 115 ms                                                 | 181 ms: 1.58x slower                                                  |
| django_template                  | 22.2 ms                                                | 35.3 ms: 1.59x slower                                                 |
| unpickle_pure_python             | 163 us                                                 | 262 us: 1.61x slower                                                  |
| pickle_pure_python               | 213 us                                                 | 346 us: 1.63x slower                                                  |
| richards_super                   | 39.1 ms                                                | 64.3 ms: 1.64x slower                                                 |
| tornado_http                     | 77.2 ms                                                | 127 ms: 1.65x slower                                                  |
| float                            | 56.2 ms                                                | 93.8 ms: 1.67x slower                                                 |
| asyncio_websockets               | 241 ms                                                 | 405 ms: 1.68x slower                                                  |
| logging_simple                   | 3.57 us                                                | 6.05 us: 1.69x slower                                                 |
| sympy_expand                     | 246 ms                                                 | 421 ms: 1.71x slower                                                  |
| logging_format                   | 3.85 us                                                | 6.60 us: 1.71x slower                                                 |
| mako                             | 7.68 ms                                                | 13.3 ms: 1.73x slower                                                 |
| chaos                            | 41.3 ms                                                | 74.2 ms: 1.80x slower                                                 |
| sympy_sum                        | 75.6 ms                                                | 137 ms: 1.81x slower                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 1.88 ms: 1.84x slower                                                 |
| scimark_lu                       | 76.5 ms                                                | 144 ms: 1.88x slower                                                  |
| sqlglot_parse                    | 856 us                                                 | 1.64 ms: 1.92x slower                                                 |
| logging_silent                   | 69.9 ns                                                | 135 ns: 1.93x slower                                                  |
| raytrace                         | 182 ms                                                 | 373 ms: 2.05x slower                                                  |
| nbody                            | 73.9 ms                                                | 154 ms: 2.08x slower                                                  |
| deltablue                        | 2.68 ms                                                | 5.63 ms: 2.10x slower                                                 |
| unpack_sequence                  | 36.1 ns                                                | 96.0 ns: 2.66x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.28x slower                                                          |

Benchmark hidden because not significant (2): async_tree_io_tg, python_startup
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.21x
- 95% likely to have a slowdown of 1.20x
- 99% likely to have a slowdown of 1.18x

# Memory
- memory change: 0.99x
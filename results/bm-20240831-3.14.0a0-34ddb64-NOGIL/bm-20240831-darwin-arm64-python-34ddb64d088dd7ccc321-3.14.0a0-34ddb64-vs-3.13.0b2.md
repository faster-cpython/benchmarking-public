# Results vs. 3.13.0b2

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: darwin-arm64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.45x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x slower
- Memory change: 0.63x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 254 ms: 1.58x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.79 sec: 1.25x slower                                                |
| html5lib       | 31.2 ms                                                    | 52.3 ms: 1.68x slower                                                 |
| tornado_http   | 66.7 ms                                                    | 110 ms: 1.66x slower                                                  |
| Geometric mean | (ref)                                                      | 1.53x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io_tg           | 768 ms                                                     | 488 ms: 1.57x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 509 ms: 1.51x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 521 ms: 1.08x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 550 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 476 ms: 1.06x slower                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 504 ms: 1.08x slower                                                  |
| async_tree_none_tg               | 198 ms                                                     | 216 ms: 1.09x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 407 ms: 1.14x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 378 ms: 1.14x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 274 ms: 1.14x slower                                                  |
| async_tree_memoization           | 260 ms                                                     | 300 ms: 1.16x slower                                                  |
| async_tree_none                  | 209 ms                                                     | 243 ms: 1.16x slower                                                  |
| async_tree_eager_memoization     | 152 ms                                                     | 192 ms: 1.26x slower                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 167 ms: 1.33x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 111 ms: 1.84x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 78.6 ms: 1.90x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.11x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| float          | 48.6 ms                                                    | 98.7 ms: 2.03x slower                                                 |
| nbody          | 59.6 ms                                                    | 159 ms: 2.67x slower                                                  |
| Geometric mean | (ref)                                                      | 1.75x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 149 ms                                                     | 139 ms: 1.07x faster                                                  |
| regex_effbot   | 2.58 ms                                                    | 2.45 ms: 1.06x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                                 |
| regex_compile  | 68.5 ms                                                    | 125 ms: 1.83x slower                                                  |
| Geometric mean | (ref)                                                      | 1.13x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 71.5 ms                                                    | 78.2 ms: 1.09x slower                                                 |
| json_loads           | 16.8 us                                                    | 19.4 us: 1.15x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 8.12 ms: 1.30x slower                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 71.9 ms: 1.37x slower                                                 |
| tomli_loads          | 1.47 sec                                                   | 2.07 sec: 1.42x slower                                                |
| xml_etree_process    | 37.1 ms                                                    | 59.8 ms: 1.61x slower                                                 |
| unpickle_pure_python | 141 us                                                     | 280 us: 1.99x slower                                                  |
| pickle_pure_python   | 179 us                                                     | 365 us: 2.04x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.40x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 19.2 ms: 1.27x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 15.6 ms: 1.27x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.27x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 29.9 ms                                                    | 51.6 ms: 1.72x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 25.8 ms: 1.86x slower                                                 |
| django_template | 19.4 ms                                                    | 37.9 ms: 1.95x slower                                                 |
| mako            | 6.99 ms                                                    | 13.7 ms: 1.97x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.87x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io_tg           | 768 ms                                                     | 488 ms: 1.57x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 509 ms: 1.51x faster                                                  |
| sqlglot_normalize                | 166 ms                                                     | 110 ms: 1.50x faster                                                  |
| create_gc_cycles                 | 897 us                                                     | 696 us: 1.29x faster                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.05 ms: 1.19x faster                                                 |
| asyncio_tcp                      | 402 ms                                                     | 352 ms: 1.14x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 521 ms: 1.08x faster                                                  |
| regex_dna                        | 149 ms                                                     | 139 ms: 1.07x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.45 ms: 1.06x faster                                                 |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.25 sec: 1.04x faster                                                |
| async_tree_io                    | 563 ms                                                     | 550 ms: 1.02x faster                                                  |
| asyncio_websockets               | 409 ms                                                     | 405 ms: 1.01x faster                                                  |
| pidigits                         | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| regex_v8                         | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 476 ms: 1.06x slower                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 504 ms: 1.08x slower                                                  |
| async_tree_none_tg               | 198 ms                                                     | 216 ms: 1.09x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 78.2 ms: 1.09x slower                                                 |
| pathlib                          | 23.3 ms                                                    | 26.5 ms: 1.13x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 407 ms: 1.14x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 378 ms: 1.14x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 274 ms: 1.14x slower                                                  |
| json_loads                       | 16.8 us                                                    | 19.4 us: 1.15x slower                                                 |
| async_tree_memoization           | 260 ms                                                     | 300 ms: 1.16x slower                                                  |
| async_tree_none                  | 209 ms                                                     | 243 ms: 1.16x slower                                                  |
| json                             | 2.93 ms                                                    | 3.42 ms: 1.17x slower                                                 |
| async_generators                 | 281 ms                                                     | 336 ms: 1.19x slower                                                  |
| bench_mp_pool                    | 47.2 ms                                                    | 56.7 ms: 1.20x slower                                                 |
| mdp                              | 1.53 sec                                                   | 1.87 sec: 1.22x slower                                                |
| docutils                         | 1.44 sec                                                   | 1.79 sec: 1.25x slower                                                |
| deepcopy                         | 204 us                                                     | 256 us: 1.26x slower                                                  |
| async_tree_eager_memoization     | 152 ms                                                     | 192 ms: 1.26x slower                                                  |
| coverage                         | 45.0 ms                                                    | 56.8 ms: 1.26x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 19.2 ms: 1.27x slower                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 15.6 ms: 1.27x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 89.9 ms: 1.28x slower                                                 |
| telco                            | 4.60 ms                                                    | 5.99 ms: 1.30x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 8.12 ms: 1.30x slower                                                 |
| pylint                           | 170 ms                                                     | 224 ms: 1.32x slower                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 167 ms: 1.33x slower                                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 4.08 sec: 1.34x slower                                                |
| xml_etree_generate               | 52.7 ms                                                    | 71.9 ms: 1.37x slower                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 2.57 us: 1.41x slower                                                 |
| tomli_loads                      | 1.47 sec                                                   | 2.07 sec: 1.42x slower                                                |
| deepcopy_memo                    | 22.6 us                                                    | 32.4 us: 1.43x slower                                                 |
| fannkuch                         | 248 ms                                                     | 358 ms: 1.44x slower                                                  |
| nqueens                          | 52.2 ms                                                    | 78.7 ms: 1.51x slower                                                 |
| pycparser                        | 632 ms                                                     | 961 ms: 1.52x slower                                                  |
| pyflate                          | 321 ms                                                     | 489 ms: 1.52x slower                                                  |
| dulwich_log                      | 27.6 ms                                                    | 42.1 ms: 1.53x slower                                                 |
| generators                       | 22.9 ms                                                    | 35.3 ms: 1.54x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 279 ms: 1.54x slower                                                  |
| sympy_integrate                  | 10.3 ms                                                    | 16.0 ms: 1.55x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 4.32 ms: 1.56x slower                                                 |
| 2to3                             | 161 ms                                                     | 254 ms: 1.58x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 78.9 ms: 1.59x slower                                                 |
| xml_etree_process                | 37.1 ms                                                    | 59.8 ms: 1.61x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 26.0 ms: 1.64x slower                                                 |
| thrift                           | 435 us                                                     | 716 us: 1.65x slower                                                  |
| tornado_http                     | 66.7 ms                                                    | 110 ms: 1.66x slower                                                  |
| html5lib                         | 31.2 ms                                                    | 52.3 ms: 1.68x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 151 us: 1.72x slower                                                  |
| genshi_xml                       | 29.9 ms                                                    | 51.6 ms: 1.72x slower                                                 |
| scimark_sor                      | 94.9 ms                                                    | 167 ms: 1.76x slower                                                  |
| sqlglot_optimize                 | 30.9 ms                                                    | 55.0 ms: 1.78x slower                                                 |
| sympy_str                        | 131 ms                                                     | 236 ms: 1.80x slower                                                  |
| bench_thread_pool                | 447 us                                                     | 810 us: 1.81x slower                                                  |
| regex_compile                    | 68.5 ms                                                    | 125 ms: 1.83x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 111 ms: 1.84x slower                                                  |
| pprint_pformat                   | 947 ms                                                     | 1.74 sec: 1.84x slower                                                |
| richards                         | 31.8 ms                                                    | 58.8 ms: 1.85x slower                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 859 ms: 1.85x slower                                                  |
| go                               | 101 ms                                                     | 186 ms: 1.85x slower                                                  |
| genshi_text                      | 13.9 ms                                                    | 25.8 ms: 1.86x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 19.3 us: 1.90x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 78.6 ms: 1.90x slower                                                 |
| richards_super                   | 35.2 ms                                                    | 68.3 ms: 1.94x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 438 ms: 1.94x slower                                                  |
| scimark_monte_carlo              | 42.5 ms                                                    | 82.6 ms: 1.95x slower                                                 |
| django_template                  | 19.4 ms                                                    | 37.9 ms: 1.95x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 7.94 ms: 1.96x slower                                                 |
| mako                             | 6.99 ms                                                    | 13.7 ms: 1.97x slower                                                 |
| unpickle_pure_python             | 141 us                                                     | 280 us: 1.99x slower                                                  |
| spectral_norm                    | 66.4 ms                                                    | 134 ms: 2.02x slower                                                  |
| float                            | 48.6 ms                                                    | 98.7 ms: 2.03x slower                                                 |
| pickle_pure_python               | 179 us                                                     | 365 us: 2.04x slower                                                  |
| sympy_sum                        | 69.2 ms                                                    | 142 ms: 2.04x slower                                                  |
| logging_simple                   | 3.04 us                                                    | 6.34 us: 2.08x slower                                                 |
| logging_format                   | 3.31 us                                                    | 6.92 us: 2.09x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 1.97 ms: 2.21x slower                                                 |
| chaos                            | 34.0 ms                                                    | 78.5 ms: 2.31x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 1.72 ms: 2.35x slower                                                 |
| scimark_lu                       | 66.9 ms                                                    | 158 ms: 2.37x slower                                                  |
| logging_silent                   | 60.1 ns                                                    | 143 ns: 2.37x slower                                                  |
| raytrace                         | 147 ms                                                     | 390 ms: 2.65x slower                                                  |
| nbody                            | 59.6 ms                                                    | 159 ms: 2.67x slower                                                  |
| deltablue                        | 2.14 ms                                                    | 5.96 ms: 2.79x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.45x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.29x
- 95% likely to have a slowdown of 1.27x
- 99% likely to have a slowdown of 1.24x

# Memory
- memory change: 0.63x
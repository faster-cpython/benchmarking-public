# Results vs. 3.13.0b2

- fork: python
- ref: 342e654b8eda24c68da6
- machine: darwin-arm64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.37x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x slower
- Memory change: 0.78x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 246 ms: 1.53x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.75 sec: 1.22x slower                                                |
| html5lib       | 31.2 ms                                                    | 51.2 ms: 1.64x slower                                                 |
| tornado_http   | 66.7 ms                                                    | 127 ms: 1.90x slower                                                  |
| Geometric mean | (ref)                                                      | 1.55x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io_tg           | 768 ms                                                     | 464 ms: 1.66x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 484 ms: 1.58x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 499 ms: 1.13x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 525 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 460 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 485 ms: 1.04x slower                                                  |
| async_tree_none_tg               | 198 ms                                                     | 206 ms: 1.04x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 263 ms: 1.10x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 395 ms: 1.10x slower                                                  |
| async_tree_memoization           | 260 ms                                                     | 288 ms: 1.11x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 367 ms: 1.11x slower                                                  |
| async_tree_none                  | 209 ms                                                     | 233 ms: 1.11x slower                                                  |
| async_tree_eager_memoization     | 152 ms                                                     | 184 ms: 1.21x slower                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 159 ms: 1.27x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 106 ms: 1.76x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 74.9 ms: 1.81x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.07x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| float          | 48.6 ms                                                    | 93.8 ms: 1.93x slower                                                 |
| nbody          | 59.6 ms                                                    | 154 ms: 2.58x slower                                                  |
| Geometric mean | (ref)                                                      | 1.71x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 149 ms                                                     | 139 ms: 1.08x faster                                                  |
| regex_effbot   | 2.58 ms                                                    | 2.44 ms: 1.06x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 17.1 ms: 1.01x faster                                                 |
| regex_compile  | 68.5 ms                                                    | 119 ms: 1.74x slower                                                  |
| Geometric mean | (ref)                                                      | 1.11x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle               | 7.48 us                                                    | 7.05 us: 1.06x faster                                                 |
| pickle_list          | 2.96 us                                                    | 2.90 us: 1.02x faster                                                 |
| xml_etree_parse      | 106 ms                                                     | 104 ms: 1.01x faster                                                  |
| pickle_dict          | 18.3 us                                                    | 18.4 us: 1.01x slower                                                 |
| xml_etree_iterparse  | 71.5 ms                                                    | 75.6 ms: 1.06x slower                                                 |
| unpickle             | 9.12 us                                                    | 9.72 us: 1.07x slower                                                 |
| json_loads           | 16.8 us                                                    | 18.8 us: 1.11x slower                                                 |
| unpickle_list        | 2.88 us                                                    | 3.25 us: 1.13x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 7.74 ms: 1.24x slower                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 68.1 ms: 1.29x slower                                                 |
| tomli_loads          | 1.47 sec                                                   | 1.99 sec: 1.36x slower                                                |
| xml_etree_process    | 37.1 ms                                                    | 57.2 ms: 1.54x slower                                                 |
| unpickle_pure_python | 141 us                                                     | 262 us: 1.87x slower                                                  |
| pickle_pure_python   | 179 us                                                     | 346 us: 1.94x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.22x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 13.6 ms: 1.10x slower                                                 |
| python_startup         | 15.2 ms                                                    | 17.0 ms: 1.12x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.11x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 29.9 ms                                                    | 49.6 ms: 1.66x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 24.9 ms: 1.79x slower                                                 |
| django_template | 19.4 ms                                                    | 35.3 ms: 1.82x slower                                                 |
| mako            | 6.99 ms                                                    | 13.3 ms: 1.91x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.79x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io_tg           | 768 ms                                                     | 464 ms: 1.66x faster                                                  |
| sqlglot_normalize                | 166 ms                                                     | 102 ms: 1.62x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 484 ms: 1.58x faster                                                  |
| create_gc_cycles                 | 897 us                                                     | 686 us: 1.31x faster                                                  |
| asyncio_tcp                      | 402 ms                                                     | 335 ms: 1.20x faster                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.05 ms: 1.20x faster                                                 |
| async_tree_io_tg                 | 565 ms                                                     | 499 ms: 1.13x faster                                                  |
| regex_dna                        | 149 ms                                                     | 139 ms: 1.08x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 525 ms: 1.07x faster                                                  |
| pickle                           | 7.48 us                                                    | 7.05 us: 1.06x faster                                                 |
| regex_effbot                     | 2.58 ms                                                    | 2.44 ms: 1.06x faster                                                 |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.24 sec: 1.04x faster                                                |
| pickle_list                      | 2.96 us                                                    | 2.90 us: 1.02x faster                                                 |
| xml_etree_parse                  | 106 ms                                                     | 104 ms: 1.01x faster                                                  |
| sqlite_synth                     | 1.55 us                                                    | 1.53 us: 1.01x faster                                                 |
| asyncio_websockets               | 409 ms                                                     | 405 ms: 1.01x faster                                                  |
| regex_v8                         | 17.3 ms                                                    | 17.1 ms: 1.01x faster                                                 |
| pidigits                         | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| pickle_dict                      | 18.3 us                                                    | 18.4 us: 1.01x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 460 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 485 ms: 1.04x slower                                                  |
| async_tree_none_tg               | 198 ms                                                     | 206 ms: 1.04x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 75.6 ms: 1.06x slower                                                 |
| unpickle                         | 9.12 us                                                    | 9.72 us: 1.07x slower                                                 |
| pathlib                          | 23.3 ms                                                    | 25.6 ms: 1.10x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 263 ms: 1.10x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 395 ms: 1.10x slower                                                  |
| python_startup_no_site           | 12.3 ms                                                    | 13.6 ms: 1.10x slower                                                 |
| async_tree_memoization           | 260 ms                                                     | 288 ms: 1.11x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 367 ms: 1.11x slower                                                  |
| async_tree_none                  | 209 ms                                                     | 233 ms: 1.11x slower                                                  |
| json_loads                       | 16.8 us                                                    | 18.8 us: 1.11x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 17.0 ms: 1.12x slower                                                 |
| unpickle_list                    | 2.88 us                                                    | 3.25 us: 1.13x slower                                                 |
| json                             | 2.93 ms                                                    | 3.35 ms: 1.14x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 54.9 ms: 1.16x slower                                                 |
| async_generators                 | 281 ms                                                     | 331 ms: 1.18x slower                                                  |
| mdp                              | 1.53 sec                                                   | 1.83 sec: 1.19x slower                                                |
| deepcopy                         | 204 us                                                     | 245 us: 1.20x slower                                                  |
| async_tree_eager_memoization     | 152 ms                                                     | 184 ms: 1.21x slower                                                  |
| docutils                         | 1.44 sec                                                   | 1.75 sec: 1.22x slower                                                |
| coverage                         | 45.0 ms                                                    | 55.6 ms: 1.24x slower                                                 |
| telco                            | 4.60 ms                                                    | 5.69 ms: 1.24x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 7.74 ms: 1.24x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 88.7 ms: 1.26x slower                                                 |
| pylint                           | 170 ms                                                     | 215 ms: 1.27x slower                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 159 ms: 1.27x slower                                                  |
| xml_etree_generate               | 52.7 ms                                                    | 68.1 ms: 1.29x slower                                                 |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.95 sec: 1.30x slower                                                |
| deepcopy_reduce                  | 1.82 us                                                    | 2.46 us: 1.35x slower                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.99 sec: 1.36x slower                                                |
| deepcopy_memo                    | 22.6 us                                                    | 31.2 us: 1.38x slower                                                 |
| fannkuch                         | 248 ms                                                     | 352 ms: 1.42x slower                                                  |
| pycparser                        | 632 ms                                                     | 913 ms: 1.44x slower                                                  |
| nqueens                          | 52.2 ms                                                    | 75.5 ms: 1.45x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 263 ms: 1.46x slower                                                  |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 4.06 ms: 1.46x slower                                                 |
| dulwich_log                      | 27.6 ms                                                    | 40.7 ms: 1.48x slower                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 15.4 ms: 1.49x slower                                                 |
| pyflate                          | 321 ms                                                     | 479 ms: 1.49x slower                                                  |
| generators                       | 22.9 ms                                                    | 34.6 ms: 1.51x slower                                                 |
| 2to3                             | 161 ms                                                     | 246 ms: 1.53x slower                                                  |
| xml_etree_process                | 37.1 ms                                                    | 57.2 ms: 1.54x slower                                                 |
| thrift                           | 435 us                                                     | 679 us: 1.56x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 77.4 ms: 1.56x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 25.0 ms: 1.58x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 142 us: 1.62x slower                                                  |
| html5lib                         | 31.2 ms                                                    | 51.2 ms: 1.64x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 50.9 ms: 1.65x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 49.6 ms: 1.66x slower                                                 |
| sympy_str                        | 131 ms                                                     | 227 ms: 1.73x slower                                                  |
| pprint_pformat                   | 947 ms                                                     | 1.64 sec: 1.74x slower                                                |
| scimark_sor                      | 94.9 ms                                                    | 165 ms: 1.74x slower                                                  |
| pprint_safe_repr                 | 465 ms                                                     | 808 ms: 1.74x slower                                                  |
| regex_compile                    | 68.5 ms                                                    | 119 ms: 1.74x slower                                                  |
| richards                         | 31.8 ms                                                    | 55.6 ms: 1.75x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 106 ms: 1.76x slower                                                  |
| bench_thread_pool                | 447 us                                                     | 792 us: 1.77x slower                                                  |
| spectral_norm                    | 66.4 ms                                                    | 118 ms: 1.78x slower                                                  |
| genshi_text                      | 13.9 ms                                                    | 24.9 ms: 1.79x slower                                                 |
| go                               | 101 ms                                                     | 181 ms: 1.80x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 74.9 ms: 1.81x slower                                                 |
| django_template                  | 19.4 ms                                                    | 35.3 ms: 1.82x slower                                                 |
| richards_super                   | 35.2 ms                                                    | 64.3 ms: 1.83x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 78.1 ms: 1.84x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 18.7 us: 1.84x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 421 ms: 1.86x slower                                                  |
| unpickle_pure_python             | 141 us                                                     | 262 us: 1.87x slower                                                  |
| hexiom                           | 4.06 ms                                                    | 7.63 ms: 1.88x slower                                                 |
| tornado_http                     | 66.7 ms                                                    | 127 ms: 1.90x slower                                                  |
| mako                             | 6.99 ms                                                    | 13.3 ms: 1.91x slower                                                 |
| float                            | 48.6 ms                                                    | 93.8 ms: 1.93x slower                                                 |
| pickle_pure_python               | 179 us                                                     | 346 us: 1.94x slower                                                  |
| sympy_sum                        | 69.2 ms                                                    | 137 ms: 1.98x slower                                                  |
| logging_simple                   | 3.04 us                                                    | 6.05 us: 1.99x slower                                                 |
| logging_format                   | 3.31 us                                                    | 6.60 us: 1.99x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 1.88 ms: 2.11x slower                                                 |
| scimark_lu                       | 66.9 ms                                                    | 144 ms: 2.15x slower                                                  |
| chaos                            | 34.0 ms                                                    | 74.2 ms: 2.18x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 1.64 ms: 2.24x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 135 ns: 2.25x slower                                                  |
| raytrace                         | 147 ms                                                     | 373 ms: 2.54x slower                                                  |
| nbody                            | 59.6 ms                                                    | 154 ms: 2.58x slower                                                  |
| deltablue                        | 2.14 ms                                                    | 5.63 ms: 2.63x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.37x slower                                                          |
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240920-3.14.0a0-342e654-NOGIL/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.25x
- 95% likely to have a slowdown of 1.23x
- 99% likely to have a slowdown of 1.20x

# Memory
- memory change: 0.78x